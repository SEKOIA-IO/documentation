uuid: bf8867ee-43b7-444c-9475-a7f43754ab6d
name: Vectra Cognito Detect
type: intake

## Overview
Vectra provides AI-powered incident detection and resolution support for native and hybrid clouds.


- **Vendor**:
- **Plan**: Defend Core & Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Authentication logs


## Configure
This setup guide will show you how to forward logs produced by your Vectra Appliance server to Sekoia.io by means of an rsyslog transport channel.

### Configure the Rsyslog server
Please consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/bf8867ee-43b7-444c-9475-a7f43754ab6d_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_bf8867ee-43b7-444c-9475-a7f43754ab6d_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/bf8867ee-43b7-444c-9475-a7f43754ab6d.md!}

