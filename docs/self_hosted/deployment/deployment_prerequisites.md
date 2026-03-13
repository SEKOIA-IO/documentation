# Self-Hosted technical requirements

Sekoia Self-Hosted requires specific infrastructure, network, and operational readiness. As a customer-operated platform, you are responsible for the end-to-end lifecycle.

## General requirements
Ensure your organization meets these operational prerequisites:

* **Operations team**: You must maintain a dedicated team responsible for deployment, configuration, and monitoring.
* **Infrastructure management**: You must be able to provision and manage your own infrastructure, whether on-premises or via virtual machines.
* **Licensing**: You must possess a valid license defining the maximum supervised assets and event-ingest capacity.

## Hardware footprint
The following specifications are estimated for a deployment of approximately 500GB/day.

| Component | Specification |
| :--- | :--- |
| **Compute servers (6x)** | 44 CPU (3.2 GHz min), 128GB RAM, 2TB SSD, Debian 11 |
| **GPU server (1x)** | NVIDIA H100 dedicated for AI processing |
| **Storage** | S3-compatible bucket |
| **Admin node (1x)** | Debian 12, Python 3.11, 4 CPU / 8GB RAM |

!!! warning "Consult Sekoia for sizing"
    These figures are estimates provided for guidance. Contact Sekoia for a full requirements review before you commence deployment.

## Network and connectivity
Configure the internal network to allow communication between platform components:

* **DNS and Time**: Provide DNS resolution for all nodes and a synchronized NTP infrastructure.
* **Load balancer**: Configure a load balancer for Web UI access (Ports 80/443) and event ingestion (Ports 10514/11514).
* **Internal traffic**: Allow communication for Kubernetes management (Ports 6443, 2379-2380) and VXLAN overlay (Port 8472).