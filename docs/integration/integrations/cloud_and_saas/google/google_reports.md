uuid: 04d36706-ee4a-419b-906d-f92f3a46bcdd
name: Google Reports
type: intake

## Overview

Google Reports is a data reporting and analysis platform offered by Google for Google Workspace services, designed to provide insights and metrics about user activities and interactions within various Google services. It allows organizations to track and visualize user engagement, application usage, and other relevant data points, enabling informed decision-making and optimization of digital experiences. 

### Supported applications

This integration can collect activities from the following GSuite applications:

- `admin` to collect activities on the Admin console 
- `calendar` to collect events from Google calendar
- `chat` to collect Chat activities
- `drive` to supervise Google Drive events
- `gcp` for the Google Cloud platform activiaties
- `groups` to collect Google groups events
- `groups_entreprise` to collect Entreprise groups events
- `jamboard` to collect Jamboard activities
- `login` to monitor authentication in Google applications
- `meet` to supervise Google meet events
- `token` for authentication supervision
- `user_accounts` to monitor Users accounts activities
- `keep` to supervices Google Keep activities


### Limitation

Only activities from one applications can be collected from one playbook.
To collect activities from several Google Application, create as many playbooks as applications to collect.

{!_shared_content/operations_center/detection/generated/suggested_rules_04d36706-ee4a-419b-906d-f92f3a46bcdd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/04d36706-ee4a-419b-906d-f92f3a46bcdd.md!}

## Configure

### Prerequisites

- Google licence Enterprise standard or higher
- Access to Sekoia.io Intakes and Playbook pages with write permissions
- Administrator access to the Google Cloud console and to Google Workspace

### Create a dedicated service account

To create a service account you have to :

  1. Create a project
  2. Turn on the APIs for the service account
    a. In your project, select *APIs & Services* and then *Library*
    b. Select the *Admin SDK API* and click on *Enable* (you can write the name in the search box to find it more easily)
  3. Under *APIs & Services*, set up the *OAuth consent screen*
    - Click on *OAuth consent screen*
    - For *User type*, select *Internal*
    - Write an *App Name*, a *User support email* and an email address for the *Developer contact information*
    - Select the following scopes (see [Choose Reports API scopes](https://developers.google.com/admin-sdk/reports/auth)):
        -  `https://www.googleapis.com/auth/admin.reports.audit.readonly`
        -  `https://www.googleapis.com/auth/admin.reports.usage.readonly`
  4. Create the service account
    - Under *IAM & Admins*, click on *Service Accounts* and click on *Create Service Account*
    - Specify the Service Account details
    - Click on *Done* (no need to *Grant this service account access to project* and *Grant users access to this service account*)
  5. Create a delegation
    - Find your new *Service Account* and select *Managed details*
    - Click on *Advanced settings*
    - Under "Domain-wide delegation" find your service account's *Client ID*. Copy the client ID value to your clipboard.
    - Click on *View Google Workspace Admin Console*, then sign in using a **super administrator user account** and continue following these steps.
    - In the Google Admin console, go to *Menu* > *Security* > *Access* and *data control* > *API controls*.
    - Click Manage Domain Wide Delegation.
    - Click *Add new*.
    - In the "Client ID" field, paste the client ID that you previously copied.
    - In the "OAuth Scopes" field, enter a comma-delimited list of the scopes required by your application. This is the same set of scopes you defined when configuring the OAuth consent screen.
        -  `https://www.googleapis.com/auth/admin.reports.audit.readonly`
        -  `https://www.googleapis.com/auth/admin.reports.usage.readonly`
    - Click *Authorize*


For more details in each steps please read this [Documentation](https://support.google.com/a/answer/7378726?hl=en) and [this one about delegation](https://developers.google.com/workspace/guides/create-credentials#optional_set_up_domain-wide_delegation_for_a_service_account)

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

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Google Report`.
2. Copy the associated Intake key

### Pull the logs to collect them on Sekoia.io

Go to the Sekoia.io [playbook page](https://app.sekoia.io/operations/playbooks), and follow these steps:

- Click on **+ PLAYBOOK** button to create a new one
- Select **Create a playbook from scratch**
- Give it a name in the field **Name**
- Open the left panel, click **Google** then select the trigger `Get user activities`
- Click on **Create**

- Create a **Module configuration** using your service account credentials from your Google Cloud environment extracted on a JSON file. Name the module configuration as you wish


-  Create a **Trigger configuration** using:

    * Type the `Intake key` created on the previous
    * Select the `application name` what you to fetch events from
    * Type the `an Google workspace admin email`.
  
!!! Important
    This Google workspace admin email is any user part of the domain **that has** the right to view de Data of Google Workspace 

- Click on the **Save** button
- **Activate the playbook** with the toggle button on the top right corner of the page

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)


## Further readings

- [Choose Reports API scopes](https://developers.google.com/admin-sdk/reports/auth)
- [Create a service account](https://support.google.com/a/answer/7378726?hl=en)
- [Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete)
