uuid: e76687ed-db66-482a-8549-f3ef3b248e06
name: Digital Shadows
type: playbook

# Digital Shadows

![Digital Shadows](/assets/playbooks/library/digital-shadows.png){ align=right width=150 }

Digital Shadows Module

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_url` | `string` | URL of the SearchLight instance |
| `searchlight_account_id` | `string` | SearchLight Account ID |
| `basicauth_key` | `string` | HTTP Basic authentication key |
| `basicauth_secret` | `string` | HTTP Basic authentication secret |

## Triggers

### Get SearchLight Alerts

Get last created SearchLight alerts and incidents

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alerts` | `array` | SearchLight Alerts |


## Extra

Module **`Digital Shadows` v1.19.0**