# Cybereason

![Cybereason](/assets/playbooks/library/cybereason.png){ align=right width=150 }

[CyberReason](https://www.cybereason.com/) is a Cybersecurity company providing products to detect and prevents attacks targeting endpoints

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | API base URL |
| `username` | `string` | The username to use to authenticate against the API |
| `password` | `string` | The password to use to authenticate against the API |

## Triggers

### [LEGACY] Fetch new events from Cybereason

Get last events from the Cybereason platform up to version 23.1.152

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `group_ids` | `array` | The sensors' group ids from which events must be retrieved |


### Fetch new events from Cybereason [23.1.152+]

Get last events from the Cybereason platform from versions 23.1.152 and higher

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `group_ids` | `array` | The sensors' group ids from which events must be retrieved |


## Extra

Module **`Cybereason` v1.13.2**