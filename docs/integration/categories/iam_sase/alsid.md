uuid: 44d41a2b-96cb-4d37-84e0-4f0c0f9138b8
name: Alsid
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**:
Alsid is an automated security solution that monitors the components of Active Directory infrastructures by detecting attacks in real time, identifying existing weaknesses and vulnerabilities.




## Configure

As of now, the main solution to collect Alsid logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

Please refer to the documentation of Alsid to forward events to your rsyslog server. The reader is also invited to consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/44d41a2b-96cb-4d37-84e0-4f0c0f9138b8_sample.md!}


## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_44d41a2b-96cb-4d37-84e0-4f0c0f9138b8_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/44d41a2b-96cb-4d37-84e0-4f0c0f9138b8.md!}

