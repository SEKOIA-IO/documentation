uuid: 57eda191-2f93-4fd9-99a2-fd8ffbcdff50
name: Bitsight SPM
type: intake

## Overview

Bitsight Security Performance Management enables organizations to continuously monitor, measure, and improve their cybersecurity performance by providing actionable insights and metrics on security posture and risk.

- **Vendor**: BitSight Technologies
- **Plan**: Defend Core & Defend Prime
- **Supported environment**: Saas
- **Detection based on**: Alert

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.
    
## Supported events

This integration supports the following events:

- Findings (with vulnerability detail and asset detail)

## Configure

This setup guide will show you how to provide an integration between Bitsight SPM and Sekoia.io.

### Generate the API token

To collect the events from the Cato Networks platform, an API token is required:

1. Make sure the Bitsight user used for the integration has at least Reader permissions.
2. Log in to Bitsight Security Ratings Platform
3. Go to `Settings` -> `Account` -> `API Token`  -> `Generate New Token (API Key)`
4. Create new API Token

    ![Personal settings](/assets/instructions/bitsight/new_token.png)


### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Bitsight SPM`. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the `Bitsight SPM` trigger
2. Set up the module configuration with the Api Token and Company UUIds. Set up the trigger configuration with the intake key
3. Start the playbook and enjoy your events

{!_shared_content/operations_center/integrations/generated/57eda191-2f93-4fd9-99a2-fd8ffbcdff50_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_57eda191-2f93-4fd9-99a2-fd8ffbcdff50_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/57eda191-2f93-4fd9-99a2-fd8ffbcdff50.md!}

## Further readings
- [Bitsight API Token Management](https://help.bitsighttech.com/hc/en-us/articles/115014888388-API-Token-Management)