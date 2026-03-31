# azure\_files

uuid: 70c5c3db-fae8-4825-8d8b-08d6315e1ef6 name: Azure Files type: intake

### Overview

Azure Files creates monitoring data by using Azure Monitor, which is a full stack monitoring service in Azure. Azure Monitor provides a complete set of features to monitor your Azure resources and resources in other clouds and on-premises.

This setup guide describe how to forward events produced by `Azure Files` to Sekoia.io.

* **Vendor**: Microsoft Azure
* **Supported environment**: SaaS
* **Detection based on**: Telemetry
* **Supported application or feature**: Azure Monitor

### Configure

#### Prerequisites

* You need to have `Contributor` role in Azure.
* You should have properly configured [Azure Event Hub](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-create)

#### How to setup Event Hub

{!\_shared\_content/operations\_center/integrations/event\_hub.md!}

#### Monitor Azure Files

* Log on Azure portal
*   Go to `Monitor`

    { align=center }
*   Go to `Diagnostic settings`

    { align=center width=150 }
*   Look for the storage account you want to monitor in the list of resources and click on `file` in the sub-resources of the storage account.

    { align=center }
*   Create a new diagnostic setting by clicking `Add diagnostic setting`

    { align=center }
* Type a new for the diagnostic setting
* In the `Logs` section, select the `audit` checkbox. This action will automatically select the related log categories.
*   In the destination details, select `Stream to an eventhub` section and select the eventhub you created before.

    { align=center }

#### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Azure Files`.

Set up the intake configuration with the EventHub's `Connection string-primary key`, the hub name, the consumer group, the storage's `Connection string-primary key` and the container name.

\{% include "\_shared\_content/operations\_center/integrations/generated/70c5c3db-fae8-4825-8d8b-08d6315e1ef6\_sample.md" %\}

\{% include "\_shared\_content/integration/detection\_section.md" %\}

\{% include "\_shared\_content/operations\_center/detection/generated/suggested\_rules\_70c5c3db-fae8-4825-8d8b-08d6315e1ef6\_do\_not\_edit\_manually.md" %\}

\{% include "\_shared\_content/operations\_center/integrations/generated/70c5c3db-fae8-4825-8d8b-08d6315e1ef6.md" %\}

{% include "../../.gitbook/includes/untitled.md" %}

