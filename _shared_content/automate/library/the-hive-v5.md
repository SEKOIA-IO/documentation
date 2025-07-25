uuid: d6c96586-707c-451f-b9f6-d31b3291f87d
name: The Hive V5
type: playbook

# The Hive V5

![The Hive V5](/assets/playbooks/library/the-hive-v5.png){ align=right width=150 }

TheHive is a scalable, open source and free Security Incident Response Platform

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Your TheHive instance URL |
| `apikey` | `string` | An API key |
| `organisation` | `string` | The user organisation |

## Actions

### Create an alert in The Hive v5



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert` | `object` | A Sekoia.io alert |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `_id` | `string` |  |
| `_type` | `string` |  |
| `_createdBy` | `string` |  |
| `_createdAt` | `integer` |  |
| `type` | `string` |  |
| `source` | `string` |  |
| `sourceRef` | `string` |  |
| `title` | `string` |  |
| `description` | `string` |  |
| `severity` | `integer` |  |
| `date` | `integer` |  |
| `tags` | `array` |  |
| `tlp` | `integer` |  |
| `pap` | `integer` |  |
| `status` | `string` |  |
| `follow` | `boolean` |  |
| `customFields` | `object` |  |
| `observableCount` | `integer` |  |
| `stage` | `string` |  |
| `extraData` | `object` |  |
| `newDate` | `integer` |  |
| `timeToDetect` | `integer` |  |


## Extra

Module **`The Hive V5` v1.0.0**