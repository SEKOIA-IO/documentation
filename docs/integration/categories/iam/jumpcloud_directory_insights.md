---
uuid: a1dbed03-cd69-4a51-8ae5-aa67d2f29fcb
title: Jumpcloud Directory Insights
name: Jumpcloud Directory Insights
type: intake
---


## Overview
Jumpcloud Directory Insights provides activity records related to your organization.

- **Vendor**: JumpCloud
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
3. Set up the intake configuration with your API Key and select the event types you want to collect (`all` by default, refer to the [Jumpcloud Directory Insights service list](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Using-the-Directory-Insights-API/JSON-POST-Request-Body) for other possible values).

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a1dbed03-cd69-4a51-8ae5-aa67d2f29fcb_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/a1dbed03-cd69-4a51-8ae5-aa67d2f29fcb.md!}

## Further Readings

- [Jumpcloud Directory Insights API documentation](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html)
