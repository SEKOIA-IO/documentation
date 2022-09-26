# Sophos

![Sophos](/assets/playbooks/library/sophos.png){ align=right width=150 }

Sophos Module

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `oauth2_authorization_url` | `string` | OAuth2 authorization URL |
| `api_host` | `string` | API Url of the Sophos Central API (e.g. 'https://api-{dataRegion}.central.sophos.com') |
| `client_id` | `string` | OAuth2 client identifier |
| `client_secret` | `string` | OAuth2 client secret |

## Triggers

### Get Sophos events

Forward Sophos Events

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `exclude_types` | `array` | A list of type to exclude from the pulling |


## Extra

Module **`Sophos` v1.1.3**