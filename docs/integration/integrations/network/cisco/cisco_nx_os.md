uuid: 591feb54-1d1f-4453-b780-b225c59e9f99
name: Cisco NX-OS
type: intake

## Overview

Cisco NX-OS is a network operating system for Cisco Nexus-series switches.

{!_shared_content/operations_center/detection/generated/suggested_rules_591feb54-1d1f-4453-b780-b225c59e9f99_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/591feb54-1d1f-4453-b780-b225c59e9f99.md!}

## Configure

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

Log on your Cisco appliance and follow [this guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/6-x/system_management/configuration/guide/b_Cisco_Nexus_9000_Series_NX-OS_System_Management_Configuration_Guide/sm_5syslog.html#task_5793349949823830091) to enable syslog forwarding.


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cisco NX-OS.

## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

## Further Readings
- [Cisco Nexus 9000 Series Documentation](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/6-x/system_management/configuration/guide/b_Cisco_Nexus_9000_Series_NX-OS_System_Management_Configuration_Guide.html)
