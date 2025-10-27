uuid: 2c9ce787-85dc-45d9-a320-33a96077fead
name: Forcepoint NGFW
type: intake

## Overview

Forcepoint Next-Generation Firewall provide advanced threat protection and network security, utilizing a blend of cloud and on-premises security solutions to safeguard organizations from cyber threats while ensuring secure connectivity and compliance.

- **Vendor**: Forcepoint
- **Supported environment**: On-premises
- **Version compatibility**: 6.5 and later
- **Detection based on**: Telemetry
- **Supported application or feature**: Network device logs, Network intrusion detection system, Network protocol, Firewall logs

{!_shared_content/operations_center/integrations/generated/2c9ce787-85dc-45d9-a320-33a96077fead_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_2c9ce787-85dc-45d9-a320-33a96077fead_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/2c9ce787-85dc-45d9-a320-33a96077fead.md!}

## Configure

This setup guide will show you how to forward your Forcepoint NGFW logs to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Must have Forcepoint NGFW device installed and configured
- Have administrative access to the Forcepoint NGFW management interface
- Have an internal log concentrator (Rsyslog) or direct syslog forwarding capability

### Enable syslog forwarding on Forcepoint NGFW

To configure Forcepoint NGFW to forward logs to Sekoia.io, follow these steps:

1. Sign in to your Forcepoint Security Management Center (SMC).
2. Navigate to Log Server Properties.
   * Click `Home`.
   * Click `Others` > `Log Server`.
   * Right-click the `Log Server` from which you want to forward logs and select properties.
3. Configure Log Forwarding.
   * In the `Log Server` properties window, click the `Log Forwarding` tab.
   * Select the LEEF or CEF format (we only accept the both).
   * Click `Add` to create a new forwarding rule.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Forcepoint NGFW` format.

### Additional Resources
- [Forcepoint NGFW: Forwarding log data from Log Servers to external hosts](https://help.forcepoint.com/ngfw/en-us/7.0.1/GUID-1856F6D5-AC49-4A41-8EE0-766BAB088E39.html)
- [Forcepoint NGFW: Add log forwarding rules to Log Servers](https://help.forcepoint.com/ngfw/en-us/7.0.1/GUID-4C98583A-7BA4-4028-AD85-6D20B58EC420.html#GUID-4C98583A-7BA4-4028-AD85-6D20B58EC420)
- [Forcepoint NGFW: Enable TLS protection for log or audit data forwarding](https://help.forcepoint.com/ngfw/en-us/7.0.0/GUID-D8B51C4D-AEAF-4108-B602-D38246F7F5BC.html)
