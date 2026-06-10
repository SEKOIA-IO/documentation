# Technical requirements

This article lists all infrastructure, hardware, software, storage, and network requirements for a Sekoia Self-Hosted deployment. Verify every requirement before starting the installation.

## Infrastructure components

You must provision and manage the following components outside the Kubernetes cluster.

| Component | CPU | RAM | Storage | Notes |
| :--- | :---: | :---: | :---: | :--- |
| Load Balancer (e.g., HAProxy, Nginx) | 4 | 8 GB | 50 MB/s | Required. Validate throughput against your actual ingest volume. |
| Orchestration node | 4 | 8 GB | 100 GB | Required. Runs the SHC CLI. See OS requirements below. |
| Local image registry (e.g., Harbor, JFrog, Nexus) | 4 | 8 GB | 5 TB | Required for air-gapped deployments. |
| Local code registry (e.g., GitLab, Gitea, ForgeJo) | 4 | 8 GB | 100 GB | Required for air-gapped deployments. |

### Orchestration node OS requirements

The orchestration node must run **Debian 12** with **Python 3.11** installed. Python is required by the Ansible component of the SHC.

!!! note "Orchestration node role"
    The orchestration node does not join the Kubernetes cluster. It drives Ansible playbooks and runs the SHC CLI. It must have SSH access to all compute nodes on TCP port 22.

## Compute node specification

Every Kubernetes worker node must meet the following minimum hardware requirements.

| Resource | Minimum requirement |
| :--- | :--- |
| CPU | 44 vCPUs at 3.2 GHz minimum |
| RAM | 128 GB |
| Storage | 4 TB SSD |
| Operating system | Debian 11 (Bullseye) |

!!! warning "SSD usage"
    The 4 TB SSD on each compute node is reserved for Kubernetes runtime and system use. Do not store long-term event data on compute node disks. Event data requires a dedicated S3-compatible bucket (see [Storage](#storage) below).

### GPU nodes (optional)

AI features require dedicated GPU nodes. GPU nodes are optional for the MVP release.

| Resource | Requirement |
| :--- | :--- |
| GPU model | NVIDIA H100 |
| Purpose | AI inference and anomaly detection workloads |

## Cluster sizing

The following table provides estimated hardware footprints per deployment size.

!!! note "Sizing guidance"
    These figures are indicative. Contact Sekoia before deployment to validate requirements against your specific workload and asset profile.

| Size | Incoming data | Assets (approx.) | Compute nodes | GPU nodes | S3 storage |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Small | 500 GB/day | ~5,000 | 6 | 1 | 200 TB |
| Medium | 1.4 TB/day | ~15,000 | 14 | 2 | 600 TB |
| Large | 5 TB/day | ~50,000 | 60 | 2 | 2,000 TB |

**What is an asset?** An asset is any monitored entity (server, endpoint, network device) that generates log events sent to the platform. The asset counts above are approximations. Actual capacity depends on the size and frequency of ingested log messages.

**S3 storage calculation:** Total S3 capacity = daily ingest (GB) x retention period (days). The table above assumes 365 days of retention.

**Node roles:** Each cluster requires at least 1 manager node (Kubernetes control plane). The remaining nodes are workers. For production high-availability, use 3 manager nodes to tolerate 1 failure. Worker count corresponds to the Compute nodes column above.

## Storage

An S3-compatible bucket is required for event data storage and platform backups. You must provision this bucket before deployment.

| Use | Notes |
| :--- | :--- |
| Event storage | Long-term data lake for all ingested events. Customer-managed. See sizing table above. |


## Network requirements

DNS management, NTP synchronization, and SMTP configuration are your responsibility.

For DNS, ensure that:

- All Sekoia application servers can resolve each other by hostname and communicate freely.
- All nodes can resolve and reach the code and artifact repositories.
- All nodes can resolve and connect to the designated SMTP server.
- The orchestration node can resolve and access every Kubernetes node by hostname.
- DNS records exist for the values you set in `global.host` and `global.alternative_hosts` before deployment.

For NTP, ensure that:

- All nodes synchronize against a customer-provided NTP server.
- Clock skew between nodes stays below 1 second at all times.

For a complete list of required ports and protocols, see [Network requirements](./network_requirements.md).

## Operational requirements

| Requirement | Details |
| :--- | :--- |
| Operations team | A dedicated in-house or partner team must handle deployment, configuration, updates, and monitoring. |
| Infrastructure management | You must provision and manage your own servers, virtual machines, or private/public cloud resources. |
| Licensing | A valid Sekoia license must be provisioned before deployment. It defines the maximum number of supervised assets and daily event-ingest capacity. The platform generates alerts and functionality may degrade if limits are reached. |

## Related links

- [Network requirements](./network_requirements.md): Full table of required network ports and protocols.
- [Reference architecture](../architecture/architecture.md): Platform components and node roles.
- [Deploy the platform](./deployment_guide.md): Step-by-step installation instructions.
