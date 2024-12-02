uuid: 9844ea0a-de7f-45d4-9a9b-b07651f0630e
name: Trend Micro Vision One Workbench Alerts [BETA]
type: intake


## Overview

Trend Micro Vision One is an extended detection and response (XDR) platform that enhances threat detection, investigation, and response across multiple security layers. It provides a centralized view for improved security posture and faster threat remediation.
This integration will ingest Workbench Alerts from Trend Micro Vision One.

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Supported environment**: SaaS
- **Detection based on**: Alerts
- **Supported application or feature**:
    - Alerts
    
## Configure

### How to create an API token

1. Log in the Trend Vision One console
2. On the left panel, click `Administration` then click `API keys`

    ![step 1](/assets/integration/cloud_and_saas/trend_micro_vision_one/01_administration.png)

3.  Click `Add API key`

    ![step 2](/assets/integration/cloud_and_saas/trend_micro_vision_one/02_create_api_key.png)

4. Type a name for the API key
5. Select the `SIEM` role and an expiration time
6. Check `status` to enable the API key

    ![step 3](/assets/integration/cloud_and_saas/trend_micro_vision_one/03_create_api_key.png)

7. Copy the API key and click `Close`

    ![step 4](/assets/integration/cloud_and_saas/trend_micro_vision_one/04_save_api_key.png)

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/operations_center/integrations/generated/9844ea0a-de7f-45d4-9a9b-b07651f0630e.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_9844ea0a-de7f-45d4-9a9b-b07651f0630e_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/9844ea0a-de7f-45d4-9a9b-b07651f0630e.md!}