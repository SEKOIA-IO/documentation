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

      Install                       Run the full installation workflow (bundle)
      CheckRequiredConfigItems      Validate the configuration file schema
      CheckLocalGit                 Test Git repository access (push and pull)
      CheckLocalOCIRegistry         Test OCI registry access (push, pull, and delete)
      CheckLocalReleaseFiles        Verify release files are present on disk
      CheckServersAreReachable      Test SSH connectivity to all inventory nodes
      CheckServerSpec               Validate node hardware meets minimum requirements
      CheckKubernetesCluster        Verify all K8s nodes are Ready
      CheckLocalConfig              Validate config.yml against the schema
      PushImages                    Push Docker images to the local registry
      PushCharts                    Push Helm charts to the local registry
      PushArgoStacks                Push ArgoCD manifests to the Git repository
      K3SInstall                    Install K3s on all inventory nodes
      GetKubeconfig                 Retrieve the cluster kubeconfig
      HelmInstall                   Deploy Helm charts to the cluster
      sekoia                        Deploy the Sekoia platform via ArgoCD sync
      DebugArgoCD                   Display ArgoCD application status dashboard
      DebugArgoCDSyncAll            Force re-synchronization of all ArgoCD apps
      DebugDatabases                Inspect database pod health
      DebugResourceAllocation       Report memory allocation vs. actual usage
      DebugMissingSecrets           Audit missing or incomplete Kubernetes secrets
      DebugKustomizeStacksTemplates Scan ArgoCD stacks for unrendered placeholders
      DebugPlatformInstallation     Launch a paused installer job for debugging
      diagnose                      Generate a diagnostic bundle for support
    ```

## Lifecycle operations

The SHC handles the full platform lifecycle beyond initial installation.

| Operation | SHC command |
| :--- | :--- |
| Post-deployment health check | `CheckKubernetesCluster`, `DebugArgoCD` |
| Database diagnostics | `DebugDatabases` |
| Resource usage analysis | `DebugResourceAllocation` |
| Platform configuration re-apply | `sekoia` |
| Full ArgoCD re-synchronization | `DebugArgoCDSyncAll` |
| Diagnostic bundle for support | `diagnose` |

## Related links

- [Deploy the platform](./deployment_guide.md): Step-by-step installation instructions.
- [Deployment configuration reference](./deployment_configuration.md): Full `config.yml` parameter reference.
- [Debug your deployment](../troubleshooting/debug_tool.md): Full SHC debug command reference.
