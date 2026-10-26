# Reference architecture

Sekoia Self-Hosted is a containerized platform deployed on a K3s Kubernetes cluster that a dedicated CLI, the self-hosted-controller (SHC), installs on the servers you provide. This article describes the platform components, their roles, the infrastructure topology, and the data flow model.

## Platform components

The platform is delivered as a release archive with a SHA-256 checksum. The container images and the security content bundles of the release are signed with cosign, and the release ships the public key of the signature, `cosign.pub`. The SHC does not verify these signatures. The release packages the following component groups.

### Orchestration layer

| Component | Role |
| :--- | :--- |
| self-hosted-controller (SHC) | The orchestration CLI used to install, configure, and diagnose the platform, back it up, and update its security content. Runs as a Docker container on the orchestration node, driven by the `config.yml` manifest. |
| K3s | A lightweight Kubernetes distribution, version v1.31.12+k3s1, that the SHC installs offline, from files shipped in its container image, on every manager and worker node. Runs all platform containers. |
| ArgoCD | GitOps engine that reconciles the desired platform state, defined by the stacks the SHC publishes to your Git repository, against the live cluster state. |
| Helm | Package manager. The SHC deploys the cluster add-ons (Cilium, CoreDNS, cert-manager, and metrics-server) with Helm, and ArgoCD deploys the platform services from the Helm charts that the SHC pushes to your OCI registry. |
| Ansible | Used by the self-hosted-controller (SHC) to act on the compute nodes over SSH: preflight checks, K3s installation, cluster add-on deployment, kubeconfig retrieval, and node cleanup when you reset the platform. Apart from the kernel settings that K3s and Kafka need and the `lvm2` and `gettext-base` packages, the SHC does not configure the operating system. |
| CoreDNS | Provides service discovery and DNS resolution inside the Kubernetes cluster, and forwards the other queries to the DNS servers set in `global.forward_dns`. |
| Cilium | Provides container networking and network policy enforcement across the cluster, and replaces kube-proxy. |
| Traefik | Runs on every node and routes the external HTTPS, Syslog, and RELP traffic to the services running in the cluster. Terminates TLS with the platform certificate you provide. |

### Application layer

The Sekoia platform logic runs as a set of decoupled microservices deployed in the Kubernetes cluster. Each microservice handles a specific domain (event ingestion, detection, case management, user management). Each microservice runs in its own Kubernetes workloads, so it can be restarted and scaled independently.

### Data layer

| Component | Purpose |
| :--- | :--- |
| **S3-compatible storage** | Primary event data store (hot and long-term retention). Provisioned and managed by the customer and provided to the platform at deployment time. Also the default destination of the backups. |
| **Rook/Ceph** | Distributed storage for persistent Kubernetes volumes, exposed to workloads through the Ceph CSI integration. Base for all other services that require storage. Rook 1.9.13 deploys Ceph 16.2.15 with Ceph-CSI 3.6.2. By default, Ceph uses the unused raw disks of every node. You can select the disks or LVM logical volumes of each node instead. |
| PostgreSQL (CloudNativePG and PgBouncer) | Relational storage for platform configuration, cases, users, community data, and the ExaLog metastore. CloudNativePG manages the database clusters, while PgBouncer pools application connections. |
| ClickHouse | Columnar database for telemetry. |
| ArangoDB | Multi-model database used by platform services, including for the CTI database, and managed in Kubernetes by the ArangoDB operator. |
| Redis and KeyDB | In-memory data stores used for caching and inter-service communication. |
| Kafka | Distributed event-streaming platform used to transport data between processing services. |
| ZooKeeper | Coordination service used by distributed data services. |
| ExaLog | Distributed event indexing and search engine backed by the customer-provided S3-compatible storage. ExaLog is built on Quickwit: SHC configuration keys, commands, and logs use the name `quickwit`. |
| MinIO | In-cluster S3-compatible storage, on a Ceph volume, for the files that platform services store, such as notebook results and exported events. It is separate from the customer-provided event store. |

### Security layer

| Component | Purpose |
| :--- | :--- |
| HashiCorp Vault | Stores the platform secrets: the credentials and keys generated at installation time, and the values you provide in the configuration, such as the S3, SMTP, Git, and registry credentials. The services receive their secrets as Kubernetes Secrets generated from Vault. |
| Dex | Identity service bundled with ArgoCD. Platform users authenticate through the Sekoia authentication service, with optional OpenID Connect SSO. |
| cert-manager | Certificate controller deployed by the SHC with the cluster add-ons. It does not issue or renew the platform certificate: you provide that certificate and replace it before it expires. |

### Observability layer

| Component | Purpose |
| :--- | :--- |
| Prometheus | Collects system- and application-level metrics across all nodes and namespaces, and evaluates the platform alert rules. |
| Alertmanager | Receives the alerts fired by the platform alert rules. It has no notification receiver: connecting it to your notification channels is your responsibility. |
| TLS certificate exporter | Checks the TLS certificate configured and served for the platform, for the console and ingestion diagnostics and alerts. |
| Loki | Centralized log aggregation. Reachable without authentication on NodePort 30011 of every node: restrict that port to your monitoring clients. See [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md#nodeport-services). |
| Promtail | Agent running on every node, scraping container logs and forwarding them to Loki. |
| Grafana | Visualization layer. Provides the **Default** dashboard, organized in rows per platform layer. Also serves as the Explore interface for Loki log queries. |

### Content layer

| Component | Purpose |
| :--- | :--- |
| Detection rules catalog | Sekoia Sigma and pattern-based detection rules, shipped with every release, deployed at installation, and updatable afterwards. See [Update the security content](/self_hosted/1.0.1/operations/update_security_content.md). |
| Intake formats | Log parsing connectors for all supported source types, deployed at installation and updatable afterwards. |
| Automation library | SOAR playbooks and modules. Stays at the version deployed during the installation. |

## Infrastructure topology

The platform spans the following infrastructure components, all provisioned and managed by the customer.

### Node roles

| Role | Minimum count | Function |
| :--- | :---: | :--- |
| Orchestration node | 1 | Runs the self-hosted-controller (SHC) CLI, pushes images and charts to your OCI registry and the ArgoCD stacks to your Git repository, drives Ansible playbooks. Does not join the K3s cluster. |
| Manager node | 3 | Runs the Kubernetes control plane (API server, etcd, and scheduler) and, like the workers, platform workloads. Three managers keep the control plane available when one of them fails. Exactly three managers is the supported production topology. |
| Worker node | 3 (more with volume, see sizing) | Runs platform microservices, databases, and observability components, alongside the managers. |

For hardware requirements and sizing per node role, see [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md).

## High availability

The minimum cluster has 6 servers: 3 managers and 3 workers. This topology provides the following:

- Control plane: etcd and the Kubernetes API server run on the 3 managers, so the cluster keeps its control plane when one manager fails.
- Replicated storage: Ceph keeps two copies of each persistent volume on two different nodes, and Kafka replicates each partition on two brokers.
- Self-healing: Kubernetes restarts failed containers and reschedules the workloads of a failed node on the remaining nodes. A service that runs a single replica is unavailable until Kubernetes reschedules it.

## Data flow

### Event ingestion path

1. Sources send logs to the Sekoia Forwarder (optional add-on) or directly to the Load Balancer via Syslog over TLS (TCP 10514), RELP over TLS (TCP 11514), or HTTPS (TCP 443).
2. The Load Balancer forwards the traffic to the nodes you register as its backends. Traefik runs on every node and routes each connection to the intake services.
3. The intake service receives events and assigns each to the correct community via its intake key.
4. The detection pipeline normalizes, enriches, and correlates events against the detection rules catalog.
5. ExaLog indexes the processed events into the customer's S3-compatible storage, which serves as the primary event store for both active use and long-term retention.

## Terminology reference

The following terms are used consistently throughout this documentation.

| Term | Definition |
| :--- | :--- |
| self-hosted-controller (SHC) | The orchestration tool (`run-shc.sh`), exposing a one-shot CLI and an interactive interface. |
| Orchestration node | The machine where you execute the self-hosted-controller (SHC). |
| Compute node | A manager or worker node of the K3s cluster. Every compute node runs Sekoia microservices. |
| Forwarder | An optional Sekoia component installed on a customer VM, used to collect and forward logs to the platform. Not part of the standard release. |
| Asset | Any monitored entity (server, endpoint, network device) that generates log events ingested by the platform. |

## Related links

- [Technical requirements](/self_hosted/1.0.1/deployment/deployment_prerequisites.md): Hardware, OS, and network prerequisites for each node role.
- [Network requirements](/self_hosted/1.0.1/deployment/network_requirements.md): Full table of required network flows and ports.
- [The deployment process](/self_hosted/1.0.1/deployment/deployment_process.md): How the SHC orchestrates the installation.
- [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md): The interactive interface of the SHC.
