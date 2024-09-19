# Trellix

Trellix has been involved in the detection and prevention of major cybersecurity attacks. It provides hardware, software, and services to investigate cybersecurity attacks, protect against malicious software, and analyze IT security risks

## Configuration

This module accepts no configuration.

## Triggers

### [ALPHA] Get Trellix ePo events

Trigger playbook to get Trellix events information

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `client_id` | `string` | Client id to interact with Trellix API |
| `client_secret` | `string` | Client secret to interact with Trellix API |
| `api_key` | `string` | Api key to interact with Trellix API |
| `delay` | `integer` | Delay between running the connector |
| `base_url` | `string` | Base url of the Trellix API |
| `auth_url` | `string` | Url of the authentication server |
| `ratelimit_per_minute` | `integer` | Maximum number of requests per minute |
| `records_per_request` | `integer` | Number of records to fetch per 1 request |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`Trellix` v1.2**