# Self-Hosted technical requirements

Sekoia Self-Hosted is an enterprise-grade solution that requires specific infrastructure, network, and operational readiness. As a customer-operated platform, you are responsible for the end-to-end lifecycle, including provisioning, management, and monitoring.

## Infrastructure Prerequisites
You must provision and manage the following dedicated infrastructure components:

| Component | CPU | RAM | Storage / Throughput |
| :--- | :--- | :--- | :--- |
| **Load Balancer** (e.g., HAProxy, Nginx) | 4 | 8GB | 50MB/s (validate per customer) |
| **Local Image Registry** (e.g., Harbor) | 4 | 8GB | 5TB |
| **Local Code Registry** (e.g., Git) | 4 | 8GB | 100GB |
| **Orchestration Node** (Admin) | 4 | 8GB | 100GB |

## Networking and Storage
* **Networking**: You must provide internal DNS resolution, synchronized NTP infrastructure, and SMTP servers for alerts.
* **S3 Storage**: You must provide an S3-compatible bucket for event storage.
    * **Calculation**: Total capacity = Raw daily ingested events (GB) x retention days.
    * **Note**: The 4TB local SSD on compute nodes is strictly for system use, not long-term event storage.

## Scaling Table
The following table outlines the estimated hardware footprint per cluster based on asset count and daily ingestion volume.

| Assets | Daily Volume | Compute Nodes | GPU Nodes |
| :--- | :--- | :--- | :--- |
| 5,000 | 500 GB | 6 | 1 |
| 10,000 | 1 TB | 12 | 1 |
| 20,000 | 2 TB | 24 | 2 |
| 50,000 | 5 TB | 60 | 2 |
| 100,000 | 10 TB | 120 | 2 |

!!! warning "Theoretical Sizing"
    The figures provided in the scaling table are estimates for guidance. Infrastructure requirements vary based on specific replication constraints, data retention policies, and query patterns. These figures must be validated by Sekoia prior to deployment.

!!! warning "Hardware Specifications"
    Each compute node must meet the minimum specification: 44 CPU (3.2 GHz minimum), 128GB RAM, and 4TB SSD (Debian 11). GPU nodes require an NVIDIA H100.

## Operational Readiness
* **Operations Team**: A dedicated in-house or partner team must handle deployment, configuration, updates, and 24/7 monitoring.
* **Infrastructure Management**: You must have the ability to provision and manage your own private cloud, on-premises servers, or virtual machines.
* **Licensing**: A valid license must be provided, defining the maximum supervised assets and daily event-ingest capacity.