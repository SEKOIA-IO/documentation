# Prepare the infrastructure

This section explains how to prepare every server and every service **before** you run the self-hosted-controller (SHC). Read it before [Deploy the platform](../deployment/deployment_guide.md).

The SHC installs Kubernetes and the Sekoia platform. It does **not** install the operating system, the load balancer, the Git server, the OCI registry or the S3 storage. You prepare them yourself, with the rules in this section.

## How to read this section

### Rule words

Each rule starts with one of these words. They have a precise meaning.

| Word | Meaning | What happens if you do not follow it |
| :--- | :--- | :--- |
| **MUST** | Mandatory. | The installation fails, or the platform does not work. |
| **MUST NOT** | Forbidden. | The installation fails, or the platform does not work. |
| **SHOULD** | Recommended. You can do something else. | You **must** change your `config.yml` or your `run-shc.sh` script. Each page has a table **"If you do not follow a SHOULD rule"** with the exact change. |
| **MAY** | Optional. | Nothing. |

### Technology tabs

Many steps depend on the product you use: for example Gogs or GitLab for Git, Harbor or another product for the OCI registry. These steps are in **tabs**, one tab per product.

Each tab starts with a **validation status**:

| Status | Meaning |
| :--- | :--- |
| **Validated in the Sekoia lab** | Sekoia installed the platform with this product, with the exact commands of the tab. |
| **Validated in a customer project** | A real installation used this product, with the commands of the tab. |

If your product has no tab, it is **not validated**. It can work if it follows every MUST rule of the page, but contact Sekoia before you use it.

!!! note "About the lab"
    The Sekoia lab runs on OpenStack virtual machines with Debian 13. It validates the **procedures**, not the hardware sizes: the lab nodes have 32 vCPUs and about 115 GiB of RAM, below the [compute node specification](../deployment/deployment_prerequisites.md#compute-node-specification), and use the `sizing/minimal.yaml` profile. Sekoia has also validated installations on Debian 12 and on nodes that meet the compute node specification. The IP addresses, names and passwords in the examples are placeholders: replace every value in angle brackets, for example `<REGISTRY_IP>`, with your own value.

### Placeholders used in this section

| Placeholder | Meaning | Example |
| :--- | :--- | :--- |
| `<ADMIN_USER>` | The Linux account the SHC uses on every Kubernetes node (`utils.ansible.user`). | `sekoia` |
| `<MANAGER_1_IP>` … `<MANAGER_3_IP>` | IP addresses of the 3 manager nodes. | `10.0.0.1` |
| `<WORKER_1_IP>` … | IP addresses of the worker nodes. | `10.0.0.10` |
| `<LB_IP>` | IP address of the load balancer. | `10.0.0.50` |
| `<REGISTRY_IP>` | IP address of the OCI registry server. | `10.0.0.60` |
| `<GIT_IP>` | IP address of the Git server. | `10.0.0.60` |
| `<DOMAIN>` | Your DNS domain. | `sekoia.example.com` |

## Order of work

Follow the pages in this order. Each page ends with a **checklist**. Do not start the next page before every item of the checklist is done.

| Step | Page | Where you work |
| :---: | :--- | :--- |
| 1 | [Prepare the Kubernetes nodes](./kubernetes_nodes.md) | Each manager and worker node |
| 2 | [Prepare the orchestration node](./orchestration_node.md) | The orchestration node |
| 3 | [Prepare the load balancer](./load_balancer.md) | The load balancer server |
| 4 | [Prepare the Git repository](./git_repository.md) | The Git server |
| 5 | [Prepare the OCI registry](./oci_registry.md) | The registry server |
| 6 | [Prepare the S3 object storage](./object_storage.md) | The S3 storage and one Kubernetes node |
| 7 | [Prepare DNS, time, email and certificates](./dns_time_certificates.md) | DNS server, all servers, orchestration node |

When every checklist is done, continue with [Deploy the platform](../deployment/deployment_guide.md).

## What the minimal configuration expects

The starter `config.yml` in [Configure the deployment](../deployment/deployment_configuration.md#create-the-configuration-file) contains only the required fields. When your infrastructure follows every **MUST** and every **SHOULD** rule of this section, you add only **one** field to it: the release mode (see the last row of the table below).

The table below summarizes what the minimal configuration expects from each service. The pages give the details.

| Service | The minimal configuration expects |
| :--- | :--- |
| Kubernetes nodes | Debian 12 or 13 in IPv4, swap disabled, the same Linux user on every node, SSH with a key on port 22, `sudo` without a password, an empty data disk. |
| Git | A repository that already exists with at least one commit, reached over HTTP or HTTPS with a public certificate, with a user name and a password. The SHC pushes to the **default branch**. |
| OCI registry | A registry over HTTPS (a self-signed certificate is accepted) with token (Bearer) authentication, a **project that already exists**, a user that can push, pull and delete. |
| S3 storage | An S3-compatible endpoint with a public certificate (or HTTP), **16 buckets that already exist**, one access key that reads and writes objects, path-style URLs. |
| Load balancer | A TCP load balancer that forwards ports 80, 443, 10514 and 11514 to the nodes. |
| DNS | Records for `global.host`, `global.delivery_host` and `global.alternative_hosts` that point to the load balancer. |
| Certificate | A certificate and its private key, in `TRAEFIK_PUBKEY` and `TRAEFIK_PRIVKEY`. An installation without a certificate is not supported in this release. |
| Release | Add `global.version.fetch.offline: true` when you extract the release archive yourself, as in [Deploy the platform](../deployment/deployment_guide.md#step-2-transfer-and-extract-the-archive). Otherwise add `global.version.fetch.endpoint`: see [Release download and security content](../deployment/deployment_configuration.md#release-download-and-security-content). |
