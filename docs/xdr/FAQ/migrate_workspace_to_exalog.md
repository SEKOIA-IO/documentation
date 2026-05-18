# Migrate your workspace to ExaLog

This article explains how to check whether your workspace uses ExaLog and how to request a migration from the legacy Hot/Cold storage model.

ExaLog is Sekoia.io's next-generation storage engine. Migrating gives you access to a unified retention window, improved search performance, and extended retention for alert-related events without any rehydration step.

## Prerequisites

- Your workspace is on FRA1 region.
- Your workspace was created before May 2026 (workspaces created from May 2026 onward on FRA 1 and SGP1 are already on ExaLog).
- You have a Customer Success Manager assigned to your account.

## Check your current storage model

To verify which storage model your workspace uses:

1. Navigate to **Settings > Subscription**.
2. Locate the **Storage** section.
3. If you see separate **Hot storage** and **Cold storage** entries, your workspace uses the legacy model and is eligible for migration.
   
![Navigation to Settings > Subscription to view hot and cold storage days](/assets/xdr/storage_subscription.png)

## Request migration to ExaLog

!!! note "Migration timeline"
    Migration is performed by our teams. The timeline depends on your workspace size and region availability. Your Customer Success Manager will confirm the schedule before any action is taken.

1. Contact your Customer Success Manager directly or through the Sekoia.io support portal.
2. Request migration of your workspace to ExaLog.
3. Confirm the migration schedule with your Customer Success Manager.

Your Customer Success Manager will coordinate the migration and notify you when your workspace is ready.

## What to expect after migration

Once your workspace is migrated to ExaLog:

- All events within your configured retention window are immediately searchable from the **Events** page.
- The rehydration process for archived events is no longer required.
- Retrohunt queries and anomaly detection jobs operate across the full retention window.
- Events linked to alerts or cases are preserved beyond the standard retention window.

!!! note "Historical data availability"
    Events ingested before the migration date are available in ExaLog only after your original retention window has fully transitioned. Full ExaLog capabilities become available progressively.

## Related articles

- [ExaLog storage engine](/xdr/FAQ/exalog_storage_engine.md): Learn about ExaLog's capabilities, benefits, and how it differs from the legacy Hot/Cold model.
- [Data storage and retention](/xdr/FAQ/data_storage_retention.md): Overview of both the legacy Hot/Cold model and ExaLog, with guidance on which applies to your workspace.
- [Restore data from cold storage](/xdr/FAQ/restore_data_cold_storage.md): How to rehydrate archived events from cold storage on legacy workspaces.
- [Events page](/xdr/features/investigate/events.md): How to search and filter events in the Sekoia.io investigation interface.
