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

Traefik runs on every Kubernetes node, and K3s binds its ports 80, 443, 10514, and 11514 on the IP address of each node. Register as load balancer backends the nodes you want to receive traffic. Use a TCP (layer 4) load balancer: Traefik terminates TLS with the platform certificate.

| Flow | Usage | Source | Destination | Protocol | Port |
| :--- | :--- | :--- | :--- | :---: | :---: |
| HTTPS | Platform UI, API, administrator portal, and HTTPS event ingestion | Application load balancer | Kubernetes application backends | TCP | 443 |
| HTTP | Redirect to HTTPS | Application load balancer | Kubernetes application backends | TCP | 80 |
| Syslog over TLS | Event ingestion | Application load balancer | Kubernetes application backends | TCP | 10514 |
| RELP over TLS | Event ingestion | Application load balancer | Kubernetes application backends | TCP | 11514 |
| Kubernetes API | K3s API access and node registration in a highly available deployment | Kubernetes API load balancer | All manager nodes | TCP | 6443 |

!!! warning "Do not send PROXY Protocol headers"
    Traefik does not accept PROXY Protocol headers on ports 80 and 443. On ports 10514 and 11514, it accepts them only from the `10.0.255.0/24` range. Configure your load balancer without PROXY Protocol.

!!! note "Port 10901"
    Traefik also binds TCP 10901 on every node. No flow uses this port, so keep it blocked at the perimeter, but leave it free on every node: if another process uses it, the node stops serving ports 80, 443, 10514, and 11514.

The Kubernetes API load balancer flow is required when `global.kube_manager_host` points to a load balancer for a highly available control plane. Restrict access to trusted cluster and administration networks.

## Flows from the orchestration node

The orchestration node does not join the Kubernetes cluster. It runs the self-hosted-controller (SHC) and requires these management flows.

| Flow | Usage | Source | Destination | Protocol | Port |
| :--- | :--- | :--- | :--- | :---: | :---: |
| SSH | Installation, upgrade, and diagnostic operations | Orchestration node | All manager and worker nodes | TCP | 22 |
| Kubernetes API | Cluster installation and management | Orchestration node | `global.kube_manager_host` | TCP | 6443 |

The orchestration node also needs access to Git, OCI, release storage, DNS, and NTP as described in [Outbound flows to infrastructure services](#outbound-flows-to-infrastructure-services).

## Kubernetes internal flows

Allow these flows on the private network between Kubernetes nodes, in both directions. Do not expose these ports to untrusted networks.

| Flow | Usage | Source | Destination | Protocol | Port |
| :--- | :--- | :--- | :--- | :---: | :---: |
| Kubernetes API | K3s agent registration and Kubernetes API access | All manager and worker nodes | `global.kube_manager_host` and all manager and worker nodes | TCP | 6443 |
| etcd client and peer | Control-plane state access and replication | All manager and worker nodes | All manager and worker nodes | TCP | 2379, 2380 |
| Kubelet API | Node management and metrics collection | All manager and worker nodes | All manager and worker nodes | TCP | 10250 |
| Cilium health and authentication | Cilium agent health and connectivity | All manager and worker nodes | All manager and worker nodes | TCP | 4240, 4250 |
| Event ingestion | Syslog and RELP intake between nodes | All manager and worker nodes | All manager and worker nodes | TCP | 10514, 11514 |
| Node metrics | Prometheus collection of the node exporter | All manager and worker nodes | All manager and worker nodes | TCP | 9100 |
| Cilium metrics | Prometheus collection of the Cilium agent, operator, and Hubble metrics | All manager and worker nodes | All manager and worker nodes | TCP | 9962, 9963, 9965 |
| Cilium VXLAN | Encapsulated pod-to-pod traffic | All manager and worker nodes | All manager and worker nodes | UDP | 8472 |
| ICMP | Path MTU discovery and network diagnostics | All manager and worker nodes | All manager and worker nodes | ICMP | N/A |

!!! warning "Open the cluster ports between all nodes"
    Etcd runs only on the manager nodes, but the `CheckNodePortReachability` preflight check probes TCP 6443, 2379, 2380, 4240, 4250, 10514, and 11514 from every node to every other node, whatever its role. Allow these ports between all manager and worker nodes, or the check blocks the installation. See [CheckNodePortReachability](../troubleshooting/debug_tool.md#checknodeportreachability).

The standard deployment disables Flannel and kube-proxy and installs Cilium with VXLAN tunneling. Cilium also handles the Kubernetes services, so a NodePort service answers on the IP address of every node. Ensure host firewalls permit forwarding for the pod network and do not apply network address translation between cluster nodes.

The cluster uses the following fixed internal ranges. Make sure that they do not overlap a network that the nodes or the platform must reach:

| Range | Usage |
| :--- | :--- |
| `10.42.0.0/16` | Pod network. |
| `10.43.0.0/16` | Service network. CoreDNS uses `10.43.0.10` and Traefik uses `10.43.111.111`. |

## Outbound flows to infrastructure services

These services may be inside the customer network. Use the port from the configured endpoint when it differs from the default shown below. Platform workloads can run on any node and leave the node with its IP address, so allow their flows from all Kubernetes nodes.

| Flow | Usage | Source | Destination | Protocol | Default port |
| :--- | :--- | :--- | :--- | :---: | :---: |
| DNS resolution | Host and external service name resolution | Orchestration node and all Kubernetes nodes | `global.forward_dns` and host DNS servers | UDP / TCP | 53 |
| NTP | Required clock synchronization | Orchestration node and all Kubernetes nodes | Customer-provided NTP servers | UDP | 123 |
| SMTP | Mail notifications and user invitation emails | All Kubernetes nodes | Configured SMTP server | TCP | 25 |
| Git over HTTPS | SHC checks and manifest pushes; ArgoCD synchronization | Orchestration node and all Kubernetes nodes | `utils.git.repo_url` | TCP | 443 |
| OCI registry over HTTPS | Image and chart pushes and pulls | Orchestration node and all Kubernetes nodes | `utils.oci_registry.host` | TCP | 443 |
| Platform S3 storage over HTTPS | Event storage of the ExaLog indexes | All Kubernetes nodes | `global.platform_storage.endpoint` | TCP | 443 |
| Release storage over HTTPS | Release archive download when files are not staged locally | Orchestration node | `self-hosted.delivery.sekoia.io` | TCP | 443 |
| Debian package repositories | Installation of `lvm2` on every node and `gettext-base` on the first manager node, when they are missing | All Kubernetes nodes | Customer package mirror or Debian repositories | TCP | 80, 443 |

SMTP port 25 is the default. Allow the configured port instead when your server uses implicit TLS, STARTTLS, or a custom port, commonly TCP 465 or 587.

## Conditional flows

Allow the following flows only when you enable or use the corresponding feature.

| Condition | Usage | Source | Destination | Protocol | Port |
| :--- | :--- | :--- | :--- | :---: | :---: |
| Git uses plain HTTP | Access to a non-TLS Git endpoint set in `utils.git.repo_url` | Orchestration node and all Kubernetes nodes | Git server | TCP | 80 or configured port |
| An HTTP or HTTPS proxy is configured | Proxied Git, image pull, or platform egress | Orchestration node and all Kubernetes nodes, as configured | Proxy server | TCP | Configured proxy port |
| Loki is consumed outside the cluster | Direct access to the Loki NodePort | Authorized monitoring clients | Kubernetes nodes | TCP | 30011 |
| Additional NodePort services are exposed | Direct access to explicitly selected NodePort services | Authorized clients | Kubernetes nodes | TCP / UDP | Selected ports in 30000-32767 |
| A community uses OpenID Connect | Authentication discovery, authorization, and token exchange | Users and all Kubernetes nodes | Identity provider | TCP | 443 or configured port |
| Connectors, actions, or webhooks call external services | Customer-enabled integrations and automation | All Kubernetes nodes | Customer-approved external services | TCP / UDP | Service-specific |

!!! warning "Block the NodePort range from untrusted networks"
    The platform creates NodePort services that answer on the IP address of every node: Loki on TCP 30011, ClickHouse on TCP 30176 (HTTP) and 30177 (native protocol), and other ports assigned automatically in the 30000-32767 range. The standard deployment does not need any of them from outside the cluster. Block TCP and UDP 30000-32767 at the perimeter, and open only the individual NodePort required by an authorized external consumer, such as Loki port 30011. Loki does not require authentication: restrict port 30011 to your monitoring clients.

!!! note "Git and OCI protocols"
    ArgoCD connects to the Git repository with a username and a password over HTTP or HTTPS, and pulls the Helm charts from the OCI registry over HTTPS. Git over SSH and an OCI registry served over plain HTTP are not supported.

When a proxy is configured, allow clients to reach the proxy and configure the proxy to reach the destinations that use it. On the platform side, the proxy applies to ArgoCD, ExaLog indexing, the threat intelligence backend, and playbook actions. Email (SMTP) and OpenID Connect connections do not use the proxy. See [Proxy](./deployment_configuration.md#proxy).

## Air-gapped environments

After the release archive is staged locally, a fully air-gapped deployment does not require internet access. It still requires the internal flows in this article and access to customer-managed DNS, NTP, SMTP, Git, OCI registry, S3-compatible storage, proxy, and Debian package mirror services as applicable.

The orchestration node pushes release artifacts to the local Git and OCI services. Kubernetes nodes and workloads then pull artifacts and access platform services entirely within the customer perimeter.

## Related links

- [Technical requirements](./deployment_prerequisites.md): Hardware, OS, and operational prerequisites.
- [Deploy the platform](./deployment_guide.md): Step-by-step installation instructions.
- [Configure the deployment](./deployment_configuration.md): Required platform storage, registry, DNS, and endpoint settings.
