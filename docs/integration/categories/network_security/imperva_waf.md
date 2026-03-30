# imperva\_waf

uuid: d9f337a4-1303-47d4-b15f-1f83807ff3cc name: Imperva Web Application Firewall type: intake

### Overview

Imperva Web Application Firewall helps you to protect your web applications and your APIs.

* **Vendor**: Imperva
* **Supported environment**: SaaS
* **Detection based on**: Telemetry
* **Supported application or feature**: Cloud WAF service

#### Supported events

This integration supports the following event types:

* `Access Logs`
* `Security Logs`

### Step-by-Step Configuration Procedure

#### Instructions on the 3rd Party Solution

* Log on to your [Imperva control panel](https://management.service.imperva.com/)
* Go to your `Account > Account Management`
* Go to [`SIEM Logs > Log Configuration`](https://management.service.imperva.com/siem-config-service).
* Click `Add connection`
* Select `Imperva API` as delivery method
* Type a name for the connection
* Click `Generate API keys`

!!! Note Copy the API ID, the API Key and the Log Server URI.

* Click `Close`
* On the new connection, click `Add log type`
* Select `Cloud WAF` as the dataset
* Select the log types to forward (at least, `Access logs`; You can add `Security Logs` for more detections)
* Select the default website log level (at least, a log level with `Access logs`)
* Select `CEF` as format
* Enable `Compress logs`
* If you wish to enable log encryption, upload your public key (see [Imperva documentation](https://docs-cybersec.thalesgroup.com/bundle/cloud-application-security/page/settings/log-integration.htm#EnableEncryption) for more details)
* Enable the state `Enabled`
* Click `Add log type` to save

#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

{!\_shared\_content/integration/connector\_configuration.md!}

{!\_shared\_content/operations\_center/integrations/generated/d9f337a4-1303-47d4-b15f-1f83807ff3cc\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_d9f337a4-1303-47d4-b15f-1f83807ff3cc\_do\_not\_edit\_manually.md!} {!\_shared\_content/operations\_center/integrations/generated/d9f337a4-1303-47d4-b15f-1f83807ff3cc.md!}

### Further Readings

* [Imperva Log Integration Documentation](https://docs-cybersec.thalesgroup.com/bundle/cloud-application-security/page/settings/log-integration.htm)
