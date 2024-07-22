uuid: 8510051d-c7cf-4b0c-a398-031afe91faa0
name: OPNSense
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:

OPNSense is a firewall software distribution based on FreeBSD.

This intake ingest filterlog from OPNSense.



## Configure

This setup guide will show you how to forward your Firewall logs
to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Have an internal log concentrator

### Enable Syslog forwarding

To enable syslog forwarding:

1. Log in your OPNSense web interface.
2. Go to `System > Settings > Logging / targets`.
3. In the `Destinations` tab, click on the `+` button to add a new destination.
4. In the modal, check the `Enabled` checkbox.
5. Select `UDP(4)` as the transport.
6. Select `filter (filterlog)` as `Applications`.
7. Set the hostname/ip and the port of the log concentrator.
8. Click on the `RFC5424` checkbox
9. Click the `Save` button


### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `OpenBSD Packet Filter`.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.






{!_shared_content/operations_center/integrations/generated/8510051d-c7cf-4b0c-a398-031afe91faa0_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_8510051d-c7cf-4b0c-a398-031afe91faa0_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/8510051d-c7cf-4b0c-a398-031afe91faa0.md!}

