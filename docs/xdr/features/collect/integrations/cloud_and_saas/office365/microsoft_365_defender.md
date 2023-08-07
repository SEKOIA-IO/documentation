uuid: 05e6f36d-cee0-4f06-b575-9e43af779f9f
name: Microsoft 365 Defender
type: intake

## Overview

**This Intake was previously called Microsoft Defender for Endpoints.**

Microsoft 365 Defender is a unified pre- and post-breach enterprise defense suite that natively coordinates detection, prevention, investigation, and response across endpoints, identities, email, and applications to provide integrated protection against sophisticated attacks.

This setup guide describes how to forward events produced by `Microsoft 365 Defender` to Sekoia.io XDR.


{!_shared_content/operations_center/detection/generated/suggested_rules_05e6f36d-cee0-4f06-b575-9e43af779f9f_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/05e6f36d-cee0-4f06-b575-9e43af779f9f.md!}

## Microsoft 365 Defender event types supported
Here is a list of all the Microsoft 365 Defender event types supported by this integration:

* Alert Evidence
* AlertInfo
* DeviceEvents
* DeviceFileCertificateInfo
* DeviceFileEvent
* DeviceImageLoadEvents
* DeviceInfo
* DeviceLogonEvents
* DeviceNetworkEvents
* DeviceNetworkInfo
* DeviceProcessEvents
* DeviceRegistryEvents
* EmailAttachmentInfo
* EmailEvents
* EmailPostDeliveryEvents
* EmailUrlInfo
* IdentityLogonEvents
* IdentityQueryEvents
* IdentityDirectoryEvents
* CloudAppEvents

Please follow [this link](https://learn.microsoft.com/en-us/microsoft-365/security/defender/supported-event-types?view=o365-worldwide) to see all the types provided by Microsoft. 

## Configure

To forward Microsoft 365 Defender events from Microsoft to Sekoia.io you need to send your event to an Azure Event Hub where Sekoia.io will collect the events.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Microsoft 365 Defender`.

### Create an Azure Event Hub

If you do not already have a Event Hub follow this guide :
{!_shared_content/operations_center/integrations/event_hub.md!}

### Send logs from 365 Defender to Azure Event Hub

When you have an Event Hub follow this guide to send your events from Microsoft 365 Defender to the Event Hub :

- Log on to Microsoft 365 Defender portal as a Global Administrator or Security Administrator.
- Go to the Streaming API settings page.
- Click on Add.
- Choose a name for your new settings.
- Choose Forward events to Azure Event Hub.

- You can select if you want to export the event data to a single Event Hub, or to export each event table to a different Event Hubs in your Event Hubs namespace.
- To export the event data to a single Event Hub, enter your Event Hub name and your Event Hub resource ID.
- To get your Event Hub resource ID, go to your Azure Event Hubs namespace page on Azure > Properties tab > copy the text under Resource ID:
(e.g. `/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX/resourceGroups/resourcegroupname/providers/Microsoft.EventHub/namespaces/namespacename`).
- An Event Hub resource ID
- Go to the Supported Microsoft 365 Defender event types in event streaming API to review the support status of event types in the Microsoft 365 Streaming API.
- Choose the events you want to stream and click Save.

{!_shared_content/operations_center/integrations/configure_consume_event_hub.md!}

#### Further Readings

- [Configure Microsoft 365 Defender to stream Advanced Hunting events to your Azure Event Hub](https://docs.microsoft.com/en-us/microsoft-365/security/defender/streaming-api-event-hub)
