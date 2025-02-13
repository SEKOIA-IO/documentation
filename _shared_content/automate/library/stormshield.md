uuid: 758103e9-eb62-4b0d-8c71-0ff9c60ca677
name: Stormshield
type: playbook

# Stormshield

![Stormshield](/assets/playbooks/library/stormshield.png){ align=right width=150 }

Stormshield Network Security is a range of network security appliances.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `url` | `string` | URL of the Stormshield instance |
| `api_token` | `string` | Authentication token for the API |

## Actions

### Deisolate agent

Deisolate an agent

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | Name or identifier of the agent |
| `comment` | `string` | Comment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `taskId` | `string` | Task ID |
| `status` | `string` | Task status |
| `requestTime` | `string` | Task request time |
| `startTime` | `string` | Task start time |
| `endTime` | `string` | Task end time |
| `errorCode` | `integer` | Error code |
| `errorMessage` | `string` | Error message |

### Isolate agent

Isolate an agent

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | Name or identifier of the agent |
| `forceServerIsolation` | `boolean` | Boolean to force the isolation |
| `comment` | `string` | Comment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `taskId` | `string` | Task ID |
| `status` | `string` | Task status |
| `requestTime` | `string` | Task request time |
| `startTime` | `string` | Task start time |
| `endTime` | `string` | Task end time |
| `errorCode` | `integer` | Error code |
| `errorMessage` | `string` | Error message |

### Quarantine file

Quarantine a file

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | Name or identifier of the agent |
| `filePath` | `string` | Path to the file to quarantine |
| `bypassExcludedDirectories` | `boolean` | Boolean to bypass excluded directories |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `taskId` | `string` | Task ID |
| `status` | `string` | Task status |
| `requestTime` | `string` | Task request time |
| `startTime` | `string` | Task start time |
| `endTime` | `string` | Task end time |
| `errorCode` | `integer` | Error code |
| `errorMessage` | `string` | Error message |

### Restore quarantine file

Restore stormshield quarantined file

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | Name or identifier of the agent |
| `fileHashSha256` | `string` | File hash sha256 |
| `overwriteExistingFile` | `boolean` | Boolean to overwrite any existing file |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `taskId` | `string` | Task ID |
| `status` | `string` | Task status |
| `requestTime` | `string` | Task request time |
| `startTime` | `string` | Task start time |
| `endTime` | `string` | Task end time |
| `errorCode` | `integer` | Error code |
| `errorMessage` | `string` | Error message |

### Terminate Stormshield process

Terminate a Stormshield process

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | Name or identifier of the agent |
| `processPath` | `string` | Executable path of the process to kill on the computer |
| `terminateProcessTree` | `boolean` | Boolean to terminate the process tree |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `taskId` | `string` | Task ID |
| `status` | `string` | Task status |
| `requestTime` | `string` | Task request time |
| `startTime` | `string` | Task start time |
| `endTime` | `string` | Task end time |
| `errorCode` | `integer` | Error code |
| `errorMessage` | `string` | Error message |

### Wait for a Stormshield task to complete

Wait until the status of the task is Succeeded or Failed

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `task_id` | `string` | Task ID |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `taskId` | `string` | Task ID |
| `status` | `string` | Task status |
| `requestTime` | `string` | Task request time |
| `startTime` | `string` | Task start time |
| `endTime` | `string` | Task end time |
| `errorCode` | `integer` | Error code |
| `errorMessage` | `string` | Error message |


## Extra

Module **`Stormshield` v1.0.0**