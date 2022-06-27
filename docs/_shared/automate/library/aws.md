# AWS



[AWS](https://aws.amazon.com/) is a one of the main cloud provider, supported by Amazon. It offers services for storage (S3, Glacier, EBS, ...), for networking (Snowball, CloudFront, ...), for computing (EC2, ECS, EKS, ...) and others.
This module provides triggers to collect events from AWS

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| aws_access_key | string | The identifier of the access key |
| aws_secret_access_key | string | The secret associated to the access key |
| aws_region_name | string | The area hosting the AWS resources |





## Triggers

### Fetch CloudTrail logs

Get the last records from CloudTrail



#### Arguments
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| frequency | integer | Batch frequency in seconds |
| bucket_name | string | The bucket that contains CloudTrail logs |
| prefix | string | Limits the response to keys that begin with the specified prefix |
| chunk_size | integer | The size of chunks for the batch processing |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| records | array | A list of CloudTrail log records |
| records_path | string | The filename containing the records |







### Fetch Flowlog records

Get the last records from FlowLog



#### Arguments
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| frequency | integer | Batch frequency in seconds |
| bucket_name | string | The bucket that contains Flowlog records |
| prefix | string | Limits the response to keys that begin with the specified prefix |
| chunk_size | integer | The size of chunks for the batch processing |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| records | array | A list of Flowlog records |
| records_path | string | The filename containing the records |















## Extra

Module **AWS v.1.8.1**