uuid: aca13e14-5f7a-4587-bd04-ce0a739f65bd
name: Linux

## Overview
Linux is a family of free and open-source software operating systems built around the Linux kernel.

## Setup
This setup guide will show you how to forward logs produced by your Linux servers to SEKOIA.IO by means of an rsyslog transport channel.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```


### Configure the Rsyslog server
By default, a Linux server logs common daemons activities, the above configuration forwards everything. Depending of the linux distribution and installed software, more configuration tuning could be required.

Open or create a new Linux configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/8-linux.conf
```

Paste the following rsyslog configuration to trigger the emission of Linux logs by your rsyslog server to SEKOIA.IO:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOLinuxTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to SEKOIA.IO intake servers under SEKOIAIOLinuxTemplate template
if $hostname == "YOUR_LINUX_HOSTNAME" then @@(o)intake.sekoia.io:10514;SEKOIAIOLinuxTemplate
```

In the above `template` instruction, change the `YOUR_LINUX_HOSTNAME` variable with the correct value, and please replace `YOUR_INTAKE_KEY` variable with your intake key.

### Restart rsyslog

```bash
sudo service rsyslog restart
```

### Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.

## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)

## Further Readings

- [Logging with rsyslog on Redhat](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/s1-basic_configuration_of_rsyslog)
