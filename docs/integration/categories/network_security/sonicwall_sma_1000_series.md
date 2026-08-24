uuid: 4ed0693e-98dc-40b3-bcba-1fa61e309dd1
name: SonicWall SMA 1000 Series
type: intake

## Overview

SonicWall Secure Mobile Access 1000 Series logs are structured text-based records (mostly syslog-like and HTTP access formats, with XML exports) that capture timestamped system, administrative, access, tunnel, flow, web proxy, unregistered device, and WorkPlace events for monitoring, auditing, and incident analysis.

- **Vendor**: SonicWall
- **Supported environment**: On prem
- **Version compatibility**: 12.5
- **Detection based on**: Telemetry
- **Supported application or feature**: DNS records

## Configure

This setup guide will show you how to forward your SonicWall SMA 1000 Series logs to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Have an internal log concentrator (Rsyslog).

### Enable Syslog forwarding for SonicWall SMA 1000 Series

1. Log in the SonicWall SMA Appliance Management Console.
2. Go to `Monitoring > Logging > Configure Logging`.
3. In the `Services Log Level` section, define the severity level of log messages.
4. In the `Syslog Configuration` section, type the IP address and the port of your log concentrator as primary syslog server (`Server #1`).

    ![SonicWall SMA 1000 Series settings](/assets/instructions/sonicwall_sma_1000_series/settings.png)

5. Click `Save` to save your logging settings.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the SonicWall SMA 1000 Series format.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/4ed0693e-98dc-40b3-bcba-1fa61e309dd1_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_4ed0693e-98dc-40b3-bcba-1fa61e309dd1_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/4ed0693e-98dc-40b3-bcba-1fa61e309dd1.md!}
