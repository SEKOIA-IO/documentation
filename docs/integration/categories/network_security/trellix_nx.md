---
uuid: bae128bb-98c6-45f7-9763-aad3451821e5
title: Trellix Network Security
name: Trellix Network Security
type: intake
---

## Overview

Trellix Network Security is an effective cyberthreat protection solution that helps your organization minimize the risk of costly breaches by accurately detecting and immediately stopping advanced, targeted, and other evasive attacks hiding in internet traffic.

- **Vendor**: Trellix
- **Supported environment**: On prem
- **Version compatibility**: 10.0.1
- **Detection based on**: Telemetry
- **Supported application or feature**: Web logs


## Configure

This setup guide will show you how to forward your Trellix Network Security logs to Sekoia.io by means of a syslog transport channel.

### Prerequisites

You should have:

- Have an admin access in Trellix platform.
- Have an internal log concentrator (Rsyslog)

### Enable Syslog forwarding for Trellix Network Security

1. Log onto the Trellix NX console
2. Go to `Settings > Notifications`
3. Click on `rsyslog` and check the `Event type` check box below
4. In the Settings panel, select the `Default format` as `CEF`
5. In the `Rsyslog Server Listing`, type a name for the new entry then click on the button `Add Rsyslog Server`
6. For the new server, check the `Enabled` checkbox, type the ip address of your syslog concentrator
7. Click on the `Update` button to validate the configuration
8. (Optional) Click on the `Test-fire` button if you want to test the forwarding of the logs

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Trellix Network Security.

### Configure the Rsyslog server
Please consult the [Rsyslog Transport](/integration/ingestion_methods/syslog/overview.md) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/bae128bb-98c6-45f7-9763-aad3451821e5_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_bae128bb-98c6-45f7-9763-aad3451821e5_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/bae128bb-98c6-45f7-9763-aad3451821e5.md!}

