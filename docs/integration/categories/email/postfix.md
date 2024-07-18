uuid: eb727929-6a06-4e68-a09d-cf0e5daf3ccd
name: Postfix
type: intake

## Overview
Postfix is a free and open-source mail transfer agent that routes and delivers electronic mail.

- **Vendor**: Postfix
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**: Email gateway, Mail server
- **Coverage Score**: 2

## Configure

As of now, the main solution to collect Postfix logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

Please refer to the documentation of Postfix to forward events to your rsyslog server. The reader can consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/eb727929-6a06-4e68-a09d-cf0e5daf3ccd_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_eb727929-6a06-4e68-a09d-cf0e5daf3ccd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/eb727929-6a06-4e68-a09d-cf0e5daf3ccd.md!}