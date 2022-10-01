uuid: d3a813ac-f9b5-451c-a602-a5994544d9ed
name: AWS CloudTrail
type: intake

## Overview
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services ([source: AWS CloudTrail Overview](https://aws.amazon.com/cloudtrail/)).

{!_shared_content/operations_center/detection/generated/suggested_rules_d3a813ac-f9b5-451c-a602-a5994544d9ed_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/aws-cloudtrail_do_not_edit_manually.md!}

## Configure

### CloudTrail trail

As a prerequisite you need an existing [CloudTrail trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-in-the-console.html) and configure it to record activities from services that you want to monitor.

In the AWS console, navigate to: `Services > CloudTrail > Trails`. From there, enable the events that you want to record:

- Management events: provide visibility into management operations that are performed on resources in your AWS account.
- Insights events: help AWS users identify and respond to unusual activity associated with write API calls by continuously analyzing CloudTrail management events. Insights events are logged when CloudTrail detects unusual write management API activity in your account.
- Data events: provide visibility into the resource operations performed on or within a resource.

Activate the logging on the trail through the switch button (On/Off) located on the top right hand corner of the trail page.

### Create a SQS queue

This integration relies on S3 Event Notifications to discover new S3 objects.

To be enable to set the S3 Event Notification, create a queue  in the SQS service according [this guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html).

In the Access Policy step choose the advanced configuration and adapt this configuration sample with your own SQS arn (the main change is the Service directive allowing S3 bucket access):
```json
{
  "Version": "2008-10-17",
  "Id": "__default_policy_ID",
  "Statement": [
    {
      "Sid": "__owner_statement",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "SQS:*",
      "Resource": "arn:aws:sqs:XXX:XXX"
    }
  ]
}
```

Please, keep in mind, to create the SQS queue in the same region as the S3 bucket you want to watch.

### Create a S3 Event Notification

Use the [following guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html) to create S3 Event Notification.
Select the notification for object create in the Event type section. As the destination, choose the SQS service and select the queue you create in the previous section.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS CloudTrail`.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Fetch new CloudTrail records on S3 connector](../../../../automate/library/aws.md#fetch-new-cloudtrail-records-on-s3).

Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the SQS queue and the intake key, from the intake previously created.

Start the playbook and enjoy your events.

## Further Readings

- [AWS CloudTrail Overview](https://aws.amazon.com/cloudtrail/)
- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [AWS S3 Overview](https://aws.amazon.com/s3/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
