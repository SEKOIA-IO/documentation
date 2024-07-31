# Imperva

![Imperva](/assets/playbooks/library/imperva.png){ align=right width=150 }

Imperva Module

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Imperva API base URL |
| `api_id` | `string` | Imperva API ID |
| `api_key` | `string` | Imperva API key |
| `keys` | `object` | Encryption keys |

## Triggers

### Imperva WAF logs

Fetch Imperva WAF logs

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds, default 2s |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_key` | `string` | Intake key to use when sending events |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `logs` | `array` | A list of logs. |
| `logs_path` | `string` | The filename containing the logs |


## Extra

Module **`Imperva` v1.16**