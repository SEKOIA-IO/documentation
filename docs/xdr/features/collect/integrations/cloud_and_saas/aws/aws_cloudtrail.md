uuid: d3a813ac-f9b5-451c-a602-a5994544d9ed
name: AWS CloudTrail
type: intake

## Overview
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services ([source: AWS CloudTrail Overview](https://aws.amazon.com/cloudtrail/)).

{!xdr/features/collect/integrations/generated/aws-cloudtrail_do_not_edit_manually.md!}

## Configure

### CloudTrail trail

As a prerequisite you need an existing [CloudTrail trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-in-the-console.html) and configure it to record activities from services that you want to monitor.

In the AWS console, navigate to: `Services > CloudTrail > Trails`. From there, enable the events that you want to record:

- Management events: provide visibility into management operations that are performed on resources in your AWS account.
- Insights events: help AWS users identify and respond to unusual activity associated with write API calls by continuously analyzing CloudTrail management events. Insights events are logged when CloudTrail detects unusual write management API activity in your account.
- Data events: provide visibility into the resource operations performed on or within a resource.

Activate the logging on the trail through the switch button (On/Off) located on the top right hand corner of the trail page.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS CloudTrail`.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [AWS Cloudtrail trigger](https://docs.sekoia.io/playbooks/library/aws/#fetch-cloudtrail-logs). You can use the existing template to fasten and ease the creation of your playbook.

Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the S3 Bucket, hosting the CloudTrail logs, and a prefix to the CloudTrail objects (e.g `AWSLogs/313400002243/CloudTrail/`).

At the end of the playbook, set up the action `Push events to intake` with a SEKOIA.IO API key and the intake key, from the intake previously created.

Start the playbook and enjoy your events.

## Further Readings


- [AWS CloudTrail Overview](https://aws.amazon.com/cloudtrail/)
- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
