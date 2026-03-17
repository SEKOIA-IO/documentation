# Alerts

Alerts are created by the Operations Center when an event matches a rule and a threat is detected. They serve as the central unit for security investigations, consolidating evidence and context.

## Alert status and lifecycle

Sekoia.io allows you to customize alert statuses to adapt them to your SOC team's specific processes. These statuses enable you to define workflows that match your organization's requirements while maintaining consistency across alerts and cases.

### Default alert statuses

By default, alerts use the following five statuses:

| Status | Description | Possible actions |
|---|---|---|
| **Pending** | Initial status when an alert is triggered. If the generation mode is Automatic, this changes to Ongoing. | Acknowledge, Reject, Validate |
| **Acknowledged** | Used when an analysis is ongoing. This status is optional if an analyst decides on a verdict quickly. | Validate, Reject |
| **Ongoing** | The alert is a true positive and countermeasures are not yet applied. This is the first status seen in automatic mode. | Close, Reject |
| **Closed** | Final status. All necessary actions have been applied. | No action accepted |
| **Rejected** | Final status. The alert was a false positive. | No action accepted |

!!! note "Automatic migration"
    Legacy alert statuses (Pending, Acknowledged, Ongoing, Closed, Rejected) are automatically converted to custom statuses for existing users. Your current workflows remain unchanged.


## Alert urgency

Urgency is a number between 1 (very low risk) and 100 (very high risk) used to score the risk associated with an alert. It is calculated from the severity of a rule and the criticality of assets related to the alert.

$$Alert\ urgency = \frac{Severity\ of\ the\ rule + Criticality\ of\ the\ asset}{2}$$

!!! note
    When the criticality of an asset is 0 (N/A), the alert urgency is equal to the severity of the rule.

The interface displays urgency in both numerical and textual formats:

| Display | Value |
|---|---|
| Low | [0–50[ |
| Medium | [50–75[ |
| High | [75–100] |


## Alert similarity

Alert similarity (Occurrence) is the process of collecting similar events into the same alert. This information is visible in the Alerts table in the **Occurrence** column.

### Similarity strategies

Alerts are considered similar if a list of fields defined by the similarity strategy have the same values for all events. Fields may be grouped so their values can be swapped. There are three priority levels for defining the strategy:

1. **Similarity by rule** — Defined during rule creation in the Rules Catalog.
2. **Similarity by event** — Logic applied by Sekoia.io based on event data (e.g., `dns.question.name`, `user.name`, or `file.hash.sha256`).
3. **Default similarity** — Uses the same `entity`, `source.ip`, and `destination.ip`.

<!-- SCREENSHOT SUGGESTION: The similarity strategy section within an alert's details tab. -->
<!-- ALT TEXT: Alert details showing the effective similarity strategy. -->

### Similarity and alert status

As long as a similar alert exists with a status in the **Open** or **In Progress** stage (e.g., Pending, Acknowledged, Ongoing), new matches are added as occurrences. If only **Closed** stage alerts are similar, a new alert is created, and previous alerts are listed in the **Similar Alerts** tab.


## Alert types and categories

The alert type is associated with the triggering rule or specific indicators from CTI rules. Types are derived from the [ENISA Reference Incident Classification Taxonomy](https://www.enisa.europa.eu/).

<!-- SCREENSHOT SUGGESTION: The alert categories diagram showing threat classifications. -->
<!-- ALT TEXT: Sekoia.io alert category taxonomy. -->

## Related articles

* [Manage alerts](/xdr/features/investigate/manage_alerts.md): Learn how to filter and process alerts in the Operations Center.
* [Investigate alerts with Graph](/xdr/features/investigate/investigate_alerts_graph.md): Use visual correlation to analyze complex threats.
* [Alert interface reference](/xdr/features/investigate/alert_interface_reference.md): Detailed lookup for alert table columns and icons.
