## OCSF Mapping for AWS Users


**OCSF Class:** `User Inventory Info`



**Class UID:** `5003`



**OCSF Version:** `1.6.0`


## Information Collected

The AWS Users fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### AWS IAM Programmatic User
IAM user with programmatic access (API keys) but no console access

```json
{
  "UserId": "AIDAI23HZ27SI6FQMGNHQ",
  "UserName": "lambda-execution-role",
  "Arn": "arn:aws:iam::123456789012:user/service-role/lambda-execution-role",
  "Path": "/service-role/",
  "CreateDate": "2020-06-04T10:00:00Z",
  "PasswordLastUsed": null,
  "AccessKeys": [
    {
      "AccessKeyId": "AKIA123456789EXAMPLE",
      "Status": "Active",
      "CreateDate": "2020-06-04T10:00:00Z"
    },
    {
      "AccessKeyId": "AKIA987654321EXAMPLE",
      "Status": "Active",
      "CreateDate": "2021-03-15T14:30:00Z"
    }
  ],
  "MFADevices": [],
  "ConsoleAccessEnabled": false,
  "Tags": [
    {
      "Key": "Purpose",
      "Value": "Lambda Execution"
    },
    {
      "Key": "Environment",
      "Value": "Production"
    }
  ]
}

```

#### AWS IAM Console User
IAM user with console access and MFA enabled

```json
{
  "UserId": "AIDACKCEVSQ6C2EXAMPLE",
  "UserName": "aws-developer-team",
  "Arn": "arn:aws:iam::123456789012:user/engineering/aws-developer-team",
  "Path": "/engineering/",
  "CreateDate": "2020-06-04T10:00:00Z",
  "PasswordLastUsed": "2025-08-26T09:30:00Z",
  "AccessKeys": [
    {
      "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
      "Status": "Active",
      "CreateDate": "2025-01-10T11:00:00Z"
    }
  ],
  "MFADevices": [
    {
      "DeviceName": "arn:aws:iam::123456789012:mfa/aws-developer-team",
      "SerialNumber": "arn:aws:iam::123456789012:mfa/aws-developer-team",
      "EnableDate": "2020-07-15T14:00:00Z"
    }
  ],
  "ConsoleAccessEnabled": true,
  "Tags": [
    {
      "Key": "Department",
      "Value": "Engineering"
    },
    {
      "Key": "Environment",
      "Value": "Development"
    }
  ]
}

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic |
|--------------|-----------------|-------------|-----------|-------|
| `static: 2` | `activity_id` | OCSF activity ID for inventory collection | `integer` | Always 2 for 'Collect' activity |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | Always 'Collect' |
| `static: Discovery` | `category_name` | OCSF category name | `string` | Always 'Discovery' |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | Always 5 for Discovery category |
| `static: User Inventory Info` | `class_name` | OCSF class name | `string` | Always 'User Inventory Info' |
| `static: 5003` | `class_uid` | OCSF class UID | `integer` | Always 5003 for User Inventory Info |
| `static: 500301` | `type_uid` | OCSF type UID | `integer` | Always 500301 for User Inventory Info: Collect type |
| `static: 'User Inventory Info: Collect'` | `type_name` | OCSF type name | `string` | Always 'User Inventory Info: Collect' |
| `CreateDate` | `time` | OCSF event timestamp (user discovery time) | `timestamp` | Convert ISO 8601 to Unix epoch for OCSF event timestamp |
| `static: AWS IAM` | `metadata.product.name` | Source product name | `string` | Always 'AWS IAM' |
| `static: N/A` | `metadata.product.version` | Source product version | `string` | There's no specific version for AWS IAM as it's a managed service; using 'N/A' |
| `static: 1.6.0` | `metadata.version` | OCSF schema version | `string` | Fixed OCSF schema version |
| `UserName` | `user.name` | AWS IAM username | `string` | Direct mapping of IAM username |
| `Arn` | `user.uid` | AWS IAM user unique identifier | `string` | Direct mapping of AWS IAM user ID |
| `Arn` | `user.groups[].uid` | Group unique identifier (using ARN for uniqueness across accounts) | `string` | Direct mapping of AWS ARN for group unique identifier |
| `GroupName` | `user.groups[].name` |  | `string` | Direct mapping of IAM group name |
| `PolicyName` | `user.groups[].privileges[]` | Privileges derived from IAM policies | `Array of strings` | This field captures the names of policies attached to the user or their groups. |
| `MFADevices` | `user.has_mfa` | Whether MFA is enabled for user account | `boolean` | true if any MFA device is registered, false otherwise |
| `UserName` | `user.account.name` | Account username | `string` | Direct mapping of IAM username |
| `Arn` | `user.account.uid` | AWS IAM user ARN (Amazon Resource Name) | `string` | Direct mapping of AWS ARN |
| `UserId` | `user.account.uid_alt` | AWS IAM UserId (alternative unique identifier) | `string` | Direct mapping of IAM UserId for alternative unique identifier |
| `static: AWS IAM` | `user.account.type` | Account type identifier | `string` | Always 'AWS IAM' |
| `static: 40` | `user.account.type_id` | OCSF account type ID | `integer` | Always 40 for AWS IAM account type |




### OCSF Model Structure

#### User Inventory Info: Collect
Transformed IAM user to OCSF User Inventory Info event

```json
{
  "activity_id": 2,
  "activity_name": "Collect",
  "category_name": "Discovery",
  "category_uid": 5,
  "class_name": "User Inventory Info",
  "class_uid": 5003,
  "type_name": "User Inventory Info: Collect",
  "type_uid": 500302,
  "severity": "Informational",
  "severity_id": 1,
  "time": 1591275600,
  "metadata": {
    "product": {
      "name": "AWS IAM",
      "version": "1.6.0"
    },
    "version": "1.6.0"
  },
  "user": {
    "uid": "AIDAI23HZ27SI6FQMGNHQ",
    "name": "lambda-execution-role",
    "full_name": "lambda-execution-role",
    "path": "/service-role/",
    "is_console_user": false,
    "has_mfa": false,
    "access_keys_count": 2,
    "password_last_used_time": null,
    "created_time": 1591275600,
    "tags": {
      "Purpose": "Lambda Execution",
      "Environment": "Production"
    },
    "account": {
      "uid": "arn:aws:iam::123456789012:user/service-role/lambda-execution-role",
      "name": "lambda-execution-role",
      "type": "AWS IAM",
      "type_id": 40
    }
  }
}

```


