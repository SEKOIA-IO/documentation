uuid: bf8867ee-43b7-444c-9475-a7f43754ab6d
name: Vectra Cognito Detect
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:
Vectra provides AI-powered incident detection and resolution support for native and hybrid clouds.




## Configure
This setup guide will show you how to forward logs produced by your Vectra Appliance server to Sekoia.io by means of an rsyslog transport channel.

### Configure the Rsyslog server
Please consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/bf8867ee-43b7-444c-9475-a7f43754ab6d_sample.md!}


## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_bf8867ee-43b7-444c-9475-a7f43754ab6d_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/bf8867ee-43b7-444c-9475-a7f43754ab6d.md!}

