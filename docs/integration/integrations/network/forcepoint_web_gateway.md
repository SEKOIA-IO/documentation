uuid: f0f95532-9928-4cde-a399-ddd992d48472
name: Forcepoint Secure Web Gateway
type: intake

## Overview
Forcepoint Secure Web Gateway (SWG) is a proxy, installed on the endpoint, applying routing policies and analyzing the traffic against threats.
This product is supported by Forcepoint LLC.

!!! note

    This integration was initially developed for the on premise product of Forcepoint Secure Web Gateway, specifically for version 8.5.

{!_shared_content/operations_center/detection/generated/suggested_rules_f0f95532-9928-4cde-a399-ddd992d48472_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/f0f95532-9928-4cde-a399-ddd992d48472.md!}

## Configure

In this guide, you will configure the gateway to forward events to syslog.

This procedure should be repeated for each Forcepoint Policy Server.

### Prerequisites

An internal syslog concentrator is required to collect and forward events to Sekoia.io. We highly recommand you to use the [Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder/).


### Enable SIEM Integration

Log on the Web Security module of the Forcepoint Security Manager and navigate to `Settings > General > SIEM Integration`.

In the `Internet Activity Log Data`, Click on the button `Add`.
Provide the IP address, the transport protocol (recommending `TCP`) and the listening port (`514`) of the concentrator.
Select the `syslog/CEF` as SIEM format. Click `OK` then `Save and Deploy` to enable the integration.

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Forcepoint Secure Web Gateway.


## Forward logs to Sekoia.io

Please consult the [Sekoia.io Forwarder](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
