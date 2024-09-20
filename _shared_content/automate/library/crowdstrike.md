# CrowdStrike

![CrowdStrike](/assets/playbooks/library/crowdstrike.png){ align=right width=150 }

[CrowdStrike] CrowdStrike provides cloud workload and endpoint security, threat intelligence, and cyberattack response services and products.
 This module provides triggers to collect events from CrowdStrike

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `aws_access_key_id` | `string` | The identifier of the access key |
| `aws_secret_access_key` | `string` | The secret associated to the access key |
| `aws_region` | `string` | The area hosting the AWS resources |

## Triggers

### Fetch new events from CrowdStrike Data replication

Forward Crowdstrike Falcon Data Replication events to Sekoia.io

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `chunk_size` | `integer` | The size of max number of messages for the batch processing (default: 20000) |
| `frequency` | `integer` | Batch frequency in seconds. Should be greater than 0 and lower then 20 (default: 10) |
| `is_fifo` | `boolean` | Flag to determine if the queue is a FIFO queue (default: false) |
| `queue_name` | `string` | The name of the SQS queue that received messages with files information |
| `queue_url` | `string` | The URL of the SQS queue that received messages with files information |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`CrowdStrike` v1.10.1**