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
