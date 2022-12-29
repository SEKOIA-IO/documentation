# CrowdStrike Falcon

![CrowdStrike Falcon](/assets/playbooks/library/crowdstrike-falcon.png){ align=right width=150 }

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

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_key` | `string` | Intake key to use when sending events |
| `tg_base_url` | `string` | The base_url for the ThreatGraphAPI |
| `tg_username` | `['string', 'null']` | The username for the ThreatGraphAPI |
| `tg_password` | `['string', 'null']` | The password for the ThreatGraphAPI |


## Extra

Module **`CrowdStrike Falcon` v1.1.0**