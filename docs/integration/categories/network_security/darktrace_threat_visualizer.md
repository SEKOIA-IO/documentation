---
uuid: 98fa7079-41ae-4033-a93f-bbd70d114188
title: Darktrace Threat Visualizer
name: Darktrace Threat Visualizer
type: intake
---

## Overview

Darktrace monitors all people and digital assets across your entire ecosystem.

- **Vendor**: Darktrace
- **Supported environment**: Cloud and On Premise versions 6.1 or above
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**: Darktrace Threat Visualizer


## Specification

### Prerequisites

For On Premise version:
- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator privileges on the Darktrace appliance
    - Root access to the Linux server with the syslog forwarder

For Cloud version, only an dministrator privileges on the Darktrace appliance is mandatory.

### Transport Protocol/Method

- **Direct HTTP** for Cloud
- **Indirect syslog** for On Premise

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Informational, Alert

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

This setup guide describes how to forward logs from Darktrace Threat visualizer to Sekoia.io.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

#### For Cloud verion only

{!_shared_content/integration/connector_configuration.md!}

### Instructions on the 3rd party solution
#### For Cloud verion - Acquire your public and private key

As a prerequisite, you need a Darktrace Threat Visualizer API tenant url.

See the [Darktrace documentation](https://customerportal.darktrace.com/product-guides/main/api-tokens) for intructions to acquire your public and private key.

#### For On Premise verion - Send logs to a syslog server

1. Open the Threat Visualizer and navigate to the **System Config** page (Main menu › Admin).
2. From the left-side menu, **select Modules**, then navigate to the **Workflow Integrations** section and choose
**Syslog**.
A window with four tabs will open, a Status tab that lists existing configurations per-Syslog server and an individual tab for each Syslog format. The Status tab may not be present if there are no existing configurations.
- If the instance is not a Unified View, proceed to Step 3.
- If the instance where configuration is being performed is a Darktrace Unified View instance, choose which Darktrace master instance will send alerts at the top of the page.
- If a a subordinate master (submaster) is selected, the master will be the instance to emit alerts but will only generate alerts originating from itself.
- If the UV instance is selected, an additional field - Master - will appear further down the page. This field is used to control the source of alerts sent by the Unified View for this configuration.
3. Syslog MUST be sent in **JSON format**.
4. Scroll past any existing configurations and click New to set up forwarding Darktrace alerts to a new server via syslog.
5. Enter the IP address of the syslog server in the Server field and optionally modify the communication port.
6. If the instance is not a Unified View, proceed to Step 7.
- If the instance where configuration is being performed is a Darktrace Unified View instance, and the Unified
View has been selected to send alerts from, an additional field - Master - will appear. This field is used to
control the source of alerts sent by the Unified View for this configuration.
- If a submaster is selected, the UV will only send alerts from that submaster for this configuration.
- If “all” is selected, alerts sourced from all submasters will be sent.
- Select the appropriate source.
7. Turn on Show Advanced Options. All options and settings are covered in Optional Filters and Settings.
8. Select **TCP-format alerting setting**
9. Select which **alert types** should be sent via Syslog. Alerts will not be sent until the master Send Alerts toggle is turned on.
10. Within the same configuration, click **Add** to **save the changes**. Observe a confirmation message.
11. Scroll to the top of the entry and **click Verify alert settings** to send a test alert to the specified Syslog server.
12. Finally, **turn on Send Alerts** and **save** changes.

{!_shared_content/integration/forwarder_configuration.md!}


{!_shared_content/operations_center/integrations/generated/98fa7079-41ae-4033-a93f-bbd70d114188_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/integrations/generated/98fa7079-41ae-4033-a93f-bbd70d114188.md!}
