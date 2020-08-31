uuid: f0a10c21-37d1-419f-8671-77903dc8de69
name: checkpoint

## Overview

Check Point’s Next Generation Firewalls (NGFW’s) are trusted by customers for their highest security effectiveness and their ability to keep organizations protected from sophisticated fifth generation cyber-attacks. Check Point’s NGFW includes 23 Firewall models optimized for running all threat prevention technologies simultaneously, including full SSL traffic inspection, without compromising on security or performance.

## Setup

This setup guide will show you how to forward your Checkpoint firewall logs
to SEKOIA.IO by means of an Rsyslog transport channel.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

We are currently supporting the following firewall versions: R77.30, R80.10, R80.20, R80.30.

### 1. Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### 2. Configure Checkpoint
The first step is to configure Checkpoint to log the awaited traffic.
This could be done differently depending on your current setup, one solution is to export logs with the [Log Exporter](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk122323).

### 3. Configure the Rsyslog server
You can configure your Rsyslog server to forward your checkpoint logs to SEKOIA.IO.

Open or create a new Checkpoint configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/52-checkpoint.conf
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
template(name="SEKOIAIOCheckpointTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] CEF:%msg%\n")

# Send your Checkpoint events to SEKOIA.IO intake servers under SEKOIAIOCheckpointTemplate template
if $hostname == "YOUR_CHECKPOINT_HOSTNAME" then @@(o)intake.sekoia.io:10514;SEKOIAIOCheckpointTemplate
```

In the above `template` instruction, change the `YOUR_CHECKPOINT_HOSTNAME` variable with the correct value, and please replace `YOUR_INTAKE_KEY` variable with your intake key.

### 4. Restart rsyslog

```bash
$ sudo service rsyslog restart
```

## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)

### 5. Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.
