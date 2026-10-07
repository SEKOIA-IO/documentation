# Release notes v1.0.0

Sekoia Self-Hosted 1.0.0 is the first generally available release of Sekoia Self-Hosted, with a node-to-node network preflight, detection rules and intake formats deployed at installation, diagnostics for every layer of the platform, and a volume-safe platform destruction. This article covers what changed since the 0.1.0 pre-release, the feature scope, functional constraints, and known issues.

!!! warning "Threat intelligence is not included in this release"
    The Sekoia CTI database is not part of Sekoia Self-Hosted 1.0.0. Every feature that reads threat intelligence is unavailable. See [Threat intelligence](#threat-intelligence).

## What's new in 1.0.0

**Node-to-node network preflight.** The `checks` stage of the `Install` execution plan now runs `CheckNodePortReachability` before K3s is installed. Each node briefly listens on the cluster TCP ports (Kubernetes API 6443, etcd, Cilium, and intake) while the other nodes probe it. A blocked path is reported as an explicit `host:port` pair, with `timeout` when packets are filtered and `refused` when the path is open but nothing listens. The check works with any firewall backend and also catches routing blocks upstream of the nodes. It is skipped once K3s is installed. See [Network requirements](deployment/network_requirements.md).

**Detection rules and intake formats deployed at installation.** The `push` stage now runs `PushDataBundles`, which publishes the detection rules and intake formats bundles to your local OCI registry, tagged with their release ID. After the platform installation, `SyncRulesCatalog` and `SyncIntakeFormats` synchronize the corresponding ArgoCD applications and wait for their PostSync jobs to succeed. The rules catalog is populated when the installation ends, with no manual ArgoCD synchronization. See [The deployment process](deployment/deployment_process.md).

**Diagnostics for every platform layer.** The `Diagnostic` module gains seven targets. Together with `alerts`, `asset_discovery`, `asset_management`, and `telemetry`, they cover the nodes, the data stores, event ingestion, indexation, detection, and playbook execution. Each failing rule comes with its likely causes and remediation. See [Run platform diagnostics](monitoring/run_diagnostics.md).

| Target | What it checks |
| :--- | :--- |
| `node` | The Kubernetes nodes and their local storage: nodes not ready or unreachable, cordoned nodes, disk and memory pressure, high memory and CPU load, clock drift, and node filesystem and orchestration volume usage, with a 24-hour fill prediction. |
| `kafka` | The Kafka cluster and its ZooKeeper ensemble: ready brokers, broker data volume usage, `kafka-exporter` availability, abnormal controller state, offline and under-replicated partitions, and ZooKeeper availability. |
| `clickhouse` | The ClickHouse cluster and its keeper ensemble: shards with no ready replica, replicas not ready, keeper availability, read-only tables, data volume usage, and the distributed insert backlog. |
| `ingest` | The syslog and HTTP ingestion chains: intakes ingesting far above their own baseline, plan-based throttling to the dead-letter queue, accepted events not published to Kafka, and a community whose ingestion collapses below its own baseline. Each result names the community and, where available, the intake key. |
| `indexation` | The ExaLog indexation pipeline: an indexer that stopped consuming, object storage that is slow or returns errors, indexer local disk usage, and ready indexation nodes. |
| `sigma_workflow` | The detection and correlation pipeline: uneven partition assignment across matcher workers, KeyDB key count disparity between replicas, growing consumer lag, correlation and rule compilation failures, correlation latency, deployments with no available replica, matchers not consuming events, alert-storm protection dropping sightings, and stalled sighting creation or sending. |
| `symphony` | Playbook execution: playbook pod and job counts by state, excess ConfigMaps, per-playbook job activity, action worker availability, and Celery queue backlog, retry, and API server error rates. |

**Volume-safe platform destruction.** Two new modules reset a dedicated cluster. `PlatformScaleDown` deletes every platform namespace except the protected infrastructure namespaces, then checks on every node that the client volumes are released. `PlatformDestroy` runs the full sequence: Cilium cleanup preparation, `PlatformScaleDown`, `K3SUninstall`, and `WipeStorageDisks`. `K3SUninstall` now removes Cilium networking on dedicated nodes and verifies the cleanup, and `CleanupCilium` recovers a node where K3s is already uninstalled. When a phase fails, the error lists the completed phases, the phases not attempted, and the next safe step.

!!! warning "Irreversible operations"
    `PlatformScaleDown` and `PlatformDestroy` permanently delete platform data. Both are disabled by default: `PlatformScaleDown` requires `modules.platform_scale_down.enabled` set to `true`, and `PlatformDestroy` also requires `modules.wipe_storage.enabled` set to `true`.

**Cleaner installation logs.** The platform installer no longer prints selected internal provisioning warnings. Other warnings and errors are unchanged.

**Faster failure on an unresponsive download endpoint.** In online mode, every S3 request now uses a 10-second connect timeout, a 60-second read timeout, and three attempts. A misconfigured `global.version.fetch` endpoint fails quickly with an error instead of hanging for minutes. See [Deployment configuration reference](deployment/deployment_configuration.md).

## Configuration changes

| Key | Change |
| :--- | :--- |
| `global.version.fetch.connect-timeout` | New. Seconds to wait for a connection to the S3 endpoint, per attempt. Default: `10`. Online mode only. |
| `global.version.fetch.read-timeout` | New. Seconds to wait for data from the S3 endpoint, per attempt. Default: `60`. Increase it behind a slow proxy. Online mode only. |
| `global.version.fetch.max-attempts` | New. Total attempts per S3 request, first try included. Default: `3`. Online mode only. |
| `modules.sync_rules_catalog.sync_timeout` | New. Maximum seconds to wait for the rules catalog synchronization and its PostSync job. Default: `900`. Increase it for large catalogs. |
| `modules.sync_intake_formats.sync_timeout` | New. Maximum seconds to wait for the intake formats synchronization and its PostSync job. Default: `900`. Increase it for large format bundles. |
| `modules.platform_scale_down.enabled` | New. Allows the irreversible deletion of platform namespaces. Required by `PlatformScaleDown` and `PlatformDestroy`. Default: `false`. |
| `modules.platform_scale_down.grace_period` | New. Seconds of graceful cleanup before blocking finalizers are removed. Must be lower than `timeout`. Default: `120`. |
| `modules.platform_scale_down.timeout` | New. Overall deadline in seconds for the cleanup and the volume release. Default: `600`. |
| `modules.platform_scale_down.poll_interval` | New. Seconds between two cleanup and volume release checks. Default: `5`. |
| `utils.port_forward.keep_alive_interval` | Removed. |

!!! warning "Remove deleted keys from your configuration"
    `CheckLocalConfig` rejects any key that is not documented. If your `config.yml` sets `utils.port_forward.keep_alive_interval`, remove it before you run the installation.

## Fixed in 1.0.0

- **Empty rules catalog after installation.** The installation now synchronizes the rules catalog itself. The manual synchronization of `rules-catalog-updater-on-self-hosted` required in 0.1.0 is no longer needed.
- **ExaLog indexers denied access to object storage.** The indexation buckets did not follow `modules.platform_configuration.config.storage-manager.s3_bucket_prefix`, so the indexers received `403 AccessDenied` errors when uploading. The buckets and their access grants are now generated from the configured prefix.
- **Diagnostic queries failing through the Prometheus tunnel.** The tunnel to `svc/prometheus-server` targeted the wrong pod port, so every `Diagnostic` query failed with "Server disconnected without sending a response". The tunnel now resolves the Service port to its target port, and each target closes its tunnel when it ends.
- **Interrupted Helm operations blocking a rerun.** A new `CleanupHelmReleases` prerequisite runs before `HelmInstall` and `PlatformInstallation`. It removes the pending, failed, and uninstalling Helm revisions left by an interrupted run, and preserves the deployed history and the chart-managed resources.
- **SHC interface started without an interactive terminal.** `shc` no longer starts its interface when no interactive terminal is attached, for example when you run the container without `-it`. It shows a warning and the CLI help instead.
- **Ceph disk wiping after K3s uninstall.** `WipeStorageDisks` failed with `wipefs: Device or resource busy` because of leftover OSD mappings. It now deactivates the unused Ceph LVM volume groups on the detected disks before wiping, and refuses mounted, open, or shared devices.
- **Existing images pushed again.** With `skip_existing_local` enabled, `PushImages` now recognizes OCI image indexes, cosign bundles with attestations, Docker manifests, and manifest lists already in the registry, and skips them.

## Carried over from the pre-releases

- **Air-gap deployment support.** You can deploy and operate the full platform in restricted or fully disconnected environments with no external connectivity.
- **SHC.** A unified orchestration tool to install, configure, diagnose, and manage the platform lifecycle.
- **Hardened preflight.** `CheckServerSpec` blocks the installation when a node shares its hostname with another node, has fewer than 44 CPU cores or less than 120 GiB of RAM, has no dedicated unused block device of 200 GB or more for Ceph and Longhorn, or has NTP disabled or an unsynchronized clock. See [CheckServerSpec](troubleshooting/debug_tool.md#checkserverspec).
- **Automated post-installation bootstrap.** `InstanceBootstrap` declares the default storage backend and reconciles the per-community ExaLog indexes, then `ScaleServices` scales the ingestion and detection workers to their configured replica count. See [Post-installation bootstrap](deployment/deployment_process.md#post-installation-bootstrap).
- **Interactive SHC interface.** A terminal interface with a Diagnostics tab that runs a target rule by rule with live status, and a live progress bar during the platform installation. See [Use the SHC interface](operations/controller_interface.md).
- **Built-in observability.** Grafana, Prometheus, Loki, Alertmanager, and Promtail are deployed as part of every installation.
- **Built-in diagnostics.** On-demand health checks for cluster nodes, ArgoCD applications, databases, secrets, and resource allocation.
- **Debian 12 on compute nodes.** The certified node operating system is Debian 12 (Bookworm), which `CheckServerSpec` enforces. See [Technical requirements](deployment/deployment_prerequisites.md).

## Technical foundation

| Attribute              | Value                         |
| :---                   | :---                          |
| Kubernetes distribution | K3s                          |
| Certified node OS      | Debian 12 (Bookworm)          |
| GitOps engine          | ArgoCD                        |
| Secret management      | HashiCorp Vault               |
| Relational database    | PostgreSQL via CloudNativePG  |
| Columnar storage       | ClickHouse                    |
| Observability stack    | Grafana, Prometheus, Loki, Alertmanager |

## Functional scope

The functional scope aligns with the **Defend Core** subscription tier. Defend Core includes the core SIEM and detection capabilities: event ingestion, detection rule evaluation, case management, playbooks, threat hunting, dashboards, and user management.

| Feature | Available | Notes |
| :--- | :---: | :--- |
| Meta-playbooks | Yes | |
| OC Notifications | Yes | |
| Observable Tags Enrichment | No | Requires threat intelligence, which is not included in this release. |
| Cloud-to-Cloud Ingestion | No | Not supported in air-gapped deployments. |
| Encrypted ingestion (Syslog TLS, RELP TLS, HTTPS) | Yes | |
| Custom Intake Formats | Yes | |
| Sigma Correlation | Yes | |
| Playbooks | Yes | |
| Automatic Asset Discovery | Yes | |
| Retrohunt | Yes | |
| Anomaly Detection Engine | Yes | |
| Case Management | Yes | |
| Hot Storage | Yes | |
| Sekoia Endpoint Agent | No | The `xdr-agent-api` service is not installed in this release. |
| Contextualized Alerts | No | Requires threat intelligence, which is not included in this release. |
| SOL Query Builder | Yes | |
| Detection Rules | Yes | Full rules catalog deployed at installation. |
| Event Drop Detection | Yes | |
| Cases Custom Status | Yes | |
| Investigation Graph | Yes | |
| Notebooks | Yes | |
| Sigma Pattern Validation | Yes | |
| SOL Dataset | Yes | |
| Dashboard Filters | Yes | |
| Roy Assistant | No | AI assistant. Not compatible with air-gapped environments. Requires GPU and cloud connectivity. |
| Dashboards | Yes | |
| APIs | Yes | Full programmatic access. |
| Member Management | Yes | RBAC and user administration. |
| SSO / MFA | Yes | OpenID Connect compatible. |
| Usage Reporting | Yes | |
| Subscription Management | Yes | |
| Region Threat Telemetry | Yes | |

## Reveal functional scope

Reveal is available with Sekoia Self-Hosted 1.0.0 under a dedicated subscription, in addition to Defend. The table below lists the Reveal features supported in this release compared with the SaaS platform.

| Feature | Available | Notes |
| :--- | :---: | :--- |
| Asset Context Panel | Yes | |
| Asset Timeline | Yes | |
| Points of Interest | Yes | |
| Attack Path Visualization | Yes | |
| Endpoint Hygiene | No | Requires the `xdr-agent-api` service, which is not installed in this release. |
| Vulnerability Enrichment | No | Requires NVD enrichment, which is not supported in this release. |
| Asset creation, enrichment, and unification | Yes | The asset connector pipeline operates as expected. |
| Defense Coverage | Yes | |

## Functional constraints

### Threat intelligence

The Sekoia CTI database is not part of Sekoia Self-Hosted 1.0.0. This is not a connectivity limitation: even a deployment with full internet access has no threat intelligence in this release.

The following capabilities are therefore unavailable:

- The Threat Intelligence research module, used to explore threat actors, campaigns, and observables.
- Observable tags enrichment.
- Contextualized alerts.

Detection capabilities remain fully operational. The Sekoia detection rules catalog and the integration connectors are deployed with the release, and they do not depend on the CTI database.

### AI features

The AI capabilities of the Sekoia platform are not available in Sekoia Self-Hosted 1.0.0. They rely on generative AI inference that this release does not provide.

The following capabilities are therefore unavailable:

- The AI Assistant (ROY), which helps analysts write detection rules, triage alerts, and drive response.
- AI Cases, which groups related alerts in real time into AI-powered incidents.
- The Elevate module, whose AI agents investigate alerts autonomously and produce audit-ready investigation reports.

### Sekoia Forwarder

The Sekoia Forwarder supports disconnected deployments but is an optional add-on not included in the standard release. Its packaging, delivery, installation, and upgrade process are managed per customer. Contact Sekoia if your deployment requires a Forwarder.

## Known issues and limitations

The following limitations apply to Sekoia Self-Hosted 1.0.0.

| Issue | Impact | Workaround |
| :--- | :--- | :--- |
| No upgrade path from the pre-releases | You cannot upgrade an existing 0.0.1 or 0.1.0 deployment to 1.0.0 with the self-hosted-controller (SHC). | Contact Sekoia to plan the migration of a pre-release deployment. |
| No graphical or web UI for platform administration | Infrastructure management is available only from the orchestration node. | Use the self-hosted-controller (SHC) terminal interface or one-shot CLI together with `config.yml` for administrative operations. |
| Automatic upgrade and rollback not available | Version updates are manual. | Follow the manual update procedure when a new release is published. |
| Server configuration not automated | The `ConfigureServersWithAnsible` module is a placeholder and does not configure the nodes. | Provision the operating system and packages listed in [Technical requirements](deployment/deployment_prerequisites.md) before you start the installation. |
| Threat intelligence not included | Every feature that reads the CTI database is unavailable, including the Threat Intelligence research module, observable tags enrichment, and contextualized alerts. Detection rules are unaffected. | None. Contact Sekoia if your deployment requires threat intelligence. |
| No content update procedure | Detection rules, intake formats, and the playbook library stay at the version deployed during the installation. No procedure covers their update after the installation. | Contact Sekoia if your deployment requires updated detection content before the next release. |
| Backup restore not yet documented | You cannot perform a tested restore from backup. | Contact Sekoia support for restore guidance specific to 1.0.0. |

## Related links

- [Technical requirements](deployment/deployment_prerequisites.md): Hardware and network prerequisites.
- [Network requirements](deployment/network_requirements.md): Network flows between the nodes and the external services.
- [Deploy the platform](deployment/deployment_guide.md): Step-by-step installation instructions.
- [The deployment process](deployment/deployment_process.md): The installation execution plan and the post-installation bootstrap.
- [Run platform diagnostics](monitoring/run_diagnostics.md): Health checks per platform area.
- [Use the SHC interface](operations/controller_interface.md): The interactive interface of the SHC.
