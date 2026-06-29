# Deploy the platform

This guide walks you through the full installation of Sekoia Self-Hosted, from downloading the release archive to validating a healthy platform state. Follow the steps in order.

## Prerequisites
- All nodes meet the requirements listed in [Technical requirements](./deployment_prerequisites.md).
- Firewall rules allow the flows listed in [Network requirements](./network_requirements.md).
- Your `config.yml` manifest is ready. See [Deployment configuration reference](./deployment_configuration.md).
- Docker is installed on the orchestration node.

## Preparation 

### Step 1: Download and verify the release archive

Sekoia provides access to a dedicated object storage bucket containing the release archive and its SHA-256 checksum. You receive the bucket credentials (endpoint, access key, and secret key) from Sekoia after contract validation.

!!! warning "Verify before you extract"
    Always verify the checksum before extracting the archive. A mismatch indicates a corrupted or incomplete download. Do not proceed if verification fails. Download the archive again before retrying.

Download the archive and its checksum file, then verify integrity. Fill in your credentials where indicated.

??? example "AWS CLI"
    ```bash
    export AWS_ACCESS_KEY_ID=""
    export AWS_SECRET_ACCESS_KEY=""
    export AWS_DEFAULT_REGION="fr-par"
    export ENDPOINT="https://fr-par-13.linodeobjects.com"
    export BUCKET="self-hosted"
    export KEY="archives/sekoia-self-hosted-v0.0.1.tar"
    export OUT="sekoia-self-hosted-v0.0.1.tar"
    export AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED
    export AWS_RESPONSE_CHECKSUM_VALIDATION=WHEN_REQUIRED

    aws --endpoint-url "$ENDPOINT" s3 cp "s3://$BUCKET/$KEY" "$OUT"
    aws --endpoint-url "$ENDPOINT" s3 cp "s3://$BUCKET/$KEY.sha256" "$OUT.sha256"

    sha256sum -c "$OUT.sha256"
    ```

    !!! note "AWS CLI v2 checksum compatibility"
        `AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED` and `AWS_RESPONSE_CHECKSUM_VALIDATION=WHEN_REQUIRED` disable the automatic checksum behavior introduced in AWS CLI v2, which is incompatible with non-AWS S3-compatible providers.

??? example "rclone"
    ```bash
    export RCLONE_CONFIG_SEKOIA_TYPE="s3"
    export RCLONE_CONFIG_SEKOIA_PROVIDER="Other"
    export RCLONE_CONFIG_SEKOIA_ACCESS_KEY_ID=""
    export RCLONE_CONFIG_SEKOIA_SECRET_ACCESS_KEY=""
    export RCLONE_CONFIG_SEKOIA_ENDPOINT="https://fr-par-13.linodeobjects.com"
    export RCLONE_CONFIG_SEKOIA_REGION="fr-par"

    rclone copyto sekoia:self-hosted/archives/sekoia-self-hosted-v0.0.1.tar ./sekoia-self-hosted-v0.0.1.tar
    rclone copyto sekoia:self-hosted/archives/sekoia-self-hosted-v0.0.1.tar.sha256 ./sekoia-self-hosted-v0.0.1.tar.sha256

    sha256sum -c sekoia-self-hosted-v0.0.1.tar.sha256
    ```

Expected output: `sekoia-self-hosted-v0.0.1.tar: OK`

### Step 2: Transfer and extract the archive

To transfer the archive to the orchestration node if you downloaded it on a separate machine, run:

```bash
scp sekoia-self-hosted-v0.0.1.tar user@<ORCHESTRATION_NODE>:$SEKOIA_LOCAL_DIR
```

!!! note "Disk space"
    Ensure at least 150 GB of available disk space at the destination before extracting.

To extract the archive on the orchestration node, run:

```bash
tar -xvf sekoia-self-hosted-v0.0.1.tar -C $SEKOIA_LOCAL_DIR
```

### Step 3: Load the SHC Docker image

For the first installation, the SHC image is not yet available on the orchestration node. Load it manually from the extracted archive:

```bash
docker load -i $SEKOIA_LOCAL_DIR/v0.0.1/images/registry.sekoia.io_sekoialab_platform-installer-self-hosted-v0.0.1.tar.gz
```

To confirm the image loaded successfully, run:

```bash
docker images | grep self-hosted-controller
```

!!! note "Air-gapped deployments"
    In air-gapped environments, the SHC image is always loaded from the local archive. After loading, tag the image and export its reference to override the default `DOCKER_IMAGE` value used by the execution script:

    ```bash
    docker tag <IMAGE_ID> sekoialab/self-hosted-controller-cli:v0.0.1
    export DOCKER_IMAGE="sekoialab/self-hosted-controller-cli:v0.0.1"
    ```

    Replace `<IMAGE_ID>` with the image ID returned by `docker images`.

### Step 4: Create the execution script

The execution script `run-shc.sh` wraps all SHC invocations, injects credentials from environment variables, and mounts your config file into the container.

Create a file named `run-shc.sh` with the following content:

```bash
#!/bin/bash
DOCKER_IMAGE="${DOCKER_IMAGE:-sekoialab/self-hosted-controller-cli:latest}"

docker run --rm \
  -e SERVERS_SUDO_PASSWORD="$SERVERS_SUDO_PASSWORD" \
  -e SERVERS_SSH_KEY="$SERVERS_SSH_KEY" \
  -e REGISTRY_USERNAME="$REGISTRY_USERNAME" \
  -e REGISTRY_PASSWORD="$REGISTRY_PASSWORD" \
  -e GIT_HTTP_USERNAME="$GIT_HTTP_USERNAME" \
  -e GIT_HTTP_PASSWORD="$GIT_HTTP_PASSWORD" \
  --network=host \
  -v $SEKOIA_CONFIG_FILE:/tmp/config.yaml \
  -v $SEKOIA_LOCAL_DIR:/opt/sekoia \
  ${DOCKER_IMAGE} -c /tmp/config.yaml "$@"
```

Set the following environment variables on the orchestration node before running the script:

| Variable | Required | Description |
| :--- | :---: | :--- |
| `SEKOIA_LOCAL_DIR` | Yes | Absolute path to the directory where you extracted the release archive. |
| `SEKOIA_CONFIG_FILE` | Yes | Absolute path to your `config.yml` manifest on the orchestration node. |
| `SERVERS_SSH_KEY` | Yes | SSH private key used to connect to Kubernetes nodes. |
| `REGISTRY_USERNAME` | Yes | Username for your local OCI registry. |
| `REGISTRY_PASSWORD` | Yes | Password for your local OCI registry. |
| `GIT_HTTP_USERNAME` | Yes | Username for your local code repository. |
| `GIT_HTTP_PASSWORD` | Yes | Password or token for your local code repository. |
| `SERVERS_SUDO_PASSWORD` | No | Sudo password for target nodes, if required by your SSH configuration. |
| `DOCKER_IMAGE` | No | Override the SHC Docker image reference. Required in air-gapped environments. |

To make the script executable and verify the SHC responds, run:

```bash
chmod +x run-shc.sh
./run-shc.sh list
```

A successful run displays the full list of available SHC commands.

## Deployment

Choose one of the two deployment options below.

### Option 1: Bundle deployment

The bundle command runs all installation steps sequentially. This is the simplest path for standard deployments.

To run the full installation, enter:

```bash
./run-shc.sh exec Install
```

Wait for the final convergence report before proceeding to [Post-deployment validation](#post-deployment-validation).

### Option 2: Step-by-step deployment

Use this option when your environment requires manual validation or approval between stages.

**Step 1: Run preflight checks.**

To validate the environment before any changes are made, run:

```bash
./run-shc.sh exec CheckLocalConfig
./run-shc.sh exec CheckLocalGit
./run-shc.sh exec CheckLocalOCIRegistry
./run-shc.sh exec CheckLocalReleaseFiles
./run-shc.sh exec CheckServersAreReachable
./run-shc.sh exec CheckServerSpec
```

!!! warning "Preflight block"
    The SHC will not proceed if any critical validation check fails. Each failure is logged with an actionable error message. Resolve all errors before continuing.

**Step 2: Configure servers.**

To prepare the operating system and install required packages on all nodes, run:

```bash
./run-shc.sh exec ConfigureServersWithAnsible
```

**Step 3: Provision local registries.**

To push all Docker images, Helm charts, and ArgoCD stack manifests to your local repositories, run:

```bash
./run-shc.sh exec PushImages
./run-shc.sh exec PushCharts
./run-shc.sh exec PushArgoStacks
```

**Step 4: Install the Kubernetes stack.**

To install K3s and deploy the cluster services, run:

```bash
./run-shc.sh exec K3SInstall
./run-shc.sh exec GetKubeconfig
./run-shc.sh exec HelmInstall
./run-shc.sh exec CheckKubernetesCluster
```

**Step 5: Deploy the Sekoia platform.**

To generate the platform configuration, run the installer job, and retrieve the initial access credentials, run:

```bash
./run-shc.sh exec PlatformConfigurationFile
./run-shc.sh exec PlatformInstallation
./run-shc.sh exec PlatformAccess
```

## Post-deployment validation

After the installation completes, run the following checks to confirm the platform is healthy before directing users to it.

**Step 1: Verify cluster node health.**

To confirm all nodes joined the cluster and are ready, run:

```bash
./run-shc.sh exec CheckKubernetesCluster
```

??? example "Expected output"
    ```
    Kubernetes cluster is healthy nodes=6 expected=6
    ```

If the node count does not match, check `kubectl get nodes` to identify which node is missing.

**Step 2: Check application sync and health status.**

To inspect every ArgoCD application, run:

```bash
./run-shc.sh exec DebugArgoCD
```

Every application must show `Sync: Synced` and `Health: Healthy`. `Progressing` is normal for a few minutes immediately after deployment. `Degraded` or `OutOfSync` requires investigation. See [Debug your deployment](../troubleshooting/debug_tool.md).

**Step 3: Verify database availability.**

To confirm all database StatefulSets and CNPG clusters are ready, run:

```bash
./run-shc.sh exec DebugDatabases
```

All entries must report `Healthy` status with the expected number of ready replicas.

**Step 4: Access the platform.**

To open the Sekoia interface, navigate to the URL set in `global.host` of your `config.yml` (for example, `https://app.sekoia.local`).

!!! note "First login"
    The platform does not create a default administrator account. You must provision the first user via an email invitation. See [Set up the first administrator account](../operations/first_login.md).

## Related links

- [Technical requirements](./deployment_prerequisites.md): Hardware and network prerequisites.
- [Deployment configuration reference](./deployment_configuration.md): Full `config.yml` parameter reference.
- [Debug your deployment](../troubleshooting/debug_tool.md): Troubleshooting commands and remediation steps.
- [Set up the first administrator account](../operations/first_login.md): Post-installation user provisioning.
