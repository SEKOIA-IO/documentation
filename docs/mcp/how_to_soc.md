# SOC how-to guides

This page provides goal-oriented recipes for the SOC data tools of the Sekoia MCP Server: alerts, cases, rules, events and SOL queries. Each recipe states the question, an example prompt and the tools your assistant calls to answer it.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

Each recipe lists the permissions its API key needs. The prompts are examples: write your own, the assistant selects the tools.

## How to explain why an alert fired

Understand what a detection rule matched and how much weight to give the alert, before opening the events.

Permissions: `View alerts`, `View Rules Catalog`.

=== "Prompt"

    ```
    Explain why alert AL2h7Kq9pXmW fired. What does the rule match, is it a behavioral detection or a vendor verdict pass-through, and does the rule document false positives?
    ```

=== "Tools called"

    1. `get_alert` with `alert_short_id = "AL2h7Kq9pXmW"` returns the alert, the rule name, its pattern and the mapped ATT&CK techniques.
    2. `get_rule` with the `rule.uuid` from the alert returns the full rule: type, pattern, severity, effort, datasources, references and the `false_positives` field.

The assistant explains the pattern in plain language and says whether the rule fires on its own logic or relays a third-party verdict, which changes how you triage it.

## How to find who and what is behind an alert

Identify the host, the user and the object the detection flagged. The alert itself does not carry them; the events do.

Permissions: `View alerts`, `View events`.

=== "Prompt"

    ```
    Which host, user and file are behind alert AL2h7Kq9pXmW? Include the parent process and whether the EDR mitigated the threat.
    ```

=== "Tools called"

    1. `get_alert` returns the alert with its `first_seen_at` and `last_seen_at`.
    2. `get_events_from_alert` with the alert short ID and those two timestamps returns the events. The assistant reads `host.name`, `user.name`, `file.name`, `file.path`, `file.hash.*`, `process.parent.name` and the vendor-specific fields such as the mitigation status.

!!! tip "Reuse the timestamps"
    Pass the alert's own `first_seen_at` and `last_seen_at` to `get_events_from_alert`. A wider window returns events unrelated to the alert.

## How to build a case timeline

Reconstruct an incident from a case: which alerts it groups, on which hosts and users, in what order.

Permissions: `View cases`.

=== "Prompt"

    ```
    Build a timeline for case CA4mN8xQ2rTz: list its alerts in chronological order with the host and user involved in each, and summarize the incident in five lines.
    ```

=== "Tools called"

    1. `get_case` with `case_short_id = "CA4mN8xQ2rTz"` returns the case, its alerts sorted by creation date and their events.

The assistant orders the alerts, extracts the hosts and users from the events and writes the summary. Ask for the ATT&CK techniques across all alerts to get a tactic-level view of the incident.

## How to check a user's recent activity

Answer "what did this user do lately?" with a SOL query the assistant writes and runs for you.

Permissions: `View query builder data sources`, `Execute query`.

=== "Prompt"

    ```
    When did alex.martin last log in successfully, and from which host and IP? Look at the last 30 days.
    ```

=== "Tools called"

    1. `run_sol_query` with a query the assistant writes:

    ```shell
    events
    | where timestamp > ago(30d)
    | where user.name == 'alex.martin' and event.category == 'authentication'
    | where action.outcome == 'success'
    | select timestamp, event.action, host.name, source.ip, sekoiaio.intake.dialect
    | order by timestamp desc
    | limit 1
    ```

    The assistant reads the row back and answers with the time, host and source IP.

### Variant: activity on a host

=== "Prompt"

    ```
    List the last 50 events on host laptop-a1b2c3 in the past 24 hours, grouped by event category.
    ```

=== "Tools called"

    1. `run_sol_query` with:

    ```shell
    events
    | where timestamp > ago(24h)
    | where host.name == 'laptop-a1b2c3'
    | select timestamp, event.category, event.action, process.name, destination.ip
    | order by timestamp desc
    | limit 50
    ```

!!! tip "Bound every query"
    Ask for a time range and a limit in the prompt. A query without them can return more rows than the assistant can read, and counts against the same rate limits as the Sekoia.io API.

## How to find every alert from one rule this week

Measure the noise of a rule: how many alerts it raised, with which statuses and urgencies, before deciding on a filter or a rule change.

Permissions: `View query builder data sources`, `Execute query`.

=== "Prompt"

    ```
    How many alerts did the rule "SentinelOne EDR Threat Detected (Malicious)" raise in the last 7 days, broken down by status? Then list the 10 most urgent ones.
    ```

=== "Tools called"

    1. `run_sol_query` for the breakdown:

    ```shell
    alerts
    | where created_at > ago(7d)
    | where rule_name == 'SentinelOne EDR Threat Detected (Malicious)'
    | aggregate count() by status
    | order by count desc
    ```

    2. `run_sol_query` for the list:

    ```shell
    alerts
    | where created_at > ago(7d)
    | where rule_name == 'SentinelOne EDR Threat Detected (Malicious)'
    | select created_at, short_ID, status, urgency
    | order by urgency desc
    | limit 10
    ```

    The assistant reports the counts and the list, and can follow up with `get_alert` on any short ID you pick.

## Related articles

* [Sekoia MCP Server](/mcp/mcp_overview.md): What the server exposes, how access control works and its current limits.
* [Threat intelligence how-to guides](/mcp/how_to_cti.md): Recipes for exposure checks, indicator enrichment and threat briefs.
* [MCP tools](/mcp/tools_reference.md): Parameters, permissions and examples for every tool.
* [Getting started with the Sekoia MCP Server](/mcp/getting_started.md): Triage an alert end to end from Claude Code.
* [SOL how-to guides](/xdr/features/investigate/sol_how_to_guides.md): Write aggregations, joins and dashboards in SOL yourself.
* [Connect Claude Desktop to the Sekoia MCP Server](/mcp/connect_claude_desktop.md): Configure Claude Desktop.
* [Connect Claude Code to the Sekoia MCP Server](/mcp/connect_claude_code.md): Configure Claude Code.
