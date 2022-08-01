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


## Extra

Module **`Sentinel One` v1.0.2**