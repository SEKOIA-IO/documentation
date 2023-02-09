uuid: aeb7d407-db57-44b2-90b6-7df6738d5d7f
name: FreeRADIUS
type: intake

## Overview

FreeRADIUS is an implementation of RADIUS, a protocol for remote user Authentication, Authorization and Accounting.

In this documentation, you will learn how to collect and send FreeRADIUS logs to SEKOIA.IO.

!!! warning
    This format is still in beta, please use it wisely.

{!_shared_content/operations_center/detection/generated/suggested_rules_aeb7d407-db57-44b2-90b6-7df6738d5d7f_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/freeradius_do_not_edit_manually.md!}

## Configure

This setup guide will lead you into forwarding FreeRADIUS's logs to SEKOIA.IO

### Prerequisites

An internal log concentrator (Rsyslog) is required to collect and forward events to SEKOIA.IO.

### Create the intake in SEKOIA.IO

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `FreeRADIUS`. Copy the intake key.

### Transport to SEKOIA.IO

Please consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO

### Enable Syslog forwarding for FreeRADIUS

On the system hosting the FreeRADIUS:

1. Edit the file `/etc/freeradius/radiusd.conf` and update the log section:

	```bash
	$ vi /etc/freeradius/radiusd.conf
	log {
	  destination = syslog
	  syslog_facility = local1
	  stripped_names = no
	  auth = yes

	  # don't logs password
	  auth_badpass = no 
	  auth_goodpass = no
	}
	```

2. Foward logs to the concentrator:

	- For Debian-based and RedHat-based linux distribution, edit the file `/etc/rsyslog.conf` and forward facility `local1`'s logs to our log concentrator:

		```bash
		$ vi /etc/rsyslog.conf
		# ensure the module imuxsock is not commented, to provide support for local system logging
		module(load="imuxsock")

		local1.* @<ip to the concentrator>
		```

		Restart the rsyslog service:

		```bash
		$ systemctl restart rsyslog
		```

	- For other linux distributions and BSD systems, edit the file `/etc/syslog.conf` and forward facility  `local1`'s logs to our concentrator:

		```bash
		$ vi /etc/syslog.conf
		local1.* @<ip to the concentrator>
		```

		Restart the syslog service.

### Enjoy your events

Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.
