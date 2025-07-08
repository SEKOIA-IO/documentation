uuid: 2bb1aaf9-a90c-411d-8e5f-c72b1b46b3d7
name: Palo Alto Cortex XDR (EDR)
type: playbook

# Palo Alto Cortex XDR (EDR)

![Palo Alto Cortex XDR (EDR)](/assets/playbooks/library/palo-alto-cortex-xdr-edr.png){ align=right width=150 }

Cortex XDR is the detection and response app that natively integrates network, endpoint and cloud data to stop sophisticated attacks.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_key` | `string` | The API Key is your unique identifier used as the authorization header |
| `api_key_id` | `string` | The API Key ID is your unique token used to authenticate the API Key |
| `fqdn` | `string` | The FQDN is a unique host and domain name associated with each tenant |

## Actions

### Block malicious files



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `stix_objects_path` | `string` | Filepath of the STIX objects fetched from the collection |
| `comment` | `string` | Comment to add to entity. |
| `incident_id` | `integer` | Incident ID. |

### Comment alerts



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_id_list` | `array` | List of alert IDs to update. |
| `comment` | `string` | Comment to add to the alert. |

### Isolate endpoint



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `endpoint_id` | `string` | Endpoint ID. |
| `incident_id` | `string` | Incident ID. |

### Quarantine the file



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | Path to the file to be quarantined. |
| `file_hash` | `string` | Hash of the file to be quarantined. |
| `endpoint_ids` | `array` | List of endpoint IDs to filter by. |

### Unisolate endpoint



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `endpoint_id` | `string` | Endpoint ID. |
| `incident_id` | `string` | Incident ID. |

### Update alert status and severity



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_id_list` | `array` | List of alert IDs to update. |
| `status` | `string` | New status for the alert. |
| `severity` | `string` | New severity for the alert. |

### XQL query



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `query` | `string` | XQL query to run. |
| `tenants` | `array` | List of tenant IDs. |
| `timeframe_from` | `integer` | Start time as UNIX timestamp. |
| `timeframe_to` | `integer` | End time as UNIX timestamp. |
| `max_wait_time` | `integer` | Maximum wait time in seconds to finish the query. If limit is reached, the action will fail. |


## Extra

Module **`Palo Alto Cortex XDR (EDR)` v1.3.6**