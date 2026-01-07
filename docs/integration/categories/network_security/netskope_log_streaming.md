---
uuid: 7b6d0592-9e0e-4db0-adf0-c9ab2d5c2162
name: Netskope Log Streaming (Transaction Events)
type: intake
---

## Overview

Netskope Log Streaming allows you to access all Netskope-generated logs directly within your preferred cloud storage and further SIEM tools without the need for additional infrastructure like VMs, improving scalability, cost efficiency, and real-time data availability.

- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**:
    - Transaction Events
 
!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.
    

## Configure

{!_shared_content/operations_center/integrations/aws_create_s3_sqs_notification.md!}


### Configure Netskope Log stream

1. Navigate to **Settings > Tools > Log Streaming** to add names and properties for the streams you want to monitor.

    ![step](/assets/integration/network_security/netskope/log_streaming_1.png){: style="max-width:100%"}

2. Click **Create Stream**. In **Name**, enter a human-readable name for the stream

    ![step](/assets/integration/network_security/netskope/log_streaming_2.png){: style="max-width:100%"}

3. Select `Transaction Events` dataset
4. Choose `GZIP`
5. For the Amazon S3 destination field, fill in the fields

    ![step](/assets/integration/network_security/netskope/log_streaming_3.png){: style="max-width:100%"}

6. Activate the stream upon saving

!!! Note
    Select Amazon S3 with SQS for optimum performance.
    Stream activation takes about 60 minutes from creation.


### Instruction on Sekoia

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Netskope Transaction Events with AWS S3`.


### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the AWS `Fetch new logs on S3` trigger. 

Set up the module configuration with the `AWS access Key ID`, the `AWS secret access Key` and the `AWS region name`.
Set up the trigger configuration with the `AWS SQS queue name` and the `intake key`,  from the intake previously created.

Start the playbook and enjoy your events.

{!_shared_content/operations_center/integrations/generated/7b6d0592-9e0e-4db0-adf0-c9ab2d5c2162_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_7b6d0592-9e0e-4db0-adf0-c9ab2d5c2162_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/7b6d0592-9e0e-4db0-adf0-c9ab2d5c2162.md!}
