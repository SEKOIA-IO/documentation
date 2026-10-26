# Sekoia Self-Hosted

!!! info "Who this section is for"
    This section covers Sekoia deployed and operated on your own infrastructure. If you use Sekoia SaaS, none of it applies to you: go to [Getting started](/getting_started/index.md).

Sekoia Self-Hosted is the Sekoia platform deployed and operated on your own infrastructure, for environments with strict regulatory, sovereignty, or connectivity constraints. It provides detection, investigation, and automation capabilities while data processing and infrastructure stay under your control. The capabilities available depend on the release: in Sekoia Self-Hosted 1.0.1, the AI features and the Intelligence module are not available. See the [release notes](/self_hosted/1.0.1/release_notes.md#functional-scope).

## Why Sekoia Self-Hosted exists

Highly regulated sectors operate under legal or technical constraints that make standard SaaS models impractical: classified or restricted networks with no external connectivity, national sovereignty requirements that limit reliance on foreign cloud providers, public procurement frameworks that impose strict hosting conditions, and mission-critical environments demanding full infrastructure control.

Sekoia Self-Hosted addresses these constraints with a self-managed platform that you deploy on the servers you provide: in a public or private cloud, on virtual machines, or on premises, including fully air-gapped networks. You run the installation, the monitoring, the backups, and the security content updates. Upgrading a deployment to a later release is not supported in Sekoia Self-Hosted 1.0.1.

!!! warning "Customer-operated platform"
    Sekoia Self-Hosted is a fully self-managed solution. Sekoia does not deploy or operate it. Your team, or a certified MSSP, is solely responsible for installation, updates, and ongoing platform management.

## Key capabilities

| Capability | Description |
| :--- | :--- |
| Data sovereignty | Data stays within your infrastructure to meet residency and regulatory requirements. |
| Air-gap compatibility | Deployment and operation in restricted or fully disconnected environments. |
| Automated orchestration | A single tool, the self-hosted-controller (SHC), checks the prerequisites, installs K3s and the platform, and runs the diagnostics, the backups, the security content updates, and the platform reset. |
| Built-in observability | Integrated Grafana, Prometheus, Loki, and Alertmanager stack for monitoring and alerting. |
| Built-in diagnostics | On-demand health checks for the cluster, applications, databases, and resources via the SHC CLI, each matched by a group of platform alerts. |
| High availability | The minimum cluster has 6 servers: 3 managers and 3 workers. The control plane stays available when one manager fails, Ceph keeps two copies of each volume on two different nodes, and Kubernetes reschedules the workloads of a failed node. See [High availability](/self_hosted/1.0.1/architecture/architecture.md#high-availability). |

## Intended audience

Sekoia Self-Hosted targets organizations that require maximum control over their security stack and have the operational capacity to run it. Typical deployments include:

- Highly regulated industries (finance, government, healthcare).
- Air-gapped or classified infrastructures (defense, critical national infrastructure).
- Organizations with strict national data sovereignty requirements.
- Large enterprises running dedicated security operations.
- Organizations working with MSSPs or sovereign service providers.

Sekoia Self-Hosted is designed for deployments that ingest at least **500 GB/day** of data or supervise at least **5,000 assets**.

!!! note "Incompatible use cases"
    Sekoia Self-Hosted is not designed for small organizations without a dedicated platform operations team, short-term or temporary projects, or purely cloud-native companies with no on-premises requirements.

## Documentation

The documentation is published per platform version. The navigation menu always shows the **current** version.

Start with the [documentation for version 1.0.1](/self_hosted/1.0.1/index.md). To see every published version, go to [Documentation versions](/self_hosted/versions.md).
