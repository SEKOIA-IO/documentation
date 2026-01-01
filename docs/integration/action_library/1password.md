# 1Password

![1Password](/assets/playbooks/library/1password.png){ align=right width=150 }

1Password's Enterprise Password Manager offers robust security features for businesses, enabling secure sharing and management of passwords and sensitive data across teams, with advanced admin controls and seamless integration into existing workflows.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | 1Password base URL |
| `api_token` | `string` | API token |

## Triggers

### [BETA] Fetch new events from 1Password EPM

Get last events from 1Password EPM

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |


## Extra

Module **`1Password` v1.0.0**