uuid: d0383e87-e054-4a21-8a2c-6a89635d8615
name: Ubika Cloud Protector
type: intake

## Overview

Ubika Cloud Protector is a cloud-native security solution, providing advanced threat detection and data protection to secure cloud environments, enabling real-time monitoring and mitigation of risks in cloud-based infrastructures.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

{!_shared_content/operations_center/detection/generated/suggested_rules_d0383e87-e054-4a21-8a2c-6a89635d8615_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d0383e87-e054-4a21-8a2c-6a89635d8615.md!}

## Configure

### How to create an API token

!!! warning
    The following instructions are based on the old interface of Ubika Cloud Protector. Please, switch to the old interface if you use the new one.
    ![choose old interfaces](/assets/operation_center/integration_catalog/cloud_and_saas/ubika_cloud_protector/switch.png){: style="max-width:100%"}

To create an API token:


1. Log in the Ubika Cloud protector
2. Go to `Account` > `API Access`

   ![api access](/assets/operation_center/integration_catalog/cloud_and_saas/ubika_cloud_protector/api_access.png){: style="max-width:100%"}

3. In the `API KEYS INFO` section, please note the `provider name` and the `tenant name`

   ![api info](/assets/operation_center/integration_catalog/cloud_and_saas/ubika_cloud_protector/api_keys_info.png){: style="max-width:100%"}

4. In the `CREATE API KEYS` section
   1. Type a description to identify the API token
   2. Select the `AUTHZ_ROLE_TENANT` role
   3. Select the `AUTHZ_ACT_LIST_LOGS` action
   4. Click `CREATE`

   ![create_token](/assets/operation_center/integration_catalog/cloud_and_saas/ubika_cloud_protector/create_api_token.png){: style="max-width:100%"}


### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Ubika Cloud Protector`.
2. Copy the associated Intake key

### Pull the logs to collect them on Sekoia.io

Go to the Sekoia.io [playbook page](https://app.sekoia.io/operations/playbooks), and follow these steps:

- Click on **+ PLAYBOOK** button to create a new one
- Select **Create a playbook from scratch**
- Give it a name in the field **Name**
- Open the left panel, click **Ubika** then select the trigger `Fetch new alerts from Ubika Cloud Protector`
- Click on **Create**
- Create a **Trigger configuration** using:

    * Type the `Intake key` created on the previous step
    * Type the `provider`, `tenant` and `token` from the `How to create an API token` step 

- Click on the **Save** button
- **Activate the playbook** with the toggle button on the top right corner of the page

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)
