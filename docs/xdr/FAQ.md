# IP

## Is the IP behind `intake.sekoia.io` static?

**IP for `intake.sekoia.io` is `51.159.9.95`.**

`intake.sekoia.io` is the domain name used to send your logs to Sekoia.io, either via Syslog or HTTP protocols. The IP address behind that service is static and stable. You can use that IP to configure your firewalls to allow connections from your forwarding systems to Sekoia.io.

## Outgoing IP addresses for playbooks runs and connectors


For all the actions available in the Playbooks section of Sekoia.io (include connectors used to retrieve logs from external sources), we use a number of outbound IP addresses. The full list is publicly accessible and can be retrieved at the following URL: [https://api.sekoia.io/outgoing-ips](https://api.sekoia.io/outgoing-ips). This will be useful to setup filtering options if needed, and even automate any future update.

We try to make this list as stable as possible, but events out of our control may result in modifications. If any changes occur, we are committed to providing our customers with advance notice of at least two weeks, either via a dedicated communication, or via our [status page](https://status.sekoia.io/).


## How to debug Rsyslog’s forward configuration to Sekoia.io?

If you use Rsyslog to forward your logs to Sekoia.io, you will probably have a section like this in your configuration files:

```
template(name="SEKOIAIOUnboundTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"jOK5bMVXz5Iz7gfogQDbCcC7l7S2IrOs5\"] %msg%\n")
if $programname startswith 'unbound' then @@(o)intake.sekoia.io:10514;SEKOIAIOUnboundTemplate

```

If you want to retrieve the raw data that is forwarded to Sekoia.io, you can duplicate the last line and make Rsyslog dump logs to a local file:

```
if $programname startswith 'unbound' then /tmp/nginx-output.log;SEKOIAIOUnboundTemplate
```

This way, you will be able to exactly identify what data is sent to Sekoia.io.


```
# tail -n 1 /tmp/nginx-output.log
<30>1 2021-01-13T14:52:06.934860+01:00 ote unbound - LOG [SEKOIA@53288 intake_key="jOK5bMVXz5Iz7gfogQDbCcC7l7S2IrOs5"]  [596451:0] info: 127.0.0.1 intake.sekoia.io. A IN
```


# Logs
## Retention
Logs are available and displayed for 90 days in Sekoia.io.

## Archiving & Rehydratation
Please contact your support for more information on archives and events rehydratation, with a clear description of your needs.

## Ingestion

### Datetime representation

SEKOIA.IO accepts two kind of representations of a datetime in the events:

- as a string with a timezone (like ISO8601 or RFC3339 strings)
- as a timestamp (from the seconds to the nanoseconds representation) or as a string without a timezone, in the UTC timezone
