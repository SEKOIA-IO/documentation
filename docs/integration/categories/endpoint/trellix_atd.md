uuid: d2fb32f0-b722-4a32-ba9f-598215a8aacd
name: Trellix Advanced Threat Defense [ Beta ]
type: intake

## Overview

The Advanced Threat Defense Appliances are purpose-built, scalable, and flexible high-performance servers designed to analyze suspicious files for malware.

- **Vendor**: Trellix
- **Supported environment**: On Premise
- **Detection based on**: Telemetry
- **Supported application or feature**: Application logs

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**
![trellix_atd_architecture](/assets/integration/trellix_atd_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Root access to the Trellix ATD web interface
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Syslog
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the vendor.

## Step-by-Step Quick Configuration Procedure

1. Log on to the Advanced Threat Defense web interface.
2. Click **Manage** → **ATD Configuration** → **Syslog**, then select **Enable Logging**
3. In the Statistic to Log section, select the entries that suits your needs.
> Note: When HTTPS Session Log is enabled, Advanced Threat Defense web performance is impacted.
4. From the drop-down menu, select TCP
> Note, if your security policy requires extra-security (ex: tls) between the application and the syslog forwarder,    modify the configuration accordingly
5. Click **Enable Syslog** 
6. Type in the IP and port of the forwarder you want the logs sent to.
7. Click **Test Connection** and expect a "Test connection successful" message.
8. Click **Submit**

!!! Note
    If you encounter any issues during the configuration specified in this section "Instructions on the 3rd Party Solution," please do not hesitate to contact your vendor. We also welcome any suggestions for improving our documentation to better serve your needs.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/d2fb32f0-b722-4a32-ba9f-598215a8aacd_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d2fb32f0-b722-4a32-ba9f-598215a8aacd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d2fb32f0-b722-4a32-ba9f-598215a8aacd.md!}
