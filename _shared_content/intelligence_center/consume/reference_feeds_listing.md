# Feeds listing

The **Feeds** page displays all feeds available in your community. Each feed appears as a row with the following columns.

| Column | Description |
| --- | --- |
| **Name** | The title of the feed |
| **Format** | The export format: JSON/STIX, Text, CSV, or Custom |
| **Created by** | The community that created the feed |
| **Filters** | Active filters applied to the feed: object types, sources, TLP levels, and observables |
| **Actions (⋯)** | Available actions: **Disseminate**, **Edit**, **Duplicate**, or **Delete**. These actions are unavailable on the Default Feed. |

## Dissemination links

When you select **Disseminate** from the **Actions (⋯)** menu of a feed, you access three integration links. A single feed can be consumed simultaneously through all three.

| Link | Use |
| --- | --- |
| **Public Feed ID** | Fetch or update the collection programmatically |
| **Public API URL** | Direct API calls and integrations (`https://app.sekoia.io/api/v2/inthreat/collections/...`) |
| **Public TAXII URL** | TAXII-compatible systems and platforms (`https://app.sekoia.io/api/v2/inthreat/taxii-server/...`) |

## Related articles

- [Feeds](concept_feeds.md)
- [Create a feed](task_create_feed.md)
- [Manage feeds](task_manage_feeds.md)
- [Create a detection rule from a feed](task_create_detection_rule_from_feed.md)
