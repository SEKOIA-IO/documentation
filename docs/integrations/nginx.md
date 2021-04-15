uuid: ab25af2e-4916-40ba-955c-34d2301c1f51
name: Nginx

## Overview
Nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server. It has a lot of features and because it is located between your application and your clients, it can give you a lot of information about either of them.

## Setup
This setup guide will show you how to forward both your NGINX access and error logs to SEKOIA.IO by means of an rsyslog transport channel.

### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### Configure the Rsyslog server
We can configure rsyslog to parse the `access_log` and `error_log` and report its entries to SEKOIA.IO.

Open or create a new Nginx configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/28-nginx.conf
```

At the beginning of the configuration file,  paste the following instruction to order the rsyslog server to load the module `imfile`:
```bash
$ModLoad imfile
```

Then paste the following configuration to leverage this module to monitor Nginx access and error output files (please note that the path to the log file may change depending on the OS and your configuration):
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# error log
$InputFileName /var/log/nginx/error.log
$InputFileTag nginx:
$InputFileStateFile stat-nginx-error
$InputFileSeverity error
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor

# access log
$InputFileName /var/log/nginx/access.log
$InputFileTag nginx:
$InputFileStateFile stat-nginx-access
$InputFileSeverity notice
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIONginxTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to SEKOIA.IO intake servers under SEKOIAIONginxTemplate template
if $programname startswith 'nginx' then @@(o)intake.sekoia.io:10514;SEKOIAIONginxTemplate
```

In the above `template` instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key.

### Restart rsyslog

```bash
$ sudo service rsyslog restart
```

### Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.


## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)


## Further Reading

- [Nginx Wiki](https://www.nginx.com/resources/wiki/start/)
- [Rsyslog IMFile module](https://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html)
