# Connect Claude Code to the Sekoia MCP Server

This article explains how to add the Sekoia MCP Server to Claude Code, Anthropic's command-line agent. Claude Code connects to remote HTTP servers natively and passes the authorization header itself, so no proxy is needed.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

## Prerequisites

- A Sekoia.io API key with the permissions matching the tools you need. See [Manage API keys](/getting_started/manage_api_keys.md) and the permission column of [MCP tools](/mcp/tools_reference.md).
- Claude Code installed and authenticated.

## Add the server

!!! tip "Keep the key out of your shell history and repositories"
    Export the key as an environment variable first, then reference the variable in the command. Never write the key into a project `.mcp.json` file that could be committed.

1. Export your API key:

    ```bash
    export SEKOIA_API_KEY="YOUR_API_KEY"
    ```

2. Add the server. The `--scope user` option makes it available in every project; omit it to register the server for the current project only:

    ```bash
    claude mcp add --transport http --scope user sekoia-mcp \
      https://api.sekoia.io/v1/generative/mcp/ \
      --header "Authorization: Bearer $SEKOIA_API_KEY"
    ```

!!! warning "Keep the trailing slash"
    The URL must end with `/`. Without it, the server redirects and the connection fails with an error that looks like an authentication problem.

## Verify the connection

1. List the configured servers:

    ```bash
    claude mcp list
    ```

    The output shows `sekoia-mcp` with its URL and a connection status.

2. Start Claude Code and type `/mcp` to see the server and the tools it exposes.

The tools listed depend on the permissions of your API key. If only the threat intelligence tools appear, the key lacks the `View alerts`, `View cases`, `View Rules Catalog`, `View events` or query builder permissions.

## Use the tools

Ask Claude Code in natural language. It selects and calls the tools for you:

```
Search Sekoia CTI for "TeamTNT" and summarize what is known about this intrusion set.
```

```
Fetch alert AL2h7Kq9pXmW, its events and the rule that raised it, then tell me whether it looks like a false positive.
```

For a complete walkthrough, see [Getting started with the Sekoia MCP Server](/mcp/getting_started.md).

## Remove the server

To remove the server from Claude Code:

```bash
claude mcp remove sekoia-mcp
```

Revoke the API key in **Settings > Workspace > API Keys** if it is no longer needed.

## Related articles

* [Sekoia MCP Server](/mcp/mcp_overview.md): What the server exposes, how access control works and its current limits.
* [Connect Claude Desktop to the Sekoia MCP Server](/mcp/connect_claude_desktop.md): The desktop application equivalent.
* [Getting started with the Sekoia MCP Server](/mcp/getting_started.md): A first investigation using the tools.
* [MCP tools](/mcp/tools_reference.md): Parameters and permissions for every tool.
* [Manage API keys](/getting_started/manage_api_keys.md): Create, scope and revoke API keys.
