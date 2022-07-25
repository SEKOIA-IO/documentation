# CrowdStrike Falcon

![CrowdStrike Falcon](/assets/playbooks/library/crowdstrike-falcon.png){ align=right }

Integrates with CrowdStrike Falcon EDR

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `client_id` | `string` | Client Identifier |
| `client_secret` | `string` | Client Secret |
| `base_url` | `string` | Base URL of the API |

## Triggers

### Fetch CrowdStrike Falcon Events

Get latest events from CrowdStrike Falcon

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`CrowdStrike Falcon` v0.9**