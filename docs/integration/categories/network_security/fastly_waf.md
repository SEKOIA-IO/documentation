uuid: 916c13a8-c109-49f0-94db-d6a2300f5580
name: Fastly Next-Gen WAF
type: intake


## Overview

Fastly Next-Gen WAF is a web application firewall solution designed to protect online assets by mitigating web application threats, ensuring security, and enhancing application performance with its edge-based, real-time protection capabilities.

- **Vendor**: Fastly
- **Supported environment**: SaaS
- **Version compatibility**:
- **Detection based on**: Alert
- **Supported application or feature**: WAF Alerts

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution
#### Creating API access tokens

1. Go to the [Fastly WAF](https://dashboard.signalsciences.net) and log in.
2. From the **My Profile** menu, select API access tokens.
3. Click **Add API access token**.
4. In the **Token name** field, enter a name to identify the access token.
5. Click **Create API access token**.
6. Record the token in a secure location for your use. Then, click **Continue** to finish creating the token.

!!! Warning
	This is the only time the token will be visible. Record the token and keep it secure.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/connector_configuration.md!}

!!! Note
    For this procedure, you will need the `Intake key` created on the previous step, and `User's email`, `API token`, `Corporation name` and `Site name` from the Fastly WAF dashboard

{!_shared_content/operations_center/integrations/generated/916c13a8-c109-49f0-94db-d6a2300f5580_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_916c13a8-c109-49f0-94db-d6a2300f5580_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/916c13a8-c109-49f0-94db-d6a2300f5580.md!}

