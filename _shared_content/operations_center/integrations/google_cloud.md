## Overview

Google Cloud Logging centralizes logs from Google Cloud products.

In this documentation, you will learn how to collect and send Google Cloud logs to SEKOIA.IO.

## Configure

Before you begin working with PubSub, [verify that you have the right permission](https://cloud.google.com/logging/docs/export/configure_export_v2?hl=en#before-you-begin).

Follow Google's documentation to [configure a dedicated PubSub receiver](https://cloud.google.com/pubsub/docs/publish-receive-messages-console). At the end of the documentation you should have done the following:

   - Setup a project
   - Create a topic
   - Add a subscription (*you should have the role `logging.admin` explicitly set on your account; for more information, see [associated documentation](https://cloud.google.com/logging/docs/export/configure_export_v2)*)
   - Try your setup by publishing a message to the topic

Next, create a [dedicated service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts). At the end of the documentation you should have done the following:

- Create a service account with the role `Pub/Sub Subscriber`

!!! Note
      To successfully activate the playbook further down this page, ensure the user has been granted the **Pub/Sub Subscriber role** for both the **Topic** and **Subscription** pages. Failure to do so will result in an error with status code 403. 

- Create and download JSON keys (*service account credentials*) 

You should now have:

   - A credentials file
   - A project ID
   - A subscription ID

To pull events, you have to:

1. Go to [the playbooks' page](https://app.sekoia.io/operations/playbooks) 
2. Click on `+New playbook` to create a new playbook 
3. Select `Use a template` when creating a playbook
4. Search for `Google Cloud` then select `Forward Google Pubsub records to Sekoia.io`

This playbook consumes records from Google Pubsub and pushes them to Sekoia.io. 

You can also create your own on the same basis by using the "Google Pub/Sub" trigger (`Connect to the specified`)

- Use the JSON keys (*service account credentials*) information downloaded to complete the fields on the trigger

**Fields description**

|Field|Meaning|
|---|---|
|name| Configuration name|
|auth_provider_x509_cert_url| The URL of the public x509 certificate, used to verify the signature on JWTs, such as ID tokens, signed by the authentication provider. `https://wwww.googleapis.com/oauth2/v1/certs`|
|auth_url| Google authentification url `https://accounts.google.com/o/oauth2/auth`|
|client_email| Client email|
|client_id| Client id|
|client_x509_cert_url| The URL of the public x509 certificate, used to verify JWTs signed by the client|
|private_key| Private key|
|private_key_id| Private key id|
|project_id| Project id|
|token_uri| token server endpoint URI `https://oauth2.googleapis.com/token`|
|type|Activity type `service_account`|

To start sending Logs to SEKOIA.IO, please create a [Logs Router Sinks](https://cloud.google.com/logging/docs/export/configure_export_v2?hl=en#creating_sink) with an [Inclusion Filter](https://cloud.google.com/logging/docs/view/logging-query-language) that fits your needs (Read the documentation dedicated to the product you want to monitor).

Last configuration on Google to setup is describe on each Intake.
