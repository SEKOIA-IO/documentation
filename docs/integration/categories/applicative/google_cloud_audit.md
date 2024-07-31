uuid: 44439212-c2d8-4645-ad60-8fd5e39140b3
name: Google Workspace and Google Cloud Audit Logs
type: intake

## Overview
- **Vendor**: Google
- **Plan**: Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Audit
- **Supported application or feature**: Application Logs

Google Cloud Logging centralizes logs from Google Cloud products.

In this documentation, you will learn how to collect and send Google Workspace and Google Cloud audit logs to Sekoia.io.



## Google Cloud configuration procedure

### Prerequisites

- Google licence Enterprise standard or higher
- Access to Sekoia.io Intakes and Playbook pages with write permissions
- Administrator access to the Google Cloud console

!!! Warning
	The administrator that proceeds to the configuration MUST explicitly have the role "Logging Admin" activated. This is not the case by default even for administrator users.

### Centralise Google Workspace logs on your Google Cloud

#### Create a topic

This topic will hold messages to be delivered.

1. In the Google Cloud console available at `console.cloud.google.com`, go to your **Pub/Sub page**
2. Click **Create topic**
3. In the window that opens, enter `sekoia-gca-topic` in the Topic ID field
4. Click **Create topic**

#### Create a subscription to query the topic

To add a subscription to the topic you just created, complete these steps:

1. Click the **Subscriptions tab**
2. Click **Create subscription**
3. Enter `sekoia-gca-subscription` in the **Subscription ID** field
4. Leave the default values for the remaining options
5. Click **Create**
6. Return to the **Topics page** and click `sekoia-gca-topic`.

!!! Note
	The `sekoia-gca-subscription` subscription is now attached to the topic `sekoia-gca-topic`. Google Pub/Sub will deliver all messages sent to `sekoia-gca-topic` to this subscription.

More information on this procedure is available in the [official google documentation](https://cloud.google.com/pubsub/docs/publish-receive-messages-console?hl=en).

#### Create a project-level log sink

This will be used to capture all logs across this project that should be sent to the Pub/Sub topic created above. 

!!! Important
	Your account should have the role **logging.admin** explicitly set on your account which is not the case of administrator accounts by default. For more information, see associated [documentation](https://cloud.google.com/logging/docs/export/configure_export_v2?hl=en#before-you-begin).

On the left panel, go to **Logs Router** then click on **Create Sink**

- Sink details
	* Name: `sekoia-gca-sink`
	* Description: `Routing sink to forward audit logs to Sekoia.io`

- Sink destination
	* Select sink service: **Cloud Pub/Sub topic**
	* Select Cloud Pub/Sub topic: **Use a Cloud Pub/Sub topic in a project**

!!! Note
	Replace `[PROJECT_ID]` by its value according to your context and `[TOPIC_ID]` by `sekoia-gca-topic`.

- Choose logs to include in sink
	* Choose **Include only logs ingested by this organisation**
	* In the section "Build inclusion filter", enter the following query:

```
LOG_ID("cloudaudit.googleapis.com/activity") 
OR LOG_ID("cloudaudit.googleapis.com/data_access")
```

- Choose logs to filter out of sink
	* If you have other products on Google Cloud such as virtual machines or Kubernetes that are part of the project, you should apply a filter that excludes these components to avoid collecting their logs in the process

- Click on **CREATE SINK**

This should add an entry in the log router sinks list named `sekoia-gca-sink` with status **Enabled** and type **Cloud Pub/Sub topic**.

!!! Note
	You cannot create aggregated sinks through the Google Cloud Console. They must be configured and managed through either the API or gcloud CLI tool. Only project-level (non-aggregated) sinks show up in Google Cloud Console. This is what we configured here.

#### Confirm the logs are received in your Pub/Sub

By following these steps, you should see events appearing on the list

1. Go to your **Pub/Sub page**, then click on **Topics** on the left panel
2. Click on your sekoia `sekoia-gca-topic` topic previously configured
3. On the bottom of the page, click on the **Message tab**
4. Select your project
5. Click on **Pull button**

#### Create a dedicated service account 

The service account will be used on Sekoia.io to pull logs available on your Google Cloud instance.

1. Go to the **Create service account** page
2. Select your cloud project
3. Enter `sekoia-gca-service-account` as a service account name
4. Click **Create and continue**
5. Set the role **Pub/Sub Subscriber**
6. Click **Continue**, then click **Done** to finish creating the service account

!!! Note
	Ensure that this user has the role **Pub/Sub Subscriber** in both **Topic** and **Subsciption** pages. Otherwise, you will have an error with status 403 when you will activate the playbook detailed on the bottom of this page. 

Find more information on the [official google documentation](https://cloud.google.com/iam/docs/service-accounts-create).

#### Create and download JSON keys (service account credentials)

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

#### Create your intake

Go to your Sekoia.io [Intakes page](https://app.sekoia.io/operations/intakes), and follow these steps:

1. Click on **+ Intake** button to create a new one
2. Choose **Google Cloud Audit Logs**, give it a name and choose the relevant Entity
3. Click on **Create** button
4. Copy the **Intake key** of this Google Intake.

!!! Note
	Save the `Intake key` on a block note. It will be used in the next step.

#### Pull the logs to collect them on Sekoia.io

Go to the Sekoia.io [playbook page](https://app.sekoia.io/operations/playbooks), and follow these steps:

- Click on **+ PLAYBOOK** button to create a new one
- Select **Use a template**
- Search for `Google` keywork on the search bar and select the template named `Forward Google Pubsub records to Sekoia.io`

![google-playbook-template](/assets/integration/cloud_and_saas/google/google-template.PNG){: style="max-width:100%"} 

- Create a **Module configuration** using your service account credentials from your Google Cloud environment extracted on a JSON file. Name the module configuration as you wish

![template-playbook-configuration](/assets/integration/cloud_and_saas/google/template-configuration.png ){: style="max-width:100%"}

-  Create a **Trigger configuration** using:

	* `Intake key` created on the previous
	* The project ID 
	* The suject ID that is `sekoia-gca-subscription`

- Click on the **Save** button
- **Activate the playbook** with the toggle button on the top right corner of the page

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/44439212-c2d8-4645-ad60-8fd5e39140b3_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/integrations/generated/44439212-c2d8-4645-ad60-8fd5e39140b3.md!}

