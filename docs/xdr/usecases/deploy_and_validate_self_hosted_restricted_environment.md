# Deploy and validate Sekoia Self-Hosted in a restricted environment

Sekoia Self-Hosted lets you deploy and operate the platform inside infrastructure that you control, including restricted and air-gapped environments. This tutorial shows how to prepare the release, configure offline delivery, install the platform with the self-hosted-controller (SHC), and validate the resulting cluster and services.

## When SaaS cannot cross the perimeter

Your security team works inside a restricted network where sensitive telemetry cannot leave the organization's infrastructure. There is no assumption of continuous internet access, but the platform still has to be installed predictably, validated before analysts use it, and supported by evidence that every required service is healthy.

This tutorial uses the air-gapped execution mode of Sekoia Self-Hosted 1.0.1. The release is transferred into the restricted environment, the SHC installs the platform from local files, and the deployment team validates each layer before opening access to users.

## Do it in Sekoia

Prepare the release, configure offline delivery, run the SHC preflight checks, install the platform, and validate the cluster and services. By the end, you will have a repeatable deployment path and a validation record for configuration, Kubernetes nodes, ArgoCD applications, databases, and platform diagnostics.

## Before you start

- You have access to the Sekoia Self-Hosted 1.0.1 release archive and its SHA-256 checksum.
- You have an orchestration node with Docker installed.
- You have provisioned the nodes and external services listed in [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md).
- Your firewall rules allow the required node-to-node and platform flows described in [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md).
- You have prepared local OCI and code registries for the restricted environment.
- You have a platform certificate and private key in PEM format.
- You have prepared a `config.yml` manifest using [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md).
- You have a secure method to transfer the release archive and checksum into the restricted environment.

!!! warning "Check the release scope"

    Sekoia Self-Hosted 1.0.1 does not include the AI features or the Intelligence module. The Elevate module, AI Cases, and the AI Assistant are not available in this release. Check the [release notes](/self_hosted/1.0.1/release_notes.md) before planning your deployment.

!!! note "Customer-operated platform"

    Your team or a certified Managed Security Service Provider (MSSP) operates the installation, monitoring, backups, and security content updates. Sekoia does not operate the customer deployment.

## Prepare and verify the release archive

Download the release archive and checksum from the delivery location provided by Sekoia. Perform this step on a machine that is allowed to access the delivery endpoint, if the target environment has no external connectivity.

1. Store the delivery credentials in a file readable only by your user.
2. Download the release archive.
3. Download the matching `.sha256` checksum file.
4. Verify the checksum before extracting the archive.
5. Stop if the checksum does not match.

The archive itself is checked with SHA-256. The release also contains signed container images and security content bundles, but the SHC does not verify those signatures.

!!! warning "Do not proceed after a checksum failure"

    A checksum mismatch indicates a corrupted or incomplete download. Download the archive again and verify it before you transfer or extract it.

For the supported download commands and credential-handling examples, see [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md#step-1-download-and-verify-the-release-archive).

## Transfer and extract the release

Move the archive and checksum into the restricted environment, then verify the checksum again on the orchestration node.

1. Transfer the archive and checksum to the orchestration node.
2. Verify the checksum in the release directory.
3. Confirm that the orchestration node has enough free space for both the archive and the extracted files.
4. Extract the archive into the directory used by your deployment.

For release 1.0.1, the extracted content includes the platform files and security content bundles. The CTI database is delivered separately and must be imported after installation when your deployment requires it.

Use the following command after replacing the release directory with your own path:

```bash
tar -xvf sekoia-self-hosted-v1.0.1.tar.gz -C "$SEKOIA_LOCAL_DIR"
```

Keep the directory layout expected by the SHC unless you also change the corresponding paths in `config.yml`. See [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md#step-2-transfer-and-extract-the-archive) for the archive layout.

## Configure offline delivery

Tell the SHC to use the files already present on the orchestration node instead of requesting them from the Sekoia delivery bucket.

1. Open `config.yml`.
2. Set `global.version.fetch.offline` to `true`.
3. Configure the customer-managed OCI registry.
4. Configure the customer-managed code registry.
5. Configure the cluster nodes, load balancer, DNS name, storage, and certificates.
6. Save the manifest.

The relevant offline setting is:

```yaml
global:
  version:
    fetch:
      offline: true
```

In air-gapped mode, release and security content download modules use the extracted files. Registry operations still point to the local registries that you define in the manifest.

For the complete configuration reference, see [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md).

## Load the SHC image

The SHC image is included in the release archive. Load it on the orchestration node before you run the controller.

1. Identify the SHC image archive under the extracted platform directory.
2. Load the image with Docker.
3. Confirm that the image is available locally.
4. Use the release execution script supplied with the archive.

The exact image filename is release-specific. Use the filename and execution instructions in [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md#step-3-load-the-self-hosted-controller-shc-docker-image).

## Validate the environment before installation

Run the SHC preflight checks before changing the nodes. These checks identify configuration, registry, release-file, tool, hardware, SSH, and network problems while the environment is still unchanged.

From the orchestration node, run the checks that apply to your deployment:

```bash
./run-shc.sh exec CheckLocalConfig
./run-shc.sh exec CheckLocalGit
./run-shc.sh exec CheckLocalOCIRegistry
./run-shc.sh exec CheckLocalReleaseFiles
./run-shc.sh exec CheckLocalTools
./run-shc.sh exec CheckNodePortReachability
./run-shc.sh exec CheckServerSpec
./run-shc.sh exec CheckServersAreReachable
```

Correct every blocking error before you continue. `CheckLocalConfig` reports missing fields, invalid formats, and unsupported keys without displaying rejected secret values.

For more detail about the execution plan and idempotent modules, see [The deployment process](/self_hosted/1.0.1/deployment/deployment_process.md).

## Install the platform

Use the bundle workflow when you want the SHC to run the installation stages in sequence. Use the step-by-step workflow when your restricted environment requires an approval or validation point between stages.

For the bundle workflow:

```bash
./run-shc.sh exec Install
```

Wait for the final convergence report. Warning messages can appear while the installation is still progressing. Treat the installation as complete when the command reports success and the post-deployment validation passes.

If the installation stops with an error, fix the reported cause and run the appropriate module again. SHC modules are designed to be rerun after a failure, except for destructive lifecycle commands documented separately.

## Validate the deployed platform

Run the post-deployment checks in order. Keep the command output as evidence that the platform passed validation.

### Check the Kubernetes nodes

Confirm that every node in the inventory joined the cluster and is ready.

```bash
./run-shc.sh exec CheckKubernetesCluster
```

The reported node count must match the number of hosts in your inventory. A six-node deployment, which is the minimum high-availability topology, should report six expected nodes.

### Check ArgoCD applications

Confirm that the platform applications are synchronized and healthy.

```bash
./run-shc.sh exec DebugArgoCD
```

Every application should report `Sync: Synced` and `Health: Healthy`. A short `Progressing` state can be normal immediately after deployment. Investigate `Degraded` or `OutOfSync` results before handing the platform to users.

### Check databases

Confirm that the database StatefulSets and clusters have the expected ready replicas.

```bash
./run-shc.sh exec DebugDatabases
```

All entries should report a healthy state with the expected number of ready replicas.

### Run platform diagnostics

Run the complete diagnostic set against the platform's Prometheus metrics.

```bash
./run-shc.sh exec Diagnostic
```

Every check must report `OK`. A `CRIT` or `WARN` result identifies the affected service or platform area and provides likely causes and remediation actions.

For targeted health checks and result interpretation, see [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md).

## Access the platform

After the validation checks pass, retrieve the platform access information and create the first administrator account.

1. Run `PlatformAccess` from the orchestration node if you need to display the generated credentials again.
2. Open the URL configured in `global.host`.
3. Follow [Set up the first administrator account](/self_hosted/1.0.1/operations/first_login.md).
4. Store generated credentials in an approved secrets store.
5. Remove credentials from shared logs before you provide logs to another team.

## Result

Sekoia Self-Hosted 1.0.1 is installed inside the restricted environment, with the release files delivered locally and the platform validated at the configuration, cluster, application, database, and service levels. The deployment team now has a repeatable record for future troubleshooting and operational reviews.

## Related articles

- [Sekoia Self-Hosted](/self_hosted/index.md): Overview of the deployment model and intended environments.
- [Sekoia Self-Hosted 1.0.1](/self_hosted/1.0.1/index.md): Quick-start path and release-specific documentation.
- [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md): Reference for infrastructure, hardware, storage, and software requirements.
- [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md): Reference for required network flows.
- [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md): How to prepare `config.yml`.
- [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md): Complete installation procedure for Sekoia Self-Hosted 1.0.1.
- [The deployment process](/self_hosted/1.0.1/deployment/deployment_process.md): Overview of SHC execution modes, modules, and installation stages.
- [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md): How to run and interpret platform health checks.
- [Debug your deployment](/self_hosted/1.0.1/troubleshooting/debug_tool.md): Reference for configuration, cluster, database, and resource diagnostics.
