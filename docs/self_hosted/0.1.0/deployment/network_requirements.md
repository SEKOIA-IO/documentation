# Network requirements

This article lists the network flows required for a Sekoia Self-Hosted deployment. Configure stateful firewalls and network policies to allow the mandatory flows before installation. Return traffic for established connections must also be allowed.

Ports marked as configured use the port declared in your Self-Hosted configuration or endpoint URL. The tables show the default port where one exists.

## External flows to the application load balancer

Allow these flows from users, API clients, and event sources to the load balancer that serves `global.host` and `global.delivery_host`.

| Flow | Usage | Source | Destination | Protocol | Port |
| :--- | :--- | :--- | :--- | :---: | :---: |
| HTTPS | Platform UI, API, administrator portal, and HTTPS event ingestion | Users, API clients, and event sources | Application load balancer | TCP | 443 |
| HTTP | Redirect to HTTPS | Users and API clients | Application load balancer | TCP | 80 |
| Syslog over TLS | Event ingestion | Forwarders or external sources | Application load balancer | TCP | 10514 |
| RELP over TLS | Event ingestion | Forwarders or external sources | Application load balancer | TCP | 11514 |

## Flows from load balancers to Kubernetes nodes

Register only the Kubernetes nodes intended to receive traffic as load balancer backends.

| Flow | Usage | Source | Destination | Protocol | Port |
| :--- | :--- | :--- | :--- | :---: | :---: |
| HTTPS | Platform UI, API, administrator portal, and HTTPS event ingestion | Application load balancer | Kubernetes application backends | TCP | 443 |
| HTTP | Redirect to HTTPS | Application load balancer | Kubernetes application backends | TCP | 80 |
| Syslog over TLS | Event ingestion | Application load balancer | Kubernetes application backends | TCP | 10514 |
| RELP over TLS | Event ingestion | Application load balancer | Kubernetes application backends | TCP | 11514 |
| Kubernetes API | K3s API access and node registration in a highly available deployment | Kubernetes API load balancer | All manager nodes | TCP | 6443 |

!!! warning "PROXY Protocol is not enabled by default"
    The standard Self-Hosted Traefik configuration preserves client addresses with `externalTrafficPolicy: Local` and does not enable PROXY Protocol. Do not send PROXY Protocol headers to ports 80, 443, 10514, or 11514 unless you have also configured Traefik to accept them.

The Kubernetes API load balancer flow is required when `global.kube_manager_host` points to a load balancer for a highly available control plane. Restrict access to trusted cluster and administration networks.

## Flows from the orchestration node

The orchestration node does not join the Kubernetes cluster. It runs the self-hosted-controller (SHC) and requires these management flows.

| Flow | Usage | Source | Destination | Protocol | Port |
| :--- | :--- | :--- | :--- | :---: | :---: |
| SSH | Installation, upgrade, and diagnostic operations | Orchestration node | All manager and worker nodes | TCP | 22 |
| Kubernetes API | Cluster installation and management | Orchestration node | `global.kube_manager_host` | TCP | 6443 |

The orchestration node also needs access to Git, OCI, release storage, DNS, and NTP as described in [Outbound flows to infrastructure services](#outbound-flows-to-infrastructure-services).

## Kubernetes internal flows

Allow these flows on the private network between Kubernetes nodes. Do not expose Cilium, etcd, kubelet, or metrics ports to untrusted networks.

| Flow | Usage | Source | Destination | Protocol | Port |
| :--- | :--- | :--- | :--- | :---: | :---: |
| Kubernetes API | K3s agent registration and Kubernetes API access | All manager and worker nodes | `global.kube_manager_host` | TCP | 6443 |
| etcd client | Control-plane state access | Manager nodes | Manager nodes | TCP | 2379 |
| etcd peer | Control-plane state replication | Manager nodes | Manager nodes | TCP | 2380 |
| Kubelet API | Node management and metrics collection | Manager nodes and cluster monitoring workloads | All manager and worker nodes | TCP | 10250 |
| Cilium health and mesh | Cilium agent health and connectivity | All manager and worker nodes | All manager and worker nodes | TCP | 4240, 4250 |
| Cilium and Hubble metrics | Internal network observability | Cluster monitoring workloads | Cilium endpoints on all nodes | TCP | 9962-9965 |
| Cilium VXLAN | Encapsulated pod-to-pod traffic | All manager and worker nodes | All manager and worker nodes | UDP | 8472 |
| ICMP | Path MTU discovery and network diagnostics | All manager and worker nodes | All manager and worker nodes | ICMP | N/A |

The standard deployment disables Flannel and installs Cilium with VXLAN tunneling. Ensure host firewalls also permit forwarding for the pod network (`10.42.0.0/16` by default) and do not apply network address translation between cluster nodes.

## Outbound flows to infrastructure services

These services may be inside the customer network. Use the port from the configured endpoint when it differs from the default shown below.

| Flow | Usage | Source | Destination | Protocol | Default port |
| :--- | :--- | :--- | :--- | :---: | :---: |
| DNS resolution | Host and external service name resolution | Orchestration node and all Kubernetes nodes | `global.forward_dns` and host DNS servers | UDP / TCP | 53 |
| NTP | Required clock synchronization | Orchestration node and all Kubernetes nodes | Customer-provided NTP servers | UDP | 123 |
| SMTP | Mail notifications and user invitation emails | Platform workloads | Configured SMTP server | TCP | 25 |
| Git over HTTPS | SHC checks and manifest pushes; ArgoCD synchronization | Orchestration node and ArgoCD workloads | `utils.git.repo_url` | TCP | 443 |
| OCI registry over HTTPS | Image and chart pushes and pulls | Orchestration node, all Kubernetes nodes, and ArgoCD workloads | `utils.oci_registry.host` | TCP | 443 |
| Platform S3 storage over HTTPS | Event indexing, backups, and miscellaneous object storage | Platform workloads | `global.platform_storage.endpoint` | TCP | 443 |
| Release storage over HTTPS | Release archive download when files are not staged locally | Orchestration node | Configured release endpoint | TCP | 443 |
| Debian package repositories | Installation of required host packages | All Kubernetes nodes | Customer package mirror or Debian repositories | TCP | 80, 443 |

SMTP port 25 is the default. Allow the configured port instead when your server uses implicit TLS, STARTTLS, or a custom port, commonly TCP 465 or 587.

## Conditional flows

Allow the following flows only when you enable or use the corresponding feature.

| Condition | Usage | Source | Destination | Protocol | Port |
| :--- | :--- | :--- | :--- | :---: | :---: |
| Git uses SSH | SHC manifest push and ArgoCD synchronization | Orchestration node and ArgoCD workloads | Git server | TCP | 22 or configured port |
| Git or OCI uses plain HTTP | Access to an explicitly configured non-TLS endpoint | SHC, ArgoCD, or Kubernetes nodes as applicable | Git or OCI service | TCP | 80 or configured port |
| An HTTP or HTTPS proxy is configured | Proxied Git, image pull, or platform egress | Configured clients | Proxy server | TCP | Configured proxy port |
| Cilium WireGuard encryption is enabled | Encrypted node-to-node pod traffic | All manager and worker nodes | All manager and worker nodes | UDP | 51871 |
| Loki is consumed outside the cluster | Direct access to the Loki NodePort | Authorized monitoring clients | Kubernetes nodes | TCP | 30011 |
| Additional NodePort services are exposed | Direct access to explicitly selected NodePort services | Authorized clients | Kubernetes nodes | TCP / UDP | Selected ports in 30000-32767 |
| OpenID Connect is configured | Authentication discovery, authorization, and token exchange | Users and platform identity workloads | Identity provider | TCP | 443 or configured port |
| Connectors, actions, or webhooks call external services | Customer-enabled integrations and automation | Platform workloads | Customer-approved external services | TCP / UDP | Service-specific |

!!! warning "Do not expose the complete NodePort range by default"
    The standard deployment does not require public access to TCP or UDP 30000-32767. Open only the individual NodePort required by an authorized external consumer. Loki port 30011 can remain blocked at the perimeter when Loki is used only inside the cluster.

When a proxy is configured, allow clients to reach the proxy and configure the proxy to reach the Git, OCI, S3, SMTP, identity, or integration destinations that use it.

## Air-gapped environments

After the release archive is staged locally, a fully air-gapped deployment does not require internet access. It still requires the internal flows in this article and access to customer-managed DNS, NTP, SMTP, Git, OCI registry, S3-compatible storage, proxy, and Debian package mirror services as applicable.

The orchestration node pushes release artifacts to the local Git and OCI services. Kubernetes nodes and workloads then pull artifacts and access platform services entirely within the customer perimeter.

## Related links

- [Technical requirements](./deployment_prerequisites.md): Hardware, OS, and operational prerequisites.
- [Deploy the platform](./deployment_guide.md): Step-by-step installation instructions.
- [Configure the deployment](./deployment_configuration.md): Required platform storage, registry, DNS, and endpoint settings.
