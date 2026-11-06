# Manage feeds

This article covers how to consume, edit, duplicate, and delete an existing feed. To create a new feed, see [Create a feed](/cti/features/consume/create_feed.md).

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

### Customize the API export for a request

You can override the output format and template through the **Public API URL**, without changing the feed's saved settings. These parameters apply to the collections API endpoint, not the TAXII URL.

For example, use `format=custom` and the URL-encoded template `$observables # $description`. Replace `BASE_URL` with the [API base URL for your region](/developer/quickstart.md#step-1-find-your-base-url), without a trailing slash: `https://api.sekoia.io` for FRA1, or `https://app.fra2.sekoia.io/api` for FRA2. Use the corresponding table entry for other regions.

```text
BASE_URL/v2/inthreat/collections/YOUR-FEED-ID/objects?format=custom&template=%24observables%20%23%20%24description&limit=2000
```

If the feed is already configured with the **Custom** format, you can supply only `template` to override its saved template for that request. If you omit `template`, the saved template is used. A feed without a saved custom template requires a template when requesting `format=custom`.

Custom CTI feed exports support up to **2,000 objects per request**, while custom IOC Collection exports support up to **10,000 indicators per request**. See [Custom export templates](/cti/features/consume/ioccollections.md#template-behavior-and-limits) for variable syntax, descriptions, and the grouping of multiple observable values.

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

Sekoia creates an exact copy of the feed's filters and settings.

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
 
