# IP

## Is the IP behind `intake.sekoia.io` static?

**IP for `intake.sekoia.io` is `51.159.9.95`.**

`intake.sekoia.io` is the domain name used to send your logs to SEKOIA.IO, either via Syslog or HTTP protocols. The IP address behind that service is static and stable. You can use that IP to configure your firewalls to allow connections from your forwarding systems to SEKOIA.IO.

## IP behind Triggers available in Playbooks Section

For all our triggers available in our Playbooks section, used to retrieve your logs, we use `141.95.157.224`. This IP will be useful to setup filtering if needed.

## How to debug Rsyslog’s forward configuration to SEKOIA.IO?

If you use Rsyslog to forward your logs to SEKOIA.IO, you will probably have a section like this in your configuration files:

```
template(name="SEKOIAIOUnboundTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"jOK5bMVXz5Iz7gfogQDbCcC7l7S2IrOs5\"] %msg%\n")
if $programname startswith 'unbound' then @@(o)intake.sekoia.io:10514;SEKOIAIOUnboundTemplate

```

If you want to retrieve the raw data that is forwarded to SEKOIA.IO, you can duplicate the last line and make Rsyslog dump logs to a local file:

```
if $programname startswith 'unbound' then /tmp/nginx-output.log;SEKOIAIOUnboundTemplate
```

This way, you will be able to exactly identify what data is sent to SEKOIA.IO.


```
# tail -n 1 /tmp/nginx-output.log
<30>1 2021-01-13T14:52:06.934860+01:00 ote unbound - LOG [SEKOIA@53288 intake_key="jOK5bMVXz5Iz7gfogQDbCcC7l7S2IrOs5"]  [596451:0] info: 127.0.0.1 intake.sekoia.io. A IN
```


# Events

## What happens when you add events to an alert? 
When you attach events to an alert, there are two mechanisms that are executed in parallel: alert generation and events externalisation.
Some latency might happen between alert generation and attaching events to an alert.

## Event search request on IP range
You can easily request an event search on IP range. For instance, with an IP address starting with 145, you can search by range as follow: `source.ip:[145.0.0.0 TO 145.255.255.255]`. 

## timestamp, event.created, event.start, event.end meaning

**timestamp** and **event.created** are the same (reception of logs and beginning of processing in SEKOIA.IO).

**event.created** is parsed and can be selected. The timezone is defined with UTC.

**event.start**   contains the date when the event started or when the activity was first observed.

**event.end**   contains the date when the event ended or when the activity was last observed.

**event.start** & **event.end** are activity and monitoring of the event (Pre-SEKOIA.IO if not producedd by SEKOIA.IO)

`event.start` <= `event.end` <= `event.created`


# Alerts

## Alert date

When an alert is triggered, additional events can enrich this alert but the date of the alert will not updated (date= 1st trigger). 

## Bell icon in alerts page

The bell icon means that "the event is involved in an alert". 

When a bell on an event is displayed on an alert page, the event is involved in the current alert AND in another alert.

If it is involved in the current alert, the bell is not displayed.

## How an alert is triggered with a delay ?

Besides matching a rule in real time, an alert can be triggered with a delay when: 
    - An IOC is published, old events are scanned and if an event matches, the rule will automatically trigger an alert. 
    - Reingesting old logs

