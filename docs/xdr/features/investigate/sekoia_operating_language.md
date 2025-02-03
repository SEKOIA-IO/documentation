# Sekoia Operating Language (SOL)

## Power and Simplicity in Security Analytics

## Overview

Sekoia Operating Language (`SOL`) is a powerful, pipe-based query language designed specifically for modern security operations. Built with similarities to `KQL` (Kusto Query Language) and `SQL`, `SOL` combines familiar syntax with advanced security-focused capabilities to deliver exceptional performance when analyzing massive security datasets.

## Datasources

`SOL` provides seamless access to all critical security data within Sekoia SOC platform:

| Data Source | Description | Use Cases |
|-------------|-------------|-----------|
| `events` | Security events | Threat hunting, incident investigation, SOC reporting |
| `alerts` | Security alerts and detections | SOC monitoring, alert pattern analysis |
| `cases` | Security incidents and cases | Case management, incident correlation |
| `intakes` | Data sources | Data source management, volume monitoring |
| `entities` | Company entities | Entity tracking, detailed reporting |
| `communities` | Multi-tenant communities (if applicable) | Cross-organization analysis |

## Operators

This section describes the different operators supported by Sekoia Operating Language (`SOL`).

### Count rows
    
#### Description

Use the `count` operator to count the number of rows returned by the statement.

``` shell
<table name>
| count

```
    
#### Example

- Count the number of rows in the `events` table

``` shell
events
| count

```

### Select columns
    
#### Description

Use the `select` operator to define the columns to retrieve from the table. The order of the columns defined in the query will define the order of the columns in the results.

``` shell
<table name>
| select <column name 1>, <column name 2>

```

#### Example

- Select the columns host.name and source.ip from the `events` table

``` shell
events
| select host.name, source.ip
| limit 100

```

### Distinct
    
#### Description

Use the `distinct` operator to list all the unique values of a column.

``` shell
<table name>
| distinct <column name>

```

#### Example

- List the unique values of client.ip from the events table

``` shell
events
| distinct client.ip
| limit 100

```

### Where
    
#### Description

Use the `where` operator to filter rows by a list of conditions. Use parenthesis and keywords `and`, `or` to define complex conditions.

``` shell
<table name>
| where <conditions>

```

#### Example 1

- Filter the query by excluding events older than `5 days` and retrieving only user agent from `Mac`

``` shell
events
| where timestamp > ago(5d) and user_agent.device.name == “Mac”

```

#### Example 2

- Filter the query by excluding events older than `5 days` and retrieving only user agent from `Mac` or `Android`

``` shell
events
| where timestamp > ago(5d) and (user_agent.device.name == “Mac” or user_agent.device.name == “Android”)

```

### Sort results
    
#### Description

Use the `order by` operator to sort rows by a column. The default sort order is descending.

``` shell
<table name>
| order by  <column name> <desc | asc>

```

#### Example

- Order the rows by the timestamp column in ascending order

``` shell
events
| order by timestamp asc
| limit 100

```

### Limit results
    
#### Description

Use the `limit` operator to retrieve the last n number of rows based on the current sort order.

``` shell
<table name>
| limit <integer>

```

#### Example

- Get `1000` events from `events` table

``` shell
events
| limit 1000

```

### Get the Top n rows 
    
#### Description

Use the `top` operator to returns the first n rows sorted by the specified column.

``` shell
<table name>
| top <integer> by <column name> [asc | desc]

```

#### Example

- Get the top `5` alerts with the most occurrences from `alerts` table

``` shell
alerts
| top 5 by occurences

```

Note that the query below is equivalent.

``` shell
alerts
| order by occurences desc
| limit 5

```

### Create calculated columns
    
#### Description

You can use `select` or `extend` operators to create calculated columns.
Use `select` to specify the columns to display. When using `extend`, the calculated column is appended to the end of the table.

``` shell
<table name>
| select <new column name> = <column name 1> + <column name 2>

```

#### Example

- Create a calculated column named total that sums the `time_to_detect`, `time_to_respond` and `time_to_resolve` values

``` shell
alerts
| select total = time_to_detect + time_to_respond + time_to_resolve

```

### Aggregate rows
    
#### Description

Use the `aggregate` operator to group rows by a column and perform aggregations with a chosen function: `count`, `sum`, `min`, `max`, `avg`, `uniquecount`.

``` shell
<table name>
| aggregate <function> by <column name>

```

#### Example

- Count the number of events per asset in the `events` table

``` shell
events
| aggregate count() by sekoiaio.any_asset.name

```

Note that you can specify a column name for the aggregation. In the example below, the column name is defined as `total`.

``` shell
events
| aggregate total = count() by sekoiaio.any_asset.name

```

### Render results in chart
    
#### Description

Use the `render` operator to display results in a chart to identify more easily anomalies or outliers. Supported charts are:

- `number`
- `piechart`
- `columnchart`
- `barchart`
- `linechart`

``` shell
<table name>
| aggregate <function> by <column name>
| render <chart_type> with (x=<column name>, y=<column name>, breakdown_by=<column name>, mode=<grouped | stacked>)

```

#### Example

- Count the number of events per asset in the events table and render it in a bar chart.

``` shell
events
| aggregate count() by sekoiaio.any_asset.name
| render barchart with (y=sekoiaio.any_asset.name)

```

### Join tables
    
#### Description

Use the `join` operator to combine data from multiple tables, enriching the data context, filtering more accurately data.

Available `join` types are:

- **inner join**: Returns records that have matching values in both tables (default)
- **left join**: Returns all records from the left table, and the matched records from the right table

``` shell
<left table name>
| inner join <right table name> on <left column name> == <right column name>
| select <model object>.<right column name>, <left column name>

```

When performing `join`, the right table is injected into a `model` object.

This `model` object (similar to a class Object in code development) contains a set properties. Each `property` represents a `column` of the original table.

!!! info
    By convention, we consider that when using `join`, the **left part** of the statement represents the column of the **left table** and the **right part** of the statement represents the column of the **right table**.

#### Example 1

- Join the tables events and intakes

``` shell
events
| inner join intakes on sekoiaio.intake.uuid == uuid   // sekoiaio.intake.uuid belongs to events table and uuid belongs to intakes table
| select intake.name

```

The `model` object default name is related to the table name it is originating from. In this case, the model name is `intake` since the join was performed on the `intakes` table.

#### Example 2

- Join the tables alerts and entities

``` shell
alerts
| inner join entities on entity_uuid == uuid   // entity_uuid belongs to alerts table and uuid belongs to entities table
| select entity.name

```

The `model` object default name is related to the table name it is originating from. In this case, the model name is `entity` since the join was performed on the `entities` table.

#### Define model object name

- In this example, we define a specific name for the model object with the into operator.

``` shell
alerts
| inner join entities on entity_uuid == uuid into my_entity
| select my_entity.name
```

### Lookup
    
#### Description

Use the `lookup` operator to extend a table. Extends the current table with values looked-up in another table.

!!! info
    The result doesn't repeat columns from the `right` table that are the basis for the join operation.
    The `lookup` operator only supports `left join`.

``` shell
<left table name>
| lookup <right table name> on <left column name> == <right column name>
| aggregate <function> by <column name>
| order by <column name>

```

Similarly to `join` operator, `lookup` will inject the right table into a `model` object.

### In
    
#### Description

Use the `in` operator to filter the rows based on a set of case-sensitive strings.

``` shell
<table name>
| where <column name> in (<value 1>, <value 2>)

```

### Contains
    
#### Description

Use the `contains` operator to filter the rows that contains a case-sensitive string.

``` shell
<table name>
| where <column name> contains <value 1>

```

### Starts with
    
#### Description

Use the `startswith` operator to filter rows that starts with a case-sensitive string.

``` shell
<table name>
| where <column name> startswith <pattern>

```

### Ends with
    
#### Description

Use the `endswith` operator to filter rows that ends with a case-sensitive string.

``` shell
<table name>
| where <column name> endswith <pattern>

```

### Variables
    
#### Description

Use the `let` operator to define variables.

``` shell
let <variable name> = <string | integer | function()>;

<table name>
| where <column name> = <variable name>

```

### Comments
    
#### Description

Use `//` to add comments in the query.
Use `Ctrl+K+C` to comment current line or selected lines.
Use `Ctrl+K+U` to uncomment current line or selected lines.

``` shell
let <variable name> = <string | integer | function()>;

<table name>
| where <column name> = <variable name>

```

### Datetime: now()
    
#### Description

Returns the current **UTC** time, optionally offset by a given timespan.

``` shell
let time = now();

let time_earlier = now(-2d);

```

### Datetime: ago()
    
#### Description

Returns a datetime value equal to the current UTC time minus the timespan.

``` shell
let time = ago(1h);

```

### Timestamp: bin()

#### Description

Rounds values down to an integer multiple of a given bin size.

``` shell
events
| aggregate count() by bin(timestamp, 1d)

```