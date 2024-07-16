uuid: ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9
name: HAProxy
type: intake
last updated: DD/MM/YYYY

## Overview

HAProxy is a free, open source software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications that spreads requests across multiple servers. HAProxy has a lot of features and because it is located between your infrastructure and your clients, it can give you a lot of information about either of them.

- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**: 2.9 or highier

- **Detection based on**: Telemetry
- **Supported application or feature**:
    - Access Traffic

## High-Level Architecture Diagram

- **Type of integration**: Outbound: PUSH to Sekoia.io

- **Schema**

![haproxy_architecture](/assets/integration/haproxy_architecture.png)

## Specification

### Prerequisites

- **Resource**:
    - Self managed syslog forwarder

- **Network**:
    - Customer Outbound traffic possible opening

- **Permissions**:
    - Configuration Access:
        - Administrator or Root of the host where HAProxy application is installed.
        - Root of the Linux server where the syslog forwarder is installed.

### Transport Protocol/Method

- **Indirect Syslog**

!!! Note
    One can also choose to directly send those logs to Sekoia.io over HTTPS by instally a Sekoia.io Endpoint Agent and using the "Collect logs in files" methode.

### Logs details

- **Supported type(s) of structure**:
    - Plain Text

- **Supported verbosity level**:
    - **Informational**: informational messages

!!! Note
    This is a description of the log level based on the taxonomy of the [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424) for standardization purpose. Please adapt to the wording used by the editor.

- **Supported functionalities**: See section "Supported application or feature" on top of this page.
- **Default Log Location**: By default events are forwarded to `/var/lib/haproxy/dev/log` then processed by a local rsyslog to store them on `/var/log/haproxy.log`.

!!! Note
    HAProxy configuration default file `haproxy.cfg` will be found in the directory `/etc/haproxy`

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

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

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

_TO REPLACE by current links about Detection rules available, List of event types, List of extracted fields_

{!_shared_content/operations_center/detection/generated/suggested_rules_ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9.md!}

## Further readings

- The code of the Intake format is available [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/HAProxy).
- [HAProxy Official Documentation](http://www.haproxy.org/#docs)

