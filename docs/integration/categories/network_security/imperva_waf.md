uuid: d9f337a4-1303-47d4-b15f-1f83807ff3cc
name: Imperva Web Application Firewall
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:

Imperva Web Application Firewall helps you to protect your web applications and your APIs.

This setup guide describes how to forward security events collected on the Imperva WAF platform to Sekoia.io.




## Configure

### In Imperva interface

In your Imperva control panel, go to [Account > Account Management > SIEM Logs > WAF Log Setup](https://management.service.imperva.com/my/web-logs/settings).
Select Imperva API, CEF format and enable compression.
Copy the API ID, the API Key and the Log Server URI.

Then go to [SIEM Logs > Websites Logs Level](https://management.service.imperva.com/my/web-logs/sites-settings) and enable for each website the log level you want to get on Sekoia.io.

### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Imperva WAF. Copy the intake key.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Imperva WAF logs trigger](../../../automate/library/imperva.md#imperva-waf-logs). You can use the existing template to fasten and ease the creation of your playbook.
Set up a new module configuration with the information you copied previously.
Set up the trigger configuration with the frequency of the pull.

At the end of the playbook, set up the action `Push events to intake` with a Sekoia.io API key and the intake key, from the intake previously created.

Start the playbook and enjoy your events.


{!_shared_content/operations_center/integrations/generated/d9f337a4-1303-47d4-b15f-1f83807ff3cc_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d9f337a4-1303-47d4-b15f-1f83807ff3cc_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/d9f337a4-1303-47d4-b15f-1f83807ff3cc.md!}

## Further Readings

- [Imperva Log Integration Documentation](https://docs.imperva.com/bundle/cloud-application-security/page/settings/log-integration.htm)
