# Getting started with SOL

This tutorial walks you through writing your first SOL queries. By the end, you'll be able to search events, filter results, and save queries for reuse.

## Accessing the Query Builder

1. Navigate to **Investigate** > **Queries** in the main navigation
2. The Query Builder opens in **code mode** by default, ready for SOL queries

For more details on the Query Builder interface, see [Discover the Query Builder](query_builder.md).

## Selecting a datasource

Every SOL query starts with a datasource name. The datasource determines what data you are querying.

The most commonly used datasources are:

| Datasource | Description |
|---|---|
| `events` | Security events and logs |
| `alerts` | Security alerts and detections |
| `cases` | Security incidents and cases |

For the full list of available datasources and their properties, see the [Datasources reference](sol_ref_datasources.md).

## Your first query

Let's start with a simple query to retrieve recent events:

```shell
events
| limit 10
```

This returns 10 events without specific order. Now let's add a time filter and select specific columns:

```shell
events
| where timestamp > ago(1h)
| select timestamp, host.name, source.ip, event.action
| limit 100
```

This query:

1. Starts from the `events` datasource
2. Filters to events from the last hour using `where` and `ago()`
3. Selects only the columns we care about with `select`
4. Limits the output to 100 rows

Click **Run** (or press the keyboard shortcut) to execute your query.

### Adding conditions

You can combine multiple conditions with `and` and `or`:

```shell
events
| where timestamp > ago(24h) and (event.category == 'authentication' or event.category == 'network')
| where action.outcome == 'failure'
| select timestamp, source.ip, user.name, event.category, action.outcome
| order by timestamp desc
| limit 100
```

This query filters events from the last 24 hours where the category is either `authentication` **or** `network`, **and** the outcome is `failure`. Note that chaining multiple `where` operators on separate lines is equivalent to combining them with `and`.

### Counting rows

Use the `count` operator to get the total number of matching rows:

```shell
events
| where timestamp > ago(24h) and event.category == 'authentication'
| count
```

This returns a single row with the total number of authentication events in the last 24 hours.

### Aggregating data

Use `aggregate` to group rows by a column and perform calculations per group:

```shell
events
| where timestamp > ago(24h)
| aggregate count() by source.ip
| order by count desc
| limit 20
```

Unlike `count` which returns one total, `aggregate count() by` groups rows and returns a count for each unique value. Here, it counts events per source IP over the last 24 hours, sorted by the most active IPs:

| source.ip | count |
|---|---|
| 192.168.1.42 | 1204 |
| 10.0.0.15 | 873 |
| 172.16.5.8 | 412 |
| 10.0.0.22 | 98 |

For more aggregation patterns, see [How to aggregate data](sol_how_to_guides.md#how-to-aggregate-data).

## Filtering your results

The `where` operator is the primary way to filter data in SOL. You can use:

- **Comparison operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **String operators**: `contains`, `startswith`, `endswith` (add `~` for case-insensitive)
- **Set membership**: `in` with a list of values
- **Negation**: `not` before any condition

```shell
events
| where timestamp > ago(24h)
| where user.name contains 'admin'
| where not source.ip in ['10.0.0.1', '10.0.0.2']
| limit 100
```

For the complete list of operators, see the [Operators reference](sol_ref_operators.md).

## Saving and reusing queries

Once you've written a useful query, you can save it for later reuse:

1. Edit the query title to give it a descriptive name
2. Click **Save** in the Query Builder toolbar
3. Your saved queries are accessible from the Queries list

Saved queries can also be used as the basis for dashboard widgets.

For more details, see [Create and manage queries](create_manage_queries.md).

## Related articles

### Getting Started & Overview
* [SOL Overview](/xdr/features/investigate/sol_overview.md): Sekoia Operating Language overview.
* [SOL Best Practices](/xdr/features/investigate/sol_best_practices.md): Best practices to use SOL effectively.

### User Guides
* [Create and Manage Queries](/xdr/features/investigate/create_manage_queries.md): Create and manage queries using SOL.
* [SOL How-to Guides](/xdr/features/investigate/sol_how_to_guides.md): Learn how to use the main functions of SOL to reach your goals (aggregate data, join tables, use external data, build a query library...).
* [SOL Query Examples](/xdr/features/investigate/sol_query_examples.md): Get inspiration from our examples.
* [SOL Datasets](/xdr/features/investigate/sol_datasets.md): Discover the CSV import feature that enables SOC analysts to enrich security investigations by importing external data sources directly into the SOL query environment.

### Technical Reference
* [SOL Data Sources Reference](/xdr/features/investigate/sol_ref_datasources.md): Technical references to access security data within the Sekoia platform thanks to SOL.
* [SOL Functions Reference](/xdr/features/investigate/sol_ref_functions.md): Reference article regarding functions used in SOL.
* [SOL Operators Reference](/xdr/features/investigate/sol_ref_operators.md): Reference article regarding operators used in the SOL language.
