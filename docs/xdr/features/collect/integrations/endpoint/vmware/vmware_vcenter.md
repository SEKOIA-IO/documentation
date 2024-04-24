uuid: 0642b03a-9d4a-4c88-a5e2-4597e366b8c4
name: VMWare VCenter
type: intake

## Overview

VMWare VCenter is a centralized management software. It provides a single point of control for managing virtual machines and ESXi hosts from a centralized interface.

{!_shared_content/operations_center/detection/generated/suggested_rules_0642b03a-9d4a-4c88-a5e2-4597e366b8c4_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/0642b03a-9d4a-4c88-a5e2-4597e366b8c4.md!}

## Configure

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

Follow [this guide](https://kb.vmware.com/s/article/2003322) to enable the log forwarding to the log concentrator.

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `VMWare VCenter`.

## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
