# microsoft\_intune

uuid: c20528c1-621e-4959-83ba-652eca2e8ed0 name: Microsoft Intune type: intake

### Overview

* **Vendor**:
* **Supported environment**:
* **Version compatibility**:
* **Detection based on**: Telemetry
* **Supported application or feature**: AuditLogs, OperationalLogs, Devices, DeviceComplianceOrg

**Microsoft Intune** helps you protect your workforce's corporate data by managing devices and apps. **Intune** provides mobile device management (MDM) and mobile app management (MAM) from a secure cloud-based service that is administered using the Microsoft Endpoint Manager admin center. Using **Intune**, you ensure your workforce's corporate resources (data, devices, and apps) are correctly configured, accessed, and updated, meeting your company's compliance policies and requirements.

This setup guide describe how to forward events produced by **Microsoft Intune** to Sekoia.io.

### Configure

To forward **Microsoft Intune** events from Microsoft to Sekoia.io you need to send your event to an **Azure Event Hub** where Sekoia.io will collect the events.

#### Prerequisite

To send **Microsoft Intune** logs to Sekoia.io, there are some prerequisites:

* Have access to the Sekoia.io XDR Operations Center
* Be a Intune Service Administrator to perform the interconnection with **Azure Event Hub**
* Be a Contributor on Azure to setup an **Event Hub**.

{!\_shared\_content/operations\_center/integrations/event\_hub.md!}

#### Send logs from Microsoft Intune to Azure Event Hub

When you have an **Event Hub** follow [this guide](https://learn.microsoft.com/en-us/mem/intune/fundamentals/review-logs-using-azure-monitor) to send your events from **Microsoft Intune** to the **Event Hub**.

#### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Microsoft Intune`.
2. To fill the form, use the table completed during the creation of the **Event Hub**.

**Enjoy your events on the** [**Events page**](https://app.sekoia.io/operations/events)

{!\_shared\_content/operations\_center/integrations/generated/c20528c1-621e-4959-83ba-652eca2e8ed0\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_c20528c1-621e-4959-83ba-652eca2e8ed0\_do\_not\_edit\_manually.md!} {!\_shared\_content/operations\_center/integrations/generated/c20528c1-621e-4959-83ba-652eca2e8ed0.md!}
