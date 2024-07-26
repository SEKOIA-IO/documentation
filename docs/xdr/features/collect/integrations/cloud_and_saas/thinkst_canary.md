uuid: 89346697-b64b-45d4-a456-72fd8a2be5d8
name: Thinkst Canary
type: intake

## Overview

Thinkst Canary is a deceptive honeypot device that mimics various systems to lure and detect cyber threats, providing early and accurate breach alerts. Canarytokens are easy-to-deploy digital traps that notify users of unauthorized access to sensitive information.

{!_shared_content/operations_center/detection/generated/suggested_rules_89346697-b64b-45d4-a456-72fd8a2be5d8_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/89346697-b64b-45d4-a456-72fd8a2be5d8.md!}

## Configure

### How to create an API Key
1. Log in the Thinkst Canary console
2. On the top panel, click the toothed wheel and got to **Global Settings**

![Click on Global Settings](/assets/operation_center/integration_catalog/cloud_and_saas/thinkst_canary/thinkstcanary_step01.png)

3. In the **Global Settings**, Click the **API** section
4. Turn on the **Enabled** toggle and Click **+** button. Write down `Domain hash`

![Click on Enabled and +](/assets/operation_center/integration_catalog/cloud_and_saas/thinkst_canary/thinkstcanary_step02.png)

5. Select **Analyst** as the API Key type
6. Type a name for the API Key
7. Click **Create**

![Click on Create](/assets/operation_center/integration_catalog/cloud_and_saas/thinkst_canary/thinkstcanary_step03.png)


### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Thinkst Canary`.
2. Copy the associated Intake key

### Pull the logs to collect them on Sekoia.io

Go to the Sekoia.io [playbook page](https://app.sekoia.io/operations/playbooks), and follow these steps:
  
- Click on **+ PLAYBOOK** button to create a new one
- Select **Create a playbook from scratch**
- Give it a name in the field **Name**
- Open the left panel, click **Thinkst Canary** then select the trigger `Fetch Thinkst Canary Events`
- Click on **Create**
- Create a **Module configuration** using:
    - `Base URL`, which should be `https://DOMAINHASH.canary.tools`, where `DOMAINHASH` is your domain hash from the `How to create an API Key` step
    - `Auth token` from the same step
- Create a **Trigger configuration** using the `Intake key` created on the previous step
- Click on the **Save** button
- **Activate the playbook** with the toggle button on the top right corner of the page

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)
