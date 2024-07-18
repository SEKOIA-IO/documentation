uuid: 3e060900-4004-4754-a597-d2944a601930
name: Amazon GuardDuty
type: intake

## Overview
AWS GuardDuty is a service that detects potential security issues within your network.

- **Vendor**: AWS
- **Plan**: Defend Core & Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: AWS CloudTrail logs, Services

## Configure

{!_shared_content/operations_center/integrations/aws_create_s3_sqs_notification.md!}

#### Forward findings to S3

To export forward findings to S3, please refer [this guide](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html).

You have to:

1. In your AWS console, navigate to: `Services > GuardDuty > Settings`
2. Go to the `Finding export options` section
3. Select the bucket you created previously. Ensure your bucket policy allows GuardDuty to add new objects
4. Select or create a key for the KMS encryption
6. Click the button `Save`

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS GuardDuty`.

### Pull events

To start to pull events, you have to:

1. Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [AWS Fetch new logs on S3 connector](../../../../automate/library/aws.md#fetch-new-logs-on-s3)
2. Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the SQS queue as well as the intake key from the intake previously created
3. Start the playbook and enjoy your events

{!_shared_content/operations_center/integrations/generated/3e060900-4004-4754-a597-d2944a601930_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_3e060900-4004-4754-a597-d2944a601930_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/3e060900-4004-4754-a597-d2944a601930.md!}

## Further Readings
- [AWS GuardDuty Overview](https://aws.amazon.com/guardduty/)
- [AWS GuardDuty Documentation](https://docs.aws.amazon.com/guardduty/)
- [AWS GuardDuty - Exporting findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html)
- [AWS S3 Overview](https://aws.amazon.com/s3/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
