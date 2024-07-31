# Ingestion Methods

In order to protect your business, you need to know what happens. The monitoring of your assets is a prerequisite to their security.

This chapter details the ingestion methods to integrate Sekoia.io into your ecosystem.

Sekoia.io is able to collect logs through various mechanisms, configuration on your side should be easy! Here is an overview on how integration could be done with Sekoia.io.

![ingestion_methods](/assets/operation_center/data_collection/ingestion_methods/ingestion_methods3.png){: style="max-width:100%"}

Sekoia.io supports the following log collecting methods:

- [HTTPS](/integration/ingestion_methods/https/overview/) (`https://intake.sekoia.io`): `POST` your JSON events to Sekoia.io.
- [Syslog](/integration/ingestion_methods/syslog/overview/) over TLS (`intake.sekoia.io:10514`): forward your events with the Syslog protocol specified in RFC 5424.
- [RELP](/integration/ingestion_methods/syslog/syslog_service/#how-to-forward-logs-to-sekoiaio-using-relp) over TLS (`relp.intake.sekoia.io:11514`): forward your events with Rsyslog’s reliable protocol called RELP.
- [Cloud hosting and API polling](/integration/ingestion_methods/cloud_saas/overview/): configure Sekoia.io to regularly retrieve your logs.

If these solutions do not meet your needs, contact our support.

## Syslog / Relp integration

To send your data to Sekoia.io using the Syslog or Relp protocols, you need to add a header to each of your messages.

Here is an example of your message before the forwarder
```
<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG RAW_MESSAGE
```
and after
```
<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] RAW_MESSAGE
```

We provide [documentation and example configurations](/integration/ingestion_methods/syslog/overview/) on how to configure your log system for Rsyslog, syslog-ng or use our [Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder/, but it should be easy to configure other log collectors to forward their events to Sekoia.io.

## HTTPS integration

To push your events through our [HTTPS log collector](/integration/ingestion_methods/https/overview/), you have to `POST` your logs in the JSON format. To send us events, you should set `Content-Type` HTTP header to `application/json`.

## Cloud & SaaS integration

Sekoia.io is also able to retrieve logs and data from [Cloud platform](/integration/ingestion_methods/cloud_saas/overview/), such as Microsoft Azure, Amazon Web Services or Google Cloud.

## Datetime representation in the events

Sekoia.io accepts any representation of a datetime; see [Datetime representation](/xdr/FAQ/datetime/) for more details.
