uuid: 2886cd2d-f686-4e7d-9976-250cba2eaf5b
name: Broadcom Edge Secure Web Gateway
type: intake

## Overview

Broadcom Edge Security Web Gateway provides comprehensive protection for web traffic, offering advanced threat detection and prevention capabilities, along with granular policy controls, to safeguard organizations against evolving cyber threats at the network edge.

- **Vendor**: Broadcom
- **Plan**: Defend Core
- **Supported environment**: On Premise
- **Version compatibility**: 7.3
- **Detection based on**: Telemetry
- **Supported application or feature**: Access logs

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![broadcom_edge_secure_web_gateway_architecture](/assets/integration/broadcom_edge_secure_web_gateway_architecture.png){: style="max-width:100%"}

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Broadcom Edge Secure Web Gateway device
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain text
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

This setup guide will show you how to provide an integration between Broadcom Edge Secure Web Gateway events and Sekoia.io.

#### Set Access Logs Format

- In the Management Console, go to `Administration` > `Logging` > `Access Logging`> `General`
- In `Log Formats`, click `Add New Format`
- Type a format name
- Select `Custom format string` as the format type
- Paste the following template in the log fields:
    ```json
    <111>1 $(date)T$(x-bluecoat-hour-utc):$(x-bluecoat-minute-utc):$(x-bluecoat-second-utc)$(s-computername) bluecoat - access_log - date=$(date) time=$(time) c-ip=$(c-ip) c-url=$(quot)$(url)$(quot) cs-Referer=$(quot)$(cs(Referer))$(quot) cs-user-agent=$(quot)$(cs(User-Agent))$(quot) cs-bytes=$(cs-bytes) cs-categories=$(cs-categories) cs-host=$(cs-host) cs-ip=$(cs-ip) cs-threat-risk=$(cs-threat-risk) cs-uri-path=$(cs-uri-path) cs-uri-port=$(cs-uri-port) cs-uri-query=$(quot)$(cs-uri-query)$(quot) cs-uri-scheme=$(cs-uri-scheme) cs-username=$(cs-username) cs-categories=$(cs-categories) cs-referer=$(cs-Referer) rs-content-type=$(quot)$(rs(Content-Type))$(quot) rs-status=$(rs-status) rs-version=$(rs-version) s-action=$(s-action) s-ip=$(s-ip) sc-bytes=$(sc-bytes) sc-status=$(sc-status) rs-content-type=$(rs-Content-Type) time-taken=$(time-taken) x-rs-certificate-hostname=$(x-rs-certificate-hostname) x-virus-id=$(x-virus-id) x-data-leak-detected=$(x-data-leak-detected) x-dns-cs-dns=$(x-dns-cs-dns) x-dns-cs-opcode=$(x-dns-cs-opcode) x-dns-cs-qclass=$(x-dns-cs-qclass) x-dns-cs-qtype=$(x-dns-cs-qtype) x-dns-cs-threat-risk-level=$(x-dns-cs-threat-risk-level) x-dns-rs-a-records=$(x-dns-rs-a-records) x-dns-rs-cname-records=$(x-dns-rs-cname-records) x-dns-rs-ptr-records=$(x-dns-rs-ptr-records) x-dns-rs-rcode-records=$(x-dns-rs-rcode-records)
    ```
- Test the format
- Apply the change

#### Enable Syslog Forwarding

- Go to `Administration` > `Logging` > `Access Logging`> `General`
- In `Logs`, click `Add New Log`
- In `Log Setting`, type the name of the log and select the format created previously
- In `Upload client`, select `custom client`
    - Type the log concentrator's IP address and port as the destination
- In `Upload Schedule`, select `continuously` for the `Upload the access log` setting
- Apply the change

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/2886cd2d-f686-4e7d-9976-250cba2eaf5b_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_2886cd2d-f686-4e7d-9976-250cba2eaf5b_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2886cd2d-f686-4e7d-9976-250cba2eaf5b.md!}

## Further readings

- [Configure an Access Log](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/edge-swg/7-3/getting-started/page-help-administration/page-help-logging/page-help-access-logging-log.html)
- [Configure an Access Log Format](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/edge-swg/7-3/getting-started/page-help-administration/page-help-logging/log-formats/page-help-access-logging-format.html)