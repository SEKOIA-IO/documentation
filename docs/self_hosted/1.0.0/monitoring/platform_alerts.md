# Platform alerts reference

Sekoia Self-Hosted evaluates a set of Prometheus alert rules against the platform's infrastructure and services. This reference lists each alert group, the conditions that trigger an alert, its operational impact, and the diagnostic that helps you investigate it.

## How platform alerts work

Prometheus continuously evaluates the alert rules bundled with the platform and forwards any firing alert to the Alertmanager instance installed on the platform.

!!! note "Where to check firing alerts"
    Review active alerts from the Prometheus **Alerts** page, or from the relevant row of the **Default** Grafana dashboard, which surfaces the underlying metrics for each alert group. See [Monitor your platform](monitoring_guide.md) for the full dashboard reference.

!!! warning "Investigate before taking action"
    A firing alert can cascade into ingestion, correlation, and alerting delays across the whole platform. Follow the [recommended incident response workflow](monitoring_guide.md#recommended-incident-response-workflow) to confirm cluster and database health before restarting or scaling affected resources.

Alerts are grouped by type, one type per infrastructure component or service. For each type, a global diagnostic analyzes the whole group: it identifies the affected component, explains the likely causes, and proposes remediations. When an alert fires, run the diagnostic of its type from the orchestration node. See [Run platform diagnostics](run_diagnostics.md) for the output formats and how to read a result.

## Kafka alerts

This group monitors the health of the Kafka message broker cluster and its Zookeeper dependency. To learn more about a Kafka alert and get remediation steps, run the Kafka diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=kafka
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| KafkaNoReadyBrokers | Critical | No Kafka broker pod is ready for 1 minute. | The Kafka cluster is entirely down. Event ingestion, correlation, and alerting stop. |
| KafkaBrokerUnavailable | Critical | Fewer broker pods are ready than the expected replica count, for 1 minute. | At least one broker is down. The cluster keeps serving traffic but with reduced capacity and fault tolerance. |
| KafkaBrokerDiskUsageHigh | Critical | A broker's data volume usage exceeds 90% for 5 minutes. | A broker is close to running out of disk space. Without action, it can stop accepting writes or lose data. |
| KafkaExporterUnavailable | Critical | The `kafka-exporter` deployment has 0 available replicas for 1 minute. | Kafka metric collection stops. The cluster may still be healthy, but Grafana and diagnostic checks lose visibility into it. |
| KafkaAbnormalControllerState | Critical | The cluster does not report exactly one active controller for 1 minute. | Cluster coordination is unstable, which can delay partition leader elections and metadata changes. |
| KafkaOfflinePartitions | Critical | One or more partitions have no active leader for 1 minute. | Producers and consumers cannot read or write to the affected partitions. |
| KafkaUnderReplicatedPartitions | Warning | One or more partitions have fewer in-sync replicas than configured, for 1 minute. | The affected topics have reduced fault tolerance. A further broker failure can cause data loss or unavailability. |
| KafkaZookeeperUnavailable | Critical | No Zookeeper pod is ready for 1 minute. | Kafka cluster coordination and broker registration are unavailable, which can prevent the cluster from recovering from other failures. |

<!--
Template for a new alert group. Copy it above "Related links" and keep one row per alert rule.

## <Component> alerts

This group monitors <scope>. To learn more about a <Component> alert and get remediation steps, run the <Component> diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=<target>
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| <AlertName> | Critical or Warning | <condition and duration> | <operational impact> |
-->

## Related links

- [Monitor your platform](monitoring_guide.md): Daily monitoring and incident-response workflows, including the Grafana dashboard reference.
- [Run platform diagnostics](run_diagnostics.md): Targeted Prometheus health checks to narrow an incident to the affected service.
- [Debug your deployment](../troubleshooting/debug_tool.md): Full SHC debug command reference with remediation steps.
