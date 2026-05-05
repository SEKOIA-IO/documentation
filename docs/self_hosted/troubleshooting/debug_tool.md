# Troubleshooting and Debugging

A centralized set of diagnostic tools is available through the Self-Hosted Controller (SHC). These commands let you validate your configuration, inspect the health of your deployment, audit secrets, diagnose database issues, and identify resource pressure on the cluster.

All commands below are executed via the `run-shc.sh` wrapper script using the `exec` subcommand, which instantiates the named module inside the controller container and runs it to completion.

---

## Configuration Validation

### Validate the local configuration file

```bash
./run-shc.sh exec CheckLocalConfig
```

Loads `config.yml` and validates every key against the schema defined in `help.yaml`. The check covers:

- **Missing required fields** — any key marked `required: true` in the schema that is absent from your config will be reported with an error log line.
- **Format mismatches** — values that do not match the expected regex pattern are flagged individually.
- **Schema integrity** — ensures no required key is hidden from the help output (which would indicate an authoring error in `help.yaml`).

If all checks pass, the command exits cleanly with:

```
Validating configuration...
Configuration is valid   entries_checked=<N>
```

If errors are found, each is logged individually before the command exits with a non-zero status:

```
Missing required config   key=global.version.platform.version
Format mismatch           key=utils.oci_registry.url  value=…  expected_format=^https?://…
Configuration validation failed: 2 error(s) found
```

### Inspect resolved environment variables (verbose mode)

```bash
./run-shc.sh -v exec CheckLocalConfig
```

Adding `-v` enables debug-level logging. Before running the schema validation, the controller dumps the **fully resolved** in-memory config tree — including every `env.VAR_NAME` value substituted with its actual environment variable content. This is the most reliable way to confirm that secrets injected via environment variables (e.g. `REGISTRY_PASSWORD`, `SERVERS_SSH_KEY`) are correctly loaded into the controller process.

---

## Infrastructure Connectivity

### Check SSH connectivity to all servers

```bash
./run-shc.sh exec CheckServersAreReachable
```

Uses Ansible to run a `ping` playbook against all hosts declared in `utils.ansible.inventory`. This confirms that the controller can open an SSH connection to every node, which is a prerequisite for any Ansible-based operation (installation, node reboots, etc.).

On success:

```
Pinging all configured servers via Ansible...
All configured servers are reachable
```

On failure, the Ansible output is surfaced and the command exits with a non-zero status indicating which host(s) could not be reached.

### Check Kubernetes cluster health

```bash
./run-shc.sh exec CheckKubernetesCluster
```

Fetches the kubeconfig, connects to the cluster API, and verifies:

- The number of nodes in the cluster matches the number of unique hosts in the Ansible inventory.
- Every node has a `Ready=True` condition.

On success:

```
Kubernetes cluster is healthy   nodes=3  expected=3
```

Fails immediately if any node is not Ready, or if the node count does not match the inventory (which may indicate a node that joined or was evicted without being reflected in the config).

---

## Local Artifact Checks

### Verify release files on disk

```bash
./run-shc.sh exec CheckLocalReleaseFiles
```

Iterates over every entry under `global.version` in your config (e.g. `platform`, `data.detection-rules`) and checks that:

1. The base directory (`path`) exists.
2. The version subdirectory (`path/<version>`) exists and is non-empty.

Useful after a `DownloadReleaseFiles` run to confirm that all expected archives are present before attempting an installation or update.

### Verify git repository access

```bash
./run-shc.sh exec CheckLocalGit
```

Clones the configured `utils.git.repo_url` into a temporary directory and tests both **pull** and **push** access using the configured credentials. Use this to validate that the git token has sufficient permissions before running any module that writes ArgoCD stacks to the repository.

### Verify OCI registry access

```bash
./run-shc.sh exec CheckLocalOCIRegistry
```

Connects to `utils.oci_registry.url` and verifies **push**, **pull**, and **delete** access. Push is tested first; if it fails, pull and delete are skipped and reported as untested. Use this to confirm registry credentials before pushing Helm charts or images.

---

## Service and Application Health

### ArgoCD status dashboard

```bash
./run-shc.sh exec DebugArgoCD
```

Connects to the ArgoCD API and renders three tables in the terminal:

| Table | Content |
|---|---|
| **Repositories** | Name, URL, and type of every registered ArgoCD repository |
| **Root Application** | Sync and health status of the root app-of-apps |
| **Applications** | Per-application sync status and health status, sorted alphabetically |

Sync statuses are colour-coded: `Synced` in green, `OutOfSync` in red. Health statuses: `Healthy` in green, `Progressing` in yellow, `Degraded`/`Missing` in red.

This is the first command to run when investigating a broken or partially deployed platform.

### Force a full re-synchronisation

```bash
./run-shc.sh exec DebugArgoCDSyncAll
```

Triggers a three-phase synchronisation of **all** ArgoCD applications in parallel:

1. **Partial sync** — for each application, syncs only resources whose `kind` matches a configurable regex (default: `secretgenerator|configmap`). This refreshes ConfigMaps and SecretGenerator objects before secrets are regenerated.
2. **Operator restart** — rolls out the `sekoiaio-secret-operator` deployment in the `support` namespace and waits for it to come back up (default: 60 s), ensuring it picks up the refreshed SecretGenerators.
3. **Full sync** — syncs every application in its entirety.

Use this when applications are stuck in `OutOfSync`, after a manual change to the ArgoCD git repository, or after a platform upgrade.

> **Note:** The sync timeout per application defaults to 300 s and up to 32 applications are synced concurrently. Both values can be overridden in `config.yml` under `modules.debug_argocd_sync_all`.

---

## Secret Diagnostics

### Audit missing or incomplete secrets

```bash
./run-shc.sh exec DebugMissingSecrets
```

Compares the desired state (every `SecretGenerator` CRD declared via `secretoperator.sekoia.io/v1alpha1`) against the actual Kubernetes `Secret` objects present in the cluster, and reports:

- Secrets that are entirely missing (the CRD exists but no `Secret` was created).
- Secrets that exist but have incomplete keys.
- For each missing key: the vault path where the value is expected to come from.

Additionally, the module runs a `platform-installer dumpconfig` job and cross-references each missing secret against the platform-installer configuration, helping distinguish between secrets that were never defined versus secrets that failed to be generated.

### Scan ArgoCD stacks for unrendered template placeholders

```bash
./run-shc.sh exec DebugKustomizeStacksTemplates
```

Clones (or pulls) the ArgoCD git repository and recursively scans every YAML file for values that still contain the `SH_TMPL` marker — the sentinel string used by the stack templater to indicate a value that should have been substituted. For each match, the following is logged:

- File path and document index within a multi-document YAML file
- Kubernetes `kind` and `metadata.name` of the affected object
- Dot-separated YAML path to the offending field and its current value

A summary of occurrences per YAML path (sorted by frequency) is printed at the end. Use this when services fail to start due to misconfigured values that were not properly rendered during installation.

---

## Database Diagnostics

### Inspect database pod health

```bash
./run-shc.sh exec DebugDatabases
```

Inspects the `support` namespace and renders two tables:

**StatefulSets** — covers non-CNPG databases (e.g. Redis, ClickHouse):

| Column | Description |
|---|---|
| Name | StatefulSet name |
| Expected / Ready | Declared vs. ready replica count |
| Status | `Healthy` / `Warning` / `Unhealthy` (colour-coded) |
| Restarts | Total container restarts across all pods |
| Last Restart | Human-readable age of the most recent restart (e.g. `5m ago`) |
| Issues | Per-pod issues: `not ready`, `waiting (CrashLoopBackOff)`, `crashed Xm ago`, etc. |

**CNPG Clusters** — same columns for all CloudNativePG `postgresql.cnpg.io/v1` clusters (e.g. the platform PostgreSQL instances).

A pod is flagged as having a **recent restart** if its last termination timestamp is within the past 10 minutes. Status is `Unhealthy` if any replica is not ready or not in `Running` phase; `Warning` if all replicas are running but recent restarts or waiting containers were detected.

---

## Cluster Resource Management

### RAM allocation waste report

```bash
./run-shc.sh exec DebugResourceAllocation
```

Queries the Kubernetes Metrics API (`metrics.k8s.io/v1beta1`) for live memory consumption across all namespaces, then compares it against each pod's declared memory `requests`. The output is two tables:

**RAM Allocation — Waste Report** — all pods that declare a memory request, sorted by wasted RAM descending:

| Column | Description |
|---|---|
| Namespace / Pod | Pod identity |
| Request | Declared memory request |
| Usage | Live memory consumption from the Metrics API |
| Waste | `request − usage` |
| Waste % | Colour-coded: green < 50 %, yellow ≥ 50 %, red ≥ 80 % |

**Pods Without Memory Requests** — pods for which no `resources.requests.memory` is set, shown with their current usage. These pods are a scheduling risk as Kubernetes cannot make informed placement decisions for them.

> **Prerequisites:** The Metrics Server must be deployed in the cluster. If the Metrics API is unavailable, the command exits with an error suggesting you run the `HelmInstall` module first.

---

## Platform Installer Debug

### Launch a paused installer job

```bash
./run-shc.sh exec DebugPlatformInstallation
```

Deploys the `platform-installer` Helm chart with a `pause` command override instead of the normal install/update sequence. The job pod starts and stays alive without performing any changes, giving you an interactive shell to inspect the installer environment, mounted secrets, and configuration files. Any stale release from a previous debug session is cleaned up automatically before deploying.

Use this when you need to manually inspect or test the platform-installer's runtime context without triggering a full installation.
