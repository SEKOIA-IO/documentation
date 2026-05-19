# ExaLog storage engine

ExaLog is Sekoia.io's log storage and search engine, designed to give security analysts and MSSPs fast, scalable, and cost-efficient event querying across extended retention windows. All events within your configured retention window are directly queryable at any time from the **Events** page, SOL queries, and notebooks — without any intermediate step.

For information on which regions and workspaces use ExaLog, see [Data storage and retention](/xdr/FAQ/data_storage_retention.md).

## How ExaLog works

ExaLog provides a unified retention window: there is no distinction between recent and older events within the retention period. All data is indexed in a single layer and available for immediate search.

Events linked to alerts or cases are preserved in dedicated indexes beyond the standard retention window, ensuring that forensic data remains available for investigation even after the original retention period expires.

## Capabilities

### Event search

ExaLog handles all search queries initiated from the **Events** page, including searches scoped to events involved in alerts.

!!! tip "Get the most out of extended retention"
    Always specify a time range in your queries. Without one, a query targets your entire retention window, which can significantly slow down results.

### Retrohunt and anomaly detection

You can run retrohunt queries and anomaly detection jobs across the full configured retention window, enabling you to hunt for threats over extended historical datasets without being limited by shorter query horizons.

### Detection rules and correlation

Detection rules and correlation logic operate over the full ExaLog retention window, enabling rule-based detections to cover longer time ranges.

## Benefits

| Benefit | Description |
|---|---|
| Unified retention | All events within the retention window are immediately searchable with no rehydration required |
| Extended retention for alert-related events | Events linked to alerts or cases are preserved beyond the standard retention window |
| Search performance | Search performance is equivalent to or better than the Hot/Cold storage model |
| Cost efficiency | The storage model reduces indexing and storage costs, enabling Sekoia.io to offer competitive retention pricing |
| Encryption | Data is encrypted at rest; Sekoia.io manages the encryption keys |
| Multi-region support | ExaLog is being rolled out to all deployment regions |

## Availability and migration

ExaLog reached general availability on FRA1 and SGP1 regions in May 2026. All new workspaces on these regions are provisioned on ExaLog. Existing FRA1 workspaces are migrated progressively.

For a full breakdown of availability by region, see [Data storage and retention](/xdr/FAQ/data_storage_retention.md).

To initiate or check the status of your workspace migration, contact your Customer Success Manager or follow the steps in [Migrate your workspace to ExaLog](/xdr/FAQ/migrate_workspace_to_exalog.md).

## Related articles

- [Data storage and retention](/xdr/FAQ/data_storage_retention.md) — Overview of both storage models and region availability.
- [Migrate your workspace to ExaLog](/xdr/FAQ/migrate_workspace_to_exalog.md) — Step-by-step guide to checking your current storage model and requesting a migration.
- [Events page](/xdr/features/investigate/events.md) — How to search and filter events in the Sekoia.io investigation interface.
- [Understand massive event export](/xdr/features/investigate/event_export.md) — How to export large volumes of events to an external S3-compatible storage.
- [Retrohunt](/xdr/features/detect/rules_catalog.md) — How to run retrohunt queries across historical event data to identify past threats.
