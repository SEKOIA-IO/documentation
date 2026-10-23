# Monitor your platform

Sekoia Self-Hosted ships with a complete observability stack and a set of on-demand diagnostic commands so you can monitor cluster health, application status, and resource usage in real time. This guide explains how to use both layers for daily monitoring and incident response.

## Before you begin

- You completed the deployment and validated post-deployment checks in [Deploy the platform](../deployment/deployment_guide.md).
- You have access to the Grafana interface at `https://<global.delivery_host>/grafana`.
- For self-hosted-controller (SHC) diagnostic commands, you must run them from the orchestration node provisioned during installation.

## Monitoring layers

Sekoia Self-Hosted provides two complementary monitoring layers.

| Layer | Tools | Purpose |
| :--- | :--- | :--- |
| Continuous monitoring | Grafana, Loki, Prometheus | Real-time dashboards, log search and metric collection. |
| On-demand diagnostics | self-hosted-controller (SHC) CLI | Targeted health checks on the cluster, applications, databases, and resources. |

Use Grafana for daily operations and trend analysis. Use SHC commands for incident triage, post-deployment validation, and structured platform snapshots.

## Use Grafana for continuous monitoring

### Navigate to the dashboard

To access Grafana:

1. Open `https://<global.delivery_host>/grafana` in your browser.
2. Select **Dashboards** from the left navigation panel.
3. Open the **Default** dashboard.

!!! note "Available dashboards"
    The platform ships one dashboard, **Default**, provisioned by the installer.

### Default dashboard

The Default dashboard is the primary monitoring view for a Self-Hosted deployment. It is organized into rows, each covering a different layer of the platform. The **Global info** and **Global workflow** rows are expanded by default. Expand any other row to display its panels.

!!! note "Panels based on Ceph metrics"
    The Ceph metrics are not collected in Self-Hosted. Panels that read them stay empty: **Ceph cluster health** and **Storage used (Ceph)** in the **Global info** row, and the Ceph cluster panels of the **Ceph** row. To check the Ceph status, use the Storage tab of the [SHC interface](../operations/controller_interface.md).

The rows appear in the following order.

#### PVC usage

Usage of every persistent volume claim, in percentage and in free space (GB).

#### CPU/RAM reservations vs usage

CPU usage relative to the CPU request, RAM usage relative to the memory limit, and the CPU and RAM reserved but not used, for every pod.

#### Global info

A row of summary panels that gives an at-a-glance overview of the whole platform.

| Panel | What it shows |
| :--- | :--- |
| Ceph cluster health | Health of the Ceph cluster. Empty in Self-Hosted. |
| Bytes In | Ingested bytes per second across the syslog chain (`oc-pre-parser`) and the HTTP chain (`sic-intake-http-rs`). |
| Load all nodes (5 minutes) | Number of nodes in each 10% bucket of 5-minute CPU load per core, over time. |
| RAM used % | Number of nodes in each 10% bucket of RAM usage, over time. |
| Time drift > 1s | Nodes whose clock drifts by more than one second. |
| Storage used (Ceph) | Space used in the Ceph cluster. Empty in Self-Hosted. |
| API Response Time | Highest mean response time across the platform APIs, read from their logs. |
| Celery Tasks | Highest Celery queue length, when it exceeds 1,000 tasks. |
| Node Load | Highest 5-minute CPU load per core across the nodes. |
| Kube | Deployments, StatefulSets, or DaemonSets that do not have all their replicas ready. |
| PVC Usage | Highest usage of a persistent volume claim, in percentage. |
| Clickhouse Status | ClickHouse read-only replicas, and the growth of the distributed insert backlog. |
| Alertmanager status | Rate of notifications that the local Alertmanager drops because its queue is full. A value above zero means that alerts are lost. |
| Storage used (!= Ceph) | Space used on the node disks, excluding the Ceph volumes. |
| API Error Rate | Highest rate of 5xx responses of a platform API, when it exceeds 5, read from the API logs. |
| Event to alert delay | Average delay between the ingestion of an event and the creation of its alert. |
| Ingestion | Highest consumer lag on the ingestion and detection topics, when it exceeds 500 messages and keeps growing. |
| FS Usage | Highest usage of a persistent volume claim or a node filesystem, when it exceeds 75%. |
| Pods Failed \| Pending \| Unknown | Number of pods in the Failed, Pending, or Unknown phase, when it exceeds 15. |

#### Global workflow

End-to-end view of the event processing pipeline. Each panel represents one stage or service, from intake to alerting and indexation.

| Panel | What it shows |
| :--- | :--- |
| sic-intake-http-rs | HTTP intake: accepted requests, rejected requests, and accepted events. |
| ingestworker1 | Event parsing: events waiting on `sic.intake.events_parser`, consumer lag, and events processed. |
| sigma-workflow-worker1 | Detection: incoming events, processed events, and consumer lag. |
| sigma-workflow-correlation | Correlation: processed events, matches, and consumer lag. |
| quickwit-forwarder | Forwarding of the enriched events to ExaLog: consumer lag, consumption rate, and forwarded messages. |
| sic-intake-rsyslog | Syslog and RELP intake: events received. |
| oc-pre-parser | Pre-parsing: events produced and consumed on `sic.raw-ecs2`, and consumer lag. |
| Pre-parser EPS per community | Valid events per second, per community. |
| sicalertapi-sightings-worker | Alert creation: sightings processed, processing errors, and discarded sightings. |
| Rate-limited alerts by community and rule | Sightings discarded by the rate limit, per community and per detection rule. |
| telemetryworker-events | Telemetry: incoming events, processed events, and consumer lag. |
| Quickwit indexers - documents/sec | Documents processed per second by the ExaLog indexers, by outcome. |
| Quickwit indexers - CPU / RAM (% of limit) | CPU and memory usage of the ExaLog indexers, relative to their limits. |
| Quickwit indexers - throughput to S3 | Bytes uploaded to and downloaded from the object storage by the ExaLog indexers. |
| Quickwit indexers - S3 request status | Object storage requests of the ExaLog indexers, by outcome. |

#### KeyDB

Cache database metrics: total items, commands executed per second, memory usage, replication offset of the read-only replicas, and changes since the last snapshot.

#### ArangoDB

ArangoDB metrics: PVC usage in percentage and GB, RAM usage in percentage and GB, and CPU usage.

#### Symphony

Playbook execution metrics: pod status, Celery tasks of the action workers by status, queued tasks, jobs per community, and task exceptions.

#### Workflow

Observable tag compilation: compiled observables, compilation failures, and time since the last update.

#### Redis

Redis metrics: total items, RAM usage, and changes since the last snapshot.

#### PostgreSQL (CloudNativePG)

PostgreSQL cluster metrics: instances with their role and state, CPU, memory, and storage usage relative to their limits, WAL generation rate and archive backlog, collector and operator errors, and PgBouncer client connections, server connections, and query throughput.

#### APIs

API service health, read from the API logs: rate of 5xx responses and mean response time, per service.

#### Celery

Background task metrics: queued tasks, 95th percentile task duration, tasks per second, tasks by status, and task exceptions.

#### Kafka

Event streaming metrics: consumer lag per topic and consumer group, lag per detection worker, log size by topic and by broker, offline partitions, messages and bytes in and out per topic, CPU and memory usage of the brokers, bytes in per broker, partitions per topic, under-replicated partitions per topic, in-sync replica expansions, and consumer group rebalances.

#### Kube

Kubernetes resource consumption: memory and CPU usage of every pod.

#### Clickhouse

ClickHouse metrics: read-only replicas and files waiting for distributed insertion.

#### Ceph

Storage metrics. The disk I/O time per device, the slow disk detection, and the CPU and RAM usage of the Ceph OSD pods work in Self-Hosted. The other panels stay empty: disk usage, estimated days before 90% usage, disk space delta, `node_disk_io_time_weighted`, usage per pool and per OSD, bytes and operations read and written, apply latency, and monitor elections.

#### ExaLog

ExaLog indexation and search metrics: cluster nodes and gossip traffic, internal gRPC requests and latency, control plane shards, scheduling, and metastore errors, documents forwarded per second, ingest write-ahead log throughput and usage, active ingest shards and in-flight messages, searcher cache size and efficiency, search tasks and outcomes, object storage reads in flight, CPU and memory usage per pod, network traffic per pod, metastore connections, and HTTP requests by status.

#### Servers $instance

Per-node Linux metrics, filtered with the `$instance` variable: CPU usage, memory usage, network traffic per interface, 5-minute CPU load, disk free space, and the CPU and RAM consumption of the pods running on the node.

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

For targeted checks on specifics services or layers of the platform using Prometheus metrics, follow [Run platform diagnostics](run_diagnostics.md).

### Check cluster node health

To confirm all Kubernetes nodes are ready, run:

```bash
exec CheckKubernetesCluster
```

??? example "Expected output"
    ```
    Kubernetes cluster is healthy nodes=6 expected=6
    ```

Run this command first when investigating any platform issue. A mismatch between actual and expected node counts indicates that a node did not join or was evicted.

### Check application status

To inspect every ArgoCD application's sync and health state, run:

```bash
exec DebugArgoCD
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
exec DebugDatabases
```

All entries must report `Healthy` status with the expected number of ready replicas. A `Warning` status indicates recent restarts. An `Unhealthy` status indicates one or more replicas are not ready.

### Check resource allocation

To review memory requests versus actual consumption across all pods, run:

```bash
exec DebugResourceAllocation
```

!!! note "Metrics Server required"
    This command queries the Kubernetes Metrics API. If the Metrics Server is not deployed, the command exits with an actionable error. Run `HelmInstall` to deploy it.

The output surfaces pods with over-provisioned memory requests (highlighted in red for 80% waste or more) and pods without any memory request declared (a scheduling risk).

## Recommended daily monitoring workflow

1. Open the **Default** dashboard in Grafana. Review the **Global info** row: check that no pods are failed or pending, that the API error rate and event-to-alert delay are within normal bounds, and that PVC and filesystem usage are not approaching saturation.
2. Expand the **Global workflow** row. Verify that ingestion, pre-parsing, sigma-workflow, and ExaLog indexation are all processing events at the expected rate and that no stage shows a backlog.
3. Expand the **Kafka** row. Confirm consumer lag is stable and no topics have offline or underreplicated partitions.
4. Expand the **PVC usage** and **Ceph** rows. Check that no volume approaches saturation and that no slow disk is reported.
5. Review the firing alerts. See [Platform alerts reference](platform_alerts.md).

## Recommended incident response workflow

When an alert fires or a dashboard shows degradation, run the following commands in order to isolate the failing layer:

```bash
# 1. Confirm all cluster nodes are ready
exec CheckKubernetesCluster

# 2. Check application sync and health
exec DebugArgoCD

# 3. Inspect database availability
exec DebugDatabases

# 4. Review resource allocation
exec DebugResourceAllocation

# 5. Check the affected platform service
exec Diagnostic
```

This sequence moves from infrastructure layer to application layer to database layer to resource layer to service layer. Each step scopes the investigation before you move on.

If applications show `OutOfSync` or `Degraded` after running `DebugArgoCD`, continue with [Debug your deployment](../troubleshooting/debug_tool.md).

## Related links

- [Run platform diagnostics](run_diagnostics.md): Targeted Prometheus health checks for platform services.
- [Use the SHC interface](../operations/controller_interface.md): Live node, cluster, storage, and diagnostics views in the interactive SHC interface.
- [Debug your deployment](../troubleshooting/debug_tool.md): Full SHC debug command reference with remediation steps.
- [Deploy the platform](../deployment/deployment_guide.md): Post-deployment validation commands.
- [Technical requirements](../deployment/deployment_prerequisites.md): Compute node and S3 storage requirements.
