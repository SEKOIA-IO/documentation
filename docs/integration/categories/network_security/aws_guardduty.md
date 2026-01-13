---
uuid: 3e060900-4004-4754-a597-d2944a601930
title: Amazon GuardDuty
name: Amazon GuardDuty
type: intake
---

## Overview
AWS GuardDuty is a service that detects potential security issues within your network.

- **Vendor**: AWS
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: GuardDuty alerts

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

{!_shared_content/integration/intake_configuration.md!}

### Pull events
#### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `AWS GuardDuty`.
2. Set up the intake account configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the intake configuration with the name of the SQS queue


{!_shared_content/operations_center/integrations/generated/3e060900-4004-4754-a597-d2944a601930_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_3e060900-4004-4754-a597-d2944a601930_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/3e060900-4004-4754-a597-d2944a601930.md!}

## Further Readings
- [AWS GuardDuty Overview](https://aws.amazon.com/guardduty/)
- [AWS GuardDuty Documentation](https://docs.aws.amazon.com/guardduty/)
- [AWS GuardDuty - Exporting findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html)
- [AWS S3 Overview](https://aws.amazon.com/s3/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
