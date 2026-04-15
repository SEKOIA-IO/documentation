This section will guide you to configure the forwarding of Cisco Umbrella logs to Sekoia.io by means of AWS S3 buckets.

### Prerequisites

- Administrator access to the Cisco Umbrella console
- Access to Sekoia.io Intakes and Playbook pages with write permissions
- Administrator access to the [Amazon console](https://console.aws.amazon.com) with permissions to create and manage S3 buckets, SQS queues, and IAM identities

### AWS Authentication Setup

Sekoia.io supports two authentication methods to access your AWS resources. Choose the one that best fits your security requirements:

| Method | Summary | When to use |
|--------|---------|-------------|
| **IAM Role with OIDC** *(Recommended)* | Sekoia.io assumes an IAM Role using short-lived credentials issued via OpenID Connect (OIDC). No long-lived access keys are stored. | Preferred for new setups and security-conscious environments |
| **Static Access Keys** | A dedicated IAM user authenticates with a static access key and secret. | Existing setups or environments where OIDC federation is not available |

=== "IAM Role with OIDC (Recommended)"

    This method uses [OpenID Connect (OIDC) federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) so that Sekoia.io can assume an AWS IAM Role and obtain short-lived credentials automatically. No long-lived access keys are stored in Sekoia.io.

    **Step 1 — Register Sekoia.io as an OIDC Identity Provider in AWS IAM**

    1. Open the [IAM console](https://console.aws.amazon.com/iam/) and navigate to **Identity providers**.
    2. Click **Add provider** and select **OpenID Connect**.
    3. Fill in the form:
        - **Provider URL**: `https://app.sekoia.io/api/v1/symphony/oidc`
        - **Audience**: `sts.amazonaws.com`
    4. Click **Add provider** to confirm.

    Once created, note the **Provider ARN** (e.g. `arn:aws:iam::XXXXXXXXXXXX:oidc-provider/app.sekoia.io/api/v1/symphony/oidc`). You will need it in the steps below.

    **Step 2 — Create an IAM Role for Sekoia.io**

    1. In the IAM console, navigate to **Roles** and click **Create role**.
    2. Select **Web identity** as the trusted entity type.
    3. Choose the `app.sekoia.io/api/v1/symphony/oidc` identity provider you just registered and set the audience to `sts.amazonaws.com`.
    4. Proceed to the **Trust policy** and replace its content with the following, substituting your AWS account ID, community UUID, and module configuration UUID:

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

<!-- !!! Info
    

    You can find your **Community UUID** and **Module Configuration UUID** in the Sekoia.io platform under the connector's configuration page. -->

    **Step 3 — Attach a permission policy to the role**

    Attach an inline or managed policy granting the role read access to the SQS queue and S3 bucket:

    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:ListBucket"
                ],
                "Resource": "arn:aws:s3:::NAME_HERE"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "sqs:GetQueueUrl",
                    "sqs:ReceiveMessage",
                    "sqs:DeleteMessage",
                    "sqs:GetQueueAttributes"
                ],
                "Resource": "arn:aws:sqs:REGION_HERE:XXXXXXXXXXXX:NAME_HERE"
            }
        ]
    }
    ```

    **Step 4 — Copy the Role ARN**

    After creating the role, note its **ARN** (e.g. `arn:aws:iam::XXXXXXXXXXXX:role/ROLE_NAME`). You will need it when configuring the connector in Sekoia.io.

    **Step 5 — Configure the Sekoia.io AWS module**

    In the Sekoia.io connector configuration, set the following fields:

    - **AWS Region** (`aws_region_name`): the AWS region where your resources are deployed (e.g. `eu-west-1`)
    - **AWS Role ARN** (`aws_role_arn`): the ARN of the role you created above

    Leave the **Access Key** and **Secret Access Key** fields empty — they are not used with this method.

=== "Static Access Keys"

    This method authenticates using a dedicated IAM user with a static access key and secret access key stored in Sekoia.io.

    **Step 1 — Create a dedicated IAM user**

    Create a dedicated IAM user in the [IAM console](https://console.aws.amazon.com/iam/) and generate programmatic access credentials (access key ID and secret access key) for that user.

    **Step 2 — Attach a resource-based policy to your SQS queue and S3 bucket**

    Ensure that the IAM user has the following permissions on your SQS queue and S3 bucket:

    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "sqs:ReceiveMessage", "sqs:DeleteMessage", "sqs:GetQueueUrl"
                ],
                "Principal": {
                    "AWS": "arn:aws:iam::XXXXXXXXXXXX:user/USERNAME_HERE"
                },
                "Resource": "arn:aws:sqs:REGION_HERE:XXXXXXXXXXXX:NAME_HERE"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject"
                ],
                "Principal": {
                    "AWS": "arn:aws:iam::XXXXXXXXXXXX:user/USERNAME_HERE"
                },
                "Resource": "arn:aws:s3:::NAME_HERE/*"
            }
        ]
    }
    ```

    **Step 3 — Configure the Sekoia.io AWS module**

    In the Sekoia.io connector configuration, set the following fields:

    - **AWS Region** (`aws_region_name`): the AWS region where your resources are deployed (e.g. `eu-west-1`)
    - **Access Key** (`aws_access_key`): the access key ID of your IAM user
    - **Secret Access Key** (`aws_secret_access_key`): the secret access key of your IAM user

    Leave the **AWS Role ARN** field empty — it is not used with this method.

### Create an AWS S3 Bucket

To create a new AWS S3 Bucket, please refer to [this guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).

1. On the AWS S3, go to `Buckets` and select our bucket.
2. Select `Permissions` tab and go to `Bucket Policy` section
3. Click `Edit` and paste [the JSON Bucket policy from Cisco Umbrella](https://docs.umbrella.com/deployment-umbrella/docs/setting-up-an-amazon-s3-bucket#json-bucket-policy)
4. In the Policy, replace the `bucketname` placeholde by the name of our bucket.
5. Click `Save changes`.

!!! Important
    Keep in mind to conserve the `/*` when defining in the policy.

### Configure Cisco Umbrella

1. Log on the Cisco Umbrella console
2. Go to `Admin` > `Log Management`
3. In the `Amazon S3` section, select `Use your company-managed Amazon S3 bucket`
4. In `Amazon S3 bucket`, type the name of your bucket and click `Verify`.

5. On your AWS console, go in your bucket.
6. In the `Objects` tab, click on `README_FROM_UMBRELLA.txt` then click on `Open`
7. Copy the token from the readme
8. On the Cisco Umbrella console, in the field `Token Number`, paste the token and click `Save`

!!! Note
    After clicking `Verify`, the message `Great! We successfully verified your Amazon S3 bucket` must be displayed

!!! Note
    After clicking `Save`, the message `We’re sending data to your S3 storage` must be displayed

!!! Important
    According to the type of the logs, the objects will be prefixed with `dnslogs/` for DNS logs, `proxylogs` for proxy logs, `iplogs` for ip logs, ...

### Create a SQS queue

The collect will rely on S3 Event Notifications (SQS) to get new S3 objects.

1. Create a queue in the SQS service by following [this guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html)
2. In the Access Policy step, choose the advanced configuration and adapt this configuration sample with your own SQS Amazon Resource Name (ARN) (the main change is the Service directive allowing S3 bucket access):
```json
{
  "Version": "2008-10-17",
  "Id": "__default_policy_ID",
  "Statement": [
    {
      "Sid": "__owner_statement",
      "Effect": "Allow",
      "Principal": {
	"Service": "s3.amazonaws.com"
      },
      "Action": "SQS:SendMessage",
      "Resource": "arn:aws:sqs:XXX:XXX"
    }
  ]
}
```

!!! Important
    Keep in mind that you have to create the SQS queue in the same region as the S3 bucket you want to watch.
