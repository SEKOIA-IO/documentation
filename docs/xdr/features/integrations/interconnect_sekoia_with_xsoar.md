# Synchronize Alerts with Palo Alto Cortex XSOAR

This use case describes how to automatically create an incident on Palo Alto Cortex XSOAR when a new alert is raised on Sekoia.io.

This integration uses the Sekoia.io Playbook and the Generic Webhook of Palo Alto XSOAR to interact between both products.
Some information will be automatically sent to Cortex XSOAR but you will be able to adapt it to your needs.

Here is a schema that illustrates this interconnection:

![Sekoia Cortex XSOAR Schema](/assets/operation_center/external_integrations/sekoia_xsoar_integration.png){: style="max-width:100%"}

## Prerequisites

- A Sekoia.io XDR licence
- Access to Sekoia.io Playbooks 
- The user who configures the Playbook should have access to the Sekoia.io Playbooks
- An API Key with a role that contains at least the following permissions:
	* `SIC_READ_ALERTS`
	* `SIC_READ_INTAKES`
	* The `SYMPHONY_*` permissions
- Admin access to Cortex XSOAR
- Cortex XSOAR available on the internet

!!! Note
    To create your API Key, follow this [documentation](../../../../getting_started/manage_api_keys/#create-an-api-key).

## Configure

### Create an new Incident type on Palo Alto Cortex XSOAR
A dedicated incident type for Sekoia.io will enable specific Incident Fields and decide what XSOAR playbook to use.

Follow these steps to create a new Incident type: 

1. From the XSOAR GUI, click on `Settings` > `OBJECTS SETUP` > `Types`
2. Click on `+ New Incident Type` and give it the name `Sekoia.io`. Please configure the other parameters depending on your needs.
3. Click on `Save`

### Create a webhook on Palo Alto Cortex XSOAR
To allow Sekoia.io to create a new incident when a new alert is raised, we need to create a Webhook.

To create this webhook, follow these steps:

1. From the XSOAR GUI, install the `Generic Webhook` published by XSOAR from the Market Place
2. Go to `Settings` > `INTEGRATIONS` > `Instances` and search `Generic Webhook`
3. Click on `Add instance` and give it the name `sekoia`
4. Under `Incident type`, select `Sekoia.io`
5. Follow the webhook documentation and configure Cortex XSOAR server rerouting to make your webhook available from your XSOAR Url in HTTPS
6. Fill out `Username` with `_header: Authorization` and `Password` with `Bearer YOUR_XSOAR_TOKEN`. Replace `YOUR_XSOAR_TOKEN` with a complex string. It will be used as an authentication
7. To be able to map information easily into XSOAR, check the option `Store sample events for mapping`
8. Click on `Save and exit`

### Create and configure a playbook on Sekoia.io
To create and configure a Cortex XSOAR playbook on Sekoia.io, follow these steps: 

1. Go the [Playbook page](https://app.sekoia.io/operations/playbooks) page and click `+ Playbook`
2. Select `Use a template` and choose the template `Automatically create an incident on Palo Alto Cortex XSOAR`
3. Click on the `Alert Created` module to configure it
4. On the right panel, under the `Module Configuration` section, click on `+ Create new configuration`
5. Complete the form with the following information and click on `Save`:
	* **Name**: Sekoia.io config
	* **Api_key**: `<YOUR_SEKOIA_APIKEY>`
	* **Base_url**: `https://api.sekoia.io`
6. Under the `Trigger Configuration` section, click on `+ Create new configuration`
7. Complete the form with the following information and click on `Save`:
    * **name**: Default
    * **Rule Filter**: `<LEAVE_IT_EMPTY>`
8. Click on the `Get Alert` module and on the right panel, select the **Sekoia.io config** previously created
9. Select the `Get events from the alert` and on the right panel, elect the **Sekoia.io config** previously created
10. Click on the `Create incident on XSOAR` module and adapt the configuration:
    * In the `Headers` section, change the value of `YOUR_XSOAR_TOKEN` with the complex string your defined during the configuration of the XSOAR webhook
    * In the `Url` section, change `<YOUR_XSOAR_DOMAIN>` with the correct value
    * The `Json` section contains the information that will be sent to XSOAR. By default, it will send the name of the rule that triggered the alert, the creation date, the alert short id, the alert URL, the urgency of the alert and the first event associated to the alert. Please adapt it to your needs if you want more information to be sent.

Your playbook is now ready!

11. **Save** your Playbook by clicking on the `Save` button on the center of the page
12. **Activate** your Playbook by toggling the value from `Off` to `On`, on the top right of the page

Now, when a new alert is raised on Sekoia.io, this playbook will run and call the XSOAR webhook to create an incident.

### XSOAR Mapping

By default, only the name of the incident and the creation date are used in the Incident.

To use the alert short ID, the alert URL, the urgency of the alert and the first event associated to the alert, you need to define a mapping on XSOAR.

Those values can be mapped as follow : 

| JSON key name | Cortex XSOAR field |
|:-------------:|:------------------:|
|    alertId    |      Alert ID      |
|    alertUrl   |      Alert URL     |
|     events    |       Events       |
|    urgency    |      severity      |

To do this mapping, follow these steps:

1. Go to `Settings` > `OBJECTS SETUP` > `Incident Fields` and edit the fields `Alert ID`, `Alert URL`, `Events` and `severity` are `Used In` to use them for the Incident type `Sekoia.io`
2. Go to `Classification & Mapping` and click `+ New`
3. Select `Incident Mapper (incoming)` and give it the name `Sekoia.io mapping`
4. On the left panel, find the XSOAR fields `Alert ID`, `Alert URL`, `Events` and `severity` and click `Choose data path` to give them the value of the corresponding `JSON key name` (for instance `Alert ID` > `alertId`)
5. Click on `Save Version`

To use this mapping with the Generic Webhook:
 
1. Go back to `Settings` > `INTEGRATIONS` > `Instances` and find the `Generic Webhook`,
2. On the `sekoia` instance, click on the edit button
3. Under `Mapper (incoming)`, select the `Sekoia.io mapping` previously created
4. Click on `Save and exit`

Congratulations! The integration with Palo Alto XSOAR is now complete! 

## View Sekoia.io playbook runs

To access Sekoia.io playbook runs, follow these steps: 

1. On the Sekoia.io GUI, go to the Playbooks page
2. Select your playbook `Automatically create an incident on Palo Alto Cortex XSOAR` and click on `Edit`
3. On the top right of the page, click on `Runs`
4. **Verify** that the displayed `Status` is `Succeeded`
5. If you click on a run from the history, you will be redirected to the Graph page. From there, you will be able to see the results of each block by clicking on it:

![Playbook History](/assets/operation_center/playbooks/playbook_history.PNG){: style="max-width:100%"}

