# ExtraHop

![ExtraHop](/assets/playbooks/library/extrahop.png){ align=right width=150 }

ExtraHop is a leading provider of network detection and response (NDR) solutions.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | API base URL |
| `client_id` | `string` | Client ID |
| `client_secret` | `string` | Client Secret |

## Triggers

### Fetch new alerts from ExtraHop Reveal(x) 360

Get last logs from the ExtraHop Reveal(x) 360

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`ExtraHop` v1.1.1**