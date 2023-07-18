uuid: 19cd2ed6-f90c-47f7-a46b-974354a107bb
name: Azure Active Directory
type: intake

## Overview

Azure Active Directory is a cloud-based Identity and Rights management service. The service is developed and managed by Microsoft Corp.

{!_shared_content/operations_center/detection/generated/suggested_rules_19cd2ed6-f90c-47f7-a46b-974354a107bb_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/19cd2ed6-f90c-47f7-a46b-974354a107bb.md!}

## Configure

This setup guide will show you how to forward events produced by Azure Active Directory service to SEKOIA.IO.

Theses changes have to be made from the [Azure Web Portal](https://portal.azure.com).

### Azure Event Hubs

As a prerequisite, you need to choose an existing “resource group”, or create a new one (e.g. `company-resource-group`).

#### Retrieve your Subscription ID

You also need your “Subscription ID” if you don't have a default one. In Azure Web Portal, navigate to: “Home”, “Cost Management + Billing”, ”Subscriptions”. From there, copy the relevant “Subscription ID” that will be used in the command line (e.g. `uuid`)

#### Create the Event Hubs

Use Azure PowerShell (within Cloud Shell interface for example) to create a namespace (e.g. `company-eventhub`) and a specific `Event Hub` (e.g. `active-directory-event`) within your “resource group” (e.g. `company-resource-group`)

```powershell
PS Azure:\> az eventhubs namespace create --name company-eventhub --resource-group company-resource-group --enable-kafka true --subscription uuid
```

```powershell
PS Azure:\> az eventhubs eventhub create --resource-group company-resource-group --namespace-name company-eventhub --name active-directory-event --message-retention 3 --partition-count 4 --subscription uuid
```

!!! info
    Please replace :

    - `company-resource-group` with the name of your “resource group”.
    - `uuid` with your subscription ID retrieved previously (see below).

#### Create “Shared Access Policies”

1. Navigate to “Home”, “Event Hubs”, “company-eventhub - Shared access policies”. From there, you can create a policy (e.g. `RootManageSharedAccessKey`) with the claims `Manage`, `Send` and `Listen`, and note the `Primary Key` that will be used as the `SharedAccessKey`.
2. Navigate to “Home”, “Event Hubs”, “company-eventhub”, “active-directory-event - Shared access policies”. From there, you can create a policy (e.g. `sekoiaio`) with the claims `Listen`. Once created, click on the policy and save the `Connection string-primary key`, to be sent to SEKOIA.IO.
3. Navigate to “Home”, “Event Hubs”, “company-eventhub”, ”active-directory-event - Consumer groups”. From there, you can create a consumer group (e.g. `consumergroup_sekoiaio`).

#### Create a Blob Storage for Checkpointing

In order to allow SEKOIA.IO keep track of the consumed events, the next step consists in creating a dedicated Azure Blob Storage.

To proceed, you can use Azure PowerShell:

```powershell
PS Azure:\> az storage account create --name "sekoiaiocheckpoint" --resource-group "company-resource-group"
```

```powershell
PS Azure:\> az storage container create --name "active-directory-event" --account-name "sekoiaiocheckpoint"
```

!!! info
    The container name, here `active-directory-event` should be the same as the Event Hub’s one.
    You also need to replace `company-resource-group` with the name of your “resource group”.

Finally, you have to retrieve the connection string from Azure Web Portal by going in “Storage Accounts”, then in the created storage (`sekoiaiocheckpoint`) and finally in the “Access Keys” section. After clicking on “Show keys”, you can copy the first of the two connection strings.

### Azure Active Directory

You need to activate and configure the Azure Active Directory diagnostic settings (e.g. `company-ad`).

Navigate to “Home”, “Azure Active Directory” (e.g. `company-ad`), “Monitoring”, ”Diagnostic settings”:

- Add a new diagnostic setting, and select “Stream to an event hub” and click on configure.
- Select the previously created “Event hubs”, “Event Hub” and “SharedAccessKey”.
- In the log section, select “AuditLogs” and “SignInLogs”.
- Choose a name for this configuration and click on “Save”.

### Connection Keys to SEKOIA.IO via Playbook

Last step to integrate your log into SEKOIA.IO, please follow the steps below:

1. Create a playbook with Trigger module **Consume Eventhub messages** in Microsoft Azure technology
2. Setup Module configuration (= default)

3. Setup Trigger configuration

 - hub_connection_string = Connection string–primary key finishing by `Entitypath =`
 - hub_consumer_group = Consumer Group name (eg. `consumergroup_sekoiaio`)
 - hub_name = value of EntityPath
 - intake_key = Microsoft Azure Intake key that can be found on intake page
 - intake_server = `https://intake.sekoia.io`
 - storage_connection_string = Storage Connection string
 - storage_container_name = value of EntityPath

**Format example**

- Azure Event Hub’s “Connection string-primary key” (e.g. `"Endpoint=sb://company-eventhub.servicebus.windows.net/;SharedAccessKeyName=sekoiaio;SharedAccessKey=XXXXXX;EntityPath=active-directory-event"`).
- Azure Event Hub’s consumer group name (e.g. `consumergroup_sekoiaio`).
- Azure Blob Storage’s connection string (e.g. `"DefaultEndpointsProtocol=https;AccountName=sekoiaiocheckpoint;AccountKey=XXXXX"`).

<img width="100%" alt="image" src="https://user-images.githubusercontent.com/101662967/185440012-876508a5-bdf6-4ad5-a212-6f4f7bc0564e.png">

### Troubleshoot

Go to events page and search events in last 5 minutes by Azure AD intake key    `customer.intake_key:"<Your_AzureAD_Intake_Key>"`

**No events**
- Please check the configuration and fill the fields with the right information

- It is possible to investigate on the tab Run and see the response by clicking on the module
<img width="100%" alt="image" src="/assets/operation_center/integration_catalog/cloud_and_saas/azure_ad/troubleshoot.png">

## Further Readings

- [Microsoft Github diagnostic Active Directory documentation](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/active-directory/reports-monitoring/tutorial-azure-monitor-stream-logs-to-event-hub.md)
