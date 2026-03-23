# Feeds

A feed is a filtered, scoped view of Cyber Threat Intelligence (CTI) objects from the Sekoia.io database. Feeds let you distribute threat intelligence to external security tools or use it as a dynamic filter within the platform.

Feeds are shared across all users within the community that created them, ensuring consistent intelligence scoping across your organization.

## What feeds are used for

Feeds serve as versatile components for both internal analysis and external integration.

**Filter reports and intelligence views** — You can use a feed as a filter on the **Reports** page to display only content matching specific criteria, such as industry sectors or geographic regions.

**Scope the intelligence database** — To visualize the exact contents of a feed, navigate to the **Intelligence Database**, click **Filters**, select **Feeds**, and choose your feed.

**Create detection rules** — If you have a Defend subscription, you can link a feed to a CTI detection rule to automatically match indicators of compromise (IOCs) against telemetry.

**Distribute to external tools** — You can share filtered data with firewalls, SIEMs, or TIPs using dedicated API or TAXII endpoints.

## The default feed

Every community with an Intelligence subscription has a **Default Feed** available out of the box, with no configuration required. It covers the entire Sekoia CTI database with no filters applied. The Default Feed is always accessible and cannot be deleted.

Use the following Feed ID to access it programmatically: `d6092c37-d8d7-45c3-8aff-c4dc26030608`

!!! tip "Creating scoped feeds"
    Create additional feeds whenever you need a filtered, scoped view — for a specific TLP level, source, or object type.

## Feeds page columns

The **Feeds** page displays all feeds available in your community. Each feed appears as a row with the following columns.

| Column | Description |
| --- | --- |
| **Name** | The title of the feed |
| **Format** | The export format: JSON/STIX, Text, CSV, or Custom |
| **Created by** | The community that created the feed |
| **Filters** | Active filters applied to the feed: object types, sources, TLP levels, and observables |
| **Actions (⋯)** | Available actions: **Disseminate**, **Edit**, **Duplicate**, or **Delete**. These actions are unavailable on the Default Feed. |

## Feed formats

When you create or edit a feed, you select an output format. The table below summarizes the available formats and their constraints.

| Format | Best suited for | Max objects per call |
| --- | --- | --- |
| JSON / STIX | CTI platforms | 10,000 |
| Text | Firewall EDLs (one object per line) | 2,000 |
| CSV | Customizable spreadsheet exports | 2,000 |
| Custom | User-defined templates using variables such as `$tlp`, `$id`, `$name`, and `$observables` | 2,000 |

## Dissemination links

When you select **Disseminate** from the **Actions (⋯)** menu of a feed, you access three integration links. A single feed can be consumed simultaneously through all three.

| Link | Use |
| --- | --- |
| **Public Feed ID** | Fetch or update the collection programmatically |
| **Public API URL** | Direct API calls and integrations (`https://app.sekoia.io/api/v2/inthreat/collections/...`) |
| **Public TAXII URL** | TAXII-compatible systems and platforms (`https://app.sekoia.io/api/v2/inthreat/taxii-server/...`) |

## Relationship handling

Feeds include only the object types you select in the **Object type** filters. Relationships between objects are not included. If you leave the object type filter empty, all object types are included.

## Related articles

- [Create a feed](/cti/features/consume/create_feed.md): Configure and activate a new feed by selecting object types, sources, TLP levels, and output format.
- [Manage feeds](/cti/features/consume/manage_feeds.md): Consume, edit, duplicate, or delete an existing feed.
- [Create a detection rule from a feed](/cti/features/consume/create_detection_rule_from_feed.md): Link a feed to a CTI detection rule to automatically match IOCs against your telemetry. Requires a Defend subscription.
 
