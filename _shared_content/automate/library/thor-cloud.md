uuid: 300b9a0b-30ba-4b4a-b0b0-f16cc6091377
name: THOR Cloud
type: playbook

# THOR Cloud

![THOR Cloud](/assets/playbooks/library/thor-cloud.png){ align=right width=150 }

Nextron THOR Cloud and THOR Cloud Lite endpoint scanner - comprehensive malware detection logs with file scanning, rootkit detection, and signature-based alerting.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_key` | `string` | API key for THOR Cloud or THOR Cloud Lite |

## Actions

### Generate THOR Cloud launcher

Link an existing or create a new THOR Cloud campaign, then generate a launcher URL and an OS-specific download-and-run command. The returned URL and command contain a sensitive campaign token and must not be logged or shared.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `campaign_id` | `string` | UUID of an active THOR Cloud campaign to use. Fill in either Campaign ID or Campaign name. |
| `campaign_name` | `string` | Name of a new campaign to create. Fill in either Campaign ID or Campaign name. |
| `launcher_type` | `string` | Launcher matching the target asset operating system |
| `product` | `string` | THOR Cloud or THOR Cloud Lite, matching the API key of the account |
| `campaign_description` | `string` | Optional description of the new campaign. Only used when creating a new campaign. |
| `assigned_contract` | `string` | Optional contract identifier used to license scans. Only used when creating a new campaign. |
| `end_date` | `string` | Optional campaign expiration in RFC 3339 format, including timezone. Only used when creating a new campaign. |
| `scan_profile` | `string` | Optional predefined profile name exactly as shown in THOR Cloud; it is resolved through the account scan profiles API. Only used when creating a new campaign. |
| `scan_limit` | `integer` | Optional maximum number of scans; zero means unlimited. Only used when creating a new campaign. |
| `scan_threads` | `integer` | Optional number of scanner threads. Only used when creating a new campaign. |

**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `campaign_id` | `string` | UUID of the THOR Cloud campaign |
| `campaign_name` | `['string', 'null']` | Name of the linked or newly created campaign |
| `campaign_created` | `boolean` | Whether this action created the campaign |
| `launcher_type` | `string` | Generated launcher type |
| `launcher_url` | `string` | Sensitive tokenized URL from which the target can download the launcher |
| `filename` | `string` | Suggested launcher filename |
| `command` | `string` | Sensitive OS-specific command that downloads and runs the launcher |


## Extra

Module **`THOR Cloud` v1.0.2**
