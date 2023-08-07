### Create and configure a playbook on Sekoia.io to collect logs from an Azure Event Hub

1. In the playbook section, create a playbook with the Trigger module **Consume Eventhub messages** in Microsoft Azure technology
2. Setup Module configuration (= default)

3. Setup Trigger configuration

 - hub_connection_string = Connection string–primary key finishing by `Entitypath =` that was found in **Create an Azure Event Hub : step 4**.
 - hub_consumer_group = Consumer Group name found in **Create an Azure Event Hub : step 5** (eg. `consumergroup_sekoiaio`)
 - hub_name = value of EntityPath within the `hub_connection_string` AKA the name of the Event Hub you specified in **Create an Azure Event Hub : step 2**
 - intake_key = Intake key that can be found on intake page
 - intake_server = `https://intake.sekoia.io`
 - storage_connection_string = Storage Connection string, found in **Create an Azure Event Hub : step 7**
 - storage_container_name = value of EntityPath within the storage_connection_string AKA the name of your Blob Storage (container name), created in **Create an Azure Event Hub : step 6** (eg. `eventhubname`)

**Format example**

- Azure Event Hub’s “Connection string-primary key” (e.g. `"Endpoint=sb://company-eventhub.servicebus.windows.net/;SharedAccessKeyName=sekoiaio;SharedAccessKey=XXXXXX;EntityPath=active-directory-event"`).
- Azure Event Hub’s consumer group name (e.g. `consumergroup_sekoiaio`).
- Azure Blob Storage’s connection string (e.g. `"DefaultEndpointsProtocol=https;AccountName=sekoiaiocheckpoint;AccountKey=XXXXX"`).

<img width="100%" alt="image" src="https://user-images.githubusercontent.com/101662967/185440012-876508a5-bdf6-4ad5-a212-6f4f7bc0564e.png">

#### Troubleshoot

Go to events page and search events in last 5 minutes by intake key    `customer.intake_key:"<Your_Intake_Key>"`

**No events**
- Please check the configuration and fill the fields with the right information

- It is possible to investigate on the tab Run and see the response by clicking on the module
<img width="100%" alt="image" src="/assets/operation_center/integration_catalog/cloud_and_saas/azure_ad/troubleshoot.png">