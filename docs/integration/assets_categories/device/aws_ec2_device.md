# aws\_ec2\_device

{% if visitor.claims.internal %}
uuid: e2a7c6b4-9f1d-4b8a-8c3e-2d5f7a1e4b9c name: AWS devices type: asset
{% endif %}

### Overview

Amazon Elastic Compute Cloud (EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers by providing a simple web service interface that allows you to obtain and configure capacity with minimal friction.

* **Vendor**: Amazon
* **Product**: AWS EC2
* **Supported environment**: Cloud

### Configure

#### How to create an IAM account with proper permissions

To connect AWS EC2 to Sekoia.io, you need to create an IAM user with the necessary permissions to access EC2 instances. Follow these steps:

1. Sign in to the AWS Management Console and navigate to the IAM service.
2. Click **Users** in the left navigation pane, then click **Create user**.
3. Enter a username for the IAM user (e.g., `sekoia-ec2-reader`) and click **Next**.
4. In the **Set permissions** step, select **Attach policies directly** and search for the following policies:
   * `AmazonEC2ReadOnlyAccess` (for basic EC2 read access)
   * `AmazonEC2FullAccess` (if you need full EC2 access)

{% hint style="warning" %}
* Granting `AmazonEC2FullAccess` provides extensive permissions that may pose security risks. Only use it if absolutely necessary and ensure to follow the principle of least privilege.
* Do not attach both policies to the same user, as this could lead to permission conflicts.
{% endhint %}

1. Click **Next** to review, then click **Create user**.

#### How to generate access keys

After creating the IAM user, you need to generate access keys for programmatic access:

1. Click on the created user name to open the user details page.
2. Click the **Create an access key** button.
3. Select **Application running outside AWS** as the use case and click **Next**.
4. Add a description tag (optional) and click **Create access key**.
5. Copy the **Access key ID** and **Secret access key** to a safe location. You'll need these credentials to configure the connector in Sekoia.io.

{% hint style="warning" %}
* The secret access key is only shown when you create it. If you lose it, you must create a new access key. - Store these credentials securely and never share them publicly. - Consider rotating access keys regularly for security best practices.
{% endhint %}

#### Required IAM permissions

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

#### Supported AWS regions

The AWS EC2 connector supports all AWS regions where EC2 is available. Common regions include:

* **US East (N. Virginia)**: `us-east-1`
* **US West (Oregon)**: `us-west-2`
* **Europe (Ireland)**: `eu-west-1`
* **Europe (London)**: `eu-west-2`
* **Asia Pacific (Tokyo)**: `ap-northeast-1`
* **Asia Pacific (Singapore)**: `ap-southeast-1`

For a complete list of available regions, refer to the [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) documentation.

#### Create your asset

To start getting your AWS EC2 instances into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.
2. Click the **+ New connector** button.
3. Choose **AWS devices**, give it a name, and fill the required fields:
4. Enter the following information:
   * **Access Key ID**: The access key ID from your IAM user
   * **Secret Access Key**: The secret access key from your IAM user
   * **Region**: The AWS region where your EC2 instances are located (e.g., `us-east-1`)
5. Test the connection by clicking the **Test connector** button.
6. Click the **Create asset connector** button.



{% include "../../.gitbook/includes/aws-device-shared-content.md" %}

{!\_shared\_content/operations\_center/integrations/generated\_assets\_documentation/aws\_device.md!}

### Further Reading

* [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
* [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
* [AWS EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/)
* [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
