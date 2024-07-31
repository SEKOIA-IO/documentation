### Create and configure a playbook on Sekoia.io to collect logs from an Azure Event Hub

1. In the playbook section, create a playbook with the Trigger module **Consume Eventhub messages** in Microsoft Azure technology
2. Setup Module configuration (= default)
3. Setup Trigger configuration:
    - **Event Hub** informations: use the table completed during the creation of the **Event Hub**.
    - Intake informations:
        - intake_key = Intake key that can be found on intake page
        - intake_server = `https://intake.sekoia.io`

<div style="text-align: center;">
    <img width="100%" alt="image" src="/assets/integration/cloud_and_saas/event_hub/playbook_conf.png">
</div>

#### Troubleshoot

Go to events page and search events in last 5 minutes by intake key    `customer.intake_key:"<Your_Intake_Key>"`

**No events**
- Please check the configuration and fill the fields with the right information

- It is possible to investigate on the tab Run and see the response by clicking on the module
<div style="text-align: center;">
    <img width="100%" alt="image" src="/assets/integration/cloud_and_saas/azure_ad/troubleshoot.png">
</div>
