---
uuid: acd3374a-9738-4650-9d20-bd0a22daac40
title: Datadome Protection
name: Datadome Protection
type: intake
---

## Overview

Datadome offers is a bot protection solution, providing real-time detection and mitigation of malicious bots, safeguarding websites and APIs from fraud, scraping, and other automated threats with advanced security measures.

- **Vendor**: DataDdome
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: Web application firewall logs


## Step-by-Step Configuration Procedure

This setup guide will show you how to forward your Datadome Protection logs to Sekoia.io

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

### Instructions on the 3rd Party Solution
#### Enable forwarding
1. Connect on the Datadome Dashboard
2. On the left panel, click `Management`
3. On the ribbon, go to `Integration` tab
4. In the `Webhook` section, click `Add Webhook`
5. Type the name of the integration
6. As URL, type `https://intake.sekoia.io/plain?intake_key=<YOUR INTAKE KEY>`
!!! warning 
    The previous URL works for the FRA1 region. For any other region, replace the domain “intake.sekoia.io” with your region’s HTTP-intake domain—for example:

    https://app.usa1.sekoia.io/api/v1/intake-http

    You can find your region’s domain here: [https://docs.sekoia.io/getting_started/regions/](https://docs.sekoia.io/getting_started/regions/)

7. Select `Default` as the payload format
8. Select `All threats` as threats
9. Click `Save`

<video controls width="100%">
  <source src="/assets/integration/cloud_and_saas/datadome/datadome_protection.webm" type="video/webm">
</video>

{!_shared_content/operations_center/integrations/generated/acd3374a-9738-4650-9d20-bd0a22daac40_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_acd3374a-9738-4650-9d20-bd0a22daac40_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/acd3374a-9738-4650-9d20-bd0a22daac40.md!}

## Further readings

- [Configure a Custom Integration in the DataDome Dashboard](https://docs.datadome.co/docs/custom)