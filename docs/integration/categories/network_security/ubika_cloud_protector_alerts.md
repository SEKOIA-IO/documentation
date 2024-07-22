uuid: d0383e87-e054-4a21-8a2c-6a89635d8615
name: Ubika Cloud Protector Alerts
type: intake

## Overview
- **Vendor**:
- **Plan**:
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:

Ubika Cloud Protector is a cloud-native security solution, providing advanced threat detection and data protection to secure cloud environments, enabling real-time monitoring and mitigation of risks in cloud-based infrastructures.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.



## Configure

### How to get API keys info
3 informations are required to collect data from Ubika:

- The `provider name` (available in Ubika interface)
- The `tenant name` (available in Ubika interface)
- A `token` (provided by Ubika support team)

!!! warning
    The following instructions are based on the old interface of Ubika Cloud Protector. Please, switch to the old interface if you use the new one.
    ![choose old interfaces](/assets/operation_center/integration_catalog/cloud_and_saas/ubika_cloud_protector/switch.png){: style="max-width:100%"}

To get API keys info:


1. Log in the Ubika Cloud protector
2. Go to `Account` > `API Access`

    ![api access](/assets/operation_center/integration_catalog/cloud_and_saas/ubika_cloud_protector/api_access.png){: style="max-width:100%"}

3. In the `API KEYS INFO` section, please note the `provider name` and the `tenant name`

    ![api info](/assets/operation_center/integration_catalog/cloud_and_saas/ubika_cloud_protector/api_keys_info.png){: style="max-width:100%"}

4. Finally, contact `Ubika support` to request a `token` for the legacy API. This specific `token` cannot be retrieved through the Ubika interface at the moment.

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
    * Type the `provider`, `tenant` and `token` from the `How to get API keys info` step 

- Click on the **Save** button
- **Activate the playbook** with the toggle button on the top right corner of the page

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/d0383e87-e054-4a21-8a2c-6a89635d8615_sample.md!}


## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_d0383e87-e054-4a21-8a2c-6a89635d8615_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/d0383e87-e054-4a21-8a2c-6a89635d8615.md!}

