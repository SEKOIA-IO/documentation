# PagerDuty

[PagerDuty](https://www.pagerduty.com/) is an incident response platform for IT departments that allows triggering alerts and managing incidents.

With this module, you can [trigger alerts](#Trigger-Alert) to PagerDuty, which allows you to receive notifications in PagerDuty when a new alert is raised.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `integration_key` | `string` | The integration key (a.k.a routing key) of your PagerDuty Service |
| `integration_url` | `string` | URL of the PagerDuty endpoint |

## Actions

### Trigger Alert

Trigger alert to PagerDuty.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_uuid` | `string` | The Unique identifier of the alert |
| `api_key` | `string` | The SEKOIA.IO API-Key to read the alert content. |
| `base_url` | `string` | Base URL of SEKOIA.IO api (e.g. https://api.sekoia.io/). |


## Extra

Module **`PagerDuty` v1.11**
