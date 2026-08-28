# Connect Claude Desktop to the Sekoia MCP Server

This article explains how to add the Sekoia MCP Server to Claude Desktop on macOS or Windows. Because the server authenticates with an API key rather than OAuth, the configuration goes through the `claude_desktop_config.json` file and a small local proxy, `mcp-remote`, that injects the authorization header.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

## Prerequisites

- A Sekoia.io API key with the permissions matching the tools you need. For the threat intelligence tools, the key needs the `View intelligence` permission; for the SOC data tools, see [MCP tools](/mcp/tools_reference.md). See [Manage API keys](/getting_started/manage_api_keys.md).
- Claude Desktop installed.
- Node.js LTS installed, so that `npx` is available.

!!! warning "Do not use the custom connector interface"
    The **Custom Connector** dialog in Claude Desktop only supports OAuth. It tries to register with the Sekoia.io endpoint, fails with an "unable to register with connection service" error, and adding a client ID does not help. Use the configuration file method described below.

## Install Node.js

Skip this section if `npx` already works on your machine.

1. Download the LTS installer from [nodejs.org](https://nodejs.org).
2. Run the installer and accept the defaults.
3. Verify the installation:

=== "macOS"

    ```bash
    which npx
    ```

    Note the path returned, for example `/opt/homebrew/bin/npx`. You may need it later.

=== "Windows"

    ```powershell
    npx --version
    ```

    A version number confirms that `npx` is on your `PATH`.

## Open the configuration file

1. Open Claude Desktop.
2. Navigate to **Settings > Developer**.
3. Click **Edit Config**.

Claude Desktop opens, or creates, the configuration file:

=== "macOS"

    ```
    ~/Library/Application Support/Claude/claude_desktop_config.json
    ```

=== "Windows"

    ```
    %APPDATA%\Claude\claude_desktop_config.json
    ```

## Add the server

!!! warning "Merge, do not overwrite"
    If the file already contains an `mcpServers` block, add the `sekoia-mcp` entry inside it. Replacing the file removes your other servers.

!!! tip "Keep the key out of the file"
    Store the API key in an environment variable rather than inline, especially if the configuration file lives in a synced folder or a dotfiles repository. Treat the key like a password: if it is ever shared in plain text, revoke it and create a new one.

To add the server, insert the following block and replace `YOUR_API_KEY` with your Sekoia.io API key:

=== "macOS"

    ```json
    {
      "mcpServers": {
        "sekoia-mcp": {
          "command": "npx",
          "args": [
            "-y",
            "mcp-remote@latest",
            "https://api.sekoia.io/v1/generative/mcp/",
            "--header",
            "Authorization:${SEKOIA_AUTH_HEADER}"
          ],
          "env": {
            "SEKOIA_AUTH_HEADER": "Bearer YOUR_API_KEY"
          }
        }
      }
    }
    ```

=== "Windows"

    Define the variable once in an elevated terminal, then reference it from the configuration:

    ```powershell
    setx SEKOIA_AUTH_HEADER "Bearer YOUR_API_KEY"
    ```

    ```json
    {
      "mcpServers": {
        "sekoia-mcp": {
          "command": "npx",
          "args": [
            "-y",
            "mcp-remote@latest",
            "https://api.sekoia.io/v1/generative/mcp/",
            "--header",
            "Authorization:${SEKOIA_AUTH_HEADER}"
          ]
        }
      }
    }
    ```

## Restart Claude Desktop

Claude Desktop only reads the configuration file when it starts. Closing the window is not enough.

=== "macOS"

    1. Click the Claude icon in the menu bar.
    2. Click **Quit**.
    3. Open Claude Desktop again.

=== "Windows"

    1. Right-click the Claude icon in the system tray.
    2. Click **Quit**.
    3. If a `Claude.exe` process remains in Task Manager, end it.
    4. Open Claude Desktop again.

## Verify the connection

1. Start a new conversation.
2. Open **Search & Tools**.
3. Check that `sekoia-mcp` appears with its list of tools.

The tools listed depend on the permissions of your API key. If only the threat intelligence tools appear, the key lacks the `View alerts`, `View cases`, `View Rules Catalog`, `View events` or query builder permissions.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `Invalid OAuth error response: ... 404 page not found` | The endpoint URL has no trailing slash, so the server redirects and `mcp-remote` reads the redirect as an authentication error | Use `https://api.sekoia.io/v1/generative/mcp/` with the trailing `/` |
| `Failed to spawn process: No such file or directory` | Claude Desktop cannot find `npx`. On macOS, applications started from the Dock do not inherit the shell `PATH`. On Windows, a fresh `PATH` is only read after a restart | On macOS, replace `"command": "npx"` with the absolute path returned by `which npx`. On Windows, restart the machine or at least the terminal and Claude Desktop |
| The server does not appear after editing the file | Claude Desktop was not fully restarted, or the JSON is invalid | Quit Claude Desktop completely and relaunch it. Validate the JSON syntax |
| The server appears but a tool returns an authorization error | The API key lacks the permission for that tool, or the key expired | Check the key in **Settings > Workspace > API Keys** and its permissions |

Logs are available in:

=== "macOS"

    ```
    ~/Library/Logs/Claude/
    ```

=== "Windows"

    ```
    %APPDATA%\Claude\logs\
    ```

To confirm that the key and the endpoint work independently of Claude Desktop, send an MCP `initialize` request from a terminal:

=== "macOS"

    ```bash
    curl -iL -X POST https://api.sekoia.io/v1/generative/mcp/ \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -H "Accept: application/json, text/event-stream" \
      -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}'
    ```

=== "Windows"

    ```powershell
    curl.exe -iL -X POST https://api.sekoia.io/v1/generative/mcp/ `
      -H "Authorization: Bearer YOUR_API_KEY" `
      -H "Content-Type: application/json" `
      -H "Accept: application/json, text/event-stream" `
      -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}'
    ```

A `200 OK` response whose body contains `"serverInfo":{"name":"Sekoia.io SOC Platform"` confirms that the server side works. Any remaining issue is in the local configuration.

## Related articles

* [Sekoia MCP Server](/mcp/mcp_overview.md): What the server exposes, how access control works and its current limits.
* [Connect Claude Code to the Sekoia MCP Server](/mcp/connect_claude_code.md): The command-line equivalent for Claude Code.
* [Getting started with the Sekoia MCP Server](/mcp/getting_started.md): A first investigation using the tools.
* [MCP tools](/mcp/tools_reference.md): Parameters and permissions for every tool.
* [Manage API keys](/getting_started/manage_api_keys.md): Create, scope and revoke API keys.
