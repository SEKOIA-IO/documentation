uuid: b02a2580-3457-49fd-9991-bae9d2fe7768
name: Forcepoint Management Server [BETA]
type: intake

## Overview

The Management Server is the central component for system administration. One Management Server can manage many different types of engines

- **Vendor**: Forcepoint
- **Supported environment**: On-premises
- **Version compatibility**: 6.5 and later
- **Detection based on**: Telemetry
- **Supported application or feature**: Network device logs, Network intrusion detection system

## Configure

This setup guide will show you how to forward your Forcepoint Management Server logs to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Must have Forcepoint Management Server device installed and configured
- Have administrative access to the Forcepoint Management Server interface
- Have an internal log concentrator (Rsyslog) or direct syslog forwarding capability

### Enable syslog forwarding on Forcepoint Management Server

To configure Forcepoint Management Server to forward logs to Sekoia.io, follow these steps:

1. Sign in to your Forcepoint Security Management Center (SMC).
2. Navigate to Management Server Properties.
   * Click `Home`.
   * Click `Others` > `Management Server`.
   * Right-click the `Management Server` from which you want to forward logs and select properties.
3. Configure Log Forwarding.
   * In the `Management Server` properties window, click the `Audit Forwarding` tab.
   * Click `Add` to create a new forwarding rule
   * Set `Target host`, `Port`and `Service` based on your sekoia forwarder server configuration.
   * Select the LEEF or CEF format (we only accept the both).

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Forcepoint NGFW` format.

{!_shared_content/operations_center/integrations/generated/b02a2580-3457-49fd-9991-bae9d2fe7768_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/integrations/generated/b02a2580-3457-49fd-9991-bae9d2fe7768.md!}
