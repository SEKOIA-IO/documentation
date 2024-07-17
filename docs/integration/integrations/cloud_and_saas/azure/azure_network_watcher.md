uuid: 340e3bc7-2b76-48e4-9833-e971451b2979
name: Azure Network Watcher (NSG flow logs)
type: intake

## Overview
Azure Network Watcher provides tools to monitor, diagnose, view metrics, and enable or disable logs for resources in an Azure virtual network. It also allows to log information about IP traffic flowing through a network security group: NSG flow logs.

{!_shared_content/operations_center/detection/generated/suggested_rules_340e3bc7-2b76-48e4-9833-e971451b2979_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/340e3bc7-2b76-48e4-9833-e971451b2979.md!}

## Configure
Please contact your support to discuss about the network security group to monitor in your Azure infrastructure in order to find the appropriate solution to forward your logs to Sekoia.io.

This setup guide will show you a method to enable and give us access to NSG flow logs produced by Azure Network Watcher service to Sekoia.io.

### Enable NSG flow logs

The following instructions are provided for the Azure web portal (https://portal.azure.com).

As a prerequisite you need at least one virtual machine with a network security group, to enable Network Watcher and to register the Microsoft.Insights provider.

Navigate to the Network Watcher service, and select `NSG flow logs` under `LOGS`. From the list of NSGs, select your VM(s), and under `Flow logs settings`, select `On` to enable the NSG flow logs. Please, select the Version 2 NSG flow log format sample which is integrated to the Operations Center.

These instructions are illustrated and more detailled [here](https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-nsg-flow-logging-portal).

### Share access to logs

This part should be discussed with Sekoia.io people to find an appropriate solution to forward your flow logs to Sekoia.io.

A possible solution consists of sharing:
- An access key for the Azure Blob Storage
- A storage token associated with the resources to share
- The name of the container where the NSG flow logs are stored

From this information, we will be able to retrieve each _PT1h.json_ blob which contains the flow logs.

## Further Readings
- [Azure Network Watcher overview](https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview)
- [Azure Network Watcher NSG flow logging overview](https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-nsg-flow-logging-overview)
