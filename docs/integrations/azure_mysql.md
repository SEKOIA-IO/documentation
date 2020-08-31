uuid: 3f99cdd8-aeca-4860-a846-6f2a794583e1
name: Azure MySQL

## Overview
Azure Database for MySQL provides fully managed, enterprise-ready community MySQL database as a service. The service is developed and managed by Microsoft Corp.

## Setup
This setup guide will show you how to forward events produced by Azure MySQL service to SEKOIA.IO.

Theses changes have to be made from the Azure web portal (https://portal.azure.com).

### 1. Event hubs
As a prerequisite you need an `Event Hubs` (e.g. company-eventhub) and to choose an existing `resourceGroup` or create a new one (e.g. company-resource-group).
You also need your `Subscription ID` if you don't have a default one.

Navigate to: `Home > Cost Management + Billing > Subscriptions`. From there, copy the relevant `Subscription ID` that will be used in the command line (e.g. uuid)

Then you use Azure powershell (within Cloud Shell interface for example): you will a create a global `Event Hubs`, then specific `Event Hub` (e.g. mysql-event).

```powershell
PS Azure:\> az eventhubs namespace create --name company-eventhub --resource-group company-resource-group --enable-kafka true --subscription uuid

PS Azure:\> az eventhubs eventhub create --resource-group company-resource-group --namespace-name company-eventhub --name mysql-event --message-retention 3 --partition-count 4 --subscription uuid
```

Navigate to: `Home > Event Hubs > company-eventhub - Shared access policies`. From there, you can create a policy (e.g. RootManageSharedAccessKey) with the claims `Manage`, `Send` and `Listen`, and note the `Primary Key` that will be used as the `SharedAccessKey`.

Navigate to: `Home > Event Hubs > company-eventhub > mysql-event - Shared access policies`. From there, you can create a policy (e.g. sekoiaio-nifi) with the claims `Listen`. Once created, click on the policy and save the `Connection string-primary key`, to be sent to SEKOIA.IO.

Navigate to: `Home > Event Hubs > company-eventhub > mysql-event - Consumer groups`. From there, you can create a consumer group (e.g. sekoiaio-nifi).

### 2. Azure MySQL
You need to activate and configure the Azure MySQL diagnostic settings (e.g. company-mysql).

Navigate to: `Home > SQL databases (e.g. company-mysql) > Monitoring > Diagnostic settings`:

- Add a new diagnostic setting, and select `Stream to an event hub`and click on configure.
- Select the previously created `Event hubs`, `Event Hub` and `SharedAccessKey`.
- In the log section, select `MySqlAuditLogs` and `MySqlSlowLogs`.
- Choose a name for this configuration and click on `Save`.

### 3. Enjoy your events
You can send to Sekoia the `Connection string-primary key` previously mentioned.

Once the configuration has been done on Sekoia side, you can go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.
