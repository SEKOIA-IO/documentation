# Plugins and skills

The Sekoia plugins for Claude Code connect the Sekoia MCP Server and add skills. A skill is a set of instructions that Claude Code loads when your question matches it. It guides the assistant through the tools: which one to call and in which order, how to read the threat intelligence fields, and how to write valid SOL queries with the right fields and time bounds.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

The plugins are published in the [Sekoia marketplace for Claude Code](https://github.com/SEKOIA-IO/claude-marketplace). See [Install the Sekoia plugins in Claude Code](/integration/mcp/install_claude_code.md).

## Use a skill

Ask in plain language: Claude Code picks the skill whose description matches your question. You can also call a skill by name, with the plugin as a prefix, for example `/sekoia-cti:query` or `/sekoia-soc:sol-hunt`.

When the API key lacks a permission, the skill does what it can with the remaining tools, says which step it skipped and names the missing permission.

## sekoia-cti

| Skill | What it is for | Example prompt | Permissions | Output |
|---|---|---|---|---|
| `query` | Any threat intelligence lookup: actors, malware, indicators, vulnerabilities, sectors, campaigns, reports. Also checks whether a threat fired or appears in your telemetry | "What does Sekoia know about TeamTNT?" | `View intelligence`; add `View query builder data sources` and `Execute query` for the telemetry check | An answer in a few sentences with IDs, dates, confidence, sources and platform links |
| `exposure-assessment` | How an actor or a campaign exposes a sector or an organisation; sector technical RFIs | "Exposure assessment on TeamTNT for cloud-native SaaS providers" | `View intelligence` | Markdown report, evidence manifest, HTML, PDF |
| `threat-horizon-assessment` | How a threat theme will evolve over 3 to 12 months | "How will AI-enabled attacks evolve for the financial sector over 12 months?" | `View intelligence` | Markdown report, evidence manifest, HTML, PDF |
| `intelligence-delta` | What Sekoia.io adds that a generic feed does not, demonstrated on one finding | "Prove the intelligence delta for an MSSP" | `View intelligence` | Markdown brief, evidence manifest, HTML, PDF |
| `evidence-protocol` | Applied by the report skills: claim types, retrieval states, boundaries, evidence manifest, rendering | Used automatically | `View intelligence` | The rules and the HTML template |
| `report-hunt` | Turn a FLINT report into a hunt pack for your community | "Build a hunt pack from FLINT 2026-011" | `View intelligence`, `View query builder data sources`, `Execute query` | Alerts already raised, telemetry coverage, built-in rules, bounded SOL queries |

## sekoia-soc

| Skill | What it is for | Example prompt | Permissions | Output |
|---|---|---|---|---|
| `alert-details` | Everything Sekoia.io holds on one alert | "Get everything on alert AL2h7Kq9pXmW" | `View alerts`, `View events`, `View Rules Catalog`; add the query builder permissions and `View intelligence` for cases, assets and threat profiles | Rule, events, entities, threats, linked cases and assets, as facts |
| `case-summary` | Brief an incident from a case | "Summarise case CA4mN8xQ2rTz" | `View cases`, `View events`; add the query builder permissions for the priority | Timeline, entities, priority, five-line narrative |
| `sol-hunt` | Any question on events, alerts, cases, assets or rules | "When did this user last log in?" | `View query builder data sources`, `Execute query` | The SOL query it ran and the result read back in words |

## Related articles

* [Install in Claude Code](/integration/mcp/install_claude_code.md): Install, update and remove the plugins.
* [SOC how-to guides](/integration/mcp/how_to_soc.md): The `sekoia-soc` skills in practice.
* [Threat intelligence how-to guides](/integration/mcp/how_to_cti.md): The `sekoia-cti` skills in practice.
* [MCP tools](/integration/mcp/tools_reference.md): The tools the skills call.
