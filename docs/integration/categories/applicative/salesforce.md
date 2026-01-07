---
uuid: d2725f97-0c7b-4942-a847-983f38efb8ff
title: Salesforce
name: Salesforce
type: intake
---

## Overview

Salesforce provides customer relationship management software and applications focused on sales, customer service, marketing automation, e-commerce, analytics, and application development.

- **Vendor**: Salesforce
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Application Logs



## Configure

This setup guide will show you how to provide an integration between Salesforce events and Sekoia.io.

!!! note
    To provide a quick detection on malicious activities, Sekoia.io recommends getting the event log files on an hourly basis.
    Please see [the Salesforce documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/event_log_file_hourly_overview.htm) to enable hourly Event Log Files.

!!! warning
    Please ensure enabling `Hourly` log collection in your Salesforce Event Log File settings before unselecting the `Daily` log option in your intake configuration. This omission will cause an `INVALID_FIELD` error in the connector.


### Configure OAuth

#### Create a new Connected App

1. On the [Salesforce App Manager](https://login.salesforce.com), go to the Setup
2. On the left menu, select `platform tools` > `Apps` > `App Manager`
3. On the `App Manager` page, click `New Connected App`
4. In the basic information section, type the name of the connected app and a contact email
5. In the `API` section, turn on `Enable OAuth Settings`
6. Type any callback url then select `Manage user data via APIs (api)` and `Perform requests at any time (refresh_token, offline_access)` as the OAuth scopes.
7. Click `Save`

<video controls width="100%">
  <source src="/assets/integration/cloud_and_saas/salesforce_events/create_connected_app.webm" type="video/webm">
</video>

#### Set the client credentials

1. On the management page of the connected app, click `Manage`
2. Click `Edit Policies` button
3. In the `Client Credentials Flow`, select a user with a `System Administrator` profile in the `Run As` field.
4. Click `Save`

<video controls width="100%">
  <source src="/assets/integration/cloud_and_saas/salesforce_events/run_as.webm" type="video/webm">
</video>

#### Get consumer key and secret

1. On the management page of the connected app, in the API section, click `Manage Consumer Details`
3. In the `Consumer details` section, copy the consumer key and the consumer secret

<video controls width="100%">
  <source src="/assets/integration/cloud_and_saas/salesforce_events/consumer_key_and_secret.webm" type="video/webm">
</video>

### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Salesforce.
2. Set up the intake configuration with the consumer key and consumer secret.


!!! note

	Salesforce generates Events Log Files hourly. It can take up to an hour for your logs to arrive. See [this documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/event_log_file_hourly_overview.htm) for more details


{!_shared_content/operations_center/integrations/generated/d2725f97-0c7b-4942-a847-983f38efb8ff_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d2725f97-0c7b-4942-a847-983f38efb8ff_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/d2725f97-0c7b-4942-a847-983f38efb8ff.md!}

## Further Readings

- [Salesforce Real-Time Event Monitoring feature is turned off by default](https://help.salesforce.com/s/articleView?id=release-notes.rn_security_em_generate_event_log_files.htm&release=244&type=5)
- [Real-Time Event Monitoring enable instructions](https://help.salesforce.com/s/articleView?id=sf.real_time_event_monitoring_enable.htm&type=5)
