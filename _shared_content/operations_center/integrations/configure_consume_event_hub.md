### Create and configure a playbook on Sekoia.io to collect logs from an Azure Event Hub

1. In the playbook section, create a playbook with the Trigger module **Consume Eventhub messages** in Microsoft Azure technology
2. Setup Module configuration (= default)
3. Setup Trigger configuration:
    - **Event Hub** informations: use the file completed during the creation of the **Event Hub**.
        ```   
            - hub_name = **To be completed at step 3** (EntityPath within the `hub_connection_string` AKA the name of the Event Hub)
            - hub_connection_string = **To be completed at step 5** (Connection string–primary key finishing by `Entitypath =`)
            - hub_consumer_group = **To be completed at step 6**
            - storage_container_name = **To be completed at step 7* (EntityPath within the storage_connection_string AKA the name of your container)
            - storage_connection_string = **To be completed at step 8**
        ```
    - Intake informations:
        - intake_key = Intake key that can be found on intake page
        - intake_server = `https://intake.sekoia.io`

**Format example**

- Azure Event Hub’s “Connection string-primary key” (e.g. `"Endpoint=sb://company-eventhub.servicebus.windows.net/;SharedAccessKeyName=sekoiaio;SharedAccessKey=XXXXXX;EntityPath=active-directory-event"`).
- Azure Event Hub’s consumer group name (e.g. `consumergroup_sekoiaio`).
- Azure Blob Storage’s connection string (e.g. `"DefaultEndpointsProtocol=https;AccountName=sekoiaiocheckpoint;AccountKey=XXXXX"`).
<div style="text-align: center;">
    <img width="100%" alt="image" src="/assets/operation_center/integration_catalog/cloud_and_saas/event_hub/playbook_conf.png">
</div>

#### Troubleshoot

Go to events page and search events in last 5 minutes by intake key    `customer.intake_key:"<Your_Intake_Key>"`

**No events**
- Please check the configuration and fill the fields with the right information

- It is possible to investigate on the tab Run and see the response by clicking on the module
<div style="text-align: center;">
    <img width="100%" alt="image" src="/assets/operation_center/integration_catalog/cloud_and_saas/azure_ad/troubleshoot.png">
</div>
