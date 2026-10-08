# Run platform diagnostics

The Diagnostic module runs targeted health checks against the platform's Prometheus metrics. It reports the health of the nodes, the data stores, and each platform feature, so you can narrow an incident to the affected service.

## Prerequisites

- You have access to the orchestration node.
- The platform and its Prometheus service are running.
- You completed the post-deployment validation in [Deploy the platform](../deployment/deployment_guide.md).

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
| `asset_discovery` | The `assetdiscoveryworker` deployment: available replicas, consumption of the `ueba.facts` topic, reconciliation cycle duration, reconciliation conflict rate, fingerprint collisions, fact production from XDR agent events, and failing discovery rules. |
| `asset_management` | The `assetmanagementapiv2` services: available replicas, compliance and event-notification worker consumption and error rates, risk-score recomputes skipped for missing assets, compiled asset inventory build failures, and an asset matcher that processes events without enriching them. |
| `clickhouse` | The ClickHouse cluster and its keeper ensemble: shards with no ready replica, replicas not ready, keeper availability, read-only tables, data volume usage, and the distributed insert backlog. |
| `indexation` | The ExaLog indexation pipeline: an indexer that stopped consuming (growing forwarder lag, forwarder not consuming, indexer producing no documents), object storage that returns errors, indexer local disk usage, and ready indexation nodes. |
| `ingest` | The syslog and HTTP ingestion chains: intakes ingesting far above their own baseline, plan-based throttling to the dead-letter queue, accepted events not published to Kafka, and a community whose ingestion collapses below its own baseline. Each result names the community and, where available, the intake key. |
| `kafka` | The Kafka cluster and its ZooKeeper ensemble: ready brokers, broker data volume usage, `kafka-exporter` availability, abnormal controller state, offline and under-replicated partitions, and ZooKeeper availability. |
| `node` | The Kubernetes nodes and their local storage: nodes not ready or unreachable, cordoned nodes, disk and memory pressure, high memory and CPU load, clock drift, and node filesystem and orchestration volume usage, with a 24-hour fill prediction. |
| `sigma_workflow` | The detection and correlation pipeline: uneven partition assignment across matcher workers, KeyDB key count disparity between replicas, growing consumer lag, correlation and rule compilation failures, correlation latency, deployments with no available replica, matchers not consuming events, alert-storm protection dropping sightings, and stalled sighting creation or sending. |
| `symphony` | Playbook execution: playbook pod and job counts by state, excess ConfigMaps, per-playbook job activity, action worker availability, and Celery queue backlog, retry, and API server error rates. |
| `telemetry` | The telemetry services: available replicas, consumption by the events, sightings, and notifications workers, and Clickhouse push failures. |

!!! note "Ceph storage pool"
    No target checks the Ceph storage pool itself, because the Ceph metrics are not collected. The `node` target covers the physical disks that Ceph uses through the node filesystem rules. To inspect Ceph, use the Storage tab of the [SHC interface](../operations/controller_interface.md).

By default, the terminal report hides successful checks. Failed or warning checks show the affected value and labels, an explanation, likely causes, and remediation actions.

## Run a diagnostic target

To investigate one platform area, set `modules.diagnostic.targets` to its target name:

```bash
exec Diagnostic --set modules.diagnostic.targets=alerts
```

To run more than one target, separate their names with commas:

```bash
exec Diagnostic --set modules.diagnostic.targets=alerts,telemetry
```

The module continues with the remaining targets when one target cannot be loaded or queried. Review the terminal error for each target that does not produce results.

## Change diagnostic output

To display successful checks as well as warnings and critical checks, set `modules.diagnostic.hide_ok` to `false`:

```bash
exec Diagnostic --set modules.diagnostic.targets=alerts --set modules.diagnostic.hide_ok=false
```

To send the report to another tool, set `modules.diagnostic.format` to `text` or `json`:

```bash
exec Diagnostic --set modules.diagnostic.format=json --set modules.diagnostic.hide_ok=false
```

To check which rules a target contains without querying Prometheus, set `modules.diagnostic.dry_run` to `true`. The module validates each rule file and lists its rules and data sources:

```bash
exec Diagnostic --set modules.diagnostic.targets=node --set modules.diagnostic.dry_run=true
```

The `json` and `text` formats apply to the terminal output. API callers receive the complete result set, including successful checks, regardless of the `hide_ok` setting.

## Run a diagnostic from the SHC interface

The interactive interface of the self-hosted-controller (SHC) exposes the same targets on its Diagnostics tab, with one collapsible panel per rule, live status, sortable result tables, and clipboard copy. See [Run a diagnostic from the Diagnostics tab](../operations/controller_interface.md#run-a-diagnostic-from-the-diagnostics-tab).

## Result

You have a diagnostic report for the selected platform areas. Use a `CRIT` result to prioritize investigation, and use a `WARN` result to identify degraded behavior before it interrupts service.

## Related links

- [Monitor your platform](monitoring_guide.md): Daily monitoring and incident-response workflows.
- [Platform alerts reference](platform_alerts.md): Platform alerts by type, and the diagnostic to run for each type.
- [Debug your deployment](../troubleshooting/debug_tool.md): Additional SHC diagnostic commands and log collection guidance.
- [Deploy the platform](../deployment/deployment_guide.md): Post-deployment validation procedure.
- [Use the SHC interface](../operations/controller_interface.md): Run the same diagnostics from the interactive interface.
