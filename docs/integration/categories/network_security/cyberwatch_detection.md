uuid: c6a43439-7b9d-4678-804b-ebda6756db60
name: Cyberwatch Detection
type: intake

## Overview

Cyberwatch is a vulnerability detection and monitoring solution.

This integration encompasses the detection logs from Cyberwatch Vulnerability Manager.

- **Vendor**: Cyberwatch
- **Plan**: Defend Prime
- **Supported environment**: On Premise / Cloud
- **Version compatibility, if applicable**:
- **Detection based on**: Vulnerability Scanning
- **Supported application or feature**: Third-party application logs
- **Coverage Score**: 3

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![cyberwatch_detection_architecture](/assets/integration/cyberwatch_detection_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Cyberwatch Vulnerability Manager
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug
- **Supported type(s) of structure**: Key-Value

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Cyberwatch Detection Logs to Sekoia.io

This setup guide will show you how to forward your Cyberwatch logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Prerequisites:**
   - Have an internal log concentrator.

2. **Enable Syslog Forwarding for Cyberwatch:**
   - Once configured, Cyberwatch will send hourly the latest CVEs detected to the remote Syslog server:
     1. Click `Administration`.
     2. Click `External tools`.
     3. Click `Remote Syslog server`.
   
   - In the Remote Syslog server configuration, provide the address, the port, and the transport to the syslog concentrator.

   <video controls width="100%">
     <source src="/assets/operation_center/integration_catalog/application/Cyberwatch.webm" type="video/webm">
   </video>

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/c6a43439-7b9d-4678-804b-ebda6756db60_sample.md!}

## Detection section


The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_c6a43439-7b9d-4678-804b-ebda6756db60_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/c6a43439-7b9d-4678-804b-ebda6756db60.md!}

## Further readings

- [Configure a remote Syslog server](https://docs.cyberwatch.fr/help/en/administration/remote_syslog_configuration/)