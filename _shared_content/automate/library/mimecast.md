# Mimecast

![Mimecast](/assets/playbooks/library/mimecast.png){ align=right width=150 }

Mimecast offers cloud-based email security, archiving, and continuity solutions to protect against cyber threats and ensure compliance.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `client_id` | `string` | Client ID |
| `client_secret` | `string` | Client Secret |

## Triggers

### [BETA] Fetch new email events from Mimecast

Mimecast - Email Security

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`Mimecast` v1.0.1**