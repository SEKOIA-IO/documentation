# Write an asset connector

An asset connector collects devices, users, applications and vulnerability findings from a product, and keeps them up to date in the asset inventory of Sekoia. This page explains how to write an asset connector your analysts can trust, and how the safeguards of Sekoia catch the mistakes a connector can make.

!!! note
    Asset connectors feed the asset inventory of the [Reveal module](/xdr/features/modules/reveal_index.md). A community needs Reveal to configure one.

## What a good asset connector does

Sekoia gives each asset a [risk score](/xdr/features/modules/asset_risk_scoring.md), which tells analysts which assets need attention first. Its vulnerabilities weigh in that score. A good asset connector keeps both the inventory and the score right:

- **One asset per machine and per account.** It reports each machine and each account with the same identifiers at every run. Otherwise, their vulnerabilities and alerts are split between several assets.
- **The changes, and everything once a week.** Sending only the changes keeps each run light. Sending everything once a week keeps the vulnerabilities that did not change in the risk score, and fills the gaps a failed push left.
- **Fixed findings closed.** Sekoia only knows that a vulnerability is fixed when the connector says so. Otherwise, fixed vulnerabilities stay open in the inventory and keep raising the risk score of their asset.
- **A CVSS score on each finding.** Without one, Sekoia cannot tell how serious a vulnerability is: it shows no severity, and the vulnerability does not count in the risk score.

Sekoia backs each of these practices with a safeguard. When a connector misses one, the safeguard stops the bad data before it reaches your inventory, and the connector receives an error that says why. The safeguards are listed in [Read the push response](#read-the-push-response).

## How an asset connector runs

An asset connector is a Python class based on [`AssetConnector`](https://github.com/SEKOIA-IO/sekoia-automation-sdk/blob/main/sekoia_automation/asset_connector/connector.py) from [sekoia-automation-sdk](https://github.com/SEKOIA-IO/sekoia-automation-sdk). It runs in cycles:

1. The SDK calls `get_assets()`, which yields items.
2. The SDK groups the items into batches of `batch_size` items and pushes each batch to Sekoia.
3. After each accepted push, the SDK calls `update_checkpoint()`.
4. When the cycle yielded no item, the connector waits until `frequency` seconds have passed since the start of the cycle. When it yielded items, the next cycle starts at once.

The checkpoint is where the connector stopped last time, such as the update time of the last machine it sent, so that the next cycle starts from there.

Because a cycle that yields items is followed at once by another one, `get_assets()` must yield only what changed since the checkpoint. See [Send only what changed](#send-only-what-changed).

## Declare the asset connector

An asset connector belongs to a module, next to its actions, triggers and connectors. See [Create a module](create_a_module.md) for the module itself.

```json
my-assets-module/
├── manifest.json  // (1)!
├── connector_machines_assets.json  // (2)!
├── logo.svg  // (3)!
├── main.py  // (4)!
├── pyproject.toml  // (5)!
├── poetry.lock
└── my_assets_module/
    └── connector.py  // (6)!
```

1. The module manifest. The credentials of the product go in its `configuration`, as for any module.
2. The asset connector manifest. Its name starts with `connector_` and ends with `_assets.json`.
3. The logo of the module, required to import it.
4. The entrypoint that registers the asset connector.
5. The dependencies, with a `poetry.lock` file to build the image.
6. The asset connector code.

### The asset connector manifest

```json
{
    "name": "Machines",
    "description": "Collect the machines of My Product",
    "uuid": "9f1bce41-4ae8-4e8b-9a76-c8a12b37c6b1",  // (1)!
    "docker_parameters": "machines_assets",  // (2)!
    "type": "asset",  // (3)!
    "capability": "host_detection",  // (4)!
    "arguments": { … }  // (5)!
}
```

1. A unique UUID.
2. The value that `main.py` registers the asset connector with.
3. `"type": "asset"` marks the file as an asset connector manifest. A file named `connector_*_assets.json` is one even without it.
4. Required. See [Choose the capability](#choose-the-capability).
5. Copy `arguments` as is from the block below. It declares `sekoia_base_url`, `sekoia_api_key`, `frequency` and `batch_size` as internal arguments, which users do not see. Do not fill them in: Sekoia sets the API key and the base URL when a user creates the configuration, and `frequency` and `batch_size` keep the defaults of the SDK, 3 hours and 100 items.

??? example "The `arguments` of an asset connector manifest"

    ```json
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
                "description": "Seconds between two cycles",
                "type": "integer",
                "minimum": 3600
            },
            "batch_size": {
                "description": "Number of items to push in one batch",
                "type": "integer",
                "minimum": 1,
                "default": 100
            }
        },
        "required": ["sekoia_api_key"],
        "secrets": ["sekoia_api_key"],
        "internal": [
            "sekoia_base_url",
            "sekoia_api_key",
            "frequency",
            "batch_size"
        ]
    }
    ```

Custom asset connectors run in the cloud. The import of the module fails at the **Validating integration** step if the manifest declares the `on_premise` execution mode or an `on_premise_action`.

### Choose the capability

The capability says what the connector is for. The integration catalog filters asset connectors on it, and the connector card shows one count chosen from it.

| Capability | Use it when the connector mainly reports | Count on the connector card |
|---|---|---|
| `host_detection` | Machines | Assets |
| `account_detection` | User accounts | Assets |
| `vulnerability_enrichment` | Vulnerability findings | Vulnerabilities |
| `software_enrichment` | Installed applications | Applications |

The capability does not restrict what the connector pushes: a `host_detection` connector can also push the applications and findings of its machines.

### Register the asset connector

```python
from sekoia_automation.module import Module

from my_assets_module.connector import MachinesAssetConnector

if __name__ == "__main__":
    module = Module()
    module.register(MachinesAssetConnector, "machines_assets")  # (1)!
    module.run()
```

1. The second argument is the `docker_parameters` of the asset connector manifest.

### Dependencies

- [sekoia-automation-sdk](https://pypi.org/project/sekoia-automation-sdk/) 1.27.3 or later. From this version, the connector logs the error code of every refused push.
- [sekoia-automation-models 1.5.0](https://github.com/SEKOIA-IO/sekoia-automation-models/releases/tag/v1.5.0) or later, for [`split_hostname()`](https://github.com/SEKOIA-IO/sekoia-automation-models/blob/v1.5.0/sekoia_automation_models/hostname.py). The SDK installs this package; require 1.5.0 explicitly.

## Write the asset connector

A subclass of [`AssetConnector`](https://github.com/SEKOIA-IO/sekoia-automation-sdk/blob/main/sekoia_automation/asset_connector/connector.py) implements four methods:

| Method | What it does |
|---|---|
| `get_assets()` | Yields the items that changed in the product since the checkpoint, oldest first. Yields nothing when nothing changed. |
| `update_checkpoint()` | Saves the position of the last item yielded. The SDK calls it after each accepted push. |
| `reset_checkpoint()` | Clears the checkpoint, so that the next cycle fetches everything again. |
| `get_mapped_fields()` | Returns how product fields map to OCSF fields. When the mapping changes from one version of the connector to the next, the SDK calls `reset_checkpoint()` and the next cycle sends every item again with the new mapping. Return `{}` to turn this off. |

The connector below collects the machines of an imaginary product. For a connector in production, see the [Okta device connector](https://github.com/SEKOIA-IO/automation-library/blob/develop/Okta/okta_modules/asset_connector/device_assets.py) of automation-library, built on `AsyncAssetConnector`, the asynchronous variant of `AssetConnector`.

??? example "A complete asset connector"

    ```python
    import time
    from collections.abc import Generator

    import requests
    from sekoia_automation.asset_connector import AssetConnector
    from sekoia_automation.storage import PersistentJSON
    from sekoia_automation_models.connector import AssetItem
    from sekoia_automation_models.hostname import split_hostname
    from sekoia_automation_models.ocsf.base import Metadata, Product
    from sekoia_automation_models.ocsf.device import (
        Device,
        DeviceOCSFModel,
        DeviceTypeId,
        DeviceTypeStr,
        OperatingSystem,
    )

    METADATA = Metadata(product=Product(name="My Product", vendor_name="My Vendor"), version="1.5.0")


    def to_device(machine: dict) -> Device | None:
        hostname, domain = split_hostname(machine["name"])
        if hostname is None:
            return None  # Not a usable hostname: skip the machine
        return Device(
            type_id=DeviceTypeId.SERVER,
            type=DeviceTypeStr.SERVER,
            uid=machine["id"],
            hostname=hostname,
            domain=domain,
            os=OperatingSystem(name=machine["os"]) if machine.get("os") else None,
        )


    def to_device_item(machine: dict) -> DeviceOCSFModel | None:  # (1)!
        device = to_device(machine)
        if device is None:
            return None
        return DeviceOCSFModel(
            activity_id=2,
            activity_name="Collect",
            category_name="Discovery",
            category_uid=5,
            class_name="Device Inventory Info",
            class_uid=5001,
            type_name="Device Inventory Info: Collect",
            type_uid=500102,
            time=time.time(),
            metadata=METADATA,
            device=device,
        )


    REFRESH_INTERVAL = 7 * 24 * 3600  # (2)!


    class MachinesAssetConnector(AssetConnector):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.context = PersistentJSON("context.json", self.data_path)
            self._last_updated_at: str | None = None
            self._ids_at_last_updated_at: list[str] = []

        def fetch_machines(self, updated_since: str | None) -> Generator[dict, None, None]:  # (3)!
            response = requests.get(
                f"{self.module.configuration['base_url']}/machines",
                headers={"Authorization": f"Bearer {self.module.configuration['api_key']}"},
                params={"updated_since": updated_since, "sort": "updated_at"},
                timeout=30,
            )
            response.raise_for_status()
            yield from response.json()["machines"]

        def get_assets(self) -> Generator[AssetItem, None, None]:
            with self.context as context:
                if time.time() - context.get("refreshed_at", 0) >= REFRESH_INTERVAL:
                    context["refreshed_at"] = time.time()
                    context.pop("last_updated_at", None)
                    context.pop("ids_at_last_updated_at", None)
                since = context.get("last_updated_at")
                self._last_updated_at = since
                self._ids_at_last_updated_at = list(context.get("ids_at_last_updated_at", []))
            pushed_at_since = set(self._ids_at_last_updated_at)

            for machine in self.fetch_machines(updated_since=since):
                if machine["updated_at"] == since and machine["id"] in pushed_at_since:
                    continue  # (4)!
                if machine["updated_at"] != self._last_updated_at:
                    self._last_updated_at = machine["updated_at"]
                    self._ids_at_last_updated_at = []
                self._ids_at_last_updated_at.append(machine["id"])
                if item := to_device_item(machine):
                    yield item

        def update_checkpoint(self) -> None:
            if self._last_updated_at:
                with self.context as context:
                    context["last_updated_at"] = self._last_updated_at
                    context["ids_at_last_updated_at"] = list(self._ids_at_last_updated_at)

        def reset_checkpoint(self) -> None:
            with self.context as context:
                context.pop("last_updated_at", None)
                context.pop("ids_at_last_updated_at", None)

        def get_mapped_fields(self) -> dict[str, str]:
            return {"name": "device.hostname", "os": "device.os.name"}
    ```

    1. Returns `None` for a machine without a usable hostname. See [Report each machine and account once](#report-each-machine-and-account-once).
    2. Once a week, the connector sends every machine again. See [Send only what changed](#send-only-what-changed).
    3. A call to the API of your product, here an imaginary one. It reads the product URL and credentials from the module configuration, and returns the machines updated at or after `updated_since`, sorted by update time, oldest first.
    4. Several machines can share an update time. The checkpoint keeps the IDs already pushed at its update time, so that the next cycle sends the others, and only them.

When `update_checkpoint()` runs, `get_assets()` is paused on the last item of the pushed batch, so `_last_updated_at` is the position of that item.

### Build items with the OCSF models

Build every item with a model of [sekoia-automation-models](https://github.com/SEKOIA-IO/sekoia-automation-models/tree/v1.5.0/sekoia_automation_models/ocsf), from `sekoia_automation_models.ocsf`. Sekoia validates each push against the same models. The SDK also exposes them under `sekoia_automation.asset_connector.models.ocsf`.

| Item | Model | `class_uid` | `category_uid` | `activity_id` | `type_uid` |
|---|---|---|---|---|---|
| Device | [`DeviceOCSFModel`](https://github.com/SEKOIA-IO/sekoia-automation-models/blob/v1.5.0/sekoia_automation_models/ocsf/device.py) | 5001, [Device Inventory Info](https://schema.ocsf.io/classes/inventory_info) | 5, Discovery | 2, Collect | 500102 |
| User | [`UserOCSFModel`](https://github.com/SEKOIA-IO/sekoia-automation-models/blob/v1.5.0/sekoia_automation_models/ocsf/user.py) | 5003, [User Inventory Info](https://schema.ocsf.io/classes/user_inventory) | 5, Discovery | 2, Collect | 500302 |
| Software | [`SoftwareOCSFModel`](https://github.com/SEKOIA-IO/sekoia-automation-models/blob/v1.5.0/sekoia_automation_models/ocsf/software.py) | 5020, [Software Inventory Info](https://schema.ocsf.io/classes/software_info) | 5, Discovery | 2, Collect | 502002 |
| Vulnerability finding | [`VulnerabilityOCSFModel`](https://github.com/SEKOIA-IO/sekoia-automation-models/blob/v1.5.0/sekoia_automation_models/ocsf/vulnerability.py) | 2002, [Vulnerability Finding](https://schema.ocsf.io/classes/vulnerability_finding) | 2, Findings | 1, Create, or 3, Close | 200201 or 200203 |

`type_uid` is `class_uid` × 100 + `activity_id`, and `type_name` is the class name and the activity name, for instance `Device Inventory Info: Collect`.

To see which OCSF fields Sekoia reads for each category, see the [Asset categories overview](/integration/assets_categories/overview.md).

## Guidelines

### Report each machine and account once

An analyst trusts an inventory where each machine is one asset. Two assets for the same machine split its vulnerabilities, its alerts and its risk score in two.

1. Build `hostname` and `domain` with [`split_hostname()`](https://github.com/SEKOIA-IO/sekoia-automation-models/blob/v1.5.0/sekoia_automation_models/hostname.py). It turns `SRV01.corp.example.com` into `srv01` and `corp.example.com`, the way Sekoia stores a hostname.
2. Skip the machine when `split_hostname()` returns no hostname.
3. Report each machine with the same hostname, and each account with the same username or email, at every run.

```python
from sekoia_automation_models.hostname import split_hostname

split_hostname("SRV01.corp.example.com")  # ("srv01", "corp.example.com")
split_hostname("srv01")  # ("srv01", None)
split_hostname("10.0.0.10")  # (None, None): skip the machine
```

`to_device()`, in the complete asset connector of [Write the asset connector](#write-the-asset-connector), uses it to build a device.

!!! info "Safeguard: hostname validation"
    Sekoia rejects an item whose `device.hostname` is a fully qualified name or not a usable hostname. The other items of the push are accepted. Without this check, a machine reported as `srv01.corp.example.com` by your connector and as `srv01` by an agent would become two assets.

#### How a push matches existing assets

A custom asset connector updates the assets your community already has, whatever source created them.

| Item | Matched to | When nothing matches |
|---|---|---|
| Device | The host asset with the same hostname, regardless of case. Revoked assets are excluded. | A new host asset is created. |
| User | The account asset with the same email when the username is an email address, or the same username otherwise. | A new account asset is created. |
| Software | The application with the same name and version, on the host asset with the same hostname as the device the item carries. A software without a name is ignored. | A new application is created. A new version creates a new application. |
| Vulnerability finding | The finding whose CVEs include all the CVEs it carries, or with the same `finding_info.uid` when it has no CVE, on the host asset with the same hostname as the device the finding carries. | A new finding is created. |

Give each software and each finding the device it belongs to, with the same hostname as the device item of that machine. [How a push updates an existing asset](/xdr/features/collect/assets.md#how-a-push-updates-an-existing-asset) says which properties a push overwrites, clears or keeps.

Set a precise `device.type` rather than Unknown or Other, and set `user.type` when the source knows it: Sekoia derives the category of a host or an account from them, and analysts filter on that category in SOL queries. [How an asset gets its category](/xdr/features/collect/assets.md#how-an-asset-gets-its-category) gives the type to category tables, and says when a push leaves the category unchanged.

### Send only what changed

A connector that sends its whole inventory at every cycle sends it again at once, since a cycle that yields items is followed by another one.

1. Fetch only what changed in the product since the checkpoint.
2. Yield nothing when nothing changed, so that the connector waits for `frequency`.
3. Let the SDK group the items into batches of at most 200 items, rather than pushing them one by one. A push keeps only its first 200 items, and drops the others without an error.
4. Send every item again at least once a week, as `REFRESH_INTERVAL` does in [Write the asset connector](#write-the-asset-connector).

The weekly refresh does two things:

- **It keeps your vulnerabilities in the risk score.** A vulnerability counts in the risk score of its asset only while a connector confirmed it in the last 30 days. A connector that sends only what changed would let unchanged vulnerabilities drop out of the score.
- **It recovers the items of a refused push.** After a push refused with an error other than 429, the SDK goes on with the next batch, and a later accepted push saves the checkpoint past the refused items. The refresh sends them again.

A refresh counts in the 24-hour item quota like any other push.

!!! info "Safeguard: rate limits"
    Each configuration has a rate limit on pushes per minute and a quota of items per 24 hours. A connector that loops on its whole inventory reaches them and receives a 429 `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED`, rather than pushing the same items over and over. The connector then pauses for one hour by default, and resumes from its last checkpoint. The values are in [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md).

### Keep items small

Send only the interfaces, groups and accounts that describe the asset. Sekoia keeps the first 10 network interfaces of a device, 20 groups of a user, 20 hashes of a software and 20 references of a vulnerability, and cuts text fields after 1,024 characters. It drops the rest without an error. The values are in [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md).

!!! info "Safeguard: item size"
    An item over the item-size limit is refused with a 413 `ASSET_CONNECTOR_PUSH_TOO_LARGE`. The connector logs the error and goes on with the next batch.

### Keep findings up to date

1. Give each finding a CVSS base score in `vulnerabilities[].cve.cvss`. Without a CVSS score, a finding shows the severity **None** and does not count in the risk score of its asset.
2. Push a finding with the Close activity (`activity_id` 3) when the product reports it fixed. Its status becomes remediated.
3. Push it again without Close if the product reports it again. Its status becomes open.

A push never changes a status a user set, such as accepted risk or false positive.

### Push the findings that matter

Filter the findings in the connector code before pushing them, for instance by CVSS score, or by known exploitation when the product reports it. Your inventory and the risk scores then reflect the vulnerabilities your analysts act on.

??? example "Push only the findings with a CVSS base score of 7.0 or more"

    ```python
    from sekoia_automation_models.ocsf.vulnerability import VulnerabilityOCSFModel


    def is_worth_sending(finding: VulnerabilityOCSFModel) -> bool:
        return any(
            cvss.base_score is not None and cvss.base_score >= 7.0
            for vulnerability in finding.vulnerabilities
            if vulnerability.cve
            for cvss in vulnerability.cve.cvss or []
        )
    ```

!!! info "Safeguard: vulnerability caps"
    An asset stores a limited number of vulnerabilities, so that a noisy product cannot bury the findings that matter under thousands of minor ones. Findings over the cap are not stored, and nothing warns about it: filtering keeps your connector under the cap. The values are in [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md).

### Let storage limits catch a runaway connector

A bug can make a connector create a new asset at every run, or never close its findings. Storage limits stop such a connector before it fills your inventory with duplicate and stale data.

!!! info "Safeguard: storage limits"
    Each configuration and each community can store a limited number of active assets, active applications and open findings, in proportion to the number of assets included in the community subscription. The community also has lifetime limits on everything it ever stored. When a limit is reached, every push of the configuration receives a 429 `ASSET_CONNECTOR_LIMIT_REACHED`, and `detail.limits` names the reached limit. The connector pauses, and pushes again once usage is back under the limit. See [Storage limits for custom asset connectors](/xdr/features/modules/reveal_asset_connectors_limits.md#storage-limits-for-custom-asset-connectors).

A connector that follows [Report each machine and account once](#report-each-machine-and-account-once) and [Keep findings up to date](#keep-findings-up-to-date) stays far from the active and open-finding limits.

Lifetime limits are different: they count every asset, application and finding your community ever stored, including closed findings and the data of deleted configurations. They decrease only when assets are revoked: a revoked asset, its applications and its findings are no longer counted. Before you collect a product whose assets come and go, such as short-lived cloud instances, check that its volume over time fits these limits.

### Keep the SDK up to date

The SDK sets the version of the push format, the same for every push of the connector. Update `sekoia-automation-sdk` as soon as a new release comes out.

!!! info "Safeguard: push format version"
    Sekoia refuses a push in a format version it does not support with a 400 `ASSET_CONNECTOR_UNSUPPORTED_VERSION`, instead of accepting it and dropping its data. Since every push of the connector carries the same version, every push is refused and the checkpoint does not move: nothing is lost. Update the SDK, and the next cycle sends the items again from the checkpoint.

## Read the push response

From `sekoia-automation-sdk` 1.27.3, every refused push appears in the connector logs with its response code and error code. A 200 means that Sekoia accepted the push, not that it processed every item: when the processing fails, the connector logs `Asset push task <id> ended with the status <status>` as an error. Find the logs in the asset connectors panel: see [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md#diagnose-push-errors).

| Response | Safeguard | Fix in the connector |
|---|---|---|
| 200 with `rejected` | Hostname validation: the listed items were rejected, the others accepted | Build hostnames with `split_hostname()` |
| 422 | Hostname validation: every item was rejected | Build hostnames with `split_hostname()` |
| 400 `ASSET_CONNECTOR_UNSUPPORTED_VERSION` | Push format version | Update `sekoia-automation-sdk` |
| 413 `ASSET_CONNECTOR_PUSH_TOO_LARGE` | Item size | Send fewer interfaces, groups or accounts per item |
| 429 `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED` | Rate limits | Send only what changed |
| 429 `ASSET_CONNECTOR_LIMIT_REACHED` | Storage limits | Find what creates duplicate assets or leaves findings open |

`rejected` lists up to 50 rejected items, each with its `index` in the push, the `field`, the `value` and the `reason`. The connector logs a push with rejected items as a success: check your hostnames with `split_hostname()` before pushing, rather than relying on this list.

## Example

This connector pushes fixed items, with no product behind it: two machines, three accounts, two applications and four findings. It shows how to build each item, a finding without a CVSS score, and a finding closed by the product.

??? example "connector.py"

    ```python
    import time
    from collections.abc import Generator
    from typing import NamedTuple

    from sekoia_automation.asset_connector import AssetConnector
    from sekoia_automation_models.connector import AssetItem
    from sekoia_automation_models.ocsf.base import Metadata, Product
    from sekoia_automation_models.ocsf.device import (
        Device,
        DeviceOCSFModel,
        DeviceTypeId,
        DeviceTypeStr,
        OperatingSystem,
        OSTypeId,
        OSTypeStr,
    )
    from sekoia_automation_models.ocsf.risk_level import RiskLevelId, RiskLevelStr
    from sekoia_automation_models.ocsf.software import (
        SoftwareBillOfMaterials,
        SoftwareEnrichmentObject,
        SoftwareOCSFModel,
        SoftwarePackage,
    )
    from sekoia_automation_models.ocsf.user import (
        Account,
        AccountTypeId,
        AccountTypeStr,
        User,
        UserOCSFModel,
        UserTypeId,
        UserTypeStr,
    )
    from sekoia_automation_models.ocsf.vulnerability import (
        CVE,
        CVSS,
        FindingInformation,
        VulnerabilityDetails,
        VulnerabilityOCSFModel,
    )

    METADATA = Metadata(product=Product(name="Sample Custom Asset Connector", vendor_name="Sekoia"), version="1.5.0")

    SERVER = Device(
        type_id=DeviceTypeId.SERVER,
        type=DeviceTypeStr.SERVER,
        uid="sample-device-server-01",
        hostname="sample-server-01",
        os=OperatingSystem(name="Ubuntu 22.04", type=OSTypeStr.LINUX, type_id=OSTypeId.LINUX),
        ip="10.0.0.10",
    )
    UNKNOWN_DEVICE = Device(
        type_id=DeviceTypeId.UNKNOWN,
        type=DeviceTypeStr.UNKNOWN,
        uid="sample-device-unknown-01",
        hostname="sample-unknown-01",
    )


    def windows_user(uid: str, name: str, user_type: UserTypeStr, full_name: str | None = None) -> User:
        return User(
            uid=uid,
            name=name,
            full_name=full_name,
            email_addr=f"{name}@example.com" if full_name else None,
            type_id=UserTypeId[user_type.name],
            type=user_type,
            account=Account(name=name, type_id=AccountTypeId.WINDOWS_ACCOUNT, type=AccountTypeStr.WINDOWS_ACCOUNT),
        )


    USERS = [
        windows_user("sample-user-01", "sample.user", UserTypeStr.USER, "Sample User"),
        windows_user("sample-admin-01", "sample.admin", UserTypeStr.ADMIN, "Sample Admin"),
        windows_user("sample-service-01", "svc-sample", UserTypeStr.SERVICE),
    ]


    def software_on_server(name: str, version: str, cpe: str | None = None) -> tuple:
        return (
            SoftwareEnrichmentObject(name=name, version=version, vendor_name="Sample Corp"),
            SoftwarePackage(name=name, version=version, cpe_name=cpe),
        )


    SOFTWARE = [
        software_on_server("sample-agent", "1.4.0", "cpe:2.3:a:sample_corp:sample_agent:1.4.0:*:*:*:*:*:*:*"),
        software_on_server("sample-tool", "2.1.0"),
    ]


    class Activity(NamedTuple):
        id: int
        name: str


    INVENTORY_COLLECT = Activity(2, "Collect")
    FINDING_CREATE = Activity(1, "Create")
    FINDING_CLOSE = Activity(3, "Close")


    def ocsf_event_fields(
        class_name: str, class_uid: int, category_name: str, category_uid: int, activity: Activity
    ) -> dict:
        """The fields every OCSF item carries: its type is its class and its activity"""
        return {
            "activity_id": activity.id,
            "activity_name": activity.name,
            "category_name": category_name,
            "category_uid": category_uid,
            "class_name": class_name,
            "class_uid": class_uid,
            "type_name": f"{class_name}: {activity.name}",
            "type_uid": class_uid * 100 + activity.id,
            "time": time.time(),
            "metadata": METADATA,
        }


    def inventory_fields(class_name: str, class_uid: int) -> dict:
        return ocsf_event_fields(class_name, class_uid, "Discovery", 5, INVENTORY_COLLECT)


    def finding_on_server(
        uid: str,
        title: str,
        cve: str,
        cvss: float | None,
        activity: Activity = FINDING_CREATE,
        risk_level: RiskLevelStr | None = None,
    ) -> VulnerabilityOCSFModel:
        return VulnerabilityOCSFModel(
            **ocsf_event_fields("Vulnerability Finding", 2002, "Findings", 2, activity),
            device=SERVER,
            finding_info=FindingInformation(uid=uid, title=title, desc=f"{title}, pushed by the sample connector"),
            vulnerabilities=[
                VulnerabilityDetails(
                    title=title,
                    cve=CVE(uid=cve, cvss=[CVSS(version="3.1", base_score=cvss)] if cvss is not None else None),
                )
            ],
            risk_level=risk_level,
            risk_level_id=RiskLevelId[risk_level.name] if risk_level else None,
        )


    def findings() -> list[VulnerabilityOCSFModel]:
        return [
            finding_on_server("sample-finding-with-cvss", "Finding with a CVSS", "CVE-2099-0001", 7.5),
            # Shows the severity None and does not count in the risk score
            finding_on_server("sample-finding-without-cvss", "Finding without a CVSS", "CVE-2099-0002", None),
            # A level without a numeric risk score, as some products send it
            finding_on_server(
                "sample-finding-critical",
                "Finding the vendor rates Critical",
                "CVE-2099-0003",
                9.8,
                risk_level=RiskLevelStr.CRITICAL,
            ),
            # Pushed with the Close activity: shows as remediated
            finding_on_server(
                "sample-finding-closed", "Finding closed by the vendor", "CVE-2099-0004", 5.3, activity=FINDING_CLOSE
            ),
        ]


    class SampleAssetConnector(AssetConnector):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._pushed_at: float | None = None

        def get_assets(self) -> Generator[AssetItem, None, None]:
            # Yield nothing until `frequency` has passed, so that the connector waits between two pushes
            now = time.time()
            if self._pushed_at is not None and now - self._pushed_at < self.frequency:
                return
            self._pushed_at = now

            for device in (SERVER, UNKNOWN_DEVICE):
                yield DeviceOCSFModel(**inventory_fields("Device Inventory Info", 5001), device=device)
            for user in USERS:
                yield UserOCSFModel(**inventory_fields("User Inventory Info", 5003), user=user)
            for software, package in SOFTWARE:
                yield SoftwareOCSFModel(
                    **inventory_fields("Software Inventory Info", 5020),
                    device=SERVER,
                    software=software,
                    sbom=SoftwareBillOfMaterials(package=package),
                )
            yield from findings()

        def update_checkpoint(self) -> None:
            """The data is fixed: nothing to remember between two pushes"""

        def reset_checkpoint(self) -> None:
            """No checkpoint to reset"""

        def get_mapped_fields(self) -> dict[str, str]:
            return {}
    ```

??? example "main.py"

    ```python
    from sekoia_automation.module import Module

    from sample_asset_connector.connector import SampleAssetConnector

    if __name__ == "__main__":
        module = Module()
        module.register(SampleAssetConnector, "sample_assets")
        module.run()
    ```

The CVEs of the example (`CVE-2099-*`) are reserved, and its applications are unknown to the NVD: the asset views show only what the connector pushed.

## Related articles

- [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md): Rate limits, caps and storage limits.
- [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md#diagnose-push-errors): Push errors and the action for each.
- [Create asset connectors](/xdr/features/modules/reveal_asset_connectors_create.md): How a user configures an asset connector.
- [Asset categories overview](/integration/assets_categories/overview.md): The OCSF fields Sekoia reads for each category.
- [How an asset gets its category](/xdr/features/collect/assets.md#how-an-asset-gets-its-category): The category a device type or a user type gives an asset.
