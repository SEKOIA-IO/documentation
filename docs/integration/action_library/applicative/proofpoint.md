# Proofpoint

![Proofpoint](/assets/playbooks/library/proofpoint.png){ align=right width=150 }

Proofpoint Module

## Configuration

This module accepts no configuration.

## Triggers

### Get Proofpoint PoD events

Forward Proofpoint PoD Events

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_host` | `string` | API Url of the ProofPoint PoD |
| `api_key` | `string` | The APIKey that authenticate the request |
| `cluster_id` | `string` | The cluster ID |
| `type` | `string` | The type of messages to collect |
| `since_time` | `['string', 'null']` | The starting time (up to 30 days ago) to collect log data, as ISO8601 format |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |


### Get Proofpoint TAP events

Forward Proofpoint TAP Events

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_host` | `string` | API Url of the ProofPoint TAP |
| `client_principal` | `string` | The authentication principal |
| `client_secret` | `string` | The authentication secret |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |


## Extra

Module **`Proofpoint` v1.12**