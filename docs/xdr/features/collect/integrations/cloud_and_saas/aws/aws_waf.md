uuid: 46e45417-187b-45bb-bf81-30df7b1963a0
name: Amazon WAF
type: intake

## Overview
AWS WAF is a web application firewall that lets you monitor the HTTP(S) requests that are forwarded to your protected web application resources.

{!_shared_content/operations_center/detection/generated/suggested_rules_46e45417-187b-45bb-bf81-30df7b1963a0_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/aws-waf_do_not_edit_manually.md!}

## Configure

### Prerequisites

#### Create a S3 bucket

Your web ACL traffic logs will be collected in an Amazon S3 bucket.

To set up the bucket, please refer to [this guide](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html).

#### Create a SQS queue

This integration relies on S3 Event Notifications to discover new S3 objects.

To be enable to set the S3 Event Notification:

1. Create a queue  in the SQS service according [this guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html).
2. In the Access Policy step choose the advanced configuration and adapt this configuration sample with your own SQS arn (the main change is the Service directive allowing S3 bucket access):
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

#### Create a S3 Event Notification

Use the [following guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html) to create S3 Event Notification and then:

1. Select the notification for object creation in the Event type section.
2. As the destination, choose the SQS service
3. Select the queue you create in the previous section.

#### Forward traffic logs to S3

To forward events produced by AWS WAF to S3, you have to: 

1. In your AWS console, navigate to: `Services > WAF & Shield > Web ACLs`.
2. Select the acl you want forwarding logs to your bucket.
3. Select the tab `Logging and metrics`.
4. In the first section, in front of the title `Logging`, click the button `Enable`.
5. Check `S3 bucket` as `Loggng destination` and select your bucket in the dropdown.
6. Click the button `Save`.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS WAF`.

### Pull events

To start to pull events, you have to: 

1. Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [AWS Fetch new logs on S3 connector](../../../../automate/library/aws.md#fetch-new-logs-on-s3).
2. Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the SQS queue and the intake key, from the intake previously created.
3. Start the playbook and enjoy your events.


## Further Readings
- [AWS WAF Overview](https://aws.amazon.com/waf/)
- [AWS WAF Documentation](https://docs.aws.amazon.com/waf/)
- [AWS S3 Overview](https://aws.amazon.com/s3/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
