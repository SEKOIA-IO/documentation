# The Hive

![The Hive](/assets/playbooks/library/the-hive.png){ align=right width=150 }

[TheHive](https://thehive-project.org/) is a scalable, open source and free Security Incident Response Platform

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Your TheHive instance URL |
| `apikey` | `string` | An API key |
| `organisation` | `string` | The user organisation |

## Actions

### Create an alert in The Hive



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert` | `object` | A Sekoia.io alert |
| `events` | `array` | The alert events used to create TheHive alert artifacts |
| `artifact_tlp` | `integer` | Case's TLP: 0, 1, 2, 3 for WHITE, GREEN, AMBER, RED. Default: 1 |
| `artifact_sighted` | `boolean` | Observable's sighted flag, True to mark the observable as sighted. Default: True |
| `artifact_ignore_similarity` | `boolean` | Observable's similarity ignore flag. `True` to ignore the observable during similarity computing. Default: True |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` |  |
| `createdBy` | `string` |  |
| `createdAt` | `string` |  |
| `updatedAt` | `string` |  |
| `type` | `string` |  |
| `source` | `string` |  |
| `sourceRef` | `string` |  |
| `externalLink` | `string` |  |
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
| `artifacts` | `array` |  |


## Extra

Module **`The Hive` v1.23.0**