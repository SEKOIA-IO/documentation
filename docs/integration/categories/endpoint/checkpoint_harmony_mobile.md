uuid: ff53e0db-059b-4e16-ba90-8c4dbf5cee35
name: Check Point Harmony Mobile
type: intake

## Overview

Check Point Harmony Mobile is the industry's first unified security solution for users devices and access.

- **Vendor**: Check Point
- **Plan**: Defend Core & Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Telemetry, Alert
- **Supported application or feature**:Network device logs, Network protocol analysis, Web logs

## Configure

### Create authentication credentials

1. Login to your Check Point Harmony account and navigate to `Profile > Global Settings`

    ![Global settings](/assets/instructions/checkpoint/checkpoint_global_settings.png)

2. Go to `API Keys` and click on `New`

    ![API Keys](/assets/instructions/checkpoint/checkpoint_new_key.png)

3. Update required fields with next information and create `API Key`:
    * Service: Harmony Mobile (1)
    * Expiration: If you pass an empty field, it means that API Key will not expire until you delete it. (2)
    * Description: You can specify any description that you want. (3)
    * Roles: `Read-Only`

    ![API Key Form](/assets/instructions/checkpoint/checkpoint_api_key_form.png)

4. Copy values of `Client ID`, `Secret Key` and `Authentication URL` and save them for the configuration of the connector.

### Create the intake

To create the intake, go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Check Point Harmony Mobile`.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Check Point Harmony Mobile](../../../automate/library/check-point.md) trigger
2. Set up the module configuration with the Client ID, Client Secret and Authentication URL.
3. Set up the trigger configuration with the intake key
4. Start the playbook and enjoy your events

{!_shared_content/operations_center/integrations/generated/ff53e0db-059b-4e16-ba90-8c4dbf5cee35_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_ff53e0db-059b-4e16-ba90-8c4dbf5cee35_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/ff53e0db-059b-4e16-ba90-8c4dbf5cee35.md!}
