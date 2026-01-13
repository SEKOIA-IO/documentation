---
uuid: 5803f97d-b324-4452-b861-0253b15de650
title: Lacework Cloud Security
name: Lacework Cloud Security
type: intake
---

## Overview

The Lacework Cloud Security provides continuous cloud security monitoring and automated threat detection, safeguarding cloud environments with real-time insights and compliance enforcement.

- **Vendor**: Lacework
- **Supported environment**: SaaS
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**:

## Prerequisites

To create API keys, you must have the account admin role or otherwise have write permissions for API keys in the Lacework Console.
## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution
#### Create Lacework Credentials

**Create a service user**

In the lacework console:

1. Go to `Settings`

    ![step 1](/assets/integration/cloud_and_saas/lacework/step_01.png)

2. In the settings, go to `Access Control` > `Users` > `Account level` and click `+ Add New`

    ![step 2](/assets/integration/cloud_and_saas/lacework/step_02.png)

3. To create a service user:

    1. Select `Service user` as user type
    2. Give the user a name and an optional description
    3. Click `Next`

        ![step 3](/assets/integration/cloud_and_saas/lacework/step_03.png)

    4. Select `Read-Only User` as user group
    5. Click `Save`

        ![step 4](/assets/integration/cloud_and_saas/lacework/step_04.png)

**Create API keys**

In the Lacework console:

1. In the `Settings`, go to `Configuration` > `API keys` > `Service User API Keys` and click `+ Add New`

    ![step 5](/assets/integration/cloud_and_saas/lacework/step_05.png)

2. To create an API Key:

    1. Give the key a name and an optional description.
    2. Click `Save`.

        ![step 6](/assets/integration/cloud_and_saas/lacework/step_06.png)

Download the generated API key file and open it in an editor to view and use the key ID and generated secret in your API requests. You can create up to 20 API keys.


### Instruction on Sekoia
#### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Lacework Cloud Security` format.
2. Set the intake account configuration with the account, the keyId and the secret of your API Key.


{!_shared_content/operations_center/integrations/generated/5803f97d-b324-4452-b861-0253b15de650_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_5803f97d-b324-4452-b861-0253b15de650_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/5803f97d-b324-4452-b861-0253b15de650.md!}

## Further Readings

- [Lacework credentials documentation](https://docs.lacework.net/api/api-access-keys-and-tokens)
- [Lacework API documentation](https://docs.lacework.net/api/v2/docs)
