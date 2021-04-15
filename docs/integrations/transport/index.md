# SEKOIA.IO Log Collector Transports

SEKOIA.IO supports multiple log collectors:

- Syslog over TLS (`intake.sekoia.io:10514`): you can forward your events by using the Syslog protocol specified in RFC 5424.
- RELP over TLS (`intake.sekoia.io:11514`): your can forward your events by using Rsyslog’s reliable protocol called RELP.
- HTTPS (`https://intake.sekoia.io`): you can `POST` your JSON events.

This makes SEKOIA.IO compatible with a large number of product and solutions to collect your logs.

Even if Rsyslog is the most supported solution to push your logs to SEKOIA.IO, you can use other solutions, such as Logstash, syslog-ng, Graylog, etc.

## Syslog integration

We are providing documentation and example configurations on how to configure your log system for Rsyslog, but it should be easy to configure other log collectors to forward their events to SEKOIA.IO.

## HTTPS integration

To push your events through our HTTP log collector, you have to `POST` your logs in the JSON format. To send us events, you should set `Content-Type` HTTP header to `application/javascript`.

## Log Aggregator Configuration

- [Rsyslog][rsyslog.md]
- [Logstash][logstash.md]
- [syslog-ng][syslog-ng.md]
