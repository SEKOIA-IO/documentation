# Install the Sekoia plugins in Claude Code

This article explains how to connect Claude Code, Anthropic's command-line agent, to the Sekoia MCP Server with the Sekoia plugins. The plugins come from the Sekoia marketplace for Claude Code. Each one connects the server and adds skills that guide the assistant through Sekoia.io data.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

| Plugin | For | Skills |
|---|---|---|
| `sekoia-cti` | CTI analysts, detection engineers, anyone who needs Sekoia.io threat intelligence | `query`, `exposure-assessment`, `threat-horizon-assessment`, `intelligence-delta`, `evidence-protocol`, `report-hunt` |
| `sekoia-soc` | SOC analysts working alerts, cases and hunts on their community | `alert-details`, `case-summary`, `sol-hunt` |

Install the plugin that matches your work, or both. See [Plugins and skills](/integration/mcp/plugins_skills.md) for what each skill does.

## Prerequisites

- Claude Code installed and authenticated.
- A Sekoia.io API key with the permissions of the plugin you install (see below). Only admins can create keys; see [Manage API keys](/getting_started/manage_api_keys.md).

## Permissions

| Plugin | Permissions on the API key |
|---|---|
| `sekoia-cti` | `View intelligence`. Add `View query builder data sources` and `Execute query` to check your own telemetry (exposure checks and FLINT hunt packs) |
| `sekoia-soc` | `View alerts`, `View cases`, `View events`, `View Rules Catalog`, `View query builder data sources`, `Execute query`. Add `View intelligence` for the threat intelligence context of alerts |

A key with fewer permissions still works: the skills say which step they skipped and which permission is missing.

## Install the plugins

!!! warning "Keep the key out of your files"
    The plugins read the key from the `SEKOIA_API_KEY` environment variable when Claude Code starts. Never write the key into a `.mcp.json` file, a dotfiles repository or any file that could be committed. If the key is ever shared in plain text, revoke it and create a new one.

1. Export your API key in the shell that starts Claude Code:

    ```bash
    export SEKOIA_API_KEY="YOUR_API_KEY"
    ```

2. Start Claude Code, then add the Sekoia marketplace:

    ```
    /plugin marketplace add SEKOIA-IO/claude-marketplace
    ```

3. Install one or both plugins:

    ```
    /plugin install sekoia-cti@sekoia
    /plugin install sekoia-soc@sekoia
    ```

4. Restart Claude Code to load the plugins.

Installing both plugins registers the server once per plugin. This is harmless: the tools are namespaced per plugin.

## Verify the connection

Type `/mcp` in Claude Code. The `sekoia` server is listed as connected, with its tools.

The tools listed depend on the permissions of your API key. If only the threat intelligence tools appear, the key lacks the SOC permissions listed above.

## Use the skills

Ask in plain language. Claude Code picks the matching skill, which calls the tools for you:

```
What does Sekoia know about TeamTNT?
```

```
Get everything on alert AL2h7Kq9pXmW.
```

You can also call a skill by name, for example `/sekoia-cti:query` or `/sekoia-soc:sol-hunt`.

See the [SOC how-to guides](/integration/mcp/how_to_soc.md) and the [Threat intelligence how-to guides](/integration/mcp/how_to_cti.md) for more prompts.

## Update the plugins

Refresh the marketplace, then update each installed plugin. From a terminal:

```bash
claude plugin marketplace update sekoia
claude plugin update sekoia-cti@sekoia
claude plugin update sekoia-soc@sekoia
```

Inside Claude Code, run `/plugin marketplace update sekoia`, then open `/plugin manage` to update the installed plugins. Restart Claude Code to load the new version.

## Remove the plugins

```
/plugin uninstall sekoia-cti@sekoia
/plugin uninstall sekoia-soc@sekoia
```

Revoke the API key in **Settings > Workspace > API Keys** if it is no longer needed.

## Connect without the plugins

To use the tools without the skills, add the server to Claude Code directly. The assistant then chooses the tools on its own, without the guidance of the skills.

!!! warning "Keep the trailing slash"
    The URL must end with `/`. Without it, the server redirects and the connection fails with an error that looks like an authentication problem.

```bash
export SEKOIA_API_KEY="YOUR_API_KEY"
claude mcp add --transport http --scope user sekoia-mcp \
  https://api.sekoia.io/v1/generative/mcp/ \
  --header "Authorization: Bearer $SEKOIA_API_KEY"
```

The `--scope user` option makes the server available in every project; omit it to register the server for the current project only. Run `claude mcp list` to check the connection, and `claude mcp remove sekoia-mcp` to remove it.

## Related articles

* [Sekoia MCP Server](/integration/mcp/overview.md): Use cases, how the server works, access control and limits.
* [Getting started with the Sekoia MCP Server](/integration/mcp/getting_started.md): A first investigation with the skills.
* [Plugins and skills](/integration/mcp/plugins_skills.md): Every skill, what it is for and the permissions it needs.
* [MCP tools](/integration/mcp/tools_reference.md): Parameters and permissions for every tool.
* [Manage API keys](/getting_started/manage_api_keys.md): Create, scope and revoke API keys.
