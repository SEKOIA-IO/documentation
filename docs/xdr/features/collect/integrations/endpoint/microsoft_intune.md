uuid: c20528c1-621e-4959-83ba-652eca2e8ed0
name: Microsoft Intune
type: intake

## Overview

Microsoft Intune helps you protect your workforce's corporate data by managing devices and apps. Intune provides mobile device management (MDM) and mobile app management (MAM) from a secure cloud-based service that is administered using the Microsoft Endpoint Manager admin center. Using Intune, you ensure your workforce's corporate resources (data, devices, and apps) are correctly configured, accessed, and updated, meeting your company's compliance policies and requirements.

This setup guide describe how to forward events produced by `Microsoft Intune` to SEKOIA.IO.
{!_shared_content/operations_center/detection/generated/suggested_rules_c20528c1-621e-4959-83ba-652eca2e8ed0_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/microsoft-intune_do_not_edit_manually.md!}

## Configure

### Prerequisites

To forward events to SEKOIA.IO, create [an Event hub namespace and an Event hub](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-create) with a consumergroup.

Once created, in your EventHubs, go to `Setting > Shared access policies`.
Create a new policy with the option `Listen` then copy the `Connection string-primary key`.

Create a [Storage accounts](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create) or use an existing one. Go to `Data storage > containers` and create a new container.
Then go to `Security + networking > Access keys` and copy the key1 `Connection string`

Configure Microsoft Intune door to stream its logs to the EventHub with [this guide](https://learn.microsoft.com/en-us/mem/intune/fundamentals/review-logs-using-azure-monitor).

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Microsoft Intune.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Consume Eventhub messages](../../../automate/library/microsoft-azure.md#consume-eventhub-messages). 

Set up the trigger configuration with the EventHub's `Connection string-primary key`, the hub name, the consumer group, the storage's `Connection string-primary key` and the container name.

Start the playbook and enjoy your [events](https://app.sekoia.io/operations/events).

## Further Readings

- [Microsoft Azure Intune logs](https://learn.microsoft.com/en-us/mem/intune/fundamentals/review-logs-using-azure-monitor)
