## Overview

Google Cloud Logging centralize logs from Google Cloud products.

In this documentation we will explain how to collect and send Google Cloud logs to SEKOIA.IO.

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