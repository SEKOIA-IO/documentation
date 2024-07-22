uuid: a2915a14-d1e9-4397-86fc-8f8b2c617466
name: Olfeo Secure Web Gateway
type: intake

## Overview
- **Vendor**:
- **Plan**:
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:

Olfeo Secure Web Gateway is a suite of cybersecurity features for analyzing, filtering and securing your web flows. Combining proxy filtering, flow antivirus and DNS filtering.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.




## Configure

This setup guide will show you how to forward your Olfeo Secure Web Gateway logs
to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Have an internal log concentrator

### Versions supported

Olfeo Secure Web Gateway On premise v6.8.6 and above

### Enable Syslog forwarding

To enable syslog forwarding:

1. Log in your Olfeo web interface.
2. Go to `Parameters > Monitoring > Syslog.`.
3. Click on `add a syslog` button.
4. Add `label, description and server adress`.
5. Click on `Create`.

Olfeo forward syslogs in UDP on port 514. You must setup your internal log concentrator to listen on this port and forward logs to Sekoia.io.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Olfeo Secure Web Gateway`.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
{!_shared_content/operations_center/integrations/generated/a2915a14-d1e9-4397-86fc-8f8b2c617466_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a2915a14-d1e9-4397-86fc-8f8b2c617466_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/a2915a14-d1e9-4397-86fc-8f8b2c617466.md!}

