uuid: a0716ffd-5f9e-4b97-add4-30f1870e3d03
name: Netskope Transaction Events
type: intake

## Overview

[Netskope](https://www.netskope.com/) is a cybersecurity company that provides solutions to protect data in cloud apps and network security while applying zero trust principles.

- **Vendor**: Netskope
- **Plan**: Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Network

## Prerequisites

- Access to the Netskope Admin console
- The **Event Streaming option activated** (Please contact the Netskope Support if not).
- Access to Sekoia.io Intakes and Playbook pages with write permissions

## Step-by-Step Configuration Procedure
### Instructions on the 3rd Party Solution

!!! Important
    The Netskope Event Streaming rely on [Google Pub/Sub lite](https://cloud.google.com/pubsub/lite/docs).

#### Create and download JSON keys

To collect transaction events, you will need a subscription key:

1. Connect to the Netskope Admin console
2. Go to `Settings > Tools`
3. On the left panel, click on the `Event Streaming`. If the section is not available in our Admin UI, please contact the Netskope Support.
4. Go to the `Subscription Key` section and click on `Generate and Download key`

Find more information about the subscription key on the [official google documentation](https://cloud.google.com/iam/docs/keys-create-delete).

**Example of JSON key file**

```JSON
{
  "type": "service_account",
  "project_id": "PROJECT_ID",
  "private_key_id": "KEY_ID",
  "private_key": "-----BEGIN PRIVATE KEY-----\nPRIVATE_KEY\n-----END PRIVATE KEY-----\n",
  "client_email": "SERVICE_ACCOUNT_EMAIL",
  "client_id": "CLIENT_ID",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/SERVICE_ACCOUNT_EMAIL"
}
```

### Instruction on Sekoia

!!! Note
    The intake you would like to configure is nammed `Netskope Transaction Events`. Not `Netskope Events`.

{!_shared_content/integration/intake_configuration.md!}

#### Pull the logs to collect them on Sekoia.io

Go to the Sekoia.io [playbook page](https://app.sekoia.io/operations/playbooks), and follow these steps:

- Click on **+ PLAYBOOK** button to create a new one
- Select **Create a playbook from scratch**
- Give it a name in the field **Name**
- Open the left panel, click **Google** then select the trigger `Fetch new transaction events from Netskope`
- Click on **Create**

-  Create a **Trigger configuration** using:
    * Your service account credentials from your Google Cloud environment extracted on a JSON file
    * Type the `Intake key` created on the previous
    * Select the `application name` what you to fetch events from
    * Type the `Admin email`

- Click on the **Save** button
- **Activate the playbook** with the toggle button on the top right corner of the page

{!_shared_content/operations_center/integrations/generated/a0716ffd-5f9e-4b97-add4-30f1870e3d03_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a0716ffd-5f9e-4b97-add4-30f1870e3d03_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/a0716ffd-5f9e-4b97-add4-30f1870e3d03.md!}

## Further readings

- [Configuring Netskope Transaction Events](https://docs.netskope.com/en/netskope-help/data-security/transaction-events/netskope-transaction-events/)
- [Create a service account](https://support.google.com/a/answer/7378726?hl=en)
- [Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete)