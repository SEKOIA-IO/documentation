# Overview

There are two ways to forward logs to SEKOIA.IO:
- [Rsyslog](#1.-Rsyslog)
- [RELP protocol](#2.-RELP-protocol)

# 1. Rsyslog

1. Create configuration files for each technology you want to forward to SEKOIA.IO.

	Create a dedicated file in `/etc/rsyslog.d/` for each technology to be collected.

	Example for the Windows log collection:

	```bash
	sudo touch /etc/rsyslog.d/15-windows.conf
	```

2. Edit each configuration file as needed

	```bash
	sudo vim /etc/rsyslog.d/15-windows.conf
	```

	The **Intake key** is needed in this step. Ensure to replace `YOUR_INTAKE_KEY` by your Windows Intake Key.

	You should also adapt the template name `SEKOIAIOWindowsTemplate` and the `if` condition parameters with appropriate content as explained in the previous section.

	Following the same example for Windows log collection:
	
	```bash
	# Refer to the location of the certificate
	$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

	# Customize the syslog header the an Intake Key to be collected on SEKOIA.IO while adding a new intake from the catalogue
	template(name="SEKOIAIOWindowsTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

	# Use a condition that identifies specifically Windows logs that send them to SEKOIA.IO
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
	```
		
3. Restart the Rsyslog service and make sure it is correctly set up 

	```bash
	sudo systemctl restart rsyslog.service
	```

# 2. RELP protocol

Rsyslog is able to push logs via a reliable protocol, called RELP. By using this protocol, SEKOIA.IO’s collection point will acknowledge logs when receiving it. This will let the client Rsyslog be able to resend events if an error occurs.

SEKOIA.IO’s RELP endpoint is available at `relp.intake.sekoia.io` (`145.239.192.124`) on port `11514`.

The most noticeable change using RELP in Rsyslog is the output module used (`omrelp`). 

Follow these steps to forward logs using RELP Protocol: 

1. Install `rsyslog-relp` and `rsyslog-openssl` packages to be able to push logs. 

	Most distributions are providing these packages natively.

2. Edit your main Rsyslog configuration to load the `omrelp` module:

	```bash
	module(load="omrelp" tls.tlslib="openssl")
	```

3. Configure the output action to push your events to SEKOIA.IO via the RELP protocol. 

	In this example, we are pushing Unbound events:

	```bash
	template(name="SEKOIAIOUnboundTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

	if ($programname startswith 'unbound') then {
	  action(
		type="omrelp"
		target="relp.intake.sekoia.io"
		port="11514"
		tls="on"
		tls.caCert="/etc/rsyslog.d/SEKOIA-IO-intake.pem"
		tls.authmode="name"
		tls.permittedPeer=["relp.intake.sekoia.io"]
		template="SEKOIAIOUnboundTemplate"
	    )
	}
	```
