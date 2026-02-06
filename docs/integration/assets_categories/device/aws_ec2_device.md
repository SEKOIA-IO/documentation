uuid: e2a7c6b4-9f1d-4b8a-8c3e-2d5f7a1e4b9c
name: AWS devices
type: asset

## Overview

Amazon Elastic Compute Cloud (EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers by providing a simple web service interface that allows you to obtain and configure capacity with minimal friction.

- **Vendor**: Amazon
- **Product**: AWS EC2
- **Supported environment**: Cloud

## Configure

### How to create an IAM account with proper permissions

To connect AWS EC2 to Sekoia.io, you need to create an IAM user with the necessary permissions to access EC2 instances. Follow these steps:

1. Sign in to the AWS Management Console and navigate to the IAM service.

    ![AWS Console IAM service selection](/assets/operation_center/asset_connectors/device/aws/aws_create_user_1.png)

2. Click **Users** in the left navigation pane, then click **Create user**.

    ![IAM Users page with Create user button highlighted](/assets/operation_center/asset_connectors/device/aws/aws_create_user_2.png)

3. Enter a username for the IAM user (e.g., `sekoia-ec2-reader`) and click **Next**.

    ![Create user form with username field](/assets/operation_center/asset_connectors/device/aws/aws_create_user_3.png)

4. In the **Set permissions** step, select **Attach policies directly** and search for the following policies:

      - `AmazonEC2ReadOnlyAccess` (for basic EC2 read access)
      - `AmazonEC2FullAccess` (if you need full EC2 access)
   
    !!! Warning

        - Granting `AmazonEC2FullAccess` provides extensive permissions that may pose security risks. Only use it if absolutely necessary and ensure to follow the principle of least privilege.
        - Do not attach both policies to the same user, as this could lead to permission conflicts.

    ![Policy attachment page with EC2 policies selected](/assets/operation_center/asset_connectors/device/aws/aws_create_user_4.png)

5. Click **Next** to review, then click **Create user**.

### How to generate access keys

After creating the IAM user, you need to generate access keys for programmatic access:

1. Click on the created user name to open the user details page.

2. Click the **Create an access key** button.

    ![Access keys section with Create access key button](/assets/operation_center/asset_connectors/device/aws/aws_create_user_5.png)

3. Select **Application running outside AWS** as the use case and click **Next**.

    ![Access key use case selection](/assets/operation_center/asset_connectors/device/aws/aws_create_user_6.png)

4. Add a description tag (optional) and click **Create access key**.

    ![Access key creation with description tag](/assets/operation_center/asset_connectors/device/aws/aws_create_user_7.png)

5. Copy the **Access key ID** and **Secret access key** to a safe location. You'll need these credentials to configure the connector in Sekoia.io.

    ![Access key credentials display](/assets/operation_center/asset_connectors/device/aws/aws_create_user_8.png)

!!! Warning
    - The secret access key is only shown when you create it. If you lose it, you must create a new access key.
    - Store these credentials securely and never share them publicly.
    - Consider rotating access keys regularly for security best practices.

### Required IAM permissions

The IAM user must have the following permissions to successfully fetch EC2 devices:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeImages",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeVolumes",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeTags"
            ],
            "Resource": "*"
        }
    ]
}
```

### Supported AWS regions

The AWS EC2 connector supports all AWS regions where EC2 is available. Common regions include:

- **US East (N. Virginia)**: `us-east-1`
- **US West (Oregon)**: `us-west-2`
- **Europe (Ireland)**: `eu-west-1`
- **Europe (London)**: `eu-west-2`
- **Asia Pacific (Tokyo)**: `ap-northeast-1`
- **Asia Pacific (Singapore)**: `ap-southeast-1`

For a complete list of available regions, refer to the [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) documentation.

### Create your asset

To start getting your AWS EC2 instances into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/device/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![New connector button highlighted](/assets/operation_center/asset_connectors/device/common/create_asset_connector_1.png)

3. Choose **AWS devices**, give it a name, and fill the required fields:

    ![AWS EC2 Device connector configuration form](/assets/operation_center/asset_connectors/device/aws/create_aws_asset_connector_1.png)

4. Enter the following information:
   - **Access Key ID**: The access key ID from your IAM user
   - **Secret Access Key**: The secret access key from your IAM user
   - **Region**: The AWS region where your EC2 instances are located (e.g., `us-east-1`)

5. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/device/aws/create_aws_asset_connector_2.png)

6. Click the **Create asset connector** button.

## Information Collected

The AWS EC2 asset connector fetches comprehensive EC2 instance information from AWS and transforms it into the OCSF (Open Cybersecurity Schema Framework) Device Inventory format for standardized security monitoring and asset management.

### Data Mapping Table

The following table shows how AWS EC2 instance data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type |
|--------------|-----------------|-------------|-----------|
| `InstanceId` | `device.uid` | EC2 instance unique identifier | String |
| `PublicDnsName` / `PrivateDnsName` | `device.hostname` | Public or private DNS name (fallback to instance ID) | String |
| `Tags[Name]` | `device.name` | Instance name from Name tag | String |
| `PlatformDetails` | `device.os.name` | Operating system name (Windows, Linux, MacOS) | String |
| `PlatformDetails` | `device.os.type` | Operating system type enum | String (Enum) |
| `PlatformDetails` | `device.os.type_id` | Operating system type ID (100=Windows, 200=Linux, 300=MacOS, 0=Unknown) | Integer (Enum) |
| `NetworkInterfaces[].NetworkInterfaceId` | `device.network_interfaces[].uid` | Network interface unique identifier | String |
| `NetworkInterfaces[].Description` | `device.network_interfaces[].name` | Network interface description | String |
| `NetworkInterfaces[].MacAddress` | `device.network_interfaces[].mac` | MAC address | String |
| `NetworkInterfaces[].PrivateIpAddress` | `device.network_interfaces[].ip` | Private IP address | String |
| `NetworkInterfaces[].PrivateDnsName` | `device.network_interfaces[].hostname` | Private DNS name | String |
| `NetworkInterfaces[]` | `device.network_interfaces[].type` | Interface type (always "Wired") | String (Enum) |
| `NetworkInterfaces[]` | `device.network_interfaces[].type_id` | Interface type ID (always 1 for Wired) | Integer (Enum) |
| `SecurityGroups[].GroupId` | `device.groups[].uid` | Security group ID | String |
| `SecurityGroups[].GroupName` | `device.groups[].name` | Security group name | String |
| `PublicIpAddress` / `PrivateIpAddress` | `device.ip` | Primary IP address (public preferred, fallback to private) | String |
| `Placement.AvailabilityZone` | `device.region` | AWS availability zone | String |
| `SubnetId` | `device.subnet` | Subnet ID | String |
| `VpcId` | `device.domain` | VPC ID (mapped as domain) | String |
| `Hypervisor` | `device.hypervisor` | Hypervisor type (e.g., xen, nitro) | String |
| Static value | `device.vendor_name` | Always "Amazon Web Services" | String |
| `InstanceType` | `device.model` | Instance type (e.g., t2.micro, m5.large) | String |
| `LaunchTime` | `device.boot_time` | Instance launch time (ISO format) | String (ISO 8601) |
| `BlockDeviceMappings[0].Ebs.AttachTime` / `LaunchTime` | `device.created_time` | Creation timestamp (Unix epoch) | Integer (timestamp) |
| `IamInstanceProfile` | `device.is_managed` | Whether instance has IAM role (managed) | Boolean |
| `Tags[aws:autoscaling:groupName]` | `device.autoscale_uid` | Auto Scaling group name | String |
| `ImageId` + `State.Name` | `device.desc` | Description with AMI ID and state | String |
| `Reservations[].OwnerId` | `device.org.uid` | AWS Account ID | String |
| `Reservations[].OwnerId` | `device.org.name` | Organization name (e.g., "AWS Account 123456789012") | String |
| Static value | `device.type` | Always "Server" | String (Enum) |
| Static value | `device.type_id` | Always 1 (Server) | Integer (Enum) |
| `LaunchTime` / `BlockDeviceMappings[0].Ebs.AttachTime` | `time` | Event timestamp for OCSF model (Unix epoch) | Integer (timestamp) |

### OCSF Model Structure

The connector generates OCSF Device Inventory events (class UID 5001) with the following structure:

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
  "time": "<unix_timestamp>",
  "metadata": {
    "product": {
      "name": "AWS EC2",
      "version": "<version>"
    },
    "version": "<ocsf_version>"
  },
  "device": {
    "type": "Server",
    "type_id": 1,
    "uid": "<instance_id>",
    "hostname": "<public_or_private_dns>",
    "name": "<name_from_tags>",
    "ip": "<public_or_private_ip>",
    "os": {
      "name": "Linux|Windows|MacOS|Unknown",
      "type": "Linux|Windows|macOS|Unknown",
      "type_id": 100|200|300|0
    },
    "network_interfaces": [
      {
        "uid": "<network_interface_id>",
        "name": "<interface_description>",
        "mac": "<mac_address>",
        "ip": "<private_ip_address>",
        "hostname": "<private_dns_name>",
        "type": "Wired",
        "type_id": 1
      }
    ],
    "groups": [
      {
        "uid": "<security_group_id>",
        "name": "<security_group_name>"
      }
    ],
    "region": "<availability_zone>",
    "subnet": "<subnet_id>",
    "domain": "<vpc_id>",
    "hypervisor": "<hypervisor_type>",
    "vendor_name": "Amazon Web Services",
    "model": "<instance_type>",
    "boot_time": "<launch_time_iso>",
    "created_time": <unix_timestamp>,
    "is_managed": true|false,
    "autoscale_uid": "<autoscaling_group_name>",
    "desc": "AMI: <image_id>, State: <state>",
    "org": {
      "name": "AWS Account <account_id>",
      "uid": "<account_id>"
    }
  }
}
```

### Enrichment Objects

The connector performs several enrichment operations to provide comprehensive device context:

#### Network Interface Enrichment
- **Source**: `NetworkInterfaces[]` array from EC2 instance data
- **Enrichment**: Extracts detailed network interface information
- **Fields added**: 
  - `device.network_interfaces[]` with ID, description, MAC address, private IP, private DNS
  - Always sets type as "Wired" (type_id: 1) for EC2 instances
- **Special handling**: Continues on individual interface extraction errors

#### Security Group Enrichment
- **Source**: `SecurityGroups[]` array from EC2 instance data
- **Enrichment**: Maps EC2 security groups to OCSF Group objects
- **Fields added**: `device.groups[]` with security group ID and name
- **Purpose**: Tracks network access control and firewall rules

#### Operating System Detection
- **Source**: `PlatformDetails` field from EC2 instance
- **Enrichment**: Determines OS type from platform details string
- **Logic**: 
  - Searches for "windows" → Windows (type_id: 100)
  - Searches for "linux" or "unix" → Linux (type_id: 200)
  - Searches for "macos" or "mac" → MacOS (type_id: 300)
  - Otherwise → Unknown (type_id: 0)
- **Fields added**: `device.os.name`, `device.os.type`, `device.os.type_id`

#### Hostname Resolution
- **Source**: `PublicDnsName` and `PrivateDnsName` fields
- **Enrichment**: Determines the best hostname for the device
- **Priority**: 
  1. Public DNS name (if available)
  2. Private DNS name (if public not available)
  3. Instance ID (if neither DNS name is available)
- **Fields added**: `device.hostname`
- **Special handling**: Empty strings treated as None

#### Tag-Based Name Extraction
- **Source**: `Tags[]` array with Key-Value pairs
- **Enrichment**: Extracts the "Name" tag value
- **Fields added**: `device.name`
- **Purpose**: Provides human-readable instance names

#### Auto Scaling Group Detection
- **Source**: `Tags[]` array with Key-Value pairs
- **Enrichment**: Extracts the "aws:autoscaling:groupName" tag
- **Fields added**: `device.autoscale_uid`
- **Purpose**: Identifies instances managed by Auto Scaling

#### Organization Enrichment
- **Source**: `OwnerId` from Reservation data
- **Enrichment**: Creates organization object from AWS Account ID
- **Fields added**: 
  - `device.org.uid` (account ID)
  - `device.org.name` (formatted as "AWS Account <account_id>")

#### Management Status Detection
- **Source**: `IamInstanceProfile` field
- **Enrichment**: Determines if instance is managed based on IAM role presence
- **Logic**: Instance is considered "managed" if it has an IAM instance profile attached
- **Fields added**: `device.is_managed` (boolean)
- **Purpose**: Identifies instances with automated management capabilities

#### Primary IP Resolution
- **Source**: `PublicIpAddress` and `PrivateIpAddress` fields
- **Enrichment**: Determines the primary IP address
- **Priority**:
  1. Public IP address (if available)
  2. Private IP address (if public not available)
- **Fields added**: `device.ip`

#### Creation Time Resolution
- **Source**: `BlockDeviceMappings[0].Ebs.AttachTime` and `LaunchTime`
- **Enrichment**: Determines the most accurate creation timestamp
- **Priority**:
  1. EBS attachment time (if available)
  2. Launch time (as fallback)
- **Fields added**: `device.created_time` (Unix timestamp), `time` (event timestamp)
- **Special handling**: Ensures UTC timezone, converts to epoch timestamp

#### Description Generation
- **Source**: `ImageId` and `State.Name` fields
- **Enrichment**: Creates a descriptive string combining AMI ID and instance state
- **Format**: "AMI: <image_id>, State: <state>"
- **Fields added**: `device.desc`
- **Purpose**: Provides quick reference to instance image and current state


## Further Reading
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
- [AWS EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/)
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

