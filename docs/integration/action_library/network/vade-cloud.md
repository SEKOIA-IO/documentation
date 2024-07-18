# Vade Cloud

![Vade Cloud](/assets/playbooks/library/vade-cloud.png){ align=right width=150 }



## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `hostname` | `string` | Vade Cloud API hostname |
| `login` | `string` | Vade Cloud Email |
| `password` | `string` | Vade Cloud password |

## Triggers

### [BETA] Fetch new logs from Vade Cloud

Get last logs from the Vade Cloud platform

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`Vade Cloud` v1.4.0**