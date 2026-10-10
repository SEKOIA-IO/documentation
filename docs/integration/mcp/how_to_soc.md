# SOC how-to guides

This page shows what the `sekoia-soc` plugin does for SOC analysts in Claude Code: gather everything on an alert, summarise a case and query your data in plain language. Each guide gives the permissions it needs, an example prompt, the result and the tools the skill calls.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

The guides assume the `sekoia-soc` plugin is installed. See [Install the Sekoia plugins in Claude Code](/integration/mcp/install_claude_code.md). The prompts are examples: write your own, Claude Code picks the matching skill.

| Use case | Skill |
|---|---|
| [Get everything on an alert](#get-everything-on-an-alert) | `alert-details` |
| [Summarise a case](#summarise-a-case) | `case-summary` |
| [Query your data in plain language](#query-your-data-in-plain-language) | `sol-hunt` |

## Get everything on an alert

Collect the full factual record of one alert so that an analyst can decide: what the rule matched, which entities are involved and what Sekoia.io intelligence says about the threats.

Permissions: `View alerts`, `View events`, `View Rules Catalog`. Add `View query builder data sources` and `Execute query` for the linked cases and assets, and `View intelligence` for the threat profiles.

=== "Prompt"

    ```
    Get everything on alert AL2h7Kq9pXmW. Which host and user are behind it, and what rule raised it?
    ```

=== "Result"

    The `alert-details` skill returns, as facts and without a verdict:

    - the alert status, urgency, detection type, first and last seen and number of occurrences;
    - the rule, its source and its type: behavioral detection, vendor verdict pass-through or threat intelligence match, with its documented false positives;
    - the entities from the events: hosts, users, files and hashes, process and parent with the command line, network values;
    - the threats with their Sekoia.io intelligence context, the matched indicator for a threat intelligence alert, and the ATT&CK techniques;
    - the linked cases and assets, and the next pivots.

=== "Tools called"

    1. `get_alert` with the alert short ID.
    2. `run_sol_query` on the `alerts` table for the fields `get_alert` does not return (entity, occurrences, linked cases and assets).
    3. `get_rule` with the rule UUID from the alert.
    4. `get_events_from_alert` with the alert's own `first_seen_at` and `last_seen_at`.
    5. `get_cti_object_by_id` on each threat.

## Summarise a case

Brief the next shift, a manager or a customer on an incident: what happened, in what order, on which assets, and where the case stands.

Permissions: `View cases`, `View events`. Add `View query builder data sources` and `Execute query` for the case priority.

=== "Prompt"

    ```
    Summarise case CA4mN8xQ2rTz as a timeline and a five-line narrative.
    ```

=== "Result"

    The `case-summary` skill returns:

    - the case status, priority, creation date and counts of alerts, hosts and users;
    - a timeline of the alerts in chronological order with the rule, status, host and user of each, alerts of the same minute on the same host grouped on one line;
    - the hosts and users involved;
    - a five-line narrative of facts, then one line of assessment, labelled as such.

    For large cases, it summarises by rule and host with counts and details the first and last alerts.

=== "Tools called"

    1. `get_case` with `include_events = false`: the case and its alerts.
    2. `run_sol_query` on the `cases` table for the priority.
    3. `get_events_from_alert` on two or three anchor alerts for the hosts and users.

## Query your data in plain language

Ask a question about your events, alerts, cases, assets or rules. The `sol-hunt` skill writes a bounded SOL query, shows it so you can rerun it in the Query Builder, runs it and reads the result back in words.

Permissions: `View query builder data sources`, `Execute query`.

!!! tip "Every query is bounded"
    The server rejects queries on `events` that are not bounded in time at both ends, for example `where timestamp between (ago(30d) .. now())`. The skill always adds the time range, aggregates before listing and adds a `limit`. It states the window in its answer, and says when a result reached the limit.

### When did a user last log in?

=== "Prompt"

    ```
    When did alex.martin last log in successfully, and from which host and IP? Look at the last 30 days.
    ```

=== "Result"

    ```shell
    events
    | where timestamp between (ago(30d) .. now())
    | where user.name == 'alex.martin' and event.category == 'authentication'
    | where action.outcome == 'success'
    | select timestamp, event.action, host.name, source.ip, sekoiaio.intake.dialect
    | order by timestamp desc
    | limit 1
    ```

    The skill answers with the time, the host, the source IP and the log source of the login.

### What happened on a host?

=== "Prompt"

    ```
    What happened on host laptop-a1b2c3 in the last 24 hours? Group the events by category.
    ```

=== "Result"

    ```shell
    events
    | where timestamp between (ago(24h) .. now())
    | where host.name == 'laptop-a1b2c3'
    | aggregate count() by event.category
    | order by count desc
    | limit 20
    ```

    Ask for examples of one category to get a short list of events.

### How many alerts did a rule raise?

=== "Prompt"

    ```
    How many alerts did the rule "SentinelOne EDR Threat Detected (Malicious)" raise in the last 7 days, by status? Then list the 10 most urgent.
    ```

=== "Result"

    ```shell
    alerts
    | where created_at > ago(7d)
    | where rule_name == 'SentinelOne EDR Threat Detected (Malicious)'
    | aggregate count() by status
    | order by count desc
    ```

    ```shell
    alerts
    | where created_at > ago(7d)
    | where rule_name == 'SentinelOne EDR Threat Detected (Malicious)'
    | select created_at, short_id, status, urgency
    | order by urgency desc
    | limit 10
    ```

    Pick any short ID from the list and ask for everything on that alert.

### Did a domain appear in our events?

=== "Prompt"

    ```
    Did any host resolve or connect to malicious.example in the last 30 days?
    ```

=== "Result"

    ```shell
    events
    | where timestamp between (ago(30d) .. now())
    | where related.hosts in ['malicious.example']
    | aggregate first_hit = min(timestamp), last_hit = max(timestamp), hits = count() by host.name
    | limit 50
    ```

    The skill names the hosts with their first and last hit. No rows means no match in that window and that telemetry, not proof of absence.

### Which log sources do we have?

=== "Prompt"

    ```
    Which log sources do we have in Sekoia, and how many events did each send yesterday?
    ```

=== "Result"

    ```shell
    events
    | where timestamp between (ago(1d) .. now())
    | aggregate count() by sekoiaio.intake.dialect
    | order by count desc
    | limit 40
    ```

## Related articles

* [Sekoia MCP Server](/integration/mcp/overview.md): Use cases, how the server works, access control and limits.
* [Threat intelligence how-to guides](/integration/mcp/how_to_cti.md): Explore, report and check your telemetry.
* [Plugins and skills](/integration/mcp/plugins_skills.md): Every skill, what it is for and the permissions it needs.
* [MCP tools](/integration/mcp/tools_reference.md): Parameters, permissions and examples for every tool.
* [Getting started with the Sekoia MCP Server](/integration/mcp/getting_started.md): Investigate an alert end to end from Claude Code.
* [SOL how-to guides](/xdr/features/investigate/sol_how_to_guides.md): Write aggregations, joins and dashboards in SOL yourself.
