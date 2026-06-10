# Debug your deployment

The Self-Hosted Controller (SHC) provides a set of diagnostic commands that let you validate configuration, inspect cluster health, audit secrets, diagnose database issues, and analyse resource usage. This article is a full reference for those commands, including expected outputs and remediation steps.

All commands are executed from the **orchestration node** using the `exec` subcommand:

```bash
./run-shc.sh exec <COMMAND>
```

## Configuration validation

### CheckLocalConfig

Validates every key in your `config.yml` against the SHC schema.

```bash
./run-shc.sh exec CheckLocalConfig
```

The check reports:

- Missing required fields.
- Values that do not match the expected format or regex.

??? example "Expected output (no errors)"
    ```
    Validating configuration...
    Configuration is valid entries_checked=42
    ```

??? example "Example failure output"
    ```
    Missing required config key=global.version.platform.version
    Format mismatch key=utils.oci_registry.url value=registry.lab expected_format=^https?://
    Configuration validation failed: 2 error(s) found
    ```

**What to do after a failure:** Review each error line. Add any missing required keys to `config.yml`. Fix values that do not match the expected format, for example a URL missing the `https://` scheme.

To inspect all resolved environment variable values before the schema check runs, add the `-v` flag:

```bash
./run-shc.sh -v exec CheckLocalConfig
```

The verbose output includes the fully resolved in-memory config tree, including every `env.VAR_NAME` value substituted with its actual content. Use this to confirm that secrets injected via environment variables are correctly loaded.

## Infrastructure connectivity

### CheckServersAreReachable

Tests SSH connectivity to all nodes listed in `utils.ansible.inventory`.

```bash
./run-shc.sh exec CheckServersAreReachable
```

??? example "Expected output"
    ```
    Pinging all configured servers via Ansible...
    All configured servers are reachable
    ```

**What to do after a failure:**

- Verify the SSH key path in `utils.ansible.ssh-key` is correct and exported in your environment.
- Confirm the target node is running and reachable from the orchestration node on TCP port 22.
- Verify the username in `utils.ansible.user` has SSH access to the node.
- If you use password-based sudo, confirm `SERVERS_SUDO_PASSWORD` is set correctly.

### CheckKubernetesCluster

Connects to the Kubernetes API and verifies that every node has a `Ready=True` condition and that the actual node count matches your Ansible inventory.

```bash
./run-shc.sh exec CheckKubernetesCluster
```

??? example "Expected output"
    ```
    Kubernetes cluster is healthy nodes=6 expected=6
    ```

**What to do after a failure:**

- Run `kubectl get nodes` to identify which nodes are not `Ready`.
- Run `kubectl describe node <node-name>` and look for taints, conditions, or resource pressure.
- Check K3s system logs on the failing node: `journalctl -u k3s -n 100`.

## Local artifact checks

### CheckLocalReleaseFiles

Verifies that every asset declared under `global.version` exists in the expected directory on the orchestration node.

```bash
./run-shc.sh exec CheckLocalReleaseFiles
```

**What to do after a failure:** Confirm that the release archive was fully extracted and that `global.version.platform.path` points to the correct directory.

### CheckLocalGit

Clones the repository configured in `utils.git.repo_url` and tests both pull and push access.

```bash
./run-shc.sh exec CheckLocalGit
```

**What to do after a failure:**

- Verify `GIT_HTTP_USERNAME` and `GIT_HTTP_PASSWORD` are set correctly.
- Confirm the repository exists and is reachable from the orchestration node.
- Ensure the user has both read and write permissions on the repository.

### CheckLocalOCIRegistry

Tests push, pull, and delete access to your OCI registry. If push fails, pull and delete are skipped and reported as untested.

```bash
./run-shc.sh exec CheckLocalOCIRegistry
```

**What to do after a failure:**

- Verify `REGISTRY_USERNAME` and `REGISTRY_PASSWORD` are set correctly.
- Confirm the registry URL is reachable from the orchestration node.
- Verify the `check_repo` path in `utils.oci_registry.check_repo` points to an existing image in your registry.

## Application health

### DebugArgoCD

Renders a three-panel status dashboard for all ArgoCD repositories, the root application, and every managed application.

```bash
./run-shc.sh exec DebugArgoCD
```

**Reading the application table:**

| Sync status | Health status | Action |
| :--- | :--- | :--- |
| Synced | Healthy | No action required. |
| Synced | Progressing | Wait 2-3 minutes, then re-run. Normal during deployments. |
| OutOfSync | Any | Run `DebugArgoCDSyncAll` to force re-synchronization. |
| Any | Degraded or Missing | Inspect pod logs and run `DebugDatabases`. See remediation below. |

**What to do for Degraded or Missing applications:**

- Run `kubectl get pods -n <namespace>` to identify failing pods.
- Run `kubectl logs -n <namespace> <pod-name>` to view pod logs.
- Run `kubectl get events -n <namespace> --sort-by='.lastTimestamp'` to view recent events.

### DebugArgoCDSyncAll

Forces a three-phase full re-synchronization of all ArgoCD applications in parallel.

```bash
./run-shc.sh exec DebugArgoCDSyncAll
```

The three phases are:

1. Partial sync of `secretgenerator` and `configmap` resources to refresh secrets before regeneration.
2. Restart of the `sekoiaio-secret-operator` deployment to pick up refreshed SecretGenerators.
3. Full sync of every application.

!!! note "Sync behavior"
    The sync timeout per application defaults to 300 seconds. Up to 32 applications are synced concurrently. Override these values in `config.yml` under `modules.debug_argocd_sync_all`.

Use this command when applications are stuck in `OutOfSync`, after a manual change to the ArgoCD repository, or after a platform upgrade.

## Secret diagnostics

### DebugMissingSecrets

Compares declared `SecretGenerator` CRDs against actual Kubernetes `Secret` objects and reports:

- Secrets that are entirely missing.
- Secrets that exist but have incomplete keys.
- The Vault path expected for each missing secret.

```bash
./run-shc.sh exec DebugMissingSecrets
```

**What to do after a failure:**

- Check the `sekoiaio-secret-operator` status: `kubectl get pods -n support | grep secret-operator`.
- Run `DebugArgoCDSyncAll` to restart the operator and trigger secret regeneration.
- If specific Vault paths are missing, contact Sekoia support with the full command output.

### DebugKustomizeStacksTemplates

Clones the ArgoCD Git repository and scans every YAML file for unrendered `SH_TMPL` template placeholders. For each match, it reports the file path, resource type, and the YAML field that was not substituted.

```bash
./run-shc.sh exec DebugKustomizeStacksTemplates
```

**What to do after a failure:**

- Each unrendered placeholder corresponds to a missing or incorrect value in `config.yml`.
- Correct the relevant parameter in `config.yml` and re-run `PushArgoStacks` to regenerate the stack manifests.

## Database diagnostics

### DebugDatabases

Inspects all StatefulSets and CloudNativePG clusters in the `support` namespace.

```bash
./run-shc.sh exec DebugDatabases
```

**Status definitions:**

| Status | Meaning |
| :--- | :--- |
| Healthy | All replicas are running and ready with no recent restarts. |
| Warning | All replicas running, but recent restarts or waiting containers detected. Monitor and re-run. |
| Unhealthy | One or more replicas are not ready. Investigate immediately. |

**What to do for Unhealthy status:**

- For a pod in `CrashLoopBackOff`: `kubectl logs -n support <pod-name> --previous`
- For a pod in `Pending` state: `kubectl describe pod -n support <pod-name>` and check for resource pressure or missing PVCs.
- For CNPG clusters: `kubectl describe cluster -n support <cluster-name>`

## Resource management

### DebugResourceAllocation

Queries the Kubernetes Metrics API and compares live memory consumption against declared memory requests for every pod.

```bash
./run-shc.sh exec DebugResourceAllocation
```

!!! note "Metrics Server required"
    This command requires the Kubernetes Metrics Server. If the Metrics API is unavailable, the command exits with an error. Run the `HelmInstall` module to deploy it.

The output shows:

- A **waste report** for all pods with a memory request, sorted by wasted RAM. Red rows indicate 80% or more waste.
- A **list of pods without memory requests**, alongside their live usage. These pods present a scheduling risk.

## Platform installer debug

### DebugPlatformInstallation

Deploys the `platform-installer` Helm chart with a `pause` command override, creating a pod that stays alive without performing any changes. Use this to open an interactive shell inside the installer container and inspect its runtime environment, mounted secrets, and configuration files.

```bash
./run-shc.sh exec DebugPlatformInstallation
```

Any previous debug session is cleaned up automatically before the new pod is created.

## Collecting logs for a support ticket

When you escalate an issue to Sekoia L3 support, include the following in your request:

1. Generate a diagnostic bundle:

    ```bash
    ./run-shc.sh exec diagnose
    ```

2. Copy the full terminal output of the failing command.

3. Share your `config.yml` with all secrets redacted (replace all passwords and keys with `***`).

4. Collect K3s system logs from the affected nodes:

    ```bash
    journalctl -u k3s -n 500 --no-pager > k3s.log
    ```

## Related links

- [Monitor your platform](../monitoring/monitoring_guide.md): Continuous monitoring with Grafana and on-demand diagnostic workflows.
- [Deploy the platform](../deployment/deployment_guide.md): Post-deployment validation commands.
- [Deployment configuration reference](../deployment/deployment_configuration.md): How to fix configuration errors flagged by `CheckLocalConfig`.
