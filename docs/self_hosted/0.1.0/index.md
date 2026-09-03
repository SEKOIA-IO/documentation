# Sekoia Self-Hosted 0.1.0

This is the documentation for Sekoia Self-Hosted **0.1.0**. It describes the configuration keys, CLI commands, and behavior of this release only.

!!! warning "Pre-release version"
    Sekoia Self-Hosted 0.1.0 is currently in pre-release and may contain bugs. Report every bug to Sekoia in a separate report so that each issue can be tracked independently.

For what Sekoia Self-Hosted is and who it is for, see the [section introduction](../index.md). To check whether a more recent release is available, see [Documentation versions](../versions.md).

## Quick start path

If you are new to Sekoia Self-Hosted, follow this sequence:

1. Read the [Reference architecture](architecture/architecture.md) to understand the platform topology.
2. Validate your infrastructure against the [Technical requirements](deployment/deployment_prerequisites.md) and [Network requirements](deployment/network_requirements.md).
3. Prepare your `config.yml` using the [Deployment configuration reference](deployment/deployment_configuration.md).
4. Follow the [Deploy the platform](deployment/deployment_guide.md) guide.
5. Create your first user with the [Set up the first administrator account](operations/first_login.md) guide.
6. Get familiar with the [self-hosted-controller (SHC) interface](operations/controller_interface.md) for day-to-day interactive operations.
7. Set up continuous monitoring using the [Monitor your platform](monitoring/monitoring_guide.md) guide.
8. Run [platform diagnostics](monitoring/run_diagnostics.md) to validate service health.

## Documentation map

### Architecture

| Document | What you will find |
| :--- | :--- |
| [Reference architecture](architecture/architecture.md) | Platform components, infrastructure topology, node roles, high availability design, and data workflow. |

### Deployment

| Document | What you will find |
| :--- | :--- |
| [Technical requirements](deployment/deployment_prerequisites.md) | Hardware, OS, storage, network, and operational requirements before you begin. |
| [Network requirements](deployment/network_requirements.md) | Full table of required network flows, ports, and protocols. |
| [The deployment process](deployment/deployment_process.md) | High-level overview of the deployment engine, execution modes, and lifecycle operations. |
| [Deploy the platform](deployment/deployment_guide.md) | Step-by-step installation: download, verification, initialization, and post-deployment validation. |
| [Configure the deployment](deployment/deployment_configuration.md) | Copyable `config.yml` starter configuration and explanations for every required field. |

### Operations

| Document | What you will find |
| :--- | :--- |
| [Set up the first administrator account](operations/first_login.md) | How to provision the first administrator account and configure initial access. |
| [Use the self-hosted-controller (SHC) interface](operations/controller_interface.md) | The interactive self-hosted-controller (SHC) interface: command input, node, cluster and storage views, and diagnostics. |

### Monitoring and troubleshooting

| Document | What you will find |
| :--- | :--- |
| [Monitor your platform](monitoring/monitoring_guide.md) | Observability stack overview, daily monitoring workflows, and self-hosted-controller (SHC) diagnostic command reference. |
| [Run platform diagnostics](monitoring/run_diagnostics.md) | How to run targeted Prometheus health checks for platform services. |
| [Debug your deployment](troubleshooting/debug_tool.md) | Full self-hosted-controller (SHC) debug command reference with remediation guidance and log collection for support. |

### Release information

| Document | What you will find |
| :--- | :--- |
| [Release notes v0.1.0](release_notes.md) | MVP feature scope, functional limitations, known issues, and support lifecycle. |
