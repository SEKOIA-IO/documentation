# Threat intelligence how-to guides

This page provides goal-oriented recipes for the threat intelligence tools of the Sekoia MCP Server. Each recipe states the question, an example prompt and the tools your assistant calls to answer it.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

All recipes on this page need an API key with the `View intelligence` permission. The exposure check also needs `View query builder data sources` and `Execute query` for its last step. The prompts are examples: write your own, the assistant selects the tools.

## How to check exposure to a threat actor

Turn "Are we exposed to this actor?" into a concrete check: find the actor, list what it uses, then look for those indicators in your own data.

=== "Prompt"

    ```
    Are we exposed to TeamTNT? Find the actor in Sekoia CTI, list the malware and tools it uses, then check whether any of the related indicators appear in our events over the last 30 days.
    ```

=== "Tools called"

    1. `search_cti` with `term = "TeamTNT"` returns the intrusion set and its aliases.
    2. `get_cti_object_relationships_by_id` with the intrusion set ID and `target_types = ["malware", "tool", "attack-pattern"]` returns the malware, tools and techniques linked to it.
    3. `get_cti_object_reports_by_id` on the intrusion set returns the reports the assistant cites.
    4. `search_observables` on the indicators named in the reports returns the observables Sekoia.io tracks for them.
    5. `run_sol_query` on `events` for those observables over the last 30 days confirms whether any of them appear in your telemetry.

The assistant ends with a short answer: exposed or not, on what evidence, and what to watch.

!!! tip "Keep relationship graphs readable"
    Well-known intrusion sets have hundreds of relationships. Naming the `target_types` you care about keeps the response within what the assistant can process.

## How to enrich an indicator during triage

Get instant context on a suspicious IP, domain, URL or hash: is it known to Sekoia.io, and which threat is it tied to?

=== "Prompt"

    ```
    Is 203.0.113.42 known to Sekoia CTI? If it is, which threat is it linked to and since when?
    ```

=== "Tools called"

    1. `search_observables` with `searches = ["203.0.113.42"]` and `with_indicated_threats` left at its default returns the observable, its validity period and the threats it indicates.
    2. `get_cti_object_by_id` on the indicated intrusion set or malware returns its profile: description, aliases, first and last seen, targeted sectors.

You can pass several indicators at once in `searches`; the assistant reports each one separately.

## How to build a sector threat brief

Assemble a sourced brief on the actors targeting a sector, for a customer, a management committee or a monthly report.

=== "Prompt"

    ```
    Build a threat brief on actors targeting the healthcare sector in 2026. For each actor give its aliases, its main malware and one cited Sekoia.io report.
    ```

=== "Tools called"

    1. `search_cti` with `term = "healthcare"` returns the sector identity and the objects mentioning it.
    2. `get_cti_object_relationships_by_id` on the sector identity with `target_types = ["intrusion-set", "campaign"]` returns the actors and campaigns that target it.
    3. `get_cti_object_relationships_by_id` on each actor with `target_types = ["malware"]` returns its malware.
    4. `get_cti_object_reports_by_id` on each actor returns the reports used as sources.

!!! tip "Ask for sources on every claim"
    State the period and the sector in the prompt, and ask the assistant to cite a report for each actor. Claims without a report reference should be treated as unverified.

## How to profile a malware family after an incident

Give the incident retrospective a complete picture of the malware involved: who uses it, what infrastructure it relies on and what has been written about it.

=== "Prompt"

    ```
    What does Sekoia CTI know about the malware family found in incident CA4mN8xQ2rTz? Which actors use it, what infrastructure is linked to it, and which reports cover it?
    ```

=== "Tools called"

    1. `get_case` with `case_short_id = "CA4mN8xQ2rTz"` returns the case and the malware name mentioned in its alerts.
    2. `search_cti` with the malware name returns the malware object.
    3. `get_cti_object_by_id` on the malware returns its profile, including the kill chain phases and malware types.
    4. `get_cti_object_relationships_by_id` on the malware with `target_types = ["intrusion-set", "infrastructure", "tool"]` returns the actors, infrastructure and tools linked to it.
    5. `get_cti_object_reports_by_id` on the malware returns the reports, most recent first.

Reading the case needs the `View cases` permission in addition to `View intelligence`. Without it, name the malware family in the prompt instead.

## How to vet a third party's infrastructure

Before onboarding a supplier or partner, check whether its known domains and IP addresses have a history of malicious activity.

=== "Prompt"

    ```
    Check these domains and IPs for any association with malicious activity in Sekoia CTI: supplier.example, mail.supplier.example, 198.51.100.7. Report matches with their validity period and the threat involved.
    ```

=== "Tools called"

    1. `search_observables` with `searches = ["supplier.example", "mail.supplier.example", "198.51.100.7"]` returns the observables known to Sekoia.io, their validity periods and the threats they indicate.
    2. `get_cti_object_by_id` on each indicated threat returns the context the assistant uses to explain the match.

A match with an expired validity period is historical context, not a current finding. Ask the assistant to separate the two in its answer.

## Related articles

* [Sekoia MCP Server](/mcp/mcp_overview.md): What the server exposes, how access control works and its current limits.
* [SOC how-to guides](/mcp/how_to_soc.md): Recipes for alerts, cases, rules and SOL queries.
* [MCP tools](/mcp/tools_reference.md): Parameters, permissions and examples for every tool.
* [Getting started with the Sekoia MCP Server](/mcp/getting_started.md): Triage an alert end to end from Claude Code.
* [Connect Claude Desktop to the Sekoia MCP Server](/mcp/connect_claude_desktop.md): Configure Claude Desktop.
* [Connect Claude Code to the Sekoia MCP Server](/mcp/connect_claude_code.md): Configure Claude Code.
