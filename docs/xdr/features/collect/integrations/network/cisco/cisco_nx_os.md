uuid: 591feb54-1d1f-4453-b780-b225c59e9f99
name: Cisco NX-OS
type: intake

## Overview

Cisco NX-OS is a network operating system for Cisco Nexus-series switches.

!!! warning
    This format is still in beta, please use it wisely.

{!_shared_content/operations_center/detection/generated/suggested_rules_466aeca2-e112-4ccc-a109-c6d85b91bbcf_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/cisco-asa_do_not_edit_manually.md!}

## Configure

### Prerequisites

An internal log concentrator (Rsyslog) is required to collect and forward events to SEKOIA.IO.

### Enable Syslog forwarding

Log on your Cisco appliance and follow [this guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/6-x/system_management/configuration/guide/b_Cisco_Nexus_9000_Series_NX-OS_System_Management_Configuration_Guide/sm_5syslog.html#task_5793349949823830091) to enable syslog forwarding.


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cisco NX-OS.

## Transport to SEKOIA.IO

Please consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

## Further Readings
- [Cisco Nexus 9000 Series Documentation](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/6-x/system_management/configuration/guide/b_Cisco_Nexus_9000_Series_NX-OS_System_Management_Configuration_Guide.html)
