# Monitoring

Sekoia Self-Hosted ships with a complete observability stack so you can monitor cluster health, application status, database availability, and resource consumption in real time. This page explains how the stack is organized, when to use which tool, and gives a full command reference for on-demand diagnostics.

This page is for platform administrators operating a Sekoia Self-Hosted instance. It covers both daily monitoring and incident response.

## Monitoring at a glance

Sekoia Self-Hosted provides two complementary monitoring layers:

| Layer | Tool | Purpose | When to use |
|---|---|---|---|
| **Continuous monitoring** | Grafana, Loki, Prometheus, Alertmanager | Real-time dashboards, log search, metric collection, alerting | Daily operations, capacity planning, alert-driven response |
| **On-demand diagnostics** | Self-Hosted Controller (SHC) CLI | Targeted health checks on cluster, applications, databases, and resources | Incident triage, post-deployment validation, troubleshooting |

In practice, you will spend most of your time in Grafana — dashboards and alerts surface issues as they happen. The SHC CLI is the tool you reach for when an alert fires, when a deployment looks wrong, or when you need a structured snapshot of platform state.

---

## Continuous monitoring: Grafana, Loki, Prometheus

The observability stack is deployed as part of the platform — no additional installation is required.

### Built-in dashboards

A set of Grafana dashboards is shipped with every release. They cover:

- **Cluster health** — node status, control-plane availability, Kubernetes events
- **Resource utilization** — CPU, memory, disk, and network usage per node and namespace
- **Throughput** — event ingestion rate, processing latency, queue depth
- **Error rates** — service-level error counts, HTTP status distribution
- **Security events** — authentication failures, audit-log highlights

You can customize these dashboards or add your own to fit your monitoring conventions.

### Centralized logs

Promtail agents run on every node and ship all container logs to a Loki cluster. Use Grafana's **Explore** view to search, filter, and inspect logs by service, namespace, pod, or time range.

Typical investigation flow:
1. Open Grafana → **Explore** → select the Loki data source
2. Filter by `namespace` and `pod` (or `app` label)
3. Narrow the time range to the incident window
4. Refine with substring or regex filters

### Metrics and alerting

Prometheus collects system- and application-level metrics across the platform. Alertmanager evaluates alerting rules and dispatches notifications.

- All metrics and alerts are visualized in Grafana.
- You can tune the default thresholds or add new rules to match your SLAs.
- Notifications can be routed to email (via the SMTP server configured at install time) or to any Alertmanager-compatible receiver.

### Retention and external forwarding

You can adjust log and metric retention to meet your compliance requirements. The stack also supports forwarding to external observability systems:

- **Metrics** — via Prometheus `remote_write`
- **Logs** — via the Loki HTTP API

---

## On-demand diagnostics: Self-Hosted Controller (SHC)

The Self-Hosted Controller (SHC) is a CLI that runs a set of targeted health checks against the cluster, ArgoCD, databases, and the Kubernetes Metrics API. It is the right tool for incident triage and structured platform snapshots.

### Prerequisites

- SHC commands are executed from the **admin node** provisioned during installation (see [Deployment prerequisites](../prerequisites/index.md)).
- All commands are invoked via the `run-shc.sh` wrapper script using the `exec` subcommand.
- The admin node must have network access to the Kubernetes API of the target cluster.
- For `DebugResourceAllocation`, the Kubernetes **Metrics Server** must be deployed. If it is not, the command exits with an actionable error — run the `HelmInstall` module first.

### When to use SHC vs Grafana

| Situation | Use |
|---|---|
| Routine monitoring, trend analysis, alert review | Grafana |
| An alert just fired and you need to confirm what's broken | SHC (`DebugArgoCD` first) |
| You just deployed or upgraded and want a clean health snapshot | SHC (full workflow, see below) |
| You want to inspect log content in detail | Grafana / Loki |
| You suspect over- or under-provisioned memory requests | SHC (`DebugResourceAllocation`) |

### Cluster node health

```bash
./run-shc.sh exec CheckKubernetesCluster
```

Connects to the Kubernetes API and performs two checks:

- The number of nodes in the cluster matches the number of unique hosts in the Ansible inventory.
- Every node reports a `Ready=True` condition.

On success:

```
Kubernetes cluster is healthy   nodes=3  expected=3
```

Run this first to confirm the cluster itself is healthy before investigating application-level issues.

### Application status

```bash
./run-shc.sh exec DebugArgoCD
```

Connects to the ArgoCD API and renders three terminal panels in sequence.

**Panel 1 — Repositories**

Lists every Git or Helm repository registered in ArgoCD:

| Column | Description |
|---|---|
| Name | Repository alias |
| URL | Remote URL |
| Type | `git` or `helm` |

**Panel 2 — Root application**

Displays the sync and health status of the root app-of-apps as a single-line summary:

```
Sync: Synced  |  Health: Healthy
```

**Panel 3 — Applications**

Lists all managed ArgoCD applications, sorted alphabetically:

| Column | Values |
|---|---|
| Name | Application name (with `-on-self-hosted` suffix stripped) |
| Sync Status | `Synced` (green) · `OutOfSync` (red) · `Unknown` (dim) |
| Health Status | `Healthy` (green) · `Progressing` (yellow) · `Degraded` / `Missing` (red) · `Suspended` (cyan) |

**Reading the output:**

- A row that is green on both columns is nominal.
- `OutOfSync` means the live cluster state diverges from the ArgoCD git source — run `DebugArgoCDSyncAll` to recover.
- `Progressing` is transient and expected during deployments; if it persists beyond a few minutes, check the pod logs for the affected application.
- `Degraded` or `Missing` indicates a service that failed to start or whose resources could not be created — use `DebugDatabases` and pod logs to investigate further.

> **Tip:** This is the first command to run when investigating a broken or partially deployed platform.

### Database health

```bash
./run-shc.sh exec DebugDatabases
```

Inspects the `support` namespace and renders two tables covering all database workloads.

**StatefulSets table**

Covers non-CNPG databases (e.g. Redis, ClickHouse, MinIO):

| Column | Description |
|---|---|
| Name | StatefulSet name |
| Expected | Declared replica count |
| Ready | Currently ready replicas |
| Status | `Healthy` (green) · `Warning` (yellow) · `Unhealthy` (red) |
| Restarts | Total container restarts across all pods |
| Last Restart | Human-readable age of the most recent restart (e.g. `5m ago`) |
| Issues | Per-pod detail: `not ready`, `waiting (CrashLoopBackOff)`, `crashed Xm ago` |

**CNPG Clusters table**

Same columns for all CloudNativePG (`postgresql.cnpg.io/v1`) clusters (platform PostgreSQL instances).

**Reading the output:**

- **Healthy** — all replicas are running and ready, no recent restarts.
- **Warning** — all replicas are running, but recent restarts (within the past 10 minutes) or waiting containers were detected. Monitor and re-run to see if the issue clears.
- **Unhealthy** — at least one replica is not ready or not in `Running` phase. Check the `Issues` column for the specific pod and reason, then inspect logs with `kubectl logs -n support <pod>`.

### Resource usage

```bash
./run-shc.sh exec DebugResourceAllocation
```

Queries the Kubernetes Metrics API (`metrics.k8s.io/v1beta1`) for live memory consumption across all namespaces and compares it against each pod's declared memory requests.

> **Prerequisite:** Metrics Server must be deployed. If the Metrics API is unavailable, the command exits with an actionable error — run the `HelmInstall` module first.

**RAM allocation — waste report**

All pods with a memory request declared, sorted by wasted RAM (highest first):

| Column | Description |
|---|---|
| Namespace | Kubernetes namespace |
| Pod | Pod name |
| Request | Declared `resources.requests.memory` |
| Usage | Live consumption from the Metrics API |
| Waste | Request − Usage |
| Waste % | Green < 50 % · Yellow ≥ 50 % · Red ≥ 80 % |

**Pods without memory requests**

A separate warning panel lists all pods for which no `resources.requests.memory` is set, alongside their current live usage. These pods are a scheduling risk — Kubernetes cannot make informed placement or eviction decisions for them.

**Reading the output:**

- Rows highlighted in red (≥ 80 % waste) indicate pods whose memory requests are significantly over-provisioned. Adjusting their requests downward reduces scheduling pressure across the cluster.
- Pods in the "Without Memory Requests" panel should be reviewed — if they consume significant memory without a declared request, they risk being evicted under node pressure.

---

## Recommended workflows

### Daily monitoring

For continuous operations, Grafana is the primary surface:

1. Review the **Cluster health** dashboard — confirm all nodes are Ready and the control plane is responsive.
2. Check the **Resource utilization** dashboard — watch for nodes or namespaces trending toward saturation.
3. Check the **Throughput** dashboard — verify ingestion rate is within expected range and no queue is backing up.
4. Review active alerts in Alertmanager — acknowledge or escalate as needed.

If any dashboard surfaces an anomaly, switch to the SHC workflow below to confirm the platform state before investigating further.

### Incident response

When an alert fires or a dashboard shows degradation, run the following sequence for a complete health snapshot:

```bash
# 1. Confirm all cluster nodes are ready
./run-shc.sh exec CheckKubernetesCluster

# 2. Check application sync and health status
./run-shc.sh exec DebugArgoCD

# 3. Inspect database availability
./run-shc.sh exec DebugDatabases

# 4. Review resource allocation efficiency
./run-shc.sh exec DebugResourceAllocation
```

This order is deliberate: cluster → applications → databases → resources. Each step rules out a layer before moving on, so when something fails you know roughly where to focus.

If applications appear `OutOfSync` or `Degraded` after running `DebugArgoCD`, see [Troubleshooting and debugging](./troubleshooting.md) for recovery procedures.