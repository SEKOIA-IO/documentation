uuid: a1dbed03-cd69-4a51-8ae5-aa67d2f29fcb
name: Jumpcloud Directory Insights
type: intake


## Overview
Jumpcloud Directory Insights provides activity records related to your organization.

- **Vendor**: JumpCloud
- **Plan**: Defend Core & Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**:OAuth audit logs, Authentication logs





## Configure

### Generate API token

1. Sign-in in your Jumpcloud tenant with administrator role
2. Click on your username on the top right of the screen
3. Select `My API Key`

### Create the intake in Sekoia.io

1. Go to the [intake page](https://app.sekoia.io/operations/intakes)
2. Create a new intake from the format `Jumpcloud Directory Insights`.
3. Copy the intake key

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Jumpcloud Directory Insights Connector](../../../automate/library/jumpcloud-directory-insights.md) trigger
2. Set up the module configuration with your API Key. Set up the trigger configuration with the intake key and select the event types you want to collect (`all` by default, refer to the [Jumpcloud Directory Insights service list](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Using-the-Directory-Insights-API/JSON-POST-Request-Body) for other possible values).
3. Start the playbook and enjoy your events


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a1dbed03-cd69-4a51-8ae5-aa67d2f29fcb_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/a1dbed03-cd69-4a51-8ae5-aa67d2f29fcb.md!}

## Further Readings

- [Jumpcloud Directory Insights API documentation](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html)
