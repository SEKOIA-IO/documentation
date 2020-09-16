uuid: 07c0cac8-f68f-11ea-adc1-0242ac120002
name: AWS Flow Logs 

## Overview
AWS VPC Flow Logs is a feature that provides the ability to capture information about IP network traffic as it enters or exits from network interface in your AWS VPC (Amazon Virtual Privacte Cloud). Flow logs can help you with a number of tasks, such as :

- Diagnosing overly restrictive security group rules
- Monitoring the traffic that is reaching your instance
- Determining the direction of the traffic to and from the network interfaces 

## Setup
Please [contact us](mailto:support@sekoia.io) to discuss about the AWS services in your organization in order to find the appropriate solution to forward Flow Logs to SEKOIA.IO.

### 1. VPC Flow Logs 

As a prerequisite you need an existing VPC, subnet or network interface (Elastic Load Balancing, Amazon RDS, Amazon ElastiCache, Amazon Redshift, Amazon WorkSpaces, NAT gateways, Transit gateways) to create a flow log. If you create a flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored.

In the AWS console, navigate to: `Services > VPC`. From there, select the resource for which you want to capture information. The flow logs are available on the following resources: VPC, subnet, or network interfaces.

For VPC and subnet:

- Select the specific resource to monitor
- Go to the tab *Flow logs*
- Click on *Create flow log*
- Set up the flow log: we recommend to capture all traffic (accepted and rejected) 

### 2. Log forwarding configuration

This part should be discussed with SEKOIA people to find an appropriate solution to forward Flow logs to SEKOIA.IO.

The following default record format is integrated to the Operation Center:

`<version> <account-id> <interface-id> <srcaddr> <dstaddr> <srcport> <dstport> <protocol> <packets> <bytes> <start> <end> <action> <log-status>`

Again, you should discuss with SEKOIA people if your flow log records are captured with a custom format.

## Further Readings
- [AWS VPC Overview](https://aws.amazon.com/vpc/)
- [AWS Flow Logs Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
