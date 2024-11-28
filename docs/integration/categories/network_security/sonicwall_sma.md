uuid: 622999fe-d383-4d41-9f2d-eed5013fe463
name: SonicWall SMA
type: intake

## Overview
SonicWall Secure Mobile Access offers secure and seamless remote access to corporate resources, applications, and data, enhancing workforce mobility while maintaining robust security and compliance measures.

- **Vendor**: SonicWall
- **Supported environment**: On prem
- **Version compatibility**: 10.2
- **Detection based on**: Telemetry
- **Supported application or feature**: DNS records


## Configure

This setup guide will show you how to forward your SonicWall SMA logs to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Have an internal log concentrator (Rsyslog)

### Enable Syslog forwarding for SonicWall SMA

1. Log in to the SonicWall SMA appliance’s management interface
2. Go to `Log > Settings`
3. In the Log & Alert levels section, define the severity level of log messages.
4. In the syslog settings, type the ip address and the port of your log concentrator as Primary syslog server.

    ![SonicWall SMA settings](/assets/instructions/sonicwall_sma/settings.png)

5. Click Accept to save your configuration settings

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format SonicWall SMA.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/622999fe-d383-4d41-9f2d-eed5013fe463_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_622999fe-d383-4d41-9f2d-eed5013fe463_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/622999fe-d383-4d41-9f2d-eed5013fe463.md!}

