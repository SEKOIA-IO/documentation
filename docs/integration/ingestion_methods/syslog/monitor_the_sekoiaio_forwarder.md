# Monitor the Sekoia.io Forwarder

The Sekoia.io Forwarder can send health metrics to a dedicated Sekoia intake. These metrics help you monitor resource usage, queue size, and message processing before a queue reaches capacity.

## Prerequisites

Before you start, make sure that:

- The Sekoia.io Forwarder is deployed. See [Configure the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md).
- You can create an intake in your Sekoia community.
- You have access to the forwarder's `intakes.yaml` file.

## Create the monitoring intake

Create a `Sekoia.io forwarder logs` intake in your community and copy its intake key. For details about the intake format, see [Sekoia.io forwarder logs](/integration/categories/applicative/sekoiaio_forwarder_logs.md).

## Enable metrics

1. Open `intakes.yaml`.
2. Add a monitoring entry with `stats: True`:

    ````yaml
    ---
    intakes:
      - name: Monitoring
        stats: True
        intake_key: INTAKE_KEY_FOR_FORWARDER_LOGS
    ````

3. Recreate the forwarder:

    ````bash
    sudo docker compose up -d
    ````

The monitoring intake does not require a port or protocol. The forwarder generates the metrics internally.

## Monitor queue health

The forwarder uses the rsyslog `impstats` module to generate internal metrics for each configured intake. The metrics identify the intake that produced them.

The following detection rule pattern identifies full queues, which can cause event loss:

````yaml
detection:
  selection:
    - sekoiaio.forwarder.queue.discarded.full|gt: 0
    - sekoiaio.forwarder.queue.discarded.nf|gt: 0
    - sekoiaio.forwarder.queue.full|gt: 0
  condition: selection
````

For the complete list of counters, see the [rsyslog statistic counter documentation](https://www.rsyslog.com/doc/configuration/rsyslog_statistic_counter.html).

## Retrieve metrics during an outage

If the forwarder cannot send metrics to Sekoia, it retains a raw copy inside the container. Copy the file to the host:

````bash
sudo docker compose cp rsyslog:/var/log/rsyslog-stats.log rsyslog-stats.log
````

## Result

The forwarder sends its health metrics to the dedicated intake, where you can use them to monitor queue capacity and service interruptions.

## Related articles

- [Configure the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md): How to deploy the forwarder and configure its intake mappings.
- [Sekoia.io forwarder logs](/integration/categories/applicative/sekoiaio_forwarder_logs.md): Overview of the forwarder health intake.
- [Troubleshoot the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/troubleshoot_the_sekoiaio_forwarder.md): How to investigate missing events and connectivity issues.
