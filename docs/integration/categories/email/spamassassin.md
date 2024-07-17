uuid: 7954ae6f-eafa-404d-8e15-4b99a12b754c
name: SpamAssassin
type: intake

## Overview

SpamAssassin is a computer program used for e-mail spam filtering. SpamAssassin uses a variety of spam-detection techniques, including DNS-based and fuzzy-checksum-based spam detection, Bayesian filtering, external programs, blacklists and online databases. It is released under the Apache License 2.0 and is now part of the Apache Foundation.

- **Vendor**: Apache Software Foundation
- **Plan**: Defend Core
- **Supported environment**: On Premise
- **Version compatibility**: 3.4.6 (Latest version as of now)
- **Detection based on**: Telemetry
- **Supported application or feature**: Email spam filtering
- **Coverage Score**: 2

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![spamassassin_architecture](/assets/integration/apache_spam_assassin_architecture.png){: style="max-width:100%"}

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
    - Administrator or Root access to the SpamAssassin host
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain Text
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**: `/var/log/spamd.log`

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward SpamAssassin Logs to Sekoia.io

This setup guide will show you how to forward logs produced by your SpamAssassin servers to Sekoia.io by means of an rsyslog transport channel.

#### Detailed Procedure:

1. **Install and Configure Rsyslog:**
   - Ensure that the `rsyslog` package is installed on your server.
   - Load the `imfile` module to read log files:

     ```bash
     $ModLoad imfile
     ```

2. **Configure Rsyslog to Monitor SpamAssassin Log Files:**
   - Add the following configuration to your `rsyslog` configuration file (usually found in `/etc/rsyslog.conf` or `/etc/rsyslog.d/`):

     ```bash
     $InputFileName /var/log/spamd.log
     $InputFileStateFile stat-apache-spamassassin
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

{!_shared_content/operations_center/detection/generated/suggested_rules_7954ae6f-eafa-404d-8e15-4b99a12b754c_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/7954ae6f-eafa-404d-8e15-4b99a12b754c.md!}

## Further readings

- The code of the Intake format is available [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/SpamAssassin).
- [SpamAssassin documentation](https://spamassassin.apache.org/)