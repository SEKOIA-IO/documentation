uuid: 60af2bd6-7ef0-48a7-a6db-90fcdd7236f1
name: FortiMail
type: intake

## Overview

Fortinet cybersecurity solutions sell physical products such as firewalls, plus software and services such as anti-virus protection, intrusion prevention systems, and endpoint security components.

- **Vendor**: Fortinet
- **Supported environment**: On Premise
- **Detection based on**: Telemetry
- **Supported application or feature**: Email Security

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![fortinet_fortimail_architecture](/assets/integration/fortinet_fortimail_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator privileges on the FortiMail appliance
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Key-Value
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

This setup guide will show you how to forward your FortiMail logs to Sekoia.io by means of a syslog transport channel.

#### FortiMail Logs

- On FortiMail appliances, most of the important hardware and software activities that are relevant for security detection and analysis are logged into six files:
    - History (statistics): Records all email traffic going through the FortiMail unit.
    - System Event (kevent): Records system management activities, including changes to the system configuration as well as administrator and user log-ins and log-outs.
    - Mail Event (event): Records mail activities.
    - Antispam (spam): Records spam detection events.
    - Antivirus (virus): Records virus intrusion events.
    - Encryption (encrypt): Records detection of IBE-related events.

#### Transport to the Collector

- **Prerequisites:**
    - Administrator privileges on the FortiMail appliance
    - Traffic towards the syslog must be open on `UDP 514`

- **Configure Logging to a Syslog Server:**

    1. Go to `Log and Report > Log Settings > Remote`.
    2. Click `New` to create a new entry OR double-click an existing entry to modify it.
    3. Select `Enable` to allow logging to a remote host.
    4. In `Profile name`, enter a profile name.
    5. In `IP`, enter the IP address of the `Syslog server` where the FortiMail unit will store the logs.
    6. In `Port`, enter the UDP port number on which the Syslog server listens for connections (by default, `UDP 514`).
    7. From `Level`, select the severity level that a log message must equal or exceed in order to be recorded to this storage location.
    8. From `Facility`, select the facility identifier that the FortiMail unit will use to identify itself when sending log messages.

        > To easily identify log messages from the FortiMail unit when they are stored on a remote logging server, enter a unique facility identifier, and verify that no other network devices use the same facility identifier.

    9. From `Log protocol`, select `Syslog`.
    10. In `Logging Policy Configuration`, enable the types of logs you want to record to this storage location.
    11. Click `Create`.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/60af2bd6-7ef0-48a7-a6db-90fcdd7236f1_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_60af2bd6-7ef0-48a7-a6db-90fcdd7236f1_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/60af2bd6-7ef0-48a7-a6db-90fcdd7236f1.md!}

## Further readings

- [Configure FortiMail Log Forwarding](https://docs.fortinet.com/document/fortimail/6.2.0/administration-guide/332364/configuring-logging#logging_2063907032_1949484)