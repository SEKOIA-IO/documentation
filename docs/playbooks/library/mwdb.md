# mwdb



MWDB Module

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| api_key | string | API key |





## Triggers

### New Config

Get MWDB configs





#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| id | string | Configuration ID |
| config_type | string | Configuration Type (static or dynamic) |
| upload_time | string | Configuration Upload Time (in ISO format) |
| type | string | Configuration Type |
| family | string | Malware Family |
| tags | array | Tags associated with this configuration |
| children | array | Configuration Children Objects |
| parents | array | Configuration Parent Objects |
| cfg | object | Configuration Content |
| files | array | Malware samples associated with this configuration |













## Actions

### Config To Observables

Convert a MWDB config to a bundle of observables



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| config_path | string | File path to the JSON config to read. |
| config | object | The JSON content of the config. |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| observables | array | Bundle with the list of observables |
| observables_path | string | Path of the file holding the bundle with the observables |












## Extra

Module **mwdb v.1.25**
