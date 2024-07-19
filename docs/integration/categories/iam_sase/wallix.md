uuid: 6b8cb346-6605-4240-ac15-3828627ba899
name: Wallix
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**: Telemetry
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:
WALLIX Bastion is a “Privileged Access Management” solution.




## Configure
This setup guide will show you how to forward logs produced by your Wallix bastion to Sekoia.io by means of an syslog transport channel.

On the "SIEM Integration" page in the "System" menu, you can set up the routing of logged information log information to one or more other network devices syslog servers.

!!! Warning
    This page is only displayed when the "SIEM" functionality is associated with the license key.

To set up routing via the syslog server you previously setup, such as the [Sekoia.io Forwarder](https://docs.sekoia.io/integration/ingestion_methods/syslog/sekoiaio_forwarder/), enter the following information:

- server IP address or FQDN,
- transmission protocol (UDP or TCP),
- port number,
- log format (standard RFC 3164 format),
    - choose the timestamp format as ISO format (YYYY-MM-DDTHH:MM:SS±TZ), that contains year and time zone.
- filter for selecting the categories of logged information to be sent via the server, including:
    * configuration changes,
    * authentication logs,
    * account activities,
    * SSH proxies events,
    * RDP proxies events,
    * SSH session,
    * RDP session,
    * VNC session.

!!! Note
    When upgrading from a version prior to WALLIX Bastion 8.2, all logged information categories are selected by default for all servers previously configured on this page.

Logs will then be sent to the selected IP address, port and transmission protocol, and also stored on the local file system, so that they are always available for reading on the "Logs audit" page in the "Configuration" menu.


### Configure the syslog server

Please consult the [Sekoia.io Forwarder](https://docs.sekoia.io/integration/ingestion_methods/syslog/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

{!_shared_content/integration/detection_section.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_6b8cb346-6605-4240-ac15-3828627ba899_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/6b8cb346-6605-4240-ac15-3828627ba899.md!}

