---
uuid: 89346697-b64b-45d4-a456-72fd8a2be5d8
title: Thinkst Canary
name: Thinkst Canary
type: intake
---

## Overview

Thinkst Canary is a deceptive honeypot device that mimics various systems to lure and detect cyber threats, providing early and accurate breach alerts. Canarytokens are easy-to-deploy digital traps that notify users of unauthorized access to sensitive information.

- **Vendor**: Thinkst Applied Research
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: events associated to the incidents
    
## Step-by-Step Configuration Procedure

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
2. Set the intake configuration with the following parameters:
    - `Base URL`, which should be `https://DOMAINHASH.canary.tools`, where `DOMAINHASH` is your domain hash from the `How to create an API Key` step
    - `Auth token` from the same step


### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)


{!_shared_content/operations_center/integrations/generated/89346697-b64b-45d4-a456-72fd8a2be5d8_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_89346697-b64b-45d4-a456-72fd8a2be5d8_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/89346697-b64b-45d4-a456-72fd8a2be5d8.md!}
