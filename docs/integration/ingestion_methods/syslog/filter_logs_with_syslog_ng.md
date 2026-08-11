# Filter logs with Syslog-ng

If you forward logs to Sekoia using a standalone Syslog-ng instance that you manage directly, you can add filter rules to drop unwanted events before they leave your infrastructure. Filtering here reduces both network bandwidth and the volume counted against your license allowance.

!!! note "This article is for standalone Syslog-ng deployments"
    If you use the Sekoia Forwarder Docker image, see [Reduce volume in the Sekoia Forwarder](/integration/ingestion_methods/syslog/filter_logs_with_sekoia_forwarder.md) instead. The Forwarder does not use Syslog-ng.

## Prerequisites

- A standalone Syslog-ng instance forwarding logs to Sekoia, as described in [Syslog-ng](/integration/ingestion_methods/syslog/syslog-ng.md).
- Root or sudo access to the host running Syslog-ng.
- Familiarity with the event structure of the log source you want to filter.

!!! warning "Dropped events are unrecoverable"
    Events discarded at the Syslog-ng level are gone permanently. Test your filter on a non-production source or with a sample of recent logs before applying it to a live pipeline.

## Identify what to filter

Before writing any configuration, identify the events you want to drop. Good candidates are:

- High-frequency, low-security-value events (successful local logons, DNS heartbeats, monitoring agent health checks).
- Events from specific processes or hosts that are known-safe and generate no actionable alerts.
- Debug or informational log levels from firewalls and cloud services that cannot be disabled at the source.

Use **Events > Search** in Sekoia, filter by the intake you want to optimize, and sort by event count to find the highest-volume event types. The [investigate overusage playbook](/xdr/usecases/playbook/investigate_overusage.md) describes this process in detail.

## Add a filter to an existing log path

Syslog-ng uses `filter` blocks to define matching conditions, and `log` path conditions to control which messages reach a destination.

1. Locate your Syslog-ng configuration file. On most systems this is `/etc/syslog-ng/syslog-ng.conf` or a file inside `/etc/syslog-ng/conf.d/`.

2. Define a filter block that matches the events you want to **drop**:

    ````
    # Define events to DROP: monitoring agent process
    filter f_drop_monitoring {
        match("monitoring-agent" value("PROGRAM"));
    };
    ````

    For log sources where messages are parsed as JSON, reference individual fields using the `$` prefix after a `json-parser`:

    ````
    filter f_drop_logoff_network {
        match("4634" value("$.event.code"))
        and match("3" value("$.action.properties.LogonType"));
    };
    ````

3. Apply the filter to your log path using `!` (NOT), so matching messages are excluded from the forwarding destination:

    ````
    log {
        source(s_windows_events);
        filter(!f_drop_monitoring);
        destination(d_sekoia_intake);
    };
    ````

    To apply multiple filters in the same log path:

    ````
    log {
        source(s_windows_events);
        filter(!f_drop_monitoring);
        filter(!f_drop_logoff_network);
        destination(d_sekoia_intake);
    };
    ````

4. Test the configuration without restarting:

    ````bash
    syslog-ng --syntax-only
    ````

5. Reload Syslog-ng:

    ````bash
    systemctl reload syslog-ng
    ````

6. Verify that events matching your filter no longer appear in **Events > Search** for the affected intake after a few minutes.

??? example "Filter for a list of program names"

    ```
    filter f_drop_known_safe_programs {
        match("monitoring-agent" value("PROGRAM"))
        or match("health-check" value("PROGRAM"))
        or match("backup-agent" value("PROGRAM"));
    };

    log {
        source(s_servers);
        filter(!f_drop_known_safe_programs);
        destination(d_sekoia_intake);
    };
    ```

## Validate the impact

After applying a filter:

1. Go to **Settings > Usage** in Sekoia and monitor the volume trend for the affected intake over the next 24 hours.
2. Use **Events > Search** with the same filter criteria to confirm no matching events are arriving.
3. If matching events are still arriving, check the Syslog-ng logs for errors:

    ````bash
    journalctl -u syslog-ng --since "10 minutes ago"
    ````

## Related articles

- [Syslog-ng](/integration/ingestion_methods/syslog/syslog-ng.md): How to set up a standalone Syslog-ng instance to forward logs to Sekoia.
- [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md): How to choose the right filtering level for your situation.
- [Reduce volume in the Sekoia Forwarder](/integration/ingestion_methods/syslog/filter_logs_with_sekoia_forwarder.md): How to add pre-transmission filtering to the Sekoia Forwarder Docker image.
- [Create an optimization rule](/xdr/features/collect/create_optimization_rule.md): How to filter events at the platform level when forwarder-level filtering is not applicable.
- [Investigate overusage](/xdr/usecases/playbook/investigate_overusage.md): How to identify which sources and event types are driving unexpected volume.
