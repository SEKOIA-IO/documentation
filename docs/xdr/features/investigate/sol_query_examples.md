# Query examples

## Join examples

### Join between events and communities tables (for Multi-tenant)

``` shell
events
| where timestamp > ago(5m)
| limit 100
| lookup communities on sekoiaio.customer.community_uuid == uuid
| select timestamp, sekoiaio.customer.community_uuid, community.name

```


### Join between events and entities tables

``` shell
events
| where timestamp > ago(24h)
| limit 100
| lookup entities on sekoiaio.entity.uuid == uuid
| aggregate count=count() by entity.name
| select entity.name, count

```


### Join between alerts and communities tables (for Multi-tenant)

``` shell
alerts
| aggregate count=count() by community_uuid
| lookup communities on community_uuid == uuid
| select community.name, community_uuid, count
| limit 100

```

### Join between events and intake_formats tables

``` shell
events
| where timestamp between (?time.start .. ?time.end)
| lookup intake_formats on sekoiaio.intake.dialect_uuid == uuid
| aggregate count() by intake_format.name
| limit 100
```


### Count events per intake format (event_telemetry)

``` shell
event_telemetry
| where bucket_start_date between (?time.start .. ?time.end)
| lookup intake_formats on intake_dialect_uuid == uuid
| aggregate sum(occurrences) by intake_format.name
| limit 100
```


### Data volume per intake format (event_telemetry)

``` shell
event_telemetry
| where bucket_start_date between (?time.start .. ?time.end)
| lookup intake_formats on intake_dialect_uuid == uuid
| aggregate sum(total_event_size) by intake_format.name
| limit 100
```


### Resolve intake format name from intakes

``` shell
intakes
| lookup intake_formats on format_uuid == uuid
| select name, intake_format.name
```


## Alerts query examples

### Detection rules ranked by number of alerts

``` shell
alerts
| where created_at > ago(30d)
| order by occurrences desc
| select rule_name, occurrences
| limit 100

```


### Assets ranked by number of alerts

``` shell
alerts
| where created_at > ago(30d)
| aggregate count=count() by assets.uuid
| order by count desc
| limit 100

```

### Threats ranked by number of alerts

``` shell
alerts
| where created_at > ago(30d)
| aggregate count=count() by threats.name
| order by count desc
| limit 100

```

### Alerts per detection type

``` shell
alerts
| where created_at > ago(30d)
| aggregate count() by detection_type

```

### Average time to detect in last 30 days

``` shell
alerts
| where created_at > ago(30d)
| aggregate avg(time_to_detect)

```


### Rename columns and convert time_to_detect in minutes

``` shell
alerts
| where time_to_detect != null
| select entity = entity_name, rule = rule_name, ttd = time_to_detect/60
| limit 10

```


### Ranking of communities by alerts

``` shell
alerts
| aggregate AlertCount = count() by community_uuid
| lookup communities on community_uuid == uuid
| order by AlertCount desc
| select community.name, AlertCount

```



## Assets query examples

### Filter assets with a specific tag

``` shell
assets
| where tags.tag in ["Admin"]
| limit 100
```


### Filter assets with multiple tags

``` shell
assets
| where tags.tag in ["Admin", "Backup"]
| limit 100
```


### List all distinct tags

``` shell
assets
| distinct tags.tag
| limit 100
```


### Filter assets where tag starts with a prefix

``` shell
assets
| where tags.tag startswith "Finance"
| limit 100
```


### Filter assets where tag contains a string (case-insensitive)

``` shell
assets
| where tags.tag contains~ "prod"
| limit 100
```

### Count assets per tag

``` shell
assets
| aggregate count() by tags.tag
| order by count desc
| limit 100
```

### Exclude assets with a specific tag

``` shell
assets
| where not tags.tag in ["Backup"]
| limit 100
```



## Events query examples

### Number of unique command lines per host.name

``` shell
events
| where timestamp > ago(24h)
| aggregate count=count_distinct(process.command_line) by host.name
| order by count desc
| limit 100

```

### Number of unique hostname per month

``` shell
events
| where timestamp > ago(90d)
| aggregate count=count_distinct(log.hostname) by month(timestamp)

```

### Top 10 visited URL

``` shell
events
| where timestamp >= ago(24h)
| aggregate count() by url.domain
| top 10 by count

```


### Top 10 blocked URL

``` shell
events
| where timestamp >= ago(24h) and event.action == 'blocked' and user.name != null and url.domain != null
| aggregate count() by url.domain
| top 10 by count

```

### Top 10 login failures on Windows

``` shell
events
| where timestamp > ago(24h) and event.code == 4625
| aggregate failed_login_count=count() by user.target.name
| top 10 by failed_login_count

```

### Sekoia.io endpoint agents per version

``` shell
events
| where timestamp >= ago(24h)
| where sekoiaio.intake.dialect == 'sekoia.io endpoint agent'
| where event.action == 'stats'
| aggregate count_distinct(agent.id) by agent.version

```


### List unique user.name

``` shell
events
| where timestamp >= ago(24h)
| distinct(user.name)
| limit 100

```

### Number of events per IP address

``` shell
events
| where timestamp > ago(30d)
| aggregate count=count() by client.ip
| order by count desc
| limit 100

```


### Aggregate events by source.ip and action.outcome

``` shell
events
| where timestamp >= ago(24h) and event.category == 'authentication'
| aggregate count() by source.ip, action.outcome
| limit 100

```


### Events where process.name starts with 'chrome'

``` shell
events
| where timestamp > ago(24h) and process.name startswith('chrome')
| limit 100

```


### Events of specific intake

``` shell
events
| where timestamp >= ago(24h)
| lookup intakes on sekoiaio.intake.uuid == uuid
| where intake.name == '<intake name>'
| limit 100

```


### Number of defended assets: unique host.name with more than 10 events during 2 weeks in the last 30 days

``` shell
events
| where timestamp > ago(30d)
| aggregate events_count = count() by host.name, week = week(timestamp)
| where events_count > 10
| aggregate week_count = count(), total_count = sum(events_count) by host.name
| where week_count >= 2
| order by total_count
| project host.name, total_count
| limit 100

```

!!! note
    Please note: the `select` command can also be used. `select` and `project` are aliases and both return the same results.
    
### host.os.type per Sekoia endpoint agent

``` shell
events
| where timestamp >= ago(24h)
| where sekoiaio.intake.dialect == 'sekoia.io endpoint agent'
| aggregate count() by host.os.type
| limit 100

```


### Received Kbytes per month per intake

``` shell
event_telemetry
| where bucket_start_date >= ago(30d)
| aggregate sum_bytes = sum(total_message_size) by intake_uuid
| lookup intakes on intake_uuid == uuid
| select sum_gb = sum_bytes / (1000*1000*1000), intake.name
| order by sum_gb desc

```

## Related articles

### Getting Started & Overview
* [SOL Overview](/xdr/features/investigate/sol_overview.md): Sekoia Operating Language overview.
* [SOL Getting Started](/xdr/features/investigate/sol_getting_started.md): This tutorial walks you through writing your first SOL queries. By the end, you'll be able to search events, filter results, and save queries for reuse.
* [SOL Best Practices](/xdr/features/investigate/sol_best_practices.md): Best practices to use SOL effectively.

### User Guides
* [Create and Manage Queries](/xdr/features/investigate/create_manage_queries.md): Create and manage queries using SOL.
* [SOL How-to Guides](/xdr/features/investigate/sol_how_to_guides.md): Learn how to use the main functions of SOL to reach your goals (aggregate data, join tables, use external data, build a query library...).
* [SOL Datasets](/xdr/features/investigate/sol_datasets.md): Discover the CSV import feature that enables SOC analysts to enrich security investigations by importing external data sources directly into the SOL query environment.

### Technical Reference
* [SOL Data Sources Reference](/xdr/features/investigate/sol_ref_datasources.md): Technical references to access security data within the Sekoia platform thanks to SOL.
* [SOL Functions Reference](/xdr/features/investigate/sol_ref_functions.md): Reference article regarding functions used in SOL.
* [SOL Operators Reference](/xdr/features/investigate/sol_ref_operators.md): Reference article regarding operators used in the SOL language.
