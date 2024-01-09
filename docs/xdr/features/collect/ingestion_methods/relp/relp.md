# Forward Logs to Sekoia.io Using RELP

Rsyslog is able to push logs via a reliable protocol, called RELP. By using this protocol, Sekoia.io’s collection point will acknowledge logs when receiving it. This will let the client Rsyslog be able to resend events if an error occurs.

Before processing, you have to:

- Connect to [Sekoia.io Operations Center](https://app.sekoia.io/operations/)
- Add an Intake to the relevant Entity
- Keep trace of the automatically generated Intake key

To forward events using this acknowledge protocol to Sekoia.io, you have to send events using TLS to `relp.intake.sekoia.io` and to respect the RFC 5426. Additionally, you need to update the syslog header with the intake key you created earlier.

The most noticeable change using RELP in Rsyslog is the output module used (`omrelp`). 

Follow these steps to forward logs using RELP Protocol: 

1. Install `rsyslog-relp` and `rsyslog-openssl` packages to be able to push logs. 

	Most distributions are providing these packages natively.

2. Edit your main Rsyslog configuration to load the `omrelp` module:

	```bash
	module(load="omrelp" tls.tlslib="openssl")
	```

3. Configure the output action to push your events to Sekoia.io via the RELP protocol. 

	In this example, we are pushing Unbound events:

	```bash
	template(name="SEKOIAIOUnboundTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

	if ($programname startswith 'unbound') then {
	  action(
		type="omrelp"
		target="relp.intake.sekoia.io"
		port="11514"
		tls="on"
		tls.caCert="/etc/rsyslog.d/Sekoia-io-intake.pem"
		tls.authmode="name"
		tls.permittedPeer=["relp.intake.sekoia.io"]
		template="SEKOIAIOUnboundTemplate"
	    )
	}
	```