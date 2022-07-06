uuid: 2d806360-5c22-4722-b335-8eaf5ab3e4bf
name: AWS S3 for logs
type: connector

## Overview

AWS S3 is a service that enables to store and manage data with scalability, high availability, and low latency with high durability. AWS S3 can hold objects up to five Terabytes in size.
Several AWS services offers to store their logs on a S3 bucket. This integration aims to collect line-oriented logs.

## Configure

### Create a SQS queue

This integration relies on S3 Event Notifications to discover new S3 objects.

To be enable to set the S3 Event Notification, create a queue  in the SQS service according [this guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html).
Please, keep in mind, to create the SQS queue in the same region as the S3 bucket you want to watch.

### Create a S3 Event Notification

Use the [following guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html) to create S3 Event Notification.
Select the notification for object create in the Event type section. As the destination, choose the SQS service and select the queue you create in the previous section.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format that will process your logs.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [AWS Fetch new logs on S3 connector](https://docs.sekoia.io/playbooks/library/aws/#fetch-new-logs-on-s3).

Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the SQS queue and the intake key, from the intake previously created.

Start the playbook and enjoy your events.

## Further Readings

- [AWS S3 Overview](https://aws.amazon.com/s3/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
