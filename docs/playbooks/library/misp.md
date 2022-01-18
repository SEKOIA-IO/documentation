# misp


![misp](../../assets/playbooks/library/misp.png)


MISP Module

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| misp_url | string | MISP server url |
| misp_api_key | string | MISP API key |





## Triggers

### New Event

Trigger playbook run on MISP event



#### Arguments
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| sleep_time | integer | Time in seconds the worker sleeps between the checks of new events |
| attributes_filter | integer | Time in seconds after which attributes are no longer considered new (0 for no filter) |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| event | object | MISP event |













## Actions

### MISP to STIX

Convert MISP event to STIX 2



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| event | object | MISP event to convert to STIX |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| bundle | object | Converted STIX Bundle |







### Publish Event

Publish MISP event



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| event | object | MISP event |
| event_path | string | MISP event (from file) |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| event | object | Published MISP event |
| event_path | string | Published MISP event (to file) |












## Extra

Module **misp v.1.27**
