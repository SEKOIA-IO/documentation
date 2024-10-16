uuid: 0664bc2d-8f09-410f-ab8f-e0e07911a6f4
name: Nybble
type: playbook

# Nybble

![Nybble](/assets/playbooks/library/nybble.png){ align=right width=150 }

[Nybble Hub](https://nybble-security.io) is the worldwide first blue team community which handles your alerts at a glance.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `nhub_url` | `string` | Nybble Hub Connector Base URL |
| `nhub_username` | `string` | Nybble Hub Connector username |
| `nhub_key` | `string` | Nybble Hub Connector Key to authenticate the requests |

## Actions

### Create Alert

Create an Alert into Nybble Hub

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_data` | `object` | Received alert, from Sekoia 'Get Alert' action |
| `rule` | `object` | Alert Rule from Rule Catalog, from Sekoia 'Get Rule' action |
| `events` | `array` | Related Events, from Sekoia 'Get The Alert Events' action |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status` | `boolean` |  |
| `details` | `string` |  |


## Extra

Module **`Nybble` v1.0.2**