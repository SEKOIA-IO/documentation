uuid: a199fbde-508e-4cb9-ae37-842703494be0
name: BIND
type: intake

## Overview

BIND is an implementation of the Domain Name System (DNS) of the Internet. It performs both of the main DNS server roles, acting as an authoritative name server for domains, and acting as a recursive resolver in the network.

- **Vendor**: ISC
- **Plan**: Defend Core & Defend Prime
- **Supported environment**: On Premise
- **Version compatibility**: 9.18.8 (Latest version as of now)
- **Detection based on**: Telemetry
- **Supported application or feature**: DNS server

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![bind_architecture](/assets/integration/bind_architecture.png){: style="max-width:100%"}

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the BIND server
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain Text
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward BIND Logs to Sekoia.io

As of now, the main solution to collect BIND logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

#### Detailed Procedure:

1. **Configure BIND to Log Queries:**
   - First, you need to configure your BIND daemon to log queries and forward them to your rsyslog instance.
   - If rsyslog and BIND are installed on the same box, you can simply add the following statement in your BIND’s main configuration file (`named.conf`):

     ```bash
     logging {
         channel syslog_chan {
             syslog daemon;
             severity dynamic;
         };
         category default { syslog_chan; };
         category queries { syslog_chan; };
         category config { syslog_chan; };
         category security { syslog_chan; };
     };
     ```

2. **Restart BIND Service:**
   - Restart the BIND service to apply the logging configuration changes:
     ```bash
     systemctl restart named
     ```

3. **Configure Rsyslog to Monitor BIND Log Files:**
   - Add the following configuration to your `rsyslog` configuration file (usually found in `/etc/rsyslog.conf` or `/etc/rsyslog.d/`):

     ```bash
     # Bind log
     $InputFileName /var/log/bind.log
     $InputFileTag bind:
     $InputFileStateFile stat-bind
     $InputFileSeverity info
     $InputFileFacility local0
     $InputFilePollInterval 10
     $InputRunFileMonitor
     ```

4. **Forward Logs to a Concentrator:**
   - Configure rsyslog to forward logs to a syslog concentrator:

     ```bash
     *.* action(type="omfwd"
        target="<Concentrator_FQDN_or_IP>"
        port="<Remote_Port>"
        protocol="tcp"
        TCP_Framing="octet-counted"
     )
     ```

5. **Verify Syslog Server Configuration:**
   - On your syslog server, verify that it is configured to accept syslog messages from the BIND server on the specified port.

For more informations on [how to configure your BIND instance on its official website](https://kb.isc.org/docs/aa-01526).

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/a199fbde-508e-4cb9-ae37-842703494be0_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a199fbde-508e-4cb9-ae37-842703494be0_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/a199fbde-508e-4cb9-ae37-842703494be0.md!}
## Further readings

- [BIND documentation](https://kb.isc.org/docs/aa-01526)