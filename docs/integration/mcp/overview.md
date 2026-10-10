# Sekoia MCP Server

The Sekoia MCP Server gives AI assistants read-only access to your Sekoia.io data through the Model Context Protocol (MCP), an open standard that lets a language model call tools hosted by a remote service. Ask in plain language: the assistant searches Sekoia.io threat intelligence, reads your alerts, cases, rules and events, and runs SOL queries for you, using an API key you control.

The recommended client is Claude Code with the **Sekoia plugins**. One install connects the server and adds skills that guide the assistant: which tool to call, how to read the threat intelligence fields and how to write valid SOL queries.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

## Use cases

### Threat intelligence

| Use case | What you get | Skill |
|---|---|---|
| [Explore Sekoia.io threat intelligence](/integration/mcp/how_to_cti.md#explore-sekoiaio-threat-intelligence) | Answers on actors, malware, indicators, vulnerabilities, sectors and campaigns, with the object IDs, confidence, dates and sources behind them | `query` |
| [Produce intelligence reports](/integration/mcp/how_to_cti.md#produce-intelligence-reports) | Exposure assessments, threat horizon assessments and intelligence delta briefs, as markdown, evidence manifest, HTML and PDF | `exposure-assessment`, `threat-horizon-assessment`, `intelligence-delta` |
| [Check whether you were exposed to a threat](/integration/mcp/how_to_cti.md#check-whether-you-were-exposed-to-a-threat) | The alerts Sekoia.io intelligence already raised on the threat in your community, and its indicators found in your events | `query` |
| [Hunt the behaviours of a FLINT report](/integration/mcp/how_to_cti.md#hunt-the-behaviours-of-a-flint-report) | A hunt pack: which behaviours your telemetry can see, which built-in rules cover them, and SOL queries for the rest | `report-hunt` |

### SOC

| Use case | What you get | Skill |
|---|---|---|
| [Get everything on an alert](/integration/mcp/how_to_soc.md#get-everything-on-an-alert) | The rule, events, hosts, users, files, network values, threats and linked cases of one alert, as facts | `alert-details` |
| [Summarise a case](/integration/mcp/how_to_soc.md#summarise-a-case) | A timeline of the case's alerts, the entities involved, its priority and a five-line narrative | `case-summary` |
| [Query your data in plain language](/integration/mcp/how_to_soc.md#query-your-data-in-plain-language) | A bounded SOL query written and run for you, shown so you can rerun it, with the result read back in words | `sol-hunt` |

## Get started

1. [Install the Sekoia plugins in Claude Code](/integration/mcp/install_claude_code.md).
2. Follow [Getting started with the Sekoia MCP Server](/integration/mcp/getting_started.md) for a first investigation.

Any other MCP client that can send a custom `Authorization` header can connect to the endpoint below. It gets the tools, not the skills.

## How it works

The server is a remote MCP endpoint hosted by Sekoia.io. Nothing runs in your environment except the MCP client you already use.

!!! warning "Keep the trailing slash"
    The endpoint URL ends with `/`. Without it, the server answers with an HTTP 307 redirect that most MCP clients do not follow, and the connection fails with an error that looks like an authentication problem.

| | |
|---|---|
| **Endpoint** | `https://api.sekoia.io/v1/generative/mcp/` |
| **Transport** | Streamable HTTP (MCP protocol version `2025-06-18`) |
| **Authentication** | `Authorization: Bearer <API key>` header, using a Sekoia.io API key |
| **Server name** | `Sekoia.io SOC Platform` |
| **Access** | Read-only |

When a client connects, the server lists the tools your API key is allowed to use. The client calls those tools as needed to answer your prompts, and the results come back into your conversation. See [MCP tools](/integration/mcp/tools_reference.md) for the full list.

All tools are read-only. The server does not change alert or case status, add comments, run playbooks or modify any configuration.

## Access control

Access is governed by the API key you give to the client:

- **Permissions decide the tool list.** Sekoia.io API keys are permissions-based. A key with only `View intelligence` exposes the threat intelligence tools. The SOC tools need `View alerts`, `View cases`, `View events`, `View Rules Catalog` and the query builder permissions (`View query builder data sources`, `Execute query`). See [Install in Claude Code](/integration/mcp/install_claude_code.md#permissions) for the permissions of each plugin.
- **One key, one community.** The client sees the data of the community the key belongs to. To work with several communities, create one key per community.
- **Admins create keys.** Only users with an admin role can create API keys, from **Settings > Workspace > API Keys**. See [Manage API keys](/getting_started/manage_api_keys.md).

!!! tip "Least privilege"
    Create a dedicated key for MCP usage with only the permissions you need, give it an expiration date and revoke it when the assistant no longer needs access.

## Your data

The Sekoia MCP Server does not send your data to any language model on its own. Your MCP client initiates every request, and the results go to the model that client uses, which you choose and configure. You keep control through the API key: you decide which permissions it holds, when it expires and when it is revoked.

If your organization restricts where security data may be processed, connect the server only from clients whose model hosting meets your requirements.

## Limits

- **Read-only.** Response actions and status changes are not available through MCP.
- **API key only.** The server does not provide OAuth yet. Clients that only support OAuth connectors cannot connect.
- **Same rate limits as the API.** Tool calls count against the rate limits of the Sekoia.io API. SOL queries also follow the Query Builder limits: 10 runs a minute and 10,000 processed rows per query.
- **Large results.** Broad SOL queries or relationship graphs of well-connected objects can return more data than a model can process at once. The skills narrow them; without the skills, add filters, limits and target types to your prompts.

## Related articles

* [Install in Claude Code](/integration/mcp/install_claude_code.md): Install the Sekoia plugins and connect the server.
* [Getting started with the Sekoia MCP Server](/integration/mcp/getting_started.md): Investigate an alert end to end from Claude Code.
* [SOC how-to guides](/integration/mcp/how_to_soc.md): Alerts, cases and SOL queries in plain language.
* [Threat intelligence how-to guides](/integration/mcp/how_to_cti.md): Explore, report and check your telemetry.
* [Plugins and skills](/integration/mcp/plugins_skills.md): Every skill, what it is for and the permissions it needs.
* [MCP tools](/integration/mcp/tools_reference.md): Parameters, permissions and examples for every tool.
* [Manage API keys](/getting_started/manage_api_keys.md): Create, scope and revoke the API keys the server relies on.
* [Sekoia Operating Language (SOL)](/xdr/features/investigate/sol_overview.md): The query language behind `run_sol_query`.
