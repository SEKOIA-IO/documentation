uuid: 700f332f-d515-4bc5-8a62-49fa5f2c9206
name: Cisco IOS
type: intake


## Overview

Cisco IOS is a network operating system for Cisco ASR routers and Cisco Catalyst switches.

{!_shared_content/operations_center/detection/generated/suggested_rules_700f332f-d515-4bc5-8a62-49fa5f2c9206_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/700f332f-d515-4bc5-8a62-49fa5f2c9206.md!}

## Configure

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

Log on your Cisco appliance and follow [this guide](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html#wp1055038) to enable syslog forwarding.


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cisco IOS.

## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

## Further Readings
- [Cisco System Message Logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html)
