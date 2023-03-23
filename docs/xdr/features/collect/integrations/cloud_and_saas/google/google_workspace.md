uuid: 44439212-c2d8-4645-ad60-8fd5e39140b3
name: Google Cloud Audit
type: intake

{!_shared_content/operations_center/integrations/google_cloud.md!}

{!_shared_content/operations_center/integrations/generated/44439212-c2d8-4645-ad60-8fd5e39140b3.md!}


## Use case - Collect Google Workspace audit logs

### Prerequisites

- Administrator access to the the Google Cloud console
- Google licence Enterprise standard or higher
- Access to SEKOIA.IO Intakes and Playbook pages with write permissions

!!! Warning
	The administrator that proceed to the configuration MUST explicitly have the role "Logging Admin" activated

### Confirm Google Cloud logs are already available on your Google Cloud console

To begin, follow the official documentation to [share audit logs with Google Cloud](https://cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs).

Once log sharing is activated, you should be able to see Google Workspace events in Google Cloud Log Explorer.
To do so:

- Go to your Google Cloud console available at `console.cloud.google.com`
- On the left panel, select the `Logging` page
- Filter on the top left corner on your domain like `mycompany.com`
- Confirm your events are available as they should be listed on the bottom of the page

### Forward the logs to SEKOIA.IO

To forward these events to SEKOIA.IO, please follow this procedure:

1. Identify the right filters

On the details of any log, look for the fields:

- `logName` with a value like "organizations/<YOUR ORGANISATION ID>/logs/cloudaudit.googleapis.com%2Factivity"
- `protoPayload.@type` with a value that exactly is "type.googleapis.com/google.cloud.audit.AuditLog"

For those two fields, click on their value and click `Show matching entries`. This should build a Query on top of your events listing that should be:

```
protoPayload.@type="type.googleapis.com/google.cloud.audit.AuditLog"
logName="organizations/<YOUR ORGANISATION ID>/logs/cloudaudit.googleapis.com%2Factivity"

```

Copy this value that will be used in the next step.


2. Configure your log routeur

On the left panel, go to `Logs Router` then click on `Create Sink`

- Sink details

* Name: `SEKOIA_IO`
* Description: `Routing sink to forward audit logs to SEKOIA.IO`

- Sink destination

* Select sink service: `Cloud Pub/Sub topic`
* Select Cloud Pub/Sub topic: `Use a Cloud Pub/Sub topic in a project`

!!! Note
Replace `[PROJECT_ID]` and `[TOPIC_ID]` by their values according to your PubSub topic (Google Cloud related documentation).

- Choose logs to include in sink

* Choose `Include only logs ingested by this organisation`
* In the section "Build inclusion filter", enter the query you copied during step 1.

That should be like the following:

```
protoPayload.@type="type.googleapis.com/google.cloud.audit.AuditLog"
logName="organizations/<YOUR ORGANISATION ID>/logs/cloudaudit.googleapis.com%2Factivity"

```

- Choose logs to filter out of sink

If you have other products on Google Cloud such as virtual machines or kubernetes that are part of the project, you should apply a filter that excludes these components to avoid collecting their logs in the process

- Click on `CREATE SINK`

This should add an entry in the log router sinks list named `SEKOIA_IO` with status `Enabled` and type `Cloud Pub/Sub topic`.

3. Confirm the logs are received in your Pub/Sub

- Go to your `Pub/Sub page`, then click on `Topics` on the left panel
- Click on your sekoia topic previously configured
- On the bottom of the page, click on the `Message tab`
- Select your project
- Click on `Pull button`, you should see events appearing on the list

4. Create your intake

- Go to your SEKOIA.IO [Intakes page](https://app.sekoia.io/operations/intakes)
- Click on `+ Intake` to create a new one
- Choose `Google Cloud Audit Logs`, give it a name and choose the relevant Entity
- Click on `Create`
- Copy the `Intake key` of this Google Intake, and save it on a block note. It will be used in the next step.

5. Pull the logs to collect them on SEKOIA.IO

- Go to the SEKOIA.IO [playbook page](https://app.sekoia.io/operations/playbooks)
- Click on `+ PLAYBOOK` to create a new one
- Select `Use a template`
- Search for "Google" keywork on the search bar and select the template named `Forward Google Pubsub records to SEKOIA.IO`

![google-playbook-template](/assets/operation_center/integration_catalog/cloud_and_saas/google/google-template.PNG){: style="max-width:100%"} 

- Create a "Module configuration" using your service account credentials from your Google Cloud environment extracted on a JSON file. Name the module configuration as you wish

![template-playbook-configuration](/assets/operation_center/integration_catalog/cloud_and_saas/google/template-configuration.png ){: style="max-width:100%"}

- Create a "Trigger configuration" using:

* The project ID and subscription ID from your Google Cloud environment
* The Intake key created on step 4.

- Click on the `Save` button
- Activate the playbook with the toggle button on the top right corner of the page