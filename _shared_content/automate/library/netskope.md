# Netskope

![Netskope](/assets/playbooks/library/netskope.png){ align=right width=150 }

[Netskope](https://www.netskope.com/) is a cybersecurity company, providing solutions to protect data in cloud apps and network security applying zero trust principles.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | API base URL |

## Triggers

### [BETA] Fetch new events from Netskope

Get last events from the Netskope platform through the API v2

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_token` | `string` | The API token |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `consumer_group` | `string` | A unique name to track event consumption (default empty for auto-generated one) |


## Extra

Module **`Netskope` v0.3**