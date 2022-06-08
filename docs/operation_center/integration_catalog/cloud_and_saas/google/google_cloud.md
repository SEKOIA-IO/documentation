## Overview

Google Cloud Logging centralizes logs from Google Cloud products.

In this documentation, you will learn how to collect and send Google Cloud logs to SEKOIA.IO.

## Configure

Before you begin working with PubSub, [verify that you have the right permission](https://cloud.google.com/logging/docs/export/configure_export_v2?hl=en#before-you-begin).

Follow Google's documentation to [configure a dedicated PubSub receiver](https://cloud.google.com/pubsub/docs/publish-receive-messages-console). At the end of the documentation you should have done the following:

   - Setup a project
   - Create a topic
   - Add a subscription 
   - Try your setup by publishing a message to the topic

Next, create a [dedicated service account](https://cloud.google.com/pubsub/docs/reference/libraries#setting_up_authentication). At the end of the documentation you should have done the following:

- Create a service account with the role `Pub/Sub Subscriber`
- Create and download JSON keys (*service account credentials*)

You should now have:

   - A credentials file
   - A project ID
   - A subscription ID

To pull events, go to [the playbook page](https://app.sekoia.io/operations/playbooks) and create your playbook with a template: "Create a new playbook" > "Use a template" > Search for Google Cloud.

You can also create your own on the same basis. A typical playbook to retrieve and send Google Cloud logs to SEKOIA.IO will use this kind of chain:

- A "Google Pub/Sub" trigger
- An action that sends events to SEKOIA.IO

To start sending Logs to SEKOIA.IO, please create a [Logs Router Sinks](https://cloud.google.com/logging/docs/export/configure_export_v2?hl=en#creating_sink) with an [Inclusion Filter](https://cloud.google.com/logging/docs/view/logging-query-language) that fits your needs (Read the documentation dedicated to the product you want to monitor).
