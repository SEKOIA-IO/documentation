# Map asset connector data to asset categories

Reveal asset connectors derive the category of the hosts and accounts they push from Open Cybersecurity Schema Framework (OCSF) values. This reference lists these mappings, the account properties that connectors set, the rules that decide when a connector applies a category, and how a push updates an existing asset.

!!! note "Reveal"
    Asset connectors require the [Reveal](/xdr/features/modules/reveal_index.md) add-on module. For the categories you can select in the asset form, see [Asset categories](/xdr/features/collect/assets.md#asset-categories).

## Host category mapping

An asset connector reads the category of a host from the OCSF [`device.type`](https://schema.ocsf.io/1.5.0/objects/device) field.

| OCSF `device.type` | Category | API value |
| --- | --- | --- |
| Desktop | Desktop | `desktop` |
| Server | Server | `server` |
| Mobile | Mobile | `mobile` |
| Virtual | Virtual | `virtual` |
| Firewall | Firewall | `firewall` |
| Switch | Switch | `switch` |
| Unknown | No category | None |
| Other | No category | None |

A connector never assigns the Phone, Unknown, or Other host categories. You can select them only in the asset form.

## Account category mapping

An asset connector reads the category of an account from the OCSF [`user.type`](https://schema.ocsf.io/1.5.0/objects/user) field.

| OCSF `user.type` | Category | API value |
| --- | --- | --- |
| User | User | `user` |
| Admin | User | `user` |
| Service | Service Account | `service_account` |
| System | System account | `system_account` |
| Unknown, or no type | No category | None |

An account pushed with the Admin user type receives the `user` category, because Admin describes a right that the account holds in one source system, not a kind of account. The connector records this right in the [`is_admin`](#account-properties-set-by-asset-connectors) property.

The OCSF [`user.account.type`](https://schema.ocsf.io/1.5.0/objects/account) field, such as LDAP Account or Windows Account, does not affect the category. It identifies the system that the account comes from and is stored in the [`user_type`](#account-properties-set-by-asset-connectors) property.

!!! note "`system_account` and `system`"
    The `system_account` category exists only on accounts categorized by an asset connector, and the asset list displays it as `system_account`. It is a different value from the System category (`system`), which you select in the asset form.

## Category precedence

The following table shows when an asset connector applies the mapped category.

| Asset processed by the connector | Category applied |
| --- | --- |
| Host or account created by the connector | The mapped category. |
| Host created from a software item | None. |
| Existing account with no category | The mapped category. |
| Existing host with no category | None. Set the category in the asset form. |
| Existing host or account with a category | None. The existing category is kept, including a category selected in the asset form. |

## Account properties set by asset connectors

Among the contextual properties that an asset connector sets on an account, two relate to its category.

| Property | Value |
| --- | --- |
| `is_admin` | `True` when the account is pushed with the OCSF user type Admin, `False` otherwise. |
| `user_type` | The OCSF `user.account.type` value, such as LDAP Account, Windows Account, or Azure AD Account. It identifies the source system and does not change the category. |

## How a push updates an existing asset

When an item an asset connector pushes matches an existing asset, the push updates the asset as follows.

!!! note "Locked properties"
    When automatic asset discovery changes a property of an asset more than 5 times in an hour, Sekoia locks the property. A push neither overwrites nor clears a locked property. The property stays locked until a user edits it.

| Item | Properties | When the push carries a value | When the push leaves it empty |
|---|---|---|---|
| Device | OS (`device.os.name`, `device.os.type`, `device.os.type_id`), location (`device.location.city`, `device.location.country`), device type (`device.type_id`), IP address (`device.ip`, or the IP of the primary interface), MAC address, organization (`device.org.name`), firewall status | Overwrites the stored value | Clears the stored value |
| Device | Other `device` fields, such as `device.name`, `device.desc` or `device.domain` | Overwrites the stored value | Keeps the stored value |
| Device | Interfaces (`device.network_interfaces`), groups (`device.groups`), partitions, accounts | Replaces the stored list | Keeps the stored list |
| User | Account type (`user.account.type`, `user.account.type_id`), organization (`user.org.name`), and the user data of `enrichments`: enabled, last logon, last password change, bad password count, number of logons, external device | Overwrites the stored value | Clears the stored value |
| User | Administrator status, from `user.type` | Set at every push | Set to not administrator |
| User | Other `user` fields, such as `user.full_name`, `user.display_name` or `user.ldap_person` | Overwrites the stored value | Keeps the stored value |
| User | Groups (`user.groups`) | Replaces the stored list | Keeps the stored list |

## Related articles

- [Assets](/xdr/features/collect/assets.md): Overview of asset types, categories, criticality, and asset properties.
- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): How to configure a Reveal asset connector.
- [Asset connector health status and logs](/xdr/features/collect/asset_connector_health.md): How to monitor connector synchronization and inspect connector logs.
- [Understand passive asset discovery](/xdr/features/modules/reveal_asset_discovery.md): Overview of how Reveal creates and enriches assets from telemetry.
- [Asset connector overview](/integration/assets_categories/overview.md): Reference for the available asset connectors and their source categories.
