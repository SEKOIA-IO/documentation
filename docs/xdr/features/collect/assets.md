# Assets

Assets are the hosts, accounts, and networks that represent the systems and identities in your environment. This article describes the asset model shared by all Sekoia SOC platform users: asset types, categories, criticality, and the properties that link assets to events.

## Asset management

Sekoia uses assets to add identity and business context to events, alerts, and investigations. When you know which systems and accounts an activity involves, and how important they are, you can assess its impact and prioritize your response.

You can create assets manually from the **Assets** page. If your community has the [Reveal](/xdr/features/modules/reveal_index.md) add-on module, Reveal can also create and enrich assets from telemetry and external systems. See [Understand passive asset discovery](/xdr/features/modules/reveal_asset_discovery.md) and [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md).

![Asset details](/assets/operation_center/assets_v2/assets-details.png){align="center", style="max-width:100%"}

## Asset types

Every asset has one type. You set the type when you create the asset, and it does not change afterward.

| Type | API value | Description |
| --- | --- | --- |
| Host | `host` | A machine, such as a workstation, server, phone, virtual machine, or network appliance. |
| Account | `account` | An identity that signs in, such as a person, a service, or a machine. |
| Network | `network` | A network. A network asset has no category. |

## Asset categories

A host or an account can also have a category that describes what kind of host or account it is. The category is optional and can change over time. The **API value** column shows the value that the API and SOL queries return.

### Host categories

| Category | API value |
| --- | --- |
| Desktop | `desktop` |
| Server | `server` |
| Mobile | `mobile` |
| Phone | `phone` |
| Virtual | `virtual` |
| Firewall | `firewall` |
| Switch | `switch` |
| Unknown | `unknown` |
| Other | `other` |

### Account categories

| Category | API value |
| --- | --- |
| User | `user` |
| Admin | `admin` |
| Service Account | `service_account` |
| Machine Account | `machine_account` |
| System | `system` |
| Unknown | `unknown` |

These tables list the categories you can select in the asset form. Reveal asset connectors assign some of these categories, and they can also assign the `system_account` category, which the asset form does not offer. See [Map asset connector data to asset categories](/xdr/features/modules/reveal_asset_connector_category_mapping.md).

## Criticality

Criticality is a value from 0 to 100 that indicates how important an asset is to your organization. A value of 0 means that the asset has no assigned criticality, and a value of 100 marks the most critical assets.

Criticality contributes to the [urgency score of alerts](/xdr/features/investigate/alerts.md). Set it on the assets that matter most so that alerts involving them are prioritized.

## Asset risk score

!!! note "Reveal"
    The asset risk score requires the [Reveal](/xdr/features/modules/reveal_index.md) add-on module.

The asset risk score indicates the current security risk associated with an asset. It combines persistent exposure and recent activity, then adjusts the result with a criticality factor. A criticality of 0 has no effect on the score.

Criticality describes how important an asset is. The risk score describes the security risk that currently affects it.

| Band | Score range |
| --- | --- |
| Low | 0 to 24 |
| Moderate | 25 to 49 |
| High | 50 to 74 |
| Critical | 75 to 100 |

Use the [`asset_risk_scores`](/xdr/features/investigate/sol_ref_datasources.md#asset_risk_scores) SOL data source to query the current score, and `asset_risk_score_history` to analyze the events that changed the score over time. See [Asset risk scoring](/xdr/features/modules/asset_risk_scoring.md) for how the score is calculated.

## Asset properties

Sekoia uses two kinds of properties: detection properties identify an asset in events, and contextual properties describe it.

### Detection properties

![Detection properties](/assets/operation_center/assets_v2/detection-properties.png){align="right", style="max-width:40%"}

Detection properties are the values that identify an asset in event fields, such as an IP address, a hostname, or an email address. When an event matches a detection property, Sekoia adds the asset UUID to the event and enriches the event with the asset's contextual properties, including its criticality.

Matching is case-insensitive.

!!! note "Detection property limits"
    An asset can hold up to 50 detection properties of one type, such as 50 IPv4 addresses or 50 SIDs. When an asset reaches this limit, Sekoia ignores new detection properties of that type that are added automatically and keeps the existing ones.

    A detection property that you add manually is always accepted. If the asset is at the limit, it replaces the oldest automatically added property of the same type.

    An asset with more than 1,000 detection properties in total receives no new automatic detection properties.

### Contextual properties

![Contextual properties](/assets/operation_center/assets_v2/context-properties.png){align="right", style="max-width:50%"}

Contextual properties add information to an asset without being used to match events. They can contain names, labels, descriptions, owners, locations, or custom identifiers.

Sekoia provides a default set of contextual properties for each asset type. You can also create custom contextual properties. When you do, follow these practices:

- Use a consistent naming convention, such as `location`, `owner`, or `department`, across all assets.
- Add only properties that serve a clear operational need.
- Review values regularly so that they stay accurate.
- Do not store passwords, financial data, or other confidential information.
- Choose values that the features consuming them can use, such as detection, reporting, and compliance.

## Related articles

- [Manage assets](/xdr/features/collect/manage_assets.md): How to review the asset inventory, apply bulk actions, and create assets manually.
- [Investigate assets](/xdr/features/investigate/investigate_assets.md): How to use assets in detection rules, alert filters, and investigations.
- [Alerts](/xdr/features/investigate/alerts.md): Overview of alerts, including how asset criticality contributes to the urgency score.
- [SOL technical reference: data sources](/xdr/features/investigate/sol_ref_datasources.md): Reference for the asset data sources, including `asset_risk_scores` and `asset_risk_score_history`.
- [Asset risk score query examples](/xdr/features/investigate/sol_query_examples.md#asset-risk-score-query-examples): Reference for SOL queries that report on asset risk scores and the events that drive them.
- [Asset risk scoring](/xdr/features/modules/asset_risk_scoring.md): Overview of how Reveal calculates the asset risk score.
- [Understand passive asset discovery](/xdr/features/modules/reveal_asset_discovery.md): Overview of how Reveal creates and enriches assets from telemetry.
- [Map asset connector data to asset categories](/xdr/features/modules/reveal_asset_connector_category_mapping.md): Reference for the categories and properties that Reveal asset connectors assign.
- [Assets FAQ](/xdr/FAQ/Assets_qa.md): Reference for frequently asked questions about assets.
