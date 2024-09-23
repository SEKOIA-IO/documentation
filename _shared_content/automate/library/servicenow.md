# ServiceNow

![ServiceNow](/assets/playbooks/library/servicenow.png){ align=right width=150 }

[ServiceNow](https://www.servicenow.com/) is an IT company allowing creating workflow to empower employees productivity and to improve customers experience

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | ServiceNox base url |
| `username` | `string` | Username |
| `password` | `string` | Password |

## Actions

### Get Table

Retrieve Service Now table

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `table_name` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `array` |  |


## Extra

Module **`ServiceNow` v1.25.0**