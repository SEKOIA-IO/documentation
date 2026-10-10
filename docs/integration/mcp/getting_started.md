# Getting started with the Sekoia MCP Server

This tutorial walks you through a first investigation with the Sekoia plugins in Claude Code. By the end, you will have investigated an alert end to end in plain language: gathered everything on the alert, checked its indicators against Sekoia threat intelligence, followed the user in your events and summarised the case.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia plans to roll out this functionality to all environments soon.

## Scenario

A SentinelOne alert, `AL2h7Kq9pXmW`, was raised on a laptop in your community. You want to know what the EDR flagged, who is impacted, whether the indicators are known to Sekoia and what the user did afterwards. You will do all of it from your terminal.

The prompts below are examples. Write your own: Claude Code picks the skill that matches your question, and the skill calls the tools.

## Step 1: Install the plugins

Follow [Install the Sekoia plugins in Claude Code](/integration/mcp/install_claude_code.md) and install both `sekoia-soc` and `sekoia-cti`. Type `/mcp` to confirm that the `sekoia` server is connected and lists its tools.

For this tutorial, your API key needs the `View alerts`, `View cases`, `View events`, `View Rules Catalog`, `View intelligence`, `View query builder data sources` and `Execute query` permissions. If a step is skipped, the skill names the permission that is missing.

## Step 2: Get everything on the alert

=== "Prompt"

    ```
    Get everything on alert AL2h7Kq9pXmW.
    ```

=== "Result"

    The `alert-details` skill gathers the full record of the alert and presents it as facts, without a verdict:

    - **The alert**: title (for example *SentinelOne EDR Threat Detected (Malicious)*), status, urgency, detection type, first and last seen.
    - **The rule**: what it matches and whether it is a behavioral detection, a pass-through of the EDR verdict or a threat intelligence match, with its documented false positives.
    - **The entities from the events**: host `laptop-a1b2c3`, user `alex.martin`, a zero-byte `.lnk` file written by `onenote.exe` in a temporary folder, and the mitigation status of the agent.
    - **The threats** with their Sekoia intelligence context, the ATT&CK techniques and the linked case.

    It ends with the next pivots: the linked case, a hunt on the host or the user.

## Step 3: Check the indicators against threat intelligence

=== "Prompt"

    ```
    Are the file hash and the external IP from this alert known to Sekoia CTI? If they are, which threat are they linked to?
    ```

=== "Result"

    The `query` skill looks up the observables, then profiles the threat they indicate. It answers in a few sentences with the object IDs, the confidence, the dates and the Sekoia source of the evidence, and says plainly when a value is not in Sekoia intelligence.

!!! tip "Pivot further"
    Ask which malware and tools the threat uses, or which reports cover it, to build a short brief without leaving the session.

## Step 4: Follow the user in your events

=== "Prompt"

    ```
    Find the last successful login of the impacted user in the last 30 days, then show the activity on the host over the last 24 hours, grouped by event category.
    ```

=== "Result"

    The `sol-hunt` skill writes two bounded SOL queries, shows them, runs them with `run_sol_query` and reads the results back in words:

    ```shell
    events
    | where timestamp between (ago(30d) .. now())
    | where user.name == 'alex.martin' and event.category == 'authentication'
    | where action.outcome == 'success'
    | select timestamp, host.name, source.ip
    | order by timestamp desc
    | limit 1
    ```

    ```shell
    events
    | where timestamp between (ago(24h) .. now())
    | where host.name == 'laptop-a1b2c3'
    | aggregate count() by event.category
    | order by count desc
    | limit 20
    ```

    For example: a successful login from the internal network, followed by ordinary process creations and DNS resolutions. Each count comes with its time window; an empty result reads "no rows for that filter in that window", never "it never happened".

## Step 5: Summarise the case

=== "Prompt"

    ```
    Summarise the case linked to this alert as a timeline and a five-line narrative.
    ```

=== "Result"

    The `case-summary` skill returns the case status and priority, a timeline of its alerts in chronological order with the host, user and rule of each, the entities involved and a five-line narrative of facts. Its assessment, if any, is labelled as such.

## Outcome

In five prompts you have:

- Gathered the alert, its rule, its events and its entities
- Checked the indicators against Sekoia threat intelligence
- Reconstructed the user's activity after the alert
- Produced a case summary you can share with the next shift

You can now decide on the alert in the platform with the full context, or paste the summary into the case.

## What to try next

- Ask an exposure question: "Has Sekoia CTI on APT28 fired in our tenant over the last 30 days?" See [Check whether you were exposed to a threat](/integration/mcp/how_to_cti.md#check-whether-you-were-exposed-to-a-threat).
- Turn a FLINT report into a hunt pack. See [Hunt the behaviours of a FLINT report](/integration/mcp/how_to_cti.md#hunt-the-behaviours-of-a-flint-report).
- Save the SOL queries the assistant wrote as [saved queries](/xdr/features/investigate/create_manage_queries.md) for your team.

## Related articles

* [Sekoia MCP Server](/integration/mcp/overview.md): Use cases, how the server works, access control and limits.
* [Install in Claude Code](/integration/mcp/install_claude_code.md): Install the Sekoia plugins and connect the server.
* [SOC how-to guides](/integration/mcp/how_to_soc.md): Alerts, cases and SOL queries in plain language.
* [Threat intelligence how-to guides](/integration/mcp/how_to_cti.md): Explore, report and check your telemetry.
* [Plugins and skills](/integration/mcp/plugins_skills.md): Every skill, what it is for and the permissions it needs.
* [Getting started with SOL](/xdr/features/investigate/sol_getting_started.md): Learn to write SOL queries yourself.
