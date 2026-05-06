uuid: 4703dc86-c39d-484c-abb5-46e126c6a05d
name: BeyondTrust PRA Team Activity
type: intake

## Overview

BeyondTrust Privileged Remote Access enables secure, controlled remote access to critical systems for employees and vendors, focusing on protecting privileged credentials and sessions. 

This integration collects the Team logs.

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Vendor**: BeyondTrust
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**:
    - Team Activity

## Configure

### How to create an API token

1. Log in the BeyondTrust Privileged Remote Access console
 
    ![Step 1](/assets/operation_center/integration_catalog/cloud_and_saas/beyondtrust/team/step_1.png){: style="max-width:100%"}

2. Click the Burger menu

    ![Step 2](/assets/operation_center/integration_catalog/cloud_and_saas/beyondtrust/team/step_2.png){: style="max-width:100%"}

3. On the left panel, click `Management`
   
    ![Step 3](/assets/operation_center/integration_catalog/cloud_and_saas/beyondtrust/team/step_3.png){: style="max-width:100%"}

4. Click `API Configuration`

    ![Step 4](/assets/operation_center/integration_catalog/cloud_and_saas/beyondtrust/team/step_4.png){: style="max-width:100%"}

5. Check `Enable XML API` and click `+ Add`

    ![Step 5](/assets/operation_center/integration_catalog/cloud_and_saas/beyondtrust/team/step_5.png){: style="max-width:100%"}

6. Check `Enable`
7. Type a name for the API Account and add a comment (optional)
8. Check `Reporting > Allow Access to Access Session Reports and Recordings`
9. Copy the OAuth client ID and the OAuth client Secret 
10. Click `Save`

    ![Step 6](/assets/operation_center/integration_catalog/cloud_and_saas/beyondtrust/team/step_6.png){: style="max-width:100%"}

### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format BeyondTrust PRA Vault Account Activity. 
2. Set up the intake configuration with the Base URL, Client ID and Client Secret

{!_shared_content/operations_center/integrations/generated/4703dc86-c39d-484c-abb5-46e126c6a05d_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_4703dc86-c39d-484c-abb5-46e126c6a05d_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/4703dc86-c39d-484c-abb5-46e126c6a05d.md!}

## Further readings

- [BeyondTrust Integrations](https://docs.beyondtrust.com/bt-docs/docs/integrations)
