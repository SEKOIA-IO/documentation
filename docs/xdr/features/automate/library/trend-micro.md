# Trend Micro

![Trend Micro](/assets/playbooks/library/trend-micro.png){ align=right width=150 }



## Configuration

This module accepts no configuration.

## Triggers

### Fetch new logs

Get last logs from the Trend Micro Email Security platform

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `service_url` | `string` | API service URL |
| `username` | `string` | Trend Micro username |
| `api_key` | `string` | Trend Micro api_key |
| `frequency` | `integer` | Batch frequency in seconds |
| `batch_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`Trend Micro` v1.4.0**