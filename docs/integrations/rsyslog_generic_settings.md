# Rsyslog set-up and troubleshoot

## Overview
Many technologies or agents allows the forwarding of their logs using the syslog protocol (RFC 5426).
We recommand to centralise them on a dedicated server: the Rsyslog.

## Prerequisites
The following prerequisites are needed in order to setup efficient Rsyslog:
- Have administrator privileges of the Debian server: `root`.
- Inbound traffic from the equipments to the Rsyslog must be open on `TCP 514`
- Outbound traffic from the Rsyslog to the SEKOIA.IO platform must be open on `TCP 10514` (IP for `intake.sekoia.io` is `145.239.192.38`)

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

> Before, connect to SEKOIA.IO Operation Center, add a Windows Intake to the relevant Entity, and note the Intake Key

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

It is possible to copy-past this configuration locally then upload it with SCP command, or simple copy-past it from the web to your remote server.

> Once the file created on the Rsyslog, dont forget to make it executable with the command `chmod +x <filename.sh>`

Then run it: 
```bash
./<filename.sh>
```

- Change the Intake Key value in the "/etc/rsyslog.d/15-windows.conf" file
- Restart the rsyslog service: 
```bash
sudo systemctl restart rsyslog.service
```

## Troubleshoot
After setting up your Rsyslog, you may face issues due to contextual environment or error during copy pasting.

### Rsyslog daemon
Ensure the Rsyslog service is currrently running on the server
```bash
ps -A | grep rsyslog 
```
You should see a line with rsyslogd daemon. If not, try to restart the service:
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
Ensure the logs are received on the Rsyslog, meaning:
- Configurations are correctly undertaken on the remote equipements
- Internal network flows are open on `TCP 514`

To check it, run the following command:
```bash
tail -n 15 /var/log/syslog
``` 

### Forwarded messages to SEKOIA.IO
Ensure the connection is `ESTABLISHED` between the Rsyslog server and SEKOIA.IO. To do so, please run the following command:
```bash
sudo ss -ltp | grep syslog 
```

If the connection is not established, and the previous statuses are operational, it is possible that a file `xx-<technology>.conf` has a mistyping.
By experience, most of the time there is a misconfiguration in the `IF` condition.

For example, if you receive the Fortigate logs in `/var/log/syslog` but not in SEKOIA.IO, you can follow those steps:
- First try to log the raw events to a local file, by appending the following line in the configuration file:
```bash
*.* then /tmp/fortigate.log;SEKOIAIOFortigateTemplate
```

- Restart the Rsyslog service
```bash
sudo systemctl restart rsyslog.service
```

-Check if the fortigate.log file is created and populated
```bash
sudo tail /tmp/fortigate.log
```

- Then edit your configuration file by adding the `if condition` step by step
