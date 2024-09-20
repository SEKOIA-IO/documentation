# Fastly

![Fastly](/assets/playbooks/library/fastly.png){ align=right width=150 }

Fastly is a content delivery network (CDN) and edge cloud platform.

## Configuration

This module accepts no configuration.

## Triggers

### Fetch new alerts from Fastly WAF [BETA]

Get last alerts from Fastly WAF

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `email` | `string` | User's email |
| `token` | `string` | API token |
| `corp` | `string` | Corporation name |
| `site` | `string` | Site name |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


### Fetch new audit logs from Fastly WAF

Get last events from Fastly WAF Audit logs

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `email` | `string` | User's email |
| `token` | `string` | API token |
| `corp` | `string` | Corporation name |
| `site` | `string` | Site name |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`Fastly` v1.0.2**