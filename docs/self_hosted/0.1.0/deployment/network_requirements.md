# Network requirements

This article lists all required network flows for a Sekoia Self-Hosted deployment, organized by source and destination. Configure your firewalls and network policies to allow every flow described below before starting the installation.

## Inbound flows to the load balancer

These flows must be open between external sources and your Load Balancer.

| Flow | Usage | Source | Protocol | Port |
| :--- | :--- | :--- | :---: | :---: |
| Syslog-RELP ingestion | Event ingestion | Forwarders or external sources | TCP | 11514 |
| Syslog ingestion | Event ingestion | Forwarders or external sources | TCP | 10514 |
| HTTPS | Platform UI access | Users | TCP | 443 |
| HTTP | Platform UI access (redirect to HTTPS) | Users | TCP | 80 |

!!! note "Proxy Protocol"
    Configure the Load Balancer backends for ports 80 and 443 with **PROXY Protocol v1** on connections to Kubernetes nodes so that client IP addresses are correctly propagated to the application layer.

## Flows from the load balancer to Kubernetes nodes

These flows must be open between your Load Balancer and all Kubernetes worker nodes.

| Flow | Usage | Protocol | Port |
| :--- | :--- | :---: | :---: |
| Syslog-RELP | Event ingestion forwarding | TCP | 11514 |
| Syslog | Event ingestion forwarding | TCP | 10514 |
| HTTP | Web UI forwarding | TCP | 80 |
| HTTPS | Web UI forwarding | TCP | 443 |

## Kubernetes internal flows

These flows must be open between the orchestration node and all Kubernetes nodes, and between Kubernetes nodes themselves.

| Flow | Usage | Source | Protocol | Port |
| :--- | :--- | :--- | :---: | :---: |
| Kubernetes API | Cluster management | Orchestration node, all K8s nodes | TCP | 6443 |
| etcd | Kubernetes control plane | Orchestration node, all K8s nodes | TCP | 2379 |
| etcd peer | Kubernetes control plane sync | Orchestration node, all K8s nodes | TCP | 2380 |
| Flannel VXLAN | Pod-to-pod networking | All K8s nodes | UDP | 8472 |
| SSH | Install, upgrade, and diagnostic operations | Orchestration node | TCP | 22 |

## Outbound flows from the cluster

These flows must be open from the orchestration node and all Kubernetes nodes to the external services listed below.

| Flow | Usage | Destination | Protocol | Port |
| :--- | :--- | :--- | :---: | :---: |
| DNS resolution | Name resolution | DNS server | UDP / TCP | 53 |
| SMTP | Mail notifications and user invitation emails | SMTP server | TCP | 25 / 465 / 587 |
| Code repository | ArgoCD GitOps synchronization | Git server | TCP | 443 |
| Artifact registry | Docker image pulls | OCI registry | TCP | 443 |
| S3 storage | Event indexing, backups, and miscellaneous storage | S3 endpoint | TCP | 443 |

## Air-gapped environments

In fully air-gapped deployments, no outbound internet connectivity is required after the initial archive download. All external flows listed above point to customer-managed services deployed within your perimeter: local Git server, local OCI registry, local S3, local DNS, local SMTP, and local NTP.

The orchestration node does not need internet access after you stage the release archive locally. All artifact push and registry operations use your local repositories.

## Related links

- [Technical requirements](./deployment_prerequisites.md): Hardware, OS, and operational prerequisites.
- [Deploy the platform](./deployment_guide.md): Step-by-step installation instructions.
- [Deployment configuration reference](./deployment_configuration.md): How to configure proxy and registry settings in `config.yml`.
