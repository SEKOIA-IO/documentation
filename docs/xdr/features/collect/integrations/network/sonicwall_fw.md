uuid: ee0b3023-524c-40f6-baf5-b69c7b679887
name: SonicWall Firewall
type: intake

## Overview

SonicWall firewalls enable you to identify and control all applications that are running on your network. By identifying applications based on their unique signatures rather than ports or protocols, this additional control improves compliance and data leakage prevention.

!!! warning
    This format is still in beta, please use it wisely.

{!_shared_content/operations_center/detection/generated/attack_ee0b3023-524c-40f6-baf5-b69c7b679887_do_not_edit_manually.json!}

{!_shared_content/operations_center/integrations/generated/sonicwall-fw_do_not_edit_manually.md!}

## Configure

This setup guide will show you how to forward your SonicWall logs
to SEKOIA.IO by means of an Rsyslog transport channel.

### Prerequisites

- Must have GMS server or On-Prem Analytics server installed and configured.
- Have an Address Object Created on the Firewall for SonicWall Analytics system.
- Have an internal log concentrator (Rsyslog)

### Enable Syslog forwarding for SonicWall 6.5 and 7.X

Log on your SonicWall appliance and follow this [guide](https://www.sonicwall.com/support/knowledge-base/how-can-i-configure-a-syslog-server-on-a-sonicwall-firewall/170505984096810/) to enable syslog forwarding.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format SonicWall Firewall.

### Transport to SEKOIA.IO

Please consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
