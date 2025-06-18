uuid: 97864342-32c5-4076-b590-ba0179db9233
name: PagerDuty
type: playbook

# PagerDuty

![PagerDuty](/assets/playbooks/library/pagerduty.png){ align=right width=150 }

PagerDuty is an incident response platform for IT departments it allows triggering alerts and managing incidents.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `integration_key` | `string` | The integration key (a.k.a routing key) of your PagerDuty Service |
| `integration_url` | `string` | URL of the PagerDuty endpoint |

## Actions

### Trigger Alert

Trigger alert to PagerDuty

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_uuid` | `string` | The Unique identifier of the alert |
| `api_key` | `string` | The Sekoia.io API-Key to read the alert content. |
| `base_url` | `string` | Base URL of Sekoia.io api (e.g. https://api.sekoia.io/). |


## Extra

Module **`PagerDuty` v1.21.0**