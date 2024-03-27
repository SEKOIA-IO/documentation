# Lacework

![Lacework](/assets/playbooks/library/lacework.png){ align=right width=150 }

[Lacework](https://www.lacework.com/) is a cybersecurity company specializing in cloud security and compliance, offering automated threat detection and response solutions for modern cloud environments.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `key_id` | `string` | The KeyId of your API Key |
| `secret` | `string` | The secret of your API Key |
| `account` | `string` | The account of your API Key (e.g: `YourLaceworkTenant.lacework.net`) |

## Triggers

### [BETA] Fetch new logs from Lacework

Get last system logs from the Lacework platform

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `filter` | `string` | [Filter Expression](https://docs.lacework.net/console/filter-alerts) that filters the results |
| `ratelimit_per_hour` | `integer` | The number of requests allowed to the API in one hour for the token |


## Extra

Module **`Lacework` v0.1.5**