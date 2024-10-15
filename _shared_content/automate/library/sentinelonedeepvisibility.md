# SentinelOneDeepVisibility

![SentinelOneDeepVisibility](/assets/playbooks/library/sentinelonedeepvisibility.png){ align=right width=150 }

This module interacts with the SentinelOne DeepVisibility using AWS S3

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `aws_access_key` | `string` | The identifier of the access key |
| `aws_secret_access_key` | `string` | The secret associated to the access key |
| `aws_region_name` | `string` | The area hosting the AWS resources |

## Triggers

### Consume SentinelOne DeepVisibility events from AWS S3

Consume SentinelOne DeepVisibility events from S3 objects based on notifications

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `queue_name` | `string` | The name of the SQS queue that received the notifications of the creation of S3 objects |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`SentinelOneDeepVisibility` v1.1.0**