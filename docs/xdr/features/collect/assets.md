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

This value contribues to the [urgency score of alerts](/xdr/features/investigate/alerts.md). Hence it plays a key role in computing and prioritizing alerts related to assets, ensuring that your SOC team focuses on addressing the most critical security incidents promptly.

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

Your Asset Inventory refers to the comprehensive and up-to-date list of all the hosts, accounts and networks manually created, imported and automatically discovered from your organization's infrastructure.

The Assets page provides a centralized view and robust tools for managing your asset inventory in a detailed table format. Each row represents a unique asset, and the columns provide key information about that asset.

The page also includes powerful filtering options to help you efficiently locate and manage specific assets. You can filter assets based on the following criteria:

- Criticality: Filter assets by their assigned criticality level
- Tags: Filter assets by specific tags applied to them
- Types: Filter assets by their classification (e.g., Account, Host, Network)
- Source: Filter assets by how they were added to the inventory (Automatic discovery or Manual creation/import)
- Status: Filter assets by their review status (Reviewed or Not Reviewed)

You can use multiple filters simultaneously to refine your view. The number next to the `Filters` button indicates the total number of assets that match your applied filter criteria.

### Bulk Actions 

The Asset Listing page supports bulk actions, allowing you to perform operations on multiple selected assets simultaneously. This significantly improves efficiency when managing your inventory. Available bulk actions include:

- Add tags: Apply one or more tags to multiple selected assets
- Revoke assets: Remove multiple selected assets from your inventory
- Change criticality: Update the criticality level for a group of selected assets
- Change status: Edit the review status (Reviewed or Not Reviewed) for multiple selected assets

!!! note
    Applying an action to a large number of assets (e.g., 10,000 assets) might take some time to process in the background. While the results won't appear instantly, the system is working, and changes will reflect gradually.
    


### Asset Discovery

Reveal supports *multi-source asset discovery*, combining several complementary methods to build a unified, contextualized Asset Inventory.  
This approach ensures maximum coverage of your environment, reduces blind spots, and provides redundancy when a single source of truth is incomplete.  
By correlating multiple identifiers and data feeds, Reveal helps analysts quickly understand what assets exist, their context, and their security posture.  

The three supported discovery methods are:  

1. **Asset Collection via Asset Connectors** *(Reveal add-on module capability)*  
2. **Automatic Asset Discovery (via Events)**  
3. **Manual Asset Creation**  

Each method has unique strengths. Together, they deliver complete asset visibility.

#### Asset Collection via Asset Connectors (Reveal add-On module) - Coming soon!

**How it works:**  
- Asset Connectors pull structured asset data directly from external systems like:  
  - Endpoint Detection & Response (EDR) platforms  
  - Vulnerability Management tools  
  - Cloud/CMDB sources  
- Each connector continuously synchronizes assets into Reveal, keeping the inventory current.  
- Collected assets can override or enrich attributes discovered automatically (e.g., “OS = Windows 11” from the EDR is authoritative).  
- Duplicates from multiple connectors are merged into a single asset record.  
- Admins can manage connectors in **Configure → Asset Connectors**: add, test, enable/disable, or delete.  

**When to use it:**  
- Recommended for critical systems where authoritative data is available (e.g., EDR agent data for all endpoints).  
- Complements automatic discovery by ensuring attributes are correct and complete.  

**Why it matters:**  
- Provides **trusted data** from security controls (less noise than event-only discovery).  
- Ensures consistency across security tools (same asset metadata shared across Sekoia, EDR, VM).  
- Reduces reliance on logs alone, especially for assets with limited event coverage.  

#### Automatic Asset Discovery

In Sekoia.io, **Asset Discovery is the live process of passively finding and consolidating assets from your events**.

It is based on the idea that events contain two kinds of fields :

- fields that denote what happened (_e.g._, a failed SSH authentication)
- fields that denote what resources were involved (_e.g._ user, the computer, the remote SSH server, the eventual proxy or gateway between them, *etc*). While these resources likely represent assets within or outside the scope of your organization, those fields are rarely trivial identifiers of them. Instead, they come as markers, traces, fingerprints, such as IP addresses, FQDNs, emails, UserAgents, *etc*.

In Sekoia.io, event field values that implicitly map to an asset are called **“atoms”**.

**When to use it:**  
- Always active if event ingestion is configured.  
- Best for environments where log coverage is strong but external CMDBs or scanners aren’t integrated.  

**Why it matters:**  
- Ensures no asset is missed, even if not registered elsewhere.  
- Detects “shadow IT” or rogue devices purely from event traces.  
- Provides forensic depth by retaining historical identity–asset mappings. 

##### What is an Atom?

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

###### Tracked Atoms and their related event fields

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


#### Asset Discovery Rules

##### Attach Operating System (OS) to Host

**Set the Contextual Property `os` to Host**

This rule enriches an existing asset with an `os` contextual property. This property is extracted from the value of all the `os` related fields of an event where its `host.name` field matches the `hostname` detection property of the asset. In addition, this rule categorizes the asset as a Server if the `host.type` contains `server`.

##### Attach EDR agent IDs to Host

**Set the Contextual Property `edr_agent_id` to Host**

This rule enriches an existing asset with the `edr_agent_id` contextual property (for example `sentinelone_agent_id`). This property is extracted from the value of `agent.id`. 

Note that this rule only applies to assets of `Host` category and that a single host can have multiple EDR agent IDs.

##### Discover unique Hosts

This rule creates a new asset for every unseen `host.name`. It also suggests the `ipv4` and `ipv6` stored in field `host.ip` of the event as detection properties of the newly created asset.

##### Discover unique Accounts

This rule creates a new asset for every unseen `user.name`. It attaches the `user.email` and `user.id` event field values as detection property of the newly created asset.

Questions? Please read our [FAQ](../../FAQ/Assets_qa.md).

#### Asset based detections

The Sekoia.io SOC platform supports the creation of detection patterns for rules or alert-filters that can be customized to apply to specific groups of assets. This feature allows you to enhance the scope of detection by targeting groups of assets that share certain attributes, such as critical servers, or by tuning the detection rules to exclude certain assets, like administrator accounts. This is accomplished by leveraging various asset attributes, as detailed below.

##### Asset fields

The following table lists the available fields for defining asset-based detection patterns, along with their types and example values:

| Field                                    | Type                | Example Value                          |
|------------------------------------------|---------------------|----------------------------------------|
| `sekoiaio.any_asset.tags`                | Set of Strings      | `{"VIP", "critical", "internal"}`      |
| `sekoiaio.any_asset.uuid`                | Set of Strings      | `{NETWORK_UUID, ENTITYLESS_HOST, USER_UUID, ENTITYSPECIFIC_HOST}` |
| `sekoiaio.any_asset.name`                | Set of Strings      | `"My asset"`                                   |
| `sekoiaio.any_asset.criticality_display` | Set of Strings      | `{"high", "low"}`                      |
| `sekoiaio.any_asset.criticality_value`   | Set of Integers    | `{80, 0}`                              |

!!! Warning
    Some of the fields listed above are removed from the events before indexing them, but they can be used in detection and filtering patterns. Indexed events will thus only contain `sekoia.assets.*.uuid`, `sekoia.assets.*.name`, `sekoia.assets.*.criticality_value`, `sekoia.any_asset.uuid`, `sekoia.any_asset.name` and `sekoia.any_asset.criticality_value`.

##### Use Case Example

To demonstrate the capabilities of asset-based detections, consider the following use case. You can create custom tags and apply them to a list of assets manually or by using a script and available APIs. Once tagged, these assets can be used in detection rules or alert filters to fine-tune the detection scope.

###### Example 1: Detection Rule

The following Sigma pattern demonstrates how to create a detection rule that targets assets tagged with "my_custom_tag_for_critical_servers":

```yaml
detection:
  selection:
    event.code: 4720
    sekoiaio.any_asset.tags: "my_custom_tag_for_critical_servers"

  condition: selection
```

###### Example 2: Alert Filter

The following Sigma pattern demonstrates how to create an alert filter that excludes assets tagged with "my_custom_tag_for_admin_assets":

```yaml
detection:
  selection:
    sekoiaio.any_asset.tags: "my_custom_tag_for_admin_assets"

  condition: selection
```

By using custom tags, you can precisely control which assets are included in or excluded from your detection rules, ensuring a more targeted and effective threat detection strategy. For more information on how to tag assets using the Sekoia.io API, refer to the API documentation.

    !!! Note
    There is no need to add the `contains` modifier when referring to a tag. Because the `sekoiaio.any_asset.tags` field is a list, `sekoiaio.any_asset.tags: mytag` already means "match if any of the tags is mytag".

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

### Asset Based Investigation

In addition to their role in managing security risks, assets in Sekoia.io support investigation based on analytics on their past behaviors. By analyzing asset activity and behavior patterns, you can identify potential patterns of malicious activity or security breaches. This information can be used to investigate and identify potential security risks.

The asset investigation feature provides a detailed view of an asset's history, including past events for a specific set of activities. This allows you to quickly identify any unusual activity and take appropriate action.

#### Authentications

Authentications are an essential part of securing a perimeter. Analyzing all the authentications of an asset provides a comprehensive view of its security posture. In this view, the user can easily spot all the authentications of an asset.

![asset_authentications](/assets/operation_center/assets_v2/asset_authentications.png){: style="max-width:100%"}

An authentication is denoted by the following properties:

- **Time of first occurrence**: The exact time when the authentication was first recorded.
- **Number of occurrences**: The total number of times the authentication occurred.
- **Source host**: The host from which the authentication attempt originated.
- **Target host**: The host that was the target of the authentication attempt.
- **Source account**: The account that initiated the authentication attempt.
- **Target account**: The account that was the target of the authentication attempt.
- **Service/Process**: The service or process involved in the authentication.
- **Authentication status**: The result of the authentication attempt (e.g., success or failure).

This page also shows the trend of the top 10 target accounts of the authentication on the current asset along with the top 5 source hosts. This visual representation helps in quickly identifying patterns and potential security issues.

By leveraging this detailed authentication data, users can enhance their understanding of the asset's security posture and take proactive measures to mitigate potential security threats.

##### Pivoting for Detailed Investigation

Each entry in the authentication logs supports pivoting to the detailed view of the source and target hosts and accounts. 

![asset_pivot](/assets/operation_center/assets_v2/asset_auth_pivot.png){: style="max-width:100%"}

This feature allows users to dive deeper into the specifics of each authentication attempt, facilitating thorough investigation and analysis. Here's how it can be used:

- Source Host Pivot: Clicking on a source host in the authentication log will take you to a detailed page about that specific source host. This page include information such as:
  - Historical activity of the source host.
  - Other assets or accounts the source host has interacted with.

- Target Host Pivot: Similarly, clicking on a target host will navigate to a detailed page about that target host. This page may include:
  - Comprehensive logs of all activities involving the target host.
  - Security posture and any past incidents involving the target host.
  - Relationships with other assets or accounts.

- Source Account Pivot: Clicking on a source account will provide detailed information about that account, including:
  - The account's activity history across various assets.
  - Authentication attempts made by the account.
  - Any security incidents or breaches involving the account.

- Target Account Pivot: Clicking on a target account will reveal detailed information, such as:
  - The account's interaction history.
  - Any security incidents or breaches involving the account.
  - The account's access permissions and any recent changes.
