uuid: f5f05e2a-32fc-432d-9f00-11f490ae15f4
name: Juniper NGFW
type: intake

## Overview

Juniper Next-Generation Firewall (NGFW) services provide a set of cyber defenses that, together, reduce your attack surface. With the SRX Series firewall and Juniper Secure Edge at their core, high-performance NGFW services deliver integrated threat protection, application recognition, user identification services, and large-scale content inspection.

- **Vendor**: Juniper
- **Supported environment**: On Premise
- **Detection based on**: Telemetry
- **Supported application or feature**: Firewall logs

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**
![juniper_ngfw_architecture](/assets/integration/juniper_ngfw_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Root access to the Juniper appliance
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Syslog
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Quick Configuration Procedure

1. Log in to your Juniper NGFW appliance.
2. Set up the log service :
    
    > Note : if your security policy requires extra-security (ex: tls) between the application and the syslog forwarder,    modify the configuration accordingly

    ```bash
    set security log mode stream
    set security log format sd-syslog
    set security log source-interface {CHANGE_WITH_YOUR_INTERFACE}}
    ```

3. Set up the destination log server (forwarder) parameters : 

    > Note : if your security policy requires extra-security (ex: tls) between the application and the syslog forwarder, modify the configuration accordingly

    ```bash
    set security log stream sekoia_forwarder format sd-syslog
    set security log stream sekoia_forwarder host {IP_OF_YOUR_SEKOIA_FORWARDER} port {SEKOIA_FORWARDER_SPECIFIC_PORT}
    set security log stream sekoia_forwarder category {ADAPT_TO_YOUR_NEEDS}
    ```
    > [log security categories reference](https://www.juniper.net/documentation/us/en/software/junos/cli-reference/topics/ref/statement/security-edit-category-security-logging.html)

!!! Note
    If you encounter any issues during the configuration specified in this section "Instructions on the 3rd Party Solution," please do not hesitate to contact your editor. We also welcome any suggestions for improving our documentation to better serve your needs.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/f5f05e2a-32fc-432d-9f00-11f490ae15f4_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/integrations/generated/f5f05e2a-32fc-432d-9f00-11f490ae15f4.md!}
