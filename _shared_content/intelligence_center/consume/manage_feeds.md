# Manage feeds

This article covers how to consume, edit, duplicate, and delete an existing feed. To create a new feed, see [Create a feed](task_create_feed.md).

## Consume a feed

To integrate a feed with an external tool such as a firewall, SIEM, or TIP, retrieve its dissemination details to obtain the relevant API or TAXII endpoint.

**Procedure**

1. Navigate to the **Feeds** page.
2. Locate the desired feed and click the **Actions (⋯)** icon.
3. Select **Disseminate**.
4. Copy the link corresponding to your integration method.

| Link | Use |
| --- | --- |
| **Public Feed ID** | Fetch or update the collection programmatically |
| **Public API URL** | Direct API calls and integrations |
| **Public TAXII URL** | TAXII-compatible systems and platforms |

A single feed can be consumed simultaneously through all three links.

## Edit a feed

Modify the filters or dissemination format of an existing feed to update the data flow to your connected tools.

**Procedure**

1. Navigate to the **Feeds** page.
2. Locate the feed and click the **Actions (⋯)** icon.
3. Select **Edit**.
4. Update the filters or settings as required.
5. Click **Save**.

## Duplicate a feed

Duplicating a feed creates a new version with the same filters and settings, without starting from scratch. Each duplicate receives its own unique Feed ID and dissemination URLs.

**Procedure**

1. Navigate to the **Feeds** page.
2. Click the **Actions (⋯)** icon on the feed row.
3. Select **Duplicate**.

Sekoia.io creates an exact copy of the feed's filters and settings.

## Delete a feed

Remove a feed that is no longer required for your operations.

!!! warning "Permanent action"
    Deleting a feed is irreversible. Any external tools relying on this Feed ID or URL will lose access to the data stream.

**Procedure**

1. Navigate to the **Feeds** page.
2. Locate the feed and click the **Actions (⋯)** icon.
3. Select **Delete**.
4. Confirm the action in the modal.

## Related articles

- [Feeds](/cti/features/consume/feeds.md) — Understand what feeds are, how they work, available formats, and the default feed.
- [Create a feed](/cti/features/consume/create_feed.md) — Configure and activate a new feed by selecting object types, sources, TLP levels, and output format.
- [Create a detection rule from a feed](/cti/features/consume/create_detection_rule_from_feed.md) — Link a feed to a CTI detection rule to automatically match IOCs against your telemetry. Requires a Defend subscription.
 
