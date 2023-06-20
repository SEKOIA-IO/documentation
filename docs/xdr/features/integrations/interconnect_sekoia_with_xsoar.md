# Synchronize Alerts with Palo Alto Cortex XSOAR

This use case describes how to automatically create an incident on Palo Alto Cortex XSOAR when on a new alert is raised on Sekoia.io.

This integration uses the Sekoia.io Playbook and the Generic Webhook of Palo Alto XSOAR to interact between both products.
Some information will be automatically sent to Cortex XSOAR but you will be able to adapt it to your need.

Here is a schema that illustrates this interconnection:

![Sekoia Cortex XSOAR Schema](/assets/operation_center/external_integrations/sekoia_xsoar_integration.png){: style="max-width:50%"}

## Prerequisites

- A Sekoia.io XDR licence
- The user that configures the Playbook should have access to the Sekoia.io Playbooks:
- An API Key with a Role that contains at least the following permissions:
	* `SIC_READ_ALERTS`
    * `SIC_READ_INTAKES`
    * The `SYMPHONY_*` permissions
- Admin access to Cortex XSOAR
- Cortex XSOAR available on the internet

!!! Note
To create your API Key, follow this [documentation](../../../../getting_started/manage_api_keys/#create-an-api-key).

## Configure

### Create an new Incident Type on Palo Alto Cortex XSOAR
A dedicated incident type for Sekoia.io will allow to enable specific Incident Fields and decide what XSOAR playbook to use.

Follow these steps to create a new Incident type: 

- From the XSOAR GUI, click on `Settings` > `OBJECTS SETUP` > `Types`
- Click on `+ New Incident Type` and give it the name `Sekoia.io`. Please configure the other parameters to your need.
- Click on `Save`

### Create a webhook on Palo Alto Cortex XSOAR
To allow Sekoia.io to create a new incident when a new alert is raised, we need to create a Webhook.

- From the XSOAR GUI, install the `Generic Webhook` published by XSOAR from the Market Place
- Go to `Settings` > `INTEGRATIONS` > `Instances` and search `Generic Webhook`
- Click on `Add instance`
- name it `sekoia`
- Under `Incident type`, select `Sekoia.io`
- Follow the webhook documentation and configure Cortex XSOAR server rerouting to make your webhook available from your XSOAR Url in HTTPS.
- Fill out `Username` with `_header: Authorization` and `Password` with `Bearer YOUR_XSOAR_TOKEN`. Replace `YOUR_XSOAR_TOKEN` with a complex string. It will be use as an authentication.
- To be able to map information easily into XSOAR, check the option `Store sample events for mapping`.
- Click on `Save & exit`

### Create and configure a playbook on Sekoia.io
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
    * In the `Url` section, change `<YOUR_XSOAR_DOMAIN>` with the correct value.
    * The `Json` section contains the information that will be sent to XSOAR. By default, it will send the name of the rule that triggered the alert, the creation date, the alert short id, the alert URL, the urgency of the alert and the first event associated to the alert. Please adapt it to your need if you want more information to be sent.

Your playbook is now ready !

- **Save** your Playbook by clicking on the `Save` button on the center of the page
- **Activate** your Playbook by toggling the value from `Off` to `On`, on the top right of the page

Now, when a new alert is raised on Sekoia.io, this playbook will run and call the XSOAR webhook to create an incident.

### XSOAR Mapping

By default, only the name of the incident and the creation date are used in the Incident.

To use the alert short id, the alert URL, the urgency of the alert and the first event associated to the alert, you need to define a mapping on XSOAR.

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
3. Select `Incident Mapper (incoming)`
4. Name it `Sekoia.io mapping`
5. On the left panel, find the XSOAR fields `Alert ID`, `Alert URL`, `Events` and `severity` and click `Choose data path` to give them the value of the corresponding `JSON key name` (for instance `Alert ID` > `alertId`)
6. Click on `Save Version`
7. Finally to use this mapping with the Generic Webhook, go back to `Settings` > `INTEGRATIONS` > `Instances`
8. Find the `Generic Webhook` and on the `sekoia` instance, click on the edit button
9. Under `Mapper (incoming)`, select the `Sekoia.io mapping` previously created
10. Click on `Save & exit`

Congratulations ! The integration with Palo Alto XSOAR is now finished !

## View Sekoia.io Playbook runs

1. On the Sekoia.io GUI, go to the Playbook page
2. Select your playbook `Automatically create an incident on Palo Alto Cortex XSOAR` and click on `Edit`
3. On the top right of the page, click on `Runs`
4. **Confirm** the displayed `Status` is `Succeeded`
5. If you click on a run from the history, you will be redirected to the Graph page. Then you will be able to see the results of each block by clicking on it:

![Playbook History](/assets/operation_center/playbooks/playbook_history.PNG)

