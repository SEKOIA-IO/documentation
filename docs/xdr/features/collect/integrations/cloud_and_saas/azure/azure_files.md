uuid: 70c5c3db-fae8-4825-8d8b-08d6315e1ef6
name: Azure Files
type: intake

## Overview

Azure Files creates monitoring data by using Azure Monitor, which is a full stack monitoring service in Azure.
Azure Monitor provides a complete set of features to monitor your Azure resources and resources in other clouds and on-premises.

This setup guide describe how to forward events produced by `Azure Files` to Sekoia.io.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.
    
{!_shared_content/operations_center/detection/generated/suggested_rules_70c5c3db-fae8-4825-8d8b-08d6315e1ef6_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/70c5c3db-fae8-4825-8d8b-08d6315e1ef6.md!}

## Configure

### Prerequisites

- You need to have `Contributor` role in Azure.
- You should have properly configured [Azure Event Hub](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-create)

### How to setup Event Hub
 
{!_shared_content/operations_center/integrations/event_hub.md!}

### Monitor Azure Files

1. Log on Azure portal
2. Go to `Monitor` 
    
   ![Azure Portal](/assets/playbooks/library/azurefiles/azure_portal.png){ align=right width=150 }

3. Go to `Diagnostic settings`

   ![Diagnostic settings](/assets/playbooks/library/azurefiles/diagnostic_settings.png){ align=right width=150 }

4. Look for the storage account you want to monitor in the list of resources and click on `file` in the sub-resources of the storage account.

   ![Storage Accounts](/assets/playbooks/library/azurefiles/storage_accounts.png){ align=right width=150 }

5. Create a new diagnostic setting by clicking `Add diagnostic setting`
   
   ![New Setting](/assets/playbooks/library/azurefiles/new_setting.png){ align=right width=150 }

6. Type a new for the diagnostic setting
7. In the `Logs` section, select the `audit` checkbox. This action will automatically select the related log categories.
8. In the destination details, select `Stream to an eventhub` section and select the eventhub you created before.

   ![Stream To Eventhub](/assets/playbooks/library/azurefiles/stream_to_eventhub.png){ align=right width=150 }
