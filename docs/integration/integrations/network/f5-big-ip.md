uuid: a14b1141-2d61-414b-bf79-da99b487b1af
name: F5 BIG-IP
type: intake

## Overview

F5's BIG-IP is a family of products covering software and hardware designed around application availability, access control, and security solutions.

## Supported events

This integration supports the events from the following F5 Big-IP modules:

- ASM
- APM
- LTM
- AFM
- PSM

{!_shared_content/operations_center/detection/generated/suggested_rules_a14b1141-2d61-414b-bf79-da99b487b1af_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/a14b1141-2d61-414b-bf79-da99b487b1af.md!}

## Configure

We expect logs formated in priority as CEF or under the reporting format (key/value pairs).

In this setup guide you will forward securely your BIG-IP logs to our servers. We first explain how to configure your syslog concentrator, then we show how to configure a *Log Publisher* to format your logs as CEF and send them to your syslog concentrator.

Most BIG-IP modules can use Log Publishers, some can directly log messages as CEF to a syslog server.

### Set up the concentrator

Please consult the [Syslog Forwarding](../../../../ingestion_methods/sekoiaio_forwarder/) documentation to set up the concentrator that will forward your logs to Sekoia.io.

### Configure a Log Publisher

Before creating a log publisher, you first need a *management port* log destination:
```
System -> Logs -> Configuration -> Log Destinations -> Create...
```
Give it a name, choose type `Management Port`, fill the address and port of your syslog concentrator and select protocol UDP
(alternatively you can define a pool of syslog servers and use it as a remote high speed log destination).

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

Some modules allow direct configuration to the syslog concentrator. As an example:
```
Security -> Event Logs -> Logging Profiles -> Create...
```
Then choose `Application Security`, select `Remote Storage` as a storage destination, `Common Event Format (ArcSight)` as a logging format, and fill in your syslog concentrator info.

The resulting logging profile can be applied to a given virtual server in:
```
Local Traffic -> Virtual Servers -> Virtual Server List
```
Then choose a virtual server, go to the `Security -> Policies` tab and apply the log profile.
