# Understand passive asset discovery

Passive Asset Discovery is a Reveal capability that creates and enriches assets from the identifiers found in your telemetry. This article explains how it identifies assets through atoms, which rules create and enrich assets, and which limits apply.

## Before you begin

Passive Asset Discovery requires the following conditions:

- The [Reveal](/xdr/features/modules/reveal_index.md) add-on module is enabled for your community.
- Sekoia receives supported telemetry that contains asset identifiers.

You do not need to enable Passive Asset Discovery. It starts as soon as Sekoia receives supported telemetry.

## Compare discovery sources

Reveal builds a single asset inventory from several sources. When two sources identify the same asset, Reveal merges them into one record.

| Source | How it creates or enriches assets | Use it when |
| --- | --- | --- |
| Passive Asset Discovery | Finds identifiers in events and creates, merges, and lightly enriches assets from them. | Your event coverage is good, but no external inventory is connected. It also reveals assets that no other system registers. |
| Asset connector | Imports structured data from an external system, such as an EDR, cloud platform, CMDB, or vulnerability scanner. | An authoritative source exists for your assets and you need accurate, complete attributes. |

The two sources complement each other: Passive Asset Discovery provides coverage, and asset connectors provide authoritative attributes. See [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md).

## Understand atoms

Events contain two kinds of fields: fields that describe what happened, such as a failed SSH authentication, and fields that identify the resources involved, such as a user, a computer, or a remote server. These resources rarely appear as clean asset identifiers. They appear as traces such as IP addresses, FQDNs, or email addresses.

Reveal calls these identifying values **atoms**. An asset can have several atoms, but each atom identifies only one asset within a given entity at a given time. For example:

- The atom `192.168.1.2` identifies the host `DESKTOP-123` in the entity `DMZ-1` on January 1, 2023.
- `Windows XP` is not an atom, because many hosts can run the same operating system. It is a contextual property.

Some atoms are exclusive identifiers. For example, an Active Directory user has exactly one Windows SID.

![Tracked atoms](/assets/operation_center/assets_v2/atoms-list.png){align="center", style="max-width:100%"}

Reveal tracks atoms even when the asset they identify is not fully qualified:

- The asset timeline keeps the history of atom-to-asset associations. Changes such as DHCP leases that move an IP address from one host to another remain available for historical investigations.
- Activity is tracked at the atom level. Events about `192.168.1.2` stay linked to that atom, even when it identifies different assets over time. The asset details page shows the weekly activity of a selected atom.

Atoms are similar to the observables of the Intelligence Center, but they serve another purpose. Atoms identify resources in your supervised environment, while observables are threat intelligence objects that can become Indicators of Compromise (IoCs).

### Tracked atoms

| Atom type | Related event fields |
| --- | --- |
| IPv4 | `client.ip`, `destination.ip`, `host.ip`, `server.ip`, `source.ip`, `related.ip` |
| IPv6 | `client.ip`, `destination.ip`, `host.ip`, `server.ip`, `source.ip`, `related.ip` |
| Hostname | `host.name`, `host.hostname`, `related.host`, `client.name`, `server.name`, `log.hostname` |
| FQDN | `dns.question.name`, `client.domain`, `client.registered_domain`, `destination.domain`, `destination.registered_domain`, `source.domain`, `source.registered_domain`, `server.domain`, `server.registered_domain`, `tls.client.x509.alternative_names`, `url.domain`, `url.registered_domain`, `x509.subject.common_name`, `x509.alternative_names`, `user.domain`, `related.host` |
| Username | `user.name`, `user.full_name`, `related.user`, `client.user.name` |
| Email | `client.user.email`, `destination.user.email`, `file.x509.alternative_names`, `host.user.email`, `server.user.email`, `source.user.email`, `tls.client.x509.alternative_names`, `user.email`, `user.changes.email`, `user.effective.email`, `user.target.email`, `x509.alternative_names`, `email.from.address`, `email.to.address` |
| SID | `user.id`, `related.user`, `client.user.id` |

!!! warning "Hostname validation"
    A hostname is valid only if it contains at least one letter, contains only letters, numbers, hyphens, and underscores, and is not a valid domain. Reveal does not create an asset from an invalid hostname.

!!! warning "SID validation"
    A `sid` detection property is only taken from a Windows security identifier (`S-1-...`). Other values of these fields, such as GUIDs, claims, or application identifiers, are ignored, as are the well-known SIDs shared by every Windows host.

## Understand discovery rules

### Attach an operating system to a host

This rule sets the `os` contextual property on an existing host. It takes the value from the operating system fields of events whose `host.name` matches the host's `hostname` detection property.

### Attach EDR agent IDs to a host

This rule sets an EDR agent ID contextual property, such as `sentinelone_agent_id`, from the `agent.id` event field. It applies only to hosts, and a host can have several EDR agent IDs.

### Discover unique hosts

This rule creates a host for each `host.name` value not seen before. It suggests the IPv4 and IPv6 addresses in the `host.ip` field as detection properties of the new host.

The rule ignores:

- Events whose `event.outcome` or `action.outcome` is `failure`, such as a failed authentication, because a client can send any device name before it is authenticated. Such an event neither creates a host nor updates an existing one.
- Placeholder names such as `unknown`, `n/a`, `null`, or `localhost`.

### Discover unique accounts

This rule creates an account for each `user.name` value not seen before. It adds the `user.email` and `user.id` values of the event as detection properties of the new account.

The rule does not create an account in the following cases:

| Case | Examples |
| --- | --- |
| The event did not succeed, or the name may come from an attacker. | An `event.outcome` or `action.outcome` other than `success`. An intrusion detection event, where `event.category` contains `intrusion_detection`. |
| Windows uses the account itself rather than a person. | Accounts that Windows creates and removes for Hyper-V virtual machines, services, IIS application pools, and OpenSSH sessions. Built-in or special-purpose accounts such as `DefaultAccount`, `WDAGUtilityAccount`, `IUSR`, or `krbtgt`. |
| The name is a placeholder or a generic name. | `n/a`, `null`, `undefined`, `root`, `admin`, `administrator`, `guest`, `test`. |
| The user field lists several people. | The collaborators of a shared document, where nothing indicates which name goes with which email. |

## Discovery limits

!!! note "Daily discovery limit"
    Passive Asset Discovery creates at most 10,000 hosts and 20,000 accounts per community and per day (UTC). Above this limit, Reveal drops the new hosts and accounts found in events. It creates them on a later day only if events identify them again. Assets already in the inventory continue to be updated.

    This limit does not apply to a community whose first asset is less than 90 days old, so that a new community can build its inventory.

## Related articles

- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md): How to configure the data sources that power Reveal.
- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md): Reference for the data sources required by each Reveal capability.
- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): How to configure a connector that enriches assets from an external system.
- [Map asset connector data to asset categories](/xdr/features/modules/reveal_asset_connector_category_mapping.md): Reference for the categories and properties assigned by asset connectors.
- [Assets](/xdr/features/collect/assets.md): Overview of asset types, categories, criticality, and asset properties.
- [Assets FAQ](/xdr/FAQ/Assets_qa.md): Reference for frequently asked questions about discovered assets.
