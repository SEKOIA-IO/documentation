uuid: d6d15297-e977-4584-9bb3-f0290b99f014
name: ArubaOS Switch
type: intake

## Overview

Aruba OS is the operating system developed by Aruba Networks, designed for their networking devices and infrastructure. It offers advanced features for wireless and wired networking, security, and management, enhancing network performance and reliability.

{!_shared_content/operations_center/detection/generated/suggested_rules_d6d15297-e977-4584-9bb3-f0290b99f014_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d6d15297-e977-4584-9bb3-f0290b99f014.md!}

## Configure

This setup guide will show you how to forward your ArubaOS logs to Sekoia.io by means of a syslog transport channel.

### Enable Syslog forwarding for ArubaOS

To forward ArubaOS logs through syslog, you'll need to configure syslog settings on your ArubaOS device to specify the syslog server's IP address and port. Here's a step-by-step procedure to set up syslog forwarding:

**Note:** Before proceeding, make sure you have a syslog server in your network. You'll need its IP address and the port it's listening on.

1. Log in to your ArubaOS device using SSH, Telnet, or the web-based management interface, depending on your preferred method.
2. Access the configuration mode on your ArubaOS device. For example, if you are using the CLI, you might use the `configure terminal` command.
3. Configure Syslog Settings:

	Use the following command to specify the syslog server's IP address and port:
	```
	logging x.x.x.x
	```
	Replace `x.x.x.x` with the IP address of your syslog concentrator.

	Additionally, you can specify the syslog server's UDP port using the `port` keyword:
	```
	logging x.x.x.x port yyyy
	```
	Replace `yyyy` with the port number your syslog concentrator is configured to listen on.
	4. Set Log Severity Levels (Optional): You can configure the severity level of logs that will be sent to the syslog server.

	For example, to send logs with severity level `informational` or higher, use the following command:
	```
	logging level informational
	```

	You can adjust the severity level as needed.

4. Save your configuration changes by issuing the appropriate command (e.g., `write memory` or `copy running-config startup-config`) to ensure that the syslog configuration persists across reboots.
5. Test Syslog Forwarding (Optional):

	You can generate a test log entry to ensure that logs are being forwarded to the syslog server.

	For example, use the following command:
	```
	logging x.x.x.x testing
	```
	This will generate a test log message that should appear in your syslog server's logs.

6. On your syslog server, verify that it is configured to accept syslog messages from the ArubaOS device on the specified port.


Once you've completed these steps, your ArubaOS device should start forwarding logs to the specified syslog server. You can then use your syslog server's features to analyze and store these logs for monitoring, troubleshooting, and security purposes.


### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format ArubaOS.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
