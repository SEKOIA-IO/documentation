# Monitor your platform

Sekoia Self-Hosted ships with a complete observability stack and a set of on-demand diagnostic commands so you can monitor cluster health, application status, and resource usage in real time. This guide explains how to use both layers for daily monitoring and incident response.

## Before you begin

- You completed the deployment and validated post-deployment checks in [Deploy the platform](../deployment/deployment_guide.md).
- You have access to the Grafana interface at `https://<global.host>/grafana`.
- For SHC diagnostic commands, you must run them from the orchestration node provisioned during installation.

## Monitoring layers

Sekoia Self-Hosted provides two complementary monitoring layers.

| Layer | Tools | Purpose |
| :--- | :--- | :--- |
| Continuous monitoring | Grafana, Loki, Prometheus | Real-time dashboards, log search and metric collection. |
| On-demand diagnostics | Self-Hosted Controller (SHC) CLI | Targeted health checks on the cluster, applications, databases, and resources. |

Use Grafana for daily operations and trend analysis. Use SHC commands for incident triage, post-deployment validation, and structured platform snapshots.

## Use Grafana for continuous monitoring

### Navigate to the dashboard

To access Grafana:

1. Open `https://<global.host>/grafana` in your browser.
2. Select **Dashboards** from the left navigation panel.
3. Open the **Default** dashboard.

!!! info "Available dashboards"
    The platform ships with two dashboards: **Default** and **Astreinte**. The Astreinte dashboard is an internal on-call tool used by the Sekoia operations team. It is not intended for platform operators and should not be consulted during normal operations. Only the **Default** dashboard is relevant for day-to-day monitoring.

### Default dashboard

The Default dashboard is the primary monitoring view for a Self-Hosted deployment. It is organized into collapsible rows, each covering a different layer of the platform. Expand a row to display its panels.

!!! warning "Elasticsearch panels"
    The **Elasticsearch** row and any individual panel referencing Elasticsearch (ES) are not applicable to Self-Hosted deployments. Elasticsearch is not deployed. Ignore those panels when they appear.

#### Global info

A row of summary statistics at the top of the dashboard provides an at-a-glance overview of the entire platform.

| Panel | What it shows |
| :--- | :--- |
| Bytes In | Volume of valid events processed by the ingestion pipeline. |
| Bits in (network) | Network-level ingestion throughput. |
| Load all nodes | 5-minute CPU load average per node (bar gauge). |
| RAM used % | RAM utilization percentage per node (bar gauge). |
| Time drift > 1s | Nodes whose system clock has drifted more than one second. |
| API Response Time | Average response time across all platform APIs. |
| Celery Tasks | Number of pending Celery background tasks. |
| Node Load | Aggregate node CPU load. |
| Kube | Kubernetes pod health summary. |
| PVC Usage | Persistent Volume Claim capacity utilization. |
| Clickhouse Status | ClickHouse cluster availability. |
| Alertmanager status | *(Alertmanager is not deployed in Self-Hosted — ignore.)* |
| Storage used (!= Ceph) | Storage consumption for non-Ceph volumes. |
| API Error Rate | Proportion of API requests returning 5xx errors. |
| Event to alert delay | End-to-end latency from event ingestion to alert creation. |
| Ingestion | Current event ingestion rate (EPS). |
| FS Usage | Filesystem usage per node. |
| Pods Failed / Pending / Unknown | Count of pods not in a running state. |
| AVG P75 event to ES | *(Elasticsearch — ignore.)* |
| ES cluster health | *(Elasticsearch — ignore.)* |
| Ceph cluster health | *(Ceph is not deployed in Self-Hosted — ignore.)* |
| Storage used (Ceph) | *(Ceph is not deployed in Self-Hosted — ignore.)* |

#### Resource observations of ingest

CPU and memory usage for the ingestion service pods, showing consumption relative to declared requests and limits.

#### CPU usage vs request

CPU and RAM usage relative to declared requests and limits for the main processing services: `oc-pre-parser`, `sigma-workflow`, and `eventindexer-ls`. Also includes cluster-wide CPU wasted and RAM wasted metrics.

!!! note
    The Elasticsearch panels in this row are not applicable to Self-Hosted deployments.

#### Global workflow

End-to-end view of the event processing pipeline. Each panel represents one stage, from intake to alerting.

| Panel | Stage |
| :--- | :--- |
| HTTP intake RS | HTTP-based event intake rate. |
| Syslog intake | Syslog-based event intake rate. |
| Ingest | Event parsing and normalization (`sic.intake.events_parser` → `sic.to-enrich-event`). |
| Ingest Best Effort | Best-effort ingestion pods throughput. |
| oc-pre-parser | Pre-parsing stage (`sic.raw-ecs2`). |
| Pre-parser EPS per community | Events per second broken down per community. |
| sigma-workflow | Sigma rule matching and enrichment. |
| Correlation Worker | Correlation engine throughput. |
| eventindexer-ls | Event indexing (`sic.enriched-event` → `sic.event`). |
| Quickwit forwarder | Forwarding enriched events to Quickwit (`workflow.enriched-events`). |
| Quickwit Indexation realtime | Real-time Quickwit indexation rate. |
| Alerts | Alert generation rate. |
| Rate-limited alerts | Alerts rate-limited by community and rule. |
| Telemetry | Telemetry pipeline throughput. |

#### KeyDB

Cache database metrics: total items stored, commands executed per second, memory usage, replication offset, and RDB snapshot state.

#### ArangoDB

ArangoDB metrics: PVC usage in percentage and GB, RAM usage in percentage and GB, and CPU consumption.

#### Symphony

Symphony orchestration engine pod status (running, pending, failed).

#### Workflow

Observable tag compilation throughput.

#### Redis

Redis cache metrics: total items stored, RAM utilization, and RDB snapshot state.

#### PostgreSQL

Relational database metrics: CPU usage, memory usage, active connections, locks, row activity across tables, and storage consumption.

#### APIs

API service health: 500-level error rate and mean response time across all platform APIs.

#### Celery

Background task queue metrics: tasks waiting, 95th-percentile task duration, task throughput per second, task status distribution, and exception rates per application.

#### Kafka

Event streaming metrics: consumer lag per topic and consumer group, Kafka log size by topic and broker, offline partitions, messages and bytes in/out per topic, CPU usage relative to pod limits, underreplicated partitions, and consumer group rebalancer activity.

#### Elasticsearch

!!! warning "Not applicable"
    Elasticsearch is not deployed in Self-Hosted. All panels in this section can be ignored.

#### Kube

Kubernetes-level resource consumption: total pod memory and CPU usage aggregated across all namespaces.

#### Clickhouse

ClickHouse database metrics: read-only replica count and files pending insertion.

#### Ceph

Rook/Ceph distributed storage metrics: disk I/O time per second, slow disks detection (I/O time > 0.97), CPU and RAM usage, disk usage per OSD, estimated days before 90% capacity is reached, bytes and operations read/write per second, apply latency, and monitor election activity.

#### Longhorn

!!! note "Deployment-dependent"
    Longhorn is not deployed in standard Self-Hosted configurations, which use Rook/Ceph. This section will show no data unless Longhorn has been explicitly configured.

Longhorn storage metrics: disk I/O time per second, disk usage percentage, read and write IOPS, read and write throughput (bytes/s), and read and write latency.

#### Servers (per node)

Per-node Linux-level metrics with a `$instance` variable to filter by node: CPU usage, memory usage, network traffic per interface, 5-minute CPU load average, and disk free space.

### Search logs with Loki

Promtail agents run on every node and ship all container logs to a Loki cluster. To search logs:

1. Select **Explore** from the left navigation panel.
2. In the data source selector, choose **Loki**.
3. Enter a LogQL query to filter by namespace, pod, application label, or time range.

??? example "Example LogQL queries"
    Filter all logs from the `support` namespace:
    ```
    {namespace="support"}
    ```
    Filter logs from a specific pod containing an error:
    ```
    {namespace="support", pod="redis-0"} |= "error"
    ```

## Use SHC commands for on-demand diagnostics

### Check cluster node health

To confirm all Kubernetes nodes are ready, run:

```bash
./run-shc.sh exec CheckKubernetesCluster
```

??? example "Expected output"
    ```
    Kubernetes cluster is healthy nodes=6 expected=6
    ```

Run this command first when investigating any platform issue. A mismatch between actual and expected node counts indicates that a node did not join or was evicted.

### Check application status

To inspect every ArgoCD application's sync and health state, run:

```bash
./run-shc.sh exec DebugArgoCD
```

The command renders three panels: registered repositories, root application status, and a per-application table.

| Sync status | Health status | Meaning |
| :--- | :--- | :--- |
| Synced | Healthy | Application is running as expected. |
| Synced | Progressing | Application is starting or rolling out. Normal for a few minutes after deployment. |
| OutOfSync | Any | Live state diverges from the ArgoCD source. Run `DebugArgoCDSyncAll` to recover. |
| Any | Degraded or Missing | A service failed to start or its resources could not be created. Inspect pod logs. |

### Check database health

To inspect all database StatefulSets and PostgreSQL clusters, run:

```bash
./run-shc.sh exec DebugDatabases
```

All entries must report `Healthy` status with the expected number of ready replicas. A `Warning` status indicates recent restarts. An `Unhealthy` status indicates one or more replicas are not ready.

### Check resource allocation

To review memory requests versus actual consumption across all pods, run:

```bash
./run-shc.sh exec DebugResourceAllocation
```

!!! note "Metrics Server required"
    This command queries the Kubernetes Metrics API. If the Metrics Server is not deployed, the command exits with an actionable error. Run `HelmInstall` to deploy it.

The output surfaces pods with over-provisioned memory requests (highlighted in red for 80% waste or more) and pods without any memory request declared (a scheduling risk).

## Recommended daily monitoring workflow

1. Open the **Default** dashboard in Grafana. Review the **Global info** row: check that no pods are failed or pending, that the API error rate and event-to-alert delay are within normal bounds, and that PVC and filesystem usage are not approaching saturation.
2. Expand the **Global workflow** row. Verify that ingestion, pre-parsing, sigma-workflow, and Quickwit indexation are all processing events at the expected rate and that no stage shows a backlog.
3. Expand the **Kafka** row. Confirm consumer lag is stable and no topics have offline or underreplicated partitions.
4. Expand the **Ceph** row. Check disk usage percentage, estimated days before capacity is reached, and confirm no slow disks are reported.
5. Review active alerts in Prometheus. Acknowledge or escalate as needed.

## Recommended incident response workflow

When an alert fires or a dashboard shows degradation, run the following commands in order to isolate the failing layer:

```bash
# 1. Confirm all cluster nodes are ready
./run-shc.sh exec CheckKubernetesCluster

# 2. Check application sync and health
./run-shc.sh exec DebugArgoCD

# 3. Inspect database availability
./run-shc.sh exec DebugDatabases

# 4. Review resource allocation
./run-shc.sh exec DebugResourceAllocation
```

This sequence moves from infrastructure layer to application layer to database layer to resource layer. Each step scopes the investigation before you move on.

If applications show `OutOfSync` or `Degraded` after running `DebugArgoCD`, continue with [Debug your deployment](../troubleshooting/debug_tool.md).

## Related links

- [Debug your deployment](../troubleshooting/debug_tool.md): Full SHC debug command reference with remediation steps.
- [Deploy the platform](../deployment/deployment_guide.md): Post-deployment validation commands.
- [Technical requirements](../deployment/deployment_prerequisites.md): Compute node and S3 storage requirements.
