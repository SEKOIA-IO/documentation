---
uuid: a0716ffd-5f9e-4b97-add4-30f1870e3d03
name: Netskope Log Streaming (Transaction Events)
type: intake
---

## Overview

Netskope Log Streaming allows you to access all Netskope-generated logs directly within your preferred cloud storage and further SIEM tools without the need for additional infrastructure like VMs, improving scalability, cost efficiency, and real-time data availability.

- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**:
    - Transaction Events
    

## Configure

{!_shared_content/operations_center/integrations/aws_create_s3_sqs_notification.md!}


### Configure Netskope Log stream

1. Navigate to **Settings > Tools > Log Streaming** to add names and properties for the streams you want to monitor.

    ![step](/assets/integration/endpoint/netskope/log_streaming_1.png){: style="max-width:100%"}

2. Click **Create Stream**. In **Name**, enter a human-readable name for the stream

    ![step](/assets/integration/endpoint/netskope/log_streaming_2.png){: style="max-width:100%"}

3. Select `Transaction Events` dataset
4. Choose `GZIP`
5. For the Amazon S3 destination field, fill in the fields

    ![step](/assets/integration/endpoint/netskope/log_streaming_3.png){: style="max-width:100%"}

6. Activate the stream upon saving

!!! Note
    Select Amazon S3 with SQS for optimum performance.
    Stream activation takes about 60 minutes from creation.


### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/operations_center/integrations/generated/a0716ffd-5f9e-4b97-add4-30f1870e3d03_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a0716ffd-5f9e-4b97-add4-30f1870e3d03_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/a0716ffd-5f9e-4b97-add4-30f1870e3d03.md!}
