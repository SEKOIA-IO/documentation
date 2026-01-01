uuid: 2b2f877e-6eaa-4d6c-a18e-f3383e52a429
name: ServiceNow
type: playbook

# ServiceNow

![ServiceNow](/assets/playbooks/library/servicenow.png){ align=right width=150 }

ServiceNow is an IT company allowing creating workflow to empower employees productivity and to improve customers experience

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