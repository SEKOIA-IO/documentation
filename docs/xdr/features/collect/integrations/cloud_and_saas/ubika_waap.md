uuid: 6dbdd199-77ae-4705-a5de-5c2722fa020e
name: Ubika WAAP Gateway
type: intake

## Overview

Ubika WAAP Gateway detect and prevent threats against your web applications and your APIs.

!!! warning
    This format is still in beta, please use it wisely.

{!_shared_content/operations_center/detection/generated/suggested_rules_6dbdd199-77ae-4705-a5de-5c2722fa020e_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/6dbdd199-77ae-4705-a5de-5c2722fa020e.md!}

## Configure

This setup guide will show you how to forward your Ubika WAAP Gateway logs
to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Have an internal log concentrator (Rsyslog)

### Enable syslog

1. Logging into the Management WAAP
2. Select the tab `Management`
3. On the left panel, click on the section `Alerting Destinations`
4. On the toolbar, click on the button `add` to add a new alerting destination.
5. In the modal, type a name for the destination and select `Syslog` as type.
6. Fill the host and the port with the ip address and the port of the log concentrator.
7. Select `No` for the option `Use TLS`
8. Save the destination by clicking `Ok`

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Ubika WAAP.


### Transport to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_docker_concentrator/) documentation to forward these logs to Sekoia.io.
