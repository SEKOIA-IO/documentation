# Alert similarity for SOL detection rules

Alert similarity controls how the matches of a SOL detection rule are grouped into alerts. By default, every match of a SOL rule is grouped into a single alert, and you can optionally configure a similarity strategy to split those matches into separate alerts by field value.

## How similarity groups alerts

A similarity strategy is a list of fields. Alerts that share the same values for every field in the strategy are considered similar: instead of raising a new alert, the platform attaches the new match to the existing alert and increments its occurrence counter. This keeps repeated detections of the same condition in one place rather than flooding the alert list.

Similarity applies across the platform, not only to SOL rules. For the full model, including how similarity interacts with alert status and the occurrence counter, see [Alert similarity](/xdr/features/investigate/alerts.md#alert-similarity).

## Why SOL rules have no default similarity strategy

For event-based and Sigma rules, the platform applies a default similarity strategy derived from the datasource, keyed on fields such as `event.dialect`, `source.ip` or `dns.question.name`. These defaults assume a known event structure.

A SOL detection rule can query any datasource: events, alerts, assets, intakes, and more. Those datasources do not share a common field structure, so a single datasource-based default cannot apply uniformly. For this reason, SOL detection rules apply no default similarity strategy based on the datasource.

## Default behavior: one alert per rule

When no similarity strategy is configured, all of a rule's matches are grouped into the same alert. Each new match increments that alert's occurrence counter instead of creating a separate alert. In effect, the SOL query is the grouping key: whatever the query returns belongs to one alert.

!!! note "Default grouping"
    Without a configured similarity strategy, a SOL detection rule produces a single alert that accumulates occurrences over time, regardless of the datasource it queries.

## Configuring a similarity strategy

To group a rule's matches into separate alerts, configure one or more similarity strategies on the rule. You select the fields that define similarity. Matches that share the same values for those fields are grouped into one alert; matches with different values are raised as separate alerts.

You can also group fields that are interchangeable so their values can be swapped when matching. Interchangeable fields are written as a nested list, for example `[source.ip, destination.ip]`, following the same notation used elsewhere for similarity strategies.

For the step-by-step procedure, see [Create a SOL detection rule](/xdr/features/detect/create_sol_detection_rule.md).

## Example

A SOL detection rule detects failed logins from a watchlist of malicious IP addresses.

- **Default (no similarity strategy):** every failed login the rule matches is grouped into one alert. The alert's occurrence counter rises as new matches arrive, no matter which source IP they come from.
- **Similarity strategy on `source.ip`:** the rule raises one alert per source IP. A repeated failed login from the same IP increments that alert's occurrences, while a failed login from a different IP opens a new alert.

This lets you choose between a single consolidated alert for the whole rule and one alert per entity you care about.

## Related articles

* [SOL detection rules](/xdr/features/detect/sol_detection_rule.md): Conceptual overview of the SOL and Event Drop detection patterns, how they work, and when to use them.
* [Create a SOL detection rule](/xdr/features/detect/create_sol_detection_rule.md): Step-by-step instructions to configure and activate a SOL or Event Drop detection rule, including the similarity strategy.
* [Alert similarity](/xdr/features/investigate/alerts.md#similarity-strategies): The platform-wide similarity model, occurrence counter, and how similarity interacts with alert status.
* [Lag management for SOL detection rules](/xdr/features/detect/sol_detection_lag_management.md): How rules handle late-arriving events through a fixed run overlap and deduplication.
