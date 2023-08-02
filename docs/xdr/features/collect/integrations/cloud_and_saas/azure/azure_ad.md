name: Azure Active Directory
type: intake

## Overview

Azure Active Directory is a cloud-based Identity and Rights management service. The service is developed and managed by Microsoft Corp.

{!_shared_content/operations_center/detection/generated/suggested_rules_19cd2ed6-f90c-47f7-a46b-974354a107bb_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/19cd2ed6-f90c-47f7-a46b-974354a107bb.md!}

## Configure

This setup guide will show you how to forward events produced by Azure Active Directory service to Sekoia.io.

Theses changes have to be made from the [Azure Web Portal](https://portal.azure.com).

### Azure Event Hubs

As a prerequisite, you need to choose an existing “resource group”, or create a new one (e.g. `company-resource-group`).

#### Step 1: Retrieve your Subscription ID

If you don't have a default one, in Azure Web Portal, go to: "Home" -  "Cost Management + Billing" - "Subscriptions". 

From there, keep the relevant “Subscription ID” that will be used along the process (e.g. `uuid`).

#### Step 2: Create Event Hub Namespace and associated Event Hub

Use Azure PowerShell (within Cloud Shell interface for example) to create an Event Hub Namespace and a specific "Event Hub" (that will be created within this Event Hub Namespace).

All of these resources will be created within your Resource Group (e.g. `company-resource-group`).


```powershell
PS Azure:\> az eventhubs namespace create --name company-eventhubnamespace --resource-group company-resource-group --enable-kafka true --subscription uuid
```

!!! info
    Please replace :
    
    - `company-resource-group` with the name of your “resource group”.
    - `uuid` with your subscription ID retrieved previously (see above).
    - `company-eventhubnamespace` with the name you wish for your Event Hub Namespace
    
```powershell
PS Azure:\> az eventhubs eventhub create --resource-group company-resource-group --namespace-name company-eventhub --name active-directory-event --message-retention 3 --partition-count 4 --subscription uuid
```

!!! info
    Please replace :
    
    - `company-resource-group` with the name of your “resource group”.
    - `uuid` with your subscription ID retrieved previously (see above).
    - `active-directory-event` with the name you wish for your Event Hub

#### Step 3: Create “Shared Access Policies” for the Event Hub Namespace 

Navigate to “Home”, “Event Hubs”, “company-eventhubnamespace - Shared access policies”. 

From there, you can create a policy (e.g. `RootManageSharedAccessKey`) with the claims `Manage`, `Send` and `Listen`.

!!! info
    Carefully store the `Connection String Primary Key` that will be used as the `SharedAccessKey` in step 8.

#### Step 4: Create “Shared Access Policies” for the Event Hub 

Navigate to “Home”, “Event Hubs”, “company-eventhubnamespace”, “active-directory-event - Shared access policies”. 

From there, you can create a policy (e.g. `sekoiaio`) with the claims `Listen`. 

Once created, click on the policy.

!!! info
    Carefully store the `Connection String Primary Key` that will be used in step 10.
    

#### Step 5: Create a Consumer group
   
Navigate to “Home”, “Event Hubs”, “company-eventhubnamespace”, ”active-directory-event - Consumer groups”. 

From there, you can create a consumer group (e.g. `consumergroup_sekoiaio`).

!!! info
    Carefully store the Consumer Group name that will be used in step 10.

#### Step 6: Create a Blob Storage for Checkpointing

In order to allow Sekoia.io keep track of the consumed events, the next step consists in creating a dedicated Azure Blob Storage.

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

#### Step 7: Retrieve Connection String

You have to retrieve the connection string from Azure Web Portal.

Go to “Storage Accounts”, "sekoiacheckpoint", "Access Keys". 

Click on "Show Keys" on the first Connection String. 
![Connection Stirng](https://github.com/jdpju/documentation/assets/113444861/dc6e176c-ac19-46d4-a65a-b97a1331a2d8)

!!! info
    Carefully store the Connection String that will be used in step 10.

### Step 8: Activate Azure Active Directory diagnostic settings

You need to activate and configure the Azure Active Directory diagnostic settings (e.g. `company-ad`).

Navigate to “Home”, “Azure Active Directory” (e.g. `company-ad`), “Monitoring”, ”Diagnostic settings”:

- Add a new diagnostic setting, and select “Stream to an event hub” and click on configure.
- Select the previously created “Event hubs”, “Event Hub” and “SharedAccessKey” (**see step 2**).
- In the log section, select “AuditLogs” and “SignInLogs”.
- Choose a name for this configuration and click on “Save”.
  
![diag](https://github.com/jdpju/documentation/assets/113444861/b5e55fd3-da86-4f2f-8095-3c1704ae7a20)

### Step 9: Create an Azure ID intake on your Sekoia.io community

Go to your Sekoia.io console. 

Go to the intake page. 

Click on the '+' on the top-right corner to add an Azure AD intake.

Create the intake. 

Once the intake is created, carefully store the intake key for the Azure AD intake you just created: 

<img width="1438" alt="image" src="https://github.com/jdpju/documentation/assets/113444861/9b92b2b3-8840-4497-a77c-f1948685c361">

### Step 10: Create and configure a playbook on Sekoia.io to collect your logs 

The last step to integrate your log into Sekoia.io, is to create a playbook that will consume your logs.
To do so, please go the playbook section. 

1. Create a playbook with the Trigger module **Consume Eventhub messages** in Microsoft Azure technology
2. Setup Module configuration (= default)

3. Setup Trigger configuration

 - hub_connection_string = Connection string–primary key finishing by `Entitypath =` that was found in **step 4**.
 - hub_consumer_group = Consumer Group name found in **step 5** (eg. `consumergroup_sekoiaio`)
 - hub_name = value of EntityPath within the `hub_connection_string` AKA the name of the Event Hub you specified in **step 2**
 - intake_key = Microsoft Azure Intake key that can be found on intake page, found in **step 9**
 - intake_server = `https://intake.sekoia.io`
 - storage_connection_string = Storage Connection string, found in **step 7**
 - storage_container_name = value of EntityPath within the storage_connection_string AKA the name of your Blob Storage (container name), created in **step 6** (eg. `active-directory-event`)

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
