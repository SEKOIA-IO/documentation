# Investigate fair use overusage

The fair use policy ensures optimal performance and cost-predictability across the Sekoia.io platform. This guide explains how to identify the specific sources and events responsible for log volume that exceeds your community threshold.

## Prerequisites

* You have access to the **Usage** dashboard.
* You have the SOL (Sekoia.io Operating Language) permissions to query the `event_telemetry` and `events` datasources.

## Identify the community in overusage

To begin your investigation, you must confirm which community is exceeding its limits.

1. Navigate to **Operations > Usage**.
2. Compare the monthly community usage against the fair use threshold.

!!! note "Reference documentation"
    For more information on reading usage metrics, see the [Usage page documentation](https://docs.sekoia.io/getting_started/usage/).

## Identify the top-consuming intakes

Once you identify the community, you must determine if the volume is concentrated on specific intakes.

1. Navigate to **Operations > Query**.
2. Select the **event_telemetry** datasource.
3. Enter the following query to view the monthly volume evolution per intake:

```kusto
let earliestTime = ago(90d); 
let lastestTime = now();
event_telemetry 
| where bucket_start_date > earliestTime and bucket_start_date < lastestTime 
| aggregate total_message_volume = sum(total_message_size) by intake_uuid, date=month(bucket_start_date) 
| join intakes on intake_uuid == uuid 
| select date, intake.name, intake_uuid, total_message_volume_gb = round(total_message_volume / 1000 / 1000 / 1000, 0)
| order by date desc, total_message_volume_gb
| render linechart with (x=date, y=total_message_volume_gb, breakdown_by=intake.name)
```

4. Click **Run**.

## Analyze by intake dialect

If the volume is spread across multiple intakes, you must analyze the volume by dialect.

1. Navigate to **Operations > Query**.
2. Select the **event_telemetry** datasource.
3. Enter the following query:

```kusto
let earliestTime = ago(90d); 
let lastestTime = now();
event_telemetry 
| where bucket_start_date > earliestTime and bucket_start_date < lastestTime 
| aggregate total_message_volume = sum(total_message_size), make_set(intake_uuid) by intake_dialect_uuid, date=month(bucket_start_date) 
| join intakes on make_set_intake_uuid[0] == uuid 
| select date, intake_exemple_for_dialect=intake.name, total_message_volume_gb = round(total_message_volume / 1000 / 1000 / 1000, 0)
| order by date desc, total_message_volume_gb
| render linechart with (x=date, y=total_message_volume_gb, breakdown_by=intake_exemple_for_dialect)
```

4. Click **Run**.

## Drill down to specific events or assets

After identifying the intake or dialect, you must find the specific verbose logs or assets.

1. Navigate to **Operations > Query**.
2. Select the **events** datasource.
3. To filter by a specific dialect, enter a query similar to the following:

```kusto
events
| where timestamp between (?time.start .. ?time.end) and sekoiaio.intake.dialect == "fortinet fortigate"
| limit 100
```

4. Click **Run**.
5. Aggregate the data based on your specific needs to find the most frequent values.

??? example "Common aggregation queries"
    **By priority level:**
    ```kusto
    events 
    | where timestamp between (?time.start .. ?time.end) and sekoiaio.intake.dialect == "sonicwall firewall" 
    | aggregate count() by sonicwall.fw.priority  
    | order by count desc 
    ```

    **By event code:**
    ```kusto
    events 
    | where timestamp between (?time.start .. ?time.end) and sekoiaio.intake.dialect == "sekoia.io endpoint agent" 
    | aggregate count() by event.code 
    | order by count desc 
    ```

    **By host name:**
    ```kusto
    events 
    | where timestamp between (?time.start .. ?time.end) and sekoiaio.intake.dialect == "sekoia.io endpoint agent" 
    | aggregate count() by host.name 
    | order by count desc 
    ```

## Result

You have identified the specific logs, event codes, or hosts responsible for the volume increase. You can now apply filtering strategies to reduce the ingestion volume.

## See also
* [Optimization rules overview](/xdr/features/collect/optimization_rules_overview.md)to learn more about optimization rules.
* [Create an optimization rule](/xdr/features/collect/create_optimization_rule.md) to start creating your rule thanks to our step by step guide. 
