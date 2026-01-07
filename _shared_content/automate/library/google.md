uuid: 4f682a9e-9a25-43a5-8a48-cd9bd7fade7e
name: Google
type: playbook

# Google

![Google](/assets/playbooks/library/google.svg){ align=right width=150 }

Google module

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `credentials` | `object` | Credentials to use. You can find them in the credentials file |

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

Module **`Google` v1.21.3**