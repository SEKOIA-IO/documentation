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
| `verify_certificate` | `boolean` | Is the server certificate verified |

## Actions

### Add a comment in The Hive v5

Action to add a comment in The Hive v5

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_id` | `string` | The id of the alert you want to add a comment to. For instance: ~12345 |
| `message` | `string` | A message to be added as an alert's comment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `_id` | `string` |  |
| `_type` | `string` |  |
| `createdBy` | `string` |  |
| `createdAt` | `integer` |  |
| `updatedAt` | `integer` |  |
| `updatedBy` | `string` |  |
| `message` | `string` |  |
| `isEdited` | `boolean` |  |
| `extraData` | `object` |  |

### Add observables in The Hive v5

Action to add a list of observables in The Hive v5

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_id` | `string` | The id of the alert you want to add observables to. For instance: ~12345 |
| `events` | `object` | The JSON Sekoia event from which to extract the observables to be added to the alert |
| `tlp` | `string` | The TLP for the observables - defaults to AMBER |
| `pap` | `string` | The PAP for the observables - defaults to AMBER |
| `areioc` | `boolean` | Indicates whether observables should be considered IOCs in TheHive - default to true |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `outputObservables` | `array` |  |

### Create an alert in The Hive v5



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sekoia_base_url` | `string` | [Optional] Sekoia base url, depends of the region you want to use |
| `alert` | `object` | A Sekoia.io alert |
| `tlp` | `` | Case's TLP: 0, 1, 2, 3, 4 |
| `pap` | `` | Case's PAP: 0, 1, 2, 3 |


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

### Upload logs to an alert in The Hive v5



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_id` | `string` | The id of the alert you want to upload logs to. For instance: ~12345 |
| `filepath` | `string` | The file to be added to the alert as attachment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `outputAttachment` | `array` |  |


## Extra

Module **`The Hive V5` v1.0.9**