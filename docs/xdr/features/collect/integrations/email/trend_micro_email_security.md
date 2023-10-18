uuid: 2e9d87ed-6606-445a-90d1-9c7695b28335
name: Trend Micro Email Security
type: intake

## Overview
Trend Micro Email Security is a robust email protection solution that safeguards against email-borne threats such as phishing, malware, and spam, offering advanced threat detection and content filtering to secure corporate email communications effectively.

{!_shared_content/operations_center/detection/generated/suggested_rules_2e9d87ed-6606-445a-90d1-9c7695b28335_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2e9d87ed-6606-445a-90d1-9c7695b28335.md!}

## Configure

### How to get an API key
1. Log on to the Trend Micro Email Security administrator console.
2. Go to **Administration**

![Step 1](/assets/operation_center/integration_catalog/email/trend_micro/step_1.png)

4. Click on **Service Integration**. The API Access tab displays by default.

![Click on Service Integration](/assets/operation_center/integration_catalog/email/trend_micro/step_2.png)

6. Click **Add** to generate an API Key.

![Click on Add](/assets/operation_center/integration_catalog/email/trend_micro/step_3.png)

9. Copy the API Key value and save the value. Keep the API Key private

### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Trend Micro Email Security`.
2. Copy the associated Intake key

### Pull the logs to collect them on Sekoia.io

Go to the Sekoia.io [playbook page](https://app.sekoia.io/operations/playbooks), and follow these steps:

- Click on **+ PLAYBOOK** button to create a new one
- Select **Create a playbook from scratch**
- Give it a name in the field **Name**
- Open the left panel, click **Trend Micro Email Security** then select the trigger `Fetch new logs`
- Click on **Create**

- Create a **Module configuration** using your service URL, username and API key. Name the module configuration as you wish


-  Create a **Trigger configuration** using:

    * Type the `Intake key` created on the previous
    * Select the `application name` what you to fetch events from
    * Type the `Admin email`

- Click on the **Save** button
- **Activate the playbook** with the toggle button in the top right corner of the page

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)
