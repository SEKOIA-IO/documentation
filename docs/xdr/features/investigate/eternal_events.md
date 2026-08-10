# Eternal events

Eternal events are the security events attached to your alerts and cases, kept independently of your retention subscription. They remain available for investigation after the same events have expired from your standard retention window.

## Why eternal events matter

Your retention window governs how long ingested events stay searchable. Once an event passes that threshold, it is permanently deleted and cannot be recovered.

Investigations rarely respect that deadline. A breach discovered in November may hinge on evidence collected in March. An auditor, a regulator or an insurer can ask you to substantiate an incident months after it closed. A post-incident review is often the moment you most need the events that triggered the original alert.

Eternal events remove that risk. As soon as an alert is raised or an event is added to a case, the underlying evidence is copied to a permanent store. It is kept independently of your retention subscription:

* **Nothing to configure.** Preservation is automatic.
* **No tier requirement.** It applies whatever retention you have purchased.
* **Not governed by your retention window.** Eternal events outlive your retention window, however long an investigation takes to reopen.

Preservation is bounded, though. See [Scope and limits](#scope-and-limits).

## What is stored eternally

Two kinds of events are preserved:

1. Events that matched a detection rule and raised an alert.
2. Events added to a case.

Coverage depends on the detection type of the rule that raised the alert:

| Detection type | Eternal events |
|---|---|
| CTI | Yes |
| CTI Retrohunt | Yes |
| Sigma | Yes |
| Sigma Correlation | Yes |
| Anomaly | No |
| SOL | No |
| Event Drop | No |

## Scope and limits

Eternal events preserve the narrow context around an incident: the events that raised an alert, and the events you deliberately add to a case. They are not a general purpose archive of your telemetry.

Sekoia.io applies throttling when a disproportionate share of your ingested events would be preserved this way. Past that point, the excess events are not preserved. The alert itself is unaffected and remains fully usable, but some of the events behind it will no longer be available once your retention window has elapsed.

!!! warning "Keep your detection rules specific"
    A rule whose pattern matches a large fraction of your telemetry preserves a correspondingly large volume of events, and can trigger throttling. Specific rule patterns keep the volume proportionate and the evidence behind each alert complete.

## How to access eternal events

Eternal events are reachable in two ways, depending on whether you are working from an alert or writing your own query.

### From the interface

Open any alert or case and go to its **Events** tab. When the original events have aged out of your retention window, the platform serves them from eternal events instead.

This is transparent. There is no switch to flip, no separate view, and no difference in how the events are displayed. An alert from two years ago shows its evidence exactly as an alert from this morning does.

### With a SOL query

To query preserved events directly, use the `eternal_events` datasource in the [Query Builder](/xdr/features/investigate/query_builder.md). Reach for it in two situations:

* **The events have passed your retention window.** They are no longer returned by the `events` datasource or the **Events** page, and `eternal_events` is the only place they still exist.
* **You want to scope a query to alert or case evidence.** Even while the events are still within your retention window, `eternal_events` holds nothing but the events attached to an alert or a case. There is no full telemetry search to narrow down, which makes it the natural datasource for investigating a given alert or building metrics over the events that raised your alerts.

```shell
eternal_events
| where alert_short_ids == "<alert short ID>"
| limit 100
```

Eternal events share the same schema as events, so the filters, aggregations and functions you already use against `events` work here too.

!!! tip "Scope your queries"
    Because eternal events are not subject to automatic time-based deletion, the datasource spans your entire history. Filter on an alert, a case or a time range rather than scanning everything.

## Eternal events and the events datasource

The two datasources answer different questions:

| | `events` | `eternal_events` |
|---|---|---|
| Scope | Every ingested event | Only events attached to an alert or a case |
| Retention | Your subscription's retention window | Not subject to automatic time-based deletion |
| Best for | Threat hunting across all your telemetry | Investigating alerts and cases beyond retention |

Eternal events live in a store of their own rather than being folded into `events`. Keeping the two separate is deliberate: each store is optimized for the way it is queried, which is what allows a search across your full alert history to stay fast.

## Eternal events and cold storage

If your workspace uses the Hot/Cold storage model, you can also [restore data from cold storage](/xdr/FAQ/restore_data_cold_storage.md). The two mechanisms solve different problems and are easy to confuse:

| | Eternal events | Cold storage restore |
|---|---|---|
| Coverage | Events attached to an alert or a case | All events over a requested timespan |
| Access | Immediate, in the interface or with SOL | Request to Sekoia.io Support |
| Delay | None | From 48 working hours |
| Lifetime | Not subject to automatic time-based deletion | Deleted after 30 days |

Use eternal events when you need the evidence behind a specific alert or case. Use a cold storage restore when you need the full picture of everything that happened during a period, including events that never raised an alert.

## Related articles

* [Alerts](/xdr/features/investigate/alerts.md): How alerts are raised and how to investigate them.
* [Cases](/xdr/features/investigate/cases.md): How to group alerts, events and findings into a single investigation.
* [Events page](/xdr/features/investigate/events.md): How to search and filter events within your retention window.
* [SOL Data Sources Reference](/xdr/features/investigate/sol_ref_datasources.md): Reference for the `eternal_events` datasource and every other datasource available to SOL.
* [Data storage and retention](/xdr/FAQ/data_storage_retention.md): Storage engines, retention windows and region availability.
* [Restore data from cold storage](/xdr/FAQ/restore_data_cold_storage.md): How to rehydrate archived events for a given timespan.
