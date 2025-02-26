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
| `verify_certificate` | `boolean` | Is the server certificate verified |


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
| `verify_certificate` | `boolean` | Is the server certificate verified |


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
| `verify_certificate` | `boolean` | Is the server certificate verified |


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
| `verify_certificate` | `boolean` | Is the server certificate verified |


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
| `verify_certificate` | `boolean` | Is the server certificate verified |


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
| `verify_certificate` | `boolean` | Is the server certificate verified |


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

## Set up

## Configuration

1. Log in to the StormShield Console as administrator
2. On the left panel, go to `System`

     ![Step 1](/assets/playbooks/library/setup/stormshield/Step01.png){: style="max-width:100%"}

3. Click the `API KEYS` tab

     ![Step 2](/assets/playbooks/library/setup/stormshield/Step02.png){: style="max-width:100%"}

4. Click the `EDIT` button

     ![Step 3](/assets/playbooks/library/setup/stormshield/Step03.png){: style="max-width:100%"}

5. Turn on the `Enable public API` toggle and Click `Add an API Key`

     ![Step 4](/assets/playbooks/library/setup/stormshield/Step04.png){: style="max-width:100%"}

6. Enter a description for the API Key and an expiration time
7. Turn on the `Agent Monitoring` and `Remediation` options
8. Click `Ok`

     ![Step 5](/assets/playbooks/library/setup/stormshield/Step05.png){: style="max-width:100%"}

9. Copy the API Key identifier and click `Close`

     ![Step 6](/assets/playbooks/library/setup/stormshield/Step06.png){: style="max-width:100%"}

10. Click `Save`

     ![Step 7](/assets/playbooks/library/setup/stormshield/Step07.png){: style="max-width:100%"}


## Extra

Module **`Stormshield` v1.0.1**