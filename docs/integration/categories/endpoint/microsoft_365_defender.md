uuid: 05e6f36d-cee0-4f06-b575-9e43af779f9f
name: Microsoft Defender XDR / Microsoft 365 Defender
type: intake

## Overview
- **Vendor**: Microsoft
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**: see section below

**This Intake was previously called Microsoft Defender for Endpoints.**

Microsoft Defender XDR (formely Microsoft 365 Defender) is a unified pre- and post-breach enterprise defense suite that natively coordinates detection, prevention, investigation, and response across endpoints, identities, email, and applications to provide integrated protection against sophisticated attacks.

This setup guide describes how to forward events produced by `Microsoft Defender XDR` to Sekoia.io XDR.


## Microsoft Defender XDR event types supported
Here is a list of all the Microsoft Defender XDR event types supported by this integration:

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

To forward **Microsoft Defender XDR** events from Microsoft to Sekoia.io you need to send your event to an **Azure Event Hub** where Sekoia.io will collect the events.
<div style="text-align: center;">
    <img width="100%" alt="image" src="/assets/integration/cloud_and_saas/event_hub/consume_azure_logs.png">
</div>

### Prerequisite

You must have the following rights to perform the installation:
- Global Administrator or Security Administrator rights on **Microsoft Defender XDR**
- Contributor write on **Azure**

{!_shared_content/operations_center/integrations/event_hub.md!}

### Send logs from Defender XDR to Azure Event Hub

When you have an **Event Hub** follow this guide to send your events from **Microsoft Defender XDR** to the **Event Hub**:

1. Open the **Microsoft 365 Security** App portal as a *Global Administrator* or *Security Administrator*.
2. On the left panel, select **Settings**.
3. Select **Microsoft Defender XDR**.
4. In **General**, click on **Streaming API** and click on **+ Add**.
5. Choose Forward events to **Azure Event Hub**.
6. To export the event data to a single **Event Hub**, enter your **Event Hub** name and your **Event Hub Namespace** resource ID. **Be sure to take the event hub namespace ID and not the event hub ID.**
7. To get your **Event Hub Namespace** resource ID, go to your **Azure Event Hub Namespace** page on Azure > Properties tab > copy the text under Resource ID:
(e.g. `/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX/resourceGroups/resourcegroupname/providers/Microsoft.EventHub/namespaces/namespacename`).
    If you don't see it, you can go on the JSON View
    <div style="text-align: center;">
        <img width="100%" alt="image" src="/assets/integration/cloud_and_saas/event_hub/json_view.png">
    </div>
    And the resource ID will appear on the first line :
    <div style="text-align: center;">
        <img width="100%" alt="image" src="/assets/integration/cloud_and_saas/event_hub/content_json_view.png">
    </div>
8. Go to the supported **Microsoft Defender XDR** event types in event streaming API to review the support status of event types in the Microsoft 365 Streaming API.
9. Choose the events you want to stream and click Save.

!!! Disclaimer
    Be sure to size your eventhub resources accordingly to the number of EPS you have (number of eventhubs, throughput, partitions...) See the Further readings section in order to estimate the number of event per second **Microsoft Defender xDR** can be on your instance.

### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Microsoft Defender XDR / Microsoft 365 Defender`
2. To fill the form, use the table completed during the creation of the **Event Hub**.

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/05e6f36d-cee0-4f06-b575-9e43af779f9f_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_05e6f36d-cee0-4f06-b575-9e43af779f9f_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/05e6f36d-cee0-4f06-b575-9e43af779f9f.md!}

#### Further Readings
- [Estimating initial Event Hub capacity](https://learn.microsoft.com/en-us/microsoft-365/security/defender/streaming-api-event-hub?view=o365-worldwide#estimating-initial-event-hub-capacity)
- [Configure Microsoft Defender XDR to stream Advanced Hunting events to your Azure Event Hub](https://docs.microsoft.com/en-us/microsoft-365/security/defender/streaming-api-event-hub)
