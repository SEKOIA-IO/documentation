uuid: 2ffff1fd-fed7-4a24-927a-d619f2bb584a
name: ESET Protect / Inspect
type: intake
last updated: 16/07/2024

## Overview

- **Plan**: Defend Core / Defend Prime
- **Supported environment**: On Premise / SaaS
- **Version compatibility, if applicable**: 9.x, 10.x, 11.x

- **Detection based on**: Security Alerts
- **Supported application or feature**:
    - Audit Events
    - Firewall aggregated events
    - HIPS aggregated events
    - Threat events
    - ESET Inspect alerts


## High-Level Architecture Diagram

- **Type of integration**: Outbound: PUSH to Sekoia.io

- **Schema**

![consume_azure_logs](/assets/integration/integration_catalog/<techno_name>/image.png)

## Specification

### Prerequisites

- **Licence level**:
    - Core
    - Prime

- **Resource**:
    - Self managed syslog forwarder

- **Network**:
    - Customer Outbound traffic possible opening

- **Permissions**:
    - API Credentials: There's no api key
    - Configuration Access:  _ Minimum level of permissions required for the user doing the configuration._
    - Service account permission: The service account permission needed  for the configuration of the intake in the Sekoia.io product.

### Transport Protocol/Method

- **Cloud Storage**: Amazon S3 Bucket / Microsoft Azure Eventhub / Microsoft Azure BlobStorage / Google Pub/Sub
- **Direct HTTP**
x **Direct Syslog**
- **Indirect Syslog**

### Logs details

- **Supported type(s) of structure**:
    - CEF
    - Common Log Format (CLF)
    - Delimiter Separated Value (DSV)
    x JSON
    - Key-Value
    - Plain Text
    - Multi-line

- **Supported verbosity level**:
    - **Emergency**: system is unusable
    X **Alert**: action must be taken immediately
    - **Critical**: critical conditions
    - **Error**: error conditions
    - **Warning**: warning conditions
    - **Notice**: normal but significant condition
    - **Informational**: informational messages
    - **Debug**: debug-level messages

!!! Note
    This is a description of the log level based on the taxonomy of the [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424) for standardization purpose. Please adapt to the wording used by the editor.

- **Supported functionalities**: See section "Supported application or feature" on top of this page.
- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd party solution

__TO ADAPT__
- Detailed Procedure: 
    To enable Syslog server in ESET Protect on On-Prem :
        1. In admin console go to `More` > `Settings`.
        2. Open `Advanced Settings` tab.

            ![Advanced Settings](/assets/instructions/eset_protect/enable_syslog_1.png)

        3. Click on `Syslog server` > `Use Syslog server`.
        4. Then click on `Logging` > `Export logs to Syslog` and choose `JSON` format.
        5. Save configuration.

            ![Syslog configuration](/assets/instructions/eset_protect/enable_syslog_2.png)

    To enable Syslog server in ESET Protect on Cloud :
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

        ![Advanced Settings](/assets/instructions/eset_protect/cloud_syslog.png)
        
- Event Categories: Network device logs, Authentication logs, Host network interface, Web application firewall logs
- Event Selection: Guidance on selecting event types when sending logs.
---> Visual Aids: Include screenshots or videos if possible.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

__TO REMOVE IF NOT RELEVANT__
{!_shared_content/integration/connector_configuration.md!}

__TO REMOVE IF NOT RELEVANT__
{!_shared_content/integration/forwarder_configuration.md!}

## Detection section


{!_shared_content/operations_center/detection/generated/suggested_rules_2ffff1fd-fed7-4a24-927a-d619f2bb584a_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2ffff1fd-fed7-4a24-927a-d619f2bb584a.md!}

## Further readings

- [Export logs to Syslog](https://help.eset.com/protect_admin/10.0/en-US/admin_server_settings_export_to_syslog.html)
- [Export logs to Syslog server from ESET PROTECT (8.x–10.x)](https://techcenter.eset.nl/en-US/kb/articles/export-logs-to-syslog-server-from-eset-protect-8x-10x)
- [Collect logs from ESET PROTECT with Elastic Agent](https://docs.elastic.co/integrations/eset_protect#to-collect-data-from-eset-protect-via-syslog-follow-the-below-steps)
- [Support: Export logs to Syslog server from ESET PROTECT On-Prem](https://support.eset.com/en/kb8022-export-logs-to-syslog-server-from-eset-protect)

