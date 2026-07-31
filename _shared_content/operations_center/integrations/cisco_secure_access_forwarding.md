This section will guide you through configuring Cisco Secure Access to forward logs to Sekoia.io using a Cisco-managed Amazon S3 bucket.

### Prerequisites

- Full Admin user role in Cisco Secure Access. For more information, see the [Manage Accounts](https://securitydocs.cisco.com/docs/csa/olh/118836.dita) documentation.
- Access to Sekoia.io Intakes and Playbook pages with write permissions.

### Step 1 — Configure the Cisco-Managed S3 Bucket

Cisco Secure Access can export your logs to a Cisco-managed Amazon S3 bucket. Cisco configures all managed buckets to use Amazon Server-Side Encryption with S3-Managed Keys (SSE-S3, AES-256). Access is provided via AWS IAM credentials.

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

### Step 2 — Create the Intake

{!_shared_content/integration/intake_configuration.md!}

### Step 3 — Configure the Connector

{!_shared_content/integration/connector_configuration.md!}

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
