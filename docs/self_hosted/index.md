# Sekoia Self-Hosted

!!! info "Who this section is for"
    This section covers Sekoia deployed and operated on your own infrastructure. If you use Sekoia SaaS, none of it applies to you: go to [Getting started](../getting_started/index.md).

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

## Documentation

The documentation is published per platform version. The navigation menu always shows the **current** version.

Start with the [documentation for version 0.1.0](0.1.0/index.md), or see [all documentation versions](versions.md) if you run an earlier release.
