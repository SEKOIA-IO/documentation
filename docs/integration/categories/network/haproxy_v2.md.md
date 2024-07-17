---
uuid: ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9
name: HAProxy
type: intake
last updated: DD/MM/YYYY
---

## Overview

HAProxy is a free, open-source software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications, distributing requests across multiple servers. As it operates between your infrastructure and your clients, HAProxy offers extensive monitoring capabilities.

- **Plan**: Defend Prime
- **Supported Environment**: On Premise
- **Version Compatibility**: 2.9 or higher
- **Detection Based On**: Telemetry
- **Supported Application or Feature**: Access Traffic

## High-Level Architecture Diagram

- **Type of Integration**: Outbound (PUSH to Sekoia.io)
- **Schema**:
![haproxy_architecture](/assets/integration/haproxy_architecture.png)

## Specification

### Prerequisites

- **Resource**: Self-managed syslog forwarder
- **Network**: Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the HAProxy host
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

!!! Note
    Logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method.

### Log Details

- **Supported Structures**: Plain Text
- **Supported Verbosity Levels**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:
    - Events forwarded to `/var/lib/haproxy/dev/log`
    - Processed by a local rsyslog to `/var/log/haproxy.log`

!!! Note
    The default HAProxy configuration file `haproxy.cfg` is located in `/etc/haproxy`

### Sample of Supported Raw Events

**TODO**: Add a directory with raw event samples for each integration.

## Step-by-Step Configuration Procedure

### Instructions on HAProxy

After configuring HAProxy, logs must be sent to a syslog concentrator and then forwarded to Sekoia.io.

**Default rsyslog Configuration at Installation**:
```plaintext
$AddUnixListenSocket /var/lib/haproxy/dev/log

:programname, startswith, "haproxy" {
    /var/log/haproxy.log
    stop
}
