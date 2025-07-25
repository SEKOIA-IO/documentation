uuid: ff675e74-e5c1-47c8-a571-d207fc297464
name: SentinelOne
type: playbook

# SentinelOne

![SentinelOne](/assets/playbooks/library/sentinelone.png){ align=right width=150 }

SentinelOne is a cybersecurity company that provides autonomous endpoint protection through AI-powered threat detection and response. Its platform offers real-time prevention, detection, and remediation of cyber threats across networks.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `hostname` | `string` | The domain-name to the SentinelOne instance |
| `api_token` | `string` | The API token to authenticate to SentinelOne |

## Actions

### [BETA] Create IOCs

Push IOCs in the Threat Intelligence API of SentinelOne

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sekoia_base_url` | `string` | Sekoia base URL |
| `stix_objects_path` | `string` | Filepath of the STIX objects fetched from the collection |
| `filters` | `object` | Filter where to add iocs  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `indicators` | `array` | All indicators pushed |

### Create Threat Note

Create a threat note in SentinelOne

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `text` | `string` | Text to add to the note |
| `filters` | `object` | Filters to select the threats to which a note will be added |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `affected` | `integer` | The number of threats to which the note was added |

### Deisolate an endpoint

Connect the endpoint back to the network

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ids` | `array` | The list of Agent IDs to filter by |
| `account_ids` | `array` | The list of Account IDs to filter by |
| `group_ids` | `array` | The list of network group to filter by |
| `site_ids` | `array` | The list of Site IDs to filter by |
| `query` | `string` | Free-text search term to use |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `affected` | `integer` | The number of deisolated endpoints |

### Get malwares from threat

Fetch the malwares associated to a threat

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `threat_id` | `string` | The identifier of threat |
| `timeout` | `integer` | The maximum time, in seconds, the malwares should be retrieved (default: 300s) |
| `filters` | `object` | Filters to select the agents from which the malware will be transferred |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status` | `string` | The status of the run |
| `status_reason` | `string` | The reason of the status |
| `files` | `object` | The list of retrieved files |

### Init a scan

Run a Full Disk Scan on Agents that match the filter

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuids` | `array` | The list of Agent uuids to filter by |
| `account_ids` | `array` | The list of Account IDs to filter by |
| `group_ids` | `array` | The list of network group to filter by |
| `site_ids` | `array` | The list of Site IDs to filter by |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `affected` | `integer` | The number of scanned agents |

### Isolate an endpoint

Disconnect the endpoint from the network

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ids` | `array` | The list of Agent IDs to filter by |
| `account_ids` | `array` | The list of Account IDs to filter by |
| `group_ids` | `array` | The list of network group to filter by |
| `site_ids` | `array` | The list of Site IDs to filter by |
| `query` | `string` | Free-text search term to use |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `affected` | `integer` | The number of isolated endpoints |

### Query events in Deep Visibility

Create a query in Deep Visibility and get the events

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `group_ids` | `array` | The list of network group to filter by |
| `site_ids` | `array` | The list of Site IDs to filter by |
| `query` | `string` | Free-text search term to use |
| `from_date` | `string` | Get events created after this timestamp |
| `to_date` | `string` | Get events created before or at this timestamp |
| `timeout` | `integer` | The maximum time, in seconds, the query should be processed in (default 300s) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status` | `string` | The status of the query |
| `status_reason` | `string` | The reason of the status |
| `events` | `array` | The events got from the query |

### Execute a remote script

Execute a remote script and get the results

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `script_id` | `string` | The identifier of the script to identify |
| `output_destination` | `string` | The destination of the result |
| `task_description` | `string` | A short description of the task |
| `timeout` | `integer` | The maximum time, in seconds, the execution should be processed in (default: 300s) |
| `settings` | `object` | The settings to forward the remote script |
| `filters` | `object` | Filters to select the agents that will run the remote script |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status` | `string` | The status of the run |
| `status_reason` | `string` | The reason of the status |
| `result_file` | `object` | The url to download the result (for cloud destination) |

### Update Threat Incident

Update a threat incident in SentinelOne

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status` | `string` | Status applied to the incident |
| `new_analyst_verdict` | `string` | New verdict of the analyst to set |
| `filters` | `object` | Filters to select the threats to update |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `affected` | `integer` | The number of threats incidents updated |

## Set up

## Explanation of Additional Configuration

### Update Threat Incident [Filter attribut]

For the action `Update Threat Incident`, there are two arguments `status` and `filters`. `filters` argument is an object, so in this section, we will explain the components within this argument.

**Arguments**

| Name               | Type     | Description                        |
|--------------------|----------|------------------------------------|
| `agent_ids`        | `string` | List of Agent IDs to filter by     |
| `account_ids`      | `array`  | List of Account IDs to filter by   |
| `group_ids`        | `array`  | List of network group to filter by |
| `site_ids`         | `array`  | List of Site IDs to filter by      |
| `ids`              | `array`  | List of threat IDs                 |
| `analyst_verdicts` | `string` | Verdicts of the analyst            |


## Extra


Module **`SentinelOne` v1.20.9**