uuid: 3c7057d3-4689-4fae-8033-6f1f887a70f2
name: harfanglab

## Overview

HarfangLab is an Endpoint detection and response (EDR) solution certified by ANSSI since 2020. 

This setup guide will show you how to forward events produced by HarfangLab EDR to SEKOIA.IO.

Theses changes have to be made from your HarfangLab instance web portal.

## HarfangLab EDR logs

You first need to navigate to `Administration > Configuration`, then switch to the `Connectors` tab.

In the `Syslog connector` panel, select the logs you want to export:

* Process
* Network
* Event log
* Remote thread
* InjectedThread
* Security Event

Then configure the syslog information with the following information:

* Host: `intake.sekoia.io`
* Port: `10514`
* App name: name of your choice
* Source host: name of your choice
* Structured data: `[SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"]`
* Protocol: `TCP/SSL`

In the above field `Structured data`, please replace `YOUR_INTAKE_KEY` variable with your intake key.

Finaly select the `Protocol` option: `TCP/SSL`, leave the other options to default.

![HarfangLab EDR](../assets/harfanglab_edr.png){: style="max-width:60%"}


## Enjoy your events

Once the configuration has been done on Sekoia side, you can go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.
