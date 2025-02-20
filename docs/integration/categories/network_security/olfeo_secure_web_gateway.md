uuid: a2915a14-d1e9-4397-86fc-8f8b2c617466
name: Olfeo Secure Web Gateway
type: intake

## Overview

Olfeo Secure Web Gateway is a suite of cybersecurity features for analyzing, filtering and securing your web flows. Combining proxy filtering, flow antivirus and DNS filtering.

- **Vendor**: Olfeo
- **Supported environment**: On Premise
- **Version compatibility**: v6.8.6 and above
- **Detection based on**: Telemetry
- **Supported application or feature**: Network web traffic

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on Olfeo
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain text
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

This setup guide will show you how to forward your Olfeo Secure Web Gateway logs to Sekoia.io by means of a syslog transport channel.

### Instructions on the 3rd Party Solution

#### Enable Syslog forwarding

To enable syslog forwarding:

1. Log in your Olfeo web interface.
2. Go to `Parameters > Monitoring > Syslog.`.
3. Click on `add a syslog` button.
4. Add `label, description and server adress`.
5. Click on `Create`.

!!! Note
    Olfeo forward syslogs in UDP on port 514. You must setup your internal log concentrator to listen on this port and forward logs to Sekoia.io.

{!_shared_content/integration/forwarder_configuration.md!}

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/operations_center/integrations/generated/a2915a14-d1e9-4397-86fc-8f8b2c617466_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a2915a14-d1e9-4397-86fc-8f8b2c617466_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/a2915a14-d1e9-4397-86fc-8f8b2c617466.md!}
