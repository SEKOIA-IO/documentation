uuid: 325369ba-8515-45b4-b750-5db882ea1266
name: sophos
type: intake

## Overview
Sophos firewalls offer an integrated software solution that provides superior performance in an all-in-one firewall. Its hardened operating system, stateful packet inspection, content filtering (virus & surf protection), application proxies and IPsec based VPN provides powerful solutions to today's security issues. It is designed to maximise networks security without compromising its performance enabling telecommuters, branch offices, customers and suppliers to safely share critical business information.


{!operation_center/integration_catalog/generated/sentinelone_do_not_edit_manually.md!}

## Configure

This setup guide will show you how to forward your Sophos logs
to SEKOIA.IO by means of an Rsyslog transport channel.

### Configure Sophos Firewall
You can configure a syslog server in Sophos Firewall by following the instructions below (Which is appropriate for an XG Firewall, please refer to your documentation in other cases).

- Go to System Services > Log Settings and click Add to configure a syslog server.
- Enter a name for the syslog server.
- Enter the IP Address of the syslog server. Messages from the device will be sent to the entered IP address.
- Enter a Port number that the device will use for communicating with the syslog server. Device will send messages using the selected port.
- Select the Facility from the available options. Note: Facility informs the syslog server of the log message's source. It is defined by the syslog protocol. You can configure the facility to distinguish log messages from different devices. This parameter helps you identify the device that recorded a specific log file.
- Select the Severity Level from the available options.
- Click Save to save the configuration.

### Configure the Rsyslog server
You can configure your Rsyslog server to forward your Sophos logs to SEKOIA.IO. Please consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
