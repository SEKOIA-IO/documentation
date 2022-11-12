uuid: d719e8b5-85a1-4dad-bf71-46155af56570
name: WatchGuard Firebox
type: intake

## Overview

WatchGuard Firebox is a serie of high-performance firewalls to protect computer networks.
Sending WatchGuard Firebox logs to SEKOIA.IO enables the discovering of potential network security threats. Spotted threats are contextualized by means of  SEKOIA.IO's Cyber Threat Intelligence (CTI).

{!_shared_content/operations_center/detection/generated/suggested_rules_d719e8b5-85a1-4dad-bf71-46155af56570_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/watchguard-firebox_do_not_edit_manually.md!}


## Configure

### Prerequisites

An internal log concentrator (Rsyslog) is required to collect and forward events to SEKOIA.IO.

### Enable Syslog forwarding

Log on your Firebox appliance and follow [this guide](https://www.watchguard.com/help/docs/help-center/en-US/Content/Integration-Guides/General/ubuntu_rsyslog.html) to enable syslog forwarding

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format WatchGuard Firebox.

## Transport to SEKOIA.IO

Please consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

## Further Readings
- [Watchguard Firebox Rsyslog Integration Overview](https://www.watchguard.com/help/docs/help-center/en-US/Content/Integration-Guides/General/ubuntu_rsyslog.html)
