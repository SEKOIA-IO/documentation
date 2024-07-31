# Bitsight

![Bitsight](/assets/playbooks/library/bitsight.png){ align=right width=150 }

Bitsight connector for audit logs

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `company_uuids` | `array` | The list of company uuids |
| `api_token` | `string` | The API Token to authenticate calls to the Bitsight API |

## Triggers

### [BETA] Fetch new findings from Bitsight

Get findings from a Bitsight

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `batch_limit` | `integer` | Maximum number of events to send in a single batch |


## Extra

Module **`Bitsight` v1.0.0**