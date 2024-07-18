uuid: 07c0cac8-f68f-11ea-adc1-0242ac120002
name: Amazon VPC Flow Logs
type: intake

## Overview

- **Vendor**: AWS
- **Plan**: Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Host network interface, Netflow/Enclave netflow, Network device logs, Network protocol analysis	
- **Coverage Score**: 3

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

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS Flowlogs`.

### Pull events

To start to pull events, you have to: 

1. Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with:
    - the [AWS Fetch new Flowlogs on S3 connector](../../../../automate/library/aws.md#fetch-new-flowlogs-on-s3) for plain text files (gzipped included)
    - the [AWS Fetch new FlowLogs Parquet records on S3 connector](../../../../automate/library/aws.md#fetch-new-flowlogs-parquet-records-on-s3) for parquet files
2. Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the SQS queue and the intake key, from the intake previously created.
3. Start the playbook and enjoy your events.

{!_shared_content/operations_center/integrations/generated/07c0cac8-f68f-11ea-adc1-0242ac120002_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_07c0cac8-f68f-11ea-adc1-0242ac120002_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/07c0cac8-f68f-11ea-adc1-0242ac120002.md!}

## Further Readings
- [AWS VPC Overview](https://aws.amazon.com/vpc/)
- [AWS Flow Logs Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
