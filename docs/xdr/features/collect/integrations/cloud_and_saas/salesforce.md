uuid: d2725f97-0c7b-4942-a847-983f38efb8ff
name: Salesforce
type: intake

## Overview

Salesforce provides customer relationship management software and applications focused on sales, customer service, marketing automation, e-commerce, analytics, and application development.

!!! warning
    This format is still in beta, please use it wisely.

{!_shared_content/operations_center/detection/generated/suggested_rules_d2725f97-0c7b-4942-a847-983f38efb8ff_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d2725f97-0c7b-4942-a847-983f38efb8ff.md!}

## Configure

This setup guide will show you how to provide an integration between Salesforce events and Sekoia.io.

### Configure OAuth

1. Go to the [Salesforce App Manager](https://login.salesforce.com)
2. Follow up [these instructions](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_api_integration.htm&type=5) to configure new app

   ***Note: After configuration is complete please check if your OAuth credentials are valid and you can interact with salesforce api***

3. Get `clientId` and `clientSecret` from your app

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Salesforce. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Salesforce](../../../automate/library/salesforce.md) trigger
2. Set up the module configuration with the Client Id and Client Secret. Set up the trigger configuration with the intake key
3. Start the playbook and enjoy your events

## Further Readings

- [Salesforce Real-Time Event Monitoring feature is turned off by default](https://help.salesforce.com/s/articleView?id=release-notes.rn_security_em_generate_event_log_files.htm&release=244&type=5)
- [Real-Time Event Monitoring enable instructions](https://help.salesforce.com/s/articleView?id=sf.real_time_event_monitoring_enable.htm&type=5)
