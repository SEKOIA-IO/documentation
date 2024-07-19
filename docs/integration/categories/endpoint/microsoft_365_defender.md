uuid: 05e6f36d-cee0-4f06-b575-9e43af779f9f
name: Microsoft 365 Defender
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**: Alert, Telemetry
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:

**This Intake was previously called Microsoft Defender for Endpoints.**

Microsoft 365 Defender is a unified pre- and post-breach enterprise defense suite that natively coordinates detection, prevention, investigation, and response across endpoints, identities, email, and applications to provide integrated protection against sophisticated attacks.

This setup guide describes how to forward events produced by `Microsoft 365 Defender` to Sekoia.io XDR.




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

To forward **Microsoft 365 Defender** events from Microsoft to Sekoia.io you need to send your event to an **Azure Event Hub** where Sekoia.io will collect the events.
<div style="text-align: center;">
    <img width="100%" alt="image" src="/assets/operation_center/integration_catalog/cloud_and_saas/event_hub/consume_azure_logs.png">
</div>

### Prerequisite

You must have the following rights to perform the installation:  
- Global Administrator or Security Administrator rights on **Microsoft 365 Defender**  
- Contributor write on **Azure** 

{!_shared_content/operations_center/integrations/event_hub.md!}

### Send logs from 365 Defender to Azure Event Hub

When you have an **Event Hub** follow this guide to send your events from **Microsoft 365 Defender** to the **Event Hub**:

1. Open the **Microsoft 365 Security** App portal as a *Global Administrator* or *Security Administrator*.
2. On the left panel, select **Settings**.
3. Select **Microsoft Defender XDR**.
4. In **General**, click on **Streaming API** and click on **+ Add**.
5. Choose Forward events to **Azure Event Hub**.
6. To export the event data to a single **Event Hub**, enter your **Event Hub** name and your **Event Hub Namespace** resource ID. **Be sure to take the event hub namespace ID and not the event hub ID.**
7. To get your **Event Hub Namespace** resource ID, go to your **Azure Event Hub Namespace** page on Azure > Properties tab > copy the text under Resource ID:
(e.g. `/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX/resourceGroups/resourcegroupname/providers/Microsoft.EventHub/namespaces/namespacename`).
8. Go to the supported **Microsoft 365 Defender** event types in event streaming API to review the support status of event types in the Microsoft 365 Streaming API.
9. Choose the events you want to stream and click Save.

!!! Disclamer
    Be sure to size your eventhub ressources accordingly to the number of EPS you have (number of eventhubs, throughput, partitions...) See the Further readings section in order to estimate the number of event per second **Microsoft 365 Defender** can be on your instance.


{!_shared_content/integration/detection_section.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_05e6f36d-cee0-4f06-b575-9e43af779f9f_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/05e6f36d-cee0-4f06-b575-9e43af779f9f.md!}

#### Further Readings
- [Estimating initial Event Hub capacity](https://learn.microsoft.com/en-us/microsoft-365/security/defender/streaming-api-event-hub?view=o365-worldwide#estimating-initial-event-hub-capacity) 
- [Configure Microsoft 365 Defender to stream Advanced Hunting events to your Azure Event Hub](https://docs.microsoft.com/en-us/microsoft-365/security/defender/streaming-api-event-hub)

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Microsoft 365 Defender`.

{!_shared_content/operations_center/integrations/configure_consume_event_hub.md!}
