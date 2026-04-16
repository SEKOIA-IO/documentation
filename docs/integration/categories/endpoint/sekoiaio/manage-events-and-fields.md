---
description: Configure optimization rules and review event-related reference content.
---

# Manage events and fields

The agent can ignore selected events before they leave the host. This page also centralizes event categories, fields, transformed samples, and example events.

### Ignore events with optimization rules

Optimization rules let you ignore events based on field values. You can define them locally in the agent configuration or centrally from the platform.

#### Optimization rule structure

Each optimization rule contains the following parts:

* A unique identifier in `uuid`
* An action code in `action`
* A list of `filters`

Inside the agent, only the ignore action is supported. Use `action: 1` to ignore matching events.

{% hint style="info" %}
String comparisons are case-sensitive.
{% endhint %}

#### Supported operators

| Operator code | Description                                           | Field type |
| ------------- | ----------------------------------------------------- | ---------- |
| ==            | The field value is equal to the value                 | all        |
| !=            | The field value is not equal to the value             | all        |
| contains      | The field value contains the value                    | string     |
| not contains  | The field value does not contain the value            | string     |
| >             | The field value is greater than the value             | number     |
| >=            | The field value is greater than or equal to the value | number     |
| <             | The field value is less than the value                | number     |
| <=            | The field value is less than or equal to the value    | number     |

#### Example local optimization rule

```yaml
- uuid: 30bb044d-f7ba-448a-81c2-7f3c41a1fbf9
  action: 1
  filters:
    - field: process.name
      operator: ==
      value: "notepad.exe"
    - field: file.extension
      operator: ==
      value: "txt"
```

{% hint style="info" %}
The performance impact of optimization rules is negligible. The agent applies them with minimal CPU and memory overhead.
{% endhint %}

#### Configure local optimization rules

1. Edit the configuration file:

{% include "../../../.gitbook/includes/endpoint-agent-configuration-file-paths.md" %}

2. Add the following configuration:

```yaml
OptimizationRules:
  - uuid: "30bb044d-f7ba-448a-81c2-7f3c41a1fbf9"
    action: 1
    filters:
      - field: process.name
        operator: ==
        value: "notepad.exe"
      - field: file.extension
        operator: ==
        value: "txt"
```

3. Restart the agent:

{% include "../../../.gitbook/includes/restart-the-endpoint-agent.md" %}

{% hint style="warning" %}
If the YAML configuration file is invalid, the agent logs an error. Invalid optimization rules are ignored. Invalid YAML stops the agent.
{% endhint %}

#### Configure remote optimization rules

Remote optimization rules are managed from the Sekoia.io platform.

{% hint style="info" %}
To manage optimization rules in the platform, you must have permission to manage intakes.
{% endhint %}

1. Edit the configuration file:

{% include "../../../.gitbook/includes/endpoint-agent-configuration-file-paths.md" %}

2. Add the following configuration:

```yaml
RemoteOptimizationRules: true
```

3. Restart the agent:

{% include "../../../.gitbook/includes/restart-the-endpoint-agent.md" %}

Once enabled:

* The agent fetches remote rules at startup and then every hour
* If the agent is offline, it retries when connectivity is restored
* Local and remote rules are merged and both are applied

#### Create optimization rules in the platform

Send a `POST` request to `https://api.sekoia.io/v1/sic/conf/intakes/optimization_rules/` with one of the following payloads.

{% tabs %}
{% tab title="For all agents from the community" %}
```json
{
  "format_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1",
  "description": "Ignore notepad txt files",
  "action": 1,
  "filters": [
    {
      "field": "process.name",
      "operator": "==",
      "value": "notepad.exe"
    },
    {
      "field": "file.extension",
      "operator": "==",
      "value": "txt"
    }
  ]
}
```
{% endtab %}

{% tab title="For a specific intake" %}
```json
{
  "intake_uuid": "your_intake_uuid",
  "format_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1",
  "description": "Ignore notepad txt files",
  "action": 1,
  "filters": [
    {
      "field": "process.name",
      "operator": "==",
      "value": "notepad.exe"
    },
    {
      "field": "file.extension",
      "operator": "==",
      "value": "txt"
    }
  ]
}
```
{% endtab %}

{% tab title="For a specific agent" %}
```json
{
  "agent_id": "your_agent_id",
  "format_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1",
  "description": "Ignore notepad txt files",
  "action": 1,
  "filters": [
    {
      "field": "process.name",
      "operator": "==",
      "value": "notepad.exe"
    },
    {
      "field": "file.extension",
      "operator": "==",
      "value": "txt"
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### Event categories, fields, and transformed samples

{!\_shared\_content/operations\_center/integrations/generated/250e4095-fa08-4101-bb02-e72f870fcbd1.md!}

### Event examples

{% tabs %}
{% tab title="Windows" %}
* Files creation and deletion
* File rename
* Process lifecycle
* Remote thread execution
* DNS resolution
* TCP connection
* PowerShell commands
* WMI activity
* NTLM
* Windows Defender events
* Sysmon events if configured
* ...
{% endtab %}

{% tab title="Linux" %}
* Root command execution
* File creation, deletion, rename, and change
* Process lifecycle
* TCP connection
* Python and Perl commands
* PIP and APT installs
* Cron configuration and scheduled jobs
* Sudoers file changes
* Passwd operations
* Suspicious activity such as `curl` and `wireshark`
* ...
{% endtab %}

{% tab title="MacOS" %}
* Root command execution
* File creation, deletion, rename, and change
* DNS resolution
* TCP connection
* PIP and APT installs
* Sudoers file changes
* Passwd operations
* Suspicious activity such as `curl` and `wireshark`
* ...
{% endtab %}
{% endtabs %}

### Related articles

* [Collect logs in files](collect-logs-in-files.md) Add file-based collection to the agent configuration.
* [Proxy support](proxy-support.md) Route agent traffic through a proxy when needed.
* [Troubleshoot](troubleshoot.md) Validate optimization rule behavior and inspect local logs.
