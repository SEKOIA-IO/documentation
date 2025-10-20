uuid: d9f337a4-1303-47d4-b15f-1f83807ff3cc
name: Imperva Web Application Firewall
type: intake

## Overview

Imperva Web Application Firewall helps you to protect your web applications and your APIs.

- **Vendor**: Imperva
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Imperva WAF dataset



## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

- Log on to your [Imperva control panel](https://management.service.imperva.com/)
- Go to [Account > Account Management > SIEM Logs > Log Configuration](https://management.service.imperva.com/siem-config-service).
- Click `Add connection`
- Select `Imperva API` as delivery method
- Type a name for the connection
- Click `Generate API keys`

!!! Note
    Copy the API ID, the API Key and the Log Server URI.

- Click `Create`
- On the new connection, click `Add log type`
- Select the log types to forward (at least, `Access logs`; You can add `Security Logs` for more detections)
- Select the default website log level (at least, a log level with `Access logs`)
- Select `CEF` as format
- Enable `Compress logs`
- If you wish to enable log encryption, upload your public key (see [Imperva documentation](https://docs-cybersec.thalesgroup.com/bundle/cloud-application-security/page/settings/log-integration.htm#EnableEncryption) for more details)
- Enable the state `Enabled`
- Click `Save`

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/connector_configuration.md!}

{!_shared_content/operations_center/integrations/generated/d9f337a4-1303-47d4-b15f-1f83807ff3cc_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d9f337a4-1303-47d4-b15f-1f83807ff3cc_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/d9f337a4-1303-47d4-b15f-1f83807ff3cc.md!}

## Further Readings

- [Imperva Log Integration Documentation](https://docs-cybersec.thalesgroup.com/bundle/cloud-application-security/page/settings/log-integration.htm)
