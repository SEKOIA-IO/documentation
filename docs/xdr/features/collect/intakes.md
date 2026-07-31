# Intakes

Intakes are data source connections that forward logs to Sekoia for centralized security monitoring. Each intake is identified by a name, a format, an entity, and an intake key.

## What is an intake

An intake represents a single data source feeding logs into Sekoia. It acts as the entry point for log collection, linking a specific technology (such as a firewall, endpoint agent, or cloud service) to a Sekoia entity.

You can create as many intakes as your infrastructure requires. Two organization strategies are available:

- **One intake per technology**: a single intake collects logs from all devices of the same type within an entity (for example, all Fortigate firewalls in a given entity)
- **One intake per device**: a dedicated intake is created for each individual device

Both strategies are valid. The right choice depends on how granular you need your monitoring and reporting to be.

All intake management features are accessible through the **Intakes** menu in the Operations Center.

## How intakes connect to Sekoia

Intakes collect logs in two ways:

- **Push intakes**: your infrastructure sends logs directly to Sekoia using the intake key as an authentication token
- **Pull intakes**: Sekoia runs a connector that actively fetches logs from your data source on a defined schedule

Pull intakes expose additional features not available for push intakes, including connector configuration parameters and connector execution logs.

## Event types

Each ingested event receives one of the following statuses based on how it was processed by the parsing pipeline.

### Valid events

A valid event was successfully received and parsed by Sekoia. It is available for detection, correlation, and investigation.

### Invalid events

An event is invalid when its data does not match the expected format (JSON, Key-value, Grok, Date, or Delimiter-separated value). Invalid events are not parsed and are not available for detection.

### Events in warning

An event generates a warning in the following cases:

- The parsing succeeded but no data was extracted. This is not an error, but may indicate an unexpected configuration.
- Some values were incompatible with their expected data type and could not be extracted.

Warning events are parsed but may be missing fields, which can affect detection quality.

## Why monitoring intakes matters

An intake that stops sending events creates blind spots in your security coverage. Sekoia provides two mechanisms to stay informed:

- **Event delivery metrics**: available on the intake details page, these indicators let you assess whether events are arriving within expected timeframes
- **Inactivity notifications**: configurable alerts that trigger when an intake has not received events for a set period

Monitoring both regularly helps ensure your data collection remains healthy and your detection coverage stays complete.

## Related articles

- [Intake details page](/xdr/features/collect/intakes_details.md): Reference for all metrics, indicators, and menu options available on the intake details page, including a full explanation of the event delivery metric.

- [Manage intakes](/xdr/features/collect/manage_intakes.md): Step-by-step procedures for creating, configuring, renaming, and deleting intakes.

- [Turn on notifications](/getting_started/notifications-Listing_Creation.md): How to configure notification channels and triggers for intake inactivity alerts.

- [Integrations](/integration/index.md): Full catalog of supported data source integrations and their setup documentation.
