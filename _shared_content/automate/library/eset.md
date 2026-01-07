uuid: 91140c5a-770f-44c6-81ce-ea57daf3fe34
name: Eset
type: playbook

# Eset

![Eset](/assets/playbooks/library/eset.png){ align=right width=150 }

ESET is a global cybersecurity company known for its antivirus and security software solutions for both businesses and consumers, providing advanced threat detection and malware protection.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `region` | `string` | Region |
| `username` | `string` | Username |
| `password` | `string` | Password |

## Actions

### Deisolate endpoints

Deisolate a list of endpoints

**Configuration**

{'description': 'The reason of the deisolation', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `device_uuids` | `array` | The identifiers of the endpoints to deisolate |
| `display_name` | `string` | A name for the action |
| `description` | `string` | The reason of the deisolation |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status_code` | `integer` | HTTP status code |
| `body` | `object` | API Response |

### Isolate endpoints

Isolate a list of endpoints

**Configuration**

{'description': 'The reason of the isolation', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `device_uuids` | `array` | The identifiers of the endpoints to isolate |
| `display_name` | `string` | A name for the action |
| `description` | `string` | The reason of the isolation |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status_code` | `integer` | HTTP status code |
| `body` | `object` | API Response |

### Init a scan

Initialize a scan on a list of endpoints

**Configuration**

{'description': 'The reason of the scan', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `device_uuids` | `array` | The identifiers of the endpoints to scan |
| `scan_profile` | `string` | The profile of the scan |
| `display_name` | `string` | A name for the action |
| `description` | `string` | The reason of the scan |
| `cleaning_enabled` | `boolean` | Enable the cleaning |
| `shutdown_enabled` | `boolean` | Shutdown the endpoints after the scan |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status_code` | `integer` | HTTP status code |
| `body` | `object` | API Response |

## Set up

## Configuration

1. Log in to the ESET Protect Hub console as administrator
2. On the left panel, go to `USERS`

    ![Step 1](/assets/playbooks/library/setup/eset/Step01.png){: style="max-width:100%"}

3. Click `ADD USER`

    ![Step 2](/assets/playbooks/library/setup/eset/Step02.png){: style="max-width:100%"}

4. Type the email of the user and click `NEXT`

    ![Step 3](/assets/playbooks/library/setup/eset/Step03.png){: style="max-width:100%"}

5. Select `Read access` for the `My company` permission
6. Select `Access` for the `ESET PROTECT` permission 
7. Check `Integrations`
8. Click `NEXT`

    ![Step 4](/assets/playbooks/library/setup/eset/Step04.png){: style="max-width:100%"}

9. Click `CREATE`


## Extra

Module **`Eset` v1.0.1**