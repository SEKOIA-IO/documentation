# Alert interface reference

This page describes the fields, columns, and icons available in the alert interface. Use it as a lookup reference when navigating the Alerts table or alert detail views.

## Alerts table columns

By default, the Alerts table displays the following columns:

| Column | Description |
|---|---|
| **Selector** | Checkbox to select alerts for bulk actions. |
| **Similarity** | Occurrence counter showing how many similar events were grouped into the alert. |
| **Date** | Alert creation date. |
| **Status** | Current alert status. Hover over the icon to see the modification date and the author of the change. |
| **Entity** | The entity to which the alert corresponds. |
| **Urgency** | Numerical score between 0 and 100. 100 is the highest urgency. |
| **Type** | Alert type based on the detection rule that triggered it. |
| **Name** | Name of the rule that triggered the alert. |
| **Threats** | Related threats in terms of malicious activities, tools, and campaigns. |
| **First seen** | Date the first matching event was observed. |
| **Last seen** | Date the most recent matching event was observed. |
| **ID** | Short identifier of the alert. |
| **UUID** | Unique identifier of the alert. |
| **Source** | Source observable of the alert. |
| **Target** | Target observable of the alert. |
| **Commu.** | Communities related to the alert. |

!!! tip
    You can show, hide, and reorder columns using the **show/hide columns** button. Your configuration is saved automatically.

!!! note
    Partners have an additional filter to display alerts related to all or a subset of their managed communities.

## Icons and indicators

| Icon | Description |
|---|---|
| **Bell icon** | Indicates the event is involved in the current alert and in at least one other alert. The bell is not displayed if the event is only involved in the current alert. |
| **Smart Descriptions** | Human-readable summaries of events displayed in the alert timeline. |

## Delayed alerts

An alert may be triggered with a delay under the following conditions:

- **IOC retro-scan** - A new IOC is published and historical events match it.
- **Log delay** - Interrupted collection or re-ingestion of old logs causes events to arrive late.

!!! note
    Refer to the `event.created` and `timestamp` documentation for more details on timing fields.

## Related articles

* [Alerts](/xdr/features/investigate/alerts.md): High-level overview of alert concepts and logic.
* [Manage alerts](/xdr/features/investigate/manage_alerts.md): Practical guide for daily operations.
* [Filter and suppress alerts](/xdr/features/investigate/filter_and_suppress_alerts.md): Build complex queries and suppress false positives.
* [Investigate an alert](/xdr/features/investigate/investigate_an_alert.md): Deep-dive into alert details, tasks, events, and similar alerts.
* [Alert rate limiting](/xdr/features/investigate/alert_rate_limiting.md): Understand thresholds, cooldown behavior, and rate-limited state indicators.
