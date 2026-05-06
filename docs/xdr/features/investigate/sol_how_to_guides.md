# How-to guides

This page provides goal-oriented instructions for common SOL tasks.

## How to aggregate data

Use the `aggregate` operator to group rows and perform calculations. SOL supports the following aggregation functions: `count`, `sum`, `min`, `max`, `avg`, `count_distinct`, `make_set`, `countif`.

### Basic aggregation

=== "Query"

    ```shell
    events
    | where timestamp > ago(24h)
    | aggregate count() by source.ip
    | order by count desc
    | limit 20
    ```

=== "Results"

    | source.ip     | count |
    | ------------- | ----- |
    | 192.168.2.10  | 204   |
    | 192.168.2.22  | 202   |
    | 192.168.2.100 | 188   |

### Multiple aggregations

You can perform multiple aggregations in a single query:

=== "Query"

    ```shell
    alerts
    | where created_at > ago(30d)
    | aggregate alert_count = count(), avg_ttd = avg(time_to_detect), max_urgency = max(urgency) by rule_name
    | order by alert_count desc
    | limit 20
    ```

=== "Results"

    | rule_name                  | alert_count | avg_ttd | max_urgency |
    | -------------------------- | ----------- | ------- | ----------- |
    | SEKOIA Intelligence Feed   | 132         | 1035.66 | 95          |
    | Suspicious Mshta Execution | 82          | 523.40  | 80          |

### Aggregation over time

Use `bin()` to group data into time buckets:

=== "Query"

    ```shell
    events
    | where timestamp > ago(7d)
    | aggregate count() by bin(timestamp, 1d)
    ```

=== "Results"

    | bin_timestamp            | count |
    | ------------------------ | ----- |
    | 2026-03-20T00:00:00.000Z | 6234  |
    | 2026-03-21T00:00:00.000Z | 7891  |
    | 2026-03-22T00:00:00.000Z | 7234  |

### Conditional counting

Use `countif()` to count rows matching specific conditions:

=== "Query"

    ```shell
    events
    | where timestamp >= ago(24h) and event.category == 'authentication'
    | aggregate success = countif(action.outcome == 'success'), failure = countif(action.outcome == 'failure') by source.ip
    | order by failure desc
    | limit 100
    ```

=== "Results"

    | source.ip  | success | failure |
    | ---------- | ------- | ------- |
    | 1.0.0.95   | 142     | 33      |
    | 1.5.178.82 | 136     | 24      |

For the full operator reference, see [Aggregate rows](sol_ref_operators.md#aggregate-rows).


## How to join multiple tables

SOL provides `join` and `lookup` operators to combine data from multiple tables.

### Using join

The `join` operator combines two tables based on matching columns. The right table is injected into a `model` object:

=== "Query"

    ```shell
    events
    | where timestamp > ago(24h)
    | limit 100
    | inner join intakes on sekoiaio.intake.uuid == uuid
    | distinct intake.name
    ```

=== "Results"

    | intake.name  |
    | ------------ |
    | Sekoia Agent |
    | Zscaler      |
    | Zscaler ZIA  |

Available join types:

- **inner join** (default): Returns only matching records
- **left join**: Returns all records from the left table, with matched records from the right

### Using lookup

Prefer `lookup` over `join` when the right table is small — it's faster and more efficient:

=== "Query"

    ```shell
    events
    | where timestamp > ago(24h)
    | aggregate count() by sekoiaio.entity.uuid
    | lookup entities on sekoiaio.entity.uuid == uuid
    | select entity.name, count
    ```

=== "Results"

    | entity.name        | count |
    | ------------------ | ----- |
    | HQ - London Office | 100   |
    | Cambridge Campus   | 20    |

### Custom model names

Use the `into` keyword to define a custom name for the model object:

=== "Query"

    ```shell
    alerts
    | where created_at > ago(24h)
    | inner join entities on entity_uuid == uuid into my_entity
    | select my_entity.name
    ```

=== "Results"

    | my_entity.name     |
    | ------------------ |
    | HQ - London Office |
    | Cambridge Campus   |

For the full operator reference, see [Join tables](sol_ref_operators.md#join-tables) and [Lookup](sol_ref_operators.md#lookup).


## How to use nested queries

Use nested queries to filter data based on the results of a previous query. Define a subquery with `let`, then reference it with `in`:

=== "Query"

    ```shell
    let chromium_browsers = events
    | where timestamp > ago(30d)
    | where process.command_line contains " --type=renderer " and process.command_line contains " --extension-process "
    | distinct process.command_line;

    events
    | where process.command_line in chromium_browsers
    | aggregate count_agents=count_distinct(agent.id), executables=make_set(process.executable) by process.name
    | order by count_agents
    ```

=== "Results"

    | process.name | count_agents | executables                      |
    | ------------ | ------------ | -------------------------------- |
    | chrome       | 304          | ["chrome.exe"]                   |
    | chrome.exe   | 290          | ["chrome.exe", "chrome_sandbox"] |

For the full operator reference, see [Nested query](sol_ref_operators.md#nested-query).


## How to create visualizations

Use the `render` operator to display query results as charts. Supported chart types:

- `number` — Single value display
- `piechart` — Pie chart
- `columnchart` — Vertical bar chart
- `barchart` — Horizontal bar chart
- `linechart` — Line chart

### Basic chart

=== "Query"

    ```shell
    events
    | where timestamp > ago(24h)
    | aggregate count() by sekoiaio.any_asset.name
    | render barchart with (y=sekoiaio.any_asset.name)
    | limit 100
    ```

=== "Results"

    | sekoiaio.any_asset.name | count |
    | ----------------------- | ----- |
    | laptop-6a1ec62f         | 16    |
    | laptop-chris            | 525   |
    | laptop-b3205bc2         | 517   |

### Chart with breakdown

Use `breakdown_by` to split data into series, and `mode` to control stacking:

=== "Query"

    ```shell
    events
    | where timestamp > ago(7d)
    | aggregate count() by bin(timestamp, 1d), event.category
    | render linechart with (x=bin, y=count, breakdown_by=event.category, mode=stacked)
    ```

=== "Results"

    | bin_timestamp            | event.category | count |
    | ------------------------ | -------------- | ----- |
    | 2026-03-20T00:00:00.000Z | authentication | 234   |
    | 2026-03-20T00:00:00.000Z | network        | 1560  |
    | 2026-03-21T00:00:00.000Z | authentication | 198   |
    | 2026-03-21T00:00:00.000Z | network        | 1734  |

For the full operator reference, see [Render results in chart](sol_ref_operators.md#render-results-in-chart).


## How to use external data with SOL Datasets

SOL Datasets allow you to import CSV files and use them in your queries. This is useful for enriching events with external context like threat intelligence, asset inventories, or user directories.

!!! example

    === "Query"

        ```shell
        events
        | where timestamp > ago(24h) and url.domain != null
        | where not url.domain in (authorized_domains | select url_domain)
        | select timestamp, source.ip, url.domain
        | limit 100
        ```

    === "Results"

        | timestamp                | source.ip    | url.domain            |
        | ------------------------ | ------------ | --------------------- |
        | 2026-03-26T15:35:14.738Z | 192.168.2.10 | www.sohu.com          |
        | 2026-03-26T15:35:03.740Z | 192.168.2.22 | www.princeton.edu     |

For the full guide on importing CSVs, multi-tenancy rules, and advanced query patterns, see the dedicated [SOL Datasets](sol_datasets.md) page.


## How to build a query library

Build a collection of reusable queries to accelerate your team's investigations:

1. **Start with common use cases**: Create queries for frequent investigations (failed logins, suspicious processes, network anomalies)
2. **Use variables** for configurable time ranges with `let`:

    === "Query"

        ```shell
        let StartTime = ago(24h);
        let EndTime = now();

        events
        | where timestamp between (StartTime .. EndTime)
        | where event.category == 'authentication' and action.outcome == 'failure'
        | aggregate count() by source.ip
        | order by count desc
        ```

    === "Results"

        | source.ip     | count |
        | ------------- | ----- |
        | 192.168.2.10  | 204   |
        | 192.168.2.22  | 202   |

3. **Save your queries**: Use the Query Builder's save functionality to store queries for reuse.
4. **Browse examples**: See the [Query examples](sol_query_examples.md) page for ready-to-use queries covering events, alerts, and joins.


## How to create a dashboard

Dashboards are built from SOL query widgets. Each widget executes a SOL query and renders the results as a table or chart.

For full instructions on creating and managing dashboards, see [Create and manage dashboards](../report/create_dashboards.md) and [Configure widgets and layout](../report/add_widgets_dashboards.md).

### Using SOL filters for interactive dashboards

Filters make SOL queries dynamic and interactive. They let you reuse the same query across dashboards and contexts by substituting values dynamically without modifying the query itself.

!!! Note
    Filters are currently released under the Early Access Program.

<center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/9q6K7vwEYv8?si=5x24TPninNak550B" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

Filters are referenced using the `?filter_name` syntax.

When a query uses one or more filters, the Query Builder and Dashboards:

* Automatically detect them,
* Display user input fields (text, date, select, etc.),
* Re-execute the query whenever a filter value changes.

#### Syntax

Use the `?filter_name` notation anywhere you would normally write a static value:

```shell
<table name>
| where <column> == ?filter_name
```

??? example "Example with a time range filter"

    ```shell
    events
    | where timestamp between (?time.start .. ?time.end)
    ```

#### Built-in Filters

Certain filters are predefined and automatically available across all queries and dashboards.

| Filter        | Type     | Description                        |
| ------------- | -------- | ---------------------------------- |
| `?time.start` | datetime | Start of the time range to analyze |
| `?time.end`   | datetime | End of the time range to analyze   |
| `?communities`   | string[] | UUID of all the communities of the workspace   |
| `?intakes`   | string[] | UUID of all the intakes of the workspace   |

#### Custom Filters

You can create additional filters for values that depend on your investigation context (e.g., hostname, domain, community, entity, etc.).

!!! example

    ```shell
    events
    | where timestamp between (?time.start .. ?time.end)
    | where process.name == ?process_name
    | select timestamp, host.name, user.name, process.name, process.command_line
    | order by timestamp desc
    | limit 100
    ```


Filters in SOL are created and managed in the Query Builder or Dashboard editor.
Each filter defines how a variable (referenced as `?filter_name`) behaves in queries — its input type, allowed values, and how it is displayed to end users.

When creating or editing a filter, you can:

* Select its type (Text, Boolean, Time, etc.)
*. Add a description to clarify its purpose
* Optionally define authorized values, either statically or dynamically
* Preview how the filter will appear to users
* Copy the syntax (`?filter_name`) to reuse in SOL queries


#### Supported Types

SOL filters support the following types:

| Type                    | Example usage                                        | Notes                               |
| ----------------------- | ---------------------------------------------------- | ----------------------------------- |
| **Text**                | `where timestamp > ago(1h) and user.name == ?username`                       | Free text input                     |
| **Boolean**             | `where timestamp > ago(1h) and event.success == ?is_success`                 | Displayed as toggle                 |
| **Time**                | `where timestamp between (?time.start .. ?time.end)` | Common in dashboards                |
| **Single Selection**    | `where uuid == ?alert_uuid`                     | One value among the accepted ones   |
| **Multiple Selection**  | `where timestamp > ago(1h) and host.name in ?hostnames`                      | Multiple values are allowed         |


#### Authorized Values

For Single or Multiple selection filters, you can define authorized values in two ways:

**Static List**

Enter comma-separated values directly in the configuration panel.

!!! example
    ```shell
    powershell.exe, cmd.exe, rundll32.exe, chrome.exe
    ```

**Dynamic List**

Generate authorized values automatically using a SOL query.

!!! example
    ```shell
    events
    | distinct process.name
    | limit 100
    ```
This example retrieves the top 100 unique process names observed in recent events and uses them as selectable options.
Dynamic lists update automatically as new data becomes available, ensuring filters stay relevant to current activity.


!!! note

    You can dissociate the technical value from its display label by using the syntax `value:Label`.
    The value (left side) is used in the SOL query, while the label (right side) is what the user sees in the interface.

    For example:

    ```shell
    powershell.exe:PowerShell, cmd.exe:Command Prompt, bash:Bash
    ```
    In this configuration:

    - The user sees **PowerShell**, **Command Prompt**, and **Bash** in the dropdown
    - The query receives `powershell.exe`, `cmd.exe`, or `bash` as the actual filter value


**Behavior**

* Values are separated by commas
* Labels after the colon (:) are optional
* Whitespace is trimmed automatically
* Duplicate values are silently ignored
* To include a comma inside a value, escape it with a backslash (`\`)


#### Filter Preview

The Preview panel (right side of the editor) shows how the filter will appear to users in dashboards or query widgets.

!!! example

    * Boolean filter → toggle with labels "On" / "Off"
    * Text filter → input field
    * Selection filters → dropdown menus
    * Time filter → unified date range picker

#### Using Filters in Queries

To use a filter in a SOL query, reference its name prefixed by `?`.

```shell
events
| where timestamp between (?time.start .. ?time.end)
| where process.name == ?process_name
| select timestamp, host.name, process.command_line
| order by timestamp desc
| limit 100
```

In this example:

* `?time.start` and `?time.end` are predefined time filters.
* `?process_name` is a custom filter (e.g., single selection).

When added to a dashboard, users can adjust these filters without modifying the query itself.


#### Filter Best Practices

* Use descriptive names like `process_name`, `user_email`, `community_uuid`.
* Reuse filter names across queries to enable dashboard-level synchronization.
* Prefer dynamic lists when values depend on live data (e.g., entities, hosts).
* Use `?time.start` and `?time.end` for all time-based filtering.
* Avoid numeric filters — they are not fully supported.
* Avoid hard-coded customer identifiers.


## Related articles

### Getting Started & Overview
* [SOL Overview](/xdr/features/investigate/sol_overview.md): Sekoia Operating Language overview.
* [SOL Getting Started](/xdr/features/investigate/sol_getting_started.md): This tutorial walks you through writing your first SOL queries. By the end, you'll be able to search events, filter results, and save queries for reuse.
* [SOL Best Practices](/xdr/features/investigate/sol_best_practices.md): Best practices to use SOL effectively.

### User Guides
* [Create and Manage Queries](/xdr/features/investigate/create_manage_queries.md): Create and manage queries using SOL.
* [SOL Query Examples](/xdr/features/investigate/sol_query_examples.md): Get inspiration from our examples.
* [SOL Datasets](/xdr/features/investigate/sol_datasets.md): Discover the CSV import feature that enables SOC analysts to enrich security investigations by importing external data sources directly into the SOL query environment.

### Technical Reference
* [SOL Data Sources Reference](/xdr/features/investigate/sol_ref_datasources.md): Technical references to access security data within the Sekoia platform thanks to SOL.
* [SOL Functions Reference](/xdr/features/investigate/sol_ref_functions.md): Reference article regarding functions used in SOL.
* [SOL Operators Reference](/xdr/features/investigate/sol_ref_operators.md): Reference article regarding operators used in the SOL language.
