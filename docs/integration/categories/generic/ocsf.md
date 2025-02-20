uuid: a9c959ac-78ec-47a4-924e-8156a77cebf5
name: AWS CloudTrail
type: intake

## Overview

The OCSF (Open Cybersecurity Schema Framework) is an initiative to create a common, open-source set of data standards and schemas for cybersecurity threat information. It aims to improve interoperability and streamline threat data sharing across different tools and platforms.

- **Vendor**: OCSF
- **Supported environment**: SaaS
- **Version compatibility**: 1.1
- **Detection based on**: Telemetry
- **Supported application or feature**: System Activity, Findings, Identity & Access Management, Network Activity, Discovery application Activity


## Configure

### Deploying the Data Collection Architecture

This section will guide you through creating all the AWS resources needed to collect OCSF events. If you already have existing resources that you want to use, you may do so, but any potential issues or incompatibilities with this tutorial will be your responsibility.

#### Prerequisites

In order to set up the AWS architecture, you need an administator access to the Amazon console with the permissions to create and manage users, Security Lake subscribers, S3 notifications, SQS queues and resource accesses (RAM).

### Create a Security DataLake subscriber

To allow Sekoia.io to collect OCSF events, you need an active [subscriber](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-data-access.html).

To create a subscriber:

1. In the AWS console, navigate to: `Services > Security Lake > Subscribers`.
2. Click `Create subscriber`.
3. Name the subscriber (e.g: `Sekoia.io`) and type a description.
4. Select `S3` as the `Data access` method.
5. Type the `accountID` and `externalID` associated to the access key.
6. Select the sources you want to forward to Sekoia.io.
7. Click `Create`

### Pull events

Go to the [intake page](https://app.sekoia.io/intakes/new) and create a new intake with the OCSF format.

Type the name of the intake, select the entity and click `Next`.
Select or create an account with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key, and the region name. Set up the configuration with the name of the SQS queue (Keep the last part from the arn of the `subscription endpoint`).

!!!important
    In the configuration settings of your OCSF intake, we recommend using the following configuration by default: chunk_size = `10000` and frequency = `10`.

[Start the intake](https://docs.sekoia.io/xdr/features/collect/intakes/#startstop-a-pull-intake) and enjoy your events.

{!_shared_content/operations_center/integrations/generated/a9c959ac-78ec-47a4-924e-8156a77cebf5_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a9c959ac-78ec-47a4-924e-8156a77cebf5_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/a9c959ac-78ec-47a4-924e-8156a77cebf5.md!}

## Further Readings

- [AWS Security Lake Overview](https://aws.amazon.com/security-lake/)
- [AWS Security Lake Documentation](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html)
- [AWS S3 Overview](https://aws.amazon.com/s3/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
