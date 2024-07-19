uuid: acd3374a-9738-4650-9d20-bd0a22daac40
name: Datadome Protection
type: intake

## Overview
  - **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**: Alert
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:

Datadome offers is a bot protection solution, providing real-time detection and mitigation of malicious bots, safeguarding websites and APIs from fraud, scraping, and other automated threats with advanced security measures.



## Configure

This setup guide will show you how to forward your Datadome Protection logs to Sekoia.io

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Datadome Protection.

### Enable forwarding
1. Connect on the Datadome Dashboard
2. On the left panel, click `Management`
3. On the ribbon, go to `Integration` tab
4. In the `Webhook` section, click `Add Webhook`
5. Type the name of the integration
6. As URL, type `https://intake.sekoia.io/plain?intake_key=<YOUR INTAKE KEY>`
7. Select `Default` as the payload format
8. Select `All threats` as threats
9. Click `Save`

<video controls width="100%">
  <source src="/assets/operation_center/integration_catalog/cloud_and_saas/datadome/datadome_protection.webm" type="video/webm">
</video>

## Further readings

- [Configure a Custom Integration in the DataDome Dashboard](https://docs.datadome.co/docs/custom)
{!_shared_content/integration/detection_section.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_acd3374a-9738-4650-9d20-bd0a22daac40_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/acd3374a-9738-4650-9d20-bd0a22daac40.md!}

