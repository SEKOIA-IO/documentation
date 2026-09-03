uuid: b031d3d0-bafa-4f4c-8f05-4fb67639b2d8
name: Amazon VPC Flow Logs (Parquet)
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

This intake collects VPC Flow Logs that are delivered to an Amazon S3 bucket in the [Apache Parquet](https://parquet.apache.org/) format. Parquet is a columnar storage format that reduces the size of the delivered log files and speeds up their processing.


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
- In the `Destination` section, select `Send to an Amazon S3 bucket` and provide the ARN of the S3 bucket created previously.
- In the `Log file format` section, select `Parquet`.

Please follow [this guide](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3.html) to configure and set up all the permissions needed.

!!! Info
    Amazon delivers VPC Flow Logs in Parquet format only when you explicitly select `Parquet` as the log file format when creating the flow log. Make sure the destination S3 bucket is the one watched by the SQS queue configured above.

### Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS Flowlogs`.
2. Set up the intake account configuration with the **AWS Region** and either:
    - The **AWS Role ARN** (for OIDC authentication — recommended)
    - The **AWS Access Key** and **Secret Access Key** (for static credentials)
3. Set up the intake configuration with the name of the SQS queue.

!!! Note
    To collect the logs stored in Parquet format, this intake relies on the `Fetch new FlowLogs Parquet records on S3` connector, which reads the Parquet objects notified by the SQS queue.

{!_shared_content/operations_center/integrations/generated/b031d3d0-bafa-4f4c-8f05-4fb67639b2d8_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_b031d3d0-bafa-4f4c-8f05-4fb67639b2d8_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/b031d3d0-bafa-4f4c-8f05-4fb67639b2d8.md!}

## Further Readings
- [AWS VPC Overview](https://aws.amazon.com/vpc/)
- [AWS Flow Logs Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [Flow log files in Apache Parquet format](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3.html#flow-logs-s3-path)
