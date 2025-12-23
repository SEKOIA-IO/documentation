uuid: 049b3dfd-8f67-40b6-a22d-b86ba3b42a05
name: Delinea PRA
type: intake

## Overview

Delinea’s Privileged Remote Access (PRA) is a secure session‐broker solution that lets organizations grant, monitor and audit elevated RDP, SSH and SFTP connections to critical systems without exposing underlying credentials to end users. PRA integrates with your vault, identity providers and SIEMs to enforce just-in-time, least-privilege access policies, record every keystroke and file transfer, and stream real-time audit events for compliance and threat detection. By isolating sessions, injecting credentials on the fly and capturing detailed forensic logs, Delinea PRA reduces risk from shared accounts, lateral movement and credential theft while delivering complete visibility into who accessed what, when and how.

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Configure

This setup guide will show you how to forward your Delinea logs to Sekoia.io by means of a syslog transport channel.

### Delinea PRA configuration

#### Configuring a Secure TCP Syslog or CEF External Audit Server in Secret Server

1. Navigate to `Admin` > `Application`. The Application page appears.
2. Click the Edit button at the top right of the page.
3. Click to select the `Enable Syslog/CEF Log Output` check box. A syslog/CEF section expands below.
4. Type IP address or name for the IIS server hosting the syslog/CEF server in the `Syslog/CEF Server` text box.
5. Type the port number where the logging information will be passed (6514 is the default port for secure TCP syslog) in the `Syslog/CEF Port` text box.
6. Click the `Syslog/CEF Protocol` dropdown list and select `Secure TCP`. Secure TCP means either TLS v1.2 or v1.1 because other versions of SSL, such as SSL v3 and TLS v1.0, have known weaknesses.
7. Click to select `Syslog/CEF Time Zone` list box to `UTC Time`
8. Click the `Syslog/CEF DateTime Format` dropdown to format Syslog timestamps. The standard for Syslog is ISO timestamps; however, some still use the legacy format. Syslog is the default for upgrades to allow current configurations to retain their behavior, and ISO format is the default in new instances. Syslog format: Jun 23 2022 11:22:33. ISO 8601 format: 2022-06-23T11:22:33.000. You must enable the configuration preview to modify this setting.
9. Click the `Syslog/CEF Site` dropdown to select the related Site that Syslog/CEF will run on.
10. Click to select the `Write Syslogs As Windows Events` check box to write audits and event subscriptions to the Windows Event Log of the server.
11. Click the `Save` button.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Delinea PRA`.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/detection/generated/suggested_rules_049b3dfd-8f67-40b6-a22d-b86ba3b42a05_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/049b3dfd-8f67-40b6-a22d-b86ba3b42a05.md!}
