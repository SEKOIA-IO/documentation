# Broadcom Cloud Secure Web Gateway

![Broadcom Cloud Secure Web Gateway](/assets/playbooks/library/broadcom-cloud-secure-web-gateway.png){ align=right width=150 }

Broadcom Cloud Secure Web Gateway is a cloud-native security solution providing advanced threat protection, content filtering, and data loss prevention, ensuring secure internet access and compliance for organizations with flexible deployment options and comprehensive web security features.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `username` | `string` | Username to do authentication on remote server |
| `password` | `string` | Password to do authentication on remote server |

## Triggers

### [BETA] Get Broadcom Cloud SWG events

Trigger playbook to get Broadcom Cloud SWG events

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |


## Extra

Module **`Broadcom Cloud Secure Web Gateway` v1.1.0**