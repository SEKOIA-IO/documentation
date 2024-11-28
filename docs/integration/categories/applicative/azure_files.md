uuid: 70c5c3db-fae8-4825-8d8b-08d6315e1ef6
name: Azure Files
type: intake

## Overview

Azure Files creates monitoring data by using Azure Monitor, which is a full stack monitoring service in Azure.
Azure Monitor provides a complete set of features to monitor your Azure resources and resources in other clouds and on-premises.

This setup guide describe how to forward events produced by `Azure Files` to Sekoia.io.

- **Vendor**: Microsoft Azure
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Azure Monitor

## Configure

### Prerequisites

- You need to have `Contributor` role in Azure.
- You should have properly configured [Azure Event Hub](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-create)

### How to setup Event Hub

{!_shared_content/operations_center/integrations/event_hub.md!}

### Monitor Azure Files

* Log on Azure portal
* Go to `Monitor`

   ![Azure Portal](/assets/playbooks/library/azurefiles/azure_portal.png){ align=center }

* Go to `Diagnostic settings`

   ![Diagnostic settings](/assets/playbooks/library/azurefiles/diagnostic_settings.png){ align=center width=150 }

* Look for the storage account you want to monitor in the list of resources and click on `file` in the sub-resources of the storage account.

   ![Storage Accounts](/assets/playbooks/library/azurefiles/storage_accounts.png){ align=center }

* Create a new diagnostic setting by clicking `Add diagnostic setting`

   ![New Setting](/assets/playbooks/library/azurefiles/new_setting.png){ align=center }

* Type a new for the diagnostic setting
* In the `Logs` section, select the `audit` checkbox. This action will automatically select the related log categories.
* In the destination details, select `Stream to an eventhub` section and select the eventhub you created before.

   ![Stream To Eventhub](/assets/playbooks/library/azurefiles/stream_to_eventhub.png){ align=center }

### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Azure Files`. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Consume Eventhub messages](/xdr/features/automate/library/microsoft-azure.md#consume-eventhub-messages)
2. Set up the trigger configuration with the EventHub's `Connection string-primary key`, the hub name, the consumer group, the storage's `Connection string-primary key` and the container name.
3. Start the playbook and enjoy your events

{!_shared_content/operations_center/integrations/generated/70c5c3db-fae8-4825-8d8b-08d6315e1ef6_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_70c5c3db-fae8-4825-8d8b-08d6315e1ef6_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/70c5c3db-fae8-4825-8d8b-08d6315e1ef6.md!}