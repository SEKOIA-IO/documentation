uuid: 19cd2ed6-f90c-47f7-a46b-974354a107bb
name: Azure Active Directory
type: intake

## Overview

Azure Active Directory is a cloud-based Identity and Rights management service. The service is developed and managed by Microsoft Corp.

{!_shared_content/operations_center/detection/generated/suggested_rules_19cd2ed6-f90c-47f7-a46b-974354a107bb_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/19cd2ed6-f90c-47f7-a46b-974354a107bb.md!}

## Configure

To forward Azure Active Directory events from Azure to Sekoia.io you need to send your event to an Azure Event Hub where Sekoia.io will collect the events.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Azure Active Directory`.

### Create an Azure Event Hub

If you do not already have a Event Hub follow this guide :
{!_shared_content/operations_center/integrations/event_hub.md!}

### Send logs from Azure Active Directory to Azure Event Hub

When you have an Event Hub follow this guide to send your Azure Active Directory events from Azure to the Event Hub :

You need to activate and configure the Azure Active Directory diagnostic settings (e.g. `company-ad`), 
to receive logs from the Azure Active Directory into your Event Hub.

Navigate to “Home”, “Azure Active Directory” (e.g. `company-ad`), “Monitoring”, ”Diagnostic settings”:

- Add a new diagnostic setting, and select “Stream to an event hub” and click on configure.
- Select the previously created “Event hubs”, “Event Hub” and “SharedAccessKey” (**see step 3 of the event hub guide**).
- In the log section, select all log categories (as shown below).
- Choose a name for this configuration and click on “Save”.
  
![diag](https://github.com/jdpju/documentation/assets/113444861/b5e55fd3-da86-4f2f-8095-3c1704ae7a20){: style="max-width:100%"}

{!_shared_content/operations_center/integrations/configure_consume_event_hub.md!}

#### Further Readings

- [Microsoft Github diagnostic Active Directory documentation](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/active-directory/reports-monitoring/tutorial-azure-monitor-stream-logs-to-event-hub.md)
