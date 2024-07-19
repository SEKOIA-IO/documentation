uuid: c20528c1-621e-4959-83ba-652eca2e8ed0
name: Microsoft Intune
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:

**Microsoft Intune** helps you protect your workforce's corporate data by managing devices and apps. **Intune** provides mobile device management (MDM) and mobile app management (MAM) from a secure cloud-based service that is administered using the Microsoft Endpoint Manager admin center. Using **Intune**, you ensure your workforce's corporate resources (data, devices, and apps) are correctly configured, accessed, and updated, meeting your company's compliance policies and requirements.

This setup guide describe how to forward events produced by **Microsoft Intune** to Sekoia.io.


## Configure

To forward **Microsoft Intune** events from Microsoft to Sekoia.io you need to send your event to an **Azure Event Hub** where Sekoia.io will collect the events.
<div style="text-align: center;">
    <img width="100%" alt="image" src="/assets/operation_center/integration_catalog/cloud_and_saas/event_hub/consume_azure_logs.png">
</div>

### Prerequisite

To send **Microsoft Intune** logs to Sekoia.io, there are some prerequisites: 

- Have access to the Sekoia.io XDR Operations Center 
- Be a Intune Service Administrator to perfom the interconnection with **Azure Event Hub**
- Be a Contributor on Azure to setup an **Event Hub**.

{!_shared_content/operations_center/integrations/event_hub.md!}

### Send logs from Microsoft Intune to Azure Event Hub

When you have an **Event Hub** follow [this guide](https://learn.microsoft.com/en-us/mem/intune/fundamentals/review-logs-using-azure-monitor) to send your events from **Microsoft Intune** to the **Event Hub**.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format **Microsoft Intune**.

{!_shared_content/operations_center/integrations/configure_consume_event_hub.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_c20528c1-621e-4959-83ba-652eca2e8ed0_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/c20528c1-621e-4959-83ba-652eca2e8ed0.md!}

