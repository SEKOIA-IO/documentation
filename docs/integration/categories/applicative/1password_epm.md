uuid: 09754cc4-e247-4712-9a76-25529ba11b8b
name: 1Password EPM
type: intake

## Overview

1Password's Enterprise Password Manager offers robust security features for businesses, enabling secure sharing and management of passwords and sensitive data across teams, with advanced admin controls and seamless integration into existing workflows.

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Plan**: 
- **Supported environment**: SaaS

- **Detection based on**: Telemetry, Audit
- **Supported application or feature**:
    - Audit Events
    - Item Usages
    - Sign-in Attempts

{!_shared_content/operations_center/detection/generated/suggested_rules_09754cc4-e247-4712-9a76-25529ba11b8b_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/09754cc4-e247-4712-9a76-25529ba11b8b.md!}

## Configure

### How to create an API token

1. Log in the 1Password console
2. On the right panel, click `Integrations`

    ![step_1.png](/assets/operation_center/integration_catalog/cloud_and_saas/1password/01_integration.png)

3. In the Events Reporting, Click the `Other`

    ![step_2.png](/assets/operation_center/integration_catalog/cloud_and_saas/1password/02_events_reporting.png)

4. Type a name for the Integration and click `Add Integration`

    ![step_3.png](/assets/operation_center/integration_catalog/cloud_and_saas/1password/03_create_token.png)

5. Type a name for the token, select the expiration period
6. Select `Audit events`, `Item usage events` and `Sign-in attempts` as events to report
7. Click `Issue token`

    ![step_4.png](/assets/operation_center/integration_catalog/cloud_and_saas/1password/04_issue_token.png)

### Create your intake

Go to your Sekoia.io [Intakes page](https://app.sekoia.io/operations/intakes), and follow these steps:

1. Click on **+ Intake** button to create a new one
2. Choose **1Password EPM**, give it a name and choose the relevant Entity
3. Click on **Create** button
4. Copy the **Intake key**

!!! Note
	Save the `Intake key` on a block note. It will be used in the next step.

### Pull the logs to collect them on Sekoia.io

Go to the Sekoia.io [playbook page](https://app.sekoia.io/operations/playbooks), and follow these steps:

1. Click on **+ PLAYBOOK** button to create a new one
2. Select **Use a template**
3. Search for `1Password` keyword on the search bar and select the template named `Fetch new events from 1Password EPM`
4. Create a **Module configuration** using 
  - API token from `How to create an API token` step. 
  - Base URL depending by the server that hosts your 1Password account:
  
    | If your account is on:	 | Your base URL is:                                                                                          |
    |-------------------------|------------------------------------------------------------------------------------------------------------|
    | 1Password.com           | https://events.1password.com (1Password Business) <br/>https://events.ent.1password.com (1Password Enterprise)  |
    | 1Password.ca            | https://events.1password.ca                                                                                |
    | 1Password.eu            | https://events.1password.eu                                                                                |

    Name the module configuration as you wish

5. Create a **Trigger configuration** using `Intake key` created on the previous step
6. Click on the **Save** button
7. Toggle **Activate the playbook** on the top right corner of the page

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)
