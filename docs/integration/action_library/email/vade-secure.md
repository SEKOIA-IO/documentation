# Vade Secure

![Vade Secure](/assets/playbooks/library/vade-secure.png){ align=right width=150 }

Vade Secure Module

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `oauth2_authorization_url` | `string` | OAuth2 authorization URL |
| `api_host` | `string` | API Url of the VadeSecure platform (e.g. 'https://m365.eu.vadesecure.com') |
| `client_id` | `string` | OAuth2 client identifier |
| `client_secret` | `string` | OAuth2 client secret |

## Triggers

### Get M365 Email Events

Get last M365 Email Events

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `tenant_id` | `string` | Identifier of your 365 Tenant |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `emails_path` | `string` | The filename containing the events (emails or remediations) |


## Extra

Module **`Vade Secure` v1.44**