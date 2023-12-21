uuid: a0716ffd-5f9e-4b97-add4-30f1870e3d03
name: Netskope Transaction Events
type: intake

## Overview

[Netskope](https://www.netskope.com/) is a cybersecurity company that provides solutions to protect data in cloud apps and network security while applying zero trust principles.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

{!_shared_content/operations_center/detection/generated/suggested_rules_a0716ffd-5f9e-4b97-add4-30f1870e3d03_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/a0716ffd-5f9e-4b97-add4-30f1870e3d03.md!}

## Configure

### Prerequisites

- Access to Sekoia.io Intakes and Playbook pages with write permissions
- Administrator access to the Google Cloud console
- Configured PubSub Lite subscription

### Create and download JSON keys (service account credentials)

To use a service account from outside of Google Cloud, such as on Sekoia.io, you must first establish the identity of the service account. Public/private key pairs provide a secure way of accomplishing this goal. When you create a service account key, the public portion is stored on Google Cloud, while the private portion is available only to you.

!!! Note
	By default, service account keys never expire.

1. Go to the Service accounts page
2. Select your cloud project
3. Click the email address of the service account that you want to create a key for
4. Click the **Keys** tab
5. Click the **Add key** drop-down menu, then select **Create new key**
6. Select **JSON** as the Key type and click **Create**

!!! Important
	Clicking **Create** downloads a service account key file. After you download the key file, you cannot download it again. You will need it on the following steps on Sekoia.io.

Find more information on the [official google documentation](https://cloud.google.com/iam/docs/keys-create-delete).

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

## Sekoia.io configuration procedure

### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Netskope Transaction Events`.
2. Copy the associated Intake key

### Pull the logs to collect them on Sekoia.io

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

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)


## Further readings

- [Configuring Netskope Transaction Events](https://docs.netskope.com/en/netskope-help/data-security/transaction-events/netskope-transaction-events/)
- [Create a service account](https://support.google.com/a/answer/7378726?hl=en)
- [Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete)

