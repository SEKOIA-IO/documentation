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
    ```

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

## Related links

- [Deploy the platform](./deployment_guide.md): Step-by-step installation instructions.
- [Deployment configuration reference](./deployment_configuration.md): Full `config.yml` parameter reference.
- [Debug your deployment](../troubleshooting/debug_tool.md): Full SHC debug command reference.
