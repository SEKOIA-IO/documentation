uuid: 3c7057d3-4689-4fae-8033-6f1f887a70f2
name: Harfanglab
type: intake

## Overview

HarfangLab is an Endpoint detection and response (EDR) solution certified by ANSSI since 2020.
This setup guide shows how to forward events produced by HarfangLab EDR to Sekoia.io.

- **Vendor**: Harfanglab
- **Plan**: Defend Prime
- **Supported environment**: On Cloud / On Premise
- **Version compatibility**:
- **Detection based on**: Telemetry / Alert
- **Supported application or feature**: Authentication, Driver, Network, Process, Web
- **Coverage Score**: 4


## Configure

### Pre-requisite

HarfangLab must setup OpenSSL to the server for protocol `TCP/SSL` to be available.

### Steps

#### In Sekoia.io

Create a new HarfangLab intake on Sekoia.io.

#### In HarfangLab

1. Navigate to `Administration` > `Configuration`, and switch to the `Connectors` tab.

2. In the `Syslog connector` panel, select the logs you want to export:
![HarfangLab Log categories](/assets/operation_center/integration_catalog/endpoint/harfanglab/harfanglab-log-categories.png)

3. Configure the Syslog information with the following details and by replacing `YOUR_INTAKE_KEY` with the Intake key previously generated in Sekoia.io:
    - Host: `intake.sekoia.io`
    - Port: `10514`
    - App name: name of your choice - **NO SPACES**
    - Source host: name of your choice **NO SPACES**
    - Structured data: `[SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"]` - please replace `YOUR_INTAKE_KEY` variable with your intake key generated in Sekoia.io.
    - Protocol: `TCP/SSL`
    - RFC : `RFC5424`

4. Finally select the `Protocol` option: `TCP/SSL`, leave the other options to default.

!!! warning
    Do not insert spaces in `App name` or `Source host`. These fields are part of the Syslog header and spaces will break the format.

![HarfangLab Configuration](/assets/operation_center/integration_catalog/endpoint/harfanglab/harfanglab_edr.png){: style="max-width:60%"}

{!_shared_content/operations_center/integrations/generated/3c7057d3-4689-4fae-8033-6f1f887a70f2_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_3c7057d3-4689-4fae-8033-6f1f887a70f2_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/3c7057d3-4689-4fae-8033-6f1f887a70f2.md!}
