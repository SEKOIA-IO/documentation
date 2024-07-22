uuid: 916c13a8-c109-49f0-94db-d6a2300f5580
name: Fastly Next-Gen WAF
type: intake


## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Alert
- **Supported application or feature**:

Fastly Next-Gen WAF is a web application firewall solution designed to protect online assets by mitigating web application threats, ensuring security, and enhancing application performance with its edge-based, real-time protection capabilities.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.



## Configure

### Creating API access tokens

1. Go to the [Fastly WAF](https://dashboard.signalsciences.net) and log in.
2. From the **My Profile** menu, select API access tokens.
3. Click **Add API access token**.
4. In the **Token name** field, enter a name to identify the access token.
5. Click **Create API access token**.
6. Record the token in a secure location for your use. Then, click **Continue** to finish creating the token.

!!! Warning
	This is the only time the token will be visible. Record the token and keep it secure.

### Sekoia.io configuration procedure

#### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Fastly WAF`.
2. Copy the associated Intake key

#### Pull the logs to collect them on Sekoia.io

Go to the Sekoia.io [playbook page](https://app.sekoia.io/operations/playbooks), and follow these steps:

1. Click **+ PLAYBOOK** button to create a new one
2. Select **Create a playbook from scratch**
3. Give it a name in the field **Name**
4. Open the left panel, click **Fastly** then select the trigger `Fetch new events from Fastly WAF`
5. Click **Create**

6. Create a **Module configuration**. Name the module configuration as you wish.
7. Create a **Trigger configuration** using: 
7.1. Type the `Intake key` created on the previous step
7.2 Enter `User's email`, `API token`, `Corporation name` and `Site name` from the Fastly WAF dashboard

- Click the **Save** button
- **Activate the playbook** with the toggle button in the top right corner of the page

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/916c13a8-c109-49f0-94db-d6a2300f5580_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_916c13a8-c109-49f0-94db-d6a2300f5580_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/916c13a8-c109-49f0-94db-d6a2300f5580.md!}

