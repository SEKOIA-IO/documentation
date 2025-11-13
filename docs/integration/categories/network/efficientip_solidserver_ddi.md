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

- 8.4.x

## Supported events

This integration supports the following events:

- DNS logs from named

## Configure

In this guide, you will configure the gateway to forward events to syslog.

### Prerequisites

An internal syslog concentrator is required to collect and forward events to Sekoia.io.


### Enable Syslog forwarding

1. Log in SOLIDServer console
2. On the left panel, click `Administration`

    ![Adminstation](/assets/integration/network/efficientip_solidserver/01 - administration.png)

3. In the `monitoring` section, click `Configuration`

    ![Configuration](/assets/integration/network/efficientip_solidserver/02 - configuration.png)

4. In the menu, click `+ Add`

    ![syslog](/assets/integration/network/efficientip_solidserver/03 - syslog.png)

5. In the `Services` drop-dwon, select the following services:
	- `named`

6. In the `Target server`, fill the ip address and the port of the log concentrator.

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
