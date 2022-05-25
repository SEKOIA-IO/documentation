uuid: f0f95532-9928-4cde-a399-ddd992d48472
name: Forcepoint Secure Web Gateway
type: intake

## Overview
Forcepoint Secure Web Gateway (SWG) is a proxy, installed on the endpoint, applying routing policies and analyzing the traffic against threats.
This product is supported by Forcepoint LLC.

{!xdr/features/collect/integrations/generated/forcepoint-swg_do_not_edit_manually.md!}

## Configure

In this guide, you will configure the gateway to forward events to syslog.

This procedure should be repeated for each Forcepoint Policy Server.

### Prerequisites

An internal log concentrator (Rsyslog) is required to collect and forward events to SEKOIA.IO.

### Enable SIEM Integration

Log on the Web Security module of the Forcepoint Security Manager and navigate to `Settings > General > SIEM Integration`.

In the `Internet Activity Log Data`, Click on the button `Add`.
Provide the IP address, the transport protocol (recommending `TCP`) and the listening port (`514`) of the concentrator.
Select the `syslog/CEF` as SIEM format. Click `OK` then `Save and Deploy` to enable the integration.

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Forcepoint Secure Web Gateway.


## Transport to SEKOIA.IO

Please consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
