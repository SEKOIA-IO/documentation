# Forward Logs to Sekoia.io Using Rsyslog

## Overview

Many technologies and agents allow the forwarding of their logs using the syslog protocol (RFC 5426).

We recommend you centralize them on a dedicated server: Rsyslog.

Before processing, you have to:

- Connect to [Sekoia.io Operations Center](https://app.sekoia.io/operations/)
- Add an Intake to the relevant Entity
- Keep trace of the automatically generated Intake key

## Rsyslog installation prerequisites

The following prerequisites are needed in order to setup efficient Rsyslog:

- Administrator privileges of the server: `root`
- Inbound traffic from the equipment to the Rsyslog must be open on `TCP 514`
- Outbound traffic from the Rsyslog to the Sekoia.io platform must be open on `TCP 10514` (IP for `intake.sekoia.io` is `51.159.9.95`)

## Rsyslog installation procedure

After receiving the IDs to connect to the Linux server, the main activities are to be followed.

1. Connect to the Rsyslog node using SSH

2. Install the relevant packages using your package manager

    === "Debian, Ubuntu"

        ```bash
        sudo apt update
        sudo apt install -y rsyslog rsyslog-gnutls wget
        ```

    === "Fedora, Red Hat, CentOS (yum)"

        ```bash
        sudo yum update
        sudo yum install -y rsyslog rsyslog-gnutls wget
        ```

    === "Fedora, Red Hat, CentOS (dnf)"
        
	    ```bash
        sudo dnf update
        sudo dnf install -y rsyslog rsyslog-gnutls wget
	    ```

3. Download the Sekoia.io certificate

	```bash
	sudo wget -O /etc/rsyslog.d/Sekoia-io-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
	```

4. Modify the `/etc/rsyslog.conf` main configuration file 

	This is an example of standard configuration file.
    In this file:

    * We allow syslog messages from `UDP 514` and `TCP 514` so that our rsyslog acts as a concentrator
    * We specify the maximum supported message size to 20K with the command `$MaxMessageSize 20k` since by default it is 8K and some messages (especially Windows) are longer

    !!!note
        It is not recommanded to change the default `$WorkDirectory` and the Rules which will depend of your distribution.
        In this example, the rule defined writes all syslog messages except those related to authentication in `/var/log/syslog`.
        Be sure a logrotate is applied to the files defined in rules for files rotation!

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

5. Verify your configuration file is correct

    ```bash
    rsyslogd -N1
    ```
    
    !!!note
        Rsyslogd may not be in your distribution PATH. It is usually found in `/sbin/rsyslogd`

6. Restart Rsyslog service and check its status

	```bash
	sudo systemctl restart rsyslog
	sudo systemctl status rsyslog
	```

## Configure Rsyslog server to receive and process logs

### Use case: process each incoming source on a specific port

In this use case, each source will send their events to a specific port to the Rsyslog in order to identify the sources easily.
In this section, let suppose that Windows event logs are sent to the Rsyslog on port `TCP 20516`

1. Modify the `/etc/rsyslog.conf` main configuration file

    Since Windows logs are sent to `TCP 20516`, logs should not be accepted on default port `514` in `TCP` or `UDP`
    Comment the following lines in the `/etc/rsyslog.conf` file.
    ```bash
    # module(load="imudp")
    # input(type="imudp" port="514")
    # input(type="imtcp" port="514")
    ```

    Make sure the line allowing `TCP` is not commented since Windows logs are sent with `TCP` in this example.
    ```bash
    module(load="imtcp")
    ```

2. Create a configuration file for each technology you want to forward to Sekoia.io.

    Create a dedicated file in `/etc/rsyslog.d/` for each technology to be collected.

    In this example one file is created for Windows events.

    ```bash
    sudo touch /etc/rsyslog.d/15-windows.conf
    ```

3. Edit each configuration file as needed

    ```bash
    sudo vim /etc/rsyslog.d/15-windows.conf
    ```

    In this file, an input is specified for the port `20516` in `TCP` and this input is associated to the ruleset `remote20516`.

    The name of the ruleset is not important but must be the same as the one defined below.

    To this ruleset, an action is defined to tell Rsyslog that all incoming messages associated to it must be forwarded to the Sekoia.io syslog endpoint on a specific Intake. Please change using the YOUR_INTAKE_KEY accordingly.

    ```bash
    $DefaultNetstreamDriverCAFile /etc/rsyslog.d/Sekoia-io-intake.pem
    input(type="imtcp" port="20516" ruleset="remote20516")

    template(name="SEKOIAIOWindowsTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")
    ruleset(name="remote20516"){
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

4. Restart the Rsyslog service and make sure it is correctly set up 

	```bash
	sudo systemctl restart rsyslog.service
	```

### Use case: pattern matching for incoming Windows logs

#### Identify the pattern

To receive and process Windows logs, you have to follow these steps: 

1. Verify that traffic is incoming from your log source

	```bash
	sudo tcpdump -i <change_with_interface_name> -c10 -nn src <IP_OF_THE_SOURCE> -vv
	```
	
	!!!tip
		Use `ip addr` command to find the relevant information to replace `<change_with_interface_name>`.


2. Ensure syslog events are correctly handled by the Rsyslog server

	For example, in Windows event logs, the field `hostname` is often used. 

	```bash
	sudo tail -f /var/log/syslog | grep -i "Hostname"
	```

    !!!note
        Depending of the rules set in `/etc/rsyslog.conf`, adapt the path `/var/log/syslog` with the path where the syslog messages are stored - For instance `/var/log/messages`

3. Identify syslog headers that will be used later

    **Method 1**: By watching messages in `/var/log/syslog`

    Messages in `/var/log/syslog` - or `/var/log/messages` depending of your `/etc/rsyslog.conf` configuration - are not raw syslog messages but contain information about syslog header such as the `hostname` or the `app-name` which can be used to identify your events.


    1. Search for Windows events in the file
    
    	```bash
	    sudo tail -f /var/log/syslog | grep -i "Hostname"
	    ```

    2. Identify the pattern. Similar log lines should be displayed within seconds:
    
        ```text
        Sep 16 12:39:18 windows-vm-0 Microsoft-Windows-Sysmon[3524] {"EventTime":"2022-09-16 12:39:18", [...] }
        ```
    
        In this example:

        * `windows-vm-0` corresponds to the `hostname`
        * `Microsoft-Windows-Sysmon` corresponds to the `app-name`

        We can use these information to catch our events.

        !!!important
            If `Microsoft-Windows-Sysmon` is used, only Sysmon events will be catched. To get the other Windows event logs, only `Microsoft-Windows` should be used.

    **Method 2: Create a configuration file to view raw syslog messages**

	This method helps find key information located in the syslog headers to split technologies into separate pipelines to be forwarded to the right Intakes on Sekoia.io.

	Log all the raw events received by the Rsyslog server to a **temporary file** named `00-testing.conf`.

	To identify syslog headers that will be used later, follow these steps: 

	1. Create a dedicated configuration file

		```bash
		sudo touch /etc/rsyslog.d/00-testing.conf
		```

	2. Edit the configuration file with the following information

		```bash
		sudo vim /etc/rsyslog.d/00-testing.conf
		```

	3. Make sure the file contains the following information only: 

		```bash
		template(name="SEKOIAIOTesting" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG 	[SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"] %msg%\n")
		*.* /var/log/testing.log;SEKOIAIOTesting
		```

	4. Restart the Rsyslog service and verify its status

		```bash
		sudo systemctl restart rsyslog.service && sudo systemctl status rsyslog.service
		```

	5. Search for Windows events that now contains the syslog headers

		```bash
		sudo tail -f /var/log/testing.log | grep -i "Hostname"
		```

		Similar log lines should be displayed within seconds: 

		```text
		<14>1 2022-03-24T14:33:36.738171+01:00 DESKTOP-XXXXXXX Microsoft-Windows-Sysmon 5504 LOG [SEKOIA@53288 intake_key="DO_NOT_CHANGE"] 	{"EventTime":"2022-03-24 14:33:36","Hostname":"DESKTOP-XXXXXXX","Keywords":-	922337203685XXXXXXX,"EventType":"INFO","SeverityValue":2,"Severity":"INFO","EventID":3,"SourceName":"Microsoft-Windows-Sysmon" [...]}
		```

		In this example, the syslog header is: 
		```text
		<14>1 2022-03-24T14:33:36.738171+01:00 DESKTOP-XXXXXXX Microsoft-Windows-Sysmon 5504 LOG [SEKOIA@53288 intake_key="DO_NOT_CHANGE"]
		```

		It corresponds to what was requested in the template `SEKOIAIOTesting`: 
		```text
		<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"]
		```

		!!!note 
			More information about the syslog properties can be found [here](https://www.rsyslog.com/doc/master/configuration/properties.html).

	6. Find unique information to isolate this particular technology

		In this example, `DESKTOP-XXXXXXX` or `Microsoft-Windows` information is precious.

		The `hostname`, `app-name` or `syslogtag` in the syslog headers are often used to determine which intake the log should be forwarded to.

		The comparison operators such as `contains`, `isequal` or `startswith` are most of the time used to link a syslog property to a value in the event log, in the `if` condition that will be used in the next paragraph.

		The `$hostname` in the `if condition` refers to the `%hostname%` value in the syslog header. Indeed, depending of your network, the syslog `%hostname%` can be an FQDN, an IP address (with or without NAT) or the real Hostname of the source machine.

	7. Comment the lines of the file `/etc/rsyslog.d/00-testing.conf`
	
		```bash
		# template(name="SEKOIAIOTesting" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"] %msg%\n")
		# *.* /var/log/testing.log;SEKOIAIOTesting
		```

	8.  Restart the Rsyslog service and check its status

		```bash
		sudo systemctl restart rsyslog.service && sudo systemctl status rsyslog.service
		```

	9. Remove the `/var/log/testing.log` file

		```bash
		sudo rm /var/log/testing.log
		```

#### Forward logs to Sekoia.io

1. Create configuration files for each technology you want to forward to Sekoia.io.

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
	$DefaultNetstreamDriverCAFile /etc/rsyslog.d/Sekoia-io-intake.pem

	# Customize the syslog header the an Intake Key to be collected on Sekoia.io while adding a new intake from the catalogue
	template(name="SEKOIAIOWindowsTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

	# Use a condition that identifies specifically Windows logs that send them to Sekoia.io
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

## See your events on Sekoia.io XDR

Once you're done with all the actions above, you should see your events displayed in real-time on Sekoia.io.

To verify that everything works well, connect to [Sekoia.io Events' page](https://app.sekoia.io/operations/events) and wait for events to come. 

If you would like to filter on specific intakes:

- Go to [Sekoia.io Intakes page](https://app.sekoia.io/operations/intakes)
- Copy your Intake Key. In this example, it can be: `88EYbSaG55YbVaTne8Gu93wKQbLE4axZ`
- Come back to [Sekoia.io Events' page](https://app.sekoia.io/operations/events)
- Query the following in the search bar: `sekoiaio.intake.key:"88EYbSaG55YbVaTne8Gu93wKQbLE4axZ"` and press `Enter`

## Troubleshooting

After setting up your Rsyslog, you may encounter errors due to the contextual environment or omissions while copying and pasting information.

Useful troubleshooting resources are:

- The [rsyslog documentation](https://www.rsyslog.com/doc/master/index.html)
- The syslog [github issue tracker](https://github.com/rsyslog/rsyslog/issues) 

Here's a non-exhaustive list of known errors: 

### 1- Rsyslog daemon error

Ensure the Rsyslog service is currently running on the server. 

```bash
sudo systemctl status rsyslog.service
```

If the service is down, try to restart Rsyslog:

```bash
sudo systemctl restart rsyslog.service
```

### 2- Checking logs sent to Rsyslog

In your configuration files, there will be a section that look like the following example:

```
template(name="SEKOIAIOUnboundTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"<intake_key>\"] %msg%\n")
if $programname startswith 'unbound' then @@(o)intake.sekoia.io:10514;SEKOIAIOUnboundTemplate

```

If you want to retrieve the raw data that is forwarded to Sekoia.io, you can duplicate the last line and make Rsyslog dump logs to a local file:

```
if $programname startswith 'unbound' then /tmp/nginx-output.log;SEKOIAIOUnboundTemplate
```

This way, you will be able to exactly identify what data is sent to Sekoia.io and to fix it if needed.

```
# tail -n 1 /tmp/nginx-output.log
<30>1 2021-01-13T14:52:06.934860+01:00 ote unbound - LOG [SEKOIA@53288 intake_key="<intake_key>"]  [596451:0] info: 127.0.0.1 intake.sekoia.io. A IN
```


### 3- Local messages not seen on the Rsyslog server

If you can't see local messages on the Rsyslog server, you have to make sure the logs are received on the Rsyslog server. This means that: 

- Configurations are correctly undertaken on the remote equipment
- Internal network flows are open on `TCP or UDP 514`

To fix this:  

1. Run the following command:

	```bash
	tail -n 15 /var/log/syslog
	```

2. Make sure an input is defined - and not commented - in the main configuration file `/etc/rsyslog.conf` or in specific files in `/etc/rsyslog.d`. For instance :

	```bash
	# provide TCP syslog reception
	module(load="imtcp")
	input(type="imtcp" port="514")

	# provides UDP syslog reception
	module(load="imudp")
	input(type="imudp" port="514")
	```

3. Verify that traffic is incoming from your log source

	```bash
	sudo tcpdump -i <change_with_interface_name> -c10 -nn src 1.1.1.1 -vv
	```

### 4- A `/etc/rsyslog/xx-<technology>.conf` file is misconfigured

If the Rsyslog service is failing to start, a mistyping may have been introduced in one of the `/etc/rsyslog/xx-<technology>.conf` files.

Run the following command to confirm it and get information about the error:

```bash
rsyslogd -N1
```
    
!!!note
    Rsyslogd may not be in your distribution PATH. It is usually found in `/sbin/rsyslogd`


If the Rsyslog service starts, the logs are correctly received and the `/etc/rsyslog.conf` file is correctly configured, but **no logs are received**, then it is highly possible that the `if` condition is **not correct**.

In this case:

1. Ensure the relevant `Intake Key` is provided in the template: [SEKOIA@53288 intake_key=\"**YOUR_INTAKE_KEY**\"]
2. Uncomment the lines in the `/etc/rsyslog.d/00-testing.conf`
3. Restart the Rsyslog service
4. Use the `grep` function to filter on the relevant data from `/var/log/testing.log` file
5. Identify the right information on the syslog header and adapt the `if` condition accordingly

It is possible to test your specific `if` condition. To do so: 

1. Add the following lines in the `/etc/rsyslog.d/00-testing.conf` and use your condition instead of `TO_BE_ADAPTED`. 

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

2. Restart the Rsyslog service and see if the new file `/var/log/troubleshoot.log` is created and populated with logs using `grep` command.
3. Comment the lines in the `/etc/rsyslog.d/00-testing.conf`
4. Restart the Rsyslog service
5. Remove the `/var/log/testing.log` file and `/var/log/troubleshoot.log` file if necessary

## Example of auto-setup configuration

In order to help users setting up this concentrator, the following bash script working for Ubuntu or Debian server is recommended.

It will automatically configure you Rsyslog server to collect and forward Windows Event logs.

!!!note
	`sudo` must be installed and set up for the current user.

1. Connect to Sekoia.io Operations Center, add a Windows Intake to the relevant Entity and copy the `Intake Key`.
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
	$DefaultNetstreamDriverCAFile /etc/rsyslog.d/Sekoia-io-intake.pem

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

	# Collect the SEKOIA Key for encryption between Rsyslog and Sekoia.io
	sudo wget -O /etc/rsyslog.d/Sekoia-io-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
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
