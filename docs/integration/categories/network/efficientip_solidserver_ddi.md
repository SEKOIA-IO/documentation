uuid: f95fea50-533c-4897-9272-2f8361e63644
name: EfficientIP SOLIDServer DDI
type: intake

## Overview

EfficientIP SOLIDserver suite of appliances is designed to deliver highly scalable, secure and robust virtual and hardware appliances for critical IPAM-DNS-DHCP-NTP-TFTP services.

- **Vendor**: EfficientIP
- **Supported environment**: On prem
- **Version Compatibility**: 8.0
- **Detection based on**: Telemetry

## Supported versions

This integration supports the following versions:
- 8.3.x
- 8.4.x

## Supported events

This integration supports the following events:

- DNS logs from named

## Configure

In this guide, you will configure the gateway to forward events to syslog.

### Prerequisites

An internal syslog concentrator is required to collect and forward events to Sekoia.io.
The SOLIDserver syslog forwarding for this integration must use the UDP protocol.


### Enable Syslog forwarding

1. Log in to the SOLIDServer console
2. On the left panel, click `Administration`

    ![Adminstation](/assets/integration/network/efficientip_solidserver/01 - administration.png)

3. In the `monitoring` section, click `Configuration`

    ![Configuration](/assets/integration/network/efficientip_solidserver/02 - configuration.png)

4. In the menu, click `+ Add`

    ![syslog](/assets/integration/network/efficientip_solidserver/03 - syslog.png)

5. Select `dns` from the `Services` drop-down and `udp` as the transport protocol.

6. In the `Target server`, fill the address of the log concentrator and a dedicated listening port.

    You can configure the target with either:
    - a hostname (for example: `syslog.internal.example`)
    - an IPv4 address (for example: `192.0.2.10`)

    Set a specific port that matches the UDP listener configured on your concentrator (for example: `514` or `10514`).
    TCP is not supported for this integration path.

    ![target](/assets/integration/network/efficientip_solidserver/04 - target.png)

7. Click `OK`


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `EfficientIP SOLIDServer DDI`.


## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/f95fea50-533c-4897-9272-2f8361e63644_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_f95fea50-533c-4897-9272-2f8361e63644_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/f95fea50-533c-4897-9272-2f8361e63644.md!}
