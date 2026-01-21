# Duo

![Duo](/assets/playbooks/library/duo.png){ align=right width=150 }

Duo is a Cisco company offering solutions for strong authentication with multi-factor authentication (MFA), single sign-on (SSO), remote access or device trusting.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `hostname` | `string` | Duo Admin API hostname |
| `integration_key` | `string` | Duo Admin API integration key |
| `secret_key` | `string` | Duo Admin API secret key |

## Triggers

### Fetch new logs from Duo

Get last logs from the Duo platform

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`Duo` v1.8.0**