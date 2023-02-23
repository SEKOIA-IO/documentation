uuid: 995d7daf-4e4a-42ec-b90d-9af2f7be7019
name: Cisco Meraki MX
type: intake

## Overview

Cisco Meraki MX is a multifunctional security and SD-WAN enterprise appliance with a wide set of capabilities.

!!! warning
    This format is still in beta, please use it wisely.

{!_shared_content/operations_center/detection/generated/suggested_rules_995d7daf-4e4a-42ec-b90d-9af2f7be7019_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/cisco-meraki-mx_do_not_edit_manually.md!}

## Configure

### Prerequisites

An internal log concentrator (Rsyslog) is required to collect and forward events to SEKOIA.IO.

### Enable Syslog forwarding

Log on your Cisco Meraki MX appliance and follow [this guide](https://documentation.meraki.com/General_Administration/Monitoring_and_Reporting/Syslog_Server_Overview_and_Configuration#Configure_Dashboard) to enable syslog forwarding.


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cisco Meraki MX.

## Transport to SEKOIA.IO

Please consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

## Further Readings
- [Cisco Meraki MX documentation](https://documentation.meraki.com/MX)
