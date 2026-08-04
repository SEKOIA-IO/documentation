# Reduce event volume with the Sekoia Endpoint Agent

The Sekoia Endpoint Agent supports optimization rules that filter events directly on the host, before they are transmitted to the platform. Filtering at the agent level reduces both network bandwidth usage and the volume counted against your license allowance, making it more effective than platform-level optimization rules for endpoint sources.

## How agent-level optimization rules differ from platform-level rules

Both the Sekoia Endpoint Agent and the Sekoia platform support optimization rules, but they work at different points in the pipeline:

| | Agent-level rules | Platform-level rules |
|---|---|---|
| **Where filtering happens** | On the host, before transmission | At the Sekoia intake, after reception |
| **Volume impact** | Reduces network usage and ingestion volume | Reduces storage and detection load only |
| **Configuration method** | API only | Platform UI or API |
| **Applicable sources** | Sekoia Endpoint Agent intakes only | Any intake |
| **Field availability** | Parsed fields only | Parsed fields only |

!!! note "Use agent-level rules first for endpoint sources"
    If you are optimizing a Sekoia Endpoint Agent intake, configure agent-level rules before resorting to platform-level optimization rules. The impact on volume and bandwidth is greater.

## Prerequisites

- At least one Sekoia Endpoint Agent deployed and sending events.
- API access to your Sekoia community (an API key with the `SIC_WRITE_CONF_INTAKES` permission).
- The `format_uuid` for the Sekoia Endpoint Agent format: `250e4095-fa08-4101-bb02-e72f870fcbd1`.

## Understand what to filter

Good candidates for agent-level filtering are high-frequency, low-security-value events that the Endpoint Agent generates continuously:

- Process creation and process end events for known-safe, non-interactive processes (monitoring agents, update services, antivirus scanners).
- DNS query events for internal resolvers or known-safe domains.
- File creation events in temporary or cache directories with no security relevance.
- Network connection events between internal hosts on known management ports.

To find the highest-volume event types, use **Events > Search** in Sekoia, filter by your endpoint intake, and sort by event count. The [investigate overusage playbook](/xdr/usecases/playbook/investigate_overusage.md) describes this process in detail.

## Create an agent-level optimization rule

Agent-level optimization rules are created via the Sekoia API. The endpoint is:

```
POST https://api.sekoia.io/v1/sic/conf/intakes/optimization_rules/
```

Authenticate with your API key in the `Authorization` header.

### Scope options

You can target the rule at three levels of granularity:

=== "All agents in the community"

    Omit `intake_uuid` and `agent_id`. The rule applies to all Endpoint Agent intakes in the community.

    ```json
    {
      "format_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1",
      "community_uuid": "YOUR_COMMUNITY_UUID",
      "description": "Drop monitoring agent process events",
      "action": 1,
      "enabled": true,
      "filters": [
        {
          "field": "process.name",
          "operator": "==",
          "value": "monitoring-agent.exe"
        }
      ]
    }
    ```

=== "A specific intake"

    Add `intake_uuid` to scope the rule to one intake only.

    ```json
    {
      "format_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1",
      "intake_uuid": "YOUR_INTAKE_UUID",
      "community_uuid": "YOUR_COMMUNITY_UUID",
      "description": "Drop monitoring agent process events on server-intake",
      "action": 1,
      "enabled": true,
      "filters": [
        {
          "field": "process.name",
          "operator": "==",
          "value": "monitoring-agent.exe"
        }
      ]
    }
    ```

=== "A specific agent"

    Add `agent_id` to scope the rule to one individual agent.

    ```json
    {
      "format_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1",
      "agent_id": "YOUR_AGENT_ID",
      "community_uuid": "YOUR_COMMUNITY_UUID",
      "description": "Drop monitoring agent process events on this host",
      "action": 1,
      "enabled": true,
      "filters": [
        {
          "field": "process.name",
          "operator": "==",
          "value": "monitoring-agent.exe"
        }
      ]
    }
    ```

### Filter multiple conditions

All filters in the `filters` array are combined with AND logic. An event is dropped only if it matches every condition.

```json
{
  "format_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1",
  "community_uuid": "YOUR_COMMUNITY_UUID",
  "description": "Drop notepad txt file events",
  "action": 1,
  "enabled": true,
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

### Filter a list of values

Use the `in` operator to match against a list of values in a single filter condition.

```json
{
  "format_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1",
  "community_uuid": "YOUR_COMMUNITY_UUID",
  "description": "Drop high-volume low-value endpoint action types",
  "action": 1,
  "enabled": true,
  "filters": [
    {
      "field": "action.name",
      "operator": "in",
      "value": [
        "file-created",
        "connected-to",
        "dns-query-result",
        "process-created",
        "process-ended"
      ]
    }
  ]
}
```

!!! warning "Filter on process-created and process-ended carefully"
    Dropping all `process-created` events removes important forensic data. Target this filter at specific, known-safe process names rather than the entire event type.

## Known limitation: enriched fields are not available

Optimization rules are evaluated at parsing time, before enrichment runs. Fields added during enrichment, such as `sekoiaio.tags.*`, are not available when the rule is evaluated. A filter on an enriched field will never match and the rule will have no effect.

Use only fields that appear in the raw parsed event. To check which fields are available at parse time, inspect a raw event in **Events > Search** before you received it.

## Allow the agent to fetch rules

After you create a rule via the API, the agent must be allowed to fetch its configuration. Check your agent deployment policy to confirm the agent can reach the Sekoia API endpoint `api.sekoia.io` on port 443. The agent fetches updated rules at its next configuration poll cycle. A restart of the agent is not required, but forces an immediate fetch:

```bash
# Restart the agent service (Linux)
sudo systemctl restart sekoia-endpoint-agent

# Restart the agent service (Windows, run as Administrator)
Restart-Service -Name "SekoiaEndpointAgent"
```

## Validate the impact

After creating the rule:

1. Wait 5 to 10 minutes for the agent to fetch the updated configuration.
2. In Sekoia, go to **Events > Search**, filter by the affected intake, and verify that events matching your filter conditions no longer appear.
3. Go to **Home > Settings > Usage** and monitor the volume trend for the intake over the next 24 hours.

If matching events are still arriving after 15 minutes, check the agent logs for rule compilation errors. A misconfigured field path generates an error like `error getting field accessor for <field>: field <X> is not in a struct`, which means the field path is invalid for the parsed event structure.

## Related articles

- [Log volume and fair use](/docs/getting_started/log_volume_and_fair_use.md): Overview of volume allowances and when to apply each filtering level.
- [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md): How to choose the right filtering level for your situation.
- [Optimization rules overview](/xdr/features/collect/optimization_rules_overview.md): Overview of platform-level optimization rules and how they differ from agent-level rules.
- [Create an optimization rule](/xdr/features/collect/create_optimization_rule.md): How to create a platform-level optimization rule when agent-level filtering is not sufficient.
- [Investigate overusage](/xdr/usecases/playbook/investigate_overusage.md): How to identify which sources and event types are driving unexpected volume.
