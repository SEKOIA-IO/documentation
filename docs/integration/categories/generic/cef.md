uuid: 1d172ee6-cdc0-4713-9cfd-43f7d9595777
name: CEF
type: intake

## Overview
ArcSight's Common Event Format (CEF) is an open log management standard. If one of your applications or devices is not covered by one of the other intakes we support but can produce logs in CEF you can use this intake. Still we recommend using an intake tailored to your specific application or device, even with CEF, in order to ensure you get the most out of your logs. If an intake is missing, please make a formal Integration request to your usual points of contact.

- **Plan**: Defend Core
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: File monitoring, Network device logs, Process monitoring, Process use of network, Web logs, Web proxy	

## Configure

As of now, the main solution to collect CEF logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

Please refer to the documentation of your vendor to forward events to your rsyslog server. The reader is also invited to consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/1d172ee6-cdc0-4713-9cfd-43f7d9595777_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_1d172ee6-cdc0-4713-9cfd-43f7d9595777_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/1d172ee6-cdc0-4713-9cfd-43f7d9595777.md!}

## Further Reading
- [CEF specification](https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors/pdfdoc/common-event-format-v25/common-event-format-v25.pdf)
