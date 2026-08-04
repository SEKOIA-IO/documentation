# Filter logs with Rsyslog or Syslog-ng

Rsyslog and Syslog-ng let you drop unwanted events at the forwarder level, before they reach Sekoia. Filtering here reduces both network bandwidth and the volume counted against your license allowance, making it more effective than platform-level optimization rules.

## Prerequisites

- A working Sekoia Forwarder deployment using Rsyslog or Syslog-ng. See [Sekoia Forwarder documentation](/integration/ingestion_methods/sekoiaio_forwarder.md) for setup instructions.
- Access to the host running the forwarder.
- Familiarity with the event structure of the log source you want to filter.

!!! warning "Dropped events are unrecoverable"
    Events discarded at the forwarder level are gone permanently. Test your filter on a non-production source or a copy of recent logs before applying it to a live pipeline.

## Understand what to filter

Before writing any configuration, identify the events you want to drop. Good candidates are:

- High-frequency, low-security-value events (successful local logons, DNS heartbeats, monitoring agent health checks).
- Events from specific processes or hosts that are known-safe and generate no actionable alerts.
- Debug or informational log levels from firewalls and cloud services that you cannot disable at the source.

To find those events, use **Events > Search** in Sekoia and sort by volume per event type or source. The [investigate overusage playbook](/xdr/usecases/playbook/investigate_overusage.md) describes this process in detail.

---

## Filter with Rsyslog

Rsyslog evaluates rules top-to-bottom inside a ruleset. You can add a `stop` action (or a `discard` in older versions) that discards matching messages before they reach the output action.

### Add a filter to an existing ruleset

1. Locate your intake's ruleset file inside the forwarder. When using the Sekoia Forwarder Docker image, custom configurations are placed under `/extended_conf/`.

2. Open the ruleset file for the intake you want to filter. The file uses a name matching the intake, for example `ruleset-windows-events.conf`.

3. Add a filter block **before** the `action` block that forwards events to Sekoia. The filter uses an `if` statement with a `stop` action:

    ````
    # Drop event ID 4634 (logoff) where the logon type is network (type 3)
    if ($!event.code == 4634) and ($!action.properties.LogonType == 3) then stop
    ````

    Replace the field names and values with the fields relevant to your event type.

    !!! note "Field names in Rsyslog"
        Rsyslog accesses parsed JSON fields using the `$!fieldname` syntax. For nested fields, use `$!parent.child` notation, for example `$!action.properties.LogonType`.

4. To filter by a string value, use string comparison:

    ````
    # Drop all events from the monitoring agent process
    if ($!process.name == "monitoring-agent.exe") then stop
    ````

5. To filter by a list of values, chain conditions with `or`:

    ````
    # Drop DNS, process creation and file creation events
    if (
      $!action.name == "dns-query-result"
      or $!action.name == "process-created"
      or $!action.name == "file-created"
    ) then stop
    ````

6. Save the file, then restart the forwarder to apply the change:

    ````bash
    docker compose restart
    ````

7. Verify that events matching your filter no longer appear in **Events > Search** for that intake after a few minutes.

??? example "Complete ruleset with a filter block"
    This example shows a full ruleset file structure with a filter added before the forwarding action.

    ```
    ruleset(name="ruleset-windows-events"
        queue.type="LinkedList"
        queue.filename="sekoia_windows_events_queue"
        queue.size="10000"
        queue.saveOnShutdown="on"
        queue.spoolDirectory="/var/spool/rsyslog/queue_buffer"
    ) {
        # Drop successful network logoffs — high volume, low value
        if ($!event.code == 4634) and ($!action.properties.LogonType == 3) then stop

        action(
            name="output-windows-events"
            type="omfwd"
            protocol="tcp"
            target="intake.sekoia.io"
            port="10514"
            TCP_Framing="octet-counted"
            StreamDriver="gtls"
            StreamDriverMode="1"
            StreamDriverAuthMode="x509/name"
            StreamDriverPermittedPeers="intake.sekoia.io"
            Template="SEKOIAIO_windows_events_Template"
        )
    }
    ```

---

## Filter with Syslog-ng

Syslog-ng uses `filter` blocks and `log` path conditions to control which messages reach a destination.

### Add a filter to an existing log path

1. Locate your Syslog-ng configuration file. On the Sekoia Forwarder, this is typically `/etc/syslog-ng/conf.d/sekoia.conf` or a file in `/extended_conf/`.

2. Define a filter that matches the events you want to **drop**. Syslog-ng filters match messages to include, so you negate the filter when attaching it to the log path:

    ````
    # Define the filter: events to DROP
    filter f_drop_monitoring {
        match("monitoring-agent" value("PROGRAM"));
    };
    ````

    For JSON-parsed fields, use the `json-parser` and reference fields with the `$` prefix:

    ````
    filter f_drop_logoff_network {
        match("4634" value("$.event.code"))
        and match("3" value("$.action.properties.LogonType"));
    };
    ````

3. Apply the filter to your log path using `!` (NOT) so matching messages are excluded:

    ````
    log {
        source(s_windows_events);
        filter(!f_drop_monitoring);
        destination(d_sekoia_intake);
    };
    ````

4. Reload the Syslog-ng configuration:

    ````bash
    syslog-ng-ctl reload
    ````

5. Verify that events matching your filter no longer appear in **Events > Search** for that intake.

---

## Validate the impact

After applying a filter, confirm the reduction is working as expected:

1. In Sekoia, go to **Home > Settings > Usage** and check the volume trend for the affected intake over the next 24 hours.
2. Use **Events > Search** with the same filter criteria to confirm no matching events are arriving.
3. If events are still arriving, check the forwarder logs for configuration errors:

    ````bash
    # Rsyslog
    docker logs <forwarder_container_name> 2>&1 | grep -i error

    # Syslog-ng
    docker logs <forwarder_container_name> 2>&1 | grep -i error
    ````

---

## Related articles

- [Log volume and fair use](/getting_started/log_volume_and_fair_use.md): Overview of volume allowances and when to apply each filtering level.
- [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md): How to choose the right filtering level for your situation.
- [Reduce event volume with the Sekoia Endpoint Agent](/integration/categories/endpoint/reduce_event_volume_endpoint_agent.md): How to filter events at the agent level for endpoint sources.
- [Create an optimization rule](/xdr/features/collect/create_optimization_rule.md): How to create a platform-level optimization rule when forwarder-level filtering is not applicable.
- [Investigate overusage](/xdr/usecases/playbook/investigate_overusage.md): How to identify which sources are driving unexpected volume.
