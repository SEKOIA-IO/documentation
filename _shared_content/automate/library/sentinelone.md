# SentinelOne

![SentinelOne](/assets/playbooks/library/sentinelone.png){ align=right width=150 }

This module interacts with the SentinelOne

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `hostname` | `string` | The domain-name to the SentinelOne instance |
| `api_token` | `string` | The API token to authenticate to SentinelOne |

## Triggers

### [DEPRECATED] Consume events from SentinelOne DeepVisibility

Consume events from SentinelOne DeepVisibility’s Kafka brokers

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `bootstrap_servers` | `string` | Kafka bootstrap servers (e.g. 'dv-exporter-kafka-eu-central-1-prod.sentinelone.net:9093') |
| `username` | `string` | Kafka username |
| `password` | `string` | Kafka password |
| `group_id` | `string` | Kafka consumer group |
| `topic` | `string` | Kafka topic |


### Collect SentinelOne alerts

Collect activities and threats from SentinelOne

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |

## Actions

### [BETA] Create IOCs

Push IOCs in the Threat Intelligence API of SentinelOne

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sekoia_base_url` | `string` | Sekoia base URL |
| `stix_objects_path` | `string` | Filepath of the STIX objects fetched from the collection |
| `filters` | `object` | Filter where to add iocs  |

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
| `filters` | `object` | Filters to select the threats to update |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `affected` | `integer` | The number of threats incidents updated |


## Extra

Module **`SentinelOne` v1.18.5**