uuid: f95fea50-533c-4897-9272-2f8361e63644
name: EfficientIP SOLIDServer DDI
type: intake

## Overview

EfficientIP SOLIDserver suite of appliances is designed to deliver highly scalable, secure and robust virtual and hardware appliances for critical IPAM-DNS-DHCP-NTP-TFTP services.

{!_shared_content/operations_center/detection/generated/suggested_rules_f95fea50-533c-4897-9272-2f8361e63644_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/f95fea50-533c-4897-9272-2f8361e63644.md!}

## Configure

In this guide, you will configure the gateway to forward events to syslog.

### Prerequisites

An internal syslog concentrator is required to collect and forward events to Sekoia.io.


### Enable Syslog forwarding

1. Log in SOLIDServer console
2. On the left panel, click `Admin Home`
3. In the `monitoring` section, click `Configuration of network logs`
4. In the menu, click `+ Add`
5. In the `Services` drop-dwon, select the following services:
   - `named`
   - `ipmserver`
   - `dhcp`
6. In the `Target server`, fill the ip address and the port of the log concentrator.
7. Click `OK`


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `EfficientIP SOLIDServer DDI`.


## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
