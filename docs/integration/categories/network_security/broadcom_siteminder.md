uuid: 2bfa5c39-bc73-48cf-afbd-7fd0eccf1d59
name: Broadcom Siteminder
type: intake

## Overview

Siteminder generates access logs directly on the system. Then the data can be sent to a log concentrator.

- **Vendor**: Broadcom
- **Supported environment**: On Premise
- **Detection based on**: Telemetry
- **Supported application or feature**: Web proxy, Web logs

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**
![broadcom_siteminder_architecture](/assets/integration/broadcom_siteminder_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Root access to the Siteminder machine
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Syslog
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

1. Log in to your Siteminder applicance as root.
2. Find the smaccess.log file on the system :
```bash
find /opt -name smaccess.log 2>/dev/null
```
3. Edit /etc/syslog-ng.conf
4. add a logging source as follows (replace {file_search_result} by the path you found above):
```bash
source s_siteminder_access {file("{file_search_result}");};
```
5. add a logging destination as follows :
> Note : if your security policy requires extra-security (ex: tls) between the application and the syslog forwarder, modify the configuration accordingly
```bash
destination d_syslog_forwarder {syslog("<YOUR_SYSLOG_FORWARDER_SERVER_IP>" transport("tcp") port(514));};
```
6. add a new "log" row filled with your new source and destination :
```bash
log {source(s_siteminder_accessdestination); destination(d_syslog_forwarder);};
```
7. save the file
8. restart the service
```bash
systemctl restart syslog-ng
```
!!! Note
    If you encounter any issues during the configuration specified in this section "Instructions on the 3rd Party Solution," please do not hesitate to contact your editor. We also welcome any suggestions for improving our documentation to better serve your needs.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/2bfa5c39-bc73-48cf-afbd-7fd0eccf1d59_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/integrations/generated/2bfa5c39-bc73-48cf-afbd-7fd0eccf1d59.md!}
