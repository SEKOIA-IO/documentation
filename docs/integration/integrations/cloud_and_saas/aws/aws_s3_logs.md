uuid: 2d806360-5c22-4722-b335-8eaf5ab3e4bf
name: AWS S3 for logs
type: connector

## Overview

AWS S3 is a service that enables to store and manage data with scalability, high availability, and low latency with high durability. AWS S3 can hold objects up to five Terabytes in size.
Several AWS services offers to store their logs on a S3 bucket. This integration aims to collect line-oriented logs.

{!_shared_content/operations_center/detection/generated/suggested_rules_2d806360-5c22-4722-b335-8eaf5ab3e4bf_do_not_edit_manually.md!}

## Configure

{!_shared_content/operations_center/integrations/aws_create_s3_sqs_notification.md!}

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format that will process your logs.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [AWS Fetch new logs on S3 connector](../../../../automate/library/aws.md#fetch-new-logs-on-s3).

Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the SQS queue and the intake key, from the intake previously created.

Start the playbook and enjoy your events.

## Further Readings

- [AWS S3 Overview](https://aws.amazon.com/s3/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
