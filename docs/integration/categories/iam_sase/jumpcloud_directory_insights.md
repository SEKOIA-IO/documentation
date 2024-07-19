uuid: a1dbed03-cd69-4a51-8ae5-aa67d2f29fcb
name: Jumpcloud Directory Insights
type: intake


## Overview
  - **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**: Telemetry
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:

Jumpcloud Directory Insights provides activity records related to your organization.




## Configure

### Generate API token

1. Sign-in in your Jumpcloud tenant with administrator role
2. Click on your username on the top right of the screen 
3. Select `My API Key

### Create the intake in Sekoia.io

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) 
2. Create a new intake from the format `Jumpcloud Directory Insights`. 
3. Copy the intake key

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Jumpcloud Directory Insights Connector](../../../automate/library/jumpcloud-directory-insights.md) trigger
2. Set up the module configuration with your API Key. Set up the trigger configuration with the intake key and select the event types you want to collect (`all` by default, refer to the [Jumpcloud Directory Insights service list](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Using-the-Directory-Insights-API/JSON-POST-Request-Body) for other possible values).
3. Start the playbook and enjoy your events


## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_a1dbed03-cd69-4a51-8ae5-aa67d2f29fcb_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/a1dbed03-cd69-4a51-8ae5-aa67d2f29fcb.md!}

## Further Readings

- [Jumpcloud Directory Insights API documentation](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html)
