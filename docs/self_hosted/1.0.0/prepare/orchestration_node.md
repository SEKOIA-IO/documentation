# Prepare the orchestration node

The orchestration node runs the self-hosted-controller (SHC) in a Docker container. It does not join the Kubernetes cluster. You run every SHC command from this node.

## Rules

- The node **MUST** run Debian 12 or 13, with 4 CPUs and 8 GB of RAM or more.
- The node **MUST** reach every Kubernetes node on TCP port 22 (SSH) and TCP port 6443 (Kubernetes API), without a jump host.
- The node **MUST** reach the Git server, the OCI registry and the DNS servers. See [Network requirements](../deployment/network_requirements.md#flows-from-the-orchestration-node).
- Docker **MUST** be installed and running.
- The user who runs the SHC **MUST** be a member of the `docker` group.
- The node **MUST** have 150 GB of free disk space for the release archive. It **SHOULD** have **300 GB** on a dedicated disk: the Sekoia lab keeps the archive and its extracted files together on a 300 GB disk.
- The Docker network (`172.17.0.0/16` by default) **SHOULD NOT** overlap one of your networks.
- The SSH private key used by the SHC **MUST NOT** have a passphrase.

### If you do not follow a SHOULD rule

| SHOULD rule not followed | What you must change |
| :--- | :--- |
| Less than 300 GB free | After the checksum is verified and the archive is extracted, delete the archive file: `rm /opt/workspace/sekoia/sekoia-self-hosted-v1.0.0.tar`. |
| `172.17.0.0/16` is used in your network | Before the first `docker load`, create `/etc/docker/daemon.json` with `{"bip": "192.168.200.1/24"}` (choose a free range), then run `sudo systemctl restart docker`. |

## Step 1: Install Docker

=== "Docker CE (Docker repository)"

    **Validation status:** validated in the Sekoia lab (Debian 13). The lab installs `docker-ce`, `docker-ce-cli` and `containerd.io`; `docker-compose-plugin` comes with them as a recommended package. The command below names it explicitly.

    1. Install the tools that `apt` needs to add the Docker repository:

        ```bash
        sudo apt-get update
        ```

        ```bash
        sudo apt-get install -y ca-certificates curl gnupg lsb-release
        ```

    2. Download the Docker signing key:

        ```bash
        curl -fsSL https://download.docker.com/linux/debian/gpg -o /tmp/docker.gpg
        ```

    3. Install the key:

        ```bash
        sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg /tmp/docker.gpg
        ```

    4. Add the Docker repository:

        ```bash
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
        ```

    5. Install Docker:

        ```bash
        sudo apt-get update
        ```

        ```bash
        sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
        ```

    6. Start Docker now and at every boot:

        ```bash
        sudo systemctl enable --now docker
        ```

    7. Check:

        ```bash
        sudo docker run --rm hello-world
        ```

        **Expected result:** the output contains `Hello from Docker!`. On an air-gapped site, this test image cannot be downloaded: run `sudo docker info` instead and check that it prints `Server Version`.

## Step 2: Give Docker access to your user

1. Add your user to the `docker` group:

    ```bash
    sudo usermod -aG docker $USER
    ```

2. **Log out and log in again.** The new group is active only in a new session.

3. Check:

    ```bash
    docker ps
    ```

    **Expected result:** a table header that starts with `CONTAINER ID`, and no `permission denied` error.

## Step 3: Prepare the release disk

**Validation status:** validated in the Sekoia lab (300 GB disk mounted on `/opt/workspace`).

Skip this step if the system disk already has 300 GB free.

1. Find the empty disk:

    ```bash
    lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS
    ```

2. Create a filesystem on it. **This command destroys all data on the disk.** Replace `<DISK>` with the disk name, for example `sdb`:

    ```bash
    sudo mkfs.ext4 /dev/<DISK>
    ```

3. Create the mount point:

    ```bash
    sudo mkdir -p /opt/workspace
    ```

4. Mount the disk at every boot. Read the identifier of the disk:

    ```bash
    sudo blkid -s UUID -o value /dev/<DISK>
    ```

    Add a line to `/etc/fstab`. Replace `<UUID>` with the value printed by the previous command:

    ```bash
    echo "UUID=<UUID> /opt/workspace ext4 defaults 0 2" | sudo tee -a /etc/fstab
    ```

5. Mount it now and give it to your user:

    ```bash
    sudo mount /opt/workspace
    ```

    ```bash
    sudo chown $USER: /opt/workspace
    ```

6. Check:

    ```bash
    df -h /opt/workspace
    ```

    **Expected result:** a line with `/opt/workspace` and the size of the disk.

## Step 4: Authorize the SSH key on every node

The SHC connects to every Kubernetes node with an SSH key. Create the key on the orchestration node, then copy its public part to every node.

1. Create the key, **without a passphrase**:

    ```bash
    ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519
    ```

2. Copy the public key to each Kubernetes node. Run the command once per node, and type the password of `<ADMIN_USER>` when asked:

    ```bash
    ssh-copy-id -i ~/.ssh/id_ed25519.pub <ADMIN_USER>@<NODE_IP>
    ```

    If the node accepts no password (cloud image), add the content of `~/.ssh/id_ed25519.pub` to `/home/<ADMIN_USER>/.ssh/authorized_keys` on the node in another way, for example with cloud-init.

3. Check each node. The command must not ask for a password:

    ```bash
    ssh -o BatchMode=yes <ADMIN_USER>@<NODE_IP> "sudo -n true && echo OK"
    ```

    **Expected result:** `OK`. If you see `Permission denied`, the key is not authorized. If you see `sudo: a password is required`, see [Configure sudo](./kubernetes_nodes.md#step-4-configure-sudo).

## Step 5: Create the SHC working directory

The SHC container runs as its own user (`shc`, user ID 1000). It writes the Kubernetes configuration file (`kubeconfig.yml`) in a working directory. Create this directory on the host, so that the file stays after the container stops:

```bash
mkdir -p ~/shc && chmod 777 ~/shc
```

## Step 6: Install the download tools

The release archive is downloaded with the AWS CLI. `pv` shows the progress of the checksum verification, which reads about 100 GB.

```bash
sudo apt-get install -y awscli pv openssl
```

## Step 7: Install kubectl (optional)

**Validation status:** validated in the Sekoia lab (kubectl v1.34.10).

`kubectl` is used in the troubleshooting pages. It is not needed for the installation.

1. Download kubectl:

    ```bash
    curl -fLO https://dl.k8s.io/release/v1.34.10/bin/linux/amd64/kubectl
    ```

2. Download its checksum and verify it:

    ```bash
    curl -fLO https://dl.k8s.io/release/v1.34.10/bin/linux/amd64/kubectl.sha256
    ```

    ```bash
    echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
    ```

    **Expected result:** `kubectl: OK`.

3. Install it:

    ```bash
    sudo install -m 0755 kubectl /usr/local/bin/kubectl
    ```

`kubectl` works after the SHC has retrieved the cluster configuration (`exec GetKubeconfig`, also run by `exec Install`), with `export KUBECONFIG=$HOME/shc/kubeconfig.yml`.

## Step 8: Create the environment file

The SHC reads passwords and keys from environment variables. Write them in one file, `~/env.rc`, and load it in **every new terminal** before you run the SHC.

1. Create the file, readable only by you:

    ```bash
    install -m 600 /dev/null ~/env.rc
    ```

2. Open it:

    ```bash
    nano ~/env.rc
    ```

3. Paste this content, then replace every value in angle brackets. Leave a line empty (`""`) when the comment says "only if".

    ```bash
    # Paths on the orchestration node
    export SEKOIA_LOCAL_DIR=/opt/workspace/sekoia             # where the release archive is extracted
    export SEKOIA_CONFIG_FILE=$HOME/config.yml                # your configuration file
    export DOCKER_IMAGE="sekoialab/self-hosted-controller-cli:v1.0.0"   # the SHC image you tag after docker load

    # Kubernetes nodes (see "Prepare the Kubernetes nodes")
    export SERVERS_SSH_KEY="$(cat ~/.ssh/id_ed25519)"         # the CONTENT of the private key, not its path
    export SERVERS_SUDO_PASSWORD=""                           # only if sudo asks for a password on the nodes

    # S3 object storage (see "Prepare the S3 object storage")
    export STORAGE_S3_REGION="<S3_REGION>"
    export STORAGE_S3_ENDPOINT="<S3_ENDPOINT_URL>"            # with http:// or https://
    export STORAGE_S3_ACCESS_KEY="<S3_ACCESS_KEY>"
    export STORAGE_S3_SECRET_KEY="<S3_SECRET_KEY>"

    # OCI registry (see "Prepare the OCI registry")
    export REGISTRY_USERNAME="<REGISTRY_USER>"
    export REGISTRY_PASSWORD='<REGISTRY_PASSWORD>'

    # Git (see "Prepare the Git repository")
    export GIT_HTTP_USERNAME="<GIT_USER>"
    export GIT_HTTP_PASSWORD='<GIT_PASSWORD_OR_TOKEN>'

    # License, provided by Sekoia
    export SEKOIA_INSTANCE_PUBLIC_KEY="<INSTANCE_PUBLIC_KEY_BASE64>"

    # Platform certificate (see "Prepare DNS, time, email and certificates")
    export TRAEFIK_PUBKEY="$(cat $HOME/shc/tls.crt 2>/dev/null)"
    export TRAEFIK_PRIVKEY="$(cat $HOME/shc/tls.key 2>/dev/null)"

    # Release bucket, only if global.version.fetch.offline is false
    export S3_ACCESS_KEY=""
    export S3_SECRET_KEY=""

    # kubectl on the orchestration node
    export KUBECONFIG=$HOME/shc/kubeconfig.yml
    ```

    !!! tip "Single quotes"
        Put passwords between **single quotes** (`'...'`) when they contain `$`, `!` or `` ` ``. Inside double quotes, the shell changes these characters.

4. Load the file:

    ```bash
    source ~/env.rc
    ```

    Run this command again **in every new terminal**. A missing variable gives misleading errors later, for example `403 Forbidden`.

## Step 9: Create the execution script

This script starts the SHC container with all the variables and directories it needs. It replaces the shorter script of [Deploy the platform](../deployment/deployment_guide.md#step-4-create-the-execution-script): it also passes the certificate variables and keeps the working directory.

1. Create the file:

    ```bash
    nano ~/run-shc.sh
    ```

2. Paste this content:

    ```bash
    #!/bin/bash
    DOCKER_IMAGE="${DOCKER_IMAGE:-sekoialab/self-hosted-controller-cli:latest}"

    # The container runs as user ID 1000: its working directory must be writable.
    mkdir -p "$HOME/shc" && chmod 777 "$HOME/shc"

    # Allocate a terminal when the script runs in a terminal (interactive interface).
    TTY_FLAGS=""
    [ -t 0 ] && [ -t 1 ] && TTY_FLAGS="-it"

    docker run --rm $TTY_FLAGS \
      -e SERVERS_SUDO_PASSWORD="$SERVERS_SUDO_PASSWORD" \
      -e SERVERS_SSH_KEY="$SERVERS_SSH_KEY" \
      -e STORAGE_S3_REGION="$STORAGE_S3_REGION" \
      -e STORAGE_S3_ENDPOINT="$STORAGE_S3_ENDPOINT" \
      -e STORAGE_S3_ACCESS_KEY="$STORAGE_S3_ACCESS_KEY" \
      -e STORAGE_S3_SECRET_KEY="$STORAGE_S3_SECRET_KEY" \
      -e REGISTRY_USERNAME="$REGISTRY_USERNAME" \
      -e REGISTRY_PASSWORD="$REGISTRY_PASSWORD" \
      -e GIT_HTTP_USERNAME="$GIT_HTTP_USERNAME" \
      -e GIT_HTTP_PASSWORD="$GIT_HTTP_PASSWORD" \
      -e SEKOIA_INSTANCE_PUBLIC_KEY="$SEKOIA_INSTANCE_PUBLIC_KEY" \
      -e TRAEFIK_PUBKEY="$TRAEFIK_PUBKEY" \
      -e TRAEFIK_PRIVKEY="$TRAEFIK_PRIVKEY" \
      -e S3_ACCESS_KEY="$S3_ACCESS_KEY" \
      -e S3_SECRET_KEY="$S3_SECRET_KEY" \
      --network=host \
      -v "$SEKOIA_CONFIG_FILE":/tmp/config.yaml \
      -v "$SEKOIA_LOCAL_DIR":/opt/sekoia \
      -v "$HOME/shc":/tmp/self-hosted-controller \
      ${DOCKER_IMAGE} -c /tmp/config.yaml "$@"
    ```

3. Make it executable:

    ```bash
    chmod +x ~/run-shc.sh
    ```

You test the script in [Deploy the platform](../deployment/deployment_guide.md#step-4-create-the-execution-script), after the SHC image is loaded.

## SHC container inputs

This table lists every input of the container and when it is needed.

### Environment variables

| Variable | Used for | Needed |
| :--- | :--- | :--- |
| `SERVERS_SSH_KEY` | SSH connection to the nodes (`utils.ansible.ssh-key`). Content of the private key. | Always |
| `SERVERS_SUDO_PASSWORD` | `sudo` and SSH password on the nodes (`utils.ansible.password`). | Only if `sudo` asks for a password |
| `STORAGE_S3_REGION`, `STORAGE_S3_ENDPOINT`, `STORAGE_S3_ACCESS_KEY`, `STORAGE_S3_SECRET_KEY` | Event storage (`global.platform_storage.*`). | Always |
| `REGISTRY_USERNAME`, `REGISTRY_PASSWORD` | OCI registry (`utils.oci_registry.username`, `password`). | Always |
| `GIT_HTTP_USERNAME`, `GIT_HTTP_PASSWORD` | Git repository (`utils.git.http.username`, `password`). | Always |
| `SEKOIA_INSTANCE_PUBLIC_KEY` | License (`modules.platform_configuration.config.global.instance_public_key`). | Always |
| `TRAEFIK_PUBKEY`, `TRAEFIK_PRIVKEY` | Platform certificate (`modules.platform_configuration.config.traefik.custom_cert.*`). | When you provide your certificate |
| `S3_ACCESS_KEY`, `S3_SECRET_KEY` | Download from the Sekoia release bucket. | Only if `global.version.fetch.offline` is `false` |
| Any variable you reference as `${env.NAME}` in `config.yml` | The field where you wrote the reference. | Add `-e NAME="$NAME"` to the script |

!!! warning "A variable is not passed automatically"
    The container sees only the variables listed with `-e` in `run-shc.sh`. If you write `${env.SMTP_PASSWORD}` in `config.yml`, you **MUST** also add `-e SMTP_PASSWORD="$SMTP_PASSWORD"` to the script and `export SMTP_PASSWORD='...'` to `env.rc`.

### Directories

| Host directory | Container directory | Needed | Content |
| :--- | :--- | :--- | :--- |
| `$SEKOIA_CONFIG_FILE` | `/tmp/config.yaml` | Always | Your configuration file. |
| `$SEKOIA_LOCAL_DIR` | `/opt/sekoia` | Always | The extracted release and the content bundles. |
| `$HOME/shc` | `/tmp/self-hosted-controller` | Always (recommended) | `kubeconfig.yml`. Without it, the file is lost when the container stops. |

## Checklist

- [ ] Docker runs, and `docker ps` works without `sudo`.
- [ ] 300 GB are free for the release (or you will delete the archive after extraction).
- [ ] `ssh -o BatchMode=yes <ADMIN_USER>@<NODE_IP> "sudo -n true && echo OK"` prints `OK` for every node.
- [ ] `~/shc` exists.
- [ ] `~/env.rc` is filled and loaded with `source ~/env.rc`.
- [ ] `~/run-shc.sh` exists and is executable.
