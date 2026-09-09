# Reduce volume in the Sekoia Forwarder

The Sekoia Forwarder is a Docker image that runs Rsyslog internally to collect and forward logs to Sekoia. You cannot edit its internal Rsyslog configuration directly. However, the Forwarder supports a custom configuration directory (`/extended_conf/`) where you can drop additional Rsyslog rules, including filters that drop events before they are transmitted.

This is an advanced technique intended for users who need to reduce volume at the forwarder host level and cannot use source-level filtering or platform-level optimization rules for their use case.

!!! warning "Platform-level optimization rules are simpler for most cases"
    If your goal is to reduce the number of events stored and processed by Sekoia, [platform-level optimization rules](/xdr/features/collect/create_optimization_rule.md) achieve this without touching the Forwarder configuration. Use the `/extended_conf/` approach only when you also need to reduce network bandwidth or when platform-level filtering is not sufficient.

!!! warning "Dropped events are unrecoverable"
    Events discarded in the Forwarder never reach Sekoia. They cannot be recovered. Test your filter carefully on a non-production intake before applying it to a live pipeline.

## Prerequisites

- The Sekoia Forwarder deployed and running as a Docker container. See [Sekoia Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md).
- Access to the host running the Forwarder Docker container.
- Familiarity with the intake name and the event structure of the log source you want to filter.

## Understand the /extended_conf/ directory

The Sekoia Forwarder supports importing custom Rsyslog configuration files from a dedicated directory. When this directory is mounted as a volume, the Forwarder's Rsyslog instance includes those files alongside its generated configuration.

To enable it, add the volume mount to your `docker-compose.yml`:

````yaml
services:
  forwarder:
    image: ghcr.io/sekoia-io/sekoiaio-docker-concentrator:latest
    volumes:
      - ./intake.yml:/intake.yml
      - ./extended_conf:/extended_conf    # ADD THIS LINE
````

Create the `extended_conf` directory next to your `docker-compose.yml`:

````bash
mkdir extended_conf
````

Any `.conf` file you place in this directory is loaded by Rsyslog when the container starts.

!!! note "Remove the intake from intake.yml when using /extended_conf/ for that intake"
    If you provide a custom Rsyslog configuration for an intake via `/extended_conf/`, remove that intake from `intake.yml` to avoid a configuration conflict. Two configurations targeting the same intake port will cause an error at startup.

## Create a filter file

1. Inside the `extended_conf` directory, create a new `.conf` file named after the intake you want to filter, for example `filter-windows.conf`.

2. Write the ruleset, placing the filter before the forwarding action. The following example drops Windows event ID 4634 (logoff) for network logon type 3:

    ````
    input(type="imtcp"
        port="YOUR_INTAKE_PORT"
        ruleset="ruleset-windows-filtered"
        name="input-windows-filtered"
        KeepAlive="on"
        KeepAlive.Interval="10"
        KeepAlive.Time="30"
    )

    template(name="SEKOIAIO_windows_filtered_Template"
        type="string"
        string="<%pri%>1 %timegenerated:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg:R,ERE,1,FIELD:^[ \t]*(.*)$--end%\n"
    )

    ruleset(name="ruleset-windows-filtered"
        queue.type="LinkedList"
        queue.filename="sekoia_windows_filtered_queue"
        queue.size="10000"
        queue.saveOnShutdown="on"
        queue.spoolDirectory="/var/spool/rsyslog/queue_buffer"
    ) {
        # Drop successful network logoffs — high volume, low security value
        if ($!event.code == 4634) and ($!action.properties.LogonType == 3) then stop

        action(
            name="output-windows-filtered"
            type="omfwd"
            protocol="tcp"
            target="intake.sekoia.io"
            port="10514"
            TCP_Framing="octet-counted"
            StreamDriver="gtls"
            StreamDriverMode="1"
            StreamDriverAuthMode="x509/name"
            StreamDriverPermittedPeers="intake.sekoia.io"
            Template="SEKOIAIO_windows_filtered_Template"
        )
    }
    ````

    Replace `YOUR_INTAKE_PORT` with the port used by this intake in `intake.yml`, and `YOUR_INTAKE_KEY` with the intake key from your Sekoia console.

3. Save the file.

4. Restart the Forwarder to apply the new configuration:

    ````bash
    docker compose restart
    ````

5. Check the Forwarder logs to confirm the configuration loaded without errors:

    ````bash
    docker logs <forwarder_container_name> 2>&1 | grep -i error
    ````

    A configuration error at startup prevents the Forwarder from running. If you see errors, check the syntax of your `.conf` file and verify that the intake was removed from `intake.yml`.

## Validate the impact

After restarting:

1. In Sekoia, go to **Events > Search**, filter by the affected intake, and verify that events matching your filter no longer appear.
2. Go to **Settings > Usage** and monitor the volume trend for the affected intake over the next 24 hours.

## Related articles

- [Sekoia Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md): How to deploy and configure the Sekoia Forwarder Docker image.
- [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md): How to choose the right filtering level for your situation.
- [Filter logs with Rsyslog](/integration/ingestion_methods/syslog/filter_logs_with_rsyslog.md): How to add filters to a standalone Rsyslog instance.
- [Create an optimization rule](/xdr/features/collect/create_optimization_rule.md): How to filter events at the platform level without touching the Forwarder configuration.
- [Investigate overusage](/xdr/usecases/playbook/investigate_overusage.md): How to identify which sources and event types are driving unexpected volume.
