# Run platform diagnostics

The Diagnostic module runs targeted health checks against the platform's Prometheus metrics. It reports the health of the nodes, the data stores, and each platform feature, so you can narrow an incident to the affected service.

## Prerequisites

- You have access to the orchestration node.
- The platform and its Prometheus service are running.
- The SHC can connect over SSH to the first manager node. When `utils.prometheus.url` is empty, which is the default, the `Diagnostic` module first runs `GetKubeconfig`, which copies the kubeconfig from that node and changes nothing on the cluster. See [Prometheus connection](#prometheus-connection).
- You completed the post-deployment validation in [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md).

!!! warning "Run diagnostics before changing the platform"
    Use the reported likely causes and remediation steps to investigate a failed check. Do not restart or reconfigure services based only on a diagnostic result.

## Run all diagnostic targets

To run every bundled diagnostic target, run:

```bash
exec Diagnostic
```

The module runs these targets in alphabetical order:

| Target | What it checks |
| :--- | :--- |
| `alerts` | The alerts pipeline: sightings worker progress, sighting processing error budget, `sicalertapi` Celery worker availability and task failures, `handle_sighting_from_redis` failures, and OC Events API worker task reception. |
| `asset_discovery` | The `assetdiscoveryworker` deployment: available replicas, consumption of the `ueba.facts` topic, reconciliation cycle duration, reconciliation conflict rate, fingerprint collisions, and failing discovery rules. |
| `asset_management` | The `assetmanagementapiv2` services: available replicas, compliance and event-notification worker consumption and error rates, risk-score recomputes skipped for missing assets, compiled asset inventory build failures, and an asset matcher that processes events without enriching them. |
| `clickhouse` | The ClickHouse cluster and its keeper ensemble: shards with no ready replica, replicas not ready, keeper availability, read-only tables, data volume usage, and the distributed insert backlog. |
| `console` | Access to the console, most likely cause first: the credentials store (Vault) sealed or down, the ingress and its TLS certificate (configured or served certificate expiring within 21 days, missing or invalid secret, failed TLS handshake, Traefik down, server error ratio on HTTPS requests, stale certificate exporter), the `front` deployment, the authentication service (`communityapi` availability, secret, and server error ratio), and the GraphQL gateway. |
| `indexation` | The ExaLog indexation pipeline: an indexer that stopped consuming (growing forwarder lag, forwarder not consuming, indexer producing no documents), object storage that returns errors, indexer local disk usage, and ready indexation nodes. |
| `ingest` | The ingestion path: intakes ingesting far above their own baseline, plan-based throttling to the dead-letter queue, accepted events not published to Kafka, a community whose ingestion collapses below its own baseline, the TLS certificate of the ingestion endpoints (configured or served certificate expiring within 21 days, missing or invalid secret, failed TLS handshake against Traefik, stale certificate exporter), and the reception and parsing stages with no available replica (HTTP intake, syslog intake, pre-parser, and parser workers). Each volume result names the community. Spike and throttling results also name the intake: its intake key on the syslog path, its intake UUID on the HTTP path. |
| `kafka` | The Kafka cluster and its ZooKeeper ensemble: ready brokers, broker data volume usage, `kafka-exporter` availability, abnormal controller state, offline and under-replicated partitions, ZooKeeper availability, a topic whose consumer backlog keeps growing, and replicas that keep leaving and re-entering the in-sync set, a sign of inter-node network latency or broker saturation. |
| `node` | The Kubernetes nodes and their local storage: nodes not ready or unreachable, cordoned nodes, disk and memory pressure, high memory and CPU load, clock drift, and the space and inode usage of the node filesystems and persistent volumes, with a 24-hour fill prediction. |
| `sigma_workflow` | The detection and correlation pipeline: uneven partition assignment across matcher workers, KeyDB key count disparity between replicas, growing consumer lag, correlation and rule compilation failures, correlation latency, deployments with no available replica, matchers not consuming events, alert-storm protection dropping sightings, and stalled sighting creation or sending. |
| `symphony` | Playbook execution: playbook pod and job counts by state, excess ConfigMaps, per-playbook job activity, action worker availability, and Celery queue backlog, retry, and API server error rates. |
| `telemetry` | The telemetry services: available replicas, consumption by the events, sightings, and notifications workers, and ClickHouse push failures. |

!!! note "Ceph storage pool"
    No target checks the Ceph storage pool, because the Ceph metrics are not collected in Self-Hosted. This is expected and does not indicate an incomplete deployment. The `node` target checks the persistent volumes that Ceph provides, but not the capacity of the Ceph pool or of its disks, which carry no node filesystem. To inspect Ceph, use the Storage tab of the [SHC interface](/self_hosted/1.0.1/operations/controller_interface.md), which shows the output of `ceph status`, `ceph osd df`, and `ceph osd tree`.

By default, the terminal report hides successful checks. Failed or warning checks show the affected value and labels, an explanation, likely causes, and remediation actions. Each check reports one of these statuses:

| Status | Meaning |
| :--- | :--- |
| `OK` | The check passed. |
| `WARN` | The value crossed the warning threshold of the check. |
| `CRIT` | The value crossed the critical threshold, or the check detected the problem it looks for. A check also reports `CRIT` when its query fails, or when a threshold check returns no data or a non-numeric value. |

The `Diagnostic` module is read-only: it queries Prometheus and changes nothing on the platform. The remediation actions of a failed check can contain `kubectl` commands. `kubectl get`, `describe`, `logs`, and `top` only read the cluster state. `kubectl rollout restart`, `delete pod`, `scale`, `cordon`, `uncordon`, `drain`, and `patch` change it: run them only once you have confirmed the cause. `kubectl exec` runs the command that follows it inside a pod.

## Run a diagnostic target

To investigate one platform area, set `modules.diagnostic.targets` to its target name:

```bash
exec Diagnostic --set modules.diagnostic.targets=alerts
```

To run more than one target, separate their names with commas:

```bash
exec Diagnostic --set modules.diagnostic.targets=alerts,telemetry
```

The module continues with the remaining targets when one target cannot be loaded or queried. For each target, the SHC logs a `diagnostic failed` error with the target name and the cause and the report holds no result for it. A misspelled target name produces the same error: check the name against the table in [Run all diagnostic targets](#run-all-diagnostic-targets). When no target produces results, the module prints no report.

## Change diagnostic output

To display successful checks as well as warnings and critical checks, set `modules.diagnostic.hide_ok` to `false`:

```bash
exec Diagnostic --set modules.diagnostic.targets=alerts --set modules.diagnostic.hide_ok=false
```

By default, `modules.diagnostic.format` is `rich`: the report is rendered with colors and tables in the terminal. To send the report to another tool, set it to `text` or `json`:

```bash
exec Diagnostic --set modules.diagnostic.format=json --set modules.diagnostic.hide_ok=false
```

To check which rules a target contains without querying Prometheus, set `modules.diagnostic.dry_run` to `true`. The module validates each rule file and lists its rules and data sources. It does not run `GetKubeconfig` and needs no access to the cluster:

```bash
exec Diagnostic --set modules.diagnostic.targets=node --set modules.diagnostic.dry_run=true
```

The `format` and `hide_ok` settings apply to the terminal report of the CLI. The Diagnostics tab of the SHC interface renders one panel per rule, successful ones included, whatever these settings are.

## Prometheus connection

By default, `utils.prometheus.url` is empty and the `Diagnostic` module reaches Prometheus through the Kubernetes API: it retrieves the kubeconfig with `GetKubeconfig`, then opens a port-forward to the Prometheus service of the platform for the duration of the run. When `GetKubeconfig` fails, the module stops with an error before it runs any check. `GetKubeconfig` is skipped for 300 seconds after a successful run in the same SHC session. When `utils.prometheus.url` is set, the module queries that URL directly and does not run `GetKubeconfig`.

The following keys control the connection. They are optional, set them in your `config.yml` only to reach Prometheus at another address or to allow slower queries.

| Field | Description | Default |
| :--- | :--- | :--- |
| `utils.prometheus.url` | Prometheus base URL, for example `http://prometheus.example.com:9090`. When set, the module queries this URL directly and opens no port-forward. When empty, it opens a port-forward to the service defined by the `utils.prometheus.port_forward` keys. | Empty |
| `utils.prometheus.query_timeout` | Maximum duration of each Prometheus query, in seconds. A query that exceeds it makes its check report `CRIT` with a `Query failed` explanation. | `10` |
| `utils.prometheus.port_forward.namespace` | Namespace of the Prometheus service. | `support` |
| `utils.prometheus.port_forward.resource` | Prometheus service targeted by the port-forward. | `svc/prometheus-server` |
| `utils.prometheus.port_forward.remote_port` | Port of the Prometheus service. | `80` |

Change the `utils.prometheus.port_forward` keys only with guidance from Sekoia: the defaults match the platform deployment.

## Run a diagnostic from the SHC interface

The interactive interface of the self-hosted-controller (SHC) exposes the same targets on its Diagnostics tab, with one collapsible panel per rule, live status, sortable result tables, and clipboard copy. You run one target at a time, or select **Run all diagnostics** to run every target in a single result view. See [Run a diagnostic from the Diagnostics tab](/self_hosted/1.0.1/operations/controller_interface.md#run-a-diagnostic-from-the-diagnostics-tab).

## Result

You have a diagnostic report for the selected platform areas. Use a `CRIT` result to prioritize investigation, and use a `WARN` result to identify degraded behavior before it interrupts service.

## Related links

- [Monitor your platform](/self_hosted/1.0.1/monitoring/monitoring_guide.md): Daily monitoring and incident-response workflows.
- [Platform alerts reference](/self_hosted/1.0.1/monitoring/platform_alerts.md): Platform alerts by type, and the diagnostic to run for each type.
- [Debug your deployment](/self_hosted/1.0.1/troubleshooting/debug_tool.md): Additional SHC diagnostic commands and log collection guidance.
- [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md): Post-deployment validation procedure.
- [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md): Run the same diagnostics from the interactive interface.
