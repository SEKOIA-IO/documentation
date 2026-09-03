# Technical requirements

This article lists all infrastructure, hardware, software, storage, and network requirements for a Sekoia Self-Hosted deployment. Verify every requirement before starting the installation.

## Infrastructure components

You must provision and manage the following components outside the Kubernetes cluster.

| Component | CPU | RAM | Storage / throughput | Notes |
| :--- | :---: | :---: | :---: | :--- |
| TCP Load Balancer (e.g., HAProxy, Nginx) | 4 | 8 GB | 100 Mbps (12.5 MB/s) | Required minimum throughput. Scale according to your actual ingest volume. |
| Orchestration node | 4 | 8 GB | 200 GB | Required. Runs the self-hosted-controller (SHC). See requirements below. |
| Local image registry (e.g., Harbor, JFrog, Nexus) | 4 | 8 GB | 5 TB | Required for air-gapped deployments. |
| Local code registry (e.g., GitLab, Gitea, ForgeJo) | 1 | 4 GB | Less than 10 GB | Required for air-gapped deployments. |

### Orchestration node requirements

The orchestration node only requires Docker to run the SHC container image. It does not require Python or Ansible to be installed directly on the host.

!!! note "Orchestration node role"
    The orchestration node does not join the Kubernetes cluster. The SHC performs preflight checks, installs the complete Kubernetes cluster, manages the platform deployment through Helm and ArgoCD, and downloads deployment resources when internet access is available. The node must have SSH access to all Kubernetes nodes on TCP port 22.

## Compute node specification

Every Kubernetes worker node must meet the following minimum hardware requirements.

| Resource | Minimum requirement | Enforced by `CheckServerSpec` |
| :--- | :--- | :--- |
| CPU | 44 vCPUs at 3.2 GHz minimum | 44 cores |
| RAM | 128 GB | 120 GiB |
| Dedicated storage disk | One unused SSD of 200 GB or more; 4 TB per worker node for deployments handling data | 200 GB |
| Operating system | Debian 12 (Bookworm) | Debian 12 or later |
| Hostname | Unique across all manager and worker nodes | Uniqueness |
| Time synchronization | NTP enabled and clock synchronized | Both |

The `CheckServerSpec` command blocks the installation when a manager or worker node fails any of the checks in the last column. See [CheckServerSpec](../troubleshooting/debug_tool.md#checkserverspec) for the failure messages and their remediation.

!!! warning "SSD usage"
    `CheckServerSpec` enforces a 200 GB dedicated-disk minimum to support ultra-tight deployments. Any deployment that handles customer data must provision 4 TB per worker node. How quickly that capacity is consumed depends on the customer's use of the platform. Do not use these disks for long-term event retention; event data requires dedicated S3-compatible storage (see [Storage](#storage) below).

### Dedicated storage disk

Ceph and Longhorn provision persistent volumes from a dedicated block device on every node. Each manager and worker node must expose at least one whole disk that meets all of the following conditions:

- 200 GB or larger.
- No partition table and no filesystem.
- Not read-only.

Attach the disk and leave it unformatted before you start the installation. `CheckServerSpec` skips this check once K3s is installed, because Ceph and Longhorn have consumed the disk by then.

!!! warning "Do not partition or format the storage disk"
    A disk that already carries a filesystem or a partition table is not counted as eligible. If the node exposes no other eligible disk, the preflight fails and the installation does not start.

### Node hostnames

Every manager and worker node must have a unique hostname. Kubernetes registers nodes by hostname, so two nodes sharing one hostname collapse into a single cluster member and lose their workloads.

To rename a node before the installation, run:

```bash
hostnamectl set-hostname <NEW_HOSTNAME>
```

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
| Medium | 2 TB/day | ~20,000 | 24 | 2 | 800 TB |
| Large | 5 TB/day | ~50,000 | 60 | 2 | 2,000 TB |

**What is an asset?** An asset is any monitored entity (server, endpoint, network device) that generates log events sent to the platform. The asset counts above are approximations. Actual capacity depends on the size and frequency of ingested log messages.

**S3 storage calculation:** Total S3 capacity = daily ingest (GB) x retention period (days). The table above assumes 365 days of retention.

**Node roles:** Each cluster requires exactly 3 manager nodes (Kubernetes control plane), which is the only supported manager-node topology. The **Compute nodes** column above corresponds to the number of worker nodes.

## Storage

An S3-compatible bucket is required for event data storage and platform backups. You must provision this bucket before deployment.

| Use | Notes |
| :--- | :--- |
| Event storage | Long-term data lake for all ingested events. Customer-managed. See sizing table above. |

The S3-compatible storage must meet the following performance requirements:

| Benchmark | Required performance |
| :--- | :---: |
| GET throughput | — MB/s |
| PUT throughput | — MB/s |
| DELETE/STAT metadata operations | — operations/s |

!!! note "S3 benchmarks in progress"
    S3 performance benchmarks are ongoing. The required values will be available by the GA release.

## Network requirements

DNS management, NTP synchronization, and SMTP configuration are your responsibility.

For DNS, ensure that:

- All Sekoia application servers can resolve each other by hostname and communicate freely.
- All nodes can resolve and reach the Git repository and OCI registry.
- All nodes can resolve and connect to the designated SMTP server.
- The orchestration node can resolve and access every Kubernetes node by hostname.
- DNS records exist for `global.host` and `global.delivery_host` before deployment.
- When `global.kube_manager_host` is configured as a hostname, its DNS record exists before deployment.

See [Platform endpoints](./deployment_configuration.md#platform-endpoints) for the complete configuration reference for these values.

For NTP, ensure that:

- All nodes synchronize against a customer-provided NTP server.
- Clock skew between nodes stays below 1 second at all times.
- A time-sync service (`systemd-timesyncd` or `chrony`) is installed and enabled on every node.

`CheckServerSpec` reads `timedatectl show` on each node and fails when NTP is disabled or the clock is not synchronized. To enable NTP on a node, run:

```bash
timedatectl set-ntp true
```

If NTP is enabled but the clock is not synchronized, verify that the node can reach your NTP servers, then restart the time-sync service with `systemctl restart systemd-timesyncd` or `systemctl restart chrony`.

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
- [Debug your deployment](../troubleshooting/debug_tool.md): `CheckServerSpec` output and remediation for each failed requirement.
- [Deploy the platform](./deployment_guide.md): Step-by-step installation instructions.
