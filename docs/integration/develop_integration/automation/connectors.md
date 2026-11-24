# Connectors

A connector is Python code that Sekoia runs on a recurring basis to collect data from an external product. It is a component of a [module](module.md), next to actions and triggers.

There are two types of connectors:

* **Event connectors** collect events, such as logs and alerts, and send them to an intake.
* **Asset connectors** collect assets, such as devices, users, software and vulnerabilities, and send them to the asset inventory.

## Choose the type of connector

| | Event connector | Asset connector |
|---|---|---|
| Collects | Events: logs, alerts, audit trails | Assets: devices, users, software, vulnerability findings |
| Sends data to | An intake, with its intake key | The asset inventory, through the Asset API |
| Data format | Raw events, parsed by the [intake format](../formats/overview.md) | Structured [OCSF](https://schema.ocsf.io) items, with no parsing |
| Base class | `sekoia_automation.connector.Connector` | `sekoia_automation.asset_connector.AssetConnector` |
| Configured from | An intake that uses the format of the connector | **Configure > Asset connectors**, with the Reveal add-on module |
| Descriptor | `connector_<name>.json`, generated from the code | `connector_<name>.json` with `"type": "asset"` and a `capability`, written by hand |

A module can contain both types. For instance, a module for an EDR can have an event connector for its alerts and an asset connector for the devices it manages.

## Event connectors

An event connector inherits from `Connector`. Its configuration inherits from `DefaultConnectorConfiguration`, which carries the `intake_key` of the intake that receives the events. The connector loops while `self.running` is true, fetches new events and sends them with `push_events_to_intakes()`.

To build one step by step, see the **Event connector** tab of [Create a module](create_a_module.md#create-your-component).

## Asset connectors

An asset connector synchronizes the inventory of an external product into the [asset inventory](/xdr/features/collect/assets.md) of a community. Assets from several sources are merged into a single asset when they share the same identifiers, such as the hostname of a device.

!!! note
    Asset connectors require the [Reveal add-on module](/xdr/features/modules/reveal_index.md).

### Requirements

* Python 3.11 or later.
* `sekoia-automation-sdk` 1.27.3 or later.
* `sekoia-automation-models` 1.5.0 or later, pinned in `pyproject.toml`. The SDK accepts older versions, which miss `split_hostname()`.

The OCSF models live in the `sekoia-automation-models` package. Import them from `sekoia_automation.asset_connector.models.ocsf`, which re-exports them.

### What the SDK does for you

The `AssetConnector` base class runs the connector. On each cycle, it:

1. Calls your `get_assets()` and groups the items it yields into batches of `batch_size` items.
2. Pushes each batch to the Asset API, then waits for Sekoia to process it.
3. Calls your `update_checkpoint()` after each push that Sekoia accepts.
4. Waits for `frequency` seconds before the next cycle when the cycle found no asset.

Do not batch, push or retry the pushes yourself.

Use `AsyncAssetConnector` instead of `AssetConnector` only when the client of the product is asynchronous.

### Implement the connector

Implement four methods:

| Method | What it does |
|---|---|
| `get_assets()` | A generator that fetches assets from the product and yields one OCSF model per item. Stream the items: do not load the whole inventory in memory. Stop the loops when `self.running` becomes false. |
| `update_checkpoint()` | Saves the progress of the connector, so that the next cycle fetches only what changed. Do nothing when nothing changed. |
| `reset_checkpoint()` | Clears every value `update_checkpoint()` saves. The SDK calls it when `get_mapped_fields()` changes, so that the next cycle fetches the whole inventory again with the new mapping. |
| `get_mapped_fields()` | Returns `{source field: OCSF field}` for every field the connector maps. Change it whenever the mapping changes. |

Read the credentials of the product from `self.module.configuration`. Never log them.

### Save progress with a checkpoint

A checkpoint is the point up to which the connector has collected data, such as the most recent modification date it has seen. Store it in a `PersistentJSON` file with a name unique within the module.

The checkpoint decides whether the inventory stays free of duplicates and gaps:

* **Advance the checkpoint only after a complete run of `get_assets()`.** The SDK calls `update_checkpoint()` after each accepted push, while `get_assets()` is still running. Only keep a new value in memory once the run is complete; otherwise, a run that stops halfway skips the items it did not reach.
* **Use the most recent date seen, not the current time.** Choose a field that changes when the asset changes, such as a modification date, not a creation date.
* **Keep the checkpoint format across versions.** When you rename a key or change the format of a date, read the old value and convert it. A lost checkpoint sends the whole inventory again.
* **Skip the items you cannot send, but count them.** Log a warning for an item that fails validation and continue with the next one. Let errors of the API of the product raise, so that the cycle stops.

After an exception, the SDK starts the next cycle at once, without waiting. A connector that fails on every cycle can quickly reach the rate limits of the Asset API.

### Build the OCSF items

Each item is an OCSF model. Set the classification fields from this table, and `type_uid` = `class_uid` × 100 + `activity_id`.

| Asset type | Model | `class_name` | `class_uid` | `category_name` (`category_uid`) | `activity_id` | `capability` |
|---|---|---|---|---|---|---|
| Device | `DeviceOCSFModel` | Device Inventory Info | 5001 | Discovery (5) | 2 (Collect) | `host_detection` |
| User | `UserOCSFModel` | User Inventory Info | 5003 | Discovery (5) | 2 (Collect) | `account_detection` |
| Software | `SoftwareOCSFModel` | Software Inventory Info | 5020 | Discovery (5) | 2 (Collect) | `software_enrichment` |
| Vulnerability | `VulnerabilityOCSFModel` | Vulnerability Finding | 2002 | Findings (2) | 1 (Create), 2 (Update) or 3 (Close) | `vulnerability_enrichment` |

Set `metadata` to the product you collect from and the OCSF version: `1.5.0` for inventory classes, `1.6.0` for vulnerability findings. Time fields are Unix timestamps, in seconds.

Never set a field that the model does not have. Read the [models](https://github.com/SEKOIA-IO/sekoia-automation-models/tree/main/sekoia_automation_models/ocsf) for the list of fields.

=== "Devices"

    * Build `hostname` and `domain` with `split_hostname()` from `sekoia_automation_models.hostname`: `hostname` gets the short name, and `domain` the rest. For instance, `SRV01.corp.example.com` gives `srv01` and `corp.example.com`.
    * Skip a device when `split_hostname()` returns no hostname. Never use the IP address or the identifier of the product as the hostname.
    * Set `type_id` and `type` to a type Sekoia accepts: Unknown (0), Server (1), Desktop (2), Mobile (5), Virtual (6), Firewall (9), Switch (10) or Other (99). Map a laptop to Desktop and a router to Other.
    * Set `vendor_name` to the maker of the hardware, not to the product you collect from.

=== "Users"

    * Set `username` to the login of the account, `email` to its email address, and `uid_alt` to the directory identifier, such as the `sAMAccountName`. Never put an email address in `username`.
    * Skip the Active Directory accounts whose name ends with `$`: they are machine accounts.
    * Skip groups, sharing links and other principals that are not accounts.

=== "Software"

    * Give each software a name and a version.
    * Give it the device it runs on, with the same hostname as the device connector sends.

=== "Vulnerabilities"

    * Give each finding the device it affects, with the same hostname as the device connector sends.
    * Put one CVE identifier in each `cve.uid`.
    * Set `activity_id` from the status in the product: 1 (Create) for a new finding, 2 (Update) for a finding reported again, 3 (Close) for a fixed finding. A closed finding becomes remediated.
    * Set `time` to an integer.
    * Keep each item small: cap the number of CVEs and do not copy the same long description into each CVE.

The same hostname in every connector of the module lets Sekoia merge their data into one asset. To see which fields Sekoia uses for each type, see the [asset categories](../../assets_categories/overview.md).

### Declare the connector

`sekoia-automation generate-files-from-code` does not generate the descriptor of an asset connector. Write `connector_<vendor>_<type>_assets.json` at the root of the module:

```json
{
  "name": "TestHTTP Devices",
  "description": "Fetch TestHTTP device assets",
  "uuid": "8a7acb0b-0004-5e17-9ab0-4c110cea795b",  // (1)!
  "docker_parameters": "testhttp_device_asset_connector",  // (2)!
  "type": "asset",  // (3)!
  "capability": "host_detection",  // (4)!
  "arguments": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "sekoia_base_url": {
        "description": "Sekoia base URL",
        "type": "string"
      },
      "sekoia_api_key": {
        "description": "API key to use from sekoia.io",
        "type": "string"
      },
      "frequency": {
        "description": "Batch frequency in seconds",
        "type": "integer",
        "minimum": 10800,
        "default": 86400
      },
      "batch_size": {
        "description": "Number of assets to process in one batch",
        "type": "integer",
        "minimum": 1,
        "maximum": 200,
        "default": 100
      }
    },
    "required": ["sekoia_api_key"],
    "secrets": ["sekoia_api_key"],
    "internal": ["sekoia_base_url", "sekoia_api_key", "frequency", "batch_size"]  // (5)!
  }
}
```

1. A new UUID, unique to this connector. Never change it once the connector is released.
2. The name the connector is registered with in `main.py`. Never change it once the connector is released.
3. Identifies the component as an asset connector.
4. The type of asset the connector collects: `host_detection`, `account_detection`, `software_enrichment` or `vulnerability_enrichment`. Sekoia stores it when the connector is created, so choose it before the first release.
5. Sekoia fills in these arguments: users do not see them.

Register the connector in `main.py`, with the same name as `docker_parameters`:

```python
from sekoia_automation.module import Module

from testhttp_modules.asset_connector.device_assets import TesthttpDeviceAssetConnector

if __name__ == "__main__":
    module = Module()
    module.register(TesthttpDeviceAssetConnector, "testhttp_device_asset_connector")
    module.run()
```

The credentials of the product go in the `configuration` of the module [manifest](module.md#the-manifest).

### Test the connector

Test at least:

* The mapping of a sample of the API to OCSF items, with anonymised data.
* Pagination, including an empty page.
* The checkpoint: a second run sends only what changed, and `reset_checkpoint()` clears everything.
* A `null` value in the API response, which must not make a whole page fail.
* An error of the API of the product.

### Examples

These modules of the [automation library](https://github.com/SEKOIA-IO/automation-library) contain asset connectors you can start from:

| Asset type | Module |
|---|---|
| Devices, vulnerabilities | [HolmSecurity](https://github.com/SEKOIA-IO/automation-library/tree/develop/HolmSecurity/holm_security/asset_connector) |
| Users | [MicrosoftEntraID](https://github.com/SEKOIA-IO/automation-library/tree/develop/MicrosoftEntraID/azure_ad/asset_connector), [Okta](https://github.com/SEKOIA-IO/automation-library/tree/develop/Okta/okta_modules/asset_connector) |
| Software | [HarfangLab](https://github.com/SEKOIA-IO/automation-library/tree/develop/HarfangLab/harfanglab/asset_connector) |

## Related articles

- [Create a module](create_a_module.md): Build an event connector or an asset connector step by step.
- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): Configure an asset connector from the integration catalog.
- [Check asset connector health](/xdr/features/collect/asset_connector_health.md): Monitor the runs of an asset connector.
- [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md): Find why an asset connector fails.
