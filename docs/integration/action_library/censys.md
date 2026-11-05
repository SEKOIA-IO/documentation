uuid: 48a7eb68-f319-4498-b3ed-461d690e6d05
name: Censys
type: playbook

# Censys

![Censys](/assets/playbooks/library/censys.png){ align=right width=150 }

Censys is Cybersecurity company discovering and inventoring assets exposed on Internet. The Censys API provides programmatic access to the same data accessible through the web interface

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_user_id` | `string` | Censys API user ID |
| `api_user_secret` | `string` | Censys API user secret |

## Actions

### Get Report

Generate a Censys report from results

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `query` | `string` | Query to execute |
| `index` | `string` | Name of the index to use |
| `field` | `string` | The field you are running a breakdown on in dot notation, e.g. location.country_code. |
| `buckets` | `integer` | The maximum number of values to be returned in the report. Maximum: 500. Default: 50 |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result_path` | `string` | Path of result file |

### Search

Search items from Censys API

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `query` | `string` | Query to execute |
| `last_run` | `string` | Date of the last run |
| `index` | `string` | Name of the index to search |
| `fields` | `array` | Fields to return |
| `max_requests` | `integer` | Maximum number of requests to send to the API. Useful to avoid spending too much credits on the same query. 0 is no limit. Defaults to 1 |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result_path` | `string` | Path of results file |

### View Item

Return the item as a structured data

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `index` | `string` | Name of the index to use |
| `item` | `string` | Item to retrieve |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result_path` | `string` | Path of result file |


## Extra

Module **`Censys` v1.25.0**