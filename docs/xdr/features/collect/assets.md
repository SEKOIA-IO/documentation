# Assets

In the context of IT and cyber infrastructure, an asset is any individual component or resource that is part or interact with the information technology system.
These assets can vary widely and may include physical devices, software applications, data, virtual machines, network equipment, and more.
Each asset plays a specific role in the functioning of the IT infrastructure and contributes to the overall network ecosystem.

Sekoia.io offers various features to manage your assets and use them to empower your detection and investigation scenarios. This documentation details these features.

## Asset Management Empowers your SOC Team

Assets play a pivotal role in empowering your SOC team to effectively safeguard your organization's IT infrastructure from cyber threats and respond proactively to security incidents.
The comprehensive understanding of assets offered by Sekoia.io enables your SOC team to gain vital visibility into the defended perimeter, monitoring all components with ease and precision.

![assets-details](/assets/operation_center/assets_v2/assets-details.png){align="center", style="max-width:100%"}

By categorizing assets based on their criticality, Sekoia.io support the prioritization of all the alert management efforts and resources, focusing on protecting the most valuable elements and reducing overall risk exposure.

Furthermore, assets serve as the basis for threat detection and incident response. With knowledge of normal behavior patterns for each asset, SOC analysts can swiftly detect anomalies and deviations, alerting them to potential security threats. Armed with this information, you can take decisive actions by isolating affected assets and mitigating damage to prevent further compromise.

In alert investigations, assets serve as valuable reference points, allowing SOC analysts to trace attack paths, identify compromised assets, and assess the extent of a breach. This information guides effective mitigation and recovery strategies.

## Classification of Assets

### Categories and sub-categories

![Assets-types](/assets/operation_center/assets_v2/assets-types.png){align="center", style="max-width:100%"}

Sekoia.io supports three types of assets: **Accounts**, **hosts** and **networks**.

For each category, there are additional sub-categories to add an optional additional level of categorization:

| Category | Sub-category |
| --- | --- |
| Account | User account, service account, machine account |
| Host | Desktop, server, mobile |
| Network | IPv4, IPv6 |


### Criticality

The asset criticality value is a numerical indicator that represents the level of criticality or importance of each asset within the organization's IT infrastructure. It ranges from 0 to 100, where 0 indicates that the asset has no criticality or minimal importance, and 100 signifies maximum criticality, denoting assets crucial for the organization's operations.

This value contribues to the [urgency score of alerts](/xdr/features/investigate/alerts). Hence it plays a key role in computing and prioritizing alerts related to assets, ensuring that your SOC team focuses on addressing the most critical security incidents promptly.

### Detection Properties

![detection properties](/assets/operation_center/assets_v2/detection-properties.png){align="right", style="max-width:40%"}

Asset matching and detection properties are fundamental features that enhance our system's event correlation and enrichment capabilities. Each asset type comes with a predefined set of detection properties that determine the criteria for matching incoming events with specific assets. When an event matches an asset based on these properties, the event is enriched with the asset UUID and inherits all the contextual properties associated with the asset, including its criticality and other relevant information.

Your SOC team can effectively correlate these events with specific assets through **asset matching**, enabling them to grasp the context and comprehend the potential impact on critical systems.

### Contextual Properties

The contextual properties enhance asset management within our system by allowing users to associate additional context and metadata with each asset. These properties provide valuable information beyond the standard asset details, enabling better asset classification and enriched insights into the organization's IT infrastructure.

![Asset contextual properties](/assets/operation_center/assets_v2/context-properties.png){align="right", style="max-width:50%"}

A contextual property is an additional attribute that can be assigned to an asset to provide more context and details about the asset. It can include any relevant information, such as names, labels, descriptions, categories, or custom identifiers.

Our asset management system comes with a default set of contextual properties tailored for each type of asset. Additionally, users have the flexibility to create custom contextual properties, allowing for the inclusion of specific details relevant to their organization's unique needs.


#### Best practices for your custom Contextual Properties

1. **Consistency:** Establish a consistent naming convention for your custom contextual properties to ensure clarity and ease of use across assets. Consider using predefined categories (e.g., "Location," "Owner," "Department") to maintain consistency.
2. **Relevance:** Only add contextual properties that provide meaningful information about the asset. Avoid including redundant or irrelevant details.
3. **Data Accuracy:** Regularly review and update contextual properties to ensure that they reflect the latest and most accurate information about your assets.
4. **Security:** Ensure that sensitive information is not exposed through contextual properties. Avoid using contextual properties to store confidential data such as passwords or financial information.
5. **Integration:** Leverage the power of contextual properties to integrate with other systems or modules, such as incident management, reporting, and compliance.




## Your Asset Inventory

Your asset inventory refers to the comprehensive and up-to-date list of all the hosts, accounts and networks manually created, imported and automatically discovered from your organization's infrastructure.


### Manual Asset Creation

![Assets-list](/assets/operation_center/assets_v2/assets-list.png){align="center", style="max-width:100%"}


To create an asset from our UI, you have to:

1. Click on `Assets` in the principal menu on the left
2. Click on the `+ New Asset` button and selects the category of the asset you want to create,
3. Give it a name and mark it as reviewed if you believe your new asset is qualified
4. Determine its sub-category
5. Define a set of optional tags you want to attach to your asset
6. Give it a description along with all the `Contextual Properties` you want
7. Don't forget to define its criticality
8. Define all the `Detection Properties` that will be used to recognize the asset among your events


### Automatic Asset Discovery

In Sekoia.io, **Asset Discovery is the live process of passively finding and consolidating assets from your events**.

It is based on the idea that events contain two kinds of fields :

- fields that denote what happened (_e.g._, a failed SSH authentication)
- fields that denote what resources were involved (_e.g._ user, the computer, the remote SSH server, the eventual proxy or gateway between them, *etc*). While these resources likely represent assets within or outside the scope of your organization, those fields are rarely trivial identifiers of them. Instead, they come as markers, traces, fingerprints, such as IP addresses, FQDNs, emails, UserAgents, *etc*.

In Sekoia.io, event field values that implicitly map to an asset are called **“atoms”**.

### What is an Atom?

Atoms are unambiguous but non-trivial identifiers of real world assets.

An asset can be associated with various atoms (e.g., bound IP addresses and hostnames for machines, usernames and emails for users). However, **each atom uniquely identifies only one asset without any ambiguity at a specific time for a given entity**. For instance:

- Atom `192.168.1.2` maps to asset `DESKTOP-123` in entity `DMZ-1` of community `MyCommunity` on 01/01/2023
- `Windows XP` is not an atom: one doesn’t uniquely identify a computer using its Operating System. Here, `Windows XP` is rather a contextual property.

Some atoms are considered **exclusive identifiers**. For example, the Windows `SID` of an Active Directory user is known to be unique. In the same Active Directory, there is no user with two different `SIDs`.

![atoms-list](/assets/operation_center/assets_v2/atoms-list.png){align="center", style="max-width:100%"}

Although these assets are not yet fully qualified, tracking atoms is still valuable and allowed in Sekoia.io:

- Attachments of atoms to assets is kept in **timeline**. Events that **mutate the structure of an asset**, such as DHCP lease renewals that attach and detach IP addresses to hosts, are therefore accessible to the user and can be used to time-travel the whole network graph for historical investigation purposes
- Behavioral activity is tracked at the atom level. For instance, even if `192.168.1.2` is associated with various assets over time, events related to this IP address are linked to that specific atom. The weekly activity of a selected atom may be seen in Sekoia.io asset details page.

Atoms may be seen as the Operation Center equivalent of **observables** in the Intelligence Center. Although very similar, those concepts have been worded differently because observables in an threat-intelligence context may be understood as external indicators candidate to be tagged as Indicators of Compromise (IoC). Atoms primarily serve as internal observables, specifically related to the supervised network, rather than functioning as global threat-intelligence objects.

#### Tracked Atoms and their related event fields

The following table lists the atom types and their related event fields that are currently tracked by Sekoia.io:

| Atom type | Related event fields |
| --- | --- |
| IPv4 | `client.ip`, `destination.ip`, `host.ip`, `server.ip`, `source.ip`, `related.ip` |
| IPv6 | `client.ip`, `destination.ip`, `host.ip`, `server.ip`, `source.ip`, `related.ip` |
| Hostname | `host.name`, `host.hostname`, `related.host`, `client.name`, `server.name`, `log.hostname` |
| fqdn | `dns.question.name`, `client.domain`, `client.registered_domain`, `destination.domain`, `destination.registered_domain`, `source.domain`, `source.registered_domain`, `server.domain`, `server.registered_domain`, `tls.client.x509.alternative_names`, `url.domain`, `url.registered_domain`, `x509.subject.common_name`, `x509.alternative_names`, `user.domain`, `related.host` |
| username | `user.name`, `user.full_name`, `related.user`, `client.user.name` |
| email | `client.user.email`, `destination.user.email`, `file.x509.alternative_names`, `host.user.email`, `server.user.email`, `source.user.email`, `tls.client.x509.alternative_names`,` user.email`, `user.changes.email`, `user.effective.email`, `user.target.email`, `x509.alternative_names`, `email.from.address`, `email.to.address` |
| sid | `user.id`, `related.user`, `client.user.id` |


## Asset Discovery Rules

### Attach IP to Host

**Attach `host.ip` to Host**

This rule enriches an existing asset with new `ipv4` or `ipv6` contextual properties. These properties are extracted from the value of an event `host.ip` field when the `hostname` detection property of the asset matches with the `host.name` field of the event.

**Attach `source.ip` to Host**

This rule enriches an existing asset with new `ipv4` or `ipv6` contextual properties. These properties are extracted from the `source.ip` field of an event when the `hostname` detection property of the asset matches with the `source.host` field of the event.

**Attach `destination.ip` to Host and categorize it as Server**

This rule enriches an existing asset with new `ipv4` or `ipv6` contextual properties. These properties are extracted from the `destination.ip` field of an event when the `hostname` detection property of the asset matches with the `destination.host` field of the event.

### Attach Operating System (OS) to Host

**Set the Contextual Property `os` to Host**

This rule enriches an existing asset with an `os` contextual property. This property is extracted from the value of all the `os` related fields of an event where its `host.name` field matches the `hostname` detection property of the asset. In addition, this rule categorizes the asset as a Server if the `host.type` contains `server`.


### Discover unique Hosts

This rule creates a new asset for every unseen `host.name`. It attaches the `ipv4` and `ipv6` stored in field `host.ip` of the event as detection properties of the newly created asset.

### Discover unique Accounts

This rule creates a new asset for every unseen `user.name`. It attaches the `user.email` and `user.id` event field values as detection property of the newly created asset.

Questions? Please read our [FAQ](../../FAQ/Assets_qa.md).
