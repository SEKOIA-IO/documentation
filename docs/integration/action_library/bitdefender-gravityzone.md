uuid: 26277889-b91b-46d0-8bac-7f6b2f6fb9a3
name: Bitdefender GravityZone
type: playbook

# Bitdefender GravityZone

![Bitdefender GravityZone](/assets/playbooks/library/bitdefender-gravityzone.png){ align=right width=150 }

Bitdefender is a global cybersecurity company renowned for its advanced antivirus software, providing comprehensive security solutions and threat intelligence for individuals and enterprises, safeguarding against evolving cyber threats.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `url` | `string` | The URL of the Bitdefender GravityZone API endpoint. |
| `api_key` | `string` | The API key for authenticating with the Bitdefender GravityZone API. |

## Actions

### Create a new custom task scan

Create a new custom task scan

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `targetIds` | `array` | A list with the IDs of the targets to scan. The target ID can designate an endpoint or a container. |
| `type` | `integer` | The type of scan. |
| `customScanSettings` | `object` | Object containing information such as scan depth and scan path(s). This object should be set only when type parameter has the value 4 (Custom Scan). |
| `returnAllTaskIds` | `boolean` | If set to true, the method will return all task IDs created by the scan. If set to false, it will return only the first task ID. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `array` | This method returns the ID of the newly created task or a boolean value which is true if the creation of the task was successful. |

### Deisolate an endpoint

Deisolate an endpoint

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `endpointId` | `string` | The ID of the endpoint to be deisolated. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `boolean` | This method returns a Boolean which is True if the operation was successful. |

### Get blocked items

Get blocked items from BitDefender GravityZone

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `page` | `integer` | The current page. |
| `perPage` | `integer` | The number of items to return per page. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `object` |  |

### Isolate an endpoint

Isolate an endpoint

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `endpointId` | `string` | The ID of the endpoint to be isolated. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `boolean` | This method returns a Boolean which is True if the operation was successful. |

### Kill a process

Kill a process

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `processId` | `integer` | The ID of the process to kill. |
| `path` | `string` | The location of the file that starts the process on the endpoint where it is stored. |
| `endpointId` | `string` | The endpoint (or node) where the process is running |
| `incidentId` | `string` | [Optional] The ID of the incident generated as a result of this process. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `string` | If the task was successful, contains the ID for the task created as a result of the request. |

### Block connections

Push connection blocks from BitDefender GravityZone

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `type` | `string` | The type of block to be push. |
| `rules` | `array` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `boolean` | This method returns a Boolean which is True if the operation was successful. |

### Block hashes

Push hash blocks from BitDefender GravityZone

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `type` | `string` | The type of block to be push. |
| `rules` | `array` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `boolean` | This method returns a Boolean which is True if the operation was successful. |

### Block Paths

Push path blocks from BitDefender GravityZone

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `type` | `string` | The type of block to be push. |
| `rules` | `array` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `boolean` | This method returns a Boolean which is True if the operation was successful. |

### Remove blocks

Remove blocks from BitDefender GravityZone

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ids` | `array` | List of block IDs to be removed. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `boolean` | This method returns a Boolean which is True if the operation was successful. |

### Create a new task scan

Create a new task scan

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `targetIds` | `array` | A list with the IDs of the targets to scan. The target ID can designate an endpoint or a container. |
| `type` | `integer` | The type of scan. |
| `returnAllTaskIds` | `boolean` | If set to true, the method will return all task IDs created by the scan. If set to false, it will return only the first task ID. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `array` | This method returns the ID of the newly created task or a boolean value which is true if the creation of the task was successful. |

### Update an incident comment

Update an incident comment

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `type` | `string` | The type of the target incident. Must be 'extendedIncidents' or 'incidents'. |
| `incidentId` | `string` | The ID of the incident to update. |
| `note` | `string` | The comment to be added to the incident. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `boolean` | This method returns a Boolean which is True if the operation was successful. |

### Update the status of an incident

Update the status of an incident

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `type` | `string` | The type of the target incident. Must be 'extendedIncidents' or 'incidents'. |
| `incidentId` | `string` | The ID of the incident to update. |
| `status` | `integer` | The status to be assigned to the incident. Possible values are: 1 - Open, 2 - Investigating, 3 - Closed, 4 - False positive. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `result` | `boolean` | This method returns a Boolean which is True if the operation was successful. |

## Set up

## Configuration

1. Log in to the Bitdefender GravityZone Control Center as an administrator.
2. In the top right, navigate to `User menu` > `My account`.

    ![Step 1](/assets/playbooks/library/setup/bitdefender-gravityzone/Step01.png)


3. Go down and click the `Add` button to create a new API key.

    ![Step 1](/assets/playbooks/library/setup/bitdefender-gravityzone/Step02.png)


4. Enter a description for the API key to identify its purpose.
5. Select the following permissions and scopes for the API key.

    ![Step 1](/assets/playbooks/library/setup/bitdefender-gravityzone/Step03.png)

7. Click `Save` to generate the API key.
8. Copy the generated API key and store it securely. You will not be able to view it again.

> `Note:` Keep your API key confidential and restrict its usage to trusted applications only.

## Extra

Module **`Bitdefender GravityZone` v1.0.6**