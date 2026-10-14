# Prepare the Kubernetes nodes

Do every step of this page on **each** manager node and **each** worker node. A standard cluster has 3 manager nodes and at least 3 worker nodes.

Hardware sizes are in [Technical requirements](../deployment/deployment_prerequisites.md#compute-node-specification). This page explains how to prepare the operating system.

## Rules

### Hardware and firmware

- The node **MUST** have 44 logical CPUs or more. On a physical server, **enable Hyper-Threading (SMT)** in the BIOS/UEFI: the SHC counts logical CPUs, not physical cores.
- The node **MUST** have 120 GiB of RAM or more, as seen by Linux (`free -g`). A server with 128 GB of RAM can show less if the firmware reserves memory.
- The node **MUST** have one **data disk** of 200 GB or more, used for nothing else (4 TB per worker node for a production deployment). Ceph uses this disk. One data disk per node is enough.
- If the server has a RAID controller, the data disk **SHOULD** be in **HBA / JBOD / passthrough** mode, not inside a RAID volume.
- The node **MUST** have a separate **system disk** for the operating system. It **SHOULD** have **400 GB** or more. See [System disk](#system-disk).

### Operating system

- The node **MUST** run **Debian 12 or Debian 13**, 64-bit (amd64).
- The node **MUST NOT** run a desktop environment or a web server. Ports 80 and 443 must stay free.
- The hostname **MUST** be unique in the cluster. It **SHOULD** contain only lowercase letters, digits and `-`. Example: `sh-mgr-1`, `sh-worker-1`.
- The node **MUST** have a fixed **IPv4** address. The IP addresses are written in `config.yml` and must never change. IPv6 is not supported.
- **Swap MUST be disabled**, also after a reboot. See [Step 5: Disable swap](#step-5-disable-swap).
- `apt` **MUST** work on the node: `sudo apt-get update` finishes without errors. The SHC installs packages with `apt` during the installation.
- These packages **MUST** be installed: `python3`, `sudo`, `openssh-server`, `lvm2`, `gettext-base`.
- A time service **MUST** be installed: `chrony` (recommended) or `systemd-timesyncd`.
- The clock **MUST** be synchronized with NTP. See [Prepare DNS, time, email and certificates](./dns_time_certificates.md#time-ntp).

### User account

- The same Linux user (`<ADMIN_USER>`) **MUST** exist on every node.
- `<ADMIN_USER>` **MUST** accept SSH connections with a key, on **port 22**.
- `<ADMIN_USER>` **SHOULD** run `sudo` **without a password**.

### If you do not follow a SHOULD rule

| SHOULD rule not followed | What you must change |
| :--- | :--- |
| `sudo` asks for a password | In `env.rc`, set `export SERVERS_SUDO_PASSWORD='<password>'`. The script `run-shc.sh` already passes this variable to the SHC. The same password is also used if SSH asks for a password. |
| The hostname contains uppercase letters | No configuration change. No problem is known, but this case is not tested. |
| The system disk is smaller than 400 GB | No configuration change. Watch the free space of `/var` closely: when it is full, the installation stops (`DiskPressure`). |
| The data disk is inside a RAID volume | No configuration change exists. Storage performance and failure handling are not validated: contact Sekoia. |

### Not supported

| Situation | Result |
| :--- | :--- |
| SSH on a port other than 22 | Not supported in this release. |
| SSH key with a passphrase | Not supported in this release. |
| `su` instead of `sudo` | Not supported in this release. |
| Access to the nodes through a jump host (bastion) | Not supported in this release: the orchestration node must reach every node directly. |
| SSH with a password only, without a key | Not supported: the SHC requires a key. |
| A different Linux user on some nodes | Not supported. |
| `doas` instead of `sudo` | Not supported. |
| IPv6 addresses | Not supported. |

<!-- SH-ISSUE #96028: review this passage when the issue is released -->

## Step 1: Install Debian

=== "Debian installer (ISO)"

    **Validation status:** reference procedure. The Sekoia lab uses Debian 13 cloud images instead of the installer.

    Download the official Debian 12 or 13 **netinst** ISO for amd64 from `https://www.debian.org/distrib/`. Start the server on it, choose **Install** or **Graphical install**, then answer the screens as follows.

    | Installer screen | What to choose | Why |
    | :--- | :--- | :--- |
    | Root password | **Leave it empty.** Press Enter twice. | With an empty root password, Debian installs `sudo` and gives `sudo` rights to the user you create next. |
    | Full name / user name | `<ADMIN_USER>`, the **same name on every node**. | The SHC connects with this user. |
    | Hostname | A unique name: lowercase letters, digits and `-` only. | Kubernetes identifies nodes by hostname. |
    | Domain name | Your domain, or empty. | |
    | Network | A **static** IP address, the gateway, and **your DNS servers**. | The IP address is written in `config.yml`. |
    | Partitioning | Select the **system disk only**. See [System disk](#system-disk). **Never select the data disk.** | A data disk with a partition or a filesystem is rejected by the SHC. |
    | Debian archive mirror | Your company mirror, or a public mirror if the node has internet access. | The SHC installs packages with `apt`. |
    | HTTP proxy | Your proxy, if the node needs one to reach the mirror. | |
    | Software selection | **Uncheck** "Debian desktop environment" and every desktop. **Uncheck** "web server". **Check** "SSH server" and "standard system utilities". | A web server uses ports 80 and 443. Without SSH, the SHC cannot connect. |

    !!! tip "How to recognize the disks"
        The installer shows each disk with its size and model. Before the installation, write down the **size and serial number** of the system disk and of the data disk. Choose the system disk by its size and model, not by its name (`sda`, `nvme0n1`): names can change.

=== "Cloud image"

    **Validation status:** validated in the Sekoia lab (Debian 13 cloud image on OpenStack).

    Create the virtual machine from the official Debian 12 or 13 cloud image. Attach the data disk as a **separate, empty volume**. Use cloud-init to create `<ADMIN_USER>` with your SSH public key and passwordless `sudo`:

    ```yaml
    #cloud-config
    system_info:
      default_user:
        name: <ADMIN_USER>
        lock_passwd: true
        groups: [adm, sudo]
        sudo: ["ALL=(ALL) NOPASSWD:ALL"]
        shell: /bin/bash
    ```

## Step 2: Check the package sources

Log in to the node as `<ADMIN_USER>`.

1. Search for a CD-ROM source. An installation from an ISO image often leaves one:

    ```bash
    grep -rn "cdrom" /etc/apt/sources.list /etc/apt/sources.list.d/
    ```

    If the command prints a line, open the file and put `#` at the start of each `cdrom` line:

    ```bash
    sudo nano /etc/apt/sources.list
    ```

2. If the node reaches the mirror through a proxy, create the proxy file. Replace the URL with your proxy:

    ```bash
    echo 'Acquire::http::Proxy "http://<PROXY_HOST>:<PROXY_PORT>";' | sudo tee /etc/apt/apt.conf.d/99proxy
    ```

3. Update the package list:

    ```bash
    sudo apt-get update
    ```

    **Expected result:** the command ends without any line that starts with `E:` or `Err:`.

!!! warning "Air-gapped sites"
    If the node cannot reach any Debian mirror, `apt` fails during the installation. You **MUST** provide an internal Debian mirror, or install every package of [Step 3](#step-3-install-the-packages) before the installation.

## Step 3: Install the packages

1. Install the mandatory packages:

    ```bash
    sudo apt-get install -y python3 sudo openssh-server lvm2 gettext-base
    ```

2. Install the time service:

    ```bash
    sudo apt-get install -y chrony
    ```

3. Install the tools used in the troubleshooting pages:

    ```bash
    sudo apt-get install -y curl tar jq dnsutils tcpdump
    ```

4. Check the installation:

    ```bash
    python3 --version
    ```

    **Expected result:** `Python 3.11.x` (Debian 12) or `Python 3.13.x` (Debian 13).

## Step 4: Configure sudo

Skip this step if you used the cloud image tab in Step 1.

1. Allow `<ADMIN_USER>` to run `sudo` without a password:

    ```bash
    echo "<ADMIN_USER> ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/<ADMIN_USER>
    ```

2. Protect the file:

    ```bash
    sudo chmod 440 /etc/sudoers.d/<ADMIN_USER>
    ```

3. Check:

    ```bash
    sudo -n true && echo SUDO-OK
    ```

    **Expected result:** `SUDO-OK`.

The SSH key of the orchestration node is authorized in [Prepare the orchestration node](./orchestration_node.md#step-4-authorize-the-ssh-key-on-every-node).

## Step 5: Disable swap

Swap **MUST** be disabled on every node, also after a reboot. Sekoia does not support Kubernetes with swap.

<!-- SH-ISSUE #96032: review this passage when the issue is released -->

1. Stop the swap now:

    ```bash
    sudo swapoff -a
    ```

2. Disable the swap lines of `/etc/fstab`, so that swap does not come back after a reboot. This command puts `#` at the start of every line that contains `swap`:

    ```bash
    sudo sed -i '/\sswap\s/ s/^\([^#]\)/#\1/' /etc/fstab
    ```

3. Reboot the node:

    ```bash
    sudo reboot
    ```

4. Check, after the reboot:

    ```bash
    /sbin/swapon --show=NAME --noheadings --raw
    ```

    **Expected result:** nothing. If a line is printed, a swap file, a systemd swap unit or a `zram` service is still active: disable it, then reboot and check again.

!!! note "IPv6"
    The platform is installed in IPv4 only. You do not need to disable IPv6 in the operating system. The Sekoia lab disables it on every node, with `net.ipv6.conf.all.disable_ipv6 = 1` in `/etc/sysctl.d/`; this is not a requirement.

## System disk

The system disk holds the operating system **and** the Kubernetes data: container images, etcd, kubelet and Ceph monitor data. These directories are all under `/var`. If `/var` is too small, the installation stops in the middle with `DiskPressure` or Ceph `MON_DISK_LOW` errors.

- The system disk **MUST NOT** use a separate small `/var` partition (for example the installer option "separate /home, /var and /tmp partitions").
- The system disk **SHOULD** follow one of the two layouts below.

=== "One root partition (simple)"

    **Validation status:** validated in the Sekoia lab, with a 400 GB system disk, one root partition, no swap, and the `sizing/minimal.yaml` profile.

    - System disk of **400 GB or more**. Sekoia plans 200 GB for the containers, 100 GB for the logs and 100 GB for the system.
    - In the Debian installer: **Guided - use entire disk**, then **All files in one partition**.
    - The installer also creates a swap partition. Disable it after the installation: see [Step 5: Disable swap](#step-5-disable-swap).

=== "LVM layout (hardened)"

    **Validation status:** validated in the Sekoia lab with these volume sizes. In the lab, `/` and `/boot` stay on a separate root disk: the `lv-root` row and the 1 GB `/boot` partition are the values planned for a physical server.

    Use this layout when your security policy requires one partition per system directory. It is larger than the 400 GB minimum: it keeps free space to grow the volumes. Create a volume group named `vg-os` on the system disk (about **700 GB**) and these logical volumes, with an `ext4` filesystem, in the Debian installer (**Manual** partitioning) or after the installation.

    | Logical volume | Mount point | Manager node | Worker node |
    | :--- | :--- | :---: | :---: |
    | `lv-root` | `/` | 24 GB | 24 GB |
    | `lv-usr` | `/usr` | 24 GB | 24 GB |
    | `lv-home` | `/home` | 4 GB | 4 GB |
    | `lv-opt` | `/opt` | 25 GB | 25 GB |
    | `lv-tmp` | `/tmp` | 22 GB | 22 GB |
    | `lv-var` | `/var` | 20 GB | 20 GB |
    | `lv-vartmp` | `/var/tmp` | 22 GB | 22 GB |
    | `lv-varlog` | `/var/log` | 25 GB | 25 GB |
    | `lv-varlogaudit` | `/var/log/audit` | 3 GB | 3 GB |
    | `lv-varlibrancher` | `/var/lib/rancher` | 300 GB | 300 GB |
    | `lv-etcd` | `/var/lib/rancher/k3s/server/db` | 30 GB | none |
    | `lv-varlibkubelet` | `/var/lib/kubelet` | 50 GB | 50 GB |
    | `lv-varlibrook` | `/var/lib/rook` | 30 GB | 5 GB |

    `/boot` stays a normal partition of 1 GB. Leave the rest of `vg-os` **free**: you can grow a volume later with `sudo lvextend -r -L +50G /dev/vg-os/<volume>`, without stopping the node.

    !!! warning "Reset or destroy the platform"
        With a separate `/var/lib/rook` volume, `PlatformDestroy` stops before it wipes the storage. Contact Sekoia before you reset a platform installed with this layout.

## Data disk

1. List the disks:

    ```bash
    lsblk -o NAME,SIZE,TYPE,FSTYPE,MODEL,SERIAL,MOUNTPOINTS
    ```

2. Find the data disk by its **size and serial number**.

    **Expected result:** the data disk line has an empty `FSTYPE` column, an empty `MOUNTPOINTS` column, and **no lines under it** (no partitions).

3. If the data disk was used before, it can still carry a partition table or a filesystem. Erase it. **This command destroys all data on the disk.** Check the disk name three times before you run it:

    ```bash
    sudo wipefs -a /dev/<DATA_DISK>
    ```

    Then run step 1 again.

## Final check

Run these commands on each node and compare with the expected result.

| Command | Expected result |
| :--- | :--- |
| `hostname` | The unique name of the node. |
| `/sbin/swapon --show=NAME --noheadings --raw` | **Nothing** (swap disabled). |
| `nproc` | `44` or more. |
| `free -g` | `total` of the `Mem:` line: `120` or more. |
| `df -h /var/lib/rancher` | Simple layout: the `Avail` column of `/` shows most of the system disk. LVM layout: the line shows `vg--os-lv--varlibrancher`. |
| `python3 --version` | `Python 3.x`. |
| `sudo -n true && echo SUDO-OK` | `SUDO-OK`. |
| `timedatectl show -p NTPSynchronized` | `NTPSynchronized=yes` (see [Time](./dns_time_certificates.md#time-ntp)). |
| `lsblk -o NAME,SIZE,FSTYPE` | The data disk has no `FSTYPE` and no partition. |

Then check that the ports that Kubernetes needs are free:

```bash
sudo ss -tlnp | grep -E ':(80|443|2379|2380|4240|4250|6443|10514|11514|10901) '
```

**Expected result:** nothing. A line means that a program uses a port that Kubernetes needs: stop this program.

## Checklist

- [ ] Every node runs Debian 12 or 13, without a desktop and without a web server.
- [ ] Every hostname is unique and lowercase.
- [ ] Every node has a fixed IPv4 address.
- [ ] Swap is disabled on every node, also after a reboot.
- [ ] `sudo apt-get update` works on every node.
- [ ] `python3`, `sudo`, `openssh-server`, `lvm2`, `gettext-base` are installed on every node.
- [ ] `<ADMIN_USER>` exists on every node and runs `sudo` without a password (or you set `SERVERS_SUDO_PASSWORD`).
- [ ] Every node has an empty data disk of 200 GB or more.
- [ ] The system disk follows one of the two layouts.
- [ ] The final check passes on every node.
