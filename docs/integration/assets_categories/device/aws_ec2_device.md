uuid: e2a7c6b4-9f1d-4b8a-8c3e-2d5f7a1e4b9c
name: AWS devices
type: asset

## Overview

Amazon Elastic Compute Cloud (EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers by providing a simple web service interface that allows you to obtain and configure capacity with minimal friction.

- **Vendor**: Amazon
- **Product**: AWS EC2
- **Supported environment**: Cloud

## Configure

Sekoia.io supports two authentication methods to access your AWS resources. Choose the one that best fits your security requirements:

| Method | Summary | When to use |
|--------|---------|-------------|
| **IAM Role with OIDC** *(Recommended)* | Sekoia.io assumes an IAM Role using short-lived credentials issued via OpenID Connect (OIDC). No long-lived access keys are stored. | Preferred for new setups and security-conscious environments |
| **Static Access Keys** | A dedicated IAM user authenticates with a static access key and secret. | Existing setups or environments where OIDC federation is not available |

=== "IAM Role with OIDC (Recommended)"

    **Step 1 — Register Sekoia.io as an OIDC Identity Provider in AWS IAM**

    1. Open the [IAM console](https://console.aws.amazon.com/iam/) and navigate to **Identity providers**.
    2. Click **Add provider** and select **OpenID Connect**.
    3. Fill in the form:
        - **Provider URL**: `https://app.sekoia.io/api/v1/symphony/oidc`
        - **Audience**: `sts.amazonaws.com`
    4. Click **Add provider** to confirm.

    Once created, note the **Provider ARN** (e.g. `arn:aws:iam::XXXXXXXXXXXX:oidc-provider/app.sekoia.io/api/v1/symphony/oidc`).

    **Step 2 — Create an IAM Role for Sekoia.io**

    1. In the IAM console, navigate to **Roles** and click **Create role**.
    2. Select **Web identity** as the trusted entity type.
    3. Choose the `app.sekoia.io/api/v1/symphony/oidc` identity provider and set the audience to `sts.amazonaws.com`.
    4. Replace the trust policy with the following, substituting your AWS account ID and community/connector UUIDs:

        ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Federated": "arn:aws:iam::XXXXXXXXXXXX:oidc-provider/app.sekoia.io/api/v1/symphony/oidc"
                    },
                    "Action": "sts:AssumeRoleWithWebIdentity",
                    "Condition": {
                        "StringEquals": {
                            "app.sekoia.io/api/v1/symphony/oidc:aud": "sts.amazonaws.com"
                        },
                        "StringLike": {
                            "app.sekoia.io/api/v1/symphony/oidc:sub": "community:<COMMUNITY_UUID>:modconf:<MODULE_CONFIGURATION_UUID>"
                        }
                    }
                }
            ]
        }
        ```

    5. Attach the permissions from the [Required IAM permissions](#required-iam-permissions) section to the role.
    6. Note the **Role ARN** (e.g. `arn:aws:iam::XXXXXXXXXXXX:role/ROLE_NAME`). You will need it when configuring the connector in Sekoia.io.

=== "Static Access Keys"

    **How to create an IAM user with proper permissions**

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

    **How to generate access keys**

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

Both the IAM Role (OIDC) and IAM user (static keys) must have the following permissions to successfully fetch EC2 devices:

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

    - **Region**: The AWS region where your EC2 instances are located (e.g., `us-east-1`)
    - For **OIDC (Recommended)**: set the **Role ARN** to the ARN of the role you created
    - For **Static Access Keys**: set the **Access Key ID** and **Secret Access Key** from your IAM user

5. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/device/aws/create_aws_asset_connector_2.png)

6. Click the **Create asset connector** button.

{!_shared_content/operations_center/integrations/generated_assets_documentation/aws_device.md!}

## Further Reading
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
- [AWS EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/)
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

