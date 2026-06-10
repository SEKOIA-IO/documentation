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

### Navigate to the dashboards

To access the Grafana dashboards:

1. Open `https://<global.host>/grafana` in your browser.
2. Select **Dashboards** from the left navigation panel.
3. Select the dashboard you want to view.

> 📸 [SCREENSHOT SUGGESTION: Grafana dashboard list showing the prebuilt dashboards: Cluster health, Resource utilization, Throughput, Error rates, Security events. | ALT TEXT: Grafana dashboard selection screen with prebuilt Sekoia dashboards.]

The platform ships with the following prebuilt dashboards:

| Dashboard | Content |
| :--- | :--- |
| Cluster health | Node status, control-plane availability, Kubernetes events. |
| Resource utilization | CPU, memory, disk, and network usage per node and namespace. |
| Throughput | Event ingestion rate, processing latency, queue depth. |
| Error rates | Service-level error counts, HTTP status distribution. |
| Security events | Authentication failures, audit-log highlights. |

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

1. Open the **Cluster health** dashboard in Grafana. Confirm all nodes are ready and the control plane is responsive.
2. Check the **Resource utilization** dashboard. Watch for nodes or namespaces trending toward saturation.
3. Check the **Throughput** dashboard. Verify the ingestion rate is within the expected range and no queue is backing up.
4. Review active alerts in Alertmanager. Acknowledge or escalate as needed.

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
