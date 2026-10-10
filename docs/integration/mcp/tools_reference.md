# MCP tools

This page lists every tool exposed by the Sekoia MCP Server, with its parameters, the permission it requires and an example prompt. All tools are read-only; your MCP client calls them on your behalf when a prompt needs Sekoia data.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia plans to roll out this functionality to all environments soon.

With the [Sekoia plugins for Claude Code](/integration/mcp/plugins_skills.md), the skills choose and chain these tools for you. This page is useful to understand what they call, or to use the tools from another MCP client.

## Summary

The server only lists the tools your API key is allowed to use. The permission names below are the labels shown in **Settings > Workspace > API Keys** when you create a key.

| Name | Description | Required permission |
| --- | --- | --- |
| [get_alert](#get_alert) | Retrieve an alert by its short ID | `View alerts` |
| [get_case](#get_case) | Retrieve a case with its alerts and events | `View cases` |
| [get_events_from_alert](#get_events_from_alert) | Retrieve the events behind an alert | `View alerts`, `View events` |
| [get_rule](#get_rule) | Retrieve a detection rule by its UUID | `View Rules Catalog` |
| [run_sol_query](#run_sol_query) | Run a SOL query and return its results | `View query builder data sources`, `Execute query` |
| [search_cti](#search_cti) | Search threat intelligence objects by keyword | `View intelligence` |
| [get_cti_object_by_id](#get_cti_object_by_id) | Retrieve a threat intelligence object | `View intelligence` |
| [get_cti_object_relationships_by_id](#get_cti_object_relationships_by_id) | Retrieve the relationships of an object | `View intelligence` |
| [get_cti_object_reports_by_id](#get_cti_object_reports_by_id) | Retrieve the reports referencing an object | `View intelligence` |
| [search_observables](#search_observables) | Look up observables and their indicated threats | `View intelligence` |

## SOC data tools

### get_alert

Retrieves an alert by its short ID.

**Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `alert_short_id` | string | Yes | The alert short ID, for example `AL2h7Kq9pXmW` |

**Returns** the alert: title, urgency, status, creation and update times, the rule that raised it (name, pattern, severity), the detection type, the mapped ATT&CK techniques and the first and last seen timestamps. The events are not included; use `get_events_from_alert`.

??? example "Example prompt"
    ```
    Fetch alert AL2h7Kq9pXmW and tell me which rule raised it and why.
    ```

### get_case

Retrieves a case by its short ID, with its alerts and their events. Alerts are sorted by creation date.

**Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `case_short_id` | string | Yes | The case short ID, for example `CA4mN8xQ2rTz` |
| `include_events` | boolean | No | Load the events linked to the case. Default `true`. Pass `false` for a faster answer when only the case and its alerts are needed: the events are then empty, not missing |

**Returns** the case details, the list of alerts and, unless `include_events` is `false`, the associated events.

??? example "Example prompt"
    ```
    Summarize case CA4mN8xQ2rTz: which hosts and users are involved, and what is the timeline?
    ```

### get_events_from_alert

Retrieves the events that triggered an alert, within a time window.

**Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `alert_short_id` | string | Yes | The alert short ID |
| `first_seen_at` | string or null | Yes | Start of the window, ISO 8601. Use the alert's `first_seen_at` |
| `last_seen_at` | string or null | Yes | End of the window, ISO 8601. Use the alert's `last_seen_at` |

**Returns** the list of events with their ECS fields (host, user, file, process, source and destination) and the raw fields of the intake.

??? example "Example prompt"
    ```
    Show me the events behind alert AL2h7Kq9pXmW. Which host and user are impacted?
    ```

### get_rule

Retrieves a detection rule by its UUID.

**Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `rule_uuid` | string | Yes | The rule UUID, as returned in the `rule` field of an alert |

**Returns** the rule: name, description, type, pattern, severity, effort, alert type and category, tags, datasources, ATT&CK references, similarity strategy, false positives and references, plus its enabled state and compilation status.

??? example "Example prompt"
    ```
    Get the rule behind this alert and explain what its pattern matches.
    ```

### run_sol_query

Runs a Sekoia Operating Language (SOL) query and returns the results with execution metadata.

**Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `query` | string | Yes | The SOL query to run |

**Returns** the query, a run UUID and the result rows.

!!! warning "Bound queries on events"
    Queries on the `events` and `eternal_events` tables must be bounded in time at both ends, for example `where timestamp between (ago(30d) .. now())`. A query with only `timestamp > ago(30d)` is rejected without running. Queries on `alerts` and `cases` accept `where created_at > ago(7d)`.

!!! tip "Keep results small"
    Aggregate before listing and add a `limit` to every query. A wide result set can exceed what your assistant can process in one response, and a query processes at most 10,000 rows.

??? example "Example prompt"
    ```
    Find the last successful login of user alex.martin in the past 30 days.
    ```

    Query generated by the assistant:

    ```shell
    events
    | where timestamp between (ago(30d) .. now())
    | where user.name == 'alex.martin' and event.category == 'authentication'
    | where action.outcome == 'success'
    | order by timestamp desc
    | limit 1
    ```

See [Sekoia Operating Language (SOL)](/xdr/features/investigate/sol_overview.md) for the syntax.

## Threat intelligence tools

### search_cti

Searches the threat intelligence database for objects matching a term: intrusion sets, malware, campaigns, vulnerabilities, reports and more.

**Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `term` | string | Yes | Free-text search term, for example a threat actor name or an alias |

**Returns** the matching STIX objects with their type, ID, name, aliases, description fields, external references and timestamps.

??? example "Example prompt"
    ```
    Search Sekoia CTI for "TeamTNT" and list the campaigns and reports associated with it.
    ```

### get_cti_object_by_id

Retrieves a threat intelligence object by its STIX ID.

**Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `object_id` | string | Yes | The STIX ID, for example `intrusion-set--21e01501-bbd1-4a6a-8efc-55d3a45f9d5a` |

**Returns** the full object: description, aliases, first and last seen, goals, resource level, targeted sectors and external references.

??? example "Example prompt"
    ```
    Give me the full profile of intrusion-set--21e01501-bbd1-4a6a-8efc-55d3a45f9d5a.
    ```

### get_cti_object_relationships_by_id

Retrieves the relationship graph around an object: the malware an intrusion set uses, the infrastructure a malware family relies on, the sectors and countries a campaign targets.

**Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `object_id` | string | Yes | The STIX ID of the object |
| `target_types` | array of strings | No | Restrict the related objects to these STIX types, for example `["malware", "tool"]` |

**Returns** the relationships and the related objects.

!!! tip "Filter well-connected objects"
    Major intrusion sets have hundreds of relationships. Ask for specific target types to keep the response readable.

??? example "Example prompt"
    ```
    Which malware and tools does this intrusion set use? Limit the relationships to malware and tool objects.
    ```

### get_cti_object_reports_by_id

Retrieves the reports referencing an object.

**Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `object_id` | string | Yes | The STIX ID of the object |

**Returns** the reports, with their name, publication date, description, linked objects, external references and attached files. For FLINT reports, the description is the introduction or the key takeaways; the full report is available as a PDF in the platform.

??? example "Example prompt"
    ```
    List the reports Sekoia published about this malware family, most recent first.
    ```

### search_observables

Looks up observables (IP addresses, domains, URLs, file hashes and more) in the threat intelligence database, with the threats they indicate.

**Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `searches` | array of strings | Yes | The observables to look up |
| `with_indicated_threats` | boolean | No | Include the threats each observable is linked to. Default `true` |

**Returns** the matching observables, their types, validity periods and, when requested, the intrusion sets, malware or campaigns they indicate.

??? example "Example prompt"
    ```
    Are 198.51.100.23 and onenote2.exe.lnk known to Sekoia, and which threat are they linked to?
    ```

## Related articles

* [Sekoia MCP Server](/integration/mcp/overview.md): Use cases, how the server works, access control and limits.
* [Plugins and skills](/integration/mcp/plugins_skills.md): The skills that call these tools for you.
* [SOC how-to guides](/integration/mcp/how_to_soc.md): Alerts, cases and SOL queries in plain language.
* [Threat intelligence how-to guides](/integration/mcp/how_to_cti.md): Explore, report and check your telemetry.
* [Install in Claude Code](/integration/mcp/install_claude_code.md): Install the Sekoia plugins and connect the server.
* [Sekoia Operating Language (SOL)](/xdr/features/investigate/sol_overview.md): The query language behind `run_sol_query`.
* [Manage API keys](/getting_started/manage_api_keys.md): Create, scope and revoke API keys.
