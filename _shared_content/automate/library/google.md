# Google

![Google](/assets/playbooks/library/google.svg){ align=right width=150 }

Google module

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `credentials` | `object` | Credentials to use. You can find them in the credentials file |

## Triggers

### Get user activities

Get user activities using google reports

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `application_name` | `string` | The application from which the activities should be fetched |
| `timedelta` | `integer` | The temporal shift, in the past, in minutes, the connector applies when fetching the events (default to 0 minutes ago) |
| `start_time` | `integer` | The number of hours from which events should be queried. |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `admin_mail` | `string` | Email of your google admin |


### Get login user activities

Get Login user activities using google reports api

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `timedelta` | `integer` | The temporal shift, in the past, in minutes, the connector applies when fetching the events (default to 150 minutes ago) |
| `start_time` | `integer` | The number of hours from which events should be queried. |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `admin_mail` | `string` | Email of your google admin |


### Connect to the specified project subscription

Connect to the Google Cloud Pub/Sub topic and return events

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_key` | `string` | Intake key to use when sending events |
| `frequency` | `integer` | Batch frequency in seconds |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `project_id` | `string` | Project ID |
| `subject_id` | `string` | Subscription ID |
| `chunk_size` | `integer` | The size of chunks for the batch processing (max is 1000) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `messages_path` | `string` | Path to the file holding the results |

## Actions

### Run a query against a BigQuery table

Execute the given query and return the results

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `query` | `string` | Query to run |
| `parameters` | `array` | Parameters to use inside the query |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `items_path` | `string` | Path to the file holding the results |


## Extra

Module **`Google` v1.20.9**