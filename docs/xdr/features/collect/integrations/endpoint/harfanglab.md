uuid: 3c7057d3-4689-4fae-8033-6f1f887a70f2
name: Harfanglab
type: intake

## Overview

HarfangLab is an Endpoint detection and response (EDR) solution certified by ANSSI since 2020.
This setup guide shows how to forward events produced by HarfangLab EDR to SEKOIA.IO.

{!xdr/features/collect/integrations/generated/harfanglab_do_not_edit_manually.md!}

## Configure

First your need to navigate to `Personal Settings`,  and in the `Api token` get your token or generate a new one.

Then you need to navigate to `Administration > Configuration`, and switch to the `Connectors` tab.

In the `Syslog connector` panel, select the logs you want to export:

* Process
* Network
* Event log
* Remote thread
* InjectedThread
* Security Event

Configure the syslog information with the following details:

* Host: `intake.sekoia.io`
* Port: `10514`
* App name: name of your choice
* Source host: name of your choice
* Structured data: `[SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"]`
* Protocol: `TCP/SSL`

In the above field `Structured data`, please replace `YOUR_INTAKE_KEY` variable with your intake key generated in SEKOIA.IO.

Finaly select the `Protocol` option: `TCP/SSL`, leave the other options to default.

![HarfangLab EDR](/assets/operation_center/integration_catalog/endpoint/harfanglab/harfanglab_edr.png){: style="max-width:60%"}
