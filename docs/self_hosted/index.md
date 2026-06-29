# Sekoia Self-Hosted

Sekoia Self-Hosted is a customer-operated deployment of the Sekoia AI SOC platform for environments with strict regulatory, sovereignty, or connectivity constraints. It delivers cloud-grade detection and automation capabilities while keeping data processing and infrastructure entirely under your authority.

## Why Sekoia Self-Hosted exists

Highly regulated sectors operate under legal or technical constraints that make standard SaaS models impractical: classified or restricted networks with no external connectivity, national sovereignty requirements that limit reliance on foreign cloud providers, public procurement frameworks that impose strict hosting conditions, and mission-critical environments demanding full infrastructure control.

Sekoia Self-Hosted addresses these constraints with a self-managed, all-in-one platform you can deploy anywhere: public or private cloud, virtual machines, or fully air-gapped on-premises. You control installation, upgrades, monitoring, and supervision while running the same capabilities as Sekoia SaaS.

!!! warning "Customer-operated platform"
    Sekoia Self-Hosted is a fully self-managed solution. Sekoia does not deploy or operate it. Your team, or a certified MSSP, is solely responsible for installation, updates, and ongoing platform management.

## Key capabilities

| Capability | Description |
| :--- | :--- |
| Data sovereignty | Data stays within your infrastructure to meet residency and regulatory requirements. |
| Air-gap compatibility | Full deployment and operation in restricted or fully disconnected environments. |
| Automated orchestration | A single CLI (Self-Hosted Controller) handles provisioning, configuration, scaling, and lifecycle. |
| Built-in observability | Integrated Grafana, Prometheus and Loki stack for real-time monitoring. |
| Built-in diagnostics | On-demand health checks for the cluster, applications, databases, and resources via the SHC CLI. |
| High availability | A 6-node minimum cluster eliminates single points of failure. Kubernetes self-healing ensures continuous operations. |

## Intended audience

Sekoia Self-Hosted targets organizations that require maximum control over their security stack and have the operational capacity to run it. Typical deployments include:

- Highly regulated industries (finance, government, healthcare).
- Air-gapped or classified infrastructures (defense, critical national infrastructure).
- Organizations with strict national data sovereignty requirements.
- Large enterprises running dedicated security operations.
- Organizations working with MSSPs or sovereign service providers.

The platform requires a minimum of **5,000 supervised assets** and **500 GB/day** of ingested data.

!!! note "Incompatible use cases"
    Sekoia Self-Hosted is not designed for small organizations without a dedicated platform operations team, short-term or temporary projects, or purely cloud-native companies with no on-premises requirements.

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
| [Deployment configuration reference](deployment/deployment_configuration.md) | Complete `config.yml` parameter reference with required and optional field indicators. |

### Operations

| Document | What you will find |
| :--- | :--- |
| [Set up the first administrator account](operations/first_login.md) | How to provision the first administrator account and configure initial access. |

### Monitoring and troubleshooting

| Document | What you will find |
| :--- | :--- |
| [Monitor your platform](monitoring/monitoring_guide.md) | Observability stack overview, daily monitoring workflows, and SHC diagnostic command reference. |
| [Debug your deployment](troubleshooting/debug_tool.md) | Full SHC debug command reference with remediation guidance and log collection for support. |

### Release information

| Document | What you will find |
| :--- | :--- |
| [Release notes v0.0.1](release_notes/0.0.1.md) | MVP feature scope, functional limitations, known issues, and support lifecycle. |

## Quick start path

If you are new to Sekoia Self-Hosted, follow this sequence:

1. Read the [Reference architecture](architecture/architecture.md) to understand the platform topology.
2. Validate your infrastructure against the [Technical requirements](deployment/deployment_prerequisites.md) and [Network requirements](deployment/network_requirements.md).
3. Prepare your `config.yml` using the [Deployment configuration reference](deployment/deployment_configuration.md).
4. Follow the [Deploy the platform](deployment/deployment_guide.md) guide.
5. Create your first user with the [Set up the first administrator account](operations/first_login.md) guide.
6. Set up continuous monitoring using the [Monitor your platform](monitoring/monitoring_guide.md) guide.
