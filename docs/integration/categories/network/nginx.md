uuid: ab25af2e-4916-40ba-955c-34d2301c1f51
name: NGINX
type: intake

## Overview

NGINX is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server. It has a lot of features and because it is located between your application and your clients, it can give you a lot of information about either of them.

- **Vendor**: F5
- **Plan**: Defend Core / Defend Prime
- **Supported environment**: On Premise / Cloud
- **Version compatibility, if applicable**:
- **Detection based on**: Network Telemetry
- **Supported application or feature**: HTTP Proxy, Reverse Proxy
- **Coverage Score**: 2

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![nginx_architecture](/assets/integration/nginx_architecture.png)

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
    - Administrator or Root access to the NGINX server
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON, key-value
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward NGINX Logs to Sekoia.io

This setup guide will show you how to forward your NGINX logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

There are two methods to collect NGINX Logs:

1. **Local Rsyslog Method:**
    - The following snippet is an illustration of rsyslog configuration to monitor nginx's `error.log` and `access.log` files.

      ```bash
      # error log
      $InputFileName /var/log/nginx/error.log
      $InputFileTag nginx:
      $InputFileStateFile stat-nginx-error
      $InputFileSeverity error
      $InputFileFacility local5
      $InputFilePollInterval 1
      $InputRunFileMonitor

      # access log
      $InputFileName /var/log/nginx/access.log
      $InputFileTag nginx:
      $InputFileStateFile stat-nginx-access
      $InputFileSeverity notice
      $InputFileFacility local5
      $InputFilePollInterval 1
      $InputRunFileMonitor
      ```

    - The reader can consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io.

2. **Configuring NGINX to Forward Logs Using Syslog and the UDP Protocol:**
    - This method is simpler as you don't need to set up Rsyslog to forward logs.
    - To configure NGINX to forward logs to an IP with syslog and the UDP protocol, please add these lines in `/etc/nginx/nginx.conf`:

      ```
      access_log syslog:server=127.0.0.1:20517,tag=nginx;
      error_log syslog:server=127.0.0.1:20517,tag=nginx;
      ```

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

{!_shared_content/operations_center/integrations/generated/ab25af2e-4916-40ba-955c-34d2301c1f51.md!}

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_ab25af2e-4916-40ba-955c-34d2301c1f51_do_not_edit_manually.md!}

## Further readings

- [Nginx Wiki](https://www.nginx.com/resources/wiki/start/)
- [Rsyslog IMFile module](https://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html)