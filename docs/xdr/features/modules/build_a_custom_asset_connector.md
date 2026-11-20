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

1. Build every item with an OCSF model of [`sekoia-automation-models`](https://github.com/SEKOIA-IO/sekoia-automation-models/tree/v1.5.0/sekoia_automation_models/ocsf): `DeviceOCSFModel`, `UserOCSFModel`, `SoftwareOCSFModel` or `VulnerabilityOCSFModel`.
2. Send the items in an `AssetList`.

Sekoia validates each push against the same models. An item updates the asset your community already has for it, whatever source created that asset. Steps 4 to 7 say how each type of item is matched. [How a push updates an existing asset](/xdr/features/collect/assets.md#how-a-push-updates-an-existing-asset) says which properties a push overwrites, clears or keeps.

## Step 3: Send items in batches

1. Group items into batches of at most 200 items instead of sending them one by one. Sekoia drops the items after the 200th of a push, without an error.
2. Keep each item under the [item-size limit](/xdr/features/modules/reveal_asset_connectors_limits.md#rate-limits-and-caps-for-every-asset-connector) of 900 KB.

Each configuration has a rate limit on pushes per minute and a 24-hour item quota. The values are in [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md).

## Step 4: Send devices

1. Build `hostname` and `domain` with [`split_hostname()`](https://github.com/SEKOIA-IO/sekoia-automation-models/blob/v1.5.0/sekoia_automation_models/hostname.py), from `sekoia_automation_models.hostname`. For instance, `SRV01.corp.example.com` gives `srv01` and `corp.example.com`.
2. Skip a device when `split_hostname()` returns no hostname.
3. Send each machine with the same hostname at every run.

`split_hostname()` applies the hostname rule of Sekoia. A device without a usable hostname would be rejected.

A device updates the host asset with the same `hostname` [detection property](/xdr/features/collect/assets.md#detection-properties), regardless of case. Revoked assets are excluded. When none matches, a new host asset is created.

## Step 5: Send users

1. Send each account with the same username at every run.

A user updates the account asset with the same email when its username is an email address, or with the same username otherwise. When none matches, a new account asset is created.

## Step 6: Send software

1. Give each software a name. A software without a name is ignored.
2. Give it the device it runs on, with the same hostname as in Step 4.

A software updates the application of the host asset with the same name and version. The host asset is the one with the same `hostname` as the device the item carries. A new version creates a new application.

## Step 7: Send vulnerability findings

A vulnerability finding is a vulnerability that the source reports on one asset.

1. Give each finding the device it affects, with the same hostname as in Step 4.
2. Filter findings in the connector code before sending them, for instance by CVSS score, or by known exploitation when the source reports it.
3. Send a finding with the Close activity when the source reports it fixed. Its status becomes remediated.
4. Send the finding again without Close if the source reports it again. Its status becomes open.

??? example "Send only the findings with a CVSS base score of 7.0 or more"

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

A push never changes a status a user set, such as accepted risk or false positive.

A finding updates the finding of the same asset whose CVEs include all the CVEs it carries, or with the same `finding_info.uid` when it has no CVE. The asset is the one with the same `hostname` as the device the finding carries. When none matches, a new finding is created.

## Step 8: Plan for storage limits

1. Close fixed findings, so that open findings stay under their limit.
2. Keep the hostnames and usernames of Steps 4 and 5 stable, so that each machine and account updates a single asset.

Each configuration and each community can store a limited number of active assets, active applications and open findings. The limits follow the number of assets your community subscribed. When a configuration reaches a storage limit, every push of the configuration receives a 429 `ASSET_CONNECTOR_LIMIT_REACHED`. See [Storage limits for custom asset connectors](/xdr/features/modules/reveal_asset_connectors_limits.md#storage-limits-for-custom-asset-connectors).

## Related articles

- [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md#diagnose-push-errors): Push errors and the action for each.
- [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md): Rate limits, caps and storage limits.
- [Assets](/xdr/features/collect/assets.md#how-a-push-updates-an-existing-asset): How a push updates the properties of an existing asset.
- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): How to configure an asset connector from the integration catalog.
