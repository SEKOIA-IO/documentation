uuid: d3a813ac-f9b5-451c-a602-a5994544d9ed
name: AWS CloudTrail

## Overview
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services ([source: AWS CloudTrail Overview](https://aws.amazon.com/cloudtrail/)).

{!operation_center/integration_catalog/generated/aws-cloudtrail_do_not_edit_manually.md!}

## Configure
Please [contact us](mailto:support@sekoia.io) to discuss about the AWS services in your organization in order to find the appropriate solution to forward CloudTrail events to SEKOIA.IO.

### CloudTrail trail

As a prerequisite you need an existing CloudTrail trail and configure it to record activities from services that you want to monitor.

In the AWS console, navigate to: `Services > CloudTrail > Trails`. From there, enable the events that you want to record:

- Management events: provide visibility into management operations that are performed on resources in your AWS account.
- Insights events: help AWS users identify and respond to unusual activity associated with write API calls by continuously analyzing CloudTrail management events. Insights events are logged when CloudTrail detects unusual write management API activity in your account.
- Data events: provide visibility into the resource operations performed on or within a resource.

Activate the logging on the trail through the switch button (On/Off) located on the top right hand corner of the trail page.

## Further Readings


- [AWS CloudTrail Overview](https://aws.amazon.com/cloudtrail/)
- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
