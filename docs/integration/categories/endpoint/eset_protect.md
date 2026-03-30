---
uuid: 2ffff1fd-fed7-4a24-927a-d619f2bb584a
name: ESET Protect / Inspect
type: intake
---

# eset\_protect

### Overview

* **Supported environment**: On Premise / SaaS
* **Version compatibility, if applicable**: 9.x, 10.x, 11.x
* **Detection based on**: Telemetry, Alerts, Audit
* **Supported application or feature**:
  * Audit Events
  * Firewall aggregated events
  * HIPS aggregated events
  * Threat events
  * ESET Inspect alerts

### High-Level Architecture Diagram

* **Type of integration**: Outbound (PUSH to Sekoia.io)
* **Schema**

{: style="max-width:100%"}

### Specification

#### Prerequisites

* **Resource**:
  * Self-managed syslog forwarder
* **Network**:
  * **On Premise**: Outbound traffic allowed
  * **SaaS**: Customer Inbound and Outbound traffic possible opening
* **Permissions**:
  * Administrator access to the ESET instance
  * Root access to the Linux server with the syslog forwarder

#### Transport Protocol/Method

* **Indirect Syslog** for On Premise and SaaS

#### Logs details

* **Supported functionalities**: See section [Overview](eset_protect.md#overview)
* **Supported type(s) of structure**: JSON
* **Supported verbosity level**: Alert, Informational

!!! Note This is a description of the log level based on the taxonomy of the [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424) for standardization purpose. Please adapt to the wording used by the editor.

### Step-by-Step Configuration Procedure

#### Create an api key

To enable Syslog server in ESET Protect on On-Prem :

1. In admin console go to `More` > `Settings`.
2. Open `Advanced Settings` tab.
3. Click on `Syslog server` > `Use Syslog server`.
4. Then click on `Logging` > `Export logs to Syslog` and choose `JSON` format.
5. Save configuration.

!!! warning Important note - For ESET Protect Cloud, you will required a secured syslog forwarder. Please read our article [how to secure data collection to the syslog forwarder](../../../../integration/ingestion_methods/syslog/secured_forwarding.md)

To enable Syslog server in ESET Protect on Cloud:

1. In admin console go to `More` > `Admin` > `Settings`.
2. Click `General` > `Syslog`
3. Check `Enable syslog sending`
4. Select `JSON` as the format of the payload
5. Select `Syslog` as the format of the envelope
6. Select `Information` as the minimal log level
7. Check all event types
8. Type the address of the log concentrator
9. Check `Validate CA Root certificates of TLS connections`
10. Copy the public certificate of the Certificate Authority in the textarea
11. Click `Apply settings`

#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

{!\_shared\_content/integration/forwarder\_configuration.md!}

{!\_shared\_content/operations\_center/integrations/generated/2ffff1fd-fed7-4a24-927a-d619f2bb584a\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_2ffff1fd-fed7-4a24-927a-d619f2bb584a\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/2ffff1fd-fed7-4a24-927a-d619f2bb584a.md!}

### Further readings

* [Export logs to Syslog](https://help.eset.com/protect_admin/10.0/en-US/admin_server_settings_export_to_syslog.html)
* [Export logs to Syslog server from ESET PROTECT (8.x–10.x)](https://techcenter.eset.nl/en-US/kb/articles/export-logs-to-syslog-server-from-eset-protect-8x-10x)
* [Collect logs from ESET PROTECT with Elastic Agent](https://docs.elastic.co/integrations/eset_protect#to-collect-data-from-eset-protect-via-syslog-follow-the-below-steps)
* [Support: Export logs to Syslog server from ESET PROTECT On-Prem](https://support.eset.com/en/kb8022-export-logs-to-syslog-server-from-eset-protect)
