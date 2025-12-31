---
uuid: 8d024a2b-3627-4909-818d-26e1e3b2409c
title: Ubika Cloud Protector Traffic
name: Ubika Cloud Protector Traffic
type: intake
---

## Overview

Ubika Cloud Protector is a cloud-native security solution, providing advanced threat detection and data protection to secure cloud environments, enabling real-time monitoring and mitigation of risks in cloud-based infrastructures.

- **Vendor**: Ubika
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Web proxy	


## Configure

### How to get API keys info

!!! warning
    The following instructions are based on the old interface of Ubika Cloud Protector. Please, switch to the old interface if you use the new one.
    ![choose old interfaces](/assets/integration/cloud_and_saas/ubika_cloud_protector/switch.png){: style="max-width:100%"}

To get API keys info:


1. Log in the Ubika Cloud protector
2. Go to `Account` > `API Access`

    ![api access](/assets/integration/cloud_and_saas/ubika_cloud_protector/api_access.png){: style="max-width:100%"}

3. In the `API KEYS INFO` section, please note the `provider name` and the `tenant name`

    ![api info](/assets/integration/cloud_and_saas/ubika_cloud_protector/api_keys_info.png){: style="max-width:100%"}

4. The documentation to retrieve the `token` is still [under construction]

### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Ubika Cloud Protector`.
2. Set the intake account configuration with the `provider`, `tenant` and `token` from the `How to get API keys info` step.


### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/8d024a2b-3627-4909-818d-26e1e3b2409c_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_8d024a2b-3627-4909-818d-26e1e3b2409c_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/8d024a2b-3627-4909-818d-26e1e3b2409c.md!}

