uuid: d9f337a4-1303-47d4-b15f-1f83807ff3cc
name: Imperva Web Application Firewall
type: intake

## Overview

Imperva Web Application Firewall helps you to protect your web applications and your APIs.

- **Vendor**: Imperva
- **Plan**: Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Imperva WAF dataset



## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

- In your Imperva control panel, go to [Account > Account Management > SIEM Logs > WAF Log Setup](https://management.service.imperva.com/my/web-logs/settings).
- Select `Imperva API`, `CEF format` and `enable compression`.

!!! Note
    Copy the API ID, the API Key and the Log Server URI.

- Then go to [SIEM Logs > Websites Logs Level](https://management.service.imperva.com/my/web-logs/sites-settings)
- Enable for each website the log level `INFO`

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/connector_configuration.md!}

!!! Important
    At the end of the playbook, set up the action `Push events to intake` with a Sekoia.io API key and the intake key, from the intake previously created.

{!_shared_content/operations_center/integrations/generated/d9f337a4-1303-47d4-b15f-1f83807ff3cc_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d9f337a4-1303-47d4-b15f-1f83807ff3cc_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/d9f337a4-1303-47d4-b15f-1f83807ff3cc.md!}

## Further Readings

- [Imperva Log Integration Documentation](https://docs.imperva.com/bundle/cloud-application-security/page/settings/log-integration.htm)
