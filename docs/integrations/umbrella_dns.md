uuid: 90179796-f949-490c-8729-8cbc9c65be55 
name: Umbrella DNS Logs 

## Overview
Cisco Umbrella offers flexible, cloud-delivered security. It combines multiple security functions into one solution, so that protection can be extended to devices, remote users, and distributed locations anywhere. CISCO Umbrella is a leading provider of network security and recursive DNS services. With the intelligent proxy, if a site is considered potentially suspicious or could host malicious content, Umbrella returns the intelligent proxy's IP address. The request to that domain is then routed through their cloud-based secure gateway, and malicious content is found and stopped before it's sent to their customers.

## Setup
This setup guide will show you how to forward logs produced by CISCO Umbrella service to SEKOIA.IO by means of an Rsyslog transport channel.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### 1. Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### 2. Collect proxylogs files and send them to rsyslog
After configuring Umbrella Log Management with AWS S3, the logs you download will be gzipped CSVs in appropriate subfolder with the following naming format:

```bash
dnslogs/<year>-<month>-<day>/<year>-<month>-<day>-<hour>-<minute>.csv.gz
```

To send these logs to SEKOIA.IO, we suggest the use of the logger Unix command. For each unzipped file, use the following command line:

```bash
logger -t dnslogs -f <YYYY>-<MM>-<DD>-<hh>-<mm>-<xxxx>.csv
```

### 3. Configure the Rsyslog server
You can configure your Rsyslog server to forward your fortigate logs to SEKOIA.IO.

Open or create a new Umbrella configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/6-umbrella.conf
```

Then paste the following configuration:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOUmbrellaDnslogsTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n") 

# Send your Umbrella events to SEKOIA.IO intake servers under SEKOIAIOUmbrellaDnslogsTemplate template
if $syslogtag contains "dnslogs" then @@(o)intake.sekoia.io:10514;SEKOIAIOUmbrellaDnslogsTemplate
```

In the above `template` instruction, replace `YOUR_INTAKE_KEY` variable with the intake key available in the `Intakes` menu of SEKOIA.IO.

### 4. Restart rsyslog

```bash
$ sudo service rsyslog restart
```

### 5. Enjoy your events

Once the configuration has been done on Sekoia side, you can go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.

## Further Readings
- [CISCO Umbrella User Guide - Logs Management](https://docs.umbrella.com/deployment-umbrella/docs/log-management)
