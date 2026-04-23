# Manage alerts

The Alerts page is the primary interface for monitoring security detections. By default, it displays the last 10 alerts ordered by the most recent.

![Alerts listing page with filters, sort options, and alert table](/assets/operation_center/alerts/alert_listing.png)

## Sort alerts

You can sort the alert listing using the following options:

| Sort option | Description |
|---|---|
| **Most Recent** | Orders alerts by creation date, newest first. Default view. |
| **Most Frequent** | Orders alerts by occurrence count. |
| **Recently Updated** | Orders alerts by the date of the last status change. |
| **Most Urgent** | Orders alerts by urgency score, highest first. |

## Process alerts in bulk

1. Select alerts using the checkboxes in the list.
2. To select alerts across all pages, click **Select all XX alerts**.
![Select all alerts confirmation](/assets/operation_center/alerts/select-all-alerts.png)
![All alerts selected message](/assets/operation_center/alerts/unselect-all-alerts.png)
4. Perform one of the following actions:
   - **Add to case** - Select an existing case or create a new one. ![Bulk add to case toolbar](/assets/operation_center/alerts/alert-to-case.png)
   - **Change status** - Select a new status, enter a comment to explain the decision, then click **Update status**. ![Bulk status change interface with status dropdown and comment field](/assets/operation_center/alerts/alert-status.png)

!!! note
    For multi-tenant communities, alerts can only be added to cases that belong to the same community. Leaving a comment when changing status is recommended but not mandatory.


## Related articles

* [Filter and suppress alerts](/xdr/features/investigate/filter_and_suppress_alerts.md): Build complex queries and suppress false positives.
* [Investigate an alert](/xdr/features/investigate/investigate_an_alert.md): Deep-dive into alert details, tasks, events, and similar alerts.
* [Investigate alerts with Graph](/xdr/features/investigate/investigate_alerts_graph.md): Use visual correlation to analyze complex threats.
* [Alerts](/xdr/features/investigate/alerts.md): Understand alert urgency, similarity, and lifecycle logic.
* [Alert interface reference](/xdr/features/investigate/alert_interface_reference.md): Detailed lookup for alert table columns and icons.
