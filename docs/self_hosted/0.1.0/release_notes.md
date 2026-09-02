# Release notes v0.1.0

Sekoia Self-Hosted 0.1.0 builds on the 0.0.1 MVP with a hardened preflight, an automated post-installation bootstrap, and diagnostics for the alerts, asset, and telemetry pipelines. This article covers what changed in this release, the feature scope, functional constraints, and known issues.

!!! warning "Threat intelligence is not included in this release"
    The Sekoia CTI database is not embedded in Sekoia Self-Hosted 0.1.0, and the SHC does not retrieve it. Every feature that reads threat intelligence is unavailable. See [Threat intelligence](#threat-intelligence).

## What's new in 0.1.0

**Hardened preflight.** `CheckServerSpec` now blocks the installation when a manager or worker node shares its hostname with another node, has fewer than 44 CPU cores or less than 120 GiB of RAM, has no dedicated unused block device of 200 GB or more for Ceph and Longhorn, or has NTP disabled or an unsynchronized clock. Each failure names the offending node and the remediation. See [CheckServerSpec](troubleshooting/debug_tool.md#checkserverspec).

**Automated post-installation bootstrap.** The `Install` execution plan ends with two new modules. `InstanceBootstrap` declares the default storage backend and reconciles the per-community ExaLog indexes, which a freshly-installed region does not have. `ScaleServices` then scales the ingestion and detection workers to their configured replica count. Both are idempotent. See [Post-installation bootstrap](deployment/deployment_process.md#post-installation-bootstrap).

**Diagnostics for the alerts, asset, and telemetry pipelines.** The `Diagnostic` module gains four targets covering the alerts pipeline, asset discovery, asset management, and telemetry, with per-rule likely causes and remediation. See [Run platform diagnostics](monitoring/run_diagnostics.md).

**Interactive controller interface.** The SHC interface adds a Diagnostics tab that runs a target rule by rule with live status, sortable result tables, and clipboard copy, and shows a live progress bar while the platform installation runs. See [Use the controller interface](operations/controller_interface.md).

**Debian 12 on compute nodes.** The certified node operating system is Debian 12 (Bookworm), which `CheckServerSpec` enforces. See [Technical requirements](deployment/deployment_prerequisites.md).

## Carried over from 0.0.1

- **Air-gap deployment support.** You can deploy and operate the full platform in restricted or fully disconnected environments with no external connectivity.
- **Self-Hosted Controller (SHC).** A unified orchestration tool to install, configure, diagnose, and manage the platform lifecycle.
- **Built-in observability.** Grafana, Prometheus, Loki, Alertmanager, and Promtail are deployed as part of every installation.
- **Built-in diagnostics.** On-demand health checks for cluster nodes, ArgoCD applications, databases, secrets, and resource allocation.

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
| Sekoia Endpoint Agent | Yes | |
| Contextualized Alerts | No | Requires threat intelligence, which is not included in this release. |
| SOL Query Builder | Yes | |
| Detection Rules | Yes | Full rules catalog embedded in the release. |
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

## Functional constraints

### Threat intelligence

The Sekoia CTI database is not included in Sekoia Self-Hosted 0.1.0. No release artifact carries it, and no SHC module downloads or installs it. This is not a connectivity limitation: even a deployment with full internet access has no threat intelligence in this release.

The following capabilities are therefore unavailable:

- The Threat Intelligence research module, used to explore threat actors, campaigns, and observables.
- Observable tags enrichment.
- Contextualized alerts.

Detection capabilities remain fully operational. The Sekoia detection rules catalog and the integration connectors are embedded in the release archive, and they do not depend on the CTI database.

### Sekoia Forwarder

The Sekoia Forwarder supports disconnected deployments but is an optional add-on not included in the standard release. Its packaging, delivery, installation, and upgrade process are managed per customer. Contact Sekoia if your deployment requires a Forwarder.

## Known issues and limitations

The following issues do not occur systematically. They are intermittent and may not affect every deployment.

| Issue | Impact | Workaround |
| :--- | :--- | :--- |
| No upgrade path documented | You cannot upgrade an existing v0.0.1 deployment to v0.1.0 via the SHC. | Contact Sekoia before you plan an upgrade. |
| No UI for platform administration | Infrastructure management is CLI-only. | Use the SHC CLI and `config.yml` for all administrative operations. |
| Automatic upgrade and rollback not available | Version updates are manual. | Follow the manual update procedure when a new release is published. |
| Threat intelligence not included | Every feature that reads the CTI database is unavailable, including the Threat Intelligence research module, observable tags enrichment, and contextualized alerts. Detection rules are unaffected. | None. Contact Sekoia if your deployment requires threat intelligence. |
| Content updates are not functional | Detection rules, intake formats, and the playbook library cannot be updated after the installation, from the interface or from the SHC. The content of your deployment stays at the version embedded in the release archive. | None. Contact Sekoia if your deployment requires updated detection content before the next release. |
| Backup restore not yet documented | You cannot perform a tested restore from backup. | Contact Sekoia support for restore guidance specific to v0.1.0. |

## Related links

- [Technical requirements](deployment/deployment_prerequisites.md): Hardware and network prerequisites.
- [Deploy the platform](deployment/deployment_guide.md): Step-by-step installation instructions.
- [The deployment process](deployment/deployment_process.md): The installation execution plan and the post-installation bootstrap.
- [Use the controller interface](operations/controller_interface.md): The interactive interface of the SHC.
