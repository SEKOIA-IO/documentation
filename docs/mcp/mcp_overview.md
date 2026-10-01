# Sekoia MCP Server

The Sekoia MCP Server exposes your Sekoia.io data to AI assistants and agents through the Model Context Protocol (MCP), an open standard that lets a language model call tools hosted by a remote service. With it, an MCP client such as Claude Desktop or Claude Code can read alerts, cases, rules and events, run SOL queries and search Sekoia.io threat intelligence on your behalf, using an API key you control.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

## How it works

The server is a remote MCP endpoint hosted by Sekoia.io. Nothing runs in your environment except the MCP client you already use.

| | |
|---|---|
| **Endpoint** | `https://api.sekoia.io/v1/generative/mcp/` |
| **Transport** | Streamable HTTP (MCP protocol version `2025-06-18`) |
| **Authentication** | `Authorization: Bearer <API key>` header, using a Sekoia.io API key |
| **Server name** | `Sekoia.io SOC Platform` |
| **Access** | Read-only |

!!! warning "Keep the trailing slash"
    The endpoint URL ends with `/`. Without it, the server answers with an HTTP 307 redirect that most MCP clients do not follow, and the connection fails with an error that looks like an authentication problem.

When you connect a client, the server lists the tools your API key is allowed to use. The client then calls those tools as needed to answer your prompts, and the results come back into your conversation.

## What you can do

The server groups its tools in two families. See [MCP tools](/mcp/tools_reference.md) for parameters and examples.

| Family | Tools | Typical question |
|---|---|---|
| **SOC data** | `get_alert`, `get_case`, `get_events_from_alert`, `get_rule`, `run_sol_query` | "What is behind alert AL2h7Kq9pXmW and when did this user last log in?" |
| **Threat intelligence** | `search_cti`, `get_cti_object_by_id`, `get_cti_object_relationships_by_id`, `get_cti_object_reports_by_id`, `search_observables` | "Is this IP known to Sekoia.io, and which intrusion set uses it?" |

All tools are read-only. The server does not change alert or case status, add comments, run playbooks or modify any configuration.

## Access control

Access is governed by the API key you give to the client:

- **Permissions decide the tool list.** Sekoia.io API keys are permissions-based. A key that only holds the `View intelligence` permission exposes the threat intelligence tools and nothing else. A key with `View alerts`, `View cases`, `View Rules Catalog`, `View events` and the query builder permissions (`View query builder data sources`, `Execute query`) also exposes the SOC data tools. See [MCP tools](/mcp/tools_reference.md) for the permission each tool requires.
- **One key, one community.** The client sees the data of the community the key belongs to. To work with several communities, create one key per community and configure one server entry per key.
- **Admins create keys.** Only users with an admin role can create API keys, from **Settings > Workspace > API Keys**. See [Manage API keys](/getting_started/manage_api_keys.md).

!!! tip "Least privilege"
    Create a dedicated key for MCP usage with only the permissions you need, give it an expiration date and revoke it when the assistant no longer needs access.

## Your data

The Sekoia MCP Server does not send your data to any language model on its own. Your MCP client initiates every request, and the results go to the model that client uses, which you choose and configure. You keep control through the API key: you decide which permissions it holds, when it expires and when it is revoked.

If your organization restricts where security data may be processed, connect the server only from clients whose model hosting meets your requirements.

## Limits

- **Read-only.** Response actions and status changes are not available through MCP.
- **API key only.** The server does not provide OAuth yet. Clients that only accept OAuth connectors, such as the Claude Desktop custom connector interface, need a local proxy. See [Connect Claude Desktop to the Sekoia MCP Server](/mcp/connect_claude_desktop.md).
- **Same rate limits as the API.** Tool calls count against the rate limits of the Sekoia.io API.
- **Large results.** Broad SOL queries or relationship graphs of well-connected objects can return more data than a model can process at once. Add filters, limits and target types to your prompts.

## Use cases

- **Assisted triage.** Ask for an alert, its events and the rule behind it, then let the assistant summarize what it found.
- **Exposure check.** Search a threat actor, pull the malware and infrastructure related to it, then look up your own indicators.
- **Threat hunting.** Draft and run SOL queries in natural language, iterate on the results without leaving your terminal.
- **Intelligence briefs.** Collect the reports referencing a malware family or an intrusion set and build a summary for your stakeholders.

## Related articles

* [Getting started with the Sekoia MCP Server](/mcp/getting_started.md): Triage an alert end to end from Claude Code, step by step.
* [Connect Claude Desktop to the Sekoia MCP Server](/mcp/connect_claude_desktop.md): Configure Claude Desktop on macOS or Windows.
* [Connect Claude Code to the Sekoia MCP Server](/mcp/connect_claude_code.md): Add the server to Claude Code with one command.
* [MCP tools](/mcp/tools_reference.md): Parameters, permissions and examples for every tool.
* [SOC how-to guides](/mcp/how_to_soc.md): Recipes for alerts, cases, rules and SOL queries.
* [Threat intelligence how-to guides](/mcp/how_to_cti.md): Recipes for exposure checks, indicator enrichment and threat briefs.
* [Manage API keys](/getting_started/manage_api_keys.md): Create, scope and revoke the API keys the server relies on.
* [Sekoia Operating Language (SOL)](/xdr/features/investigate/sol_overview.md): The query language behind `run_sol_query`.
