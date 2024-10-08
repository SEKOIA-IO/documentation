---
uuid: ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9
name: HAProxy
type: intake
---

## Overview

HAProxy is a free, open-source software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications, distributing requests across multiple servers. As it operates between your infrastructure and your clients, HAProxy offers extensive monitoring capabilities.

- **Vendor**: HAProxy Technologies
- **Supported Environment**: On Premise
- **Version Compatibility**: 2.9 or higher
- **Detection Based On**: Telemetry
- **Supported Application or Feature**: Access Traffic

## High-Level Architecture Diagram

- **Type of Integration**: Outbound (PUSH to Sekoia.io)
- **Schema**:

![haproxy_architecture](/assets/integration/haproxy_architecture.png){: style="max-width:100%"}

!!! Alternative Log Collection Method

    This will not be detailed on this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites

- **Resource**: Self-managed syslog forwarder
- **Network**: Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the HAProxy host
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported Structures**: Plain Text
- **Supported Verbosity Levels**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:
    - Events forwarded to `/var/lib/haproxy/dev/log`
    - Processed by a local rsyslog to `/var/log/haproxy.log`

!!! Note
    The default HAProxy configuration file `haproxy.cfg` is located in `/etc/haproxy`

### Sample of supported raw events

__TODO_BEFORE_MERGE__
## Step-by-Step Configuration Procedure

### Instructions on the 3rd party solution

After HAProxy has been setup and configured, the logs have to be sent to a syslog concentrator then forwarded to Sekoia.io.

By default, at HAProxy first installation, an rsyslog configuration is created on the repository `/etc/rsyslog.d/`, it contains the following lines:

```
# Create an additionnal socket in haproxy's chroot in order to allow logging via
# /dev/log to chroot'ed HAProxy processes
$AddUnixListenSocket /var/lib/haproxy/dev/log

# Send HAProxy messages to a dedicated logfile
:programname, startswith, "haproxy" {
    /var/log/haproxy.log
    stop
}
```

You only have to replace the configuration by the following lines:

```
# Create an additionnal socket in haproxy's chroot in order to allow logging via
# /dev/log to chroot'ed HAProxy processes
$AddUnixListenSocket /var/lib/haproxy/dev/log

# Use a condition that identifies specifically HaProxy logs that send them to a syslog concentrator
if ($programname startswith 'haproxy') then {
    # Log events locally
    /var/log/haproxy.log

    # Forward HAProxy logs to a concentrator
    action(
    type="omfwd"
    protocol="tcp"
    target="<Concentrator_FQDN_or_IP>"
    port="<Remote_Port>"
    TCP_Framing="octet-counted"
    )
}
```

For more information on Rsyslog configuration, please consult the [official website](https://www.rsyslog.com/doc/configuration/templates.html).

!!! Note
    If you encounter any issues during the configuration specified in this section "Instructions on the 3rd Party Solution," please do not hesitate to contact your editor. We also welcome any suggestions for improving our documentation to better serve your needs.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9.md!}
## Further readings

- [HAProxy Official Documentation](http://www.haproxy.org/#docs)
