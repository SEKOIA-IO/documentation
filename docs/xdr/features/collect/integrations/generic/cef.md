uuid: 1d172ee6-cdc0-4713-9cfd-43f7d9595777
name: CEF
type: intake

## Overview
ArcSight's Common Event Format (CEF) is an open log management standard.
If one of your applications or devices is not covered by one of the other intakes we support but can produce logs in CEF you can use this intake.

Still we recommend using an intake tailored to your specific application or device, even with CEF, in order to ensure you get the most out of your logs. If an intake is missing, please [contact us](mailto:support@sekoia.io).

{!xdr/features/collect/integrations/generated/cef_do_not_edit_manually.md!}

## Configure

As of now, the main solution to collect CEF logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

Please refer to the documentation of your vendor to forward events to your rsyslog server. The reader is also invited to consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.


## Further Reading
- [CEF specification](https://community.microfocus.com/dcvta86296/attachments/dcvta86296/connector-documentation/1197/2/CommonEventFormatV25.pdf)
