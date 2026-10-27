# Release notes v1.0.1

Sekoia Self-Hosted 1.0.1 is the first generally available release of Sekoia Self-Hosted. This article describes what the release contains, the available modules and their feature scope, the functional constraints, and the limitations.

!!! note "Import the threat intelligence after the installation"
    The installation does not deploy the Sekoia CTI database. Import it with the SHC once the platform is installed. See [Threat intelligence](#threat-intelligence).

## What's in 1.0.1

**Self-hosted-controller (SHC).** One orchestration tool, run as a Docker container on the orchestration node, installs, configures, diagnoses, and resets the platform. You use it as a one-shot CLI or through its terminal interface, which shows a progress bar while it downloads the release files, pushes the images, and installs the platform, and a Diagnostics tab that runs a target rule by rule with live status. See [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md).

**Air-gapped deployment.** You can deploy and operate the platform in restricted or fully disconnected environments, with no external connectivity. The SHC then uses the files extracted from the release archive and makes no request to the Sekoia release bucket. See [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md).

**Preflight checks.** The `checks` stage of the `Install` execution plan validates your environment before it changes anything. `CheckServerSpec` blocks the installation when a node shares its hostname with another node, has fewer than 44 logical CPUs or less than 120 GiB of RAM, does not run Debian 12 or later, has an active swap device, has no unused block device of 200 GB or more for Ceph, or has NTP disabled or an unsynchronized clock. `CheckNodePortReachability` then tests the cluster TCP ports between the nodes (Kubernetes API 6443, etcd, Cilium, and intake) before K3s is installed: each node briefly listens on these ports while the other nodes probe it. A blocked path is reported with the destination node, the port, and the reason: `timeout` when packets are silently dropped, `refused` when a firewall rule rejects the connection. The check works with any firewall backend and also catches blocks in security groups and network firewalls upstream of the nodes. It is skipped once K3s is installed on every node. See [CheckServerSpec](/self_hosted/1.0.1/troubleshooting/debug_tool.md#checkserverspec) and [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md).

**Detection rules and intake formats deployed at installation.** The `push` stage runs `PushDataBundles`, which publishes the detection rules and intake formats bundles to your local OCI registry, tagged with their release ID. After the platform installation, `SyncRulesCatalog` and `SyncIntakeFormats` synchronize the corresponding ArgoCD applications and wait for their PostSync jobs to succeed. The rules catalog is populated when the installation ends, with no manual ArgoCD synchronization. See [The deployment process](/self_hosted/1.0.1/deployment/deployment_process.md).

**Post-installation bootstrap.** `InstanceBootstrap` declares the default storage backend and reconciles the per-community ExaLog indexes, then `ScaleServices` scales the ingestion and detection workers to their configured replica count. See [Post-installation bootstrap](/self_hosted/1.0.1/deployment/deployment_process.md#post-installation-bootstrap).

**CTI database import.** `ImportArangoCollection` imports the Sekoia CTI database into the platform, from the Sekoia release bucket or, in air-gapped mode, from the daily CTI archive published by Sekoia. Once imported, it feeds contextualized alerts. The installation also creates the `SEKOIA Intelligence Feed` detection rule, which matches events against the indicators of the CTI database. The SHC reads the ArangoDB password from the cluster: you do not provide it. See [Import the CTI database](/self_hosted/1.0.1/operations/import_cti_database.md).

**Platform backups.** With `modules.platform_configuration.config.backups.enabled` set to `true`, the platform backs up Vault (daily encrypted snapshot, 30 kept), every PostgreSQL cluster including the ExaLog metastore (daily base backup and continuous WAL archiving, kept 30 days), ArangoDB (daily encrypted archive), and ClickHouse (encrypted daily incremental backups in monthly chains, 3 months kept). All backups go to one S3 bucket, by default `exalog-self-hosted-backups` on the platform storage, which you create beforehand. The encryption keys come from the `BACKUP_VAULT_CRYPT_KEY`, `BACKUP_ARANGO_CRYPT_KEY`, and `BACKUP_CLICKHOUSE_CRYPT_KEY` environment variables: keep a copy of them outside the platform. The `Backups` module checks the backup status from the S3 bucket, without access to the cluster, and `exec Backups -m run_now` triggers a backup of every enabled component. Backups are disabled by default. Restoring from a backup is not available in this release. See [Back up the platform](/self_hosted/1.0.1/operations/backups.md).

**Security content updates.** The `UpdatePlatformData` module updates the detection rules and intake formats of an installed platform in one run. It downloads the bundles, or in air-gapped mode uses the bundles copied to the orchestration node, publishes them to your OCI registry, updates the ArgoCD stacks, and synchronizes the rules catalog and the intake formats. When a bundle is unavailable or its tag cannot be verified in the registry, it stops before it changes the deployed versions. The playbook library cannot be updated after the installation. See [Update the security content](/self_hosted/1.0.1/operations/update_security_content.md).

**Certificate and credential rotation.** To replace the platform TLS certificate, you update the `TRAEFIK_PUBKEY` and `TRAEFIK_PRIVKEY` environment variables, then run `exec PlatformConfigurationFile` and `exec PlatformInstallation`. The `RestartAllMicroservices` module restarts the platform services and waits for their rollouts, so that they load refreshed Kubernetes Secrets. It leaves the databases running. See [Rotate the certificate and credentials](/self_hosted/1.0.1/operations/rotate_certificate_and_credentials.md).

**Manual Ceph storage selection.** By default, Ceph uses the unused raw disks it finds on the nodes. With `modules.platform_configuration.config.rook.storage.mode` set to `manual`, you list in `modules.platform_configuration.config.rook.storage.nodes` the raw disks or prepared LVM logical volumes that Ceph uses on each node, identified by its hostname. Before K3s is installed, `CheckServerSpec` checks the selected devices without changing them. Manual mode creates one Ceph OSD per device. `WipeStorageDisks` does not wipe manually selected devices: you clean them up yourself after a platform destruction. See [Ceph storage devices](/self_hosted/1.0.1/deployment/deployment_configuration.md#ceph-storage-devices).

**Diagnostics for every platform layer.** The `Diagnostic` module checks the platform with twelve targets. The `alerts`, `asset_discovery`, `asset_management`, and `telemetry` targets check these services, and the following targets cover the nodes, the data stores, access to the console, event ingestion, indexation, detection, and playbook execution. Each failing rule comes with its likely causes and remediation. The `DebugArgoCD`, `DebugDatabases`, and `DebugResourceAllocation` commands also check the ArgoCD applications, the databases, and the resource allocation on demand. See [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md).

| Target | What it checks |
| :--- | :--- |
| `node` | The Kubernetes nodes and their local storage: nodes not ready or unreachable, cordoned nodes, disk and memory pressure, high memory and CPU load, clock drift, and node filesystem and persistent volume usage, with a 24-hour fill prediction. |
| `kafka` | The Kafka cluster and its ZooKeeper ensemble: ready brokers, broker data volume usage, `kafka-exporter` availability, abnormal controller state, offline and under-replicated partitions, ZooKeeper availability, a topic whose consumer backlog keeps growing, and replicas that keep leaving and re-entering the in-sync set. |
| `clickhouse` | The ClickHouse cluster and its keeper ensemble: shards with no ready replica, replicas not ready, keeper availability, read-only tables, data volume usage, and the distributed insert backlog. |
| `ingest` | The ingestion path: intakes ingesting far above their own baseline, plan-based throttling to the dead-letter queue, accepted events not published to Kafka, a community whose ingestion collapses below its own baseline, the TLS certificate of the ingestion endpoints, and the reception and parsing stages with no available replica. |
| `console` | Access to the console: the credentials store (Vault), the ingress and its TLS certificate, the `front` deployment, the authentication service, and the GraphQL gateway. |
| `indexation` | The ExaLog indexation pipeline: an indexer that stopped consuming, object storage that returns errors, indexer local disk usage, and ready indexation nodes. |
| `sigma_workflow` | The detection and correlation pipeline: uneven partition assignment across matcher workers, KeyDB key count disparity between replicas, growing consumer lag, correlation and rule compilation failures, correlation latency, deployments with no available replica, matchers not consuming events, alert-storm protection dropping sightings, and stalled sighting creation or sending. |
| `symphony` | Playbook execution: playbook pod and job counts by state, excess ConfigMaps, per-playbook job activity, action worker availability, and Celery queue backlog, retry, and API server error rates. |

**Platform alerts for every diagnostic.** Each diagnostic target has a matching group of Prometheus alerts, loaded at installation. Each alert is named after the diagnostic rule it mirrors, with the same query and thresholds, and points to the diagnostic to run. Alerts have three severities: `critical` when a component is down or a pipeline has stopped, `error` when a feature fails or is degraded, and `warning` for early signals. Prometheus sends the firing alerts to the Alertmanager of the platform, which has no notification receiver: connecting the alerts to your notification channels is your responsibility. See [Platform alerts reference](/self_hosted/1.0.1/monitoring/platform_alerts.md).

**Built-in observability.** Grafana, Prometheus, Loki, Alertmanager, and Promtail are deployed as part of every installation. See [Monitor your platform](/self_hosted/1.0.1/monitoring/monitoring_guide.md).

**Volume-safe platform destruction.** `PlatformScaleDown` and `PlatformDestroy` reset a dedicated cluster. `PlatformScaleDown` deletes every platform namespace except the protected infrastructure namespaces, then checks on every node that the client volumes are released. `PlatformDestroy` runs the full sequence: Cilium cleanup preparation, `PlatformScaleDown`, `K3SUninstall`, and `WipeStorageDisks`. `K3SUninstall` removes the Cilium networking on dedicated nodes and verifies the cleanup, and `CleanupCilium` recovers a node where K3s is already uninstalled. When a phase fails, the error lists the completed phases, the phases not attempted, and the next safe step. See [Reset or destroy the platform](/self_hosted/1.0.1/operations/reset_platform.md).

!!! warning "Irreversible operations"
    `PlatformScaleDown` and `PlatformDestroy` permanently delete platform data. Both are disabled by default: `PlatformScaleDown` requires `modules.platform_scale_down.enabled` set to `true`, and `PlatformDestroy` also requires `modules.wipe_storage.enabled` set to `true`, except in manual Ceph storage mode.

**Bounded download timeouts.** In online mode, every request to the Sekoia release bucket uses a 10-second connect timeout, a 60-second read timeout, and three attempts, so a misconfigured `global.version.fetch` endpoint fails quickly with an error. See [Release download and security content](/self_hosted/1.0.1/deployment/deployment_configuration.md#release-download-and-security-content).

**Third-party license notices.** Each release ships `licenses/THIRD-PARTY-NOTICES.md` in its platform directory. It lists each third-party application with its license and source, includes the license texts, and explains how to obtain the source code of copyleft components.

## Technical foundation

The versions below are those of the release bundle.

| Attribute | Value |
| :--- | :--- |
| Kubernetes distribution | K3s v1.31.12+k3s1 |
| Supported node OS | Debian 12 (Bookworm) or Debian 13 (Trixie) |
| Container networking | Cilium 1.15.10 |
| Cluster DNS | CoreDNS 1.11.1 |
| HTTP entry point | Traefik v2.11.2 |
| Certificates | cert-manager v1.15.3 |
| Persistent storage | Rook v1.9.13 and Ceph v16.2.15 |
| GitOps engine | ArgoCD v3.1.0 |
| Secret management | HashiCorp Vault |
| Relational database | PostgreSQL 17 via CloudNativePG 1.25 |
| Columnar storage | ClickHouse 24.8.8 |
| Event streaming | Two Kafka clusters: the platform event bus, with ZooKeeper 3.7, and the ExaLog indexing cluster, Kafka 4 managed by the Strimzi operator 0.51.0 |
| Other data stores | ArangoDB 3.8.9, KeyDB 6.3.4, Redis 8.4.0, MinIO |
| Observability stack | Grafana 13.2.4, Prometheus v2.46.0, Alertmanager v0.33.1, Loki 2.8.7, Promtail 2.1.0 |

## Available modules

| Module | Availability |
| :--- | :--- |
| Defend | Available. Its scope is compared with the Defend Prime plan of the SaaS platform in [Defend functional scope](#defend-functional-scope). |
| Reveal | Available under a dedicated subscription, in addition to Defend. See [Reveal functional scope](#reveal-functional-scope). |
| Elevate | Not available yet. Its AI agents rely on generative AI inference, which this release does not provide. See [AI features](#ai-features). |
| Intelligence | Not available yet. The CTI database that you import feeds Defend, but you cannot explore threat actors, campaigns, and observables in the Intelligence module. See [Threat intelligence](#threat-intelligence). |

## Defend functional scope

The table below compares Defend Self-Hosted 1.0.1 with the Defend Prime plan of the SaaS platform. Defend Self-Hosted includes the SIEM and detection capabilities of Defend Prime: event ingestion, detection rule evaluation, case management, playbooks, threat hunting, dashboards, and user management. The features marked **No** are available in Defend Prime but not in Defend Self-Hosted 1.0.1.

| Feature | Available | Notes |
| :--- | :---: | :--- |
| Meta-playbooks | Yes | |
| Notifications | Yes | |
| Observable Tags Enrichment | No | The [CTI database import](/self_hosted/1.0.1/operations/import_cti_database.md) contains the CTI objects and their relationships, but not the observables and their tags. |
| Encrypted ingestion (Syslog TLS, RELP TLS, HTTPS) | Yes | |
| Custom Intake Formats | Yes | |
| Sigma Correlation | Yes | |
| Playbooks | Yes | |
| Automatic Asset Discovery | Yes | |
| Retrohunt | Yes | |
| Anomaly Detection Engine | Yes | |
| Case Management | Yes | |
| Hot Storage | Yes | |
| Sekoia Endpoint Agent | No | The `xdr-agent-api` service and its databases are deployed with the platform, but the Sekoia Endpoint Agent is not supported in this release. Do not enroll agents. |
| Contextualized Alerts | Yes | Requires the [CTI database import](/self_hosted/1.0.1/operations/import_cti_database.md). |
| SOL Query Builder | Yes | |
| Detection Rules | Yes | Full rules catalog deployed at installation. |
| IoC Collections | Yes | |
| Runbooks | No | Not available in this release. |
| Runbooks Edition | No | Not available in this release. |
| Event Drop Detection | Yes | |
| Cases Custom Status | Yes | |
| Investigation Graph | Yes | |
| Notebooks | Yes | |
| Sigma Pattern Validation | Yes | |
| SOL Dataset | Yes | |
| Dashboard Filters | Yes | |
| Roy Assistant | No | AI assistant. Not compatible with air-gapped environments. Requires GPU and cloud connectivity. |
| AI Cases | No | Relies on generative AI inference, which this release does not provide. See [AI features](#ai-features). |
| Custom Apps | No | Not available in this release. |
| Dashboards | Yes | |
| APIs | Yes | Full programmatic access. |
| Member Management | Yes | RBAC and user administration. |
| Multi-Community Management | Yes | |
| SSO / MFA | Yes | OpenID Connect compatible. |
| Usage Reporting | Yes | |
| Subscription Management | Yes | |
| Region Threat Telemetry | Yes | Telemetry of your deployed instance only. It does not include the telemetry of the Sekoia SaaS regions. |

## Reveal functional scope

Reveal is available with Sekoia Self-Hosted 1.0.1 under a dedicated subscription, in addition to Defend. The table below lists the Reveal features supported in this release compared with the SaaS platform.

| Feature | Available | Notes |
| :--- | :---: | :--- |
| Asset Context Panel | Yes | |
| Asset Timeline | Yes | |
| Points of Interest | Yes | |
| Attack Path Visualization | Yes | |
| Endpoint Hygiene | No | Requires the Sekoia Endpoint Agent, which is not supported in this release. |
| Vulnerability Enrichment | No | Requires NVD enrichment, which is not supported in this release. |
| Asset creation, enrichment, and unification | Yes | The asset connector pipeline operates as expected. |
| Defense Coverage | Yes | |

## Functional constraints

### Threat intelligence

The installation does not deploy the Sekoia CTI database. Until you [import it](/self_hosted/1.0.1/operations/import_cti_database.md), contextualized alerts and the `SEKOIA Intelligence Feed` rule have no threat intelligence to work with.

The import contains the CTI objects and their relationships, but not the observables and their tags: observable tags enrichment is not available, even after the import.

The Intelligence module, used to explore threat actors, campaigns, and observables, is not available in Sekoia Self-Hosted 1.0.1, even after the import.

In online mode, the import downloads the CTI database from the Sekoia release bucket. In air-gapped mode, it reads the CTI archive that you download from the release bucket and extract on the orchestration node. The other detection rules and the integration connectors do not depend on the CTI database.

### AI features

The AI capabilities of the Sekoia platform are not available in Sekoia Self-Hosted 1.0.1. They rely on generative AI inference that this release does not provide.

The following capabilities are therefore unavailable:

- The AI Assistant (ROY), which helps analysts write detection rules, triage alerts, and drive response.
- AI Cases, which groups related alerts into incidents.
- The Elevate module, whose AI agents investigate alerts and write investigation reports.

### Sekoia Forwarder

The Sekoia Forwarder supports disconnected deployments but is an optional add-on not included in the standard release. Its packaging, delivery, installation, and upgrade process are managed per customer. Contact Sekoia if your deployment requires a Forwarder.

## Limitations

The following operations and capabilities are not part of Sekoia Self-Hosted 1.0.1.

| Limitation | Impact | Workaround |
| :--- | :--- | :--- |
| Upgrade and rollback not supported | You cannot upgrade a 1.0.1 deployment to a later release, or roll it back to an earlier release, with the SHC. | None in 1.0.1. The release notes of each later version describe its upgrade path. |
| Restore from backup not available | The platform backs up Vault, PostgreSQL, ArangoDB, and ClickHouse, but the SHC provides no restore procedure. `Backups` checks the backup files in the S3 bucket and does not test a restore. | Contact Sekoia support if you need to restore data from a backup. |
| Playbook library not updatable | `UpdatePlatformData` updates the detection rules and intake formats, but the playbook library stays at the version deployed during the installation. | Contact Sekoia if your deployment requires an updated playbook library before the next release. |
| Node removal not supported | You cannot remove a node from a running cluster with the SHC. | None. |
| No graphical or web UI for platform administration | Infrastructure management is available only from the orchestration node. | Use the self-hosted-controller (SHC) terminal interface or one-shot CLI together with `config.yml` for administrative operations. |
| Node operating system not managed by the SHC | The SHC does not install or harden the operating system of the nodes. During the K3s installation, it only installs `lvm2` and `gettext-base`, adds a systemd unit that activates the Ceph LVM volume groups at boot, and raises the inotify and `vm.max_map_count` kernel limits. | Provision the operating system and packages listed in [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md) before you start the installation, and review [Changes applied by the SHC to the nodes](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#changes-applied-by-the-shc-to-the-nodes). |

## Related links

- [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md): Hardware and network prerequisites.
- [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md): Network flows between the nodes and the external services.
- [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md): Step-by-step installation instructions.
- [The deployment process](/self_hosted/1.0.1/deployment/deployment_process.md): The installation execution plan and the post-installation bootstrap.
- [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md): Health checks per platform area.
- [Platform alerts reference](/self_hosted/1.0.1/monitoring/platform_alerts.md): Alert groups, severities, and the diagnostic to run for each one.
- [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md): The interactive interface of the SHC.
- [Reset or destroy the platform](/self_hosted/1.0.1/operations/reset_platform.md): Volume-safe platform destruction.
