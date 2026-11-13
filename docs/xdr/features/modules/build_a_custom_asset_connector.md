# Build a custom asset connector

_**[Reveal module](/xdr/features/modules/reveal_index.md)** — This feature requires the Reveal add-on module._ 

This article explains how to build a custom asset connector that sends valid data and keeps your inventory free of duplicate assets. It applies to custom asset connectors only: connectors your community creates and runs.

## Before you begin

- The Reveal add-on module is enabled for your community.
- You have Python 3.11 or later and the `sekoia-automation-sdk` package.
- You use `sekoia-automation-models` 1.5.0 or later.

## Step 1: Set up the custom integration

1. Create the integration that will hold the asset connector. See [Create your own integration](/xdr/features/collect/integrations_hub.md#create-your-own-integration).
2. Add the asset connector to the integration.
3. Import the integration into your community.
4. Check that the import passes the **Validating integration** step.

A community can own up to 10 custom integrations that contain an asset connector. Over this number, the import fails at the **Validating integration** step.

## Step 2: Build valid connector items

1. Build every item with an OCSF model of `sekoia-automation-models`: `DeviceOCSFModel`, `UserOCSFModel`, `SoftwareOCSFModel` or `VulnerabilityOCSFModel`.
2. Send the items in an `AssetList`.

Sekoia validates each push against the same models.

## Step 3: Normalize hostnames

1. Build `hostname` and `domain` with `split_hostname()`.
2. Skip a device when `split_hostname()` returns no hostname.

`split_hostname()` applies the hostname rule of Sekoia. A device without a usable hostname would be rejected.

## Step 4: Send items in batches

1. Group items into batches instead of sending them one by one.
2. Keep each item under the item-size limit.
3. Filter findings in the connector code before sending them, for instance by CVSS score, or by known exploitation when the source reports it.

??? example "send only the findings with a CVSS base score of 7.0 or more"

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

Each configuration has a rate limit on pushes per minute and a 24-hour item quota. The values are in [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md).

## Step 5: Keep findings up to date

1. Send a finding with the Close activity when the source reports it fixed. Its status becomes remediated.
2. Send the finding again without Close if the source reports it again. Its status becomes open.

A push never changes a status a user set, such as accepted risk or false positive.

## Step 6: Plan for storage limits

1. Close fixed findings, so that open findings stay under their limit.
2. Send each machine and account with the same hostname or username at every run, so that each one updates a single asset.

Each configuration and each community can store a limited number of active assets, active applications and open findings. The limits follow the number of assets your community subscribed. When a configuration reaches a storage limit, every push of the configuration receives a 429 `ASSET_CONNECTOR_LIMIT_REACHED`. See [Storage limits for custom asset connectors](/xdr/features/modules/reveal_asset_connectors_limits.md#storage-limits-for-custom-asset-connectors).

## How pushed data is matched

A custom asset connector updates the assets your community already has, whatever source created them.

| Item | Matched to | When nothing matches |
|---|---|---|
| Device | The host asset with the same `hostname` [detection property](/xdr/features/collect/assets.md#detection-properties), regardless of case. Revoked assets are excluded. | A new host asset is created. |
| User | The account asset with the same email when the username is an email address, or the same username otherwise. | A new account asset is created. |
| Vulnerability finding | The finding of the same asset whose CVEs include all the CVEs it carries, or with the same `finding_info.uid` when it has no CVE. | A new finding is created. |

When an item matches an asset:

- Each property the item carries overwrites the stored value.
- Empty core properties of a device, such as OS, IP address or MAC address, clear the stored value.
- Interfaces, groups, partitions and accounts the item carries replace the stored ones. When the item carries none, the stored ones are kept.

## Related articles

- [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md#diagnose-push-errors): Push errors and the action for each.
- [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md): Rate limits, caps and storage limits.
- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): How to configure an asset connector from the integration catalog.
