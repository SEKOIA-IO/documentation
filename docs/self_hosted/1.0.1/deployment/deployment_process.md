# The deployment process

The self-hosted-controller (SHC) manages every phase of the Sekoia Self-Hosted platform lifecycle, from initial installation to day-to-day operations. It provides an interactive terminal user interface (TUI) for operators and a one-shot command-line interface (CLI) for scripts and unattended runs. This article explains how the SHC works, what commands it exposes, and how it handles different deployment environments.

## Core principles

The SHC is built on three design pillars.

**Preflight validation.** Before it changes the nodes, the `Install` command runs a set of checks: configuration schema, repository access, local release directories, SSH access, OS versions and hardware, required tools, and network paths between the nodes. Every module of the `checks` stage is blocking: the installation stops at the first check that fails. `CheckLocalConfig` validates the required keys, the value formats, and the key names, but it does not validate the optional settings your environment needs, so some configuration errors only appear in later stages. For example, when backups are enabled, a missing backup encryption key is reported by `PlatformConfigurationFile` in the `platform` stage.

**Declarative configuration.** The `config.yml` manifest is the single source of truth for the entire platform state: infrastructure settings (node IPs, load balancers, DNS), service configuration (SMTP, feature toggles), and scaling parameters (node counts, resource quotas). Each run converges the platform to this declared state.

**Idempotency.** Installation modules can be re-run safely. Existing artifacts and already-converged resources are skipped or reconciled, so you can run `Install` again after a failure without undoing the work already completed. See [Resume after a failure](#resume-after-a-failure). Destructive lifecycle commands, such as `PlatformScaleDown`, `PlatformDestroy`, `K3SUninstall`, `CleanupCilium`, and `WipeStorageDisks`, are exceptions and must be used only for their documented purpose. See [Commands that need care](#commands-that-need-care).

## Execution modes

| Mode | Description | When to use |
| :--- | :--- | :--- |
| Online | The self-hosted-controller (SHC) downloads the release files and the latest security content bundles from Sekoia's S3 bucket. Requires internet access to `https://self-hosted.delivery.sekoia.io` and the `S3_ACCESS_KEY` and `S3_SECRET_KEY` credentials provided by Sekoia. Configured via `global.version.fetch` in `config.yml`, with `global.version.fetch.endpoint` set to the delivery endpoint. | Standard internet-connected deployments. |
| Air-gapped | The self-hosted-controller (SHC) operates in fully disconnected mode using the files extracted from the release archive. Requires `global.version.fetch.offline` set to `true`. All registry operations point to customer-managed repositories. | Restricted or classified environments with no external connectivity. |

## Available commands

Run `./run-shc.sh` without a command to open the TUI. Use it for streamed command output, installation progress, and live Machines, Kubernetes, Storage, and Diagnostics views. See [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md).

The SHC accepts the following commands, in the TUI and in one-shot CLI mode:

| Command | Description |
| :--- | :--- |
| `list` | Lists every module with a one-line description. |
| `exec <MODULE>` | Runs a module. |
| `exec <MODULE> -m <METHOD>` | Runs another method of a module, for example `exec Backups -m run_now`. |
| `exec <MODULE> --set KEY=VALUE` | Runs a module with a configuration value overridden for this run only. Repeat `--set` to override several values. |
| `help` | Displays the command reference. |
| `help <MODULE>` | Lists the configuration keys that the module accepts as `--set` overrides, with their default value and format. |
| `config help [PREFIX]` | Displays the configuration reference. See [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md#inspect-the-configuration-with-the-shc). |
| `config show [PREFIX]` | Displays the computed configuration. |

!!! note "Runtime overrides"
    A module accepts `--set` only for the keys it declares. To see them, run `help <MODULE>`. An override applies to the module and to the prerequisite modules it runs, and is never written to `config.yml`. The values `on`, `off`, `yes`, and `no` stay text values: a boolean key accepts only `true` or `false`.

To display the list of SHC modules, run:

```bash
list
```

??? example "Example output"
    ```text
    Name                           Function
    Backups                        Check (-m status) or trigger (-m run_now) Vault, PostgreSQL, ArangoDB and ClickHouse backups
    CheckKubernetesCluster         Check the Kubernetes cluster is reachable and all nodes are Ready
    CheckLocalConfig               Validate the local controller configuration file
    CheckLocalGit                  Verify connectivity and access to the git repository
    CheckLocalOCIRegistry          Verify push/pull/delete access to the OCI registry
    CheckLocalReleaseFiles         Verify that all release files are present on disk
    CheckLocalTools                Check presence of local binary tools
    CheckNodePortReachability      Check every node can reach the other nodes on the cluster ports (6443, etcd, cilium, intake)
    CheckS3Performance             Benchmark the S3 endpoint per worker node with warp and check thresholds
    CheckServerSpec                Check that servers meet hardware and OS requirements
    CheckServersAreReachable       Check SSH connectivity to all configured servers
    CleanupCilium                  Destructively remove Cilium networking on dedicated nodes after K3s is stopped
    CleanupHelmReleases            Remove pending, failed, or uninstalling Helm revision secrets
    DebugArgoCD                    Display ArgoCD status dashboard (repositories, root app, applications)
    DebugArgoCDSyncAll             Sync all ArgoCD applications (partial → restart operator → full sync)
    DebugDatabases                 Report health of StatefulSets and CNPG Clusters in support namespace
    DebugMissingSecrets            Check SecretGenerator objects for missing or incomplete secrets
    DebugResourceAllocation        Show per-pod RAM request vs actual usage, sorted by waste
    Diagnostic                     Run diagnostic checks on the self-hosted platform
    DownloadDataFiles              Download self-hosted data bundles from S3 to local storage
    DownloadReleaseFiles           Download release files from S3 to local storage
    GetKubeconfig                  Retrieve kubeconfig from the first K3s manager node
    GetServerStatus                Fetch live status (CPU/RAM/disk/load) for all servers, read-only
    HelmInstall                    Install Helm and deploy offline charts via Ansible
    ImportArangoCollection         Import one or more ArangoDB collections from S3 or a local directory (mirrors arango-export)
    Install                        Run the full installation workflow
    InstanceBootstrap              Bootstrap default storage and per-community Quickwit indexes
    K3SInstall                     Install a K3s cluster on managers and workers via Ansible
    K3SUninstall                   Uninstall K3s and remove Cilium networking on dedicated nodes via Ansible
    KubeCrashRecovery              Restart all pods in ordered namespace phases
    PlatformAccess                 Display platform access credentials (URLs, users, passwords)
    PlatformConfigurationFile      Generate the platform-installer Helm values file
    PlatformDestroy                Irreversibly destroy the platform (requires modules.platform_scale_down.enabled; auto-mode Ceph disk wiping also requires modules.wipe_storage.enabled)
    PlatformInstallation           Run the platform installation via a single installer job
    PlatformScaleDown              Irreversibly delete non-protected namespaces and verify client volume release
    PushArgoStacks                 Sync ArgoCD application stacks to the git repository
    PushCharts                     Push Helm chart archives to the OCI registry
    PushDataBundles                Push self-hosted data bundles to the OCI registry
    PushImages                     Push Docker image archives to the OCI registry
    RebootNodes                    Reboot all nodes in the inventory
    RestartAllMicroservices        Restart all marked microservices and wait for their rollouts, leaving databases running
    ScaleServices                  Scale Deployments (e.g. ingest/sigma-workflow workers) to their configured replica count
    SyncArgoRootApp                Sync the ArgoCD root application and wait for completion
    SyncIntakeFormats              Sync the intake formats data bundle through ArgoCD
    SyncRulesCatalog               Sync the rules catalog data bundle through ArgoCD
    UpdatePlatformData             Update intake formats and rules catalog data releases
    WipeStorageDisks               Wipe auto-mode Ceph disks and Rook host state (requires modules.wipe_storage.enabled; K3s/Ceph stopped)
    ```

ExaLog, the event storage and search capability, runs on Quickwit. Some module names, logs, and configuration keys keep the `quickwit` name, such as the `InstanceBootstrap` description above.

### Commands that need care

The following commands delete data, interrupt the service, or exist for Sekoia support. Run a destructive or disruptive command only for its documented purpose, and a support-only command only when Sekoia support asks you to.

| Command | Category | Effect |
| :--- | :--- | :--- |
| `PlatformDestroy` | Destructive | Deletes the platform workloads, uninstalls K3s, and wipes the Ceph disks. Everything stored on Ceph is lost. Requires `modules.platform_scale_down.enabled` and, in `auto` storage mode, `modules.wipe_storage.enabled`. See [Reset or destroy the platform](/self_hosted/1.0.1/operations/reset_platform.md). |
| `PlatformScaleDown` | Destructive | Deletes the platform namespaces and the platform data stored in the cluster, and keeps the Kubernetes cluster. Requires `modules.platform_scale_down.enabled`. See [Reset or destroy the platform](/self_hosted/1.0.1/operations/reset_platform.md). |
| `WipeStorageDisks` | Destructive | Wipes the Ceph disks and the Rook host state of every node. Requires `modules.wipe_storage.enabled`, with K3s and Ceph stopped. |
| `K3SUninstall` | Destructive | Uninstalls K3s and removes the Cilium networking from every node. It requires no safety flag. |
| `CleanupCilium` | Destructive | Removes the Cilium networking from nodes where K3s is stopped. It requires no safety flag. |
| `RestartAllMicroservices` | Disruptive | Restarts every microservice and waits for the rollouts. The databases keep running. |
| `RebootNodes` | Disruptive | Reboots the nodes of the inventory without draining them first. |
| `KubeCrashRecovery` | Disruptive | Restarts every pod, namespace by namespace. |
| `CheckS3Performance` | Disruptive, support only | Generates a sustained load on your S3-compatible storage and creates `warp-preflight-*` benchmark buckets on it, which it does not delete. |

## The installation execution plan

The `Install` command runs every module below, in order, grouped into four stages. A stage starts only when the previous one completed. If a module fails, the installation stops on that module. See [Resume after a failure](#resume-after-a-failure).

| Stage | Modules | What the stage does |
| :--- | :--- | :--- |
| `checks` | `CheckLocalConfig`, `CheckLocalGit`, `CheckLocalOCIRegistry`, `DownloadReleaseFiles`, `CheckLocalReleaseFiles`, `CheckServersAreReachable`, `CheckServerSpec`, `CheckLocalTools`, `CheckNodePortReachability` | Validates the configuration and the repositories, downloads the release files in online mode, then validates the local release directories, the controller tools, every node against the hardware, OS, storage, hostname, and time-sync requirements, and the network paths between nodes on the cluster ports. |
| `push` | `DownloadDataFiles`, `PushImages`, `PushDataBundles` | Resolves the security content bundles, then publishes the images and the detection rules and intake formats bundles to your local OCI registry. |
| `kubernetes` | `K3SInstall`, `GetKubeconfig`, `HelmInstall`, `CheckKubernetesCluster` | Installs the K3s cluster and the cluster services, then verifies that every node is `Ready`. |
| `platform` | `PushArgoStacks`, `PlatformConfigurationFile`, `PlatformInstallation`, `SyncRulesCatalog`, `SyncIntakeFormats`, `PlatformAccess`, `InstanceBootstrap`, `ScaleServices` | Publishes the Helm charts and the ArgoCD stacks to your local repositories, renders the installer values, runs the platform installer, deploys the detection rules catalog and the intake formats, returns the access credentials, provisions the default storage and ExaLog indexes, and scales the workers to their target replica count. |

`DownloadReleaseFiles` runs in the `checks` stage. In online mode, it downloads the release files from the Sekoia S3 bucket, so missing or invalid bucket credentials fail the installation at this point. In air-gapped mode, it uses the files extracted from the archive. `PushArgoStacks` runs after the cluster is installed, because it retrieves the cluster credentials and synchronizes the ArgoCD root application when it already exists.

### Automatic prerequisites and repeated modules

Some modules invoke their prerequisites every time they run. Consequently, the log contains more module executions than the four-stage table:

- `PushImages` and `PushCharts` invoke `DownloadReleaseFiles` first, and `PushDataBundles` invokes `DownloadDataFiles` first.
- `PushArgoStacks` runs `PushCharts` to publish the Helm charts, then retrieves a current kubeconfig, before it publishes the stacks.
- `HelmInstall`, `PlatformInstallation`, `PlatformAccess`, `DebugMissingSecrets`, and `CheckS3Performance` first run `CleanupHelmReleases`, which retrieves a current kubeconfig. See [Interrupted Helm operations](#interrupted-helm-operations).
- `PlatformInstallation`, `PlatformAccess`, and `DebugMissingSecrets` also regenerate the platform configuration before running.
- `SyncRulesCatalog` and `SyncIntakeFormats` each run `SyncArgoRootApp` first, so the ArgoCD root application applies the latest application definitions before the content synchronization.
- `CheckKubernetesCluster`, `Diagnostic`, `InstanceBootstrap`, `ScaleServices`, and the other modules that read the cluster retrieve a current kubeconfig before running.

A prerequisite runs again every time a module needs it, and its failure stops the module that depends on it. `DownloadReleaseFiles`, `DownloadDataFiles`, and `GetKubeconfig` are the exceptions: as prerequisites, they are skipped for 300 seconds after a successful run in the same SHC session, which is one CLI command or one TUI session. When you run them directly, they always run.

These repeated executions are expected. They ensure that a module also works when you run it directly instead of through `Install`.

By default, repeated runs publish the artifacts again. In online mode, `DownloadReleaseFiles` downloads every release file again and removes the local files that are no longer part of the release. In air-gapped mode, it makes no download. `PushImages` and `PushCharts` push every image and chart again, and `PushArgoStacks` does not create a commit when the generated manifests are unchanged. These outcomes indicate successful convergence, not an incomplete installation.

### Resume after a failure

When a module fails, `Install` stops on that module and the log reports `Install.start terminated` with `success=False`. Nothing is rolled back: the work of the modules that completed is kept.

To resume the installation:

1. Fix the cause reported in the log.
2. Run `exec Install` again, or run the failed module alone with `exec <MODULE>`, then the next modules of the plan in order, as in the [step-by-step deployment](/self_hosted/1.0.1/deployment/deployment_guide.md#option-2-step-by-step-deployment).

`Install` always starts again from the `checks` stage. On nodes where K3s already runs, `CheckServerSpec` skips its port and storage disk checks, `CheckNodePortReachability` is skipped once every node runs K3s, and `K3SInstall` does not reinstall K3s.

A failed `PlatformInstallation` removes its installer job and the `shpi-*` Helm releases in the `sekoia-system` namespace, and keeps the components that the installer already deployed. Run again, it starts the platform installer from its first step and skips the components that are already up to date. When you run `PlatformInstallation` alone, run the remaining modules of the `platform` stage after it, in order: `SyncRulesCatalog`, `SyncIntakeFormats`, `PlatformAccess`, `InstanceBootstrap`, and `ScaleServices`.

### Interrupted Helm operations

An installation interrupted during a Helm operation leaves the Helm release in a `pending-install`, `pending-upgrade`, `pending-rollback`, `failed`, or `uninstalling` state, which blocks the next Helm operation on that release. `CleanupHelmReleases` deletes these revision records in every namespace before each module that runs Helm. The deployed and superseded revisions and the resources created by the charts are preserved.

!!! warning "Run it only when no Helm operation is in progress"
    `CleanupHelmReleases` also deletes the record of a Helm operation that is still running. Do not run a module that depends on it while another SHC session is installing or upgrading the platform.

### Post-installation bootstrap

The last two modules of the `platform` stage bring a freshly-installed region into a usable state. Both are idempotent, so you can re-run them on their own.

`InstanceBootstrap` provisions the storage layer the platform needs before it can write events:

1. Declares the default storage backend on the `communityapi` deployment in the `common` namespace.
2. Reconciles the per-community ExaLog indexes and their Kafka sources on the `storage-manager` deployment in the `sic` namespace.

On a new region ExaLog has no index, so without this step the indexers stay idle and never write to your S3-compatible storage.

`ScaleServices` then scales the ingestion and detection Deployments (for example `ingestworker1` and `sigma-workflow-worker1`) to their configured replica count. Deployments already at their target count are left untouched. The module runs last so the workers start consuming only once the storage layer is ready.

## Lifecycle operations

The SHC handles the full platform lifecycle beyond initial installation.

| Operation | self-hosted-controller (SHC) command |
| :--- | :--- |
| Post-deployment health check | `CheckKubernetesCluster`, `DebugArgoCD` |
| Database diagnostics | `DebugDatabases` |
| Resource usage analysis | `DebugResourceAllocation` |
| Platform configuration re-apply | `PlatformConfigurationFile`, `PlatformInstallation` |
| Full ArgoCD re-synchronization | `DebugArgoCDSyncAll` |
| Cold restart of the whole cluster, with a full outage | `RebootNodes`, then `KubeCrashRecovery`. See [Run a cold restart of the whole cluster](/self_hosted/1.0.1/operations/node_maintenance.md#run-a-cold-restart-of-the-whole-cluster). |
| Restart every pod after a crash of several nodes, with a full outage | `KubeCrashRecovery`. See [KubeCrashRecovery](/self_hosted/1.0.1/troubleshooting/debug_tool.md#kubecrashrecovery). |
| Live node resource usage | `GetServerStatus` |
| Service health check per platform area | `Diagnostic` |
| Import the CTI database | `ImportArangoCollection`. See [Import the CTI database](/self_hosted/1.0.1/operations/import_cti_database.md). |
| Check or trigger the backups | `Backups`. See [Back up the platform](/self_hosted/1.0.1/operations/backups.md). |
| Update the detection rules and the intake formats | `UpdatePlatformData`. See [Update the security content](/self_hosted/1.0.1/operations/update_security_content.md). |
| Rotate the platform certificate or credentials | `PlatformConfigurationFile`, `PlatformInstallation`, `RestartAllMicroservices`. See [Rotate the certificate and credentials](/self_hosted/1.0.1/operations/rotate_certificate_and_credentials.md). |
| Object storage performance benchmark, at the request of Sekoia support | `CheckS3Performance` |
| Clean up interrupted Helm operations | `CleanupHelmReleases` |
| Redeploy the detection rules catalog and the intake formats | `SyncRulesCatalog`, `SyncIntakeFormats` |
| Delete the platform workloads and keep the cluster | `PlatformScaleDown`. See [Reset or destroy the platform](/self_hosted/1.0.1/operations/reset_platform.md). |
| Destroy the platform and wipe the storage disks | `PlatformDestroy`. See [Reset or destroy the platform](/self_hosted/1.0.1/operations/reset_platform.md). |

## Related links

- [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md): Step-by-step installation instructions.
- [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md): Starter configuration and required-field reference.
- [Debug your deployment](/self_hosted/1.0.1/troubleshooting/debug_tool.md): Full SHC debug command reference.
- [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md): The interactive interface of the SHC.
- [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md): Targeted Prometheus health checks per platform area.
