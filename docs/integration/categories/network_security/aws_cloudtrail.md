---
uuid: d3a813ac-f9b5-451c-a602-a5994544d9ed
title: AWS CloudTrail
name: AWS CloudTrail
type: intake
---

## Overview
AWS CloudTrail is a service that enables governance, compliance, and operational and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides the event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services ([source: AWS CloudTrail Overview](https://aws.amazon.com/cloudtrail/)).

- **Vendor**: AWS
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: AWS CloudTrail logs, Services

## Configure

{!_shared_content/operations_center/integrations/aws_create_s3_sqs_notification.md!}

#### Send CloudTrail trail to an AWS S3 bucket

To allow Cloudtrail to store logs in S3, you have to create an **AWS S3 Policy**. Follow [this guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.html) to edit your S3 Bucket.

For CloudTrail to record activities across your desired AWS services, you need an active [CloudTrail trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-in-the-console.html).

To configure your trail:

1. In the AWS console, navigate to: `Services > CloudTrail > Trails`.
2. Activate the specific events you want to log:

- Management events: provide visibility into management operations that are performed on resources in your AWS account.
- Insights events: help AWS users identify and respond to unusual activity associated with write API calls by continuously analyzing CloudTrail management events. Insights events are logged when CloudTrail detects unusual write management API activity in your account.
- Data events: provide visibility into the resource operations performed on or within a resource.

Activate the logging on the trail through the switch button (On/Off) located at the top right corner of the trail page.

{!_shared_content/integration/intake_configuration.md!}

### Pull events
#### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `AWS CloudTrail`.
2. Set up the intake account configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the intake configuration with the name of the SQS queue


!!!important
    In the "intake configuration" settings, we recommend using the following configuration by default: chunk_size = `10000`, frequency = `10` and `tick the box` "delete_consumed_messages" that will delete [S3 notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html) of your Amazon Simple Queue Service to avoid duplicates.

Start the playbook and enjoy your events.

{!_shared_content/operations_center/integrations/generated/d3a813ac-f9b5-451c-a602-a5994544d9ed_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d3a813ac-f9b5-451c-a602-a5994544d9ed_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d3a813ac-f9b5-451c-a602-a5994544d9ed.md!}

## Further Readings

- [AWS CloudTrail Overview](https://aws.amazon.com/cloudtrail/)
- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [AWS S3 Overview](https://aws.amazon.com/s3/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
