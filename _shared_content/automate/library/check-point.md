# Check Point

![Check Point](/assets/playbooks/library/check-point.png){ align=right width=150 }

Check Point Harmony is the industry’s first unified security solution for users devices and access.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `client_id` | `string` | Client Id to interact with Checkpoint API |
| `secret_key` | `string` | Secret key to work with Checkpoint API |
| `authentication_url` | `string` | Authentication url to authenticate Checkpoint API |
| `base_url` | `string` | Base url to interact with Checkpoint API |

## Triggers

### [BETA] Collect Checkpoint Harmony Mobile events

Trigger playbook to get Checkpoint Harmony Mobile events

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ratelimit_per_minute` | `integer` | Maximum number of requests per minute |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |
| `frequency` | `integer` | Batch frequency in seconds |


## Extra

Module **`Check Point` v1.1.7**