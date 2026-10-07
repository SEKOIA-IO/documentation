# The deployment process

The self-hosted-controller (SHC) manages every phase of the Sekoia Self-Hosted platform lifecycle, from initial installation to day-to-day operations. It provides an interactive terminal user interface (TUI) for operators and a one-shot command-line interface (CLI) for scripts and unattended runs. This article explains how the SHC works, what commands it exposes, and how it handles different deployment environments.

## Core principles

The SHC is built on three design pillars.

**Preflight validation.** Before executing any change, the SHC runs a comprehensive set of checks: OS versions, network connectivity, configuration schema, local release directories, required tools, and repository access. Execution is blocked until every check passes.

**Declarative configuration.** The `config.yml` manifest is the single source of truth for the entire platform state: infrastructure settings (node IPs, load balancers, DNS), service configuration (SMTP, feature toggles), and scaling parameters (node counts, resource quotas). The SHC computes the difference between the actual and desired state and executes only the tasks required to converge.

**Idempotency.** Installation modules can be re-run safely. Existing artifacts and already-converged resources are skipped or reconciled, so the workflow can continue from where it left off. Destructive lifecycle commands, such as `PlatformScaleDown`, `PlatformDestroy`, `K3SUninstall`, `CleanupCilium`, and `WipeStorageDisks`, are exceptions and must be used only for their documented purpose.

## Execution modes

| Mode | Description | When to use |
| :--- | :--- | :--- |
| Online | The self-hosted-controller (SHC) downloads the release files and the latest security content bundles from Sekoia's S3 bucket. Requires internet access to `https://self-hosted.delivery.sekoia.io` and the `S3_ACCESS_KEY` and `S3_SECRET_KEY` credentials provided by Sekoia. Configured via `global.version.fetch` in `config.yml`, with `global.version.fetch.endpoint` set to the delivery endpoint. | Standard internet-connected deployments. |
| Air-gapped | The self-hosted-controller (SHC) operates in fully disconnected mode using the files extracted from the release archive. Requires `global.version.fetch.offline` set to `true`. All registry operations point to customer-managed repositories. | Restricted or classified environments with no external connectivity. |

## Available commands

Run `./run-shc.sh` without a command to open the TUI. Use it for streamed command output, installation progress, and live Machines, Kubernetes, Storage, and Diagnostics views. See [Use the SHC interface](../operations/controller_interface.md).

The SHC accepts the following commands, in the TUI and in one-shot CLI mode:

| Command | Description |
| :--- | :--- |
| `list` | Lists every module with a one-line description. |
| `exec <MODULE>` | Runs a module. |
| `exec <MODULE> --set KEY=VALUE` | Runs a module with a configuration value overridden for this run only. Repeat `--set` to override several values. |
| `help` | Displays the command reference. |
| `help <MODULE>` | Lists the configuration keys that the module accepts as `--set` overrides, with their default value and format. |
| `config help [PREFIX]` | Displays the configuration reference. See [Configure the deployment](./deployment_configuration.md#inspect-the-configuration-with-the-shc). |
| `config show [PREFIX]` | Displays the computed configuration. |

!!! note "Runtime overrides"
    A module accepts `--set` only for the keys it declares. To see them, run `help <MODULE>`. An override applies to the module and to the prerequisite modules it runs, and is never written to `config.yml`.

To display the full list of SHC modules, run:

```bash
list
```

??? example "Example output"
    ```
    Name                          Function
    CheckKubernetesCluster        Check the Kubernetes cluster is reachable and all nodes are Ready
    CheckLocalConfig              Validate the local controller configuration file
    CheckLocalGit                 Verify connectivity and access to the git repository
    CheckLocalOCIRegistry         Verify push/pull/delete access to the OCI registry
    CheckLocalReleaseFiles        Verify that all release files are present on disk
    CheckLocalTools               Check presence of local binary tools
    CheckNodePortReachability     Check every node can reach the other nodes on the cluster ports (6443, etcd, cilium, intake)
    CheckS3Performance            Benchmark the S3 endpoint per worker node with warp and check thresholds
    CheckServerSpec               Check that servers meet hardware and OS requirements
    CheckServersAreReachable      Check SSH connectivity to all configured servers
    CleanupCilium                 Destructively remove Cilium networking on dedicated nodes after K3s is stopped
    CleanupHelmReleases           Remove pending, failed, or uninstalling Helm revision secrets
    DebugArgoCD                   Display ArgoCD status dashboard (repositories, root app, applications)
    DebugArgoCDSyncAll            Sync all ArgoCD applications (partial → restart operator → full sync)
    DebugDatabases                Report health of StatefulSets and CNPG Clusters in support namespace
    DebugKustomizeStacksTemplates Scan ArgoCD stacks for leftover template placeholders
    DebugMissingSecrets           Check SecretGenerator objects for missing or incomplete secrets
    DebugPlatformInstallation     Create a platform-installer pause job for debugging
    DebugResourceAllocation       Show per-pod RAM request vs actual usage, sorted by waste
    Diagnostic                    Run diagnostic checks on the self-hosted platform
    DownloadDataFiles             Download self-hosted data bundles from S3 to local storage
    DownloadReleaseFiles          Download release files from S3 to local storage
    E2ETester                     Inspect/control the e2etester cron deployment
    E2ETesterReports              Inspect/manage self-hosted e2etester reports
    GetKubeconfig                 Retrieve kubeconfig from the first K3s manager node
    GetServerStatus               Fetch live status (CPU/RAM/disk/load) for all servers, read-only
    HelmInstall                   Install Helm and deploy offline charts via Ansible
    ImportArangoCollection        Import one or more ArangoDB collections from S3 or a local directory (mirrors arango-export)
    Install                       Run the full installation workflow
    InstanceBootstrap             Bootstrap default storage and per-community Quickwit indexes
    K3SInstall                    Install a K3s cluster on managers and workers via Ansible
    K3SUninstall                  Uninstall K3s and remove Cilium networking on dedicated nodes via Ansible
    KubeCrashRecovery             Restart all pods in ordered namespace phases
    PlatformAccess                Display platform access credentials (URLs, users, passwords)
    PlatformConfigurationFile     Generate the platform-installer Helm values file
    PlatformDestroy               Irreversibly destroy the platform and wipe Ceph disks (requires both safety flags)
    PlatformInstallation          Run the platform installation via a single installer job
    PlatformScaleDown             Irreversibly delete non-protected namespaces and verify client volume release
    PushArgoStacks                Sync ArgoCD application stacks to the git repository
    PushCharts                    Push Helm chart archives to the OCI registry
    PushDataBundles               Push self-hosted data bundles to the OCI registry
    PushImages                    Push Docker image archives to the OCI registry
    RebootNodes                   Reboot all nodes in the inventory
    RunEventLoadTesting           Deploy/scale the offline event load generator (helm upgrade --install)
    ScaleServices                 Scale Deployments (e.g. ingest/sigma-workflow workers) to their configured replica count
    SyncArgoRootApp               Sync the ArgoCD root application and wait for completion
    SyncIntakeFormats             Sync the intake formats data bundle through ArgoCD
    SyncRulesCatalog              Sync the rules catalog data bundle through ArgoCD
    WipeStorageDisks              Wipe Ceph disks and Rook host state (requires modules.wipe_storage.enabled; K3s/Ceph stopped)
    ```

## The installation execution plan

The `Install` command runs every module below, in order, grouped into four stages. A stage starts only when the previous one completed. If a module fails, the installation stops on that module, so you can fix the cause and re-run `Install` without undoing the stages that already succeeded.

| Stage | Modules | What the stage does |
| :--- | :--- | :--- |
| `checks` | `CheckLocalConfig`, `CheckLocalGit`, `CheckLocalOCIRegistry`, `CheckLocalReleaseFiles`, `CheckServersAreReachable`, `CheckServerSpec`, `CheckLocalTools`, `CheckNodePortReachability` | Validates the configuration, the repositories, the local release directories, the controller tools, every node against the hardware, OS, storage, hostname, and time-sync requirements, and the network paths between nodes on the cluster ports. |
| `push` | `DownloadDataFiles`, `PushImages`, `PushCharts`, `PushDataBundles`, `PushArgoStacks` | Resolves the security content bundles, then publishes the images, the charts, the detection rules and intake formats bundles, and the ArgoCD stacks to your local repositories. |
| `kubernetes` | `K3SInstall`, `GetKubeconfig`, `HelmInstall`, `CheckKubernetesCluster` | Installs the K3s cluster and the cluster services, then verifies that every node is `Ready`. |
| `platform` | `PlatformConfigurationFile`, `PlatformInstallation`, `SyncRulesCatalog`, `SyncIntakeFormats`, `PlatformAccess`, `InstanceBootstrap`, `ScaleServices` | Renders the installer values, runs the platform installer, deploys the detection rules catalog and the intake formats, returns the access credentials, provisions the default storage and ExaLog indexes, and scales the workers to their target replica count. |

### Automatic prerequisites and repeated modules

Some modules invoke their prerequisites every time they run. Consequently, the log contains more module executions than the four-stage table:

- Each of `PushImages`, `PushCharts`, and `PushArgoStacks` invokes `DownloadReleaseFiles` first, and `PushDataBundles` invokes `DownloadDataFiles` first.
- `HelmInstall`, `PlatformInstallation`, `PlatformAccess`, `DebugPlatformInstallation`, `DebugMissingSecrets`, and `CheckS3Performance` first run `CleanupHelmReleases`, which retrieves a current kubeconfig. See [Interrupted Helm operations](#interrupted-helm-operations).
- `PlatformInstallation`, `PlatformAccess`, `DebugPlatformInstallation`, and `DebugMissingSecrets` also regenerate the platform configuration before running.
- `SyncRulesCatalog` and `SyncIntakeFormats` each run `SyncArgoRootApp` first, so the ArgoCD root application applies the latest application definitions before the content synchronization.
- `CheckKubernetesCluster`, `InstanceBootstrap`, `ScaleServices`, and the `Debug` modules that read the cluster retrieve a current kubeconfig before running.

A prerequisite runs again every time a module needs it, and its failure stops the module that depends on it.

These repeated executions are expected. They ensure that a module also works when you run it directly instead of through `Install`.

Artifact operations are also cache-aware. `DownloadReleaseFiles` skips files already present, `PushImages` skips images already available in the target registry, and `PushArgoStacks` does not create a commit when the generated manifests are unchanged. These outcomes indicate successful convergence, not an incomplete installation.

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
| Graceful node reboot | `RebootNodes` |
| Recover from a node crash or cluster restart | `KubeCrashRecovery` |
| Live node resource usage | `GetServerStatus` |
| Service health check per platform area | `Diagnostic` |
| Object storage performance benchmark | `CheckS3Performance` |
| Clean up interrupted Helm operations | `CleanupHelmReleases` |
| Redeploy the detection rules catalog and the intake formats | `SyncRulesCatalog`, `SyncIntakeFormats` |
| Delete the platform workloads and keep the cluster | `PlatformScaleDown`. See [Reset or destroy the platform](../operations/reset_platform.md). |
| Destroy the platform and wipe the storage disks | `PlatformDestroy`. See [Reset or destroy the platform](../operations/reset_platform.md). |

## Related links

- [Deploy the platform](./deployment_guide.md): Step-by-step installation instructions.
- [Configure the deployment](./deployment_configuration.md): Starter configuration and required-field reference.
- [Debug your deployment](../troubleshooting/debug_tool.md): Full SHC debug command reference.
- [Use the SHC interface](../operations/controller_interface.md): The interactive interface of the SHC.
- [Run platform diagnostics](../monitoring/run_diagnostics.md): Targeted Prometheus health checks per platform area.
