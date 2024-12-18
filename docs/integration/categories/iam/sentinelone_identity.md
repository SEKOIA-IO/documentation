uuid: b502e522-6996-4b12-9538-f69326b68243
name: SentinelOne Identity
type: intake

## Overview
SentinelOne Singularity Identity is a cybersecurity solution that provides identity protection and zero-trust security by continuously monitoring and analyzing user behaviors to detect and prevent potential threats.

- **Vendor**: SentinelOne
- **Supported environment**: Cloud
- **Detection based on**: Telemetry
- **Detection based on**: Alert

## Configure

### Generate API token

1. Log in the SentinelOne Singularity console
2. On the left panel, click `Settings`

    ![Settings](/assets/operation_center/integration_catalog/cloud_and_saas/sentinelone_identity/01-Settings.png)

3. Click `Users`
    ![Users](/assets/operation_center/integration_catalog/cloud_and_saas/sentinelone_identity/02-Users.png)

4. On the left, click `Service Users`
    
    ![Service Users](/assets/operation_center/integration_catalog/cloud_and_saas/sentinelone_identity/03-Service_users.png)

5. Click `Actions`, then click `Create New Service User`

    ![Create New Service User](/assets/operation_center/integration_catalog/cloud_and_saas/sentinelone_identity/04-Create_new_services_users.png)

6. Type a name, a description and Select the expiration duration for the Service User
7. Click `Next`

    ![Generate API Key](/assets/operation_center/integration_catalog/cloud_and_saas/sentinelone_identity/05-Generate.png)

8. Select the scope of the access with the `viewer` role. We recommend using the `site` scope.
9. Click `Create User`

    ![Create User](/assets/operation_center/integration_catalog/cloud_and_saas/sentinelone_identity/06-Scope.png)

10. Copy and save the APIToken then click `Close`
    
    ![Copy API Token](/assets/operation_center/integration_catalog/cloud_and_saas/sentinelone_identity/07-APIToken.png)

### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `SentinelOne Identity`. Copy the intake key.

{!_shared_content/operations_center/integrations/generated/b502e522-6996-4b12-9538-f69326b68243.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_b502e522-6996-4b12-9538-f69326b68243_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/b502e522-6996-4b12-9538-f69326b68243.md!}
