# Create a feed

A feed generates a filtered, scoped view of threat intelligence based on criteria such as TLP levels, sources, or object types. Follow this procedure to configure and activate a new feed.

**Prerequisites**

You must have the necessary permissions within your community to manage CTI configurations.

**Procedure**

1. Navigate to the **Feeds** page from the main menu.
2. At the top right of the page, click **+ Feed**.
3. In the **Define your feed** section, select the **Object type** filters to include specific STIX objects.

    !!! note "Relationship handling"
        The feed includes only the selected object types. Relationships between objects are excluded. If you leave this field empty, all object types are included.

4. Select the **Intelligence sources** to scope the data.
5. Select the allowed **TLP levels**: White, Green, Amber, or Red.
6. Select whether to exclude indicators that are expired or revoked.
7. Click **Next**.
8. In the **Configure dissemination settings** section, select the sorting order.
    - Select **Newest to oldest** for single-batch retrieval.
    - Select **Oldest to newest** for paginated retrieval.
9. Select the output **Format** and configure its specific parameters.

    ??? example "Feed format specifications"
        * **JSON / STIX** — Standard for CTI platforms. Maximum 10,000 objects per call.
        * **Text** — One object per line. Ideal for firewall EDLs. Maximum 2,000 objects per call.
        * **CSV** — Customizable spreadsheet format. Maximum 2,000 objects per call.
        * **Custom** — User-defined template using variables such as `$tlp`, `$id`, `$name`, and `$observables`. Maximum 2,000 objects per call.

10. Click **Save**.

The feed is now active and appears in the feed listing, ready for internal use or external dissemination.

## Related articles

- [Feeds](/_shared_content/intelligence_center/consume
/feeds.md): Understand what feeds are, how they work, available formats, and the default feed.
- [Manage feeds](/_shared_content/intelligence_center/consume
/manage_feeds.md): Consume, edit, duplicate, or delete an existing feed.
- [Create a detection rule from a feed](/_shared_content/intelligence_center/consume
/create_detection_rule_from_feed.md): Link a feed to a CTI detection rule to automatically match IOCs against your telemetry. Requires a Defend subscription.
