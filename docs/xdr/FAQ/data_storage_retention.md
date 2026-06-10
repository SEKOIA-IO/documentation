# Data storage and retention

Sekoia.io stores and indexes security events to support detection, investigation, and compliance. Two storage engines are available across Sekoia.io regions: **Hot/Cold storage** and **ExaLog**.

## Region availability

The storage engine available to your workspace depends on your region and provisioning date.

| Region | Storage engine | Notes |
|--------|---------------|-------|
| FRA1 | ExaLog | Workspaces created from May 2026 onward. Workspaces created before May 2026 are being migrated progressively. |
| SGP1 | ExaLog | All workspaces. |
| FRA2 | Hot/Cold storage | — |
| EUR1 | Hot/Cold storage | — |
| MCO1 | Hot/Cold storage | — |
| UAE1 | Hot/Cold storage | — |
| USA1 | Hot/Cold storage | — |

!!! tip "FRA1 workspaces created before May 2026"
    If your workspace is on FRA1 and was provisioned before May 2026, you can request migration to ExaLog. Migration gives you a unified retention window, direct search across all retained events, and no rehydration step for older data. Contact your Customer Success Manager or see [Migrate your workspace to ExaLog](/xdr/FAQ/migrate_workspace_to_exalog.md).

!!! note "Rollout to additional regions"
    ExaLog is being rolled out to additional regions. When ExaLog becomes available in a new region, only events ingested after the activation date are indexed in ExaLog. Existing data is not migrated retroactively. Full capabilities become available progressively as your original retention window expires.

---

## Hot/Cold storage

Workspaces running Hot/Cold storage use a two-tier model that separates active, searchable events from archived data.

### Hot storage

Hot storage contains your most recent events and is optimized for immediate operational use.

- **Availability**: Events are immediately searchable for threat hunting and detection.
- **Retention**: The default period is 30 days, extendable up to 365 days.
- **Performance**: High-performance indexing for rapid querying.

### Cold storage

Cold storage (also called "Archives") is an optional tier for older events. It provides a cost-effective way to retain data for compliance without keeping it in the active search index.

- **Availability**: Events are not immediately searchable. You must trigger a rehydration process to access archived data.
- **Retention**: Combined retention (Hot + Cold) typically ranges from 30 to 365 days.
- **Resiliency**: Sekoia.io maintains the same level of data resiliency for both storage tiers.

### View your storage capacity

You can verify the storage durations included in your subscription directly in the platform.

1. Navigate to **Settings > Subscription**.
2. Locate the **Storage** section to see your allocated days for each tier.

![Navigation to Settings > Subscription to view hot and cold storage days](/assets/xdr/storage_subscription.png)

### Storage limitations

!!! warning "Permanent data deletion"
    Sekoia.io cannot retrieve data that exceeds your defined storage thresholds. If your total retention is 120 days, any data older than this limit is permanently deleted and cannot be recovered.

Retention periods are strictly governed by your contractual agreement.

---

## ExaLog

ExaLog is Sekoia.io's log storage and search engine for high-volume workloads. It provides a unified retention window with no distinction between hot and cold tiers. All events within your configured retention period are directly queryable from the **Events** page without any rehydration step.

| Characteristic | Details |
|---|---|
| Retention | Configurable retention window; events linked to alerts or cases are preserved beyond the standard window |
| Search | All events are searchable within the retention period without delay |
| Encryption | Data is encrypted at rest; Sekoia.io manages the encryption keys |
| Export | Large-volume exports to S3-compatible storage are supported (available June 2026) |

To learn more about ExaLog capabilities, see [ExaLog storage engine](/xdr/FAQ/exalog_storage_engine.md).

---

## Related articles

- [ExaLog storage engine](/xdr/FAQ/exalog_storage_engine.md) — Learn about ExaLog's capabilities and how it differs from Hot/Cold storage.
- [Migrate your workspace to ExaLog](/xdr/FAQ/migrate_workspace_to_exalog.md) — Step-by-step guide to checking your current storage model and requesting a migration to ExaLog.
- [Restore data from cold storage](/xdr/FAQ/restore_data_cold_storage.md) — How to rehydrate archived events from cold storage.
- [Events page](/xdr/features/investigate/events.md) — How to search and filter events in the Sekoia.io investigation interface.
- [Understand massive event export](/xdr/features/investigate/event_export.md) — How to export large volumes of events to an external S3-compatible storage.
