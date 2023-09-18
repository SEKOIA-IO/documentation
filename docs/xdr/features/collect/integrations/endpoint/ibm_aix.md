uuid: e8cb3372-41c8-409f-8e0e-ca4e6cecf7e6
name: IBM AIX 
type: intake

## Overview

AIX (Advanced Interactive eXecutive), is a series of proprietary Unix operating systems developed and sold by IBM for several of its computer platforms.
{!_shared_content/operations_center/detection/generated/suggested_rules_e8cb3372-41c8-409f-8e0e-ca4e6cecf7e6_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/e8cb3372-41c8-409f-8e0e-ca4e6cecf7e6.md!}

## Configure

In this guide, you will configure the gateway to forward events to syslog.

### Prerequisites

An internal syslog concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

Follow [this guide](https://www.ibm.com/docs/en/dsm?topic=aado-configuring-aix-audit-dsm-send-syslog-events-qradar) to enable syslog forwarding for audit events

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format IBM AIX.


## Send logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
