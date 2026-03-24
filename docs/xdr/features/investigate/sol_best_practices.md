# Understand SOL performance

SOL is a unified query language that lets you query all your security data without needing to know the underlying storage technology. You can even combine multiple data sources in a single query.

This power comes with a trade-off: the more flexible a query is, the harder it can be to execute efficiently.

## The Pipe-Based Model

All queries are built as pipelines:

```shell
datasource
| command 1
| command 2
| command 3
```

Each step takes the previous result, transforms it and passes it forward.

**The goal: reduce early**

A well-written query behaves like a funnel where data volume shrinks at each stage:

```
Raw Data (large) → Filter (smaller) → Transform (smaller) → Aggregate (tiny)
```

The earlier you reduce the data, the faster your query runs.

## How Queries Actually Run

Behind the scenes, your query is executed across two layers:

- **Datasource layer** — filters and operations that execute natively within the underlying storage engine, close to the data
- **SOL Engine layer** — operations that require fetching data into memory for processing

Understanding which layer handles each part of your query is key to writing efficient queries.

## Pushdown: The Fast Path

Pushdown means executing parts of your query directly inside the Datasource layer, before any data is transferred to the SOL Engine.

Why it's fast:

- Leverages native indexes
- Avoids transferring unnecessary data
- Runs close to storage

Example — both conditions below are typically pushed down:

```shell
events
| where timestamp > ago(24h)
| where event.category == "authentication"
```

## Engine Execution: The Flexible Path

When an operation cannot be handled by the Datasource layer, it runs inside the SOL Engine instead.

Why this can be slower:

- Data must be fetched first
- Processing happens in memory
- Performance depends on the volume of data fetched

Example — `extract` is never supported at the datasource level, so the engine must fetch all matching events before processing:

```shell
events
| extend domain = extract(@'https?://([^/]+)', 1, url.original)
```

## Mental Model: "Where Does This Run?"

For every step in your query, ask yourself:

> Is this a simple operation that the Datasource layer can handle natively?

If yes, the command is pushed down (fast). If not, execution falls back to the SOL Engine. Because queries are pipe-based, there is a virtual **pushdown limit** — the point where execution shifts from the datasource to the SOL Engine. Everything before this limit runs at the source; everything after runs in memory.

```shell
events
| where timestamp > ago(24h)
| where event.category == "web"
// PUSHDOWN LIMIT
// Commands above run inside the datasource engine
// Commands below run inside the SOL engine
| extend domain = extract(@'https?://([^/]+)', 1, url.original)
| where domain endswith ".io"
```

The query will only be fast if the number of rows **before the pushdown limit** is small. Ensure you apply your most selective filters before any non-pushable operation.

### Pushdown reference table

Use this table to identify which operations can be pushed down to the datasource:

| SOL Operation | Can be pushed down? |
|---|---|
| `\| count` | ✅ Always |
| `\| distinct <definitions>` | When `<definitions>` are simple field references |
| `\| extend ...` | ❌ Never |
| `\| join ...`, `\| lookup ...` | ❌ Never |
| `\| select <definitions>` | When `<definitions>` are simple field references |
| `\| order by <definitions>` | When `<definitions>` are simple field references. For the `events` and `eternal_events` datasources, `order by` cannot be pushed down after an aggregation |
| `\| aggregate <aggregations>` | When `<aggregations>` operate on simple field references. Only the first `aggregate` command can be pushed down |
| `\| limit ...` | ✅ Always |
| `\| top X by <definitions>` | When `<definitions>` are simple field references. For the `events` and `eternal_events` datasources, `top` cannot be pushed down after an aggregation |
| `\| where <conditions>` | When `<conditions>` are simple comparison expressions over simple field references |
| Constants and time functions (e.g. `now()`, `ago(24h)`) | ✅ Always |
| Group-by time functions (`bin`, `year`, `month`, `week`) | ✅ Always |
| `countif` aggregation function | ❌ Never |
| Row-level functions (e.g. `coalesce`, `extract`, `iff`, `tolower`) | ❌ Never |

## SOL Engine Limitations

### Internal Fetch Limit

To protect the engine from runaway queries, the SOL Engine enforces a limit on the number of rows fetched for a single query. The default is **10 000** rows.

When this limit is hit, a warning is displayed and only partial results are returned:

!!! warning
    There were too many rows to process (> 10 000), please refine your query. Partial results are displayed.

If your query legitimately requires more rows, you can raise the limit up to **1 000 000** by adding the following at the top of your query:

```shell
set internal_fetch_limit = 100000;

datasource
| where ...
```

!!! danger
    Do not set `internal_fetch_limit` as a default in all your queries. Doing so masks performance issues and makes it harder to diagnose query errors. Only use it when you are confident your query is well-designed and genuinely requires a larger result set.

### Memory Limit

When raising `internal_fetch_limit`, your query may fail if the data volume exceeds the engine's memory capacity. Each query has a hard limit of **3 GB** of memory. This value cannot be changed.

## Best practices

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

## Related articles

### Getting Started & Overview
* [SOL Overview](/xdr/features/investigate/sol_overview.md): Sekoia Operating Language overview.
* [SOL Getting Started](/xdr/features/investigate/sol_getting_started.md): This tutorial walks you through writing your first SOL queries. By the end, you'll be able to search events, filter results, and save queries for reuse.

### User Guides
* [Create and Manage Queries](/xdr/features/investigate/create_manage_queries.md): Create and manage queries using SOL.
* [SOL How-to Guides](/xdr/features/investigate/sol_how_to_guides.md): Learn how to use the main functions of SOL to reach your goals (aggregate data, join tables, use external data, build a query library...).
* [SOL Query Examples](/xdr/features/investigate/sol_query_examples.md): Get inspiration from our examples.
* [SOL Datasets](/xdr/features/investigate/sol_datasets.md): Discover the CSV import feature that enables SOC analysts to enrich security investigations by importing external data sources directly into the SOL query environment.

### Technical Reference
* [SOL Data Sources Reference](/xdr/features/investigate/sol_ref_datasources.md): Technical references to access security data within the Sekoia platform thanks to SOL.
* [SOL Functions Reference](/xdr/features/investigate/sol_ref_functions.md): Reference article regarding functions used in SOL.
* [SOL Operators Reference](/xdr/features/investigate/sol_ref_operators.md): Reference article regarding operators used in the SOL language.
