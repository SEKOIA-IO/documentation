uuid: ce491d8d-87a8-45af-a7c5-ede98c4a4ba3
name: MicrosoftDefenderXDR
type: playbook

# MicrosoftDefenderXDR

![MicrosoftDefenderXDR](/assets/playbooks/library/microsoftdefenderxdr.png){ align=right width=150 }

 Microsoft Defender for Endpoint is an Endpoint Detection and Response (EDR) product that monitors the security of endpoints. The module required, at least, the Microsoft Defender for Endpoint plan 1

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

## Set up

## Configuration

### Collect events

#### Create an Azure application

1. On the Azure Portal, in the search bar, go to `App registrations`
2. Click `+ New registration`
3. Type a name
4. Select `Accounts in this organizational directory only` option as account type
5. Click `Register`
6. From the `Overview` page, copy `Application (client) ID` and `Directory (tenant) ID`


#### Create a client secret

1. Go to `Manage` > `Certificates & secrets`
2. Click `+ New client secret`
3. Type a description and select the desirated expiration period
4. Click `Add`
5. Copy the `Value` of the client secret

#### Add permissions

1. Go to `Manage` > `API permissions`
2. Click `Add a permissions`
3. On the right panel, Select `APIs my organization uses` tab
4. Click `Office 365 Management APIs`
5. Click `Application permissions`
6. Select `ActivityFeed.Read`
7. Click `Add permissions`
8. In the `API permissions` page, click `Grant admin consent for TENANT_NAME`
9. Click `Yes` in the `Grant admin consent confirmation` modal

#### Install Agent

1. On security.microsoft.com, go to `System > Parameters`
2. Click `Endpoints` 
3. Go to `Device Management > Onboarding`
4. Download the Integration package

[Read More](https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-script)

#### Create an application with the permission

1. In Microsoft EntraID, create a new application under `App registrations`.
2. For the permissions, go to `API permission`
3. Click `+ Add a permission`. Select `APIs my organization uses` and type `WindowsDefenderATP`. 
4. Select `WindowsDefenderATP`.
5. In the permissions, select:
   - Machine.Isolate
   - Machine.Offboard
   - Machine.Read.All
   - Machine.RestrictExecution
   - Machine.Scan
   - Machine.StopAndQuarantine
   - Ti.Read.All
   - Ti.ReadWrite
   - Ti.ReadWrite.All
   - Alert.ReadWrite.All
6. After permissions selection, grant the admin consent.
                          
[Read More](https://learn.microsoft.com/en-us/defender-endpoint/api/exposed-apis-create-app-webapp)

## Extra

Module **`MicrosoftDefenderXDR` v1.0.0**