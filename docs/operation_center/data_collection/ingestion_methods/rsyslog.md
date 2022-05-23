# Forward Logs to SEKOIA.IO Using Rsyslog

## Overview

Many technologies or agents allows the forwarding of their logs using the syslog protocol (RFC 5426).

We recommand to centralise them on a dedicated server: Rsyslog.

## Prerequisites

The following prerequisites are needed in order to setup efficient Rsyslog:

- Have administrator privileges of the Debian server: `root`.
- Inbound traffic from the equipments to the Rsyslog must be open on `TCP 514`.
- Outbound traffic from the Rsyslog to the SEKOIA.IO platform must be open on `TCP 10514` (IP for `intake.sekoia.io` is `145.239.192.38`).

## General procedure

After receiving the IDs to connect to the Linux server, the main activities are to be followed.

- Connect to the Rsyslog node using SSH
- Install the relevant packages
- Modify the `/etc/rsyslog.conf` main configuration file
- Create configuration files for each technology you want to forward to SEKOIA.IO
- Edit these files with the related Intake Keys
- Download the SEKOIA.IO certificate
- Start the Rsyslog service and ensure it is correclty set-up

## Example of auto-setup configuration

In order to help users setting up this concentrator we suggest the following bash script working for Ubuntu or Debian server.

It will automatically configure you Rsyslog server to collect and forward Windows Event logs.
`sudo` must be installed and set-up for the current user.

> Before, connect to SEKOIA.IO Operations Center, add a Windows Intake to the relevant Entity, and note the Intake Key

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
$ActionQueueSaveOnShutdown on   # write on disk is the rsyslog is whut down
$ActionResumeRetryCount -1      # prevent the rsyslog from droping the logs if the connexion is interrupted

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

# Collect the Sekoia Key for encryption between Rsyslog and Sekoia.io
sudo wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

It is possible to copy-paste this configuration locally then upload it with SCP command, or simple copy-paste it from the web to your remote server.

> Once the file created on the Rsyslog, dont forget to make it executable with the command `chmod +x <filename.sh>`

Then run it:
```bash
./<filename.sh>
```

- Change the intake key value in the `/etc/rsyslog.d/15-windows.conf` file
- Restart the Rsyslog service:
```bash
sudo systemctl restart rsyslog.service
```

## Forward Logs Using RELP Protocol

Rsyslog is able to push logs via a reliable protocol, called RELP. By using this prococol, SEKOIA.IO’s collection point will acknowledge logs when receiving it. This will let the client Rsyslog be able to resend events if an error occured.

SEKOIA.IO’s RELP endpoint is available at `relp.intake.sekoia.io` (`145.239.192.124`) on port `11514`.

The most noticeable change using RELP in Rsyslog, is the output module used (`omrelp`). The first step is to install `rsyslog-relp` and `rsyslog-openssl` packages to be able to push logs. Most distributions are providing these packages natively.

Then, you have to edit your main Rsyslog configuration to load the `omrelp` module:

```
module(load="omrelp" tls.tlslib="openssl")
```

Finally, you have to configure the output action to push your events to SEKOIA.IO via the RELP protocol. In this example, we are pushing Unbound events.

```
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

## Troubleshooting

After setting up your Rsyslog, you may face issues due to contextual environment or error during copy pasting.

### Rsyslog daemon

Ensure the Rsyslog service is currrently running on the server
```bash
ps -A | grep rsyslog
```
You should see a line with `rsyslogd` daemon. If not, try to restart the service:
```bash
sudo systemctl restart rsyslog.service
```

Also insure the following lines are not commented in the configuration file `/etc/rsyslog.conf`:
```bash
# provide TCP syslog reception
module(load="imtcp")
input(type="imtcp" port="514")

# provides UDP syslog reception
module(load="imudp")
input(type="imudp" port="514")
```

### Local messages

Ensure the logs are received on the Rsyslog server, meaning:
- Configurations are correctly undertaken on the remote equipements
- Internal network flows are open on `TCP or UDP 514`

To check it, run the following command:
```bash
tail -n 15 /var/log/syslog
```

### Forwarded messages to SEKOIA.IO

Ensure the connection is `ESTABLISHED` between the Rsyslog server and SEKOIA.IO. To do so, please run the following command:
```bash
sudo ss -ltp | grep syslog
```

- Check that traffic is incoming from your log source
```bash
sudo tcpdump -i <change_with_interface_name> -c10 -nn src 1.1.1.1 -vv
```

If the connection is not established, and the previous statuses are operational, it is possible that a file `xx-<technology>.conf` has a mistyping.
By experience, most of the time there is a misconfiguration in the `IF` condition.

For example, if you receive the Fortigate logs in `/var/log/syslog` but not in SEKOIA.IO, you can follow those steps:

- First try to log the raw events **with the syslog header** to a local file, by appending the following line in the configuration file (/etc/rsyslog.conf or /etc/rsyslog.d/xx-<technology>.conf):
```bash
template(name="SEKOIAIOTroubleshoot" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"] %msg%\n")
*.* /var/log/troubleshoot.log;SEKOIAIOTroubleshoot
```

- Restart the Rsyslog service and check its status

```bash
sudo systemctl restart rsyslog.service
sudo systemctl status rsyslog.service
```

- Check if the `troubleshoot.log` file is created and populated
```bash
sudo tail /var/log/troubleshoot.log
```
- Comment the two lines prviously added, starting with `template` et `*.*`
    
- Restart the Rsyslog service after 1 to 5 minutes since the `troubleshoot.log` file is begining to be populated depending on the verbosity of the asset you would like to collect. And check for its status
```bash
sudo systemctl restart rsyslog.service
sudo systemctl status rsyslog.service
```
    
- Search for a specific value that is only present on this technology (a field name, the name of the device...)
```bash
sudo cat /var/log/troubleshoot.log | grep "The_specifique_value_you_are_looking_for"
```
    
- Identify the information you were looking for in the `if condition` of your `/etc/rsyslog.d/xx-<technology>.conf`

You should see log lines starting with the syslog header like `<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"]` followed by the message itself.

The `$hostname` in the `if condition` refers to the `%hostname%` value in the syslog header. Indeed, depending of your network, the syslog `%hostname%` can be an FQDN, an IP address (with or withou NAT) or the real Hostname of the source machine. 
    
- Then edit your configuration file by adding the `if condition` step by step, and verify you apply the right template with your Intake Key
