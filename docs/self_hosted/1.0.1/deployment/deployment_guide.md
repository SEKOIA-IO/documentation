# Deploy the platform

This guide walks you through the full installation of Sekoia Self-Hosted, from downloading the release archive to validating a healthy platform state. Follow the steps in order.

## Prerequisites
- All nodes meet the requirements listed in [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md).
- The operating system and the packages listed in [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md) are installed on every node. The SHC does not install or harden the operating system. It only applies the changes listed in [Changes applied by the SHC to the nodes](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#changes-applied-by-the-shc-to-the-nodes).
- Firewall rules allow the flows listed in [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md).
- Your `config.yml` manifest is ready. See [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md).
- Docker is installed on the orchestration node.
- The platform certificate and its private key are available in PEM format. See [TLS certificate](/self_hosted/1.0.1/deployment/deployment_configuration.md#tls-certificate).

## Preparation

### Step 1: Download and verify the release archive

Sekoia provides access to a dedicated object storage bucket containing the release archive and its SHA-256 checksum. You receive the bucket credentials (endpoint, access key, and secret key) from Sekoia after contract validation.

The checksum detects a corrupted or incomplete download: the archive itself is not signed. The container images and the security content bundles it contains are signed with cosign, and the public key `cosign.pub` ships in `platform/v1.0.1/`. The SHC does not verify these signatures.

!!! warning "Verify before you extract"
    Always verify the checksum before extracting the archive. A mismatch indicates a corrupted or incomplete download. Do not proceed if verification fails. Download the archive again before retrying.

!!! tip "Keep the credentials out of the shell history"
    Do not type the access key and the secret key on the command line, where they stay in the shell history. Write their `export` lines in a file that only your user can read, for example `~/sekoia-delivery.env` protected with `chmod 600 ~/sekoia-delivery.env`, and load it with `source` as the examples do. The examples remove the credentials from the shell with `unset` once the download completes.

Download the archive and its checksum file, then verify integrity.

??? example "AWS CLI"
    ```bash
    source ~/sekoia-delivery.env  # exports AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
    export AWS_DEFAULT_REGION="fr-par-2"
    export ENDPOINT="https://self-hosted.delivery.sekoia.io"
    export BUCKET="self-hosted"
    export KEY="platform/v1.0.1/archives/v1.0.1.tar.gz"
    export OUT="sekoia-self-hosted-v1.0.1.tar.gz"
    export AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED
    export AWS_RESPONSE_CHECKSUM_VALIDATION=WHEN_REQUIRED

    aws --endpoint-url "$ENDPOINT" s3 cp "s3://$BUCKET/$KEY" "$OUT"
    aws --endpoint-url "$ENDPOINT" s3 cp "s3://$BUCKET/$KEY.sha256" "$OUT.sha256"
    unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY

    echo "$(cut -d' ' -f1 "$OUT.sha256")  $OUT" | sha256sum -c -
    ```

    !!! note "AWS CLI v2 checksum compatibility"
        `AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED` and `AWS_RESPONSE_CHECKSUM_VALIDATION=WHEN_REQUIRED` disable the automatic checksum behavior introduced in AWS CLI v2, which is incompatible with non-AWS S3-compatible providers.

??? example "rclone"
    ```bash
    source ~/sekoia-delivery.env  # exports RCLONE_CONFIG_SEKOIA_ACCESS_KEY_ID and RCLONE_CONFIG_SEKOIA_SECRET_ACCESS_KEY
    export RCLONE_CONFIG_SEKOIA_TYPE="s3"
    export RCLONE_CONFIG_SEKOIA_PROVIDER="Other"
    export RCLONE_CONFIG_SEKOIA_ENDPOINT="https://self-hosted.delivery.sekoia.io"
    export RCLONE_CONFIG_SEKOIA_REGION="fr-par-2"

    rclone copyto sekoia:self-hosted/platform/v1.0.1/archives/v1.0.1.tar.gz ./sekoia-self-hosted-v1.0.1.tar.gz
    rclone copyto sekoia:self-hosted/platform/v1.0.1/archives/v1.0.1.tar.gz.sha256 ./sekoia-self-hosted-v1.0.1.tar.gz.sha256
    unset RCLONE_CONFIG_SEKOIA_ACCESS_KEY_ID RCLONE_CONFIG_SEKOIA_SECRET_ACCESS_KEY

    echo "$(cut -d' ' -f1 sekoia-self-hosted-v1.0.1.tar.gz.sha256)  sekoia-self-hosted-v1.0.1.tar.gz" | sha256sum -c -
    ```

Expected output: `sekoia-self-hosted-v1.0.1.tar.gz: OK`

### Step 2: Transfer and extract the archive

To transfer the archive and its checksum file to the orchestration node if you downloaded them on a separate machine, run:

```bash
scp sekoia-self-hosted-v1.0.1.tar.gz sekoia-self-hosted-v1.0.1.tar.gz.sha256 user@<ORCHESTRATION_NODE>:<SEKOIA_LOCAL_DIR>/
```

Replace `<SEKOIA_LOCAL_DIR>` with the absolute path of the release directory on the orchestration node. To check that the transfer did not alter the archive, run `echo "$(cut -d' ' -f1 sekoia-self-hosted-v1.0.1.tar.gz.sha256)  sekoia-self-hosted-v1.0.1.tar.gz" | sha256sum -c -` again in this directory on the orchestration node.

!!! note "Disk space"
    The extracted files take about as much space as the archive, about 110 GB for 1.0.1. Before you extract it, make sure the orchestration node has this free space in addition to the archive: about 220 GB in total. You can delete the archive and its checksum file once it is extracted. See [Orchestration node requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#orchestration-node-requirements).

To extract the archive on the orchestration node, run:

```bash
tar -xvf sekoia-self-hosted-v1.0.1.tar.gz -C $SEKOIA_LOCAL_DIR
```

The archive contains the platform release and the latest security content bundles:

| Directory | Content |
| :--- | :--- |
| `$SEKOIA_LOCAL_DIR/platform/v1.0.1/` | Release manifest, the cosign public key `cosign.pub`, Docker images, Helm charts, ArgoCD stacks, and the third-party license notices in `licenses/THIRD-PARTY-NOTICES.md`. |
| `$SEKOIA_LOCAL_DIR/data/<TYPE>/` | One security content bundle per type (`detection-rules`, `intake-formats`, and `playbook-library`), with a `latest` file that names the bundle to use. |

The archive does not include the Sekoia CTI database. In air-gapped mode, download its separate archive once the platform is installed. See [Import the CTI database](/self_hosted/1.0.1/operations/import_cti_database.md#prepare-the-cti-export-in-air-gapped-mode).

The execution script mounts `$SEKOIA_LOCAL_DIR` on `/opt/sekoia` in the SHC container, which matches the default values of `global.version.platform.path` (`/opt/sekoia/platform/`) and `global.version.data.<TYPE>.path` (`/opt/sekoia/data/`). Keep this layout unless you also change these paths.

!!! warning "Air-gapped deployments"
    Set `global.version.fetch.offline` to `true` in your `config.yml`. With this setting, `DownloadReleaseFiles` and `DownloadDataFiles` use the extracted files and make no request to the Sekoia S3 bucket. Without it, they try to download the release again and fail without internet access. See [Release download and security content](/self_hosted/1.0.1/deployment/deployment_configuration.md#release-download-and-security-content).

### Step 3: Load the self-hosted-controller (SHC) Docker image

The SHC image ships in the release archive, in online mode as in air-gapped mode. To load it on the orchestration node, run:

```bash
docker load -i $SEKOIA_LOCAL_DIR/platform/v1.0.1/images/registry.sekoia.io_sekoialab_self-hosted-controller-cli-2.20261027-40526598025-01c5f7786cea2516605ec317c83b1f24bcee8b12.tar.gz
```

The command prints the reference of the loaded image: `registry.sekoia.io/sekoialab/self-hosted-controller-cli:2.20261027-40526598025-01c5f7786cea2516605ec317c83b1f24bcee8b12`.

To give the image the reference that the execution script runs, run:

```bash
docker tag registry.sekoia.io/sekoialab/self-hosted-controller-cli:2.20261027-40526598025-01c5f7786cea2516605ec317c83b1f24bcee8b12 sekoialab/self-hosted-controller-cli:v1.0.1
```

To confirm, run `docker images sekoialab/self-hosted-controller-cli`. Expected output: one image with the `v1.0.1` tag.

### Step 4: Create the execution script

The execution script `run-shc.sh` wraps all SHC invocations, injects credentials from environment variables, and mounts your config file into the container.

Create a file named `run-shc.sh` with the following content:

```bash
#!/bin/bash
DOCKER_IMAGE="${DOCKER_IMAGE:-sekoialab/self-hosted-controller-cli:v1.0.1}"

# Allocate a TTY when the script runs in a terminal, so the interactive
# interface can render. Skipped in non-interactive contexts such as CI.
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
  -e BACKUP_VAULT_CRYPT_KEY="$BACKUP_VAULT_CRYPT_KEY" \
  -e BACKUP_ARANGO_CRYPT_KEY="$BACKUP_ARANGO_CRYPT_KEY" \
  -e BACKUP_CLICKHOUSE_CRYPT_KEY="$BACKUP_CLICKHOUSE_CRYPT_KEY" \
  --network=host \
  -v $SEKOIA_CONFIG_FILE:/tmp/config.yaml \
  -v $SEKOIA_LOCAL_DIR:/opt/sekoia \
  ${DOCKER_IMAGE} -c /tmp/config.yaml "$@"
```

!!! note "Container user"
    The SHC container runs as the `shc` user, with UID 1000. This user must be able to read `$SEKOIA_CONFIG_FILE`. It must also be able to write to `$SEKOIA_LOCAL_DIR`, where the SHC stores the per-run log file and, in online mode, the downloaded release files. Give UID 1000 write access to this directory in every mode, for example with `sudo chown -R 1000 $SEKOIA_LOCAL_DIR`. Without it, the SHC starts without file logging. See [SHC log file](/self_hosted/1.0.1/deployment/deployment_configuration.md#shc-log-file).

Set the following environment variables on the orchestration node before running the script:

| Variable | Required | Description |
| :--- | :---: | :--- |
| `SEKOIA_LOCAL_DIR` | Yes | Absolute path to the directory where you extracted the release archive. |
| `SEKOIA_CONFIG_FILE` | Yes | Absolute path to your `config.yml` manifest on the orchestration node. |
| `SERVERS_SSH_KEY` | Yes | SSH private key used to connect to Kubernetes nodes. |
| `STORAGE_S3_REGION` | Yes | Region of the S3-compatible platform storage. |
| `STORAGE_S3_ENDPOINT` | Yes | Endpoint of the S3-compatible platform storage. |
| `STORAGE_S3_ACCESS_KEY` | Yes | Access key for the S3-compatible platform storage. |
| `STORAGE_S3_SECRET_KEY` | Yes | Secret key for the S3-compatible platform storage. |
| `REGISTRY_USERNAME` | Yes | Username for your local OCI registry. |
| `REGISTRY_PASSWORD` | Yes | Password for your local OCI registry. |
| `GIT_HTTP_USERNAME` | Yes | Username for your local code repository. |
| `GIT_HTTP_PASSWORD` | Yes | Password or token for your local code repository. |
| `SERVERS_SUDO_PASSWORD` | No | Sudo password for target nodes, if `sudo` asks for one. The SHC also uses it when the SSH server asks for a password. |
| `DOCKER_IMAGE` | No | Override the self-hosted-controller (SHC) Docker image reference. Default: `sekoialab/self-hosted-controller-cli:v1.0.1`, the tag that you set in [Step 3](#step-3-load-the-self-hosted-controller-shc-docker-image). |
| `SEKOIA_INSTANCE_PUBLIC_KEY` | Yes | Public key for the Sekoia instance. |
| `TRAEFIK_PUBKEY` | Yes | Platform certificate chain in PEM format. See [TLS certificate](/self_hosted/1.0.1/deployment/deployment_configuration.md#tls-certificate). |
| `TRAEFIK_PRIVKEY` | Yes | Private key of the platform certificate in PEM format. |
| `S3_ACCESS_KEY` | Online mode only | Access key for the Sekoia release bucket, provided by Sekoia. |
| `S3_SECRET_KEY` | Online mode only | Secret key for the Sekoia release bucket, provided by Sekoia. |
| `BACKUP_VAULT_CRYPT_KEY` | Only when backups are enabled | Encryption key of the Vault snapshots, at least 16 characters. Keep a copy outside the platform. See [Back up the platform](/self_hosted/1.0.1/operations/backups.md). |
| `BACKUP_ARANGO_CRYPT_KEY` | Only when backups are enabled | Passphrase of the ArangoDB backups, at least 16 characters. Keep a copy outside the platform. |
| `BACKUP_CLICKHOUSE_CRYPT_KEY` | Only when backups are enabled | Encryption key of the ClickHouse backups, exactly 64 hexadecimal characters, for example generated with `openssl rand -hex 32`. Keep a copy outside the platform. |

!!! tip "Load the credentials from a protected file"
    Do not type secrets on the command line, where they stay in the shell history. Write the `export` lines of these variables in a file that only your user can read, for example `~/sekoia-shc.env` protected with `chmod 600 ~/sekoia-shc.env`, and load it with `source ~/sekoia-shc.env` before you run the script. When you are done, remove the variables from the shell with `unset`. To keep them out of your interactive shell entirely, run the script in a subshell instead, for example `(source ~/sekoia-shc.env && ./run-shc.sh)`.

To make the script executable and verify the SHC responds, run:

```bash
chmod +x run-shc.sh
./run-shc.sh list
```

A successful run displays the full list of available SHC commands.

!!! note "Commands in this documentation"
    Commands elsewhere in this documentation omit the `./run-shc.sh` prefix. Enter them as shown in the TUI, or prefix them with `./run-shc.sh` to run them in one-shot CLI mode.

!!! note "Interactive interface"
    Running `./run-shc.sh` with no command opens the interactive interface of the SHC instead of returning a one-shot result. See [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md).

## Deployment

Choose one of the two deployment options below.

### Option 1: Bundle deployment

The bundle command runs all installation steps sequentially. This is the simplest path for standard deployments.

To run the full installation, enter:

```bash
exec Install
```

The platform installation is normally the longest stage. Leave the command running while it continues to emit progress messages, then wait for the final convergence report before proceeding to [Post-deployment validation](#post-deployment-validation). `PlatformInstallation` fails when the installer job has not completed after 2 hours.

!!! note "Warning messages during installation"
    Warning-level log messages can be normal during the installation. Do not interrupt an installation only because a warning appears while the workflow continues to make progress. The installation has completed when the terminal `Install.start terminated` message reports `success=True` and the [post-deployment validation](#post-deployment-validation) passes. Investigate a terminal `success=False` result, exhausted retries, or a workflow that stops making progress.

If the installation fails, fix the cause reported in the log, then resume it. See [Resume after a failure](/self_hosted/1.0.1/deployment/deployment_process.md#resume-after-a-failure).

### Option 2: Step-by-step deployment

Use this option when your environment requires manual validation or approval between stages. The steps run the modules of the `Install` stages, in the same order. See [The installation execution plan](/self_hosted/1.0.1/deployment/deployment_process.md#the-installation-execution-plan).

**Step 1: Run preflight checks.**

To validate the environment before any change to the nodes, run:

```bash
exec CheckLocalConfig
exec CheckLocalGit
exec CheckLocalOCIRegistry
exec DownloadReleaseFiles
exec CheckLocalReleaseFiles
exec CheckServersAreReachable
exec CheckServerSpec
exec CheckLocalTools
exec CheckNodePortReachability
```

In online mode, `DownloadReleaseFiles` downloads the release files that `CheckLocalReleaseFiles` then checks. In air-gapped mode, it makes no download.

!!! warning "Preflight block"
    Every check is blocking: a failed check stops with an error message that names the cause. Resolve all errors before continuing. `CheckLocalConfig` does not validate the optional settings your environment needs, so some configuration errors only appear in later stages.

`DownloadReleaseFiles` downloads the release files from the Sekoia S3 bucket in online mode, and uses the files extracted from the archive in air-gapped mode. Run it before `CheckLocalReleaseFiles`: in online mode, the release directory does not exist until the download completes.

`CheckServerSpec` fails the installation when a manager or worker node has fewer than 44 logical CPUs or less than 120 GiB of RAM, does not run Debian 12 or later, has an active swap device, shares its hostname with another node, or has no synchronized clock. Before K3s is installed, it also fails when a required port is already in use on the node or, in the default `auto` storage mode, when the node has no unused block device of at least 200 GB. See [CheckServerSpec](/self_hosted/1.0.1/troubleshooting/debug_tool.md#checkserverspec) for each failure message and its remediation.

`CheckNodePortReachability` fails when a node cannot reach another node on one of the cluster ports. See [CheckNodePortReachability](/self_hosted/1.0.1/troubleshooting/debug_tool.md#checknodeportreachability).

**Step 2: Push the images and the security content.**

First resolve the versioned detection-rules, intake-formats, and playbook-library bundles. Then push the Docker images and the detection rules and intake formats bundles to your local OCI registry:

```bash
exec DownloadDataFiles
exec PushImages
exec PushDataBundles
```

`PushImages` runs `DownloadReleaseFiles` as an automatic prerequisite, and `PushDataBundles` runs `DownloadDataFiles`. In online mode, they download the release artifacts and the content bundles; in air-gapped mode, they use the files extracted from the archive. A missing bundle is reported as a warning and skipped, and a bundle that still fails after three push attempts is reported as an error and skipped. In both cases, the platform keeps the content version shipped with the release. By default, repeated runs push every image again. See [Automatic prerequisites and repeated modules](/self_hosted/1.0.1/deployment/deployment_process.md#automatic-prerequisites-and-repeated-modules). The Helm charts and the ArgoCD stacks are published in step 4, once the cluster exists.

**Step 3: Install the Kubernetes stack.**

To install K3s and deploy the cluster services, run:

```bash
exec K3SInstall
exec GetKubeconfig
exec HelmInstall
exec CheckKubernetesCluster
```

**Step 4: Deploy the Sekoia platform.**

To publish the Helm charts and the ArgoCD stacks, generate the platform configuration, run the installer job, deploy the detection rules catalog and the intake formats, and retrieve the initial access credentials, run:

```bash
exec PushArgoStacks
exec PlatformConfigurationFile
exec PlatformInstallation
exec SyncRulesCatalog
exec SyncIntakeFormats
exec PlatformAccess
```

`PushArgoStacks` first runs `PushCharts`, which pushes the Helm charts to your OCI registry, then publishes the ArgoCD stack manifests to your Git repository. It needs the installed cluster: it retrieves the cluster credentials and synchronizes the ArgoCD root application when it already exists. Run it after `PushDataBundles`: it points the content updaters to the bundles only once they are in your registry. A repeated run succeeds without a commit when the generated manifests are unchanged.

`SyncRulesCatalog` and `SyncIntakeFormats` synchronize their ArgoCD applications and wait for the job that loads the content to succeed, for up to 900 seconds each. To allow more time for a large catalog, add `--set modules.sync_rules_catalog.sync_timeout=<SECONDS>` or `--set modules.sync_intake_formats.sync_timeout=<SECONDS>`.

**Step 5: Bootstrap and scale the platform.**

To provision the default storage and the per-community ExaLog indexes, then scale the ingestion and detection workers to their configured replica count, run:

```bash
exec InstanceBootstrap
exec ScaleServices
```

Run these two modules in this order. Until `InstanceBootstrap` completes, ExaLog has no index and cannot write events to your S3-compatible storage. See [Post-installation bootstrap](/self_hosted/1.0.1/deployment/deployment_process.md#post-installation-bootstrap) for what each module provisions.

!!! note "Repeated prerequisite modules"
    The SHC automatically retrieves a current kubeconfig before cluster and platform operations. `PlatformInstallation` and `PlatformAccess` also regenerate the platform configuration before running. Repeated `GetKubeconfig` and `PlatformConfigurationFile` entries in the log are expected and allow each module to run independently.

## Post-deployment validation

After the installation completes, run the following checks to confirm the platform is healthy before directing users to it.

**Step 1: Verify cluster node health.**

To confirm all nodes joined the cluster and are ready, run:

```bash
exec CheckKubernetesCluster
```

??? example "Expected output with 3 managers and 3 workers"
    ```text
    Kubernetes cluster is healthy nodes=6 expected=6
    ```

The `expected` value is the number of unique hosts in `utils.ansible.inventory`. If the node count does not match, the command fails with `Node count mismatch`: run `kubectl get nodes` to identify which node is missing.

**Step 2: Check application sync and health status.**

To inspect every ArgoCD application, run:

```bash
exec DebugArgoCD
```

Every application must show `Sync: Synced` and `Health: Healthy`. `Progressing` is normal for a few minutes immediately after deployment. `Degraded` or `OutOfSync` requires investigation. See [Debug your deployment](/self_hosted/1.0.1/troubleshooting/debug_tool.md).

**Step 3: Verify database availability.**

To confirm all database StatefulSets and CNPG clusters are ready, run:

```bash
exec DebugDatabases
```

All entries must report `Healthy` status with the expected number of ready replicas.

**Step 4: Check the health of the platform services.**

To run every bundled diagnostic target against the platform's Prometheus metrics, run:

```bash
exec Diagnostic
```

Every check must report `OK`. A `CRIT` or `WARN` result names the affected service, its likely causes, and the remediation actions. See [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md).

**Step 5: Access the platform.**

To open the Sekoia interface, navigate to the URL set in `global.host` of your `config.yml` (for example, `https://app.sekoia.local`).

!!! note "First login"
    `PlatformAccess` displays the generated instance-administrator credentials during the installation, before `InstanceBootstrap` and `ScaleServices` run. Scroll back in the output, or run `exec PlatformAccess` to display them again. Store them securely, then use them to create your first operational community. See [Set up the first administrator account](/self_hosted/1.0.1/operations/first_login.md). In the TUI, they are also written to the run log file, so remove them from that file before you share it.

## Related links

- [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md): Hardware and network prerequisites.
- [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md): Starter configuration and required-field reference.
- [Debug your deployment](/self_hosted/1.0.1/troubleshooting/debug_tool.md): Troubleshooting commands and remediation steps.
- [Set up the first administrator account](/self_hosted/1.0.1/operations/first_login.md): Post-installation user provisioning.
- [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md): Follow the installation and inspect the cluster from the interactive interface.
- [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md): Targeted Prometheus health checks per platform area.
