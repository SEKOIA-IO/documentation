# Platform alerts reference

Sekoia Self-Hosted evaluates a set of Prometheus alert rules against the platform's infrastructure and services. This reference lists each alert group, the conditions that trigger an alert, its operational impact, and the diagnostic that helps you investigate it.

## How platform alerts work

Prometheus evaluates the alert rules bundled with the platform every 15 seconds and forwards any firing alert to the Alertmanager instance installed on the platform. In Sekoia Self-Hosted 1.0.1, Alertmanager has no notification receiver configured: a firing alert is not sent by email or to any external tool. Review the alerts in Grafana.

!!! note "Where to check firing alerts"
    Prometheus and Alertmanager are not exposed outside the cluster: only Grafana has an ingress. To review the alert rules and their state, open `https://<global.delivery_host>/grafana`, then select **Alerting > Alert rules**. The platform alerts appear as data-source-managed rules of the Prometheus data source, grouped by alert group, with their `Normal`, `Pending`, or `Firing` state. The rows of the **Default** Grafana dashboard show the underlying metrics, not the alert states. See [Monitor your platform](/self_hosted/1.0.1/monitoring/monitoring_guide.md) for the full dashboard reference.

!!! warning "Investigate before taking action"
    A firing alert can cascade into ingestion, correlation, and alerting delays across the whole platform. Follow the [recommended incident response workflow](/self_hosted/1.0.1/monitoring/monitoring_guide.md#recommended-incident-response-workflow) to confirm cluster and database health before restarting or scaling affected resources.

Alerts are grouped by type, one type per infrastructure component or service. For each type, a global diagnostic analyzes the whole group: it identifies the affected component, explains the likely causes, and proposes remediations. Each alert is named after the diagnostic rule it mirrors and uses the same query and thresholds. When an alert fires, run the diagnostic of its type from the orchestration node. See [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md) for the output formats and how to read a result.

### Severity levels

| Severity | Meaning |
| :--- | :--- |
| Critical | A component is down or a pipeline has stopped. |
| Error | A feature fails or is degraded. |
| Warning | An early signal: a saturation or a degradation is building up. |

Some alerts have two thresholds: they fire as a warning first, then as an error when the condition worsens.

Alerts and diagnostics share the same queries and thresholds, but name their levels differently. A diagnostic check reports `OK`, `WARN`, or `CRIT`. As a rule, a `WARN` threshold raises a `warning` alert, and a `CRIT` threshold raises an `error` or a `critical` alert depending on its impact: `critical` when a component is down or a pipeline has stopped, `error` otherwise. A few alerts depart from this rule in either direction, so rely on the severity listed in the tables below. The timing also differs: an alert fires only once its condition has held for the duration given in the **Fires when** column, while a diagnostic evaluates the current value when you run it. A diagnostic can therefore report `WARN` or `CRIT` before the matching alert fires.

### Alert groups

| Alert group | What it monitors | Diagnostic target |
| :--- | :--- | :--- |
| [Alert pipeline](#alert-pipeline) | The creation of alerts from detection sightings. | `alerts` |
| [Asset discovery](#asset-discovery) | The discovery and reconciliation of assets from events. | `asset_discovery` |
| [Asset management](#asset-management) | The asset management API and workers, and asset enrichment in detection. | `asset_management` |
| [ClickHouse](#clickhouse) | The ClickHouse cluster that stores reporting data. | `clickhouse` |
| [Console](#console) | Access to the console: credentials store, ingress and TLS, front, and authentication. | `console` |
| [Indexation](#indexation) | The ExaLog indexation pipeline that makes events searchable. | `indexation` |
| [Ingestion](#ingestion) | Event reception, the TLS certificate of the ingestion endpoints, and ingestion volumes. | `ingest` |
| [Kafka](#kafka) | The Kafka message broker cluster and its Zookeeper dependency. | `kafka` |
| [Nodes](#nodes) | The Kubernetes nodes and their local storage. | `node` |
| [Detection](#detection) | The detection and correlation pipeline. | `sigma_workflow` |
| [Playbooks](#playbooks) | The execution of playbooks by Symphony. | `symphony` |
| [Telemetry](#telemetry) | The telemetry services behind reporting. | `telemetry` |

## Alert pipeline

This group monitors the creation of alerts from detection sightings. To learn more about an alert of this group and get remediation steps, run the alert pipeline diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=alerts
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| AlertsPipelineHealth | Critical | Sightings keep arriving but no alert is created or updated, for 5 minutes. | The detection-to-alert pipeline is stalled. |
| AlertsSightingsErrorRate | Error | More than 1.44% of the sightings fail to be processed into alerts, for 5 minutes. | Alerts may be lost. |
| AlertsCeleryWorkerDown | Critical | No `sicalertapi` Celery worker is up, for 1 minute. | Alert handling tasks cannot run. |
| AlertsHandleSightingFromRedisErrors | Error | The `handle_sighting_from_redis` task fails, for 5 minutes. | Alert creation and updates are delayed or dropped. |
| AlertsCeleryTaskErrors | Warning | One or more `sicalertapi` Celery tasks fail, for 5 minutes. | Background alert processing, such as notifications and aggregation, may be degraded. |
| AlertsOcEventsApiWorkerDown | Error | The OC Events API worker receives no task, for 5 minutes. | Anomaly detection processing may be stalled. |

## Asset discovery

This group monitors the discovery and reconciliation of assets from events. To learn more about an alert of this group and get remediation steps, run the asset discovery diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=asset_discovery
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| AssetDiscoveryDeploymentNoAvailableReplicas | Error | The `assetdiscoveryworker` deployment has no available replica, for 1 minute. | No new asset is discovered or reconciled. |
| AssetDiscoveryWorkerNotConsuming | Error | Facts are produced but the asset discovery worker does not consume them, for 5 minutes. | No new asset is discovered, merged, or reconciled. |
| AssetDiscoveryReconciliationDurationHigh | Warning, Error | A reconciliation cycle takes more than 5 seconds (warning) or 15 seconds (error), for 15 minutes. | The worker falls behind, and new assets take longer to appear. |
| AssetDiscoveryReconciliationConflicts | Warning, Error | Reconciliation conflicts exceed 0.1 per second (warning) or 0.5 per second (error), for 15 minutes. | Conflicting discovery facts can lead to inconsistent asset merges. |
| AssetDiscoveryFingerprintCollisions | Warning | Discovered assets are cancelled because of fingerprint collisions, for 15 minutes. | Legitimate assets can be dropped instead of merged. |
| TelemetryAssetDiscoveryRuleFailures | Warning | An asset discovery rule raises errors, for 5 minutes. | The rule stops emitting facts for the affected communities. |

## Asset management

This group monitors the asset management API and workers, and the enrichment of detection with known assets. To learn more about an alert of this group and get remediation steps, run the asset management diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=asset_management
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| AssetManagementDeploymentNoAvailableReplicas | Error | An asset management deployment has no available replica, for 1 minute. | Its function is down: REST API, compliance enrichment, notification handling, or risk scoring. |
| AssetManagementComplianceWorkerNotConsuming | Error | Compliance events arrive but the compliance worker does not consume them, for 5 minutes. | Software, accounts, partitions, and vulnerabilities are no longer derived from agent data. |
| AssetManagementComplianceProcessingErrorRateHigh | Warning, Error | More than 1% (warning) or 5% (error) of the compliance events fail, for 5 minutes. | Asset properties derived from agent compliance data are lost for those events. |
| AssetManagementEventNotificationWorkerNotConsuming | Error | Events arrive but the event notification worker does not consume them, for 5 minutes. | Assets are no longer kept in sync with alerts, cases, and other changes. |
| AssetManagementEventNotificationErrorRateHigh | Error | More than 5% of the events processed by the event notification worker fail, for 5 minutes. | Assets are not updated in response to these events. |
| AssetManagementRiskScoreComputationSkippedAssetNotFound | Warning, Error | Risk score computations skip missing assets more than 0.1 times per second (warning) or once per second (error), for 15 minutes. | Risk scores are silently skipped. |
| SigmacompilerAssetV2CompilationFailures | Error | The asset inventory used for detection fails to compile, for 5 minutes. | Detection enrichment with known assets runs on stale or empty data. |
| SigmaworkflowAssetV2MatcherSilentFailure | Warning | The asset matcher processes events but enriches none of them, for 15 minutes. | Detection is not enriched with known assets. |

## ClickHouse

This group monitors the ClickHouse cluster that stores reporting data. To learn more about an alert of this group and get remediation steps, run the ClickHouse diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=clickhouse
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| ClickhouseNoReadyReplicas | Critical | A ClickHouse shard has no ready replica, for 1 minute. | The data of the shard cannot be read or written: reports and asset queries reaching it fail. |
| ClickhouseReplicaUnavailable | Warning, Error | One replica (warning) or more than one replica (error) is not ready, for 5 minutes. | The shard keeps serving, but with reduced redundancy. |
| ClickhouseKeeperUnavailable | Critical | The keeper ensemble has no ready pod, for 1 minute. | Replicated tables switch to read-only and inserts fail. |
| ClickhouseReadonlyTables | Critical | A ClickHouse node has read-only tables, for 5 minutes. | Writes are rejected and reporting data silently stops being ingested. |
| ClickhouseDiskUsageHigh | Warning, Error | A data volume is more than 80% (warning) or 90% (error) full, for 5 minutes. | Merges and inserts start failing, and tables can switch to read-only. |
| ClickhouseDistributedFilesBacklog | Warning, Error | More than 100 (warning) or 1,000 (error) files wait for distributed insertion, for 15 minutes. | Reporting lags behind live traffic. |

## Console

This group monitors access to the console: the credentials store, the ingress and its TLS certificate, the front, and the authentication service. To learn more about an alert of this group and get remediation steps, run the console diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=console
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| ConsoleCredentialsStoreSealed | Critical | Vault has no ready replica, for 1 minute. | Logins fail, while ingestion and detection keep running. |
| ConsoleTlsSecretCertExpiry | Warning, Error | The configured TLS certificate expires within 21 days (warning) or 7 days (error), for 1 hour. | Once it expires, clients refuse the console, the APIs, and the HTTPS intake. |
| ConsoleTlsServedCertExpiry | Warning, Error | The certificate served by Traefik expires within 21 days (warning) or 7 days (error), for 1 hour. | Once it expires, clients refuse the console, the APIs, and the HTTPS intake. |
| ConsoleTlsSecretMissing | Critical | The TLS certificate secret is missing or invalid, for 5 minutes. | The platform cannot serve its certificate. |
| ConsoleTlsProbeFailed | Critical | A TLS handshake against Traefik fails, for 5 minutes. | Neither the console nor the HTTPS intake can be reached. |
| ConsoleIngressControllerDown | Critical | No Traefik pod is ready, for 1 minute. | The console, the APIs, and the HTTPS intake are unreachable from outside the cluster. |
| ConsoleIngressServerErrorRatio | Warning, Error | More than 5% (warning) or 20% (error) of the HTTPS requests end in a server error, for 5 minutes. | The console, the APIs, or the HTTPS intake fail for part of the requests. |
| ConsoleFrontDown | Critical | The `front` deployment has no available replica, for 1 minute. | The console cannot be loaded. |
| ConsoleAuthApiDown | Critical | The authentication service has no available replica, for 1 minute. | The console loads, but nobody can log in. |
| ConsoleAuthSecretMissing | Critical | The secret of the authentication service is missing, for 5 minutes. | The authentication service cannot start. |
| ConsoleAuthApiServerErrorRatio | Warning, Error | More than 5% (warning) or 20% (error) of the authentication requests end in a server error, for 5 minutes. | Logins fail for part of the users. |
| ConsoleGraphqlGatewayDown | Error | The GraphQL gateway has no available replica, for 1 minute. | Dashboard widgets and threat panels in alerts and cases fail to load. |
| ConsoleTlsExporterStale | Warning | The TLS certificate exporter has not completed a check for more than 15 minutes, for 5 minutes. | A certificate expiry can go unnoticed. |

## Indexation

This group monitors the ExaLog indexation pipeline that makes events searchable. To learn more about an alert of this group and get remediation steps, run the indexation diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=indexation
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| IndexationForwarderKafkaLagGrowing | Error | The indexation consumer lag exceeds 500 messages and 2 minutes of consumption, and has kept growing over the last 10 minutes, for 5 minutes. | Recent events become searchable later and later. |
| IndexationForwarderNotConsuming | Critical | Enriched events are produced but the indexation pipeline does not consume them, for 5 minutes. | No new event is indexed, and recent events are not searchable. |
| IndexationIndexerProducingNoDocuments | Critical | Events are forwarded but the indexers produce no document, for 5 minutes. | Recent events are not turned into searchable data. |
| IndexationObjectStorageErrorRatio | Warning, Error | More than 2% (warning) or 10% (error) of the object storage requests of the indexers fail, for 5 minutes. | Indexation slows down or stalls. |
| IndexationIndexerDiskUsageHigh | Warning, Error | The local volume of an indexer is more than 85% (warning) or 95% (error) full, for 5 minutes. | Once full, the indexer stops and indexation stalls. |
| IndexationNoReadyQuickwitNodes | Critical | No indexation node is ready, for 1 minute. | Nothing is indexed and no event search can be served. |

## Ingestion

This group monitors event reception, the TLS certificate of the ingestion endpoints, and the ingested volumes. To learn more about an alert of this group and get remediation steps, run the ingestion diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=ingest
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| IngestVolumeSpikeVsBaselinePreparser | Warning, Error | A syslog intake ingests more than 3 times (warning) or 10 times (error) its own baseline, for 15 minutes. | Processing, storage, and billing inflate, usually because of a misbehaving event source. |
| IngestVolumeSpikeVsBaselineHttp | Warning, Error | An HTTP intake ingests more than 3 times (warning) or 10 times (error) its own baseline, for 15 minutes. | Processing, storage, and billing inflate, usually because of a misbehaving event source. |
| IngestThrottlingActive | Warning | Ingestion is throttled for an intake, for 15 minutes. | The throttled events do not reach detection. |
| IngestKafkaPublicationFailing | Error | Accepted events fail to be published to Kafka, for 5 minutes. | The events are lost before detection. |
| IngestVolumeCollapseVsBaseline | Warning, Error | A community ingests less than 25% (warning) or 10% (error) of its own baseline, for 15 minutes. | The community has a detection blind spot. |
| IngestTlsConfiguredCertExpiring | Warning, Error | The configured TLS certificate expires within 21 days (warning) or 7 days (error), for 1 hour. | Once it expires, sources refuse the handshake and nothing is ingested over HTTPS or TLS syslog. |
| IngestTlsServedCertExpiring | Warning, Error | The certificate served by Traefik expires within 21 days (warning) or 7 days (error), for 1 hour. | Once it expires, sources refuse the handshake and nothing is ingested over HTTPS or TLS syslog. |
| IngestTlsSecretMissing | Critical | The Traefik TLS secret is missing or invalid, for 5 minutes. | Traefik serves its default certificate, and sources refuse to send events. |
| IngestTlsEndpointNotServing | Critical | A TLS handshake against Traefik fails, for 5 minutes. | Every ingestion endpoint is unreachable. |
| IngestTlsExporterStale | Warning, Error | The TLS certificate exporter has not completed a check for more than 15 minutes (warning) or 1 hour (error), for 5 minutes. | A certificate expiry can go unnoticed. |
| IngestHttpIntakeEndpointDown | Critical | The HTTP intake service has no available replica, for 1 minute. | Every source that pushes events over HTTPS is refused. |
| IngestRsyslogIntakeEndpointDown | Critical | The syslog intake service has no available replica, for 1 minute. | Every source that ships events over syslog or RELP is refused. |
| IngestPreparserStageDown | Critical | The pre-parser stage has no available replica, for 1 minute. | Ingestion stalls for all intakes. |
| IngestParserStageDown | Critical | No parser worker has an available replica, for 1 minute. | Events are received but never parsed, and never reach detection. |

The baseline of an intake or a community is its average rate over the 6 hours that end 30 minutes before the evaluation. The spike alerts ignore intakes whose baseline is 0.1 event per second or less, and the collapse alert ignores communities whose baseline is 1 event per second or less.

## Kafka

This group monitors the health of the Kafka message broker cluster and its Zookeeper dependency. To learn more about an alert of this group and get remediation steps, run the Kafka diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=kafka
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| KafkaNoReadyBrokers | Critical | No Kafka broker pod is ready for 1 minute. | The Kafka cluster is entirely down. Event ingestion, correlation, and alerting stop. |
| KafkaBrokerUnavailable | Error | Fewer broker pods are ready than the expected replica count, for 1 minute. | At least one broker is down. The cluster keeps serving traffic but with reduced capacity and fault tolerance. |
| KafkaBrokerDiskUsageHigh | Warning, Error | A broker's data volume usage exceeds 85% (warning) or 95% (error) for 5 minutes. | A broker is close to running out of disk space. Without action, it can stop accepting writes or lose data. |
| KafkaExporterUnavailable | Error | The `kafka-exporter` deployment has 0 available replicas for 1 minute. | Kafka metric collection stops. The cluster may still be healthy, but Grafana and diagnostic checks lose visibility into it. |
| KafkaAbnormalControllerState | Critical | The cluster does not report exactly one active controller for 1 minute. | Cluster coordination is unstable, which can delay partition leader elections and metadata changes. |
| KafkaOfflinePartitions | Critical | One or more partitions have no active leader for 1 minute. | Producers and consumers cannot read or write to the affected partitions. |
| KafkaUnderReplicatedPartitions | Warning | One or more partitions have fewer in-sync replicas than configured, for 1 minute. | Kafka keeps two copies of each partition, so the affected partitions have a single copy left. A further broker failure can cause data loss or unavailability. |
| KafkaZookeeperUnavailable | Critical | No Zookeeper pod is ready for 1 minute. | Kafka cluster coordination and broker registration are unavailable, which can prevent the cluster from recovering from other failures. |
| KafkaTopicBacklogGrowing | Error | The consumer backlog of a topic exceeds 500 messages and 2 minutes of consumption, and has kept growing over the last 10 minutes, for 5 minutes. | Everything downstream of the topic falls behind. |

The `kafka` diagnostic also reports replicas that keep leaving and re-entering the in-sync set. This check has no matching alert: run the diagnostic to see it.

The `kafka_replica_isr_flapping` rule of the Kafka diagnostic has no matching alert. It reports replicas that keep leaving and re-entering the in-sync set, a sign of inter-node network latency or broker saturation, and is evaluated only when you run the Kafka diagnostic.

## Nodes

This group monitors the Kubernetes nodes and their local storage. To learn more about an alert of this group and get remediation steps, run the node diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=node
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| NodeNotReady | Critical | A node is not ready, for 5 minutes. | Its pods are evicted, and the stateful services running on it lose a replica. |
| NodeUnreachable | Critical | Prometheus cannot reach the node exporter of a node, for 5 minutes. | The node is likely down or unreachable. |
| NodeUnschedulable | Warning | A node is excluded from scheduling, for 1 hour. | The cluster loses the capacity of the node for new pods. |
| NodeDiskPressure | Error | A node reports disk pressure, for 5 minutes. | The node evicts pods, and no new pod can be scheduled on it. |
| NodeMemoryPressure | Error | A node reports memory pressure, for 5 minutes. | The node evicts pods, and no new pod can be scheduled on it. |
| NodeMemoryUsageHigh | Warning, Error | Processes use more than 90% (warning) or 95% (error) of the memory of a node, for 5 minutes. | Pods on the node are about to be terminated. |
| NodeCpuLoadHigh | Warning, Error | The 15-minute load per CPU core exceeds 1 (warning) or 2 (error), for 15 minutes. | Every workload on the node slows down. |
| NodeClockDrift | Warning | The clock of a node drifts by more than 1 second, for 5 minutes. | TLS validation, cluster coordination, and event timestamps break. |
| NodeFilesystemUsageHigh | Warning, Error | A node filesystem is at least 80% (warning) or 90% (error) full, for 5 minutes. | Once full, pods are evicted and services writing to the node fail. |
| NodeFilesystemInodesUsageHigh | Warning, Error | A node filesystem uses at least 80% (warning) or 95% (error) of its inodes, for 5 minutes. | Once exhausted, no new file can be created on the filesystem. |
| NodeFilesystemPredictedFull | Warning | A node filesystem more than 60% full is predicted to fill up within 24 hours, for 1 hour. | The filesystem will be full without action. |
| NodePvcUsageHigh | Warning, Error | A persistent volume is at least 80% (warning) or 90% (error) full, for 5 minutes. | Once full, the owning service crashes or switches to read-only. |
| NodePvcInodesUsageHigh | Warning, Error | A persistent volume uses at least 80% (warning) or 95% (error) of its inodes, for 5 minutes. | Once exhausted, the owning service cannot create any new file. |
| NodePvcPredictedFull | Warning | A persistent volume more than 60% full is predicted to fill up within 24 hours, for 1 hour. | The volume will be full without action. |

The node filesystem alerts exclude the Ceph-backed volumes (`rbd` devices), which the persistent volume alerts cover. The persistent volume alerts exclude the Kafka and ClickHouse data volumes, which have their own alerts in the [Kafka](#kafka) and [ClickHouse](#clickhouse) groups. No alert covers the Ceph storage pool: the Ceph metrics are not collected in Self-Hosted, which is expected. To check the Ceph status, use the Storage tab of the [SHC interface](/self_hosted/1.0.1/operations/controller_interface.md).

## Detection

This group monitors the detection and correlation pipeline. To learn more about an alert of this group and get remediation steps, run the detection diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=sigma_workflow
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| SigmaWorkflowWorkerPartitionAssignmentImbalance | Warning, Error | The busiest detection worker has more than 2 (warning) or 4 (error) partitions more than the least busy one, for 15 minutes. | Some workers carry a disproportionate share of the event stream. |
| SigmaWorkflowKeydbKeyCountDisparity | Warning, Error | The key count differs by more than 200 (warning) or 500 (error) between the KeyDB replicas, for 15 minutes. | Detection can run on stale rules, assets, or correlation state. |
| SigmaWorkflowCorrelationKafkaLagGrowing | Error | The correlation consumer lag exceeds 500 messages and 2 minutes of consumption, and has kept growing over the last 10 minutes, for 5 minutes. | Correlation falls behind the live event stream. |
| SigmaWorkflowMatcherKafkaLagGrowing | Error | The detection consumer lag exceeds 500 messages and 2 minutes of consumption, and has kept growing over the last 10 minutes, for 5 minutes. | Detection falls behind the live event stream, and alerts are late. |
| SigmaWorkflowCorrelationHighFailureRatio | Warning, Error | More than 10% (warning) or 25% (error) of the correlation queries fail, for 5 minutes. | Correlation rules stop producing alerts. |
| SigmaWorkflowRuleCompilationHighFailureRatio | Warning, Error | More than 10% (warning) or 25% (error) of the detection rules fail to compile, for 15 minutes. | Detection silently runs on stale rules. |
| SigmaWorkflowDeploymentNoAvailableReplicas | Critical | A detection deployment has no available replica, for 1 minute. | Event matching, correlation, or rule compilation is down. |
| SigmaWorkflowMatcherNotConsuming | Critical | Events are produced but the detection workers do not consume them, for 5 minutes. | No event is evaluated against detection rules. |
| SigmaWorkflowAlertStormBlockingSightings | Warning | The alert storm protection drops sightings, for 5 minutes. | Some alerts are intentionally dropped, and real detections can be hidden. |
| SigmaWorkflowCorrelationHighLatency | Warning, Error | The 95th percentile duration of the correlation queries exceeds 5 seconds (warning) or 15 seconds (error), for 15 minutes. | Correlation rules are slow to match. |
| SigmaWorkflowSightingCreatorProducingNoSightings | Warning | Detection processes events but has created no sighting in the last 6 hours, for 1 hour. | Alerting from live detection has effectively stopped. |
| SigmaWorkflowSightingSenderStalled | Critical | Sightings are created but none is forwarded for alert creation, for 5 minutes. | Detections do not become alerts. |

## Playbooks

This group monitors the execution of playbooks by Symphony. To learn more about an alert of this group and get remediation steps, run the playbook diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=symphony
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| SymphonyPendingPodExcess | Warning, Error | More than 25 (warning) or 50 (error) playbook pods are pending, for 5 minutes. | Playbook executions are delayed or blocked. |
| SymphonySuccessfulPodExcess | Warning, Error | More than 100 (warning) or 500 (error) completed playbook pods accumulate, for 15 minutes. | The Kubernetes API slows down. |
| SymphonyErrorPodExcess | Warning, Error | More than 10 (warning) or 20 (error) playbook pods are in error, for 15 minutes. | Playbook actions consistently fail to run. |
| SymphonyFailedPodExcess | Warning, Error | More than 10 (warning) or 20 (error) playbook pods have failed, for 15 minutes. | Playbook executions do not complete. |
| SymphonyRunningPodCountHigh | Warning, Error | Running playbook pods use more than 80% (warning) or 95% (error) of their quota, for 5 minutes. | New playbook pods will be rejected once the quota is reached. |
| SymphonyConfigmapExcess | Warning, Error | More than 100 (warning) or 500 (error) ConfigMaps accumulate in the playbook namespace, for 15 minutes. | The Kubernetes API slows down, which can degrade the whole cluster. |
| SymphonySuccessfulJobExcess | Warning, Error | More than 100 (warning) or 500 (error) completed playbook jobs accumulate, for 15 minutes. | The Kubernetes API slows down. |
| SymphonyFailedJobExcess | Warning, Error | More than 10 (warning) or 50 (error) failed playbook jobs accumulate, for 15 minutes. | Failed playbook jobs are not cleaned up. |
| SymphonyPlaybookJobActivityHigh | Warning, Error | A single playbook retains more than 50 (warning) or 150 (error) jobs, for 15 minutes. | Jobs pile up, possibly because a playbook triggers itself in a loop. |
| SymphonyActionWorkerActionsNoAvailableReplicas | Critical | The `symphonyactionworker-actions` deployment has no available replica, for 1 minute. | Playbook actions are not processed. |
| SymphonyActionWorkerTriggersNoAvailableReplicas | Critical | The `symphonyactionworker-triggers` deployment has no available replica, for 1 minute. | Playbook triggers and connectors are not processed. |
| SymphonyCeleryQueueBacklogHigh | Warning, Error | More than 10 (warning) or 100 (error) tasks wait in the actions or triggers queue, for 5 minutes. | Playbook executions are delayed. |
| SymphonyCeleryRetryRateHigh | Warning, Error | Playbook action tasks retry more than 0.2 times per second (warning) or once per second (error), for 5 minutes. | Playbook actions repeatedly fail before they succeed. |
| SymphonyApiServerErrorRateHigh | Warning, Error | At least 5 (warning) or 20 (error) playbook tasks fail on Kubernetes API server errors in 10 minutes, for 5 minutes. | Playbook action pods cannot be created, and executions stall. |

## Telemetry

This group monitors the telemetry services behind reporting. To learn more about an alert of this group and get remediation steps, run the telemetry diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=telemetry
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| TelemetryDeploymentNoAvailableReplicas | Error | A telemetry deployment has no available replica, for 1 minute. | Its reporting function is down. |
| TelemetryEventsWorkerNotConsuming | Error | Events are produced but the telemetry events worker does not consume them, for 5 minutes. | Event counters and authentication telemetry stop being updated. |
| TelemetrySightingsWorkerNotConsuming | Error | Sightings are produced but the telemetry sightings worker does not consume them, for 5 minutes. | Rule and observable sighting statistics stop being updated. |
| TelemetryNotificationsWorkerNotConsuming | Error | Notifications arrive but the telemetry notifications worker does not consume them, for 5 minutes. | Playbook, alert filter, and usage telemetry is no longer reflected in reporting. |
| TelemetryClickhousePushFailures | Error | Telemetry workers fail to push data to ClickHouse, for 5 minutes. | Telemetry data is lost or delayed. |

<!--
Template for a new alert group. Copy it above "Related links", add the group to the "Alert groups" table, and keep one row per alert.

## <Group>

This group monitors <scope>. To learn more about an alert of this group and get remediation steps, run the <group> diagnostic:

```bash
exec Diagnostic --set modules.diagnostic.targets=<target>
```

| Alert | Severity | Fires when | Impact |
| :--- | :--- | :--- | :--- |
| <AlertName> | Critical, Error, or Warning | <condition and duration> | <operational impact> |
-->

## Related links

- [Monitor your platform](/self_hosted/1.0.1/monitoring/monitoring_guide.md): Daily monitoring and incident-response workflows, including the Grafana dashboard reference.
- [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md): Targeted Prometheus health checks to narrow an incident to the affected service.
- [Debug your deployment](/self_hosted/1.0.1/troubleshooting/debug_tool.md): Full SHC debug command reference with remediation steps.
