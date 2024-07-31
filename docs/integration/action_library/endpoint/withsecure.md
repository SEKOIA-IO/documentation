# WithSecure

![WithSecure](/assets/playbooks/library/withsecure.png){ align=right width=150 }

Interact with WithSecure Elements

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `client_id` | `string` | Client identifier |
| `secret` | `string` | API secret to authenticate |

## Triggers

### Fetch security events

Get last security events

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |

## Actions

### Add comment on Incident

Add comment on Incident.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target` | `string` | Incident identifier to comment. |
| `comment` | `string` | Comment. |

### Isolate Device From Network

Isolate a device from network connections.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target` | `string` | Device identifier of the computer to isolate. |
| `message` | `string` | Optional message that is displayed on isolated device. |

### List Detections For Incident

List Detections For Incident.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target` | `string` | Incident identifier to list detections. |

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

### Scan Device For Malware

Scan Device For Malware.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target` | `string` | Device identifier to scan for malware. |

### Update status on Incident

Update status on Incident.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `target` | `string` | Incident identifier to comment. |
| `status` | `string` | Status. |
| `resolution` | `string` | Resolution. |


## Extra

Module **`WithSecure` v2.14.0**