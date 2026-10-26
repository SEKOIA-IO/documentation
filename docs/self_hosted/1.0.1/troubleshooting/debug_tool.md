# Debug your deployment

The self-hosted-controller (SHC) provides a set of diagnostic commands that let you validate configuration, inspect cluster health, check that the expected secrets exist, diagnose database issues, and analyze resource usage. This article is a full reference for those commands, including expected outputs and remediation steps.

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
    ```text
    Validating configuration...
    Configuration is valid entries_checked=42
    ```

??? example "Example failure output"
    ```text
    Missing required config description=Platform release version to deploy key=global.version.platform.version
    Format mismatch expected_format=^[a-zA-Z0-9][a-zA-Z0-9\-\.]*(:\d+)?$ key=utils.oci_registry.host
    Configuration validation failed: 2 error(s) found. Missing required configuration: global.version.platform.version (Platform release version to deploy).
    ```

Each error names the configuration key and the expected format. It never displays the rejected value.

**What to do after a failure:** Review each error line. Add any missing required keys to `config.yml`. Remove or correct the keys reported as undocumented: `config help <PREFIX>` lists the supported keys of a section. Fix values that do not match the expected format. For example, `utils.oci_registry.host` must be a bare hostname with no `http://` or `https://` scheme.

A required key that reads an environment variable that is not set is reported as a missing key. To check that the secrets injected through environment variables are loaded, run `CheckLocalConfig` and look for missing keys: do not print the resolved configuration, because `config show` displays every secret in clear.

To enable the debug logs of a command, add the `-v` option. The option does not print the resolved configuration.

!!! warning "Verbose logs contain the registry password"
    With `-v`, `K3SInstall` logs its Ansible variables at debug level, including the OCI registry password in clear. The SHC also writes this output to its run log file. Before you share verbose output or a log file, redact it as described in [Collecting logs for a support ticket](#collecting-logs-for-a-support-ticket).

```bash
-v exec CheckLocalConfig
```

## Infrastructure connectivity

### CheckServersAreReachable

Tests SSH connectivity to all nodes listed in `utils.ansible.inventory`.

```bash
exec CheckServersAreReachable
```

??? example "Expected output"
    ```text
    Pinging all configured servers via Ansible...
    All configured servers are reachable
    ```

**What to do after a failure:**

- Verify that `SERVERS_SSH_KEY`, which `utils.ansible.ssh-key` reads, holds the SSH private key itself, with real newlines, and is exported in your environment.
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
| Ceph node names, manual storage mode only | Every node name in `modules.platform_configuration.config.rook.storage.nodes` is the hostname of an inventory node |
| OS family | Debian-based |
| OS version | Debian 12 or later |
| Swap | No active swap device |
| CPU | 44 logical CPUs or more per node |
| RAM | 120 GiB or more per node |
| NTP enabled | `timedatectl` reports `NTP=yes` |
| Clock synchronized | `timedatectl` reports `NTPSynchronized=yes` |
| Port availability | TCP 80, 443, 2379, 2380, 4240, 4250, 6443, 10514, and 11514 can be bound before K3s is installed |
| Dedicated storage disk, automatic storage mode | One unused block device of 200 GB or more, with no partition table and no filesystem, before K3s is installed |
| Selected Ceph devices, manual storage mode only | `lvm2` is installed, and each device listed for the node is a writable whole disk or logical volume of 200 GB or more, unmounted, with no filesystem, partition table, or signature, before K3s is installed |

The port and storage checks are skipped once K3s is installed on the node. After the installation, the ports are bound by the cluster and the storage devices are consumed by Ceph, so requiring them to be free would fail every re-run.

**What to do after a failure:**

| Failure | Remediation |
| :--- | :--- |
| Duplicate hostnames | The error lists the inventory host to hostname mapping. Rename the affected nodes with `hostnamectl set-hostname <NEW_HOSTNAME>`, then re-run the command. |
| Debian version too old | Reinstall the node on Debian 12 or later. See [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#compute-node-specification). |
| Active swap | Run `sudo swapoff -a`, remove or comment out the swap entries in `/etc/fstab`, and disable any systemd swap unit or zram service that enables swap. Reboot the node, then check that `/sbin/swapon --show=NAME --noheadings --raw` returns no entry. See [Swap](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#swap). |
| CPU or RAM below the minimum | Resize the node. The error reports the detected value. |
| NTP not enabled | Install and enable `systemd-timesyncd` or `chrony`, then run `timedatectl set-ntp true`. |
| Clock not synchronized | Verify that the node reaches your NTP servers, then run `systemctl restart systemd-timesyncd` or `systemctl restart chrony`. |
| A required port is already bound | Run `ss -tlnp` on the node to identify the process holding the port, then stop it or reconfigure it to another port. |
| No unused extra disk | Attach a block device of 200 GB or more to the node and leave it unformatted, with no partition table. A disk that already carries a filesystem or partitions is rejected. |
| Manual Ceph node names do not match | Set each `name` in `modules.platform_configuration.config.rook.storage.nodes` to the short hostname of the node, as returned by `hostname -s`. |
| Selected Ceph device rejected | The error names the device and the reason. Create and activate the logical volume, or select another device, then re-run the command. |

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
    ```text
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

Before you run the benchmark, check the following points with your storage administrator:

- The benchmark uses the endpoint and the credentials of the platform storage, `global.platform_storage`, which ExaLog also uses to store the events. These credentials must allow creating a bucket, and writing, reading, listing, and deleting objects.
- Each worker node writes objects of up to 8 MiB to its own `warp-preflight-<NODE_NAME>` bucket. The SHC does not delete these buckets or their objects, so they keep using storage capacity until you delete them.
- The benchmark pods run without CPU or memory limits, and their requests add to the platform traffic on the same storage and network. On a platform that ingests events, the benchmark can slow down ingestion and indexation while it runs.

```bash
exec CheckS3Performance
```

The command deploys a temporary `s3-warp-benchmark` Helm release in the `sekoia-system` namespace. One `minio/warp` pod per worker node runs a mixed workload of GET, PUT, STAT, and DELETE requests against its bucket. The SHC removes the release when the benchmark completes, whether it passes or fails. The command displays a table with the measured value, the threshold, and the result of each metric. Each value is the median of the measurements across the worker nodes.

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
| `modules.check_s3_performance.distribution` | Weights of the GET, PUT, STAT, and DELETE requests in the mixed workload. | `get: 40`, `put: 40`, `stat: 10`, `delete: 10` |
| `modules.check_s3_performance.obj_size_max` | Maximum object size in bytes. Object sizes are randomized up to this value. | `8388608` |
| `modules.check_s3_performance.bucket_prefix` | Prefix of the benchmark bucket names. | `warp-preflight` |
| `modules.check_s3_performance.image` | Benchmark image. | `docker.io/minio/warp:v0.8.0` |
| `modules.check_s3_performance.tls` | `false` to connect without TLS when the endpoint has no `http://` or `https://` scheme. A scheme in the endpoint takes precedence. | `true` |
| `modules.check_s3_performance.insecure` | `true` to skip TLS certificate verification. | `false` |
| `modules.check_s3_performance.thresholds` | Thresholds of the metrics. | See the table above. |

Once the benchmark is complete, whatever its result, delete the `warp-preflight-*` buckets and their objects from your storage, then list the buckets of the storage to confirm that none remains.

**What to do after a failure:** Compare each failed metric with the [storage requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#storage), and review the storage capacity and the network path between the worker nodes and the S3 endpoint with your storage provider.

### CheckKubernetesCluster

Connects to the Kubernetes API and verifies that every node has a `Ready=True` condition and that the actual node count matches your Ansible inventory.

```bash
exec CheckKubernetesCluster
```

??? example "Expected output"
    ```text
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

**What to do after a failure:** The tools ship with the SHC image. A failure usually means that the container does not run the SHC image of the release. Load the image from the release archive and set `DOCKER_IMAGE` as described in [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md#step-3-load-the-self-hosted-controller-shc-docker-image).

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

Tests push, pull, and delete access to your OCI registry. The command pushes an empty test artifact, tagged `check-<TIMESTAMP>`, to the repository set in `utils.oci_registry.check_repo` (default: `<utils.oci_registry.project>/shc-probe`), pulls it, then deletes it. If push fails, pull and delete are skipped and reported as untested.

```bash
exec CheckLocalOCIRegistry
```

**What to do after a failure:**

- Verify `REGISTRY_USERNAME` and `REGISTRY_PASSWORD` are set correctly.
- Confirm the registry URL is reachable from the orchestration node.
- Verify that the registry credentials can push to and delete from the repository set in `utils.oci_registry.check_repo`. The repository does not need to hold an image.

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
| OutOfSync | Any | Check the Git repository, then run `DebugArgoCDSyncAll` to force re-synchronization. See the warning below. |
| Any | Degraded or Missing | Inspect pod logs and run `DebugDatabases`. See remediation below. |

**What to do for Degraded or Missing applications:**

- Run `kubectl get pods -n <namespace>` to identify failing pods.
- Run `kubectl logs -n <namespace> <pod-name>` to view pod logs.
- Run `kubectl get events -n <namespace> --sort-by='.lastTimestamp'` to view recent events.

### DebugArgoCDSyncAll

Forces a three-phase full re-synchronization of all ArgoCD applications in parallel.

!!! warning "A forced sync overwrites manual changes"
    The sync applies the manifests of the ArgoCD Git repository to the cluster. Any change made directly in the cluster to a resource that ArgoCD manages is overwritten. Before you run the command, check the recent commits of the repository set in `utils.git.repo_url`, and run `DebugKustomizeStacksTemplates` to detect unrendered values.

```bash
exec DebugArgoCDSyncAll
```

The three phases are:

1. Partial sync of `secretgenerator` and `configmap` resources to refresh secrets before regeneration.
2. Restart of the `sekoiaio-secret-operator` deployment to pick up refreshed SecretGenerators.
3. Full sync of every application.

!!! note "Sync behavior"
    The sync timeout per application is 300 seconds. Up to 32 applications are synced concurrently.

Use this command when applications are stuck in `OutOfSync`, or after a manual change to the ArgoCD repository.

## Secret diagnostics

### DebugMissingSecrets

Checks that the secrets the platform expects exist. The command compares the declared `SecretGenerator` CRDs against actual Kubernetes `Secret` objects and reports:

- Secrets that are entirely missing.
- Secrets that exist but have incomplete keys.
- The Vault path expected for each missing key, and whether the platform installer configuration declares it.

The output lists Vault paths and key names, not secret values.

!!! warning "The command refreshes the secrets"
    Before the comparison, the command runs the `VaultContent` step of the platform installer, which creates the missing Vault secrets and updates the values that come from your configuration. It then deletes every Kubernetes secret managed by a `SecretGenerator` object, restarts `sekoiaio-secret-operator`, and waits up to 120 seconds for the secrets to be recreated. Run it when you investigate missing secrets, not as a routine check.

```bash
exec DebugMissingSecrets
```

The command leaves the `shpi-debug-dumpconfig` installer release in the `sekoia-system` namespace. Like every installer release, it holds the rendered platform configuration, secret values included. Once the investigation is complete, remove it:

```bash
helm uninstall shpi-debug-dumpconfig -n sekoia-system
```

**What to do after a failure:**

- Check the `sekoiaio-secret-operator` status: `kubectl get pods -n support | grep secret-operator`.
- Run `DebugArgoCDSyncAll` to restart the operator and trigger secret regeneration.
- If specific Vault paths are missing, contact Sekoia support. Share the Vault paths only if Sekoia support asks for them, and only through a secure channel. Never share a secret value.

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

To update the detection rules and the intake formats after the installation, see [Update the security content](/self_hosted/1.0.1/operations/update_security_content.md).

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
| Warning | All replicas running, but restarts in the last 10 minutes or waiting containers detected. Monitor and re-run. |
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

## Helm releases

### CleanupHelmReleases

Deletes the Helm revision records left in the `pending-install`, `pending-upgrade`, `pending-rollback`, `failed`, or `uninstalling` state by an interrupted run, in every namespace. The deployed and superseded revisions and the resources created by the charts are preserved. Each deletion is logged as a warning with the release name and its status.

```bash
exec CleanupHelmReleases
```

The SHC runs this command automatically before `HelmInstall`, `PlatformInstallation`, `PlatformAccess`, `DebugMissingSecrets`, and `CheckS3Performance`.

!!! warning "Run it only when no Helm operation is in progress"
    The command also deletes the record of a Helm operation that is still running. Do not run it, or a module that depends on it, while another SHC session is installing or upgrading the platform.

## Operations

### RebootNodes

Reboots all nodes listed in `utils.ansible.inventory` and waits for them to come back online.

```bash
exec RebootNodes
```

Use this when patching the OS or applying kernel updates. The playbook waits for SSH to become available again on each node before reporting success.

The nodes reboot in parallel, without being drained, so the platform is unavailable until the nodes and their workloads restart. If pods stay in a failed state after the reboot, run `KubeCrashRecovery`.

### KubeCrashRecovery

Restarts all pods across the cluster in ordered namespace phases and waits for each phase to become healthy before moving to the next. Use this after an unexpected node crash or manual cluster restart that left pods stuck in a failed state.

```bash
exec KubeCrashRecovery
```

The phases run in this order: `kube*` namespaces → `rook-ceph` → `vault` → `*system*` → `support` → all remaining namespaces. Each phase waits up to 5 minutes before giving up.

In the `support` phase, the command does not wait for the ArangoDB pods to become ready. Once the command completes, run `DebugDatabases` to check them.

**What to do after a timeout:** Run `kubectl get pods -A --field-selector=status.phase!=Running,status.phase!=Succeeded` to identify the stuck pods. Check their events and logs, then re-run `KubeCrashRecovery`.

### RestartAllMicroservices

Restarts every deployment, StatefulSet, and DaemonSet marked as a Sekoia microservice, with a rolling restart, and waits up to 300 seconds in total for the rollouts to complete. The databases are not restarted. Use it after the Kubernetes secrets are refreshed, so that the services load the new values. See [Rotate the certificate and credentials](/self_hosted/1.0.1/operations/rotate_certificate_and_credentials.md#restart-the-microservices).

```bash
exec RestartAllMicroservices
```

A workload whose rollout is paused, partitioned, or set to `OnDelete` cannot be restarted and is reported as an error, like a rollout that does not complete in time.

### PlatformScaleDown and PlatformDestroy

`PlatformScaleDown` deletes the platform namespaces and verifies that every node has released its storage volumes. `PlatformDestroy` also uninstalls K3s and, in the automatic storage mode, wipes the Ceph storage disks. Both commands are disabled by default and require safety flags. They provide no restore path. See [Reset or destroy the platform](/self_hosted/1.0.1/operations/reset_platform.md).

### K3SUninstall

Uninstalls K3s from the worker nodes, then from the manager nodes, then removes the Cilium networking from every node.

!!! warning "Destructive and irreversible"
    This command removes the Kubernetes cluster and every workload it runs. Run it only to reset a dedicated cluster. `PlatformDestroy` runs it after a verified cleanup of the platform workloads. See [Reset or destroy the platform](/self_hosted/1.0.1/operations/reset_platform.md).

```bash
exec K3SUninstall
```

If the error reports that K3s was removed but the Cilium networking cleanup is incomplete, do not wipe the disks or reinstall. Run `CleanupCilium`.

### CleanupCilium

Removes the Cilium networking left on dedicated nodes after a K3s uninstall: network interfaces, BPF programs, and `CILIUM_` firewall rules. The command refuses to run while K3s or a Cilium agent is still running on a node. See [Clean up the Cilium networking](/self_hosted/1.0.1/operations/reset_platform.md#clean-up-the-cilium-networking).

```bash
exec CleanupCilium
```

### WipeStorageDisks

Detects the disks used by Ceph on every node, deactivates their Ceph volume groups, and erases them. It then removes the Rook host state, `/var/lib/rook`, on every node, including the nodes without a Ceph disk. The command refuses to run while K3s or Ceph processes are still running on a node, and refuses a disk that is mounted, still in use, or shared with a volume group that is not a Ceph volume group.

!!! warning "Destructive and irreversible"
    This command permanently destroys all data on detected Ceph disks. Run it only once K3s is uninstalled, as the last phase of a full cluster reset. See [Reset or destroy the platform](/self_hosted/1.0.1/operations/reset_platform.md).

The command does not accept `--set` overrides. To run it, set `modules.wipe_storage.enabled: true` in your `config.yml`. With the flag unset, the command logs a warning and completes without wiping any disk.

```bash
exec WipeStorageDisks
```

In the manual storage mode, with `modules.platform_configuration.config.rook.storage.mode: manual`, the command wipes nothing and removes nothing: it logs a warning, and cleaning up the Ceph devices and `/var/lib/rook` is your responsibility.

## Service diagnostics

### Diagnostic

Evaluates rule-based health checks against the platform's Prometheus metrics and reports the state of each platform area.

```bash
exec Diagnostic
```

Use this command once the infrastructure and application layers are healthy but a platform feature misbehaves, for example alerts that stop being created or assets that stop being discovered. For the available targets, the output formats, and how to read a result, see [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md).

## Increase the Ansible output

The SHC runs the node operations, such as `CheckServerSpec`, `K3SInstall`, or `WipeStorageDisks`, through Ansible. By default, it streams only the task headers, the failures, and the final summary. To investigate a node operation, set the following keys in your `config.yml`, then run the command again:

| Field | Description | Default |
| :--- | :--- | :--- |
| `utils.ansible.verbosity` | Ansible output streamed to the log: `normal` for the headers, failures, and summary, `full` for every line, or `silent` for no output. | `normal` |
| `utils.ansible.debug_level` | Ansible verbosity level, from `0` to `4`, equivalent to the `-v` to `-vvvv` options. | `0` |

Reset both values once the investigation is complete. The detailed output can include host details and task values: redact it before you share it.

## Collecting logs for a support ticket

!!! warning "Redact the output before you share it"
    Command output, logs, and configuration files can contain secrets and customer information. Before you collect or send anything, check it against the following list, and replace each match with `***`:

    - Credentials: passwords, tokens, API keys, and private keys, such as the credentials displayed by `PlatformAccess`, the registry password in `-v` output, and the values of the environment variables of the execution script.
    - Vault secret values. Share Vault paths or values only when Sekoia support asks for them, and only through a secure channel.
    - Private hostnames, IP addresses, and internal URLs.
    - Customer data, such as community names, user names, email addresses, and event contents.

When you escalate an issue to Sekoia L3 support, include the following in your request:

1. Copy the full terminal output of the failing command. The SHC also writes its log lines to a run log file, `/tmp/<TIMESTAMP>_self-hosted-controller.log` in the container. See [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md#navigate-the-interface) to keep this file.

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

- [Monitor your platform](/self_hosted/1.0.1/monitoring/monitoring_guide.md): Continuous monitoring with Grafana and on-demand diagnostic workflows.
- [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md): Post-deployment validation commands.
- [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md): How to fix configuration errors flagged by `CheckLocalConfig`.
- [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md): Targeted Prometheus health checks per platform area.
- [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md): Run commands and diagnostics from the interactive interface.
