# Getting started with the Sekoia MCP Server

This tutorial walks you through a first investigation with the Sekoia MCP Server from Claude Code. By the end, you will have triaged an alert end to end in natural language: fetched the alert, read its events and its rule, checked the indicators against Sekoia.io threat intelligence and run a SOL query to close the loop.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

## Scenario

A SentinelOne alert, `AL2h7Kq9pXmW`, was raised on a laptop in your community. You want to know what the EDR flagged, who is impacted, whether the indicators are known to Sekoia.io and what the user did afterwards. You will do all of it from your terminal.

The prompts below are examples. Write your own; the assistant picks the tools it needs.

## Step 1: Connect Claude Code

Follow [Connect Claude Code to the Sekoia MCP Server](/mcp/connect_claude_code.md), then start a session and type `/mcp` to confirm that `sekoia-mcp` is connected and lists its tools.

For this tutorial, your API key needs the `View alerts`, `View events`, `View Rules Catalog`, `View intelligence`, `View query builder data sources` and `Execute query` permissions. If some tools are missing from the list, check the permissions of your key.

## Step 2: Fetch the alert

=== "Prompt"

    ```
    Fetch alert AL2h7Kq9pXmW from Sekoia and summarize it.
    ```

=== "What happens"

    The assistant calls `get_alert` with `alert_short_id = "AL2h7Kq9pXmW"` and summarizes the result: the title (for example *SentinelOne EDR Threat Detected (Malicious)*), the urgency, the current status, the rule and its pattern, the ATT&CK techniques and the first and last seen timestamps.

The alert itself does not carry the host or the user. That information lives in the events.

## Step 3: Read the events

=== "Prompt"

    ```
    Get the events behind this alert. Which host and user are impacted, and what did the EDR flag?
    ```

=== "What happens"

    The assistant calls `get_events_from_alert` with the alert short ID and the first and last seen timestamps it got in step 2. It reads the ECS fields of the event: `host.name`, `user.name`, `file.name`, `file.path`, `process.parent.name`, the detection engine and the mitigation status.

At this point you know, for example, that the flagged object is a zero-byte `.lnk` file written by `onenote.exe` in a temporary folder, on host `laptop-a1b2c3`, for user `alex.martin`, and that the agent runs in detect-only mode.

## Step 4: Read the rule

=== "Prompt"

    ```
    Show me the rule that raised this alert. What does it match, and does it document false positives?
    ```

=== "What happens"

    The assistant calls `get_rule` with the `rule.uuid` from the alert. It reports the rule type, the pattern, the severity, the datasources, the ATT&CK references and whether the `false_positives` field is filled.

You now understand whether the alert reflects a behavioral detection or a pass-through of the EDR verdict, which changes how much weight to give it.

## Step 5: Check the indicators against threat intelligence

=== "Prompt"

    ```
    Are the file hash and the external IP from these events known to Sekoia CTI? If they are, which threat are they linked to?
    ```

=== "What happens"

    The assistant calls `search_observables` with the hash and the IP in `searches`, keeping `with_indicated_threats` at its default. If an observable matches, it follows up with `search_cti` or `get_cti_object_by_id` on the indicated intrusion set and summarizes its profile.

!!! tip "Pivot further"
    Ask for the relationships of the intrusion set with `target_types` limited to `malware` and `tool`, or for its reports, to build a short brief without leaving the session.

## Step 6: Hunt with SOL

=== "Prompt"

    ```
    Find the last successful login of the impacted user in the last 30 days, then list the most recent activity on the host.
    ```

=== "What happens"

    The assistant writes and runs two SOL queries with `run_sol_query`:

    ```shell
    events
    | where timestamp > ago(30d)
    | where user.name == 'alex.martin' and event.category == 'authentication'
    | where action.outcome == 'success'
    | order by timestamp desc
    | limit 1
    ```

    ```shell
    events
    | where timestamp between (ago(1d) .. now())
    | where host.name == 'laptop-a1b2c3'
    | select timestamp, event.category, event.action, process.name, destination.ip
    | order by timestamp desc
    | limit 100
    ```

    It then reads the results back and relates them to the login time it found: a successful login from the internal IP, followed by ordinary process creations and DNS resolutions.

## Outcome

In six prompts you have:

- Retrieved the alert and its rule
- Identified the host, the user and the flagged file
- Checked the indicators against Sekoia.io threat intelligence
- Reconstructed the user's activity after the alert

You can now decide on the alert in the platform with the full context, or paste the assistant's summary into the case.

## What to try next

- Start from a case instead of an alert with `get_case`, and ask for a timeline across all its alerts.
- Ask an exposure question: "Are we exposed to intrusion set X?" and let the assistant chain the intelligence tools with `search_observables` on your own indicators.
- Save the SOL queries the assistant wrote as [saved queries](/xdr/features/investigate/create_manage_queries.md) for your team.

## Related articles

* [Sekoia MCP Server](/mcp/mcp_overview.md): What the server exposes, how access control works and its current limits.
* [MCP tools](/mcp/tools_reference.md): Parameters, permissions and examples for every tool.
* [SOC how-to guides](/mcp/how_to_soc.md): Recipes for alerts, cases, rules and SOL queries.
* [Threat intelligence how-to guides](/mcp/how_to_cti.md): Recipes for exposure checks, indicator enrichment and threat briefs.
* [Connect Claude Code to the Sekoia MCP Server](/mcp/connect_claude_code.md): Add the server to Claude Code.
* [Connect Claude Desktop to the Sekoia MCP Server](/mcp/connect_claude_desktop.md): Configure Claude Desktop.
* [Getting started with SOL](/xdr/features/investigate/sol_getting_started.md): Learn to write SOL queries yourself.
