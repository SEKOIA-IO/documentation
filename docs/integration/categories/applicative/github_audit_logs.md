uuid: 80de6ccb-7246-40de-bcbb-bc830118c1f9
name: Github Audit Logs
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**: Telemetry
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:
Github audit logs represents activities on your Github organization.

This setup guide describes how to forward audit logs from Github to Sekoia.io.



## Configure

### Prerequisites

- Your organization must use GitHub Entreprise Cloud to [get access to audit log API](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#using-the-audit-log-api)
- You must be Administrator of the organization. There are two options on how to configure connector:
    * [With Github API Key](#creating-the-github-api-key)
    * [With Github PEM file](#creating-the-github-pem-file)

### Creating the Github API key

To create an API key on [Github](https://github.com/):

1. On the top right corner, click on your profile picture then on `Settings`.

    ![Personal settings](/assets/instructions/github_audit_logs/personal_settings.png)

2. On the Developper Settings, create a Personnal access token (classic) with read access to the audit_logs.

    ![Developer settings](/assets/instructions/github_audit_logs/developer_settings.png)

    ![Personal tokens](/assets/instructions/github_audit_logs/personal_tokens.png)

    ![Generate new token](/assets/instructions/github_audit_logs/generate_new_token.png)
    
    ![Generate new token](/assets/instructions/github_audit_logs/generate_new_token.png)

3. Validate the configuration and save the token for the configuration of the connector.


### Create the Github PEM file

1. On the top right corner, click on your profile picture then on `Your organizations`.

    ![Users organizations](/assets/instructions/github_audit_logs/users_organizations.png)

2. Select organization you want to create PEM file for:
    
    ![Select organization](/assets/instructions/github_audit_logs/select_organization.png)

3. Scroll to `Developer settings` and select `Github apps`:
    
    ![Org developer settings](/assets/instructions/github_audit_logs/github_apps.png)

4. Click on edit `Github app`:
    
    ![Edit Github app](/assets/instructions/github_audit_logs/edit_github_app.png)

    * Make sure you have all necessary rights (#1)
    * After that click on edit (#2)
   
5. Go to `General` section:
    
    ![General](/assets/instructions/github_audit_logs/general_section.png)

6. Scroll to `Private keys` section and click on `Generate a private key`:
    
    ![Private keys](/assets/instructions/github_audit_logs/generate_private_key.png)

7. Follow all necessary instructions and save PEM file for the configuration of the connector.

8. Scroll up and copy `App ID` for the configuration of the connector.
    
    ![App ID](/assets/instructions/github_audit_logs/app_id.png)

9. As a result you should have `App ID` and `PEM file` for the configuration of the connector.

### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Github  audit logs`. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Fetch new audit logs from Github](../../../automate/library/github.md) trigger
2. Set up the module configuration with the Github organization and the APIkey. Set up the trigger configuration with the intake key
3. Start the playbook and enjoy your events

{!_shared_content/integration/detection_section.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_80de6ccb-7246-40de-bcbb-bc830118c1f9_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/80de6ccb-7246-40de-bcbb-bc830118c1f9.md!}

