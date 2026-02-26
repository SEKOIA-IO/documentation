uuid: 7954ae6f-eafa-404d-8e15-4b99a12b754c
name: SpamAssassin
type: intake

## Overview

SpamAssassin is a computer program used for e-mail spam filtering. SpamAssassin uses a variety of spam-detection techniques, including DNS-based and fuzzy-checksum-based spam detection, Bayesian filtering, external programs, blacklists and online databases. It is released under the Apache License 2.0 and is now part of the Apache Foundation.

- **Vendor**: Apache Software Foundation
- **Supported environment**: On Premise
- **Version compatibility**: 3.4.6 (Latest version as of now)
- **Detection based on**: Telemetry
- **Supported application or feature**: Email spam filtering

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![spamassassin_architecture](/assets/integration/apache_spam_assassin_architecture.png){: style="max-width:100%"}

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites


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
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**: `/var/log/spamd.log`

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward SpamAssassin Logs to Sekoia.io

This setup guide will show you how to forward logs produced by your SpamAssassin servers to Sekoia.io by means of an rsyslog transport channel.

#### Detailed Procedure:

1. **Install Rsyslog:**
    - Ensure that the `rsyslog` package is installed on your server.

2. **Create a dedicated configuration**
    - Add a dedicated configuration file for SpamAssassin logs in `/etc/rsyslog.d/18-spamassassin.conf`:

     ```text
        module(load="imfile" PollingInterval="5")
        module(load="omfwd")

        input(
            type="imfile"
            File="/var/log/spamd.log"
            Facility="local5"
            Severity="notice"
            StateFile="stat-apache-spamassassin"
            PersistStateInterval="200"
            Ruleset="spamassassin-logs"
        )

        ruleset(name="spamassassin-logs") {
            # Forward to remote concentrator
            action(
                type="omfwd"
                target="CONCENTRATOR_FQDN_OR_IP"
                port="REMOTE_PORT"
                protocol="tcp"
                TCP_Framing="octet-counted"
            )
            # Prevent further processing of these messages
            stop
        }
     ```

!!! Note
    If you encounter any issues during the configuration specified in this section "Instructions on the 3rd Party Solution," please do not hesitate to contact your editor. We also welcome any suggestions for improving our documentation to better serve your needs.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/7954ae6f-eafa-404d-8e15-4b99a12b754c_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_7954ae6f-eafa-404d-8e15-4b99a12b754c_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/7954ae6f-eafa-404d-8e15-4b99a12b754c.md!}

## Further readings

- The code of the Intake format is available [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/SpamAssassin).
- [SpamAssassin documentation](https://spamassassin.apache.org/)
