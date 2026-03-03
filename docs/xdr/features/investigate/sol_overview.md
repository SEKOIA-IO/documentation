# Sekoia Operating Language (SOL)

Sekoia Operating Language (`SOL`) is a powerful, pipe-based query language designed specifically for modern security operations. Built with similarities to `KQL` (Kusto Query Language) and `SQL`, `SOL` combines familiar syntax with advanced security-focused capabilities to deliver exceptional performance when analyzing massive security datasets.

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
