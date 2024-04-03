uuid: d3a813ac-f9b5-451c-a602-a5994544d9ed
name: AWS CloudTrail
type: intake

## Overview
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services ([source: AWS CloudTrail Overview](https://aws.amazon.com/cloudtrail/)).

{!_shared_content/operations_center/detection/generated/suggested_rules_d3a813ac-f9b5-451c-a602-a5994544d9ed_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d3a813ac-f9b5-451c-a602-a5994544d9ed.md!}

## Configure

{!_shared_content/operations_center/integrations/aws_create_s3_sqs_notification.md!}

### CloudTrail trail

In order to allow Cloudtrail to store logs in S3, you have to create an **AWS S3 Policy**. Follow [this guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.html) to edit your S3 Bucket.

You need an existing [CloudTrail trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-in-the-console.html) and configure it to record activities from services that you want to monitor.

In the AWS console, navigate to: `Services > CloudTrail > Trails`. From there, enable the events that you want to record:

- Management events: provide visibility into management operations that are performed on resources in your AWS account
- Insights events: help AWS users identify and respond to unusual activity associated with write API calls by continuously analyzing CloudTrail management events. Insights events are logged when CloudTrail detects unusual write management API activity in your account
- Data events: provide visibility into the resource operations performed on or within a resource

Activate the logging on the trail through the switch button (On/Off) located on the top right hand corner of the trail page.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS CloudTrail`.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Fetch new CloudTrail records on S3 connector](../../../../automate/library/aws.md#fetch-new-cloudtrail-records-on-s3).

Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the SQS queue and the intake key, from the intake previously created.

!!!important
    In the "Trigger Configuration" settings of your Cloudtrail playbook, we recommand the following configuration by default: chunk_size = `10000`, frequency = `10` and `tick the box` "delete_consumed_messages" that will delete [S3 notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html) of your Amazon Simple Queue Service, avoiding duplicates.

Start the playbook and enjoy your events.

## Further Readings

- [AWS CloudTrail Overview](https://aws.amazon.com/cloudtrail/)
- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [AWS S3 Overview](https://aws.amazon.com/s3/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
