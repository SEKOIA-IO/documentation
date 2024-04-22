# Ubika

![Ubika](/assets/playbooks/library/ubika.png){ align=right width=150 }

Ubika is a cybersecurity company offering products to protect web applications and APIs

## Configuration

This module accepts no configuration.

## Triggers

### [BETA] Fetch new alerts from Ubika Cloud Protector



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `provider` | `string` | Id of cirrus provider |
| `tenant` | `string` | Id of cirrus tenant |
| `token` | `string` | API token |


## Extra

Module **`Ubika` v0.1.1**