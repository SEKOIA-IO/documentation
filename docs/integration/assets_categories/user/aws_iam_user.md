uuid: e2a7c1b4-5d8f-4e3a-9c2b-7f1e6d8a3b2c
name: AWS users
type: asset

## Overview

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.

- **Vendor**: Amazon
- **Product**: AWS IAM
- **Supported environment**: Cloud

## Configure

### How to create an IAM account with proper permissions

To connect AWS IAM to Sekoia.io, you need to create an IAM user with the necessary permissions to access IAM users and groups. Follow these steps:

1. Sign in to the AWS Management Console and navigate to the IAM service.

    ![AWS Console IAM service selection](/assets/operation_center/asset_connectors/user/aws/aws_create_user_1.png)

2. Click **Users** in the left navigation pane, then click **Create user**.

    ![IAM Users page with Create user button highlighted](/assets/operation_center/asset_connectors/user/aws/aws_create_user_2.png)

3. Enter a username for the IAM user (e.g., `sekoia-iam-reader`) and click **Next**.

    ![Create user form with username field](/assets/operation_center/asset_connectors/user/aws/aws_create_user_9.png)

4. In the **Set permissions** step, select **Attach policies directly** and search for the following policies:

      - `IAMReadOnlyAccess` (recommended for ingestion; grants only read access to IAM resources)
      - `IAMFullAccess` (only if you require full IAM management capabilities)
   
    !!! Warning

        - Granting `IAMFullAccess` provides extensive permissions that may pose security risks. Only use it if absolutely necessary and ensure to follow the principle of least privilege.
        - Do not attach both policies to the same user, as this could lead to permission conflicts.

   ![Policy attachment page with IAM policies selected](/assets/operation_center/asset_connectors/user/aws/aws_create_user_10.png)

5. Click **Next** to review, then click **Create user**.

### How to generate access keys

After creating the IAM user, you need to generate access keys for programmatic access:

1. Click on the created user name to open the user details page.

2. Click the **Create an access key** button.

    ![Access keys section with Create access key button](/assets/operation_center/asset_connectors/user/aws/aws_create_user_5.png)

3. Select **Application running outside AWS** as the use case and click **Next**.

    ![Access key use case selection](/assets/operation_center/asset_connectors/user/aws/aws_create_user_6.png)

4. Add a description tag (optional) and click **Create access key**.

    ![Access key creation with description tag](/assets/operation_center/asset_connectors/user/aws/aws_create_user_7.png)

5. Copy the **Access key ID** and **Secret access key** to a safe location. You'll need these credentials to configure the connector in Sekoia.io.

    ![Access key credentials display](/assets/operation_center/asset_connectors/user/aws/aws_create_user_8.png)

!!! Warning
    - The secret access key is only shown when you create it. If you lose it, you must create a new access key.
    - Store these credentials securely and never share them publicly.
    - Consider rotating access keys regularly for security best practices.

### Required IAM permissions

The IAM user must have the following permissions to successfully fetch IAM users and groups:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:ListUsers",
                "iam:GetUser",
                "iam:ListGroups",
                "iam:GetGroup",
                "iam:ListGroupsForUser",
                "iam:ListUserPolicies",
                "iam:ListAttachedUserPolicies",
                "iam:GetUserPolicy",
                "iam:ListGroupPolicies",
                "iam:ListAttachedGroupPolicies",
                "iam:GetGroupPolicy",
                "iam:ListAccessKeys",
                "iam:ListSigningCertificates",
                "iam:ListSSHPublicKeys",
                "iam:ListServiceSpecificCredentials",
                "iam:ListMFADevices",
                "iam:GetLoginProfile",
                "iam:ListUserTags",
                "iam:ListGroupTags",
                "iam:GetAccountSummary"
            ],
            "Resource": "*"
        }
    ]
}
```

### Supported AWS regions

The AWS IAM connector supports all AWS regions where IAM is available. IAM is a global service, but you can specify any AWS region for the API calls. Common regions include:

- **US East (N. Virginia)**: `us-east-1`
- **US West (Oregon)**: `us-west-2`
- **Europe (Ireland)**: `eu-west-1`
- **Europe (London)**: `eu-west-2`
- **Asia Pacific (Tokyo)**: `ap-northeast-1`
- **Asia Pacific (Singapore)**: `ap-southeast-1`

For a complete list of available regions, refer to the [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) documentation.

### Create your asset

To start getting your AWS IAM users into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![New connector button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_1.png)

3. Choose **AWS users**, give it a name, and fill the required fields:

    ![AWS IAM User connector configuration form](/assets/operation_center/asset_connectors/user/aws/create_aws_asset_connector_3.png)

4. Enter the following information:

     - **Access Key ID**: The access key ID from your IAM user
     - **Secret Access Key**: The secret access key from your IAM user
     - **Region**: The AWS region for API calls (e.g., `us-east-1`)

5. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/user/aws/create_aws_asset_connector_4.png)

6. Click the **Create asset connector** button.

## Information Collected

The AWS IAM asset connector fetches comprehensive user information from AWS IAM and transforms it into the OCSF (Open Cybersecurity Schema Framework) User Inventory format for standardized security monitoring and asset management.

### Data Mapping Table

The following table shows how AWS IAM user data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type |
|--------------|-----------------|-------------|-----------|
| `UserName` | `user.name` | The IAM user's username | String |
| `Arn` | `user.uid` | AWS Resource Name (unique identifier) | String |
| `UserId` | `user.account.uid_alt` | AWS internal user ID | String |
| `CreateDate` | `time` | User creation timestamp (Unix epoch) | Integer (timestamp) |
| `UserName` | `user.account.name` | Account name (same as username) | String |
| `Arn` | `user.account.uid` | Account unique identifier (ARN) | String |
| `Groups[].GroupName` | `user.groups[].name` | Name of IAM group | String |
| `Groups[].Arn` | `user.groups[].uid` | Group unique identifier (ARN) | String |
| `Groups[].Policies` | `user.groups[].privileges[]` | List of policy names attached to group | Array[String] |
| `MFADevices[]` | `user.has_mfa` | Whether user has MFA enabled | Boolean |
| `Arn` (extracted) | `user.org.uid` | AWS Account ID extracted from ARN | String |
| `Arn` (extracted) | `user.org.name` | Organization name (e.g., "AWS Account 123456789012") | String |
| Admin policy check | `user.type` | User type: "Admin" or "User" | String (Enum) |
| Admin policy check | `user.type_id` | User type ID: 2 (Admin) or 1 (User) | Integer (Enum) |

### OCSF Model Structure

The connector generates OCSF User Inventory events (class UID 5003) with the following structure:

```json
{
  "activity_id": 2,
  "activity_name": "Collect",
  "category_name": "Discovery",
  "category_uid": 5,
  "class_name": "User Inventory",
  "class_uid": 5003,
  "type_name": "User Inventory Info: Collect",
  "type_uid": 500301,
  "time": "<unix_timestamp>",
  "metadata": {
    "product": {
      "name": "AWS IAM Asset Connector",
      "version": "<version>"
    },
    "version": "<ocsf_version>"
  },
  "user": {
    "name": "<username>",
    "uid": "<user_arn>",
    "type": "User|Admin",
    "type_id": 1|2,
    "has_mfa": true|false,
    "account": {
      "name": "<username>",
      "type": "AWS Account",
      "type_id": 10,
      "uid": "<user_arn>",
      "uid_alt": "<user_id>"
    },
    "groups": [
      {
        "name": "<group_name>",
        "uid": "<group_arn>",
        "privileges": ["<policy_name>", ...]
      }
    ],
    "org": {
      "name": "AWS Account <account_id>",
      "uid": "<account_id>"
    }
  }
}
```

### API Endpoints Used

The connector uses the following AWS IAM API endpoints to collect user information:

| API Endpoint | Purpose | Pagination | Error Handling |
|--------------|---------|------------|----------------|
| `list_users` | Retrieve all IAM users in the account | Yes (paginated) | ClientError, BotoCoreError, NoCredentialsError |
| `list_groups_for_user` | Get groups for a specific user | Yes (paginated) | ClientError, BotoCoreError |
| `list_attached_group_policies` | Get policies attached to a group | Yes (paginated) | ClientError, BotoCoreError |
| `list_mfa_devices` | Check if user has MFA devices configured | No | ClientError, BotoCoreError |

#### API Call Workflow

1. **Initial Collection**: The connector starts by calling `list_users` to retrieve all IAM users
2. **Per-User Enrichment**: For each user, the connector performs:
   - `list_groups_for_user` to get user's groups
   - For each group: `list_attached_group_policies` to get group privileges
   - `list_mfa_devices` to check MFA status
3. **Incremental Collection**: Uses checkpoint mechanism to track the most recent collection date
4. **Date Filtering**: Only collects users created after the last checkpoint date (incremental updates)

#### Performance Considerations

- All API calls use pagination to handle large datasets efficiently
- The connector implements error handling at multiple levels to continue collection even if individual API calls fail
- Checkpoint mechanism reduces redundant API calls by tracking already-processed users
- Batch processing yields users in pages for memory-efficient operation

## Further Reading
- [AWS IAM Documentation](https://docs.aws.amazon.com/iam/)
- [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
- [AWS IAM API Reference](https://docs.aws.amazon.com/IAM/latest/APIReference/)

