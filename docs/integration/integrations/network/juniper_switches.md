uuid: b1545bb3-6f55-4ba4-ac80-d649040a127c
name: Juniper Network Switches
type: intake

## Overview

Juniper Networks' JunOS is an advanced operating system powering Juniper's networking devices, renowned for its reliability, performance, and comprehensive feature set for routing, switching, and security functionalities in enterprise networks.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Supported versions

This integration supports the following versions:

- 23.2

## Supported events

This integration supports the following events:

- Firewall events

{!_shared_content/operations_center/detection/generated/suggested_rules_b1545bb3-6f55-4ba4-ac80-d649040a127c_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/b1545bb3-6f55-4ba4-ac80-d649040a127c.md!}

## Configure
This setup guide will show you how to forward your Juniper Switches logs to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Have an internal log concentrator

### Enable Syslog forwarding
1. Log into the firewall console
2. Configure the log forwarding to the log concentrator
```shell
root@:~ #cli

root> configure

[edit]
root# set system syslog host <ip of the log concentrator> firewall any

[edit]
root# set system syslog host <ip of the log concentrator> port <port of the log concentrator>

[edit]
root# commit
```

3. Configure a firewall filters to log events (see [Juniper documentation](https://www.juniper.net/documentation/us/en/software/junos/routing-policy/topics/example/firewall-filter-option-logging-example.html#configuration1385__d58769e137) for more details)
```shell
user@:~ #cli

user> configure

[edit]
user# edit firewall family <family> filter <filter_name>

[edit firewall family <family> filter <filter_name>]
user# set term <term_name> then syslog

[edit firewall family <family> filter <filter_name>]
user# commit
```

4. Apply the filter to a logical interface (see [Juniper documentation](https://www.juniper.net/documentation/us/en/software/junos/routing-policy/topics/example/firewall-filter-option-logging-example.html#configuration1385__d58769e196) for more details)
```shell
user@:~ #cli

user> configure

[edit]
user# edit interfaces <interface_name> unit 0 family <family>

[edit interfaces <interface_name> unit 0 family <family>]
user# set filter input <filter_name>

[edit interfaces <interface_name> unit 0 family <family>]
user# commit
```
5. Exit the console

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Juniper Switches.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
