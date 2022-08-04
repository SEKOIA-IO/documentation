# Sentinel One

![Sentinel One](/assets/playbooks/library/sentinel-one.png){ align=right width=150 }

This module interacts with the Sentinel One API

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `hostname` | `string` | The domain-name to the Sentinel One instance |
| `api_token` | `string` | The API token to authenticate the requests |

## Actions

### Deisolate an endpoint

Connect the endpoint back to the network

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ids` | `array` | The list of Agent IDs to filter by |
| `account_ids` | `array` | The list of Account IDs to filter by |
| `group_ids` | `array` | The list of network group to filter by |
| `site_ids` | `array` | The list of Site IDs to filter by |
| `query` | `string` | Free-text search term to use |


#### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `affected` | `integer` | The number of deisolated endpoints |

### Isolate an endpoint

Disconnect the endpoint from the network

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ids` | `array` | The list of Agent IDs to filter by |
| `account_ids` | `array` | The list of Account IDs to filter by |
| `group_ids` | `array` | The list of network group to filter by |
| `site_ids` | `array` | The list of Site IDs to filter by |
| `query` | `string` | Free-text search term to use |


#### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `affected` | `integer` | The number of isolated endpoints |

### Query events in Deep Visibility

Create a query in Deep Visibility and get the events

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `group_ids` | `array` | The list of network group to filter by |
| `site_ids` | `array` | The list of Site IDs to filter by |
| `query` | `string` | Free-text search term to use |
| `from_date` | `string` | Get events created after this timestamp |
| `to_date` | `string` | Get events created before or at this timestamp |
| `timeout` | `integer` | The maximum time, in seconds, the query should be processed in (default 300s) |


#### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status` | `string` | The status of the query |
| `status_reason` | `string` | The reason of the status |
| `events` | `array` | The events got from the query |

### Execute a remote script

Execute a remote script and get the results

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `script_id` | `string` | The identifier of the script to identify |
| `output_destination` | `string` | The destination of the result |
| `task_description` | `string` | A short description of the task |
| `timeout` | `integer` | The maximum time, in seconds, the execution should be processed in (default: 300s) |
| `settings` | `object` | The settings to forward the remote script |
| `filters` | `object` | Filters to select the agents that will run the remote script |


#### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status` | `string` | The status of the run |
| `status_reason` | `string` | The reason of the status |
| `result_file` | `object` | The url to download the result (for cloud destination) |


## Extra

Module **`Sentinel One` v1.1.2**