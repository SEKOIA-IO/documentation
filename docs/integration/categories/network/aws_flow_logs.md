uuid: 07c0cac8-f68f-11ea-adc1-0242ac120002
name: Amazon VPC Flow Logs
type: intake

## Overview

- **Vendor**: AWS
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Host network interface, Netflow/Enclave netflow, Network device logs, Network protocol analysis

Amazon VPC Flow Logs is a feature that provides the ability to capture information about IP network traffic as it enters or exits from network interface in your Amazon VPC (Amazon Virtual Private Cloud). VPC Flow Logs can help you with a number of tasks, such as:

- Diagnosing overly restrictive security group rules
- Monitoring the traffic that is reaching your instance
- Determining the direction of the traffic to and from the network interfaces


## Configure

{!_shared_content/operations_center/integrations/aws_create_s3_sqs_notification.md!}

### VPC Flow Logs

As a prerequisite, you need an existing VPC, subnet or network interface (Elastic Load Balancing, Amazon RDS, Amazon ElastiCache, Amazon Redshift, Amazon WorkSpaces, NAT gateways, Transit gateways) to create a flow log. If you create a flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored.

In the AWS console, navigate to: `Services > VPC`. From there, select the resource for which you want to capture information. The flow logs are available on the following resources: VPC, subnet, or network interfaces.

For VPC and subnet:

- Select the specific resource to monitor
- Go to the tab `Flow logs`
- Click on `Create flow log`
- Set up the flow log: we recommend to capture all traffic (accepted and rejected).

Please follow [this guide](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3.html) to configure and set up all the permissions needed.

### Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS Flowlogs`.
2. Set up the intake account configuration with the **AWS Region** and either:
    - The **AWS Role ARN** (for OIDC authentication — recommended)
    - The **AWS Access Key** and **Secret Access Key** (for static credentials)
3. Set up the intake configuration with the name of the SQS queue.

!!! Warning "Internal traffic filtering"
    By default, to reduce the volume of ingested events, the connector discards every flow log record in which **all** IP addresses are private (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, loopback or link-local addresses). Only records involving at least one public IP address (traffic entering or leaving your VPC through the Internet) are forwarded to Sekoia.io.

    As a consequence, if your flow logs only contain internal traffic (e.g. between instances of the same VPC, or between peered VPCs), no event will appear in the intake even though the connector is correctly reading the S3 bucket.

    To collect internal traffic as well, disable the `filter_internal_traffic` option in the intake configuration (enabled by default). Keep in mind that this can significantly increase the volume of ingested events.

{!_shared_content/operations_center/integrations/generated/07c0cac8-f68f-11ea-adc1-0242ac120002_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_07c0cac8-f68f-11ea-adc1-0242ac120002_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/07c0cac8-f68f-11ea-adc1-0242ac120002.md!}

## Further Readings
- [AWS VPC Overview](https://aws.amazon.com/vpc/)
- [AWS Flow Logs Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
