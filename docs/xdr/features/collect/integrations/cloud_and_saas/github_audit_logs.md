uuid: 80de6ccb-7246-40de-bcbb-bc830118c1f9
name: Github Audit Logs
type: intake

## Overview
Github audit logs represents activities on your Github organization.

This setup guide describes how to forward audit logs from Github to Sekoia.io.

!!! warning
    This format is still in beta, please use it wisely.

{!_shared_content/operations_center/detection/generated/suggested_rules_80de6ccb-7246-40de-bcbb-bc830118c1f9_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/80de6ccb-7246-40de-bcbb-bc830118c1f9.md!}

## Configure

!!! Note
    Your organization must use GitHub Entreprise Cloud to [get access to audit log API](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#using-the-audit-log-api) and
    You must be Administrator of the organization to create the audit logs API KEY.

### Creating the Github API key

To create an API key on [Github](https://github.com/):

1. On the top right corner, click on your profile picture then on `Settings`.
2. On the Developper Settings, create a Personnal access token (classic) with read access to the audit_logs.
3. Validate the configuration and save the token for the configuration of the connector.


### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Github  audit logs`. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Fetch new audit logs from Github](../../../automate/library/github.md) trigger
2. Set up the module configuration with the Github organization and the APIkey. Set up the trigger configuration with the intake key
3. Start the playbook and enjoy your events
