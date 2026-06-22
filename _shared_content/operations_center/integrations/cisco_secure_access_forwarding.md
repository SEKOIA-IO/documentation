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

In the connector configuration, set the following fields:

- **AWS Region** (`aws_region_name`): the region you selected when configuring the S3 bucket in Cisco Secure Access.
- **AWS Access Key** (`aws_access_key`): the Access Key copied from the Cisco Secure Access Amazon S3 Summary page.
- **AWS Secret Access Key** (`aws_secret_access_key`): the Secret Key copied from the Cisco Secure Access Amazon S3 Summary page.
