# Sekoia Operating Language (SOL)

Sekoia Operating Language (`SOL`) is a pipe-based query language for security operations on the Sekoia platform. Inspired by `KQL` (Kusto Query Language), it lets you query and correlate all your security data (events, alerts, cases, assets, and more) using a single, unified syntax.

## SOL vs the Events page

Sekoia.io provides two ways to search and analyze your security data:

| | Events page | SOL (Query Builder) |
|---|---|---|
| **Interface** | UI-based search with filters and buttons | Code-based query editor |
| **Best for** | Quick searches, viewing individual logs, adding events to cases | Complex analytics, aggregations, cross-table joins, dashboards |
| **Query language** | [Events Query Language](events_query_language.md) with filter badges | SOL with full operator and function support |
| **Visualization** | Histogram with basic aggregation | Charts (bar, line, pie, column) with full render control |
| **Data sources** | Events only | Events, alerts, cases, assets, intakes, communities, and more |
| **Saving & sharing** | Browser-based saved queries | Persistent saved queries, shared across team, dashboard widgets |

Use the **Events page** when you need to quickly browse logs, inspect individual events, or add evidence to a case. Use **SOL in the Query Builder** when you need analytics, cross-table correlation, or dashboard creation.

For more details on the Events page, see the [Events documentation](events.md).

## Key differences from KQL

SOL is inspired by KQL but has its own conventions:

| Feature | KQL | SOL |
|---|---|---|
| Aggregation operator | `summarize` | `aggregate` |
| Column selection | `project` | `select` |
| In operator | `"abc" in ("123", "345", "abc")` | `"abc" in ["123", "345", "abc"]` |
| Not operator | `"abc" !in ("123", "345", "abc")` | `not "abc" in ["123", "345", "abc"]` |
| Table references in joins | Direct column access | `model` object (e.g., `intake.name`) |
| Sort operator | `sort by` | `order by` |
| Limit operator | `take` | `limit` |
| Time literals | `ago(1h)` | `ago(1h)` |
| Comments | `//` | `//` |

## Where SOL is used

SOL powers two key features in the Sekoia.io platform:

### Query Builder

The [Query Builder](query_builder.md) is the primary interface for writing SOL queries. It provides:

- A code editor with syntax highlighting and autocompletion
- Result visualization with tables and charts
- Query saving, sharing, and management

### Dashboards

SOL queries are the foundation of [dashboard widgets](../report/dashboards.md). Each widget in a dashboard is powered by a SOL query, and SOL [filters](sol_how_to_guides.md#how-to-create-a-dashboard) make widgets interactive and configurable for end users.

## Related articles

### Getting Started & Overview
* [SOL Getting Started](/xdr/features/investigate/sol_getting_started.md): This tutorial walks you through writing your first SOL queries. By the end, you'll be able to search events, filter results, and save queries for reuse.
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
