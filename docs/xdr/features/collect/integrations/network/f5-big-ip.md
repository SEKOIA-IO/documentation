uuid: a14b1141-2d61-414b-bf79-da99b487b1af
name: F5 BIG-IP
type: intake

## Overview

F5's BIG-IP is a family of products covering software and hardware designed around application availability, access control, and security solutions.

{!xdr/features/collect/integrations/generated/f5-big-ip_do_not_edit_manually.md!}

## Configure

We expect logs formated in priority as CEF or under the reporting format (key/value pairs).

In this setup guide you will set up an rsyslog server to add your intake key and forward securely your BIG-IP logs to our servers. We first explain how to configure your rsyslog server, then we show how to configure a *Log Publisher* to format your logs as CEF and send them to your rsyslog server.

Most BIG-IP modules can use Log Publishers, some can directly log messages as CEF to an rsyslog server.

### Configure a Log Publisher

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


### Direct Configuration

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

### Rsyslog

Please consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
