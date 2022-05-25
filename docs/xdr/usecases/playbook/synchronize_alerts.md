# Synchronise Alerts with an external tool

This use case describes how to automatically push new Alerts in an external security tool such as SIRP, SOAR or EDR etc.

## Prerequisites

- A SEKOIA.IO XDR licence
- The user that configures the Playbook should have a Role that contains:
	* The SYMPHONY permissions
- An API Key with a Role that contains at least the following permission:
	* SIC_READ_ALERTS

> To create your API Key, follow this [documentation](https://docs.sekoia.io/user_center/apikeys/).

## Playbook creation

First create a new playbook by following those steps:

- **Go to** the [Playbook page](https://app.sekoia.io/operations/playbooks)
- **Click** on `+ PLAYBOOK`
- If multi-tenant is available, **select** the Community where the Playbook should be executed
- **Select** the option `Create a playbook from scratch`
- **Select** the block `Alert Created`

> The Playbook will automatically be executed when a new alert is created in SEKOIA.IO.

## Playbook configuration

1. Configure the `Alert Created` block

- On the right panel, under the Module Configuration section, click on `+ Create new configuration`
- Complete the form with the following information:
	* **Name**: ReadAlertContent
	* **Api_key**: TO BE REPLACED BY YOUR SEKOIA.IO API KEY
	* **Base_url**: `https://api.sekoia.io`
- Click on the `Save` button

2. Get Alert information

- On the left panel, **search for** the `Get Alert` block
- **Drag and drop** it underneath the `Alert Created` block
- On the right panel, select the **ReadAlertContent** configuration previously created
- Select the `Alert Created` block and click on `alert_uuid` **copy** icon
- Select the `Get Alert` block and **past** the content in the Configuration section, on the `uuid` cell
- Link the blocs `Alert Created` to `Get Alert`

3. Make HTTP Requests

- On the left panel, **search for** the `Request URL` block
- **Drag and drop** it underneath the `Get Alert` block
- On the right panel, **complete the form** with the following information:

	* **JSON**: `{"alert_short_id":"{{ node.0['alert_uuid'] }}", "rule_name":"{{ node.1['rule']['name'] }}","rule_severity":"{{ node.1['rule']['severity'] }}","description":"This is a description"}`
	* **Method**: `post`
	* **URL**: `YOUR_PRODUCT_EXTERNAL_URL`
	* **Headers**: `{"Authorization": "Bearer YOUR_EXTERNAL_PRODUCT_API_KEY_NOT_THE_SEKOIAIO_ONE"}`

!!! info
	Please replace the headers by following your third party product documentation.

Your playbook should look like the following:

[Playbook Use Case](/assets/operation_center/playbooks/playbook_usecase_request_url.PNG)

## Your Playbook is ready

- **Save** your Playbook by clicking on the `SAVE` button on the center of the page
- **Activate** your Playbook by toggling the value form Off to `On`, on the top right of the page

## See your Playbook runs

- On the top right of the page, **click** on `Runs`
- **Confirm** the displayed `Status` is `Succeeded`
- If you click on a run form the history, you will be redirected to the Graph page. Then you will be able to see the results of each block by clicking on it, as of the following picture:

[Playbook History](/assets/operation_center/playbooks/playbook_history.PNG)

## Bonus

To highlight this specific example, we tested to send a message with alert metadata to a simple [Custom format Intake](https://docs.sekoia.io/operation_center/intakes_customformat/) of SEKOIA.IO made for this occasion on a personal Community.
With the same playbook logic, we only changed the `Request URL` block configuration parameters as following:
* **JSON**:
```json
{"json":"'{\"alert_short_id\":\"{{ node.0['alert_uuid'] }}\", \"rule_name\":\"{{ node.1['rule']['name'] }}\",\"rule_severity\":\"{{ node.1['rule']['severity'] }}\",\"description\":\"An HTTP request was made from SEKOIA.IO Playbook\"}'",
"intake_key":"MYINTAKEKEY"}
```
* **Method**: `post`
* **URL**: `https://intake.sekoia.io`

!!! info
	Those configuration parameters were filled-in by following this [documentation](https://docs.sekoia.io/playbooks/library/http/#request-url).

The result is an event received on SEKOIA.IO in a dedicated Intake, with the content of the POST request that was mapped in the relevant ECS fields (thanks to the Custom Format) mandatory to display a SMART Description.

[Display the Request](/assets/operation_center/playbooks/request_display.PNG)
