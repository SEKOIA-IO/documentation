# Debug your deployment

The self-hosted-controller (SHC) provides a set of diagnostic commands that let you validate configuration, inspect cluster health, audit secrets, diagnose database issues, and analyse resource usage. This article is a full reference for those commands, including expected outputs and remediation steps.

All commands are executed from the **orchestration node** using the `exec` subcommand:

```bash
exec <COMMAND>
```

## Configuration validation

### CheckLocalConfig

Validates every key in your `config.yml` against the SHC schema.

```bash
exec CheckLocalConfig
```

The check reports:

- Missing required fields.
- Values that do not match the expected format or regex.
- Keys that the configuration reference does not declare, for example a typo such as `global.hots`. The check reads every key of the computed configuration, including the keys inherited from the sizing profile.

??? example "Expected output (no errors)"
    ```
    Validating configuration...
    Configuration is valid entries_checked=42
    ```

??? example "Example failure output"
    ```
    Missing required config key=global.version.platform.version
    Format mismatch key=utils.oci_registry.host value=https://registry.lab expected_format=^[a-zA-Z0-9]
    Configuration validation failed: 2 error(s) found
    ```

**What to do after a failure:** Review each error line. Add any missing required keys to `config.yml`. Remove or correct the keys reported as undocumented: `config help <PREFIX>` lists the supported keys of a section. Fix values that do not match the expected format. For example, `utils.oci_registry.host` must be a bare hostname with no `http://` or `https://` scheme.

To inspect all resolved environment variable values before the schema check runs, add the `-v` flag:

```bash
-v exec CheckLocalConfig
```

The verbose output includes the fully resolved in-memory config tree, including every `${env.VAR_NAME}` value substituted with its actual content. Use this to confirm that secrets injected via environment variables are correctly loaded.

## Infrastructure connectivity

### CheckServersAreReachable

Tests SSH connectivity to all nodes listed in `utils.ansible.inventory`.

```bash
exec CheckServersAreReachable
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

### CheckServerSpec

Runs the `check_servers_spec` Ansible playbook against every manager and worker node in `utils.ansible.inventory`, and reports the first requirement each node fails.

```bash
exec CheckServerSpec
```

The command checks the following, in this order.

| Check | Requirement |
| :--- | :--- |
| Unique hostnames | No two nodes share a hostname |
| OS family | Debian-based |
| OS version | Debian 12 or later |
| CPU | 44 cores or more per node |
| RAM | 120 GiB or more per node |
| NTP enabled | `timedatectl` reports `NTP=yes` |
| Clock synchronized | `timedatectl` reports `NTPSynchronized=yes` |
| Port availability | TCP 80, 443, 2379, 2380, 4240, 4250, 6443, 10514, and 11514 can be bound before K3s is installed |
| Dedicated storage disk | One unused block device of 200 GB or more, with no partition table and no filesystem, before K3s is installed |

The last two checks are skipped once K3s is installed on the node. After the installation, the ports are bound by the cluster and the storage disk is consumed by Ceph and Longhorn, so requiring them to be free would fail every re-run.

**What to do after a failure:**

| Failure | Remediation |
| :--- | :--- |
| Duplicate hostnames | The error lists the inventory host to hostname mapping. Rename the affected nodes with `hostnamectl set-hostname <NEW_HOSTNAME>`, then re-run the command. |
| Debian version too old | Reinstall the node on Debian 12 or later. See [Technical requirements](../deployment/deployment_prerequisites.md#compute-node-specification). |
| CPU or RAM below the minimum | Resize the node. The error reports the detected value. |
| NTP not enabled | Install and enable `systemd-timesyncd` or `chrony`, then run `timedatectl set-ntp true`. |
| Clock not synchronized | Verify that the node reaches your NTP servers, then run `systemctl restart systemd-timesyncd` or `systemctl restart chrony`. |
| A required port is already bound | Run `ss -tlnp` on the node to identify the process holding the port, then stop it or reconfigure it to another port. |
| No unused extra disk | Attach a block device of 200 GB or more to the node and leave it unformatted, with no partition table. A disk that already carries a filesystem or partitions is rejected. |

### CheckNodePortReachability

Verifies that every node can reach every other node on the TCP ports the cluster needs. The command runs on all manager and worker nodes, whatever their role.

```bash
exec CheckNodePortReachability
```

Each node briefly opens a listener on the ports below while the other nodes connect to it. Every connection attempt times out after 5 seconds.

| Port | Purpose |
| :--- | :--- |
| 6443 | Kubernetes API |
| 2379 | etcd client |
| 2380 | etcd peer |
| 4240 | Cilium health |
| 4250 | Cilium mutual authentication |
| 10514 | Syslog intake |
| 11514 | Syslog intake |

The check is skipped when K3s is installed on every node. When K3s is installed on some nodes only, those nodes open no listener, and the check reports only the connections that time out towards them.

??? example "Example failure output"
    ```
    Some nodes cannot reach each other on the ports the cluster needs, so the installation would fail. Fix the points below, then re-run CheckNodePortReachability.

    Blocked connections between nodes:
      - 10.0.0.11 does not accept TCP 2379 (etcd client) from any other node: packets are silently dropped (firewall, cloud security group, network firewall or stale Cilium BPF state).

    Ports already used by another service (stop it before installing):
      - 10.0.0.12: TCP 10514 (syslog intake) cannot be opened (Address already in use). Find the process with: sudo ss -ltnp 'sport = :10514'
    ```

**What to do after a failure:**

| Failure | Remediation |
| :--- | :--- |
| Connection dropped (`timeout`) | Allow inbound TCP from the other cluster nodes on the listed port, in the host firewall (`iptables`, `nftables`, `ufw`, or `firewalld`) and in every security group or network firewall between the nodes. To inspect the host firewall, run `sudo iptables -S` or `sudo nft list ruleset` on the node. |
| Connection rejected (`refused`) | A firewall rule rejects the connection. Remove or adapt the rule on the destination node or on the network path. |
| Port already used | Run `sudo ss -ltnp 'sport = :<PORT>'` on the node to identify the process, then stop it. |
| Node could not be checked | Verify the SSH access to the node with `CheckServersAreReachable`, and confirm that `python3` is installed on the node. |

!!! warning "Nodes reused after a previous K3s installation"
    After a K3s uninstall, leftover Cilium network programs can still drop traffic even when the firewall accepts it. On dedicated nodes where K3s is stopped, run `CleanupCilium`, then run `CheckNodePortReachability` again. Do not bypass the check.

### CheckS3Performance

Benchmarks the S3-compatible platform storage from every worker node and compares the results with minimum thresholds. The command is not part of `Install`.

!!! warning "Run it only when Sekoia asks you to"
    The benchmark generates a sustained load on your S3-compatible storage and creates buckets on it. Run it only at the request of Sekoia support, for example to investigate slow indexation, once the Kubernetes cluster is installed.

```bash
exec CheckS3Performance
```

The command deploys a temporary `s3-warp-benchmark` Helm release in the `sekoia-system` namespace. One `minio/warp` pod per worker node runs a mixed workload of GET, PUT, STAT, and DELETE requests against a bucket named `warp-preflight-<NODE_NAME>`, then the release is removed. The command displays a table with the measured value, the threshold, and the result of each metric. Each value is the median of the measurements across the worker nodes.

| Metric | Threshold |
| :--- | :--- |
| GET and PUT throughput | 50 MiB/s or more |
| STAT and DELETE throughput | 100 operations/s or more |
| Request latency (90th percentile) | 200 ms or less |
| Time to first byte for GET and PUT (90th percentile) | 100 ms or less |

The benchmark reads the platform storage endpoint and credentials from the computed configuration. Adjust it with the following keys in `config.yml`. The command does not accept `--set` overrides.

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.check_s3_performance.skip` | `true` to skip the benchmark. | `false` |
| `modules.check_s3_performance.enforce` | `false` to report thresholds that are not met as a warning instead of a failure. | `true` |
| `modules.check_s3_performance.duration` | Duration of each benchmark pass. | `5m` |
| `modules.check_s3_performance.passes` | Number of benchmark passes. | `1` |
| `modules.check_s3_performance.concurrent` | Concurrent requests per worker node. | `20` |
| `modules.check_s3_performance.obj_size_max` | Maximum object size in bytes. Object sizes are randomized up to this value. | `8388608` |
| `modules.check_s3_performance.bucket_prefix` | Prefix of the benchmark bucket names. | `warp-preflight` |
| `modules.check_s3_performance.image` | Benchmark image. | `docker.io/minio/warp:v0.8.0` |
| `modules.check_s3_performance.insecure` | `true` to skip TLS certificate verification. | `false` |
| `modules.check_s3_performance.thresholds` | Thresholds of the metrics. | See the table above. |

**What to do after a failure:** Compare each failed metric with the [storage requirements](../deployment/deployment_prerequisites.md#storage), and review the storage capacity and the network path between the worker nodes and the S3 endpoint with your storage provider. The SHC does not delete the `warp-preflight-*` buckets: remove them from your storage once the benchmark is complete.

### CheckKubernetesCluster

Connects to the Kubernetes API and verifies that every node has a `Ready=True` condition and that the actual node count matches your Ansible inventory.

```bash
exec CheckKubernetesCluster
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

Verifies that the platform release directory, `<global.version.platform.path>/<global.version.platform.version>`, exists on the orchestration node and is not empty. The command does not check the content of the directory or the security content bundles.

```bash
exec CheckLocalReleaseFiles
```

**What to do after a failure:** Confirm that the release archive was fully extracted and that `global.version.platform.path` points to the correct directory.

!!! note "Missing security content bundles"
    A missing or unreadable bundle in `data/<TYPE>/` does not fail the checks. `PushDataBundles` reports it as a warning and skips it, and the platform keeps the content version shipped with the release. Look for these warnings in the `push` stage output.

### CheckLocalTools

Verifies that the tools used to push the signed release artifacts are available in the SHC container: `cosign` in a 2.x version, and `skopeo`.

```bash
exec CheckLocalTools
```

**What to do after a failure:** The tools ship with the SHC image. A failure usually means that the container does not run the SHC image of the release. Load the image from the release archive and set `DOCKER_IMAGE` as described in [Deploy the platform](../deployment/deployment_guide.md#step-3-load-the-self-hosted-controller-shc-docker-image).

### CheckLocalGit

Clones the repository configured in `utils.git.repo_url` and tests both pull and push access.

```bash
exec CheckLocalGit
```

**What to do after a failure:**

- Verify `GIT_HTTP_USERNAME` and `GIT_HTTP_PASSWORD` are set correctly.
- Confirm the repository exists and is reachable from the orchestration node.
- Ensure the user has both read and write permissions on the repository.

### CheckLocalOCIRegistry

Tests push, pull, and delete access to your OCI registry. If push fails, pull and delete are skipped and reported as untested.

```bash
exec CheckLocalOCIRegistry
```

**What to do after a failure:**

- Verify `REGISTRY_USERNAME` and `REGISTRY_PASSWORD` are set correctly.
- Confirm the registry URL is reachable from the orchestration node.
- Verify the `check_repo` path in `utils.oci_registry.check_repo` points to an existing image in your registry.

## Application health

### DebugArgoCD

Renders a three-panel status dashboard for all ArgoCD repositories, the root application, and every managed application.

```bash
exec DebugArgoCD
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
exec DebugArgoCDSyncAll
```

The three phases are:

1. Partial sync of `secretgenerator` and `configmap` resources to refresh secrets before regeneration.
2. Restart of the `sekoiaio-secret-operator` deployment to pick up refreshed SecretGenerators.
3. Full sync of every application.

!!! note "Sync behavior"
    The sync timeout per application is 300 seconds. Up to 32 applications are synced concurrently.

Use this command when applications are stuck in `OutOfSync`, after a manual change to the ArgoCD repository, or after a platform upgrade.

## Secret diagnostics

### DebugMissingSecrets

Compares declared `SecretGenerator` CRDs against actual Kubernetes `Secret` objects and reports:

- Secrets that are entirely missing.
- Secrets that exist but have incomplete keys.
- The Vault path expected for each missing secret.

```bash
exec DebugMissingSecrets
```

**What to do after a failure:**

- Check the `sekoiaio-secret-operator` status: `kubectl get pods -n support | grep secret-operator`.
- Run `DebugArgoCDSyncAll` to restart the operator and trigger secret regeneration.
- If specific Vault paths are missing, contact Sekoia support with the full command output.

### DebugKustomizeStacksTemplates

Clones the ArgoCD Git repository and scans every YAML file for unrendered `SH_TMPL` template placeholders. For each match, it reports the file path, resource type, and the YAML field that was not substituted.

```bash
exec DebugKustomizeStacksTemplates
```

**What to do after a failure:**

- Each unrendered placeholder corresponds to a missing or incorrect value in `config.yml`.
- Correct the relevant parameter in `config.yml` and re-run `PushArgoStacks` to regenerate the stack manifests.

## Security content

### SyncRulesCatalog and SyncIntakeFormats

Synchronize the `rules-catalog-updater-on-self-hosted` and `intake-formats-updater-on-self-hosted` ArgoCD applications, then wait for the job that loads the content into the platform to succeed. Each command first runs `SyncArgoRootApp`, which synchronizes the ArgoCD root application and waits up to 5 minutes for it to complete.

```bash
exec SyncRulesCatalog
exec SyncIntakeFormats
```

Each command waits up to 900 seconds for its job. To allow more time, set `modules.sync_rules_catalog.sync_timeout` or `modules.sync_intake_formats.sync_timeout`:

```bash
exec SyncRulesCatalog --set modules.sync_rules_catalog.sync_timeout=1800
```

**What to do after a failure:**

- If the error reports an operation already running on the application, wait for it to complete, then run the command again.
- If the job did not succeed, locate it with `kubectl get jobs -A | grep -E 'rules-catalog-updater|intake-formats-updater'`, then read its logs with `kubectl logs -n <NAMESPACE> job/<JOB_NAME>`.
- Run `DebugArgoCD` to check the state of the two applications.

## Database diagnostics

### DebugDatabases

Inspects all StatefulSets and CloudNativePG clusters in the `support` namespace.

```bash
exec DebugDatabases
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
exec DebugResourceAllocation
```

!!! note "Metrics Server required"
    This command requires the Kubernetes Metrics Server. If the Metrics API is unavailable, the command exits with an error. Run the `HelmInstall` module to deploy it.

The output shows:

- A **waste report** for all pods with a memory request, sorted by wasted RAM. Red rows indicate 80% or more waste.
- A **list of pods without memory requests**, alongside their live usage. These pods present a scheduling risk.

## Platform installer debug

### DebugPlatformInstallation

Deploys the `platform-installer` Helm chart with a `pause` command override, creating a pod that stays alive without performing any changes. The command returns as soon as the Helm install succeeds; it does **not** wait for the pod to start.

Use this to open an interactive shell inside the installer container and inspect its runtime environment, mounted secrets, and configuration files.

```bash
exec DebugPlatformInstallation
```

Once the pod is running, open a shell with:

```bash
kubectl exec -it -n support <pod-name> -- /bin/bash
```

Any previous debug session is cleaned up automatically before the new pod is created.

### CleanupHelmReleases

Deletes the Helm revision records left in the `pending-install`, `pending-upgrade`, `pending-rollback`, `failed`, or `uninstalling` state by an interrupted run, in every namespace. The deployed and superseded revisions and the resources created by the charts are preserved. Each deletion is logged as a warning with the release name and its status.

```bash
exec CleanupHelmReleases
```

The SHC runs this command automatically before `HelmInstall`, `PlatformInstallation`, `PlatformAccess`, `DebugPlatformInstallation`, `DebugMissingSecrets`, and `CheckS3Performance`.

!!! warning "Run it only when no Helm operation is in progress"
    The command also deletes the record of a Helm operation that is still running. Do not run it, or a module that depends on it, while another SHC session is installing or upgrading the platform.

## Operations

### RebootNodes

Reboots all nodes listed in `utils.ansible.inventory` and waits for them to come back online.

```bash
exec RebootNodes
```

Use this when patching the OS or applying kernel updates. The playbook waits for SSH to become available again on each node before reporting success.

### KubeCrashRecovery

Restarts all pods across the cluster in ordered namespace phases and waits for each phase to become healthy before moving to the next. Use this after an unexpected node crash or manual cluster restart that left pods stuck in a failed state.

```bash
exec KubeCrashRecovery
```

The phases run in this order: `kube*` namespaces → `rook-ceph` → `vault` → `*system*` → `support` → all remaining namespaces. Each phase waits up to `modules.kube_crash_recovery.pod_ready_timeout` seconds (default: `300`) before giving up.

**What to do after a timeout:** Run `kubectl get pods -A --field-selector=status.phase!=Running,status.phase!=Succeeded` to identify the stuck pods. Check their events and logs, then re-run `KubeCrashRecovery`.

### PlatformScaleDown and PlatformDestroy

`PlatformScaleDown` deletes the platform namespaces and verifies that every node has released its storage volumes. `PlatformDestroy` also uninstalls K3s and wipes the Ceph storage disks. Both commands are disabled by default and require safety flags. See [Reset or destroy the platform](../operations/reset_platform.md).

### K3SUninstall

Uninstalls K3s from the worker nodes, then from the manager nodes, then removes the Cilium networking from every node.

!!! warning "Destructive and irreversible"
    This command removes the Kubernetes cluster and every workload it runs. Run it only to reset a dedicated cluster. `PlatformDestroy` runs it after a verified cleanup of the platform workloads. See [Reset or destroy the platform](../operations/reset_platform.md).

```bash
exec K3SUninstall
```

If the error reports that K3s was removed but the Cilium networking cleanup is incomplete, do not wipe the disks or reinstall. Run `CleanupCilium`.

### CleanupCilium

Removes the Cilium networking left on dedicated nodes after a K3s uninstall: network interfaces, BPF programs, and `CILIUM_` firewall rules. The command refuses to run while K3s or a Cilium agent is still running on a node. See [Clean up the Cilium networking](../operations/reset_platform.md#clean-up-the-cilium-networking).

```bash
exec CleanupCilium
```

### WipeStorageDisks

Detects the disks used by Ceph on every node, deactivates their Ceph volume groups, and erases them. It then removes the Rook host state, `/var/lib/rook`, on every node, including the nodes without a Ceph disk. The command refuses to run while K3s or Ceph processes are still running on a node, and refuses a disk that is mounted, still in use, or shared with a volume group that is not a Ceph volume group.

!!! warning "Destructive and irreversible"
    This command permanently destroys all data on detected Ceph disks. Run it only once K3s is uninstalled, as the last phase of a full cluster reset. See [Reset or destroy the platform](../operations/reset_platform.md).

The command does not accept `--set` overrides. To run it, set `modules.wipe_storage.enabled: true` in your `config.yml`. With the flag unset, the command logs a warning and completes without wiping any disk.

```bash
exec WipeStorageDisks
```

## Service diagnostics

### Diagnostic

Evaluates rule-based health checks against the platform's Prometheus metrics and reports the state of each platform area.

```bash
exec Diagnostic
```

Use this command once the infrastructure and application layers are healthy but a platform feature misbehaves, for example alerts that stop being created or assets that stop being discovered. For the available targets, the output formats, and how to read a result, see [Run platform diagnostics](../monitoring/run_diagnostics.md).

## Increase the Ansible output

The SHC runs the node operations, such as `CheckServerSpec`, `K3SInstall`, or `WipeStorageDisks`, through Ansible. By default, it streams only the task headers, the failures, and the final summary. To investigate a node operation, set the following keys in your `config.yml`, then run the command again:

| Field | Description | Default |
| :--- | :--- | :--- |
| `utils.ansible.verbosity` | Ansible output streamed to the log: `normal` for the headers, failures, and summary, `full` for every line, or `silent` for no output. | `normal` |
| `utils.ansible.debug_level` | Ansible verbosity level, from `0` to `4`, equivalent to the `-v` to `-vvvv` options. | `0` |

Reset both values once the investigation is complete.

## Collecting logs for a support ticket

When you escalate an issue to Sekoia L3 support, include the following in your request:

1. Copy the full terminal output of the failing command.

2. Share your `config.yml` with all secrets redacted (replace all passwords and keys with `***`).

3. Collect K3s system logs from the affected nodes:

    ```bash
    journalctl -u k3s -n 500 --no-pager > k3s.log
    ```

4. If applications are degraded, collect ArgoCD and pod logs:

    ```bash
    exec DebugArgoCD
    kubectl get pods -A --field-selector=status.phase!=Running,status.phase!=Succeeded
    kubectl logs -n <namespace> <pod-name> --previous
    ```

## Related links

- [Monitor your platform](../monitoring/monitoring_guide.md): Continuous monitoring with Grafana and on-demand diagnostic workflows.
- [Deploy the platform](../deployment/deployment_guide.md): Post-deployment validation commands.
- [Deployment configuration reference](../deployment/deployment_configuration.md): How to fix configuration errors flagged by `CheckLocalConfig`.
- [Run platform diagnostics](../monitoring/run_diagnostics.md): Targeted Prometheus health checks per platform area.
- [Use the SHC interface](../operations/controller_interface.md): Run commands and diagnostics from the interactive interface.
