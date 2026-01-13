uuid: 8aa9f86c-f360-4ae7-84f5-b61c6917cf01
name: WithSecure
type: playbook

# WithSecure

![WithSecure](/assets/playbooks/library/withsecure.png){ align=right width=150 }

WithSecure, formerly known as F-Secure Business, provides cybersecurity solutions focusing on threat detection, incident response, and endpoint protection. It delivers comprehensive security services tailored to businesses to safeguard against evolving cyber threats.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `client_id` | `string` | Client identifier |
| `secret` | `string` | API secret to authenticate |

## Actions

### Add comment on Incident

Add comment on Incident.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target` | `string` | Incident identifier to comment. |
| `comment` | `string` | Comment. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `items` | `array` |  |

### Enumerate processes

Enumerate processes.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `organization_id` | `string` | UUID of an organization. |
| `target` | `string` | Device identifier on which action is created. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` |  |

### Isolate Device From Network

Isolate a device from network connections.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target` | `string` | Device identifier of the computer to isolate. |
| `message` | `string` | Optional message that is displayed on isolated device. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `multistatus` | `array` |  |
| `transactionId` | `string` |  |

### Kill process

Kill process.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `organization_id` | `string` | UUID of an organization. |
| `target` | `string` | Device identifier on which action is created. |
| `match` | `string` | Strategy used to match processes (processId,processName,processNameRegex,processPath,processPathRegex) |
| `process_match_values` | `array` | List of values that are used to match process to kill. Depending on selected strategy it might be list of identifiers, names or regular expressions. |
| `process_memory_dump` | `boolean` | Whether to run memory dump on process before killing it. |
| `memory_dump_flag` | `string` | full - memory dump includes all accessible memory of process, pmem - only information necessary to capture process' stack traces |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` |  |

### Kill thread

Kill thread.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `organization_id` | `string` | UUID of an organization. |
| `target` | `string` | Device identifier on which action is created. |
| `thread_id` | `integer` | Thread ID |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` |  |

### List Detections For Incident

List Detections For Incident.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target` | `string` | Incident identifier to list detections. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `detections` | `array` |  |

### List devices

Retrieves devices details.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `organization_id` | `string` | UUID of an organization. If organizationId is missing, default organization of authenticated client is used. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `devices` | `array` |  |

### Release Device From Network Isolation

Release a device from network isolation.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target` | `string` | Device identifier of the computer to release. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `multistatus` | `array` |  |
| `transactionId` | `string` |  |

### Scan Device For Malware

Scan Device For Malware.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target` | `string` | Device identifier to scan for malware. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `multistatus` | `array` |  |
| `transactionId` | `string` |  |

### Update status on Incident

Update status on Incident.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target` | `string` | Incident identifier to update. |
| `status` | `string` | Status. |
| `resolution` | `string` | Resolution. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `multistatus` | `string` |  |
| `transactionId` | `string` |  |


## Extra

Module **`WithSecure` v2.16.1**