---
description: Review supported commands, arguments, and command-line options.
---

# Available arguments and options

Use this page to look up supported commands and flags for the Sekoia.io Endpoint Agent. It also shows the command syntax for each supported operating system.

### Display help

{% tabs %}
{% tab title="Windows" %}
```shell
.\agent-latest.exe -h
```
{% endtab %}

{% tab title="Linux" %}
```shell
agent -h
```
{% endtab %}

{% tab title="MacOS" %}
```shell
/Applications/SekoiaEndpointAgent.app/Contents/MacOS/SekoiaEndpointAgent -h
```
{% endtab %}
{% endtabs %}

### Usage

{% tabs %}
{% tab title="Windows" %}
```shell
.\agent-latest.exe <command> [<args>]
```
{% endtab %}

{% tab title="Linux" %}
```shell
agent-latest <command> [<args>]
```
{% endtab %}

{% tab title="MacOS" %}
```shell
/Applications/SekoiaEndpointAgent.app/Contents/MacOS/SekoiaEndpointAgent <command> [<args>]
```
{% endtab %}
{% endtabs %}

### Options

| Option     | Meaning                  |
| ---------- | ------------------------ |
| --help, -h | Display help and exit    |
| --version  | Display version and exit |

### Commands

| Command   | Meaning             |
| --------- | ------------------- |
| install   | Install the agent   |
| update    | Update the agent    |
| uninstall | Uninstall the agent |

### Related articles

* [Install the endpoint agent](install-the-endpoint-agent.md) Use the install commands for each supported platform.
* [Manage the endpoint agent](manage-the-endpoint-agent.md) Apply update and uninstall commands safely.
* [Troubleshoot](troubleshoot.md) Verify commands and collect diagnostics when a command fails.
