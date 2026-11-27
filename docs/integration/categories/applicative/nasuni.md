uuid: 1646972c-7cae-410c-95e3-c79c6844d190
name: Nasuni
type: intake

## Overview
- **Vendor**: Nasuni
- **Supported environment**: On-premise
- **Version compatibility**: 10
- **Detection based on**: Telemetry
- **Supported application or feature**: Application Logs

Nasuni is the unstructured data foundation for enterprise teams and AI. Powering the operational file layer where work happens

## Supported versions

This integration supports the following versions:

- 10

## Configure

This setup guide will show you how to forward your Nasuni logs to Sekoia.io by means of a syslog transport channel.

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Enable Volume Auditing

1. Log in to the Nasuni Management Console.

2. Go to the “Volumes” tab on the navigation bar.

3. Go to “Auditing” in the “Volume Services” section.

4. Select every volume that needs to send its logs.

5. Press the button "Edit X Volumes"

6. Toggle the Auditing Enabled ON/OFF button

7. Select the event types you wish to monitor

8. Select a retention time in the "Prune Audit Logs" section according to your needs and available storage (Warning, auditing data can take a lot of storage space)

9. Check the "Send Audit messages to syslog" checkbox

10. Save Auditing Settings. 

### Edit Syslog Export settings

1. Log in to the Nasuni Management Console.

2. Go to the "Filers" tab on the navigation bar.

3. Go to "Syslog Export Settings  in the "Filer Settings" section on the left.

4. Select every FIler that needs to send its logs.

5. Press the button "Edit X Filer"

6. In the Servers section, fill in your syslog forwarder's IP and port (ex: 192.168.1.20:514) 

7. Toggle the "Send Auditing Messages" ON/OFF button

8. Save Settings. 

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the Nasuni format.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/1646972c-7cae-410c-95e3-c79c6844d190_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_1646972c-7cae-410c-95e3-c79c6844d190_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/1646972c-7cae-410c-95e3-c79c6844d190.md!}

