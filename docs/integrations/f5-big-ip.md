uuid: a14b1141-2d61-414b-bf79-da99b487b1af
name: F5 BIG-IP

## Overview

F5's BIG-IP is a family of products covering software and hardware designed around application availability, access control, and security solutions.

## Setup

We expect logs formated in priority as CEF, and encapsulated in a syslog message including your intake key, to be sent on `intake.sekoia.io:10514` using the following certificate: [`SEKOIA-IO-intake.pem`](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem). The other reporting format (key/value pairs) is also supported, but the required configuration will note be detailed in the following example.

In this setup guide you will set up an rsyslog server to add your intake key and forward securely your BIG-IP logs to our servers. We first explain how to configure your rsyslog server, then we show how to configure a *Log Publisher* to format your logs as CEF and send them to your rsyslog server.

Most BIG-IP modules can use Log Publishers, some can directly log messages as CEF to an rsyslog server.

On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### 1. Configure the Rsyslog server

In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

You can now configure your Rsyslog server to forward your logs to SEKOIA.IO.

Open or create a new configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/22-big-ip.conf
```

Then paste the following configuration:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver, make sure rsyslog-gnutls is installed
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOBigIpTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# send the logs corresponding to a given module, as an example for ASM:
if $programname startswith 'ASM' then @@(o)intake.sekoia.io:10514;SEKOIAIOBigIpTemplate
```

In the above `template` instruction, adapt the line corresponding to your use case in the last block, and please replace `YOUR_INTAKE_KEY` variable with your intake key.

Restart rsyslog:
```bash
$ sudo service rsyslog restart
```

### 2. Configure a Log Publisher

Before creating a log publisher, you first need a *management port* log destination:
```
System -> Logs -> Configuration -> Log Destinations -> Create...
```
Give it a name, choose type `Management Port`, fill the address and port of your rsyslog server and select protocol UDP
(alternatively you can define a pool of rsyslog servers and use it as a remote high speed log destination).

Then you need another log destination to format your logs in CEF:
```
System -> Logs -> Configuration -> Log Destinations -> Create...
```
Give it a name, choose type `ArcSight`, and forward to the log destination you just created.

You can now create a log publisher:
```
System -> Logs -> Configuration -> Log Publishers -> Create...
```
Give it a name, and select the ArcSight log destination you just created.

You can now use this log publisher to define logging profiles in your BIG-IP modules. As an example in:
```
Access -> Overview -> Event Logs -> Settings -> Create -> Access System Logs -> Publisher
```
or
```
Security -> Event Logs -> Logging Profiles -> Create... -> Publisher
```


### 3. Direct Configuration

Some modules allow direct configuration to the rsyslog server. As an example:
```
Security -> Event Logs -> Logging Profiles -> Create...
```
Then choose `Application Security`, select `Remote Storage` as a storage destination, `Common Event Format (ArcSight)` as a logging format, and fill in your rsyslog server info.

The resulting logging profile can be applied to a given virtual server in:
```
Local Traffic -> Virtual Servers -> Virtual Server List
```
Then choose a virtual server, go to the `Security -> Policies` tab and apply the log profile.


## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)

### 4. Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.
