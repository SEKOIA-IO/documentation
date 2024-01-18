# AWS

![AWS](/assets/playbooks/library/aws.svg){ align=right width=150 }

[AWS](https://aws.amazon.com/) is a one of the main cloud provider, supported by Amazon. It offers services for storage (S3, Glacier, EBS, ...), for networking (Snowball, CloudFront, ...), for computing (EC2, ECS, EKS, ...) and others.
This module provides triggers to collect events from AWS

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `aws_access_key` | `string` | The identifier of the access key |
| `aws_secret_access_key` | `string` | The secret associated to the access key |
| `aws_region_name` | `string` | The area hosting the AWS resources |

## Triggers

### Fetch CloudTrail logs (deprecated)

Get the last records from CloudTrail (deprecated in flavor of Fetch new CloudTrail records on S3)

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `bucket_name` | `string` | The bucket that contains CloudTrail logs |
| `prefix` | `string` | Limits the response to keys that begin with the specified prefix |
| `chunk_size` | `integer` | The size of chunks for the batch processing |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `records` | `array` | A list of CloudTrail log records |
| `records_path` | `string` | The filename containing the records |


### Fetch Flowlog records (deprecated)

Get the last records from FlowLog (deprecated in flavor of Fetch new logs on S3)

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `bucket_name` | `string` | The bucket that contains Flowlog records |
| `prefix` | `string` | Limits the response to keys that begin with the specified prefix |
| `chunk_size` | `integer` | The size of chunks for the batch processing |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `records` | `array` | A list of Flowlog records |
| `records_path` | `string` | The filename containing the records |


### [BETA] Fetch new CloudFront logs on S3

Get all CloudFront records from S3

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `queue_name` | `string` | The name of the SQS queue that received the notifications of the creation of S3 objects |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `separator` | `string` | The separator used between each records (default: the linefeed character '\n') |
| `skip_first` | `integer` | The number of records to skip at the begining of each S3 object (default: 0) |
| `delete_consumed_messages` | `boolean` | Flag to delete consuming messages (default: false) |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


### Fetch new Flowlogs on S3

Get line-oriented Flowlog records from new S3 objects based on notifications

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `queue_name` | `string` | The name of the SQS queue that received the notifications of the creation of S3 objects |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `separator` | `string` | The separator used between each records (default: the linefeed character '\n') |
| `skip_first` | `integer` | The number of records to skip at the begining of each S3 object (default: 0) |
| `ignore_comments` | `boolean` | Flag to ignore commented lines (starting with the character `#`; default: false) |
| `delete_consumed_messages` | `boolean` | Flag to delete consuming messages (default: false) |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


### Fetch new FlowLogs Parquet records on S3

Get FlowLogs records from new S3 Parquet objects based on notifications

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `queue_name` | `string` | The name of the SQS queue that received the notifications of the creation of S3 objects |
| `delete_consumed_messages` | `boolean` | Flag to delete consuming messages (default: false) |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


### Fetch new logs on S3

Get line-oriented records from new S3 objects based on notifications

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `queue_name` | `string` | The name of the SQS queue that received the notifications of the creation of S3 objects |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `separator` | `string` | The separator used between each records (default: the linefeed character '\n') |
| `skip_first` | `integer` | The number of records to skip at the begining of each S3 object (default: 0) |
| `ignore_comments` | `boolean` | Flag to ignore commented lines (starting with the character `#`; default: false) |
| `delete_consumed_messages` | `boolean` | Flag to delete consuming messages (default: false) |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


### Fetch new CloudTrail records on S3

Get Cloudtrail records from new S3 objects based on notifications

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `queue_name` | `string` | The name of the SQS queue that received the notifications of the creation of S3 objects |
| `delete_consumed_messages` | `boolean` | Flag to delete consuming messages (default: false) |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


### Fetch new messages from the SQS

Get messages from SQS

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `queue_name` | `string` | The name of the SQS queue |
| `delete_consumed_messages` | `boolean` | Flag to delete consuming messages (default: false) |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`AWS` v1.29.6**