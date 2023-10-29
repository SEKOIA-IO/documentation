---
title: uuid: 46e45417-187b-45bb-bf81-30df7b1963a0
---

uuid: 46e45417-187b-45bb-bf81-30df7b1963a0
name: Amazon WAF
type: intake

## Overview
AWS WAF is a web application firewall that lets you monitor the HTTP(S) requests that are forwarded to your protected web application resources.

{!_shared_content/operations_center/detection/generated/suggested_rules_46e45417-187b-45bb-bf81-30df7b1963a0_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/46e45417-187b-45bb-bf81-30df7b1963a0.md!}

## Configure

### Prerequisites

#### Create a S3 bucket

Your web ACL traffic logs will be collected in an Amazon S3 bucket.

To set up the bucket, please refer to [this guide](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html).

{!_shared_content/operations_center/integrations/aws_create_sqs_queue.md!}

{!_shared_content/operations_center/integrations/aws_create_s3_notification.md!}

#### Forward traffic logs to S3

To forward events produced by AWS WAF to S3, you have to: 

1. In your AWS console, navigate to: `Services > WAF & Shield > Web ACLs`
2. Select the acl you want forwarding logs to your bucket
3. Select the tab `Logging and metrics`
4. In the first section, in front of the title `Logging`, click the button `Enable`
5. Check `S3 bucket` as `Logging destination` and select your bucket in the dropdown
6. Click the button `Save`

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS WAF`.

### Pull events

To start to pull events, you have to: 

1. Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [AWS Fetch new logs on S3 connector](../../../../automate/library/aws.md#fetch-new-logs-on-s3)
2. Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the SQS queue and the intake key, from the intake previously created
3. Start the playbook and enjoy your events


## Further Readings
- [AWS WAF Overview](https://aws.amazon.com/waf/)
- [AWS WAF Documentation](https://docs.aws.amazon.com/waf/)
- [AWS S3 Overview](https://aws.amazon.com/s3/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
