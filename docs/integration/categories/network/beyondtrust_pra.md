uuid: f6cfddb4-543a-41fe-9802-c66b7c90366d
name: BeyondTrust PRA
type: intake

## Overview

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Vendor**: BeyondTrust
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Authentication logs, Application logs

## Configure

### How to create an API token

1. Log in the BeyondTrust Privileged Remote Access console
2. On the left panel, click `Management`

    ![Management](/assets/operation_center/integration_catalog/cloud_and_saas/beyondtrust/01_management.png){: style="max-width:100%"}

3. Click `API Configuration`
   
    ![Configuration](/assets/operation_center/integration_catalog/cloud_and_saas/beyondtrust/02_configuration.png){: style="max-width:100%"}

4. Check `Enable XML API` and click `+ Add`

    ![Enable](/assets/operation_center/integration_catalog/cloud_and_saas/beyondtrust/03_enable_api_key.png){: style="max-width:100%"}

5. Check `Enable`
6. Type a name for the API Account and add a comment (optional)
7. Check `Reporting > Allow Access to Access Session Reports and Recordings`
8. Copy the OAuth client ID and the OAuth client Secret
9. Click `Save`

    ![Click Save](/assets/operation_center/integration_catalog/cloud_and_saas/beyondtrust/04_create_api_key.png){: style="max-width:100%"}

### Instruction on Sekoia

{!_shared_content/operations_center/integrations/generated/f6cfddb4-543a-41fe-9802-c66b7c90366d.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_f6cfddb4-543a-41fe-9802-c66b7c90366d_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/f6cfddb4-543a-41fe-9802-c66b7c90366d.md!}
