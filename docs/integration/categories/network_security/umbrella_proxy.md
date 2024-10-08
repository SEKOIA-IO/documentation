uuid: 5a8ef52f-d143-4735-8546-98539fc07725
name: Umbrella Proxy Logs
type: intake

## Overview

Cisco Umbrella offers flexible, cloud-delivered security. It combines multiple security functions into one solution, so that protection can be extended to devices, remote users, and distributed locations anywhere. CISCO Umbrella is a leading provider of network security and recursive DNS services.

- **Vendor**: Cisco
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Web logs, Web proxy

## Configure

{!_shared_content/operations_center/integrations/cisco_umbrella_set_aws_forwarding.md!}

### Create a S3 Event notification


Use the [following guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html) to create S3 Event Notification.
Once created:

1. In the General configuration, type `dnslogs/` as the Prefix
2. Select the notification for object creation in the Event type section
3. As the destination, choose the SQS service
4. Select the queue you created in the previous section

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/connector_configuration.md!}

!!! Info
    Please find here the official documentation related to [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

{!_shared_content/operations_center/integrations/generated/5a8ef52f-d143-4735-8546-98539fc07725_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_5a8ef52f-d143-4735-8546-98539fc07725_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/5a8ef52f-d143-4735-8546-98539fc07725.md!}

## Further Readings
- [CISCO Umbrella User Guide - Manage your logs](https://docs.umbrella.com/deployment-umbrella/docs/setting-up-an-amazon-s3-bucket)
