# The deployment process

The Self-Hosted Controller (SHC) is the orchestration CLI that manages every phase of the Sekoia Self-Hosted platform lifecycle, from initial installation to day-to-day operations. This article explains how the SHC works, what commands it exposes, and how it handles different deployment environments.

## Core principles

The SHC is built on three design pillars.

**Preflight validation.** Before executing any change, the SHC runs a comprehensive set of checks: OS versions, network connectivity, configuration schema, file checksums, and repository access. Execution is blocked until every check passes.

**Declarative configuration.** The `config.yml` manifest is the single source of truth for the entire platform state: infrastructure settings (node IPs, load balancers, DNS), service configuration (SMTP, feature toggles), and scaling parameters (node counts, resource quotas). The SHC computes the difference between the actual and desired state and executes only the tasks required to converge.

**Idempotency.** Every SHC command can be re-run safely. If a step already completed successfully, the SHC skips it and continues from where it left off.

## Execution modes

| Mode | Description | When to use |
| :--- | :--- | :--- |
| Online | The SHC fetches release artifacts from Sekoia's authorized S3 bucket. Requires internet access. Configured via `global.version.fetch` in `config.yml`. | Standard internet-connected deployments. |
| Air-gapped | The SHC operates in fully disconnected mode using a pre-staged release archive and locally cached manifests. All registry operations point to customer-managed repositories. | Restricted or classified environments with no external connectivity. |

## Available commands

To display the full list of SHC commands and their descriptions, run:

```bash
./run-shc.sh list
```

??? example "Example output"
    ```
    Available commands:

      Install                       Run the full installation workflow
      DownloadReleaseFiles          Download release files from S3 to local storage

      CheckLocalConfig              Validate the local controller configuration file
      CheckLocalGit                 Verify connectivity and access to the git repository
      CheckLocalOCIRegistry         Verify push/pull/delete access to the OCI registry
      CheckLocalReleaseFiles        Verify that all release files are present on disk
      CheckServersAreReachable      Check SSH connectivity to all configured servers
      CheckServerSpec               Check that servers meet hardware and OS requirements
      CheckKubernetesCluster        Check the Kubernetes cluster is reachable and all nodes are Ready
      GetServerStatus               Fetch live status (CPU/RAM/disk/load) for all servers, read-only

      ConfigureServersWithAnsible   Configure servers using Ansible playbooks
      PushImages                    Push Docker image archives to the OCI registry
      PushCharts                    Push Helm chart archives to the OCI registry
      PushArgoStacks                Sync ArgoCD application stacks to the git repository

      K3SInstall                    Install a K3s cluster on managers and workers via Ansible
      K3SUninstall                  Uninstall K3s from all nodes via Ansible
      GetKubeconfig                 Retrieve kubeconfig from the first K3s manager node
      HelmInstall                   Install Helm and deploy offline charts via Ansible

      PlatformConfigurationFile     Generate the platform-installer Helm values file
      PlatformInstallation          Run the platform installation via a single installer job
      PlatformAccess                Display platform access credentials (URLs, users, passwords)
      InstanceBootstrap             Bootstrap default storage and per-community Quickwit indexes
      ScaleServices                 Scale Deployments to their configured replica count

      RebootNodes                   Reboot all nodes in the inventory
      KubeCrashRecovery             Restart all pods in ordered namespace phases
      WipeStorageDisks              Wipe disks previously used by Ceph (requires modules.wipe_storage.enabled)

      DebugArgoCD                   Display ArgoCD status dashboard (repositories, root app, applications)
      DebugArgoCDSyncAll            Sync all ArgoCD applications (partial → restart operator → full sync)
      DebugDatabases                Report health of StatefulSets and CNPG Clusters in support namespace
      DebugResourceAllocation       Show per-pod RAM request vs actual usage, sorted by waste
      DebugMissingSecrets           Check SecretGenerator objects for missing or incomplete secrets
      DebugKustomizeStacksTemplates Scan ArgoCD stacks for leftover template placeholders
      DebugPlatformInstallation     Create a platform-installer pause job for debugging
      Diagnostic                    Run diagnostic checks on the self-hosted platform
    ```

## The installation execution plan

The `Install` command runs every module below, in order, grouped into five stages. A stage starts only when the previous one completed. If a module fails, the installation stops on that module, so you can fix the cause and re-run `Install` without undoing the stages that already succeeded.

| Stage | Modules | What the stage does |
| :--- | :--- | :--- |
| `checks` | `CheckLocalConfig`, `CheckLocalGit`, `CheckLocalOCIRegistry`, `CheckLocalReleaseFiles`, `CheckServersAreReachable`, `CheckServerSpec` | Validates the configuration, the repositories, the local artifacts, and every node against the hardware, OS, storage, hostname, and time-sync requirements. |
| `server_config` | `ConfigureServersWithAnsible` | Prepares the operating system and installs the required packages on all nodes. |
| `push` | `PushImages`, `PushCharts`, `PushArgoStacks` | Publishes the images, the charts, and the ArgoCD stacks to your registries. |
| `kubernetes` | `K3SInstall`, `GetKubeconfig`, `HelmInstall`, `CheckKubernetesCluster` | Installs the K3s cluster and the cluster services, then verifies that every node is `Ready`. |
| `platform` | `PlatformConfigurationFile`, `PlatformInstallation`, `PlatformAccess`, `InstanceBootstrap`, `ScaleServices` | Renders the installer values, runs the platform installer, returns the access credentials, provisions the default storage and Quickwit indexes, and scales the workers to their target replica count. |

### Post-installation bootstrap

The last two modules of the `platform` stage bring a freshly-installed region into a usable state. Both are idempotent, so you can re-run them on their own.

`InstanceBootstrap` provisions the storage layer the platform needs before it can write events:

1. Declares the default storage backend on the `communityapi` deployment in the `common` namespace.
2. Reconciles the per-community Quickwit indexes and their Kafka sources on the `storage-manager` deployment in the `sic` namespace.

On a new region the Quickwit metastore holds no index, so without this step the indexers stay idle and never write to your S3 bucket.

`ScaleServices` then scales the ingestion and detection Deployments (for example `ingestworker1` and `sigma-workflow-worker1`) to their configured replica count. Deployments already at their target count are left untouched. The module runs last so the workers start consuming only once the storage layer is ready.

## Lifecycle operations

The SHC handles the full platform lifecycle beyond initial installation.

| Operation | SHC command |
| :--- | :--- |
| Post-deployment health check | `CheckKubernetesCluster`, `DebugArgoCD` |
| Database diagnostics | `DebugDatabases` |
| Resource usage analysis | `DebugResourceAllocation` |
| Platform configuration re-apply | `PlatformConfigurationFile`, `PlatformInstallation` |
| Full ArgoCD re-synchronization | `DebugArgoCDSyncAll` |
| Graceful node reboot | `RebootNodes` |
| Recover from a node crash or cluster restart | `KubeCrashRecovery` |
| Live node resource usage | `GetServerStatus` |
| Service health check per platform area | `Diagnostic` |

## Related links

- [Deploy the platform](./deployment_guide.md): Step-by-step installation instructions.
- [Deployment configuration reference](./deployment_configuration.md): Full `config.yml` parameter reference.
- [Debug your deployment](../troubleshooting/debug_tool.md): Full SHC debug command reference.
- [Use the controller interface](../operations/controller_interface.md): The interactive interface of the SHC.
- [Run platform diagnostics](../monitoring/run_diagnostics.md): Targeted Prometheus health checks per platform area.
