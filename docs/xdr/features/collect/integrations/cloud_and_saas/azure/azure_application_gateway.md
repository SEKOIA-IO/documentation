uuid: 6967b0ca-f27e-480a-b124-fa4ab0b9d889
name: Azure Application Gateway
type: intake

## Overview
Azure Application Gateway is a web traffic load balancer that manages traffic to your web applications with advanced routing, SSL termination, and Web Application Firewall (WAF) features. It ensures high availability, scalability, and integrates seamlessly with other Azure services for efficient deployment and management. Additionally, it offers insights and diagnostics to monitor and optimize application performance.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Supported events

This integration supports the following events:

- Access logs
- Firewall logs

{!_shared_content/operations_center/detection/generated/suggested_rules_6967b0ca-f27e-480a-b124-fa4ab0b9d889_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/6967b0ca-f27e-480a-b124-fa4ab0b9d889.md!}

## Configure

### Prerequisites

- You need to have `Contributor` role in Azure.
- You should have properly configured [Azure Event Hub](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-create)

### How to setup Event Hub
 
{!_shared_content/operations_center/integrations/event_hub.md!}

### Enable Application Gateway diagnostics logs

The following instructions are provided for the Azure web portal (https://portal.azure.com).

1. In the Azure portal, find your resource and select Diagnostic settings.
2. To start collecting data, select Turn on diagnostics.
3. The Diagnostics settings page provides the settings for the diagnostic logs. You should use Event Hub configuration. More details about how it works you can find [here](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log?tabs=powershell#send-to-azure-event-hubs)
   * Please select Access Logs and Firewall Logs to stream them to the Event Hub.
4. Type a name for the settings, confirm the settings, and select Save.

These instructions are illustrated and more detailed [here](https://learn.microsoft.com/en-us/azure/application-gateway/application-gateway-diagnostics#enable-logging-through-the-azure-portal).

### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Azure Application Gateway`. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Consume Eventhub messages](/xdr/feature/automate/library/microsoft-azure.md#consume-eventhub-messages)
2. Set up the trigger configuration with the EventHub's `Connection string-primary key`, the hub name, the consumer group, the storage's `Connection string-primary key` and the container name.
3. Start the playbook and enjoy your events

## Further Readings
- [Diagnostic logs for Application Gateway](https://learn.microsoft.com/en-us/azure/application-gateway/application-gateway-diagnostics)
- [Send Azure Monitor activity log data](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log?tabs=powershell#send-to-azure-storage)
