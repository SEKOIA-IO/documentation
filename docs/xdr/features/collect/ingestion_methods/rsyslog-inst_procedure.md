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

3. Download the SEKOIA.IO certificate

	```bash
	sudo wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
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
