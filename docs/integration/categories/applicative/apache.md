uuid: 6c2a44e3-a86a-4d98-97a6-d575ffcb29f7
name: Apache HTTP Server
type: intake

## Overview

The Apache HTTP Server, colloquially called Apache, is free and open-source cross-platform web server software, released under the terms of Apache License 2.0. Apache is developed and maintained by an open community of developers under the auspices of the Apache Software Foundation.

!!! info
    Access logs from Tomcat are compatible with the existing format Apache HTTP server. Catalina logs are not supported.

- **Vendor**: Apache Software Foundation
- **Plan**: Defend Core
- **Supported environment**: On Premise
- **Version compatibility, if applicable**: 2.4.51 (Latest version as of now)
- **Detection based on**: Telemetry
- **Supported application or feature**: Access and error log monitoring
- **Coverage Score**: 1

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![apache_http_server_architecture](/assets/integration/apache_http_server_architecture.png)

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites

- **Licence level**:
    - Open Source
- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Apache HTTP Server host
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Common Log Format (CLF), Combined Log Format (combined)
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Apache Logs to Sekoia.io

This setup guide will show you how to forward both your access and error logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Install and Configure Rsyslog:**
   - Ensure that the `rsyslog` package is installed on your server.
   - Load the `imfile` module to read log files:

     ```bash
     $ModLoad imfile
     ```

2. **Configure Rsyslog to Monitor Apache Log Files:**
   - Add the following configuration to your `rsyslog` configuration file (usually found in `/etc/rsyslog.conf` or `/etc/rsyslog.d/`):

     ```bash
     # Error log
     $InputFileName /var/log/apache2/error.log
     $InputFileTag apache:
     $InputFileStateFile stat-apache-error
     $InputFileSeverity error
     $InputFileFacility local5
     $InputFilePollInterval 1
     $InputRunFileMonitor

     # Access log
     $InputFileName /var/log/apache2/access.log
     $InputFileTag apache:
     $InputFileStateFile stat-apache-access
     $InputFileSeverity notice
     $InputFileFacility local5
     $InputFilePollInterval 1
     $InputRunFileMonitor
     ```

3. **Forward Logs to a Concentrator:**
   - Configure rsyslog to forward logs to a syslog concentrator:

     ```bash
     *.* action(type="omfwd"
        target="<Concentrator_FQDN_or_IP>"
        port="<Remote_Port>"
        protocol="tcp"
        TCP_Framing="octet-counted"
     )
     ```

!!! Note
    If you encounter any issues during the configuration specified in this section "Instructions on the 3rd Party Solution," please do not hesitate to contact your editor. We also welcome any suggestions for improving our documentation to better serve your needs.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/integrations/generated/6c2a44e3-a86a-4d98-97a6-d575ffcb29f7.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_6c2a44e3-a86a-4d98-97a6-d575ffcb29f7_do_not_edit_manually.md!}

## Further readings

- The code of the Intake format is available [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Apache).
- [Apache documentation](http://httpd.apache.org/docs/)