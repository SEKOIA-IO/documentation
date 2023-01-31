# Overview

In order to help users setting up this concentrator, the following bash script working for Ubuntu or Debian server is recommended.

It will automatically configure you Rsyslog server to collect and forward Windows Event logs.

!!!note
	`sudo` must be installed and set up for the current user.

# Steps

1. Connect to SEKOIA.IO Operations Center, add a Windows Intake to the relevant Entity and copy the `Intake Key`.
	It is possible to copy and paste this configuration locally then upload it with SCP command, or simple copy and paste it from the web to your remote server.


	```bash
	#!/bin/bash
	##### This file is used to automate the Rsyslog setup

	# Install service and dependances
	sudo apt update
	sudo apt install -y rsyslog rsyslog-gnutls wget

	### Create a dedicated Rsyslog configuration file
	RsyslogConfFile="/etc/rsyslog.conf"

	sudo /bin/cat <<\EOM >$RsyslogConfFile
	# /etc/rsyslog.conf configuration file for Rsyslog
	module(load="imuxsock") # provides support for local system logging
	module(load="imklog")   # provides kernel logging support

	# Set the maximum supported message size
	$MaxMessageSize 20k

	# provides UDP syslog reception
	module(load="imudp")
	input(type="imudp" port="514")

	# provides TCP syslog reception
	module(load="imtcp")
	input(type="imtcp" port="514")

	# Use traditional timestamp format.
	$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat

	# Set the default permissions for all log files.
	$FileOwner root
	$FileGroup adm
	$FileCreateMode 0640
	$DirCreateMode 0755
	$Umask 0022

	$ActionQueueType LinkedList     # create a queue stored in the RAM
	$ActionQueueFileName sek_fwd    # set up the prefix for writting
	$ActionQueueMaxDiskSpace 5g     # allow 5 giga of storage for the buffer
	$ActionQueueSaveOnShutdown on   # write on disk is the Rsyslog is whut down
	$ActionResumeRetryCount -1      # prevent the Rsyslog from droping the logs if the connexion is interrupted

	# Where to place spool and state files
	$WorkDirectory /var/spool/rsyslog
	$IncludeConfig /etc/rsyslog.d/*.conf

	# Rules
	*.*;auth,authpriv.none          -/var/log/syslog
	EOM

	### Create a dedicated Windows configuration file
	WindowsFile="/etc/rsyslog.d/15-windows.conf"

	sudo /bin/cat <<\EOM >$WindowsFile
	$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

	template(name="SEKOIAIOWindowsTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

	if ($syslogtag contains 'Microsoft-Windows') then {
	    action(
		type="omfwd"
		protocol="tcp"
		target="intake.sekoia.io"
		port="10514"
		TCP_Framing="octet-counted"
		StreamDriver="gtls"
		StreamDriverMode="1"
		StreamDriverAuthMode="x509/name"
		StreamDriverPermittedPeers="intake.sekoia.io"
		Template="SEKOIAIOWindowsTemplate"
	    )
	}
	EOM

	# Collect the SEKOIA Key for encryption between Rsyslog and SEKOIA.IO
	sudo wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
	```

2. Once the file created on the Rsyslog, make it executable with the command `chmod +x <filename.sh>`.

3. Run it using this command: 

	```bash
	./<filename.sh>
	```

4. Change the intake key value in the `/etc/rsyslog.d/15-windows.conf` file
5. Restart the Rsyslog service:

	```bash
	sudo systemctl restart rsyslog.service
	```
