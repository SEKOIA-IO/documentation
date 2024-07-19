uuid: ee0b3023-524c-40f6-baf5-b69c7b679887
name: SonicWall Firewall
type: intake

## Overview
  - **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**: Telemetry
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:

SonicWall firewalls enable you to identify and control all applications that are running on your network. By identifying applications based on their unique signatures rather than ports or protocols, this additional control improves compliance and data leakage prevention.



## Configure

This setup guide will show you how to forward your SonicWall logs
to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Must have GMS server or On-Prem Analytics server installed and configured.
- Have an Address Object Created on the Firewall for SonicWall Analytics system.
- Have an internal log concentrator (Rsyslog)

### Enable Syslog forwarding for SonicWall 6.5 and 7.X


!!! info
    Only the Syslog format `ArcSight` is supported by this integration.

Log on your SonicWall appliance and follow this [guide](https://www.sonicwall.com/support/knowledge-base/how-can-i-configure-a-syslog-server-on-a-sonicwall-firewall/170505984096810/) to enable syslog forwarding,
except for the step 4 : Select Syslog Format as 'Enhanced', you must select Syslog format 'ArcSight' instead. 


### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format SonicWall Firewall.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_ee0b3023-524c-40f6-baf5-b69c7b679887_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/ee0b3023-524c-40f6-baf5-b69c7b679887.md!}

