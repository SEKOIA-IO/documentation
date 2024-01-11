# Ingestion Methods

In order to protect your business, you need to know what happens. The monitoring of your assets is a prerequisite to their security.

This chapter details the ingestion methods to integrate Sekoia.io into your ecosystem.

Sekoia.io is able to collect logs through various mechanisms, configuration on your side should be easy! Here is an overview on how integration could be done with Sekoia.io.

![ingestion_methods](/assets/operation_center/data_collection/ingestion_methods/ingestion_methods2.png){: style="max-width:100%"}

Sekoia.io supports the following log collecting methods:

- [HTTPS](./https/overview.md) (`https://intake.sekoia.io`): `POST` your JSON events to Sekoia.io.
- [Syslog](./syslog/overview.md) over TLS (`intake.sekoia.io:10514`): forward your events with the Syslog protocol specified in RFC 5424.
- [RELP](./syslog/rsyslog.md#how-to-forward-logs-to-sekoiaio-using-relp) over TLS (`relp.intake.sekoia.io:11514`): forward your events with Rsyslog’s reliable protocol called RELP.
- [Cloud hosting and API polling](./cloud_saas/overview.md): configure Sekoia.io to regularly retrieve your logs.

If these solutions do not meet your needs, contact our support.

## Syslog / Relp integration

To send your data to Sekoia.io using the Syslog or Relp protocols, you need to add a header to each of your messages.
We provide documentation and example configurations on how to configure your log system for Rsyslog, but it should be easy to configure other log collectors to forward their events to Sekoia.io.

## HTTPS integration

To push your events through our HTTP log collector, you have to `POST` your logs in the JSON format. To send us events, you should set `Content-Type` HTTP header to `application/json`.

## Cloud & SaaS integration

Sekoia.io is also able to retrieve logs and data from cloud platforms, such as Microsoft Azure, Amazon Web Services or Google Cloud.

## Datetime representation in the events

Sekoia.io accepts any representation of a datetime; see [Datetime representation](../../../FAQ/datetime.md) for more details.
