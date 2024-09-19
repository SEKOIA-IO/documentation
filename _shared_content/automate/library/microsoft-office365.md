# Microsoft Office365

![Microsoft Office365](/assets/playbooks/library/microsoft-office365.png){ align=right width=150 }

Microsoft Office 365 is an online service, providing the Microsoft Office Products.

## Configuration

This module accepts no configuration.

## Triggers

### Fetch events from MessageTrace API (deprecated)

Fetch events for MessageTrace API

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `timedelta` | `integer` | The temporal shift, in the past, in minutes, the connector applies when fetching the events (default to 5 minutes ago) |
| `start_time` | `integer` | The number of hours from which events should be queried. |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `account_name` | `string` | The account name to use |
| `account_password` | `string` | The password associated with the account |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


### Fetch events from MessageTrace API (OAuth)

Fetch events for MessageTrace API (OAuth)

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `tenant_id` | `string` | The ID of the corresponding Tenant |
| `client_id` | `string` | The account name to use |
| `client_secret` | `string` | The password associated with the account |
| `timedelta` | `integer` | The temporal shift, in the past, in minutes, the connector applies when fetching the events (default to 5 minutes ago) |
| `start_time` | `integer` | The number of hours from which events should be queried. |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`Microsoft Office365` v2.11**