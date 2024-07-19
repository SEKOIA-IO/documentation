uuid: 6dbdd199-77ae-4705-a5de-5c2722fa020e
name: Ubika WAAP Gateway
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**:

Ubika WAAP Gateway detect and prevent threats against your web applications and your APIs.



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


### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_6dbdd199-77ae-4705-a5de-5c2722fa020e_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/6dbdd199-77ae-4705-a5de-5c2722fa020e.md!}

