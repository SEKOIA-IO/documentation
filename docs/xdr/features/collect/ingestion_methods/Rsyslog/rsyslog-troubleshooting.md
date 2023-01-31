# Overview

After setting up your Rsyslog, you may encounter errors due to the contextual environment or omissions while copying and pasting information.

Useful troubleshooting resources are:

- The [rsyslog documentation](https://www.rsyslog.com/doc/master/index.html)
- The syslog [github issue tracker](https://github.com/rsyslog/rsyslog/issues) 

Here's a non-exhaustive list of known errors: 
- [1- Rsyslog daemon error](#-1.-Rsyslog-daemon-error)
- [2- Checking logs sent to Rsyslog](#-2.-Checking-logs-sent-to-Rsyslog)
- [3- Local messages not seen on the Rsyslog server](#-3.-Local-messages-not-seen-on-the-Rsyslog-server)
- [4- A `/etc/rsyslog/xx-<technology>.conf` file is misconfigured](#-4.-A`-/etc/rsyslog/xx-<technology>.conf`-file-is-misconfigured)



## 1. Rsyslog daemon error

Ensure the Rsyslog service is currently running on the server. 

```bash
sudo systemctl status rsyslog.service
```

If the service is down, try to restart Rsyslog:

```bash
sudo systemctl restart rsyslog.service
```

## 2. Checking logs sent to Rsyslog

In your configuration files, there will be a section that look like the following example:

```
template(name="SEKOIAIOUnboundTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"<intake_key>\"] %msg%\n")
if $programname startswith 'unbound' then @@(o)intake.sekoia.io:10514;SEKOIAIOUnboundTemplate

```

If you want to retrieve the raw data that is forwarded to SEKOIA.IO, you can duplicate the last line and make Rsyslog dump logs to a local file:

```
if $programname startswith 'unbound' then /tmp/nginx-output.log;SEKOIAIOUnboundTemplate
```

This way, you will be able to exactly identify what data is sent to SEKOIA.IO and to fix it if needed.

```
# tail -n 1 /tmp/nginx-output.log
<30>1 2021-01-13T14:52:06.934860+01:00 ote unbound - LOG [SEKOIA@53288 intake_key="<intake_key>"]  [596451:0] info: 127.0.0.1 intake.sekoia.io. A IN
```


## 3. Local messages not seen on the Rsyslog server

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

## 4. A `/etc/rsyslog/xx-<technology>.conf` file is misconfigured

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
