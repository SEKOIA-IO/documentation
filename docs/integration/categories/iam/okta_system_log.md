uuid: e6bb2404-8fc8-4124-a785-c1276277b5d7
name: Okta System log
type: intake


## Overview
Okta System log provides activity records related to your organization.

- **Vendor**: Okta
- **Plan**: Core + Prime
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: OAuth audit logs, Authentication logs


## Configure

### Generate API token

Sign in your Okta organization with administrator role and follow [this guide](https://developer.okta.com/docs/guides/create-an-api-token/main/#create-the-token) to create an API token.

### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Okta System logs`. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Fetch new system logs from OKTA](../../../automate/library/okta.md) trigger
2. Set up the module configuration with your API Key and the base url of your Okta instance. Set up the trigger configuration with the intake key
3. Start the playbook and enjoy your events

    !!! note

        According to your Okta subscription, you may need to decrease the ratelimit_per_minute in the trigger configuration. Please see the [OKTA documentation](https://help.okta.com/en-us/Content/Topics/Security/API.htm) for more information


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_e6bb2404-8fc8-4124-a785-c1276277b5d7_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/e6bb2404-8fc8-4124-a785-c1276277b5d7.md!}

## Further Readings

- [Okta documentation - create an API token](https://developer.okta.com/docs/guides/create-an-api-token/main/)
- [Okta documentation - System Log](https://developer.okta.com/docs/reference/api/system-log/)
