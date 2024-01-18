uuid: 3f99cdd8-aeca-4860-a846-6f2a794583e1
name: Azure MySQL
type: intake

## Overview

Azure Database for MySQL provides fully managed, enterprise-ready community MySQL database as a service. The service is developed and managed by Microsoft Corp.

{!_shared_content/operations_center/detection/generated/suggested_rules_3f99cdd8-aeca-4860-a846-6f2a794583e1_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/3f99cdd8-aeca-4860-a846-6f2a794583e1.md!}

## Configure

This setup guide will show you how to forward events produced by Azure MySQL service to Sekoia.io.

Theses changes have to be made from the [Azure Web Portal](https://portal.azure.com).

### Azure Event Hubs

As a prerequisite, you need to choose an existing **resource group**, or create a new one (e.g. `company-resource-group`).

#### Retrieve your Subscription ID

You also need your **Subscription ID** if you don't have a default one. 

In Azure Web Portal:

1. Navigate to: `Home` > `Cost Management + Billing` > `Subscriptions`
2. From there, copy the relevant **Subscription ID** that will be used in the command line (e.g. `uuid`)

#### Create the Event Hubs

Use Azure PowerShell (within Cloud Shell interface for example) to create a **namespace** (e.g. `company-eventhub`) and a specific **Event Hub** (e.g. `mysql-event`) within your **resource group** (e.g. `company-resource-group`)

```powershell
PS Azure:\> az eventhubs namespace create --name company-eventhub --resource-group company-resource-group --enable-kafka true --subscription uuid
```

```powershell
PS Azure:\> az eventhubs eventhub create --resource-group company-resource-group --namespace-name company-eventhub --name mysql-event --message-retention 3 --partition-count 4 --subscription uuid
```

!!! info
    Please replace :

    - `company-resource-group` with the name of your **resource group**
    - `uuid` with your subscription ID retrieved previously (see below)

#### Create “Shared Access Policies”

1. Navigate to `Home` > `Event Hubs`> `company-eventhub - Shared access policies`
    - From there, you can create a **policy** (e.g. `RootManageSharedAccessKey`) with the claims `Manage`, `Send` and `Listen` and note the **Primary Key** that will be used as the **SharedAccessKey**

2. Navigate to `Home` > `Event Hubs` > `company-eventhub` > `mysql-event - Shared access policies`
    - From there, you can create a **policy** (e.g. `sekoiaio`) with the claims `Listen`
    - Once created, click on the policy and save the **Connection string-primary key**, to be sent to Sekoia.io

5. Navigate to `Home`> `Event Hubs`> `company-eventhub`> `mysql-event - Consumer groups`
    - From there, you can create a **consumer group** (e.g. `sekoiaio`)

#### Create a Blob Storage for Checkpointing

In order to allow Sekoia.io, keep track of the consumed events, the next step consists in creating a dedicated Azure Blob Storage.

To proceed, you can use Azure PowerShell:

```powershell
PS Azure:\> az storage account create --name "sekoiaiocheckpoint" --resource-group "company-resource-group"
```

```powershell
PS Azure:\> az storage container create --name "mysql-event" --account-name "sekoiaiocheckpoint"
```

!!! info
    The container name, here `mysql-event` should be the same as the Event Hub’s one.
    You also need to replace `company-resource-group` with the name of your **resource group**.

Finally, you have to retrieve the **connection string** from Azure Web Portal by going in **Storage Accounts**, then in the created storage (`sekoiaiocheckpoint`) and finally in the **Access Keys** section. After clicking on **Show keys**, you can copy the first of the two connection strings.

### Azure MySQL

You need to activate and configure the Azure MySQL diagnostic settings (e.g. `company-mysql`).
To configure these settings, follow these steps: 

1. Navigate to `Home` > `SQL databases` (e.g. `company-mysql`) > `Monitoring` > `Diagnostic settings`
2. Add a new diagnostic setting, select **Stream to an event hub** and click on Configure
3. Select the previously created **Event hubs**, **Event Hub** and **SharedAccessKey**
4. In the log section, select **MySqlAuditLogs** and **MySqlSlowLogs**
5. Choose a name for this configuration and click on **Save**

### Forward the Connection Keys to Sekoia.io

Finally, please send to Sekoia.io the following information:

- Azure Event Hub’s **Connection string-primary key** (e.g. `"Endpoint=sb://company-eventhub.servicebus.windows.net/;SharedAccessKeyName=sekoiaio;SharedAccessKey=XXXXXX;EntityPath=mysql-event"`)
- Azure Event Hub’s **consumer group name** (e.g. `sekoiaio`)
- Azure Blob Storage’s **connection string** (e.g. `"DefaultEndpointsProtocol=https;AccountName=sekoiaiocheckpoint;AccountKey=XXXXX"`)
