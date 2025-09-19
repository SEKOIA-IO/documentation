uuid: 99a97295-dad0-4deb-af50-521c76cad45d
name: Azure Network Watcher Flow Logs
type: intake

## Overview
Azure Network Watcher provide insights into the traffic flowing within and out of your Azure Virtual Network. Virtual Network flow logs capture detailed information about allowed and denied network traffic, helping to enhance security and network monitoring. Sending flow logs to Sekoia.io will allow you to detect threats from the IP traffic, thanks to daily contextualized and actionable cyber threat indicators.

- **Vendor**: Microsoft Azure
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Host network interface, Netflow/Enclave netflow, Network device logs, Network protocol analysis

## Configure

### Register Insights provider

1. Log into Azure console
2. In the search bar, enter `Subscriptions`

   ![Subscriptions](/assets/instructions/azure_network_watcher_flow_logs/subscriptions.png){ align=center width=100% }

3. Click your subscription

   ![Single Subscription](/assets/instructions/azure_network_watcher_flow_logs/single_subscription.png){ align=center width=100% }

4. On the left panel, go to `Settings` > `Resource providers`

   ![Resource Providers](/assets/instructions/azure_network_watcher_flow_logs/resource_providers.png){ align=center width=100% }

5. Search the Insight providers, select `microsoft.insights` and click `Register`

   ![Microsoft Insights](/assets/instructions/azure_network_watcher_flow_logs/microsoft_insights.png){ align=center width=100% }

### Create a new flow log

1. Go to `Network Watcher`
2. On the left panel, go to `Logs` > `Flow Logs`
3. Click `+ Create`

   ![Create Flow Log](/assets/instructions/azure_network_watcher_flow_logs/create_flow_log.png){ align=center width=100% }

4. Select the subscription to associate to the flow log
5. Select `Virtual network` as the Flow log type
6. Select a target resource
7. Select a existing storage account or create a new one. If you need to create a new storage account, we recommend creating a StorageV2 account kind.

   ![Storage Account](/assets/instructions/azure_network_watcher_flow_logs/storage_account.png){ align=center width=100% }

8. Enter a retention period for the logs
9. Click `Review + create`

   ![Review + Create](/assets/instructions/azure_network_watcher_flow_logs/review_create.png){ align=center width=100% }

10. In the review, Click `Create`
    
   ![Create](/assets/instructions/azure_network_watcher_flow_logs/review_create_1.png){ align=center width=100% }

### Get the credentials

1. Go to your storage account
2. Go to `Data storage` > `container` and copy the name of your new container (`insight-logs-flowlogflowevent`)

   ![Container](/assets/instructions/azure_network_watcher_flow_logs/container.png){ align=center width=100% }

3. Go to `Data storage` > `Access Key`
4. Copy the storage account name and the key

   ![Access Key](/assets/instructions/azure_network_watcher_flow_logs/access_key.png){ align=center width=100% }

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Azure Network Watcher Flow Logs`.

{!_shared_content/operations_center/integrations/generated/99a97295-dad0-4deb-af50-521c76cad45d_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_99a97295-dad0-4deb-af50-521c76cad45d_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/99a97295-dad0-4deb-af50-521c76cad45d.md!}

## Further Readings
- [Azure Network Watcher overview](https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview)
- [Create, change, enable, disable, or delete virtual network flow logs](https://learn.microsoft.com/en-us/azure/network-watcher/vnet-flow-logs-manage?tabs=portal)
