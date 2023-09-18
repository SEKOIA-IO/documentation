uuid: 02a74ceb-a9b0-467c-97d1-588319e39d71
name: Citrix ADC
type: intake

## Overview

Citrix ADC (formely Citrix NetScaler) is a delivery controller and load-balancing tool that offers enhanced security and application performance.

!!! warning
    This format is in beta.

{!_shared_content/operations_center/detection/generated/suggested_rules_02a74ceb-a9b0-467c-97d1-588319e39d71_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/02a74ceb-a9b0-467c-97d1-588319e39d71.md!}

## Configure

### Prerequisites

- Have an internal log concentrator
- Have a NSLog server with the syslog protocol
- Have an auditing module which runs on the NetScaler appliance.

### Enable syslog

follow this [guide](https://docs.netscaler.com/en-us/citrix-adc/current-release/system/audit-logging/configuring-audit-logging.html) to enable syslog forwarding.

**IMPORTANT:** please make sure `-dateFormat MMDDYYYY` is set and date is present in logs

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Citrix ADC.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
