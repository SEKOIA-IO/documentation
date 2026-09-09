# Filter logs with Rsyslog

If you forward logs to Sekoia using a standalone Rsyslog instance that you manage directly, you can add filter rules to drop unwanted events before they leave your infrastructure. Filtering here reduces both network bandwidth and the volume counted against your license allowance.

!!! note "This article is for standalone Rsyslog deployments"
    If you use the Sekoia Forwarder Docker image, see [Reduce volume in the Sekoia Forwarder](/integration/ingestion_methods/syslog/filter_logs_with_sekoia_forwarder.md) instead. The Forwarder runs Rsyslog internally and uses a different configuration mechanism.

## Prerequisites

- A standalone Rsyslog instance forwarding logs to Sekoia, as described in [Rsyslog](/integration/ingestion_methods/syslog/rsyslog.md).
- Root or sudo access to the host running Rsyslog.
- Familiarity with the event structure of the log source you want to filter.

!!! warning "Dropped events are unrecoverable"
    Events discarded at the Rsyslog level are gone permanently. Test your filter on a non-production source or with a sample of recent logs before applying it to a live pipeline.

## Identify what to filter

Before writing any configuration, identify the events you want to drop. Good candidates are:

- High-frequency, low-security-value events (successful local logons, DNS heartbeats, monitoring agent health checks).
- Events from specific processes or hosts that are known-safe and generate no actionable alerts.
- Debug or informational log levels from firewalls and cloud services that cannot be disabled at the source.

Use **Events > Search** in Sekoia, filter by the intake you want to optimize, and sort by event count to find the highest-volume event types. The [investigate overusage playbook](/xdr/usecases/playbook/investigate_overusage.md) describes this process in detail.

## Add a filter to an existing ruleset

Rsyslog evaluates rules top-to-bottom inside a ruleset. A `stop` action discards the matching message before it reaches the forwarding action.

1. Locate the ruleset file for the intake you want to filter. Rsyslog configuration files are typically stored in `/etc/rsyslog.d/`.

2. Open the file and add a filter block **before** the `action` block that forwards events to Sekoia:

    ````
    # Drop event ID 4634 (logoff) where the logon type is network (type 3)
    if ($!event.code == 4634) and ($!action.properties.LogonType == 3) then stop
    ````

    !!! note "Field names in Rsyslog"
        Rsyslog accesses parsed JSON fields using the `$!fieldname` syntax. Use dot notation for nested fields: `$!action.properties.LogonType`.

3. To filter by a string value:

    ````
    # Drop all events from the monitoring agent process
    if ($!process.name == "monitoring-agent.exe") then stop
    ````

4. To filter by a list of values, chain conditions with `or`:

    ````
    # Drop DNS, process creation, and file creation events
    if (
      $!action.name == "dns-query-result"
      or $!action.name == "process-created"
      or $!action.name == "file-created"
    ) then stop
    ````

5. Save the file, then restart Rsyslog:

    ````bash
    sudo systemctl restart rsyslog
    ````

6. Verify that events matching your filter no longer appear in **Events > Search** for the affected intake after a few minutes.

??? example "Complete ruleset with a filter block"

    ```
    ruleset(name="ruleset-windows-events"
        queue.type="LinkedList"
        queue.filename="sekoia_windows_events_queue"
        queue.size="10000"
        queue.saveOnShutdown="on"
        queue.spoolDirectory="/var/spool/rsyslog/queue_buffer"
    ) {
        # Drop successful network logoffs
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

## Validate the impact

After applying a filter:

1. Go to **Settings > Usage** in Sekoia and monitor the volume trend for the affected intake over the next 24 hours.
2. Use **Events > Search** with the same filter criteria to confirm no matching events are arriving.
3. If matching events are still arriving, check the Rsyslog logs for configuration errors:

    ````bash
    sudo journalctl -u rsyslog --since "10 minutes ago"
    ````

## Related articles

- [Rsyslog](/integration/ingestion_methods/syslog/rsyslog.md): How to set up a standalone Rsyslog instance to forward logs to Sekoia.
- [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md): How to choose the right filtering level for your situation.
- [Reduce volume in the Sekoia Forwarder](/integration/ingestion_methods/syslog/filter_logs_with_sekoia_forwarder.md): How to add pre-transmission filtering to the Sekoia Forwarder Docker image.
- [Create an optimization rule](/xdr/features/collect/create_optimization_rule.md): How to filter events at the platform level when forwarder-level filtering is not applicable.
- [Investigate overusage](/xdr/usecases/playbook/investigate_overusage.md): How to identify which sources and event types are driving unexpected volume.
