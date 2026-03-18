# Alert rate limiting

Alert rate limiting automatically contains misconfigured or runaway detection rules to protect your community from alert storms. For SOC teams, this preserves triage usability, keeps queues actionable, and reduces analyst fatigue.

## How it works

Rate limiting is evaluated per detection rule and per community.

### Detection rules

- Rate limiting is applied at the rule level.
- The platform tracks how fast a rule produces distinct alerts using a rolling counter.
- If a detection rule generates 30 distinct alerts within 30 seconds, that rule enters a rate-limited state for 30 minutes.
- Alerts considered similar to an existing alert do not count toward this threshold.

### CTI rules

- Rate limiting is applied at the individual IOC level.
- If a specific IOC reaches the threshold, only that rule and IOC combination enters a rate-limited state for 30 minutes.
- Other IOCs within the same CTI rule remain unaffected and continue generating alerts normally.

## During the rate-limited state

- No new alerts are raised for the affected rule, or affected rule and IOC combination for CTI rules.
- Matching events remain visible, allowing investigations to continue.
- You can configure notifications when a rule enters a rate-limited state.

## Cooldown behavior

- If new threshold breaches occur during the cooldown period, the 30-minute timer resets.
- The affected rule exits the rate-limited state only after 30 minutes pass without a new threshold breach.

## What you see in the interface

| Indicator | Description |
|---|---|
| **Rate-Limited icon** | Displayed on matching events during the rate-limited state. |
| **Explanation message** | Visible when expanding a rate-limited event. |

<img width="437" height="559" alt="image" src="https://github.com/user-attachments/assets/f3ee6754-58db-4135-ac36-6eb7da549a3a" />

## Notifications when Alert Rate Limitation engage
You can set up notifications to alert you whenever an alert rate limit is engaged. To do so, use the following trigger in your [notification configuration](/getting_started/notifications-Listing_Creation.md):
**Detection rule enters a rate-limited state**



## Related articles

* [Alerts](/xdr/features/investigate/alerts.md): Understand alert urgency, similarity, and lifecycle logic.
* [Alert interface reference](/xdr/features/investigate/alert_interface_reference.md): Detailed lookup for alert table columns and icons.
