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

## Archive and restore data

!!! Info
    
    Depending on your plan we can archive your data and restore it on demand
    
    Option not available for all plans


### Restoration process : 

- The request must be made to [support@sekoia.io](mailto:support@sekoia.io)

- We try to restore in less than 48 working hours

- The data requested must be less than 12 months old (the end date of the requested period must be less than 365 days)

- Restored data will be deleted after 30 days

### Restoration flow:

<img style="max-width:100%" alt="Archiving diagram" src="/xdr/FAQ/archiving_process.png">