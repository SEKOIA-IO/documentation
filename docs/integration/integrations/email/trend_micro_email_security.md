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

1. Click on **+ PLAYBOOK** button to create a new one
2. Select **Create a playbook from scratch**
3. Give it a name in the field **Name**
4. Open the left panel, click **Trend Micro Email Security** then select the trigger `Fetch new logs`
5. Click on **Create**

6. Create a **Trigger configuration** using your `Service URL`, `Username`, `API key` and `Intake key`. All four are required.

* `API key` is created on the first step 
* `username` is your `Login ID` entered during account creating
* The value of `service URL` varies according to your location:

| Location                                      | Service URL                 |
|-----------------------------------------------|-----------------------------|
| North America, Latin America and Asia Pacific | api.tmes.trendmicro.com     |
| Europe, the Middle East and Africa            | api.tmes.trendmicro.eu      |
| Australia and New Zealand                     | api.tmes-anz.trendmicro.com |
| Japan                                         | api.tmems-jp.trendmicro.com |
| Singapore                                     | api.tmes-sg.trendmicro.com  |
| India                                         | api.tmes-in.trendmicro.com  |

* Type the `Intake key` created on the previous step

7. Click on the **Save** button
8. **Activate the playbook** with the toggle button in the top right corner of the page

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)
