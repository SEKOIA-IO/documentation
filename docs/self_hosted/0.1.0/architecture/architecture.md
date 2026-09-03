# Reference architecture

Sekoia Self-Hosted is a containerized platform deployed on a customer-managed Kubernetes cluster and orchestrated by a dedicated CLI called the self-hosted-controller (SHC). This article describes the platform components, their roles, the infrastructure topology, and the data flow model.

## Platform components

The platform is delivered as a single digitally signed archive. It packages the following component groups.

### Orchestration layer

| Component | Role |
| :--- | :--- |
| self-hosted-controller (SHC) | The orchestration CLI used to install, configure, update, and diagnose the platform. Runs as a Docker container on the orchestration node, driven by the `config.yml` manifest. |
| K3s | A lightweight, certified Kubernetes distribution embedded in the platform. Manages the lifecycle of all platform containers. |
| ArgoCD | GitOps engine that continuously reconciles the desired platform state (defined in your local Git repository) against the live cluster state. |
| Helm | Package manager used for initial service deployment and upgrades. |
| Ansible | Used by the self-hosted-controller (SHC) to provision compute nodes: OS configuration, K3s installation, kubeconfig retrieval. |
| CoreDNS | Provides service discovery and DNS resolution inside the Kubernetes cluster. |
| Cilium | Provides container networking and network policy enforcement across the cluster. |
| Traefik | Routes external HTTP and HTTPS traffic to services running in the cluster. |

### Application layer

The Sekoia platform logic runs as a set of decoupled microservices deployed in the Kubernetes cluster. Each microservice handles a specific domain (event ingestion, detection, case management, user management). Microservices are isolated from each other to prevent cascading failures and allow independent scaling.

### Data layer

| Component | Purpose |
| :--- | :--- |
| **S3-compatible storage** | Primary event data store (hot and long-term retention). Provisioned and managed by the customer and provided to the platform at deployment time. |
| **Rook/Ceph** | Distributed storage for persistent Kubernetes volumes, exposed to workloads through the Ceph CSI integration. Base for all other services that require storage. |
| PostgreSQL (CloudNativePG and PgBouncer) | Relational storage for platform configuration, cases, users, and community data. CloudNativePG manages the database clusters, while PgBouncer pools application connections. |
| ClickHouse | Columnar database for telemetry. |
| ArangoDB | Multi-model database used by platform services and managed in Kubernetes by the ArangoDB operator. |
| Redis and KeyDB | In-memory data stores used for caching and inter-service communication. |
| Kafka | Distributed event-streaming platform used to transport data between processing services. |
| ZooKeeper | Coordination service used by distributed data services. |
| ExaLog | Distributed event indexing and search engine backed by the customer-provided S3-compatible storage. |
| MinIO | Internal S3-compatible storage for low-volume files that services need to persist between runs. It is separate from the customer-provided event store. |

### Security layer

| Component | Purpose |
| :--- | :--- |
| HashiCorp Vault | All platform secrets (database credentials, API keys, certificates) are generated at installation time and stored in Vault. Each microservice accesses only the secrets it needs. |
| Dex | Identity provider used to authenticate users and integrate platform access with supported identity systems. |
| cert-manager | Automates the issuance and renewal of TLS certificates used by services in the cluster. |

### Observability layer

| Component | Purpose |
| :--- | :--- |
| Prometheus | Collects system- and application-level metrics across all nodes and namespaces. |
| Loki | Centralized log aggregation. |
| Promtail | Agent running on every node, scraping container logs and forwarding them to Loki. |
| Grafana | Visualization layer. Provides prebuilt dashboards for cluster health, throughput, error rates, and security events. Also serves as the Explore interface for Loki log queries. |

### Content layer

| Component | Purpose |
| :--- | :--- |
| Detection rules catalog | Sekoia Sigma and pattern-based detection rules, embedded in every release. |
| Intake formats | Log parsing connectors for all supported source types. |
| Automation library | SOAR playbooks and modules. |

## Infrastructure topology

The platform spans the following infrastructure components, all provisioned and managed by the customer.

### Node roles

| Role | Minimum count | Function |
| :--- | :---: | :--- |
| Orchestration node | 1 | Runs the self-hosted-controller (SHC) CLI, pushes images and charts to registries, drives Ansible playbooks. Does not join the K3s cluster. |
| Manager node | 3 | Runs the Kubernetes control plane: API server, etcd, and scheduler. Three manager nodes provide control-plane fault tolerance. In tight deployments, they can also double as worker nodes. |
| Worker node | Varies (see sizing) | Runs all platform microservices, databases, and observability components. |
| GPU node | 0 to 2 | Optional. Required for AI features (NVIDIA H100). |

For hardware requirements and sizing per node role, see [Technical requirements](../deployment/deployment_prerequisites.md).

## High availability

The 6-node minimum cluster (3 manager + 3 workers) is a guarantee, not overhead. It ensures:

- No single point of failure: ingestion and detection continue even if a node fails.
- Resource isolation: microservices are decoupled to prevent cascading failures.
- Self-healing: Kubernetes automatically restarts failed containers and reschedules workloads on healthy nodes.

## Data flow

### Event ingestion path

1. Sources send logs to the Sekoia Forwarder (optional add-on) or directly to the Load Balancer via Syslog (TCP 10514), Syslog-RELP (TCP 11514), or HTTPS (TCP 443).
2. The Load Balancer distributes traffic across all K3s worker nodes.
3. The intake service receives events and assigns each to the correct community via its intake key.
4. The detection pipeline normalizes, enriches, and correlates events against the detection rules catalog.
5. Processed events are written to the customer's S3 bucket, which serves as the primary event store for both active use and long-term retention.

## Terminology reference

The following terms are used consistently throughout this documentation.

| Term | Definition |
| :--- | :--- |
| self-hosted-controller (SHC) | The orchestration tool (`run-shc.sh`), exposing a one-shot CLI and an interactive interface. Previously referred to as Deployer in some documents. |
| Orchestration node | The machine where you execute the self-hosted-controller (SHC). Also called admin node in some contexts. |
| Compute node | A Kubernetes worker node running Sekoia microservices. |
| Forwarder | An optional Sekoia component installed on a customer VM, used to collect and forward logs to the platform. Not part of the standard release. |
| Asset | Any monitored entity (server, endpoint, network device) that generates log events ingested by the platform. |

## Related links

- [Technical requirements](../deployment/deployment_prerequisites.md): Hardware, OS, and network prerequisites for each node role.
- [Network requirements](../deployment/network_requirements.md): Full table of required network flows and ports.
- [The deployment process](../deployment/deployment_process.md): How the SHC orchestrates the installation.
- [Use the SHC interface](../operations/controller_interface.md): The interactive interface of the SHC.
