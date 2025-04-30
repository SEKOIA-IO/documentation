## Collect Office365 events through Azure EventHub

This is the alternative way to collect Office365 events.

### Prerequisites

This setup guide will show you how to generate, store and forward events produced by Office 365 service to Sekoia.io.
Theses changes have to be made from the Azure web portal ([https://portal.azure.com](https://portal.azure.com)).

### A. Event Hubs

As a prerequisite you need an `Event Hub` (e.g. company-eventhub) and to choose an existing `resourceGroup` or create a new one (e.g. company-resource-group).
You also need your `Subscription ID` if you don't have a default one.

Navigate to: `Home > Cost Management + Billing > Subscriptions`. From there, copy the relevant `Subscription ID` that will be used in the command line (e.g. uuid)
Then you use Azure PowerShell (within Cloud Shell interface for example): you will create a global `Event Hubs`, then specific `Event Hub` (e.g. o365-event).
```powershell
PS Azure:\> az eventhubs namespace create --name company-eventhub --resource-group company-resource-group --enable-kafka true --subscription uuid

PS Azure:\> az eventhubs eventhub create --resource-group company-resource-group --namespace-name company-eventhub --name o365-event --message-retention 3 --partition-count 4 --subscription uuid
```

Navigate to: `Home > Event Hubs > company-eventhub - Shared access policies`. From there, you can create a policy (e.g. RootManageSharedAccessKey) with the claims `Manage`, `Send` and `Listen`, and note the `Primary Key` that will be used as the `SharedAccessKey`.
Navigate to: `Home > Event Hubs > company-eventhub > o365-event - Shared access policies`. From there, you can create a policy (e.g. sekoiaio-nifi) with the claims `Listen`.
> Once created, click on the policy and save the `Connection string-primary key`, to be sent to Sekoia.io.
Navigate to: `Home > Event Hubs > company-eventhub > o365-event - Consumer groups`. From there, you can create a consumer group (e.g. sekoiaio-nifi).

### B. Office 365

Office 365 has to be added through Azure portal following the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/azure-monitor/insights/solution-office-365)

Then you need to activate and configure the Office 365 diagnostic settings.
Navigate to: `Home > Office 365 > Monitoring > Diagnostic settings`:
- Add a new diagnostic setting, and select `Stream to an event hub`and click on configure.
- Select the previously created `Event hubs`, `Event Hub` and `SharedAccessKey`.
- Choose a name for this configuration and click on `Save`.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes), create a new intake from the format `Office365` and choose the manual way.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Consume Eventhub messages](../../../../automate/library/microsoft-azure.md#consume-eventhub-messages). 

Set up the trigger configuration with the EventHub's `Connection string-primary key`, the hub name, the consumer group, the storage's `Connection string-primary key` and the storage's container.

Start the playbook and enjoy your [events](https://app.sekoia.io/operations/events).

## Further Readings
- [Microsoft Stream Azure monitoring data to an event hub](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/stream-monitoring-data-event-hubs)