uuid: ce491d8d-87a8-45af-a7c5-ede98c4a4ba3
name: MicrosoftDefender
type: playbook

# MicrosoftDefender

![MicrosoftDefender](/assets/playbooks/library/microsoftdefender.png){ align=right width=150 }

 [Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/) is an Endpoint Detection and Response (EDR) product that monitors the security of endpoints. The module required, at least, the Microsoft Defender for Endpoint plan 1

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Base URL |
| `app_id` | `string` | The identifier of the Azure Application |
| `app_secret` | `string` | The value of the secret associated to the Azure Application |
| `tenant_id` | `string` | The identifier of the Azure Directory |

## Actions

### Comment an alert

Comment an alert

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_id` | `string` | Alert ID |
| `comment` | `string` | Comment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the alert |

### Cancel machine action

Cancel machine action

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `action_id` | `string` | Action ID |
| `comment` | `string` | Comment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the action |
| `type` | `string` | The type of the action |
| `status` | `string` | The status of the action |
| `requestor` | `string` | Identify who executed the action |
| `title` | `string` | The title of the action |
| `machineid` | `string` | The identifier of the machine |

### Get action info

Retrieve the status of an action of the machine

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `action_id` | `string` | Action ID |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the action |
| `type` | `string` | The type of the action |
| `status` | `string` | The status of the action |
| `requestor` | `string` | Identify who executed the action |
| `title` | `string` | The title of the action |
| `machineid` | `string` | The identifier of the machine |

### Isolate a machine

Isolate a machine

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `machine_id` | `string` | Machine ID |
| `comment` | `string` | Comment |
| `isolation_type` | `string` | Isolation Type |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the action |
| `type` | `string` | The type of the action |
| `scope` | `string` | The scope of the action |
| `status` | `string` | The status of the action |
| `requestor` | `string` | Identify who executed the action |
| `title` | `string` | The title of the action |
| `machineid` | `string` | The identifier of the machine |

### Push IOCs

Push IOCs in the TI API of Microsoft Defender

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `stix_objects_path` | `string` | Filepath of the STIX objects fetched from the collection |
| `sekoia_base_url` | `string` | [Optional] Sekoia base url, used to generate direct links to IOCs |
| `action` | `string` | Action to apply |
| `severity` | `string` | Severity |
| `generate_alert` | `boolean` | Generate Alert? |

### Restrict code execution

Restrict the execution of code on a machine

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `machine_id` | `string` | Machine ID |
| `comment` | `string` | Comment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the action |
| `type` | `string` | The type of the action |
| `status` | `string` | The status of the action |
| `requestor` | `string` | Identify who executed the action |
| `title` | `string` | The title of the action |
| `machineid` | `string` | The identifier of the machine |

### Scan a machine

Run an Anti-Virus scan on a machine

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `machine_id` | `string` | Machine ID |
| `comment` | `string` | Comment |
| `scan_type` | `string` | Scan Type |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the action |
| `type` | `string` | The type of the action |
| `scope` | `string` | The scope of the action |
| `status` | `string` | The status of the action |
| `requestor` | `string` | Identify who executed the action |
| `title` | `string` | The title of the action |
| `machineid` | `string` | The identifier of the machine |

### Deisolate a machine

Deisolate a machine

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `machine_id` | `string` | Machine ID |
| `comment` | `string` | Comment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the action |
| `type` | `string` | The type of the action |
| `status` | `string` | The status of the action |
| `requestor` | `string` | Identify who executed the action |
| `title` | `string` | The title of the action |
| `machineid` | `string` | The identifier of the machine |

### Unrestrict code execution

Remove the restriction of the code execution on a machine

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `machine_id` | `string` | Machine ID |
| `comment` | `string` | Comment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the action |
| `type` | `string` | The type of the action |
| `status` | `string` | The status of the action |
| `requestor` | `string` | Identify who executed the action |
| `title` | `string` | The title of the action |
| `machineid` | `string` | The identifier of the machine |

### Update an alert

Update an alert

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_id` | `string` | Alert ID |
| `status` | `string` | Status |
| `classification` | `string` | Classification of the alert |
| `determination` | `string` | Determination of the alert.<br/>The determination must match the classification (see https://learn.microsoft.com/en-us/defender-endpoint/api/update-alert) |
| `comment` | `string` | Comment |
| `owner` | `string` | Owner of the alert |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | The identifier of the alert |
| `title` | `string` | The title of the alert |
| `description` | `string` | The description of the alert |
| `status` | `string` | The status of the alert |
| `classification` | `string` | The classification of the alert |
| `determination` | `string` | The determination of the alert |
| `category` | `string` | The category of the alert |


## Extra

Module **`MicrosoftDefender` v1.0.0**