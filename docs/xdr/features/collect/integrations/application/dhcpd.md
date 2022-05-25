uuid: 9044ba46-2b5d-4ebd-878a-51d62e84c8df
name: ISC DHCP
type: intake

## Overview
ISC DHCP offers a complete open source solution for implementing DHCP servers.

{!xdr/features/collect/integrations/generated/dhcpd_do_not_edit_manually.md!}

## Configure

As of now, the main solution to collect ISC DHCP logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

Please refer to the documentation of ISC DHPD to forward events to your rsyslog server. The reader can consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
