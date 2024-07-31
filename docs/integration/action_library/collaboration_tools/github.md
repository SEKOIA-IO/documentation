# Github

![Github](/assets/playbooks/library/github.png){ align=right width=150 }

Github connector for audit logs

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `org_name` | `string` | The name of your Github organization |
| `apikey` | `string` | The APIkey to authenticate call to the Github API |
| `pem_file` | `string` | Pem file to interact with Github API |
| `app_id` | `integer` | Github app id to interact with Github API |

## Triggers

### Fetch new audit logs from Github

Get last audit logs from a Github organization

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `ratelimit_per_minute` | `integer` | The number of requests allowed to the API in one minute for the token |


## Extra

Module **`Github` v1.5.0**