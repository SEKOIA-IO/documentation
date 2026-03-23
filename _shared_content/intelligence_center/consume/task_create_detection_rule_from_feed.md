# Create a detection rule from a feed

Link a feed to a CTI detection rule to automatically monitor your environment for specific threats. This feature requires a Defend subscription.

**Prerequisites**

You must have a Defend subscription and the necessary permissions to manage detection rules.

**Procedure**

1. Navigate to **Rules catalog**.
2. Click to create a new CTI rule.
3. In the source selection, select **IOC collections**.
4. Select your custom feed from the list.
5. Configure the rule logic and status.
6. Click **Save**.

The rule is now active. It checks both incoming telemetry and historical events for matches against the feed indicators.

## Related articles

- [Feeds](concept_feeds.md)
- [Feeds listing](reference_feeds_listing.md)
- [Create a feed](task_create_feed.md)
- [Manage feeds](task_manage_feeds.md)
