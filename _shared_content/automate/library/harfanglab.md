uuid: 8380240b-61a4-48b7-93e4-044a7ee2309b
name: HarfangLab
type: playbook

# HarfangLab

![HarfangLab](/assets/playbooks/library/harfanglab.png){ align=right width=150 }

HarfangLab is an Endpoint detection and response (EDR) solution certified by ANSSI since 2020

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `url` | `string` | URL of the HarfangLab instance |
| `api_token` | `string` | Authentication token for the API |

## Actions

### Add comment to Threat

Add comment to Threat

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | Threat IDs |
| `comment` | `string` | Comment to add |

### Create IOCs

Create IOCs

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `stix_objects_path` | `string` | Filepath of the STIX objects fetched from the collection |
| `sekoia_base_url` | `string` | [Optional] Sekoia base url, used to generate direct links to IOCs |
| `source_id` | `string` | Source ID |
| `block_on_agent` | `boolean` | Block on agent |
| `quarantine_on_agent` | `boolean` | Quarantine on agent |
| `detect_on_agent` | `boolean` | Endpoint detection |

### Download File from Endpoint

Download an arbitrary file from an HarfangLab endpoint

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | Identifier of the endpoint agent |
| `path` | `string` | Absolute path to the file to download from the endpoint |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `path` | `string` | Downloaded file's path |

### Deisolate an agent

Deisolate an agent

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the agent to deisolate |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `requested` | `array` | The list of identifiers of non-deisolated endpoints |
| `unrequested` | `array` | The list of identifiers of deisolated endpoints |

### Isolate an agent

Isolate an agent

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the agent to isolate |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `requested` | `array` | The list of identifiers of isolated endpoints |
| `unrequested` | `array` | The list of identifiers of non-isolated endpoints |

### Deisolate a group

Deisolate a group of endpoints

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the group to deisolate |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `requested` | `array` | The list of identifiers of non-deisolated endpoints |
| `unrequested` | `array` | The list of identifiers of deisolated endpoints |

### Isolate a group

Isolate a group of endpoints

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the group to isolate |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `requested` | `array` | The list of identifiers of isolated endpoints |
| `unrequested` | `array` | The list of identifiers of non-isolated endpoints |

### Hostname by IP

Get the hostname of a machine by its IP address

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target_ip` | `string` | Targeted IP address |
| `get_only_last_seen` | `boolean` | Get the last seen hostname only |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `hostnames` | `array` | Hostnames |

### List named pipes

Get the list of named pipe on the systems

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target_agents` | `string` | Targeted agents identifier |
| `target_groups` | `string` | Targeted groups identifier |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | Identifier of the job |
| `action` | `string` | Name of job action |
| `creationtime` | `string` | Creation date of the job |
| `parameters` | `object` | Parameters of the job |

### List processes

Get the list of processes on the systems

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target_agents` | `string` | Targeted agents identifier |
| `target_groups` | `string` | Targeted groups identifier |
| `get_connections_list` | `boolean` | Get list of connections (listening and connected sockets) |
| `get_handles_list` | `boolean` | Get list of open handles |
| `get_signatures_list` | `boolean` | Get signature info of processes and DLLs |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | Identifier of the job |
| `action` | `string` | Name of job action |
| `creationtime` | `string` | Creation date of the job |
| `parameters` | `object` | Parameters of the job |

### Update Threat status

Update Threat status

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `threat_ids` | `array` | Threats IDs |
| `new_status` | `string` | New status |
| `update_by_query` | `boolean` | Update by query |


## Extra

Module **`HarfangLab` v1.24.0**