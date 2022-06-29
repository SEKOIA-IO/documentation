uuid: d9f337a4-1303-47d4-b15f-1f83807ff3cc
name: Imperva Web Application Firewall
type: intake

## Overview

Imperva Web Application Firewall helps you to protect your web applications and your APIs.

This setup guide describes how to forward security events collected on the Imperva WAF platform to SEKOIA.IO.

{!xdr/features/collect/integrations/generated/imperva-waf_do_not_edit_manually.md!}

## Configure

### In Imperva interface

In your Imperva control panel, go to [Account > Account Management > SIEM Logs > WAF Log Setup](https://management.service.imperva.com/my/web-logs/settings).
Select Imperva API, CEF format and enable compression.
Copy the API ID, the API Key and the Log Server URI.

Then go to [SIEM Logs > Websites Logs Level](https://management.service.imperva.com/my/web-logs/sites-settings) and enable for each website the log level you want to get on SEKOIA.IO.

### Create the intake in SEKOIA.IO

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Imperva WAF. Copy the intake key.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Imperva WAF logs trigger](https://docs.sekoia.io/playbooks/library/imperva/#imperva-waf-logs). You can use the existing template to fasten and ease the creation of your playbook.
Set up a new module configuration with the information you copied previously.
Set up the trigger configuration with the frequency of the pull.

At the end of the playbook, set up the action `Push events to intake` with a SEKOIA.IO API key and the intake key, from the intake previously created.

Start the playbook and enjoy your events.

## Further Readings

- [Imperva Log Integration Documentation](https://docs.imperva.com/bundle/cloud-application-security/page/settings/log-integration.htm)