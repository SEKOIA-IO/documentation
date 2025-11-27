uuid: 6f3d8a54-d51c-47d0-b77c-dbcf31393d59
name: TrendMicro VisionOne
type: playbook

# TrendMicro VisionOne

![TrendMicro VisionOne](/assets/playbooks/library/trendmicro-visionone.png){ align=right width=150 }

Trend Micro Vision One is a comprehensive XDR platform that integrates data from various sources, such as: email, company intranet, workstations and servers, containerized environments, cloud environments, integrated solutions from the Trend Micro ecosystem, and third-party integrations (EntraID, Okta, Office365, etc.) to detect, analyze, and respond to threats.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Base URL |
| `api_key` | `string` | Trend Micro api_key |

## Actions

### Add alert note

Add a note to a workbench alert

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_id` | `string` | The identifier of the alert |
| `note` | `string` | The content of the note |

### Collect a file

Collect a file from a list of endpoints and send it to TrendMicro VisionOne

**Configuration**

{'description': 'The reason of the action', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `agent_guids` | `array` | The identifiers of the endpoints |
| `description` | `string` | The reason of the action |
| `file_path` | `string` | The filepath of the file to collect |

### Deisolate endpoints

Restores the network connectivity of the endpoints

**Configuration**

{'description': 'The reason of the action', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `agent_guids` | `array` | The identifiers of the endpoints to deisolate |
| `description` | `string` | The reason of the action |

### Isolate endpoints

Isolate a list of endpoints from the network

**Configuration**

{'description': 'The reason of the action', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `agent_guids` | `array` | The identifiers of the endpoints to isolate |
| `description` | `string` | The reason of the action |

### Init a scan

Initialize a scan on the endpoints

**Configuration**

{'description': 'The reason of the action', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `agent_guids` | `array` | The identifiers of the endpoints to scan |
| `description` | `string` | The reason of the action |

### Terminate a process

Terminate a process that is running on a list of endpoints

**Configuration**

{'description': 'The reason of the action', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `agent_guid` | `string` | The identifiers of the endpoints to isolate |
| `process_id` | `integer` | Process ID to terminate |
| `description` | `string` | The reason of the action |
| `file_sha1` | `string` | The SHA-1 hash of the executable file of the process to terminate |
| `file_name` | `string` | The Filename of the response task target |

### Update alert status

Update the status of an alert

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_id` | `string` | The identifier of the alert to update |
| `status` | `string` | The new status of the alert |
| `investigation_result` | `string` | The result of the investigation |


## Extra

Module **`TrendMicro VisionOne` v0.1.3**