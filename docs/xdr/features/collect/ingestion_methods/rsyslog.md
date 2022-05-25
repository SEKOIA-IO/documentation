# Forward Logs to SEKOIA.IO Using Rsyslog

## Overview

Many technologies or agents allows the forwarding of their logs using the syslog protocol (RFC 5426).

We recommend to centralise them on a dedicated server: Rsyslog.

Before processing, we suggest to:

- Connect to SEKOIA.IO Operations Center
- Add an Intake to the relevant Entity

- Keep trace of the automatically generated **Intake Key**.

## Rsyslog installation prerequisites

The following prerequisites are needed in order to setup efficient Rsyslog:

- Have administrator privileges of the Debian server: `root`.
- Inbound traffic from the equipment to the Rsyslog must be open on `TCP 514`.
- Outbound traffic from the Rsyslog to the SEKOIA.IO platform must be open on `TCP 10514` (IP for `intake.sekoia.io` is `145.239.192.38`).

## Rsyslog installation procedure

After receiving the IDs to connect to the Linux server, the main activities are to be followed.

### Connect to the Rsyslog node using SSH

### Install the relevant packages

```bash
sudo apt update
sudo apt install -y rsyslog rsyslog-gnutls wget
```

### Download the SEKOIA.IO certificate

```bash
sudo wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia/assets/files/SEKOIA-IO-intake.pem
```

### Modify the `/etc/rsyslog.conf` main configuration file. This is an example of standard configuration file, to adapt if needed:

```bash
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
```

### Ensure Rsyslog service is running

```bash
ps -A | grep rsyslog
sudo systemctl status rsyslog.service
```

## Configure the Rsyslog server to receive and treat incoming logs - Example with Windows logs

### Check that traffic is incoming from your log source

```bash
sudo tcpdump -i <change_with_interface_name> -c10 -nn src <IP_OF_THE_SOURCE> -vv

```

> Use `ip addr` command to find the relevant information to relace `<change_with_interface_name>`

### Ensure that syslog events are correctly handled by the Rsyslog server

For example looking Windows event logs, knowing that many logs uses the field "Hostname":

```bash
sudo tail -f /var/log/syslog | grep -i "Hostname"
```

### Create a configuration file to identify syslog headers that will be used later

This method helps finding key information located in the syslog headers to split technologies into separate pipelines to be forwarded to the right Intakes on SEKOIA.IO.
We will log all the raw events received by the Rsyslog server to a **temporary file** named "00-testing.conf"

- First create a dedicated configuration file

```bash
sudo touch /etc/rsyslog.d/00-testing.conf
```

- Edit the configuration file with the following information

```bash
sudo vim /etc/rsyslog.d/00-testing.conf
```

- Ensure this file will contain the following information only

```bash
template(name="SEKOIAIOTesting" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"] %msg%\n")
*.* /var/log/testing.log;SEKOIAIOTesting
```

- Restart the Rsyslog service and check its status

```bash
sudo systemctl restart rsyslog.service && sudo systemctl status rsyslog.service
```

- Search for Windows events that now contains the syslog headers

```bash
sudo tail -f /var/log/testing.log | grep -i "Hostname"
```

After few seconds, this should display similar log lines as following:

```text
<14>1 2022-03-24T14:33:36.738171+01:00 DESKTOP-XXXXXXX Microsoft-Windows-Sysmon 5504 LOG [SEKOIA@53288 intake_key="DO_NOT_CHANGE"] {"EventTime":"2022-03-24 14:33:36","Hostname":"DESKTOP-XXXXXXX","Keywords":-922337203685XXXXXXX,"EventType":"INFO","SeverityValue":2,"Severity":"INFO","EventID":3,"SourceName":"Microsoft-Windows-Sysmon" [...]}
```

In this example, the syslog header is: `<14>1 2022-03-24T14:33:36.738171+01:00 DESKTOP-XXXXXXX Microsoft-Windows-Sysmon 5504 LOG [SEKOIA@53288 intake_key="DO_NOT_CHANGE"]`

Corresponding to what was requested in the template "SEKOIAIOTesting": `<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"]`

> More information about the syslog properties can be found [here](https://www.rsyslog.com/doc/master/configuration/properties.html).

- Find unique information to isolate this particular technology

In this example, "DESKTOP-XXXXXXX" or "Microsoft-Windows" information is precious.

> The `hostname`, `app-name` or `syslogtag` in the syslog headers are often used to determine to which intake the log should be forwarded.

> The comparison operators such as `contains`, `isequal` or `startswith` are most of the time used to link a syslog property to a value in the event log, in the `if` confition that will be used in the next paragraph.

> The `$hostname` in the `if condition` refers to the `%hostname%` value in the syslog header. Indeed, depending of your network, the syslog `%hostname%` can be an FQDN, an IP address (with or without NAT) or the real Hostname of the source machine. 

- Comment the lines of the file "/etc/rsyslog.d/00-testing.conf"

```bash
# template(name="SEKOIAIOTesting" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"] %msg%\n")
# *.* /var/log/testing.log;SEKOIAIOTesting
```

-  Restart the Rsyslog service and check its status

```bash
sudo systemctl restart rsyslog.service && sudo systemctl status rsyslog.service
```

- Remove the "/var/log/testing.log" file

```bash
sudo rm /var/log/testing.log
```

## Forward logs to SEKOIA.IO

### Create configuration files for each technology you want to forward to SEKOIA.IO. 

We recommend to create a dedicated file in `/etc/rsyslog.d/` for each technology to be collected.
Example for the Windows log collection:

```bash
sudo touch /etc/rsyslog.d/15-windows.conf
```

### Edit each configuration file as needed

```bash
sudo vim /etc/rsyslog.d/15-windows.conf
```

> The **Intake key** is needed at this step. Ensure to replace "YOUR_INTAKE_KEY" by your Windows Intake Key.
> Please also adapt the template name "SEKOIAIOWindowsTemplate"
> And the `if` condition parameters with appropriate content as explained in the previous section.

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

- Start the Rsyslog service and ensure it is correctly set-up

```bash
sudo systemctl restart rsyslog.service
```

## See your events on SEKOIA.IO XDR

Once all the above actions performed, you should see your events displaying in real-time on SEKOIA.IO.

To do so connect to [SEKOIA.IO Events page](https://app.sekoia.io/operations/events)

If you would like to filter on specific Intakes:

- Go to [SEKOIA.IO Intakes page](https://app.sekoia.io/operations/intakes)
- Copy your Intake Key, for instance: `88EYbSaG55YbVaTne8Gu93wKQbLE4axZ`
- Come back to [SEKOIA.IO Events page](https://app.sekoia.io/operations/events)
- In the search bar, query the following: `customer.intake_key:"88EYbSaG55YbVaTne8Gu93wKQbLE4axZ"` in this example and press `Enter`

## Forward Logs Using RELP Protocol

Rsyslog is able to push logs via a reliable protocol, called RELP. By using this protocol, SEKOIA.IO’s collection point will acknowledge logs when receiving it. This will let the client Rsyslog be able to resend events if an error occurred.

SEKOIA.IO’s RELP endpoint is available at `relp.intake.sekoia.io` (`145.239.192.124`) on port `11514`.

The most noticeable change using RELP in Rsyslog, is the output module used (`omrelp`). The first step is to install `rsyslog-relp` and `rsyslog-openssl` packages to be able to push logs. Most distributions are providing these packages natively.

Then, you have to edit your main Rsyslog configuration to load the `omrelp` module:

```bash
module(load="omrelp" tls.tlslib="openssl")
```

Finally, you have to configure the output action to push your events to SEKOIA.IO via the RELP protocol. In this example, we are pushing Unbound events.

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

## Troubleshooting

After setting up your Rsyslog, you may face issues due to contextual environment or error during copy pasting.

### Rsyslog daemon error

Ensure the Rsyslog service is currently running on the server

```bash
ps -A | grep rsyslog
```
You should see a line with `rsyslogd` daemon. If not, try to restart the service:

```bash
sudo systemctl restart rsyslog.service
```

### Local messages not seen on the Rsyslog server


Ensure the logs are received on the Rsyslog server, meaning:

- Configurations are correctly undertaken on the remote equipment
- Internal network flows are open on `TCP or UDP 514`

To check it, run the following command:

```bash
tail -n 15 /var/log/syslog
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

- Check that traffic is incoming from your log source

```bash
sudo tcpdump -i <change_with_interface_name> -c10 -nn src 1.1.1.1 -vv
```

### A `/etc/rsyslog/xx-<technology>.conf` file is misconfigured

If the Rsyslog service is failing to start, a mistyping can have been introduced in one of the `/etc/rsyslog/xx-<technology>.conf` files.

If the Rsyslog service starts, the logs are correctly received and the `/etc/rsyslog.conf` file is correctly configured but still no logs are received.
Then it is highly possible that the `if` condition is not correct.
In this case: 

- Ensure the relevant `Intake Key` is provided in the template: [SEKOIA@53288 intake_key=\"**YOUR_INTAKE_KEY**\"]
- Uncomment the lines in the "/etc/rsyslog.d/00-testing.conf"
- Restart the Rsyslog service
- Use the `grep` function to filter on the relevant data from "/var/log/testing.log" file
- Identify the right information on the syslog header and adapt the `if` condition accordingly

> It is possible to test the your specific `if` condition by adding the following lines in the "/etc/rsyslog.d/00-testing.conf", and using your condition instead of "TO_BE_ADAPTED"

```bash
template(name="SEKOIAIOTroubleshoot" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"] %msg%\n")

if (TO_BE_ADAPTED) then {
    action(
	    type="omfile"
	    file="/var/log/troubleshoot.log"
	    Template="SEKOIAIOTroubleshoot"
    )
}
```

> Restart the Rsyslog service and see if the new file "/var/log/troubleshoot.log" is created and populated with logs using `grep` command

Once the modification(s) performed:

- Comment the lines in the "/etc/rsyslog.d/00-testing.conf"
- Restart the Rsyslog service
- Remove the "/var/log/testing.log" file, and "/var/log/troubleshoot.log" file if necessary

## Example of auto-setup configuration

In order to help users setting up this concentrator we suggest the following bash script working for Ubuntu or Debian server.

It will automatically configure you Rsyslog server to collect and forward Windows Event logs.
`sudo` must be installed and set-up for the current user.

> Before, connect to SEKOIA.IO Operations Center, add a Windows Intake to the relevant Entity, and note the `Intake Key`

It is possible to copy-paste this configuration locally then upload it with SCP command, or simple copy-paste it from the web to your remote server.

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

# Collect the Sekoia Key for encryption between Rsyslog and Sekoia.io
sudo wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia/assets/files/SEKOIA-IO-intake.pem
```

> Once the file created on the Rsyslog, don't forget to make it executable with the command `chmod +x <filename.sh>`

Then run it:

```bash
./<filename.sh>
```

- Change the intake key value in the `/etc/rsyslog.d/15-windows.conf` file
- Restart the Rsyslog service:

```bash
sudo systemctl restart rsyslog.service
```
