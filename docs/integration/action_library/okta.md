# Okta

![Okta](/assets/playbooks/library/okta.png){ align=right width=150 }

[Okta](https://www.okta.com/) is an entreprise-grade, identity management service compatible with cloud apps as well as many on-premises applications

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | The url to your Okta tenant |
| `apikey` | `string` | The APIkey to authenticate call to the API |

## Triggers

### Fetch new audit logs from OKTA

Get last system logs from the OKTA platform

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `filter` | `string` | [Filter Expression](https://developer.okta.com/docs/reference/api/system-log/#expression-filter) that filters the results |
| `q` | `string` | Filters the log events results by one or more exact [keywords](https://developer.okta.com/docs/reference/api/system-log/#keyword-filter) |
| `ratelimit_per_minute` | `integer` | The number of requests allowed to the API in one minute for the token |


## Extra

Module **`Okta` v2.8.0**