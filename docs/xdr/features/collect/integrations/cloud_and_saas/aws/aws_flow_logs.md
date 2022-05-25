uuid: 07c0cac8-f68f-11ea-adc1-0242ac120002
name: Amazon VPC Flow Logs
type: intake

## Overview
Amazon VPC Flow Logs is a feature that provides the ability to capture information about IP network traffic as it enters or exits from network interface in your Amazon VPC (Amazon Virtual Private Cloud). VPC Flow Logs can help you with a number of tasks, such as:

- Diagnosing overly restrictive security group rules.
- Monitoring the traffic that is reaching your instance.
- Determining the direction of the traffic to and from the network interfaces.

{!xdr/features/collect/integrations/generated/aws-flow-logs_do_not_edit_manually.md!}

## Configure

### VPC Flow Logs

As a prerequisite you need an existing VPC, subnet or network interface (Elastic Load Balancing, Amazon RDS, Amazon ElastiCache, Amazon Redshift, Amazon WorkSpaces, NAT gateways, Transit gateways) to create a flow log. If you create a flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored.

In the AWS console, navigate to: `Services > VPC`. From there, select the resource for which you want to capture information. The flow logs are available on the following resources: VPC, subnet, or network interfaces.

For VPC and subnet:

- Select the specific resource to monitor
- Go to the tab *Flow logs*
- Click on *Create flow log*
- Set up the flow log: we recommend to capture all traffic (accepted and rejected).

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS Flowlogs`.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [AWS Flowlogs trigger](https://docs.sekoia.io/playbooks/library/aws/#fetch-flowlog-records). You can use the existing template to fasten and ease the creation of your playbook.

Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the S3 Bucket, hosting the Flowlogs records, and a prefix to select the objects (optional, e.g `WSLogs/313000002243/vpcflowlogs/`).

At the end of the playbook, set up the action `Push events to intake` with a SEKOIA.IO API key and the intake key, from the intake previously created.

Start the playbook and enjoy your events.


## Further Readings
- [AWS VPC Overview](https://aws.amazon.com/vpc/)
- [AWS Flow Logs Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
