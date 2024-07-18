uuid: ab25af2e-4916-40ba-955c-34d2301c1f51
name: NGINX
type: intake

## Overview

NGINX is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server. It has a lot of features and because it is located between your application and your clients, it can give you a lot of information about either of them.

- **Vendor**: F5
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Network Telemetry
- **Supported application or feature**: Access and Error logs
- **Coverage Score**: 2

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![nginx_architecture](/assets/integration/nginx_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the NGINX server
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain Text
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:
    - Access: `/var/log/nginx/access.log`
    - Error: `/var/log/nginx/error.log`

## Step-by-Step Configuration Procedure

This setup guide will show you how to forward your NGINX logs to Sekoia.io by means of a syslog transport channel.

### Instructions on the 3rd Party Solution

#### Forward NGINX Logs to a syslog forwarder

To configure NGINX to forward logs to an IP with syslog and the UDP protocol, please add these lines in `/etc/nginx/nginx.conf`:

```
access_log syslog:server=REMOTE_SERVER_IP:LISTENING_PORT_UDP,tag=nginx;
error_log syslog:server=REMOTE_SERVER_IP:LISTENING_PORT_UDP,tag=nginx;
```

!!! Note
    Please replace `REMOTE_SERVER_IP` by you syslog forwarder IP and `LISTENING_PORT_UDP` by the relevant value.


### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/ab25af2e-4916-40ba-955c-34d2301c1f51_sample.md!}

## Detection section


The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_ab25af2e-4916-40ba-955c-34d2301c1f51_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/ab25af2e-4916-40ba-955c-34d2301c1f51.md!}

## Further readings

- [Nginx Wiki](https://www.nginx.com/resources/wiki/start/)
- [Rsyslog IMFile module](https://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html)