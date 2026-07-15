This section will guide you through configuring Cisco Secure Access to forward logs to Sekoia.io using an Amazon S3 bucket, either managed by Cisco or owned by you.

### Prerequisites

- Full Admin user role in Cisco Secure Access. For more information, see the [Manage Accounts](https://securitydocs.cisco.com/docs/csa/olh/118836.dita) documentation.
- Access to Sekoia.io Intakes and Playbook pages with write permissions.
- If you plan to use your own S3 bucket, administrator access to the [Amazon console](https://console.aws.amazon.com) with permissions to create and manage S3 buckets, SQS queues, and IAM identities.

### Step 1 — Configure the S3 Bucket

Cisco Secure Access can export your logs either to a Cisco-managed Amazon S3 bucket, or to an Amazon S3 bucket that you own and manage yourself.

=== "Cisco-Managed S3 Bucket (Recommended)"

    Cisco configures all managed buckets to use Amazon Server-Side Encryption with S3-Managed Keys (SSE-S3, AES-256). Access is provided via AWS IAM credentials.

    1. In the Cisco Secure Access dashboard, navigate to `Admin > Log Management`.
    2. Click `Set up cloud storage` and select **Cisco**.
    3. Select a **Region** — choose the region closest to you to minimize latency when downloading logs.

        !!! Warning
            The selected region cannot be changed later without deleting your current settings and starting over. Not all AWS regions are available.

    4. Select a **Retention Duration** — choose 7, 14, or 30 days.

        !!! Note
            Beyond the selected time period, all data is purged and cannot be retrieved. A shorter duration is recommended if your ingestion cycle is frequent.

    5. Click `Save`. Cisco Secure Access activates log export to the S3 bucket. When activation is complete, the **Amazon S3 Summary** page appears.

    6. **Copy the Access Key and Secret Key** and store them in a safe place.

        !!! Warning
            The Access Key and Secret Key are displayed only once. If you lose them, you must regenerate them by rotating the keys in Cisco Secure Access.

    7. Click `Done`.

=== "Your Own S3 Bucket"

    Cisco Secure Access can also export logs to an Amazon S3 bucket that you own and manage. For more information, see the [Enable Logging to Your Own S3 Bucket](https://securitydocs.cisco.com/docs/csa/olh/121203.dita) and [Configure Your Own S3 Bucket](https://securitydocs.cisco.com/docs/csa/olh/121228.dita) Cisco documentation.

    **Create the S3 bucket**

    1. Create a bucket in Amazon S3 to store your logs. For more information, see [Amazon's S3 documentation](https://aws.amazon.com/documentation/s3/?id=docs_gateway).

        !!! Important
            Periods (`.`) in the S3 bucket name and Object Lock on the S3 bucket are not supported.

    2. On the AWS console, go to your bucket, select the `Permissions` tab, and edit the `Bucket Policy`.
    3. Paste the following JSON policy, substituting `bucketname` with the name of your bucket, then click `Save changes`:

        ```json
        {
          "Version": "2008-10-17",
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::568526795995:user/logs"
              },
              "Action": "s3:PutObject",
              "Resource": "arn:aws:s3:::bucketname/*"
            },
            {
              "Sid": "",
              "Effect": "Deny",
              "Principal": {
                "AWS": "arn:aws:iam::568526795995:user/logs"
              },
              "Action": "s3:GetObject",
              "Resource": "arn:aws:s3:::bucketname/*"
            },
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::568526795995:user/logs"
              },
              "Action": "s3:GetBucketLocation",
              "Resource": "arn:aws:s3:::bucketname"
            },
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::568526795995:user/logs"
              },
              "Action": "s3:ListBucket",
              "Resource": "arn:aws:s3:::bucketname"
            }
          ]
        }
        ```

    **Configure Cisco Secure Access**

    1. In the Cisco Secure Access dashboard, navigate to `Admin > Log Management > Set up cloud storage` and click on the **Amazon** card.
    2. In the **Amazon** field, type or paste the exact name of the bucket you created and click `Verify`. Secure Access verifies your bucket, connects to it, and saves a `README_FROM_UMBRELLA.txt` file to your bucket.
    3. On the AWS console, open your bucket, open the `README_FROM_UMBRELLA.txt` file, and copy the token listed in it.
    4. Back in Cisco Secure Access, paste the token in the **Token Number** field and click `Save`.
    5. A summary page shows you the bucket name. Click `Done`.

        !!! Note
            A pop-up window appears when verification is successful, confirming that your Amazon S3 bucket is now connected.

    **Create a SQS queue**

    Since you own and manage this bucket, the connector relies on S3 Event Notifications (SQS) to get new S3 objects.

    1. Create a queue in the SQS service by following [this guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html).
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

    3. Configure an [S3 Event Notification](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html) on your bucket for object creation events, using the SQS queue you just created as the destination.

        !!! Important
            Keep in mind that you have to create the SQS queue in the same region as the S3 bucket you want to watch.

    **Set up AWS authentication**

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

### Step 2 — Create the Intake

{!_shared_content/integration/intake_configuration.md!}

### Step 3 — Configure the Connector

{!_shared_content/integration/connector_configuration.md!}

=== "Cisco-Managed S3 Bucket"

    When selecting the trigger, choose **Fetch new logs on S3 (without SQS)**.

    Before configuring the connector, retrieve the **Data path** from the Cisco Secure Access **Amazon S3 Summary** page. It looks like this:

    ```text
    s3://cisco-managed-eu-central-1/1234567_a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0
    ```

    From this path:

    - the **bucket name** is the first segment after `s3://` — here, `cisco-managed-eu-central-1`.
    - the **base prefix** is the second segment — here, `1234567_a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0`. Cisco stores each log type in a dedicated subfolder under this prefix.

    In the connector configuration, set the following fields:

    - **AWS Region** (`aws_region_name`): the region you selected when configuring the S3 bucket in Cisco Secure Access (for example, `eu-central-1`).
    - **AWS Access Key** (`aws_access_key`): the Access Key copied from the Cisco Secure Access Amazon S3 Summary page.
    - **AWS Secret Access Key** (`aws_secret_access_key`): the Secret Key copied from the Cisco Secure Access Amazon S3 Summary page.
    - **Bucket** (`bucket`): the bucket name extracted from the Data path (for example, `cisco-managed-eu-central-1`).
    - **Prefix filter** (`prefix_filter`): the base prefix followed by the subfolder matching the log type you want to collect. Since the bucket holds several log types, this filter ensures the connector only ingests the logs for this intake.
    - **Intake key** (`intake_key`): the intake key generated when you created the intake in [Step 2](#step-2-create-the-intake).

    Cisco Secure Access stores each log type in a dedicated subfolder under the base prefix. Set the **Prefix filter** to `<base_prefix>/<subfolder>`, using the subfolder that matches the intake you are configuring:

    | Intake | Subfolder | Example prefix filter |
    | --- | --- | --- |
    | Cisco Secure Access - DNS | `dnslogs` | `1234567_a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0/dnslogs` |
    | Cisco Secure Access - Web | `proxylogs` | `1234567_a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0/proxylogs` |
    | Cisco Secure Access - Cloud Firewall | `firewalllogs` | `1234567_a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0/firewalllogs` |
    | Cisco Secure Access - IPS | `intrusionlogs` | `1234567_a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0/intrusionlogs` |
    | Cisco Secure Access - File Events | `fileeventlogs` | `1234567_a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0/fileeventlogs` |

    !!! Note
        Replace `1234567_a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0` with the base prefix extracted from your own Cisco Secure Access Data path.

=== "Your Own S3 Bucket"

    When selecting the trigger, choose **Fetch new logs on S3**.

    In the connector configuration, set the following fields:

    - **AWS Region** (`aws_region_name`): the AWS region where your S3 bucket and SQS queue are deployed.
    - **AWS Role ARN** (`aws_role_arn`) or **AWS Access Key** / **AWS Secret Access Key**: the credentials configured when you [set up AWS authentication](#step-1-configure-the-s3-bucket) in Step 1.

    In the trigger configuration, set the following fields:

    - **AWS SQS queue name** (`queue_name`): the name of the SQS queue you created in Step 1 to receive S3 object creation notifications.
    - **Intake key** (`intake_key`): the intake key generated when you created the intake in [Step 2](#step-2-create-the-intake).

    Cisco Secure Access stores each log type in a dedicated subfolder at the root of your bucket. Since your bucket may hold several log types, you can restrict the connector to a single one with a **Prefix filter** (`prefix_filter`) matching the subfolder of the intake you are configuring:

    | Intake | Subfolder |
    | --- | --- |
    | Cisco Secure Access - DNS | `dnslogs` |
    | Cisco Secure Access - Web | `proxylogs` |
    | Cisco Secure Access - Cloud Firewall | `firewalllogs` |
    | Cisco Secure Access - IPS | `intrusionlogs` |
    | Cisco Secure Access - File Events | `fileeventlogs` |
