# Technical requirements

This article lists all infrastructure, hardware, software, storage, and network requirements for a Sekoia Self-Hosted deployment. Verify every requirement before starting the installation.

## Infrastructure components

You must provision and manage the following components outside the Kubernetes cluster.

| Component | CPU | RAM | Storage / throughput | Notes |
| :--- | :---: | :---: | :---: | :--- |
| TCP Load Balancer (e.g., HAProxy, Nginx) | 4 | 8 GB | 100 Mbps (12.5 MB/s) | Required minimum throughput. Scale according to your actual ingest volume. Layer 4 only: Traefik terminates TLS. See [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md#flows-from-load-balancers-to-kubernetes-nodes). |
| Orchestration node | 4 | 8 GB | 200 GB | Required. Runs the self-hosted-controller (SHC). See requirements below. |
| Local image registry (e.g., Harbor, JFrog, Nexus) | 4 | 8 GB | 1 TB | Required. The SHC publishes the images and Helm charts to it, and the Kubernetes nodes pull them from it. Must serve HTTPS, with token (Bearer) authentication. See [OCI registry](/self_hosted/1.0.1/deployment/deployment_configuration.md#oci-registry). |
| Local code registry (e.g., GitLab, Gitea, ForgeJo) | 1 | 4 GB | Less than 10 GB | Required. The SHC publishes the ArgoCD stack manifests to it, and ArgoCD reads them from it. Must be reached over HTTP or HTTPS, with a username and a password. See [Git repository](/self_hosted/1.0.1/deployment/deployment_configuration.md#git-repository). |
| S3-compatible object storage | | | See [Storage](#storage) | Required. Stores the indexed events. |

### Orchestration node requirements

The orchestration node only requires Docker to run the SHC container image. It does not require Python or Ansible to be installed directly on the host.

!!! note "Orchestration node role"
    The orchestration node does not join the Kubernetes cluster. The SHC performs preflight checks, installs the complete Kubernetes cluster, manages the platform deployment through Helm and ArgoCD, and downloads deployment resources when internet access is available. The node must have SSH access to all Kubernetes nodes on TCP port 22.

## Compute node specification

Every Kubernetes node, manager or worker, must meet the following minimum hardware requirements. `CheckServerSpec` applies the same checks to both roles.

| Resource | Minimum requirement | Enforced by `CheckServerSpec` |
| :--- | :--- | :--- |
| CPU | 44 vCPUs at 3.2 GHz minimum | 44 logical CPUs |
| RAM | 128 GB | 120 GiB |
| Dedicated storage disk | One unused SSD of 200 GB or more; 4 TB per worker node for deployments handling data | 200 GB |
| System disk | 400 GB recommended, separate from the dedicated storage disk | Not checked |
| Operating system | Debian 12 (Bookworm) or Debian 13 (Trixie), amd64 | Debian 12 or later |
| Swap | Disabled, including after a reboot | No active swap device |
| Hostname | Unique across all manager and worker nodes | Uniqueness |
| Time synchronization | NTP enabled and clock synchronized | Both |
| Free ports | TCP 80, 443, 2379, 2380, 4240, 4250, 6443, 10514, and 11514 not bound by another process | All nine ports, before K3s is installed |
| SSH account | Key-based SSH access and full sudo privileges. See [SSH account](#ssh-account). | Not checked. `CheckServersAreReachable` fails when the connection or the privilege escalation fails. |
| Python 3 | `python3` installed, in online and air-gapped mode alike. See [Operating system packages](#operating-system-packages). | Not checked. Every Ansible playbook, `CheckServerSpec` included, fails on a node without it. |

The `CheckServerSpec` command blocks the installation when a manager or worker node fails any of the checks in the last column. See [CheckServerSpec](/self_hosted/1.0.1/troubleshooting/debug_tool.md#checkserverspec) for the failure messages and their remediation.

`CheckServerSpec` counts the logical CPUs that Linux reports. On a physical server, enable simultaneous multithreading (Hyper-Threading) in the firmware to expose every logical CPU.

The system disk holds the operating system and the Kubernetes data under `/var`: container images, etcd, kubelet, and Ceph monitor data. Do not give `/var` a small separate partition. When `/var` fills up, Kubernetes reports `DiskPressure`, and the installation stops.

!!! warning "SSD usage"
    `CheckServerSpec` enforces a 200 GB dedicated-disk minimum to support ultra-tight deployments. Any deployment that handles customer data must provision 4 TB per worker node. How quickly that capacity is consumed depends on the customer's use of the platform. Do not use these disks for long-term event retention; event data requires dedicated S3-compatible storage (see [Storage](#storage) below).

### Dedicated storage disk

Ceph provisions persistent volumes from a dedicated block device on every node. Each manager and worker node must expose at least one whole disk that meets all of the following conditions:

- 200 GB or larger.
- No partition table and no filesystem.
- Not read-only.

Attach the disk and leave it unformatted before you start the installation. `CheckServerSpec` skips this check once K3s is installed, because Ceph has consumed the disk by then. On a server with a RAID controller, expose the disk in HBA, JBOD, or passthrough mode: Sekoia does not validate Ceph on a RAID volume.

By default, Ceph uses every unused raw disk of every node. To use only the disks or the LVM logical volumes that you select, set the manual Ceph storage mode: `CheckServerSpec` then checks the selected devices instead. See [Ceph storage devices](/self_hosted/1.0.1/deployment/deployment_configuration.md#ceph-storage-devices).

!!! warning "Do not partition or format the storage disk"
    A disk that already carries a filesystem or a partition table is not counted as eligible. If the node exposes no other eligible disk, the preflight fails and the installation does not start.

### SSH account

The SHC configures every manager and worker node over SSH, as the user set in `utils.ansible.user`, with the private key set in `utils.ansible.ssh-key`. It runs every Ansible playbook with privilege escalation, so the account needs full `sudo` privileges on every node. Grant them in one of two ways:

- Passwordless sudo, with a `NOPASSWD` rule for the account.
- Sudo with a password, passed to the SHC in the `SERVERS_SUDO_PASSWORD` environment variable. See [Create the execution script](/self_hosted/1.0.1/deployment/deployment_guide.md#step-4-create-the-execution-script).

The SHC also offers the value of `SERVERS_SUDO_PASSWORD` as the SSH password of the account. Keep the two passwords identical if the account authenticates with a password instead of the key.

### Free ports

K3s, Traefik, etcd, Cilium, and the intake services bind TCP ports 80, 443, 2379, 2380, 4240, 4250, 6443, 10514, and 11514 on every node. `CheckServerSpec` fails when another process already listens on one of them. The check is skipped once K3s is installed, because the cluster then holds the ports itself. To identify the process that uses a port, run `sudo ss -ltnp 'sport = :<PORT>'` on the node. See [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md#kubernetes-internal-flows) for the flows on these ports.

### Node hostnames

Every manager and worker node must have a unique hostname. Kubernetes registers nodes by hostname, so two nodes sharing one hostname collapse into a single cluster member and lose their workloads.

To rename a node before the installation, run:

```bash
hostnamectl set-hostname <NEW_HOSTNAME>
```

### Node access

The SHC configures every manager and worker node over SSH, with Ansible. Each node must meet the following conditions:

- It has a fixed IPv4 address. The inventory of `config.yml` accepts IPv4 addresses only, and the platform is installed in IPv4 only.
- The same Linux account, set in `utils.ansible.user`, exists on every node.
- This account accepts SSH key authentication on TCP port 22, directly from the orchestration node.
- This account runs `sudo`. If `sudo` asks for a password, set it in `SERVERS_SUDO_PASSWORD`: the SHC also uses this password when the SSH server asks for one.

The following setups are not supported in Sekoia Self-Hosted 1.0.1:

| Setup | Status |
| :--- | :--- |
| SSH on a port other than 22 | Not supported: no setting changes the SSH port. |
| Access through a jump host (bastion) | Not supported: the orchestration node must reach every node directly. |
| SSH key protected by a passphrase | Not supported: the SHC cannot answer the passphrase prompt. |
| SSH with a password only | Not supported: the SHC requires an SSH key. |
| `su` or `doas` instead of `sudo` | Not supported. |
| A different account on some nodes | Not supported. |
| IPv6 addresses | Not supported. |

To check the access to a node from the orchestration node, run:

```bash
ssh -o BatchMode=yes <USER>@<NODE_IP> "sudo -n true && echo OK"
```

Expected output: `OK`. If you set `SERVERS_SUDO_PASSWORD`, `sudo -n` fails: run `sudo -v` in the SSH session instead.

### Swap

Swap must be disabled on every manager and worker node, including after a reboot: the Kubernetes nodes refuse to start with swap enabled. `CheckServerSpec` fails when a node has an active swap device.

To disable swap on a node:

1. Run `sudo swapoff -a`.
2. Remove or comment out the swap entries in `/etc/fstab`.
3. Disable any systemd swap unit or zram service that enables swap.
4. Reboot the node, then check that `/sbin/swapon --show=NAME --noheadings --raw` returns no entry.

### Operating system packages

The following packages are required on every compute node:

- `python3`: required by the SHC to run its checks and operations on the node. The SHC runs them with Ansible, which executes its modules with the Python interpreter of the node. The SHC never installs it, and `CheckServerSpec` reports the node as not checked when it is missing. The Debian installer includes `python3` with the standard system utilities, but check that a minimal installation provides it.
- `lvm2`: required for the K3s installation. The SHC installs it with `apt` on every node when it is missing. With manual Ceph storage, install it beforehand on every node that has a selected device: `CheckServerSpec` checks it before the SHC installs any package.
- `gettext-base`: required for the Helm installation. The SHC installs it with `apt` on the first manager node when it is missing.

Because the SHC may install packages, `apt` must work on every node: `sudo apt-get update` ends without errors.

!!! note "Air-gapped deployments"
    In air-gapped environments, nodes cannot download packages during the installation, so the SHC cannot install `lvm2` and `gettext-base` itself. Install the three packages on every compute node before you start, or provide an internal Debian mirror.

### Changes applied by the SHC to the nodes

The SHC does not install or harden the operating system of the nodes. During the `kubernetes` stage, `K3SInstall` and `HelmInstall` apply the following changes to the nodes. Review them against your hardening policy before the installation.

| Change | Nodes | Purpose |
| :--- | :--- | :--- |
| Installs the `lvm2` package with the system package manager, when it is missing | All | Required by Ceph to manage the dedicated storage disk. |
| Creates and enables the `lvm-vg-activate` systemd unit, which runs `vgchange -ay` at boot | All | Activates the Ceph LVM volume groups after a reboot, so that the Ceph OSDs find their disk. |
| Writes `/etc/sysctl.d/99-k3s-inotify.conf`: `fs.inotify.max_user_instances = 8192`, `fs.inotify.max_user_watches = 1048576`, `fs.inotify.max_queued_events = 65536` | All | Raises the inotify limits required by K3s and the platform containers. |
| Writes `/etc/sysctl.d/99-k3s-kafka.conf`: `vm.max_map_count = 262144` | All | Raises the memory map limit required by Kafka. |
| Installs the K3s binary and installation script in `/usr/local/bin` and `/srv`, the K3s images in `/var/lib/rancher/k3s/agent/images`, the registry mirrors in `/etc/rancher/k3s/registries.yaml`, and the `k3s` or `k3s-agent` systemd unit | All | Runs the Kubernetes control plane on the managers and the Kubernetes agent on the workers. |
| Installs the `gettext-base` package with the system package manager, when it is missing | First manager | Provides `envsubst`, used to render the Helm values of the cluster services. |
| Copies the Helm binary to `/usr/local/bin/helm` | First manager | Installs the cluster services (Cilium, CoreDNS, cert-manager, metrics-server) from the first manager node. |

The sysctl values are persistent and applied immediately. The installation does not change the bootloader, the host firewall configuration, the SSH configuration, or the user accounts of the nodes. The package installations reach the Debian repositories or your package mirror; see [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md#outbound-flows-to-infrastructure-services) for the flow.

### GPU nodes

The AI features of the platform, which run on GPU nodes, are not available in Sekoia Self-Hosted 1.0.1. Do not provision GPU nodes for this release. See the [release notes](/self_hosted/1.0.1/release_notes.md#ai-features).

## Cluster sizing

The following table provides estimated hardware footprints per deployment size.

!!! note "Sizing guidance"
    These figures are indicative. Contact Sekoia before deployment to validate requirements against your specific workload and asset profile.

| Size | Incoming data | Assets (approx.) | Servers (3 managers included) | Object storage to provision (365 days) |
| :--- | :---: | :---: | :---: | :---: |
| Small | 500 GB/day | ~5,000 | 6 (3 managers + 3 workers) | 159 TB |
| Medium | 2 TB/day | ~20,000 | 24 (3 managers + 21 workers) | 635 TB |
| Large | 5 TB/day | ~50,000 | 60 (3 managers + 57 workers) | 1,588 TB |

**What is an asset?** An asset is any monitored entity (server, endpoint, network device) that generates log events sent to the platform. The asset counts above are approximations. Actual capacity depends on the size and frequency of ingested log messages.

**Object storage:** The table applies the formulas in [Size the object storage](#size-the-object-storage) with 365 days of retention.

**Node roles:** Each production cluster has exactly 3 manager nodes (Kubernetes control plane), the only supported manager-node topology. The SHC does not check this count: `utils.ansible.inventory.managers` accepts any number of addresses, and `CheckServerSpec` validates each node on its own. The topology is a Sekoia support requirement. The **Servers** column includes the manager nodes. They also run platform workloads, like the worker nodes, and must meet the same [compute node specification](#compute-node-specification). With 1 or 2 managers, etcd has no fault tolerance: the loss of one manager stops the Kubernetes API.

**Sizing profiles:** The table sizes the servers and the object storage. The sizing profiles of the SHC set the resources and the replicas of the platform services, not the number of nodes. `sizing/500gb-day.yaml` and `sizing/2tb-day.yaml` target the daily volumes of the Small and Medium sizes, and no profile targets the Large size. The profiles are pending performance validation: choose the profile and adjust it with Sekoia. See [Select and adjust a sizing profile](/self_hosted/1.0.1/deployment/deployment_configuration.md#select-and-adjust-a-sizing-profile).

## Storage

An S3-compatible object storage is required for the event data lake. ExaLog writes the indexed events of every community to it. You must provision it before deployment.

| Requirement | Details |
| :--- | :--- |
| Protocol | S3 API, reached at `global.platform_storage.endpoint` from every Kubernetes node. The scheme and the port come from the endpoint URL. |
| TLS | HTTP or HTTPS. With HTTPS, the certificate of the storage must be signed by a public certificate authority: no setting accepts a private certificate authority for the storage. |
| Region | Required, even when your storage has no region concept: use the value it accepts by default, for example `us-east-1`. |
| Addressing | Path-style requests by default (`global.platform_storage.force_path_style_access`), so bucket names do not need DNS records. |
| Buckets | 16 buckets, named `exalog-self-hosted-events-0` to `exalog-self-hosted-events-f`, plus the `exalog-self-hosted-backups` bucket when you enable backups. You create them before the installation: the platform does not create them. See [Event storage buckets](#event-storage-buckets) and [Backup bucket](#backup-bucket). |
| Credentials | One access key with read, write, list, and delete permissions on these buckets. It does not need to create buckets, except to run the [storage performance check](#storage-performance-check). See [Platform storage](/self_hosted/1.0.1/deployment/deployment_configuration.md#platform-storage). |

### Size the object storage

Size the capacity and the throughput of the object storage with the following formulas.

| Variable | Meaning | Value |
| :--- | :--- | :--- |
| D | Raw data ingested per day, in TB | Your daily ingestion volume |
| R | Retention, in days | Your retention period |
| A | Parsing and enrichment amplification | 2.9 |
| C | Compression ratio | 0.2 |

| Metric | Formula | Example: D = 0.5 TB/day, R = 90 days |
| :--- | :--- | :--- |
| Active storage used (S), in TB | S = D x A x R x C | 0.5 x 2.9 x 90 x 0.2 = 26.1 TB |
| Object storage to provision | 1.5 x S | 39 TB |
| Write capacity, in PUT requests per second | 0.35 x D x A | 0.5 PUT/s |
| Write throughput, in MB/s | 23 x D x A | 33.4 MB/s |
| Read capacity, in GET requests per second | S | 26.1 GET/s |
| Read throughput, in MB/s | 8 x S | 209 MB/s |

These formulas cover the event data only. When you enable backups, the backup bucket uses additional capacity.

Validate the result with Sekoia before you order the storage.

### Storage performance check

On request from Sekoia support, the `CheckS3Performance` benchmark measures the storage from every worker node and compares the median across the nodes with the following minimums: 50 MiB/s for GET and PUT throughput, 100 operations/s for STAT and DELETE, 200 ms for the request latency, and 100 ms for the time to first byte, both at the 90th percentile. See [CheckS3Performance](/self_hosted/1.0.1/troubleshooting/debug_tool.md#checks3performance).

### Event storage buckets

ExaLog stores events across 16 dedicated buckets. The platform does not create these buckets, so bucket creation is your responsibility. Before you start the installation, create one bucket per hexadecimal digit on your S3-compatible storage, named `exalog-self-hosted-events-<digit>`, where `<digit>` is `0` to `9` and `a` to `f`:

```text
exalog-self-hosted-events-0
exalog-self-hosted-events-1
exalog-self-hosted-events-2
...
exalog-self-hosted-events-e
exalog-self-hosted-events-f
```

The buckets do not need individual quotas. Provision all 16 buckets on a single storage pool sized according to [Cluster sizing](#cluster-sizing).

The prefix `exalog-` comes from `modules.platform_configuration.config.storage-manager.s3_bucket_prefix`. If you change it, name the buckets accordingly.

### Backup bucket

When you enable backups, the platform writes the backups of Vault, the PostgreSQL databases, ArangoDB, and ClickHouse to one more bucket, named `<prefix>self-hosted-backups`: `exalog-self-hosted-backups` with the default prefix. By default, this bucket is on the platform storage, and the platform reaches it with the platform storage access key. The platform does not create this bucket on your storage: create it before you enable backups, and give the access key the same permissions on it as on the event buckets.

To use another bucket, endpoint, or access key for the backups, see [Back up the platform](/self_hosted/1.0.1/operations/backups.md).

## Network requirements

DNS management, NTP synchronization, and SMTP configuration are your responsibility.

For DNS, ensure that:

- All Sekoia application servers can resolve each other by hostname and communicate freely.
- All nodes can resolve and reach the Git repository and OCI registry.
- All nodes can resolve and connect to the designated SMTP server.
- The DNS server set in `global.forward_dns` resolves the hostnames of the Git repository, the OCI registry, the S3 storage, and the SMTP server. The platform services do not read the `/etc/hosts` file of the nodes.
- The orchestration node can access every Kubernetes node at the IPv4 address of the inventory.
- DNS records exist for `global.host` and `global.delivery_host` before deployment.
- When `global.kube_manager_host` is configured as a hostname, its DNS record exists before deployment.

See [Platform endpoints](/self_hosted/1.0.1/deployment/deployment_configuration.md#platform-endpoints) for the complete configuration reference for these values.

For NTP, ensure that:

- All nodes synchronize against a customer-provided NTP server.
- Clock skew between nodes stays below 1 second at all times.
- A time-sync service (`systemd-timesyncd` or `chrony`) is installed and enabled on every node.

`CheckServerSpec` reads `timedatectl show` on each node and fails when NTP is disabled or the clock is not synchronized. To enable NTP on a node, run:

```bash
timedatectl set-ntp true
```

If NTP is enabled but the clock is not synchronized, verify that the node can reach your NTP servers, then restart the time-sync service with `systemctl restart systemd-timesyncd` or `systemctl restart chrony`.

For a complete list of required ports and protocols, see [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md).

## Operational requirements

| Requirement | Details |
| :--- | :--- |
| Operations team | A dedicated in-house or partner team must handle deployment, configuration, updates, and monitoring. |
| Infrastructure management | You must provision and manage your own servers, virtual machines, or private/public cloud resources. |
| Licensing | A valid Sekoia license must be provisioned before deployment. It defines the maximum number of supervised assets and daily event-ingest capacity. The platform generates alerts and functionality may degrade if limits are reached. |

## Related links

- [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md): Full table of required network ports and protocols.
- [Reference architecture](/self_hosted/1.0.1/architecture/architecture.md): Platform components and node roles.
- [Debug your deployment](/self_hosted/1.0.1/troubleshooting/debug_tool.md): `CheckServerSpec` output and remediation for each failed requirement.
- [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md): Step-by-step installation instructions.
