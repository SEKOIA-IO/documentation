# Create a detection rule from a feed

Link a feed to a CTI detection rule to automatically monitor your environment for specific threats. This feature requires a Defend subscription.

**Prerequisites**

You must have a Defend subscription and the necessary permissions to manage detection rules.

**Procedure**

1. Navigate to **Rules catalog**.
2. Click to create a new rule.
3. In the detection pattern, select **CTI**.
4. Select your custom feed from the list.
5. Configure the rule logic and status.
6. Click **Save**.

The rule is now active. It checks both incoming telemetry and historical events for matches against the feed indicators.

## Related articles

- [Feeds](/cti/features/consume/feeds.md): Understand what feeds are, how they work, available formats, and the default feed.
- [Create a feed](/cti/features/consume/create_feed.md): Configure and activate a new feed by selecting object types, sources, TLP levels, and output format.
- [Manage feeds](/cti/features/consume/manage_feeds.md): Consume, edit, duplicate, or delete an existing feed.
 
