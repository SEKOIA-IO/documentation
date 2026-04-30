# Deploy the platform

This guide describes how to install the Sekoia Self-Hosted platform using the orchestration CLI.

## Prerequisites
* An orchestration node running with docker installed on it. 
* Access to the digitally signed Sekoia installer archive.

## Preparation work

### 1. Download and Extract

1. **Download**: Follow the dedicated procedure and use your specific credentials to download the Self-Hosted release.
2. **Transfer**: Import your archive into the admin node.
3. **Integrity Check**: Always verify the archive checksum before proceeding.
4. **Extract**: 
   ```bash
   tar -xvf sekoia-archive.tar.gz -C $SEKOIA_LOCAL_DIR
    ```
!!! note "Disk space requirements"
    Ensure the destination directory provides at least 100 GB of available disk space to extract the Sekoia release.

### 2. Initialize the Controller

For the first installation, the Self-Hosted Controller (SHC) is not available as a service. You must load the Docker image manually to initialize the environment:

```bash
     docker load -i $SEKOIA_LOCAL_DIR/v0.0.1/images/self-hosted-controller.tgz
```

### 3. Write your configuration file

Prepare your config.yml manifest. This file acts as the single source of truth for your infrastructure, service, and network parameters. Ensure this file is ready before moving to the next step, as it will be mapped to the container during script execution. Please read [this documentation](./deployment_configuration.md) to define your parameters

### 4. Create the Execution Script
To simplify Sekoia installation commands and manage environment variables, create a local script called run-shc.sh with the following content:

```bash
#!/bin/bash
DOCKER_IMAGE="sekoialab/self-hosted-controller-cli:latest"

docker run --rm \
-e SERVERS_SUDO_PASSWORD="$SERVERS_SUDO_PASSWORD" \
-e SERVERS_SSH_KEY="$SERVERS_SSH_KEY" \
-e REGISTRY_USERNAME="$REGISTRY_USERNAME" \
-e REGISTRY_PASSWORD="$REGISTRY_PASSWORD" \
-e GIT_HTTP_USERNAME="$GIT_HTTP_USERNAME" \
-e GIT_HTTP_PASSWORD="$GIT_HTTP_PASSWORD" \
--network=host \
-v $CONFIG_HOST:/tmp/config.yaml \
-v $SEKOIA_LOCAL_DIR:/opt/sekoia \
${DOCKER_IMAGE} -c /tmp/config.yaml "$@"
```

!!! note "Environment variable configuration"
    You can define these variables directly in your configuration file or as environment variables on the host system.

| Variable | Description |
| :--- | :--- |
| `SEKOIA_LOCAL_DIR` | The directory used to extract the local Sekoia release. |
| `SEKOIA_CONFIG_FILE` | The path to the local configuration file for the self-hosted controller. |
| `SERVERS_SUDO_PASSWORD` | The sudo password to access target machines (optional, depends on your configuration). |
| `SERVERS_SSH_KEY` | The SSH key used to access remote machines. |
| `REGISTRY_USERNAME` | The username for the OCI registry. |
| `REGISTRY_PASSWORD` | The password for the OCI registry. |
| `GIT_HTTP_USERNAME` | The username for Code repository. |
| `GIT_HTTP_PASSWORD` | The password for Code repository. |


Once created, make the script executable and test your configuration:

```bash
chmod +x run-shc.sh
./run-shc list
```

## Deployment Options

### Option 1: Bundle Deployment

This method executes all commands sequentially, providing the simplest installation path.

Trigger the deployment:

```bash
./run-shc exec Install
```

Wait for the final convergence report.

### Option 2: Step-by-Step Deployment

If you prefer manual control, you can execute the deployment stages individually.

#### 1. Run Preflight Checks
You must validate the environment before proceeding. The tool checks the Self-Hosted configuration, local Git, local OCI registry, release files, and server availability.

```bash
./run-shc exec CheckRequiredConfigItems
./run-shc exec CheckLocalGit
./run-shc exec CheckLocalOCIRegistry
./run-shc exec CheckLocalReleaseFiles
./run-shc exec CheckServersAreReachable
./run-shc exec CheckServerSpec
```

!!! warning "Preflight block"
    The installation will not proceed if critical validation checks fail.

#### 2. Provision Local Registries

```bash
./run-shc exec PushImages
./run-shc exec PushCharts
./run-shc exec PushArgoStacks
```

#### 3. Install Kube Stack

```bash
./run-shc exec K3SInstall
./run-shc exec GetKubeconfig
./run-shc exec HelmInstall
./run-shc exec CheckKubernetesCluster
```

#### 4. Deploy Sekoia Platform

```bash
./run-shc exec sekoia
```

## Results

The Sekoia platform is now operational. You can access the interface via the Load Balancer URL provided in your configuration.