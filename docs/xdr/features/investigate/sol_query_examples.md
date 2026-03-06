# Query examples

## Join examples

### Join between events and communities tables (for Multi-tenant)

``` shell
events
| where timestamp > ago(5m)
| limit 100
| join communities on sekoiaio.customer.community_uuid == uuid
| select timestamp, sekoiaio.customer.community_uuid, community.name

```

---

### Join between events and entities tables

``` shell
events
| limit 100
| lookup entities on sekoiaio.entity.uuid == uuid
| aggregate count=count() by entity.name
| select entity.name, count

```

---

### Join between alerts and communities tables (for Multi-tenant)

``` shell
alerts
| aggregate count=count() by community_uuid
| join communities on community_uuid == uuid
| select community.name, community_uuid, count
| limit 100

```

## Alerts query examples

### Detection rules ranked by number of alerts

``` shell
alerts
| where created_at > ago(30d)
| order by occurrences desc
| select rule_name, occurrences

```

---

### Assets ranked by number of alerts

``` shell
alerts
| where created_at > ago(30d)
| aggregate count=count() by assets.uuid
| order by count desc
| limit 100

```

---

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

---

### Average time to detect in last 30 days

``` shell
alerts
| where created_at > ago(30d)
| aggregate avg(time_to_detect)

```

---

### Rename columns and convert time_to_detect in minutes

``` shell
alerts
| where time_to_detect != null
| select entity = entity_name, rule = rule_name, ttd = time_to_detect/60
| limit 10

```

---

### Ranking of communities by alerts

``` shell
alerts
| aggregate AlertCount = count() by community_uuid
| left join communities on community_uuid == uuid
| order by AlertCount desc
| select community.name, AlertCount

```

---

### Ranking of communities by intakes

``` shell
alerts
| aggregate AlertCount = count() by community_uuid
| left join communities on community_uuid == uuid
| order by AlertCount desc
| select community.name, AlertCount

```

---

## Events query examples

### Number of unique command lines per host.name

``` shell
events
| where timestamp > ago(24h)
| aggregate count=count_distinct(process.command_line) by host.name
| order by count desc

```

---

### Number of unique hostname per month

``` shell
events
| where timestamp > ago(90d)
| aggregate count=count_distinct(log.hostname) by month(timestamp)

```

---

### Top 10 visited URL

``` shell
events
| where timestamp >= ago(24h)
| aggregate count() by url.domain
| top 10 by count

```

---

### Top 10 blocked URL

``` shell
events
| where timestamp >= ago(24h) and event.action == 'blocked' and user.name != null and url.domain != null
| aggregate count() by url.domain
| top 10 by count

```

---

### Top 10 login failures on Windows

``` shell
events
| where timestamp > ago(24h) and event.code == 4625
| aggregate failed_login_count=count() by user.target.name
| top 10 by failed_login_count

```

---

### Sekoia.io endpoint agents per version

``` shell
events
| where timestamp >= ago(24h)
| where sekoiaio.intake.dialect == 'sekoia.io endpoint agent'
| where event.action == 'stats'
| aggregate count_distinct(agent.id) by agent.version

```

---

### List unique user.name

``` shell
events
| where timestamp >= ago(24h)
| distinct(user.name)

```

---

### Number of events per IP address

``` shell
events
| where timestamp > ago(30d)
| aggregate count=count() by client.ip
| order by count desc

```

---

### Aggregate events by source.ip and action.outcome

``` shell
events
| where timestamp >= ago(24h) and event.category == 'authentication'
| aggregate count() by source.ip, action.outcome

```

---

### Events where process.name starts with 'chrome'

``` shell
events
| where timestamp > ago(24h) and process.name startswith('chrome')
| limit 100

```

---

### Events of specific intake

``` shell
events
| left join intakes on sekoiaio.intake.uuid == uuid
| where timestamp >= ago(24h) and intake.name == '<intake name>'
| limit 100

```

---

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

```
Please note: the `select` command can also be used. `select` and `project` are aliases and both return the same results.
---

### host.os.type per Sekoia endpoint agent

``` shell
events
| where sekoiaio.intake.dialect == 'sekoia.io endpoint agent'
| aggregate count() by host.os.type
| limit 100

```

---


### Received Kbytes per month per intake

``` shell
event_telemetry
| where bucket_start_date >= ago(30d)
| summarize sum_bytes = sum(total_message_size) by intake_uuid
| lookup intakes on intake_uuid == uuid
| select sum_gb = sum_bytes / (1000*1000*1000), intake.name
| order by sum_gb desc

```
