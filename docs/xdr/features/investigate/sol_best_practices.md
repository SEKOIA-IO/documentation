# SOL best practices

This page covers best practices for writing performant and maintainable SOL queries.

## Writing performant queries

### Always filter by time first

Every query on the `events` datasource should start with a time filter. This is the single most impactful optimization, it determines how much data the query engine needs to scan.

```shell
// Good: time filter as the first condition
events
| where timestamp > ago(24h)
| where source.ip == '10.0.0.1'
| limit 100

// Bad: no time filter, scans all retained data
events
| where source.ip == '10.0.0.1'
| limit 100
```

### Use `limit` to cap result sets

Always include a `limit` operator to prevent queries from returning excessively large result sets. This is especially important for exploratory queries.

```shell
events
| where timestamp > ago(24h)
| select timestamp, host.name, source.ip
| limit 1000
```

### Filter before aggregating

Apply `where` filters before `aggregate` to reduce the amount of data that needs to be processed.

```shell
// Good: filter first, then aggregate
events
| where timestamp > ago(24h) and event.category == 'authentication'
| aggregate count() by source.ip

// Bad: aggregate everything first
events
| aggregate count() by source.ip, event.category
| where event.category == 'authentication'
```

### Use `lookup` instead of `join` for small tables

When the right-side table is small (e.g., `entities`, `intakes`, `communities`), prefer `lookup` over `join` for better performance.

```shell
// Good: lookup for small reference tables
events
| where timestamp > ago(24h)
| lookup intakes on sekoiaio.intake.uuid == uuid
| aggregate count() by intake.name

// Avoid: join when lookup would suffice
events
| where timestamp > ago(24h)
| inner join intakes on sekoiaio.intake.uuid == uuid
| aggregate count() by intake.name
```

### Filter before joining

Apply time and condition filters to the main table before performing joins or lookups to minimize the data processed.

```shell
events
| where timestamp > ago(1h) and user.name != null
| lookup entities on sekoiaio.entity.uuid == uuid
| select timestamp, user.name, entity.name
| limit 100
```

## Writing maintainable queries

### Use variables for reusable values

Use `let` to define variables for time ranges or repeated values. This makes queries easier to modify and understand.

```shell
let StartTime = ago(7d);
let EndTime = now();

alerts
| where created_at between (StartTime .. EndTime)
| aggregate count() by detection_type
```

### Use comments to explain intent

Add comments with `//` to explain complex logic or business context.

```shell
// Count failed logins from external IPs (excluding known VPN ranges)
events
| where timestamp > ago(24h)
| where event.category == 'authentication' and action.outcome == 'failure'
| where not source.ip startswith '10.'  // Exclude internal network
| aggregate count() by source.ip
| order by count desc
```

### Name your aggregation columns

Give meaningful names to aggregated columns for clearer results.

```shell
// Good: descriptive column names
alerts
| where created_at > ago(30d)
| aggregate alert_count = count(), avg_ttd = avg(time_to_detect) by rule_name
| order by alert_count desc

// Less clear: default column names
alerts
| where created_at > ago(30d)
| aggregate count(), avg(time_to_detect) by rule_name
```

### Use `coalesce` for null handling

When fields might be null, use `coalesce` to provide fallback values.

```shell
events
| where timestamp > ago(24h)
| aggregate count() by user = coalesce(user.name, user.email, "Unknown")
```
