# Sekoia Self-Hosted 1.0.1

This is the documentation for Sekoia Self-Hosted **1.0.1**. It describes the configuration keys, CLI commands, and behavior of this release only.

For what Sekoia Self-Hosted is and who it is for, see the [section introduction](/self_hosted/index.md). To check whether a more recent release is available, see [Documentation versions](/self_hosted/versions.md).

## Quick start path

If you are new to Sekoia Self-Hosted, follow this sequence:

1. Read the [Reference architecture](/self_hosted/1.0.1/architecture/architecture.md) to understand the platform topology.
2. Validate your infrastructure against the [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md) and [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md).
3. Prepare your `config.yml` with [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md).
4. Follow the [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md) guide.
5. Create your first user with the [Set up the first administrator account](/self_hosted/1.0.1/operations/first_login.md) guide.
6. Import the threat intelligence with the [Import the CTI database](/self_hosted/1.0.1/operations/import_cti_database.md) guide.
7. Turn on the platform backups with the [Back up the platform](/self_hosted/1.0.1/operations/backups.md) guide.
8. Get familiar with the [self-hosted-controller (SHC) interface](/self_hosted/1.0.1/operations/controller_interface.md) for day-to-day interactive operations.
9. Set up continuous monitoring using the [Monitor your platform](/self_hosted/1.0.1/monitoring/monitoring_guide.md) guide.
10. Run [platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md) to validate service health.

## Documentation map

### Architecture

| Document | What you will find |
| :--- | :--- |
| [Reference architecture](/self_hosted/1.0.1/architecture/architecture.md) | Platform components, infrastructure topology, node roles, high availability design, and data workflow. |

### Deployment

| Document | What you will find |
| :--- | :--- |
| [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md) | Hardware, OS, storage, network, and operational requirements before you begin. |
| [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md) | Full table of required network flows, ports, and protocols. |
| [The deployment process](/self_hosted/1.0.1/deployment/deployment_process.md) | High-level overview of the deployment engine, execution modes, and lifecycle operations. |
| [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md) | Step-by-step installation: download, verification, initialization, and post-deployment validation. |
| [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md) | Copyable `config.yml` starter configuration and explanations for every required field. |

### Operations

| Document | What you will find |
| :--- | :--- |
| [Set up the first administrator account](/self_hosted/1.0.1/operations/first_login.md) | How to provision the first administrator account and configure initial access. |
| [Use the self-hosted-controller (SHC) interface](/self_hosted/1.0.1/operations/controller_interface.md) | The interactive self-hosted-controller (SHC) interface: command input, node, cluster and storage views, and diagnostics. |
| [Import the CTI database](/self_hosted/1.0.1/operations/import_cti_database.md) | How to import the Sekoia CTI database into the platform with the SHC. |
| [Back up the platform](/self_hosted/1.0.1/operations/backups.md) | How to turn on the backups of Vault, PostgreSQL, ArangoDB, and ClickHouse, trigger a backup, and check the backup status. |
| [Update the security content](/self_hosted/1.0.1/operations/update_security_content.md) | How to update the detection rules and intake formats after the installation. |
| [Apply a configuration change](/self_hosted/1.0.1/operations/apply_configuration_change.md) | How to change `config.yml` after the installation and apply it with an idempotent run of `Install`, and what the run restarts. |
| [Rotate the certificate and credentials](/self_hosted/1.0.1/operations/rotate_certificate_and_credentials.md) | How to replace the platform TLS certificate and credentials, then restart the platform services to load them. |
| [Patch and restart the nodes](/self_hosted/1.0.1/operations/node_maintenance.md) | How to patch the nodes one at a time without an outage, and how to run a cold restart of the whole cluster. |
| [Reset or destroy the platform](/self_hosted/1.0.1/operations/reset_platform.md) | How to delete the platform workloads and keep the cluster, or destroy the platform and wipe the storage disks before a reinstallation. |

### Monitoring and troubleshooting

| Document | What you will find |
| :--- | :--- |
| [Monitor your platform](/self_hosted/1.0.1/monitoring/monitoring_guide.md) | Observability stack overview, daily monitoring workflows, and self-hosted-controller (SHC) diagnostic command reference. |
| [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md) | How to run targeted Prometheus health checks for platform services. |
| [Platform alerts reference](/self_hosted/1.0.1/monitoring/platform_alerts.md) | Every platform alert by group, with its severity, its impact, and the diagnostic to run. |
| [Debug your deployment](/self_hosted/1.0.1/troubleshooting/debug_tool.md) | Full self-hosted-controller (SHC) debug command reference with remediation guidance and log collection for support. |

### Release information

| Document | What you will find |
| :--- | :--- |
| [Release notes v1.0.1](/self_hosted/1.0.1/release_notes.md) | Content of the release, feature scope, and functional constraints. |
