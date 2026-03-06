uuid: 325369ba-8515-45b4-b750-5db882ea1266
name: Sophos Firewall
type: intake

## Overview
Sophos firewalls offer an integrated software solution that provides superior performance in an all-in-one firewall. Its hardened operating system, stateful packet inspection, content filtering (virus & surf protection), application proxies and IPsec based VPN provides powerful solutions to today's security issues. It is designed to maximise networks security without compromising its performance enabling telecommuters, branch offices, customers and suppliers to safely share critical business information.

- **Vendor**: Sophos
- **Supported environment**: On prem
- **Version compatibility**: 19.5
- **Detection based on**: Telemetry
- **Supported application or feature**: Network device logs, Network protocol analysis


## Configure

This setup guide will show you how to forward your Sophos logs
to Sekoia.io by means of a syslog transport channel.

### Configure Sophos Firewall
You can configure a syslog server in Sophos Firewall by following the instructions below (Which is appropriate for an XG Firewall, please refer to your documentation in other cases).

- Go to System Services > Log Settings and click Add to configure a syslog server.
- Enter a name for the syslog server.
- Enter the IP Address of the syslog server. Messages from the device will be sent to the entered IP address.
- Enter a Port number that the device will use for communicating with the syslog server. Device will send messages using the selected port.
- Select the Facility from the available options, "DAEMON" should work.

!!! Note
    Facility informs the syslog server of the log message's source. It is defined by the syslog protocol. You can configure the facility to distinguish log messages from different devices. This parameter helps you identify the device that recorded a specific log file.

- Confirm the protocol is UDP.
- Select the Severity Level from the available options.
- Deactivate the option "Secure log transmission".
- Click Save to save the configuration.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.


{!_shared_content/operations_center/integrations/generated/325369ba-8515-45b4-b750-5db882ea1266_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_325369ba-8515-45b4-b750-5db882ea1266_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/325369ba-8515-45b4-b750-5db882ea1266.md!}

