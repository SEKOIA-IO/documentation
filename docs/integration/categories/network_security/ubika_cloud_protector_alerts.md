uuid: d0383e87-e054-4a21-8a2c-6a89635d8615
name: Ubika Cloud Protector Alerts
type: intake

## Overview

Ubika Cloud Protector is a cloud-native security solution, providing advanced threat detection and data protection to secure cloud environments, enabling real-time monitoring and mitigation of risks in cloud-based infrastructures.

- **Vendor**:Ubika
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: Web application firewall logs


## Configure

### How to get API keys info
3 information are required to collect data from Ubika:

- The `provider name` (available in Ubika interface)
- The `tenant name` (available in Ubika interface)
- A `token` (provided by Ubika support team)

!!! warning
    The following instructions are based on the old interface of Ubika Cloud Protector. Please, switch to the old interface if you use the new one.
    ![choose old interfaces](/assets/integration/cloud_and_saas/ubika_cloud_protector/switch.png){: style="max-width:100%"}

To get API keys info:


1. Log in the Ubika Cloud protector
2. Go to `Account` > `API Access`

    ![api access](/assets/integration/cloud_and_saas/ubika_cloud_protector/api_access.png){: style="max-width:100%"}

3. In the `API KEYS INFO` section, please note the `provider name` and the `tenant name`

    ![api info](/assets/integration/cloud_and_saas/ubika_cloud_protector/api_keys_info.png){: style="max-width:100%"}

4. Finally, contact `Ubika support` to request a `token` for the legacy API. This specific `token` cannot be retrieved through the Ubika interface at the moment.

### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Ubika Cloud Protector`.
2. Set the intake account configuration with the `provider`, `tenant` and `token` from the `How to get API keys info` step

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/d0383e87-e054-4a21-8a2c-6a89635d8615_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d0383e87-e054-4a21-8a2c-6a89635d8615_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/d0383e87-e054-4a21-8a2c-6a89635d8615.md!}

