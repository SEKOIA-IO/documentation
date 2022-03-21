# harfanglab


![harfanglab](../../assets/playbooks/library/harfanglab.png)


HarfangLab is an Endpoint detection and response (EDR) solution certified by ANSSI since 2020

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| url | string | URL of the HarfangLab instance |
| api_token | string | Authentication token for the API |








## Actions

### List processes

Get the list of processes on the systems



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target_agents | string | Targeted agents identifier |
| target_groups | string | Targeted groups identifier |
| get_connections_list | boolean | Get list of connections (listening and connected sockets) |
| get_handles_list | boolean | Get list of open handles |
| get_signatures_list | boolean | Get signature info of processes and DLLs |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| id | str | Identifier of the job |
| action | str | Name of job action |
| creationtime | string | Creation date of the job |
| parameters | object | Parameters of the job |







### List named pipes

Get the list of named pipe on the systems



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target_agents | string | Targeted agents identifier |
| target_groups | string | Targeted groups identifier |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| id | str | Identifier of the job |
| action | str | Name of job action |
| creationtime | string | Creation date of the job |
| parameters | object | Parameters of the job |












## Extra

Module **harfanglab v.1.9**
