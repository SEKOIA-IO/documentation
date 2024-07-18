uuid: 59991ced-c2a0-4fb0-91f3-49e3993c16f5
name: Tanium
type: intake

## Overview
Tanium solutions manage and protect networks and endpoints.

- **Vendor**: Tanium
- **Plan**: Defend Prime
- **Supported environment**: On Cloud / On Premise
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**: File, Network, Process, Registry
- **Coverage Score**: 4

## Configure
Tanium logs can be collected under the rsyslog format and then forward to Sekoia.io. Refer to the official documentation of Tanium to forward your logs under rsyslog format and consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/59991ced-c2a0-4fb0-91f3-49e3993c16f5_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_59991ced-c2a0-4fb0-91f3-49e3993c16f5_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/59991ced-c2a0-4fb0-91f3-49e3993c16f5.md!}
