uuid: 3c7057d3-4689-4fae-8033-6f1f887a70f2
name: Harfanglab
type: intake

## Overview

HarfangLab is an Endpoint detection and response (EDR) solution certified by ANSSI since 2020.
This setup guide shows how to forward events produced by HarfangLab EDR to SEKOIA.IO.

{!_shared_content/operations_center/detection/generated/suggested_rules_3c7057d3-4689-4fae-8033-6f1f887a70f2_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/3c7057d3-4689-4fae-8033-6f1f887a70f2.md!}

## Configure

### Pre-requisite

HarfangLab must setup OpenSSL to the server for protocol `TCP/SSL` to be available.

### Steps

#### In SEKOIA.IO

Create a new HarfangLab intake on Sekoia.io.

#### In HarfangLab

1. Navigate to `Administration` > `Configuration`, and switch to the `Connectors` tab.

2. In the `Syslog connector` panel, select the logs you want to export:

   - Process
   - Network
   - Event log
   - Remote thread
   - InjectedThread
   - Security Event

3. Configure the Syslog information with the following details and by replacing `YOUR_INTAKE_KEY` with the Intake key previously generated in SEKOIA.IO:
   - Host: `intake.sekoia.io`
   - Port: `10514`
   - App name: name of your choice - **NO SPACES**
   - Source host: name of your choice **NO SPACES**
   - Structured data: `[SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"]` - please replace `YOUR_INTAKE_KEY` variable with your intake key generated in SEKOIA.IO.
   - Protocol: `TCP/SSL`
   - RFC : `RFC5424`

!!! warning
    Do not insert spaces in `App name` or `Source host`. These fields are part of the Syslog header and spaces will break the format.

4. Finally select the `Protocol` option: `TCP/SSL`, leave the other options to default.

![HarfangLab Configuration](/assets/operation_center/integration_catalog/endpoint/harfanglab/harfanglab_edr.png){: style="max-width:60%"}
