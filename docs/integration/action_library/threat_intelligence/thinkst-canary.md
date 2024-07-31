# Thinkst Canary

![Thinkst Canary](/assets/playbooks/library/thinkst-canary.png){ align=right width=150 }

Thinkst Canary specializes in innovative cybersecurity solutions, particularly using honeypot technology to detect and alert on threats within networks. They provide early warnings of breaches with minimal false positives.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Base URL |
| `auth_token` | `string` | Auth token |

## Triggers

### [BETA] Fetch Thinkst Canary Events

Get latest events from Thinkst Canary

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_server` | `string` |  |
| `intake_key` | `string` |  |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |
| `frequency` | `integer` | Batch frequency in seconds |
| `acknowledge` | `boolean` | Whether to acknowledge received events |


## Extra

Module **`Thinkst Canary` v1.0.0**