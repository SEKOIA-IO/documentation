uuid: 5803f97d-b324-4452-b861-0253b15de650
name: Lacework Cloud Security
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**:

The Lacework Cloud Security provides continuous cloud security monitoring and automated threat detection, safeguarding cloud environments with real-time insights and compliance enforcement.



## Configure

### Prerequisites

To create API keys, you must have the account admin role or otherwise have write permissions for API keys in the Lacework Console.

### Create Lacework Credentials

#### Create a service user

In the lacework console:

1. Go to `Settings`

    ![step 1](/assets/operation_center/integration_catalog/cloud_and_saas/lacework/step_01.png)

2. In the settings, go to `Access Control` > `Users` > `Account level` and click `+ Add New`

    ![step 2](/assets/operation_center/integration_catalog/cloud_and_saas/lacework/step_02.png)

3. To create a service user:

    1. Select `Service user` as user type 
    2. Give the user a name and an optional description
    3. Click `Next`

        ![step 3](/assets/operation_center/integration_catalog/cloud_and_saas/lacework/step_03.png)

    4. Select `Read-Only User` as user group 
    5. Click `Save`

        ![step 4](/assets/operation_center/integration_catalog/cloud_and_saas/lacework/step_04.png)

#### Create API keys

In the Lacework console:

1. In the `Settings`, go to `Configuration` > `API keys` > `Service User API Keys` and click `+ Add New`

    ![step 5](/assets/operation_center/integration_catalog/cloud_and_saas/lacework/step_05.png)

2. To create an API Key:

    1. Give the key a name and an optional description.
    2. Click `Save`.

        ![step 6](/assets/operation_center/integration_catalog/cloud_and_saas/lacework/step_06.png)

Download the generated API key file and open it in an editor to view and use the key ID and generated secret in your API requests. You can create up to 20 API keys.


### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Lacework Cloud Security` format.

### Pull events

To start to pull events, you have to:

1. Go to the [Playbook page](https://app.sekoia.io/operations/playbooks).
2. Click on `+ PLAYBOOK` and choose `Create a playbook from scratch`.
3. Give it a name and a description and click on `Next`.
4. In `Choose a trigger`, select `Fetch new logs from Lacework`.
5. On the right sidebar, in "Using which account ?", select `+ Add new account`.
6. Write a `name` and set up the account configuration with the account, the keyId and the secret of your API Key.
7. In the `Trigger Configuration` section, click on `Create new configuration`.
8. Write a `name`, choose a `frequency` - Default is `60` -, paste the `intake_key` associated to your `Lacework Cloud Security` intake and click on `Save`.
9. On the top right corner, start the Playbook. You should see monitoring messages in the `Trigger logs` section.
10. Check on the [Events page](https://app.sekoia.io/operations/events) that the Lacework logs are being received.


{!_shared_content/operations_center/integrations/generated/5803f97d-b324-4452-b861-0253b15de650_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_5803f97d-b324-4452-b861-0253b15de650_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/5803f97d-b324-4452-b861-0253b15de650.md!}

## Further Readings

- [Lacework credentials documentation](https://docs.lacework.net/api/api-access-keys-and-tokens)
- [Lacework API documentation](https://docs.lacework.net/api/v2/docs)
