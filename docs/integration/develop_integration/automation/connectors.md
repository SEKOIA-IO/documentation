# Connectors

A connector is Python code that Sekoia runs on a recurring basis to collect data from an external product. It is a component of a [module](module.md), next to actions and triggers.

There are two types of connectors:

* **Event connectors** collect events, such as logs and alerts, and send them to an intake.
* **Asset connectors** collect assets, such as machines, user accounts, applications and vulnerability findings, and send them to the asset inventory.

A module can contain both types. For instance, a module for an EDR can have an event connector for its alerts and an asset connector for the machines it manages.

## Choose the type of connector

| | Event connector | Asset connector |
|---|---|---|
| Collects | Events: logs, alerts, audit trails | Assets: machines, user accounts, applications, vulnerability findings |
| Sends data to | An intake, with its intake key | The asset inventory |
| Data format | Raw events, parsed by the [intake format](../formats/overview.md) | Structured [OCSF](https://schema.ocsf.io) items, with no parsing |
| Base class | `sekoia_automation.connector.Connector` | `sekoia_automation.asset_connector.AssetConnector` |
| Manifest | `connector_<name>.json`, generated from the code | `connector_<name>_assets.json`, with `"type": "asset"` and a `capability` |
| Configured from | An intake that uses the format of the connector | The integration catalog, with the [Reveal module](/xdr/features/modules/reveal_index.md) |

## Event connectors

An event connector inherits from `Connector`. Its configuration inherits from `DefaultConnectorConfiguration`, which carries the `intake_key` of the intake that receives the events. Its `iterate()` method yields the new events of the product, and the SDK pushes them to the intake.

To declare, write and test one, see [Build an event connector](event_connector.md).

## Asset connectors

An asset connector inherits from `AssetConnector`. It synchronizes the inventory of an external product into the [asset inventory](/xdr/features/collect/assets.md) of a community. Assets from several sources are merged into a single asset when they share the same identifiers, such as the hostname of a machine.

To declare, write and test one, see [Build an asset connector](asset_connector.md).

## Related articles

- [Create a module](create_a_module.md): Set up a module and its components.
- [Build an event connector](event_connector.md): Write an event connector and keep it from losing or duplicating events.
- [Build an asset connector](asset_connector.md): Write an asset connector and follow the practices that keep the asset inventory reliable.
- [Create asset connectors](/xdr/features/modules/reveal_asset_connectors_create.md): Configure an asset connector from the integration catalog.
