## OCSF Mapping for AWS Devices


**OCSF Class:** `Device Inventory Info`



**Class UID:** `5001`



**OCSF Version:** `1.6.0`


## Information Collected

The AWS Devices fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### AWS EC2 Instance
EC2 instance with network interfaces, security groups, and organizational context

```json
{
  "InstanceId": "i-0abcd1234efgh5678",
  "InstanceType": "t3.medium",
  "ImageId": "ami-0c55b159cbfafe1f0",
  "State": {
    "Name": "running",
    "Code": 16
  },
  "PublicDnsName": "ec2-11-22-44-66.compute-1.amazonaws.com",
  "PublicIpAddress": "1.2.3.4",
  "PrivateDnsName": "ip-11-00-1-15.ec2.internal",
  "PrivateIpAddress": "11.00.1.15",
  "PlatformDetails": "Linux/UNIX",
  "LaunchTime": "2025-08-26T14:34:38.000Z",
  "Hypervisor": "xen",
  "SubnetId": "subnet-0123abcd",
  "VpcId": "vpc-12345678",
  "Tags": [
    {
      "Key": "Name",
      "Value": "web-server-prod-01"
    },
    {
      "Key": "aws:autoscaling:groupName",
      "Value": "asg-web-servers"
    }
  ],
  "SecurityGroups": [
    {
      "GroupId": "sg-0123abcd",
      "GroupName": "web-sg"
    },
    {
      "GroupId": "sg-0123efgh",
      "GroupName": "default"
    }
  ],
  "NetworkInterfaces": [
    {
      "NetworkInterfaceId": "eni-0123abcd",
      "Description": "Primary network interface",
      "MacAddress": "01:01:ac:00:01:96",
      "PrivateIpAddress": "11.00.1.15",
      "PrivateDnsName": "ip-11-00-1-15.ec2.internal"
    }
  ],
  "IamInstanceProfile": {
    "Arn": "arn:aws:iam::123456789012:instance-profile/ec2-role"
  },
  "BlockDeviceMappings": [
    {
      "DeviceName": "/dev/xvda",
      "Ebs": {
        "VolumeId": "vol-0123abcd",
        "AttachTime": "2025-08-26T14:34:38.000Z",
        "DeleteOnTermination": true,
        "Status": "attached"
      }
    }
  ]
}

```

#### AWS EC2 Instance Minimal
EC2 instance with minimal configuration

```json
{
  "InstanceId": "i-1234567890abcdef0",
  "InstanceType": "t2.micro",
  "ImageId": "ami-12345678",
  "State": {
    "Name": "running"
  },
  "PrivateDnsName": "ip-2-3-0-1.ec2.internal",
  "PrivateIpAddress": "2.3.0.1",
  "PlatformDetails": "Linux/UNIX",
  "LaunchTime": "2025-06-15T10:00:00.000Z",
  "Hypervisor": "xen",
  "SubnetId": "subnet-default",
  "VpcId": "vpc-default",
  "Tags": [],
  "SecurityGroups": [
    {
      "GroupId": "sg-default",
      "GroupName": "default"
    }
  ],
  "NetworkInterfaces": [
    {
      "NetworkInterfaceId": "eni-default",
      "MacAddress": "02:ab:cd:ef:12:34",
      "PrivateIpAddress": "1.2.3.4",
      "PrivateDnsName": "ip-1-2-3-4.ec2.internal"
    }
  ]
}

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic |
|--------------|-----------------|-------------|-----------|-------|
| `InstanceId` | `device.uid` | Unique EC2 instance identifier | `string` | Direct mapping of EC2 instance ID |
| `PublicDnsName || PrivateDnsName || InstanceId` | `device.hostname` | Device hostname or DNS name | `string` | Fallback chain: PublicDnsName → PrivateDnsName → InstanceId; skip empty strings |
| `Tags[Key='Name'].Value` | `device.name` | Device name from tags | `string` | Extract 'Name' tag value; if absent, use InstanceId |
| `static: Server` | `device.type` | OCSF device type | `string` | Always 'Server' for EC2 instances |
| `static: 1` | `device.type_id` | OCSF device type ID | `integer` | Always 1 for Server type |
| `PlatformDetails` | `device.os.name` | Operating system name | `string` | Direct mapping (e.g., 'Linux/UNIX', 'Windows', 'macOS') |
| `PlatformDetails` | `device.os.type` | Operating system type | `string` | Parse OS: 'windows'→Windows, 'linux'/'unix'→Linux, 'mac'→macOS, else→Unknown |
| `PlatformDetails` | `device.os.type_id` | OCSF OS type ID | `integer` | Map OS type: Windows→100, Linux→200, macOS→300, Unknown→0 |
| `NetworkInterfaces[]` | `device.network_interfaces[]` | List of network interfaces attached to device | `object` | Iterate over network interfaces; map each field according to sub-mappings below |
| `NetworkInterfaces[].NetworkInterfaceId` | `device.network_interfaces[].uid` | Network interface unique ID | `string` | Direct mapping of ENI ID |
| `NetworkInterfaces[].Description` | `device.network_interfaces[].name` | Interface description or name | `string` | Direct mapping; fallback to 'Primary network interface' if empty |
| `NetworkInterfaces[].MacAddress` | `device.network_interfaces[].mac` | MAC address | `string` | Direct mapping |
| `NetworkInterfaces[].PrivateIpAddress` | `device.network_interfaces[].ip` | Network interface IP address | `ip` | Direct mapping of private IP |
| `NetworkInterfaces[].PrivateDnsName` | `device.network_interfaces[].hostname` | Network interface hostname | `string` | Direct mapping of private DNS name |
| `static: Wired` | `device.network_interfaces[].type` | Interface type | `string` | Always 'Wired' for EC2 network interfaces |
| `static: 1` | `device.network_interfaces[].type_id` | Interface type ID | `integer` | Always 1 for Wired interface type |
| `PublicIpAddress || PrivateIpAddress` | `device.ip` | Primary device IP address | `ip` | Prefer public IP; fallback to private IP |
| `SecurityGroups[]` | `device.groups[]` | Security groups associated with instance | `object` | Iterate over security groups; map according to sub-mappings below |
| `SecurityGroups[].GroupId` | `device.groups[].uid` | Security group unique ID | `string` | Direct mapping of security group ID |
| `SecurityGroups[].GroupName` | `device.groups[].name` | Security group name | `string` | Direct mapping of security group name |
| `Placement.AvailabilityZone || Placement` | `device.region` | AWS availability zone (region) | `string` | Extract availability zone (e.g., 'us-east-1a') |
| `SubnetId` | `device.subnet` | VPC subnet ID | `string` | Direct mapping of subnet ID |
| `VpcId` | `device.domain` | VPC ID for network domain | `string` | Direct mapping of VPC ID (mapped as domain) |
| `Hypervisor` | `device.hypervisor` | Hypervisor type | `string` | Direct mapping (e.g., 'xen', 'nitro') |
| `InstanceType` | `device.model` | EC2 instance type | `string` | Direct mapping (e.g., 't3.medium', 'm5.large') |
| `ImageId` | `device.image_id` | EC2 AMI (Amazon Machine Image) ID | `string` | Direct mapping of AMI ID |
| `State.Name` | `device.state` | Instance state | `string` | Direct mapping (running, stopped, terminated, etc.) |
| `static: Amazon Web Services` | `device.vendor_name` | Device vendor name | `string` | Always 'Amazon Web Services' |
| `LaunchTime` | `device.boot_time` | Instance launch/boot time | `timestamp` | Convert ISO 8601 to string (ISO format preferred) |
| `BlockDeviceMappings[0].Ebs.AttachTime || LaunchTime` | `device.created_time` | Device creation timestamp | `timestamp` | Use EBS attachment time if available; fallback to launch time; convert to Unix epoch |
| `LaunchTime` | `time` | OCSF event timestamp | `timestamp` | Convert ISO 8601 to Unix epoch for OCSF event timestamp |
| `IamInstanceProfile` | `device.is_managed` | Whether instance has IAM role (managed by policies) | `boolean` | true if IamInstanceProfile is present and not empty; false otherwise |
| `Tags[Key='aws:autoscaling:groupName'].Value` | `device.autoscale_uid` | Auto Scaling group name | `string` | Extract 'aws:autoscaling:groupName' tag value if present |
| `OwnerId` | `device.org.uid` | AWS account ID | `string` | Direct mapping of AWS account ID |
| `OwnerId` | `device.org.name` | Organization/Account name | `string` | Format as 'AWS Account <OwnerId>' |
| `ImageId + State.Name` | `device.desc` | Device description with image and state | `string` | Concatenate as 'AMI: <ImageId>, State: <State.Name>' |
| `static: AWS EC2` | `metadata.product.name` | Product name | `string` | Always 'AWS EC2' |
| `static: 1.6.0` | `metadata.version` | OCSF schema version | `string` | Fixed OCSF schema version |
| `static: 2` | `activity_id` | OCSF activity ID | `integer` | Always 2 for 'Collect' activity |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | Always 'Collect' for asset inventory |
| `static: Discovery` | `category_name` | OCSF category name | `string` | Always 'Discovery' |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | Always 5 for Discovery category |
| `static: Device Inventory Info` | `class_name` | OCSF class name | `string` | Always 'Device Inventory Info' |
| `static: 5001` | `class_uid` | OCSF class UID | `integer` | Always 5001 for Device Inventory Info |
| `computed: 500100 + activity_id` | `type_uid` | OCSF type UID | `integer` | Base 500100 + activity_id (2 = 500102) |
| `computed: class_name + ': ' + activity_name` | `type_name` | OCSF type name | `string` | Concatenate 'Device Inventory Info: Collect' |
| `static: Informational` | `severity` | Event severity | `string` | Always 'Informational' for inventory events |
| `static: 1` | `severity_id` | OCSF severity ID | `integer` | Always 1 for Informational severity |




### OCSF Model Structure

#### Device Inventory Info: Collect
Transformed EC2 instance to OCSF Device Inventory Info event

```json
{
  "activity_id": 2,
  "activity_name": "Collect",
  "category_name": "Discovery",
  "category_uid": 5,
  "class_name": "Device Inventory Info",
  "class_uid": 5001,
  "type_name": "Device Inventory Info: Collect",
  "type_uid": 500102,
  "severity": "Informational",
  "severity_id": 1,
  "time": 1725011678,
  "metadata": {
    "product": {
      "name": "AWS EC2",
      "version": "1.6.0"
    },
    "version": "1.6.0"
  },
  "device": {
    "uid": "i-0abcd1234efgh5678",
    "name": "web-server-prod-01",
    "hostname": "ec2-11-22-44-66.compute-1.amazonaws.com",
    "type": "Server",
    "type_id": 1,
    "vendor_name": "Amazon Web Services",
    "ip": "1.2.3.4",
    "model": "t3.medium",
    "image_id": "ami-0c55b159cbfafe1f0",
    "state": "running",
    "region": "us-east-1a",
    "subnet": "subnet-0123abcd",
    "domain": "vpc-12345678",
    "hypervisor": "xen",
    "is_managed": true,
    "autoscale_uid": "asg-web-servers",
    "boot_time": "2025-08-26T14:34:38Z",
    "created_time": 1725011678,
    "os": {
      "name": "Linux/UNIX",
      "type": "Linux",
      "type_id": 200
    },
    "network_interfaces": [
      {
        "uid": "eni-0123abcd",
        "name": "Primary network interface",
        "ip": "11.00.1.15",
        "hostname": "ip-11-00-1-15.ec2.internal",
        "mac": "01:01:ac:00:01:96",
        "type": "Wired",
        "type_id": 1
      }
    ],
    "groups": [
      {
        "uid": "sg-0123abcd",
        "name": "web-sg"
      },
      {
        "uid": "sg-0123efgh",
        "name": "default"
      }
    ],
    "org": {
      "uid": "123456789012",
      "name": "AWS Account 123456789012"
    },
    "desc": "AMI: ami-0c55b159cbfafe1f0, State: running"
  }
}

```


