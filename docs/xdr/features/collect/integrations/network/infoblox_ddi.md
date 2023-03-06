uuid: 864ade96-a96d-4a0e-ab3d-b7cb7b7db618
name: Infoblox DDI
type: intake

## Overview

Infoblox DNS, DHCP and IP address management (DDI) enables customer to control and automate their network. It performs both of the main DNS server roles, acting as an authoritative name server for domains, and acting as a recursive resolver in the network.


{!_shared_content/operations_center/detection/generated/suggested_rules_864ade96-a96d-4a0e-ab3d-b7cb7b7db618_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/864ade96-a96d-4a0e-ab3d-b7cb7b7db618.md!}

## Configure

In this guide, you will configure the gateway to forward events to syslog.

### Prerequisites

An internal log concentrator (Rsyslog) is required to collect and forward events to SEKOIA.IO.

### Enable Syslog forwarding

Log on your NIOS appliance and follow [this guide](https://docs.infoblox.com/space/NAG8/22252249/Using+a+Syslog+Server) to enable syslog forwarding

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Infoblox DDI.


## Transport to SEKOIA.IO

Please consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
