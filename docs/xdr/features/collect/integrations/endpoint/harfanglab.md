uuid: 3c7057d3-4689-4fae-8033-6f1f887a70f2
name: Harfanglab
type: intake

## Overview

HarfangLab is an Endpoint detection and response (EDR) solution certified by ANSSI since 2020.
This setup guide shows how to forward events produced by HarfangLab EDR to SEKOIA.IO.

{!_shared_content/operations_center/detection/generated/suggested_rules_3c7057d3-4689-4fae-8033-6f1f887a70f2_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/3c7057d3-4689-4fae-8033-6f1f887a70f2.md!}

## Configure


### On SEKOIA.IO

To create the intake key to be used when setting up HarfangLab, please select `manual` mode. 

### On Harfang Lab

First your need to navigate to `Personal Settings`,  and in the `Api token` get your token or generate a new one.

### Pre-requisite


HarfangLab must setup OpenSSL to the server for protocol `TCP/SSL` to be available.

### Steps

#### In SEKOIA.IO

Create a new HarfangLab intake on SEKOIA.IO and select the manual mode.
![Create HarfangLab Intake Key](/assets/operation_center/integration_catalog/endpoint/harfanglab/harfanglab_createintake.png){: style="max-width:60%"}


* Host: `intake.sekoia.io`
* Port: `10514`
* App name: in the syslog header (cf illustration below), please use [RFC5424 format](https://www.rfc-editor.org/rfc/rfc5424.html#page-14)
* Source host: name of your choice
* Structured data: `[SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"]`
* Protocol: `TCP/TLS`
* RFC: `RFC5424`

- **Syslog header and fields**
![AppName](https://user-images.githubusercontent.com/101662967/195819283-06e69207-a245-470d-83e5-c83687606719.png)



#### In HarfangLab

1. Go to `Personal Settings` > `API Key` and get your token or generate a new one.

2. Navigate to `Administration` > `Configuration`, and switch to the `Connectors` tab.

3. In the `Syslog connector` panel, select the logs you want to export:

    * Process
    * Network
    * Event log
    * Remote thread
    * InjectedThread
    * Security Event

4. Configure the Syslog information with the following details and by replacing `YOUR_INTAKE_KEY` with the Intake key previously generated in SEKOIA.IO:

    * Host: `intake.sekoia.io`
    * Port: `10514`
    * App name: name of your choice - **NO SPACES**
    * Source host: name of your choice **NO SPACES**
    * Structured data: `[SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"]`
    * Protocol: `TCP/SSL`
    * RFC : `RFC5424`

    !!! WARNING
        Don't insert spaces in `App name` or `Source host`. These fields are part of the Syslog header and spaces will break the format.

5. Finally select the `Protocol` option: `TCP/SSL`, leave the other options to default.


In the above field `Structured data`, please replace `YOUR_INTAKE_KEY` variable with your intake key generated in SEKOIA.IO.
