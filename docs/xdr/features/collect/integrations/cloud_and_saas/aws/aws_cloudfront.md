uuid: fc99c983-3e6c-448c-97e6-7e0948e12415
name: Amazon CloudFront Logs
type: intake

## Overview
Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you're serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

{!_shared_content/operations_center/detection/generated/suggested_rules_fc99c983-3e6c-448c-97e6-7e0948e12415_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/fc99c983-3e6c-448c-97e6-7e0948e12415.md!}

## Configure

!!! Important
    Cloudfront have strict requirements regarding regions. Make sure to check [the regions availabled](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html#access-logs-choosing-s3-bucket) before creating the data collection architecture.

{!_shared_content/operations_center/integrations/aws_create_s3_sqs_notification.md!}

#### CloudFront Logs

You can configure CloudFront to create log files that contain detailed information about every user request that CloudFront receives. These are called standard logs, also known as access logs. 

First of all, follow the [regions and s3 buckets requirements](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html#access-logs-choosing-s3-bucket) 

also your AWS account must have the following permissions for the bucket that you specify for log files - see [this link](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html#AccessLogsBucketAndFileOwnership) for more information:

- The S3 access control list (ACL) for the bucket must grant you FULL_CONTROL. If you're the bucket owner, your account has this permission by default. If you're not, the bucket owner must update the ACL for the bucket.
- s3:GetBucketAcl
- s3:PutBucketAcl

To turn on standard logging for a CloudFront distribution, follow these steps:

1. Access the CloudFront console.
2. Choose the distribution you want to update.
3. On the General tab, under Settings, choose Edit.
4. For Standard logging, select On.
5. Choose the S3 bucket where you want CloudFront to deliver the log files. You can specify an optional prefix for the file names.
6. Choose Save changes.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS CloudFront`

### Pull events

To start to pull events, you have to: 

1. Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Fetch new CloudFront logs on S3](../../../../automate/library/aws.md#fetch-new-logs-on-s3).
2. Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the SQS queue and the intake key, from the intake previously created.
3. Start the playbook and enjoy your events.

## Further Readings
- [AWS CloudFront configuration doc](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html)