# Reference: Operators

The next sections describe the different operators supported by Sekoia Operating Language (`SOL`).

## Count rows

**Description**

Use the `count` operator to count the number of rows returned by the statement.

``` shell
<table name>
| count

```

**Example**

Count the number of rows in the `events` table

``` shell
events
| where timestamp > ago(30m)
| count

```

---

## Select columns

**Description**

Use the `select` operator to define the columns to retrieve from the table. The order of the columns defined in the query will define the order of the columns in the results.

``` shell
<table name>
| select <column name 1>, <column name 2>

```

**Example**

Select the columns host.name and source.ip from the `events` table

``` shell
events
| select host.name, source.ip
| limit 100

```

---

## Distinct

**Description**

Use the `distinct` operator to list all the unique values of a column.

``` shell
<table name>
| distinct <column name>

```

**Example**

List the unique values of client.ip from the events table

``` shell
events
| where timestamp > ago(24h)
| distinct client.ip
| limit 100

```

---

## Where

**Description**

Use the `where` operator to filter rows by a list of conditions. Use parenthesis and keywords `and`, `or` to define complex conditions.

``` shell
<table name>
| where <conditions>

```

**Example 1**

Filter the query by excluding events older than `5 days` and retrieving only user agent from `Mac`

``` shell
events
| where timestamp > ago(5d) and user_agent.device.name == 'Mac'
| limit 100

```

**Example 2**

Filter the query by excluding events older than `5 days` and retrieving only user agent from `Mac` or `Android`

``` shell
events
| where timestamp > ago(5d) and (user_agent.device.name == 'Mac' or user_agent.device.name == 'Android')
| limit 100

```

**Example 3**

Same as example 2 but with multiple `where` statements

``` shell
events
| where timestamp > ago(5d)
| where user_agent.device.name == 'Mac' or user_agent.device.name == 'Android'
| limit 100

```

---

## Nested query

**Description**

Use the `in` operator to use the results of a previous query.

``` shell
let query = <table name> | select <column name>;

<table name>
| where <column name> in query

```

**Example**

``` shell
let chromium_browsers =  events
| where timestamp > ago(30d)
| where process.command_line contains " --type=renderer " and process.command_line contains " --extension-process "
| distinct process.command_line;

events
| where process.command_line in chromium_browsers
| aggregate count_agents=count_distinct(agent.id), executables=make_set(process.executable) by process.name
| order by count_agents

```

---

## Sort results

**Description**

Use the `order by` operator to sort rows by a column. The default sort order is descending.

``` shell
<table name>
| order by  <column name> <desc | asc>

```

**Example 1**

Order the rows by the timestamp column in ascending order

``` shell
events
| order by timestamp asc
| limit 100

```

---

**Example 2**

Order alerts by descending urgency and ascending first_seen_at

``` shell
alerts
| select short_id, rule_name, urgency, first_seen_at
| order by urgency desc, first_seen_at asc
| limit 100

```

---

## Limit results

**Description**

Use the `limit` operator to retrieve the last n number of rows based on the current sort order.

``` shell
<table name>
| limit <integer>

```

**Example**

Get `1000` events from `events` table

``` shell
events
| limit 1000

```

---

## Get the Top n rows

**Description**

Use the `top` operator to returns the first n rows sorted by the specified column.

``` shell
<table name>
| top <integer> by <column name> [asc | desc]

```

**Example**

Get the top `5` alerts with the most occurrences from `alerts` table in the last 7 days

``` shell
alerts
| where created_at > ago(7d)
| top 5 by occurrences

```

Note that the query below is equivalent.

``` shell
alerts
| order by occurrences desc
| limit 5

```

---

## Create calculated columns

**Description**

You can use `select` or `extend` operators to create calculated columns.
Use `select` to specify the columns to display. When using `extend`, the calculated column is appended to the end of the table.

``` shell
<table name>
| select <new column name> = <column name 1> + <column name 2>

```

**Example**

Create a calculated column named total that sums the `time_to_detect`, `time_to_respond` and `time_to_resolve` values

``` shell
alerts
| select total = time_to_detect + time_to_respond + time_to_resolve
| limit 100

```

---

## Aggregate rows

**Description**

Use the `aggregate` operator to group rows by a column and perform aggregations with a chosen function: `count`, `sum`, `min`, `max`, `avg`, `count_distinct`, `make_set`, `countif`.

``` shell
<table name>
| aggregate <function> by <column name>

```

**Example 1**

Count the number of events per asset in the `events` table

``` shell
events
| aggregate count() by sekoiaio.any_asset.name
| limit 100

```

Note that you can specify a column name for the aggregation. In the example below, the column name is defined as `total`.

``` shell
events
| aggregate total = count() by sekoiaio.any_asset.name
| limit 100

```

**Example 2**

Count the number of events per source.ip and per action.outcome in the `events` table

``` shell
events
| where timestamp >= ago(24h) and event.category == 'authentication'
| aggregate count() by source.ip, action.outcome

```

**Example 3**

Sum the values of 'time_to_detect' column in the `alerts` table

``` shell
alerts
| aggregate sum(time_to_detect)
| limit 100

```

**Example 4**

Retrieve the minimum value of 'time_to_detect' column in the `alerts` table

``` shell
alerts
| aggregate min(time_to_detect)
| limit 100

```

**Example 5**

Retrieve the maximum value of 'time_to_detect' column in the `alerts` table

``` shell
alerts
| aggregate max(time_to_detect)
| limit 100

```

**Example 6**

Calculate the average value of 'time_to_detect' column in the `alerts` table

``` shell
alerts
| aggregate avg(time_to_detect)
| limit 100

```

**Example 7**

Count unique values of 'source.ip' column in the `events` table

``` shell
events
| aggregate count_distinct(source.ip)
| limit 100

```

**Example 8**

Create an array of the set of distinct values of 'source.ip' column in the `events` table.
Note that `null` values are ignored.

``` shell
events
| aggregate make_set(source.ip)
| limit 100

```

**Example 9**

Count allowed and denied network events per destination port using `countif`

``` shell
events
| where timestamp >= ago(24h) and event.category == 'network'
| aggregate allowed = countif(action.outcome == 'success'), denied = countif(action.outcome == 'failure') by destination.port
| order by denied desc
| limit 100

```

---

## Render results in chart

**Description**

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

**Example**

Count the number of events per asset in the events table and render it in a bar chart.

``` shell
events
| aggregate count() by sekoiaio.any_asset.name
| render barchart with (y=sekoiaio.any_asset.name)
| limit 100

```

---

## Join tables

**Description**

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

**Example 1**

Join the tables events and intakes

``` shell
events
| where timestamp > ago(24h)
| limit 100
| inner join intakes on sekoiaio.intake.uuid == uuid   // sekoiaio.intake.uuid belongs to events table and uuid belongs to intakes table
| distinct intake.name

```

The `model` object default name is related to the table name it is originating from. In this case, the model name is `intake` since the join was performed on the `intakes` table.

**Example 2**

Join the tables alerts and entities

``` shell
alerts
| where created_at > ago(24h)
| limit 100
| inner join entities on entity_uuid == uuid   // entity_uuid belongs to alerts table and uuid belongs to entities table
| distinct entity.name

```

The `model` object default name is related to the table name it is originating from. In this case, the model name is `entity` since the join was performed on the `entities` table.

**Define model object name**

In this example, we define a specific name for the model object with the into operator.

``` shell
alerts
| where created_at > ago(24h)
| inner join entities on entity_uuid == uuid into my_entity
| select my_entity.name
```

---

## Lookup

**Description**

Use the `lookup` operator to extend a table. Extends the current table with values looked-up in another table.
Prefer the `lookup` operator over `join` when the right table is small enough to fit into memory to improve query performance.

!!! info
    The result doesn't repeat columns from the `right` table that are the basis for the join operation.
    The `lookup` operator only supports `left join`.

``` shell
<left table name>
| lookup <right table name> on <left column name> == <right column name>
| aggregate <function> by <column name>
| order by <column name>

```

Similarly to `join` operator, `lookup` will inject the right table into a `model` object.

---

## Compare

**Description**

Use the following operators to compare values.

| Comparator | Description | Examples |
| --- | --- | --- |
| == | Equals | `1 == 1` |
| =~ | Equals (case insensitive) | `'.exe' == '.EXE'` |
| != | Not equals | `1 != 0` |
| < | Less | `1 < 10` |
| <= | Less or equals | `4 <= 5` |
| > | Greater | `20 > 10` |
| >= | Greater or equals | `5 >= 4` |

---

## In

**Description**

Use the `in` operator to filter the rows based on a set of case-sensitive strings.
Use `in~` to filter on a set of case-insensitive strings.

``` shell
<table name>
| where <column name> in [<value 1>, <value 2>]

```

**Example 1**

Find events where `client.ip` equals to theses values: 192.168.0.1, 192.168.0.2.

``` shell
events
| where client.ip in ['192.168.0.1', '192.168.0.2']
| limit 100

```

**Example 2**

Find events where `process.name` equals to theses values ignoring case-sensitivity: powershell.exe, powershell_ise.exe.

``` shell
events
| where process.name in~ ['powershell.exe', 'powershell_ise.exe']
| limit 100

```

---

## Contains

**Description**

Use the `contains` operator to filter the rows that contains a case-sensitive string.
Use `contains~` to switch to case-insensitive strings.

``` shell
<table name>
| where <column name> contains <value 1>

```

**Example 1**

Find events where `user.full_name` contains the string `Admin` (case sensitive).

``` shell
events
| where user.full_name contains 'Admin'
| limit 100

```

**Example 2**

Find events where `user.full_name` contains the string `ADMIN` (case insensitive).

``` shell
events
| where user.full_name contains~ 'ADMIN'
| limit 100

```

---

## Starts with

**Description**

Use the `startswith` operator to filter rows that starts with a case-sensitive string.
Use `startswith~` to switch to case-insensitive strings.

``` shell
<table name>
| where <column name> startswith <pattern>

```

**Example 1**

Find events where `url.domain` starts with the string `api.prod`.

``` shell
events
| where url.domain startswith 'api.prod'
| limit 100

```

**Example 2**

Find events where `process.command_line` starts with the string `Invoke` ignoring case-sensitivity.

``` shell
events
| where process.command_line startswith~ 'Invoke'
| limit 100

```

---

## Ends with

**Description**

Use the `endswith` operator to filter rows that ends with a case-sensitive string.
Use `endswith~` to switch to case-insensitive strings.

``` shell
<table name>
| where <column name> endswith <pattern>

```

**Example 1**

Find events where `url.path` ends with the string `/admin`.

``` shell
events
| where url.path endswith '/admin'
| limit 100

```

**Example 2**

Find events where `process.command_line` ends with the string `.DLl` ignoring case-sensitivity.

``` shell
events
| where process.command_line endswith~ '.DLl'
| limit 100

```

---

## Not

**Description**

Use the `not` operator to negate any comparison.

``` shell
<table name>
| where not <column name> <comparison operator> <pattern>

```

**Example 1**

Find events where `client.ip` does not equal to theses values: 192.168.0.1, 192.168.0.2.

``` shell
events
| where not client.ip in ['192.168.0.1', '192.168.0.2']
| limit 100

```

**Example 2**

Find events where `user.full_name` does not contain the string `Admin` (case sensitive).

``` shell
events
| where not user.full_name contains 'Admin'
| limit 100

```

**Example 3**

Find events where `process.command_line` does not start with the string `Invoke` ignoring case-sensitivity.

``` shell
events
| where not process.command_line startswith~ 'Invoke'
| limit 100

```

**Example 4**

Find events where `process.command_line` does not end with the string `.DLl` ignoring case-sensitivity.

``` shell
events
| where not process.command_line endswith~ '.DLl'
| limit 100

```

---

## Regex

**Description**

Use the `matches regex` operator to filter the rows based on a regex pattern.

``` shell
<table name>
| where <column name> matches regex <pattern>

```

| Pattern | Description | Example |
| --- | --- | --- |
| `.` | Matches any character | `ab.` matches 'aba', 'abb', 'abz' |
| `?` | Repeat the preceding character zero or one times | `abc?` matches 'ab' and 'abc' |
| `+` | Repeat the preceding character one or more times | `ab+` matches 'ab', 'abb', 'abbb' |
| `*` | Repeat the preceding character zero or more times | `ab*` matches 'a', 'ab', 'abb', 'abbb' |
| `{}` | Minimum and maximum number of times the preceding character can repeat | `a{2}` matches 'aa'<br>`a{2,5}` matches 'aa', 'aaa' and 'aaaa'<br>`a{2,}` matches 'a' repeated two or more times |
| `|` | OR operator. The match will succeed if the longest pattern on either the left side OR the right side matches | `abc|xyz` matches 'abc' and 'xyz' |
| `(...)` | Forms a group. You can use a group to treat part of the expression as a single character | `abc(def)?` matches 'abc' and 'abcdef' but not 'abcd' |
| `[...]` | Match one of the character in the brackets<br>Inside the brackets, `-` indicates a range unless `-` is the first character or escaped<br>A `^` before a character in the brackets negates the character or range  | `[abc]` matches 'a', 'b', 'c'<br>`[-abc]` matches '-', 'a', 'b', 'c'<br>`[^abc]` matches any character except 'a', 'b', or 'c' |

!!! info
    Some characters are reserved as operators: `.` `?` `+` `*` `|` `{` `}` `[` `]` `(` `)` `"` `\` .<br>Escape reserved operators with a preceding backslash `\` or surround them with double quotes `""`.<br>`\@` renders as a literal '@'.<br>`\\` renders as a literal '\'.<br>`"john@smith.com"` renders as 'john@smith.com'.

**Example**

Find events where `file.name` contains '.sh'.

``` shell
let StartTime = ago(1h);
let EndTime = now();

events
| where timestamp between (StartTime .. EndTime)
| where file.name matches regex '.*\.sh'
| limit 100

```

---

## Variables

**Description**

Use the `let` operator to define variables.

``` shell
let <variable name> = <string | integer>;

<table name>
| where <column name> == <variable name>

```

**Example**

Count the number of events in the last 24 hours.

``` shell
let StartTime = ago(24h);
let EndTime = now();

events
| where event.created > StartTime and event.created <= EndTime
| count

```

---

## Comments

**Description**

Use `//` to add comments in the query.

**Example**

``` shell
// Comment the filtering condition

<table name>
//| where <column name> = <variable name>
| limit 100

```
