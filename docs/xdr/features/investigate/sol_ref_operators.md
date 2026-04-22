# Reference: Operators

The next sections describe the different operators supported by Sekoia Operating Language (`SOL`).

## Count rows

Use the `count` operator to count the number of rows returned by the statement.

``` shell
<table name>
| count

```

!!! example "Count the number of rows in the `events` table"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(30m)
        | count

        ```

    === "Results"

        | count |
        | ----- |
        | 1284  |



## Select columns

Use the `select` operator to define the columns to retrieve from the table. The order of the columns defined in the query will define the order of the columns in the results.

``` shell
<table name>
| select <column name 1>, <column name 2>

```

!!! example "Select the columns host.name and source.ip from the `events` table"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | select host.name, source.ip
        | limit 100

        ```

    === "Results"

        | host.name       | source.ip     |
        | --------------- | ------------- |
        | laptop-chris    | 192.168.2.10  |
        | laptop-6a1ec62f | 192.168.2.22  |
        | laptop-b3205bc2 | 10.0.0.45     |


## Distinct

Use the `distinct` operator to list all the unique values of a column.

``` shell
<table name>
| distinct <column name>

```

!!! example "List the unique values of client.ip from the events table"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(24h)
        | distinct client.ip
        | limit 100

        ```

    === "Results"

        | client.ip     |
        | ------------- |
        | 192.168.2.10  |
        | 192.168.2.22  |
        | 10.0.0.45     |

## Where

Use the `where` operator to filter rows by a list of conditions. Use parenthesis and keywords `and`, `or` to define complex conditions.

``` shell
<table name>
| where <conditions>

```

!!! example "Filter the query by excluding events older than `5 days` and retrieving only user agent from `Mac`"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(5d) and user_agent.device.name == 'Mac'
        | limit 100

        ```

    === "Results"

        | timestamp                | user_agent.device.name |
        | ------------------------ | ---------------------- |
        | 2026-03-26T14:22:03.120Z | Mac                    |
        | 2026-03-26T14:19:47.883Z | Mac                    |
        | 2026-03-26T14:17:31.554Z | Mac                    |

!!! example "Filter the query by excluding events older than `5 days` and retrieving only user agent from `Mac` or `Android`"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(5d) and (user_agent.device.name == 'Mac' or user_agent.device.name == 'Android')
        | limit 100

        ```

    === "Results"

        | timestamp                | user_agent.device.name |
        | ------------------------ | ---------------------- |
        | 2026-03-26T14:22:03.120Z | Mac                    |
        | 2026-03-26T14:20:15.441Z | Android                |
        | 2026-03-26T14:19:47.883Z | Mac                    |

!!! example "Same as previous but with multiple `where` statements"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(5d)
        | where user_agent.device.name == 'Mac' or user_agent.device.name == 'Android'
        | limit 100

        ```

    === "Results"

        | timestamp                | user_agent.device.name |
        | ------------------------ | ---------------------- |
        | 2026-03-26T14:22:03.120Z | Mac                    |
        | 2026-03-26T14:20:15.441Z | Android                |
        | 2026-03-26T14:19:47.883Z | Mac                    |

## Nested query

Use the `in` operator to use the results of a previous query.

``` shell
let query = <table name> | select <column name>;

<table name>
| where <column name> in query

```

!!! example

    === "Query"

        ``` shell
        let chromium_browsers =  events
        | where timestamp > ago(30d)
        | where process.command_line contains " --type=renderer " and process.command_line contains " --extension-process "
        | distinct process.command_line;

        events
        | where timestamp > ago(1h)
        | where process.command_line in chromium_browsers
        | aggregate count_agents=count_distinct(agent.id), executables=make_set(process.executable) by process.name
        | order by count_agents

        ```

    === "Results"

        | process.name | count_agents | executables                      |
        | ------------ | ------------ | -------------------------------- |
        | chrome       | 304          | ["chrome.exe"]                   |
        | chrome.exe   | 290          | ["chrome.exe", "chrome_sandbox"] |

## Sort results

Use the `order by` operator to sort rows by a column. The default sort order is descending.

``` shell
<table name>
| order by  <column name> <desc | asc>

```

!!! example "Order the rows by the timestamp column in ascending order"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | order by timestamp asc
        | limit 100

        ```

    === "Results"

        | timestamp                | host.name       | source.ip    |
        | ------------------------ | --------------- | ------------ |
        | 2026-03-19T00:00:01.002Z | laptop-6a1ec62f | 10.0.0.45    |
        | 2026-03-19T00:00:04.118Z | laptop-chris    | 192.168.2.10 |
        | 2026-03-19T00:00:07.553Z | laptop-b3205bc2 | 192.168.2.22 |

!!! example "Order alerts by descending urgency and ascending first_seen_at"

    === "Query"

        ``` shell
        alerts
        | where created_at > ago(1h)
        | select short_id, rule_name, urgency, first_seen_at
        | order by urgency desc, first_seen_at asc
        | limit 100

        ```

    === "Results"

        | short_id | rule_name                  | urgency | first_seen_at            |
        | -------- | -------------------------- | ------- | ------------------------ |
        | ALT-0042 | SEKOIA Intelligence Feed   | 95      | 2026-03-20T08:14:22.000Z |
        | ALT-0087 | Suspicious Mshta Execution | 80      | 2026-03-21T11:03:47.000Z |
        | ALT-0031 | Suspicious Mshta Execution | 80      | 2026-03-22T09:55:10.000Z |

## Limit results

Use the `limit` operator to retrieve the last n number of rows based on the current sort order.

``` shell
<table name>
| limit <integer>

```

!!! example "Get `1000` events from `events` table"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | limit 1000

        ```

    === "Results"

        | timestamp                | host.name       | source.ip     |
        | ------------------------ | --------------- | ------------- |
        | 2026-03-26T14:22:03.120Z | laptop-chris    | 192.168.2.10  |
        | 2026-03-26T14:21:58.774Z | laptop-6a1ec62f | 192.168.2.22  |
        | 2026-03-26T14:21:44.331Z | laptop-b3205bc2 | 10.0.0.45     |

## Get the Top n rows

Use the `top` operator to returns the first n rows sorted by the specified column.

``` shell
<table name>
| top <integer> by <column name> [asc | desc]

```

!!! example "Get the top `5` alerts with the most occurrences from `alerts` table in the last 7 days"

    === "Query"

        ``` shell
        alerts
        | where created_at > ago(7d)
        | top 5 by occurrences

        ```

    === "Results"

        | rule_name                        | occurrences |
        | -------------------------------- | ----------- |
        | SEKOIA Intelligence Feed         | 312         |
        | Suspicious Mshta Execution       | 204         |
        | Brute Force Authentication       | 187         |
        | Credential Dumping via Mimikatz  | 143         |
        | Suspicious PowerShell Invocation | 98          |

    Note that the query below is equivalent.

    ``` shell
    alerts
    | where created_at > ago(7d)
    | order by occurrences desc
    | limit 5

    ```

## Create calculated columns

You can use `select` or `extend` operators to create calculated columns.
Use `select` to specify the columns to display. When using `extend`, the calculated column is appended to the end of the table.

``` shell
<table name>
| select <new column name> = <column name 1> + <column name 2>

```

!!! example "Create a calculated column named total that sums the `time_to_detect`, `time_to_respond` and `time_to_resolve` values"

    === "Query"

        ``` shell
        alerts
        | where created_at > ago(1h)
        | limit 100
        | select total = time_to_detect + time_to_respond + time_to_resolve

        ```

    === "Results"

        | total    |
        | -------- |
        | 3847.20  |
        | 2103.55  |
        | 1589.80  |

## Aggregate rows

Use the `aggregate` operator to group rows by a column and perform aggregations with a chosen function: `count`, `sum`, `min`, `max`, `avg`, `count_distinct`, `make_set`, `countif`.

``` shell
<table name>
| aggregate <function> by <column name>

```

!!! example "Count the number of events per asset in the `events` table"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | aggregate count() by sekoiaio.any_asset.name
        | limit 100

        ```

    === "Results"

        | sekoiaio.any_asset.name | count |
        | ----------------------- | ----- |
        | laptop-6a1ec62f         | 16    |
        | laptop-chris            | 525   |
        | laptop-b3205bc2         | 517   |

    Note that you can specify a column name for the aggregation. In the example below, the column name is defined as `total`.

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | aggregate total = count() by sekoiaio.any_asset.name
        | limit 100

        ```

    === "Results"

        | sekoiaio.any_asset.name | total |
        | ----------------------- | ----- |
        | laptop-6a1ec62f         | 16    |
        | laptop-chris            | 525   |
        | laptop-b3205bc2         | 517   |

!!! example "Count the number of events per source.ip and per action.outcome in the `events` table"

    === "Query"

        ``` shell
        events
        | where timestamp >= ago(24h) and event.category == 'authentication'
        | aggregate count() by source.ip, action.outcome

        ```

    === "Results"

        | source.ip    | action.outcome | count |
        | ------------ | -------------- | ----- |
        | 192.168.2.10 | success        | 142   |
        | 192.168.2.10 | failure        | 33    |
        | 1.5.178.82   | success        | 136   |
        | 1.5.178.82   | failure        | 24    |

!!! example "Sum the values of 'time_to_detect' column in the `alerts` table"

    === "Query"

        ``` shell
        alerts
        | where created_at > ago(1h)
        | aggregate sum(time_to_detect)
        | limit 100

        ```

    === "Results"

        | sum_time_to_detect |
        | ------------------ |
        | 284610.40          |

!!! example "Retrieve the minimum value of 'time_to_detect' column in the `alerts` table"

    === "Query"

        ``` shell
        alerts
        | where created_at > ago(1h)
        | aggregate min(time_to_detect)
        | limit 100

        ```

    === "Results"

        | min_time_to_detect |
        | ------------------ |
        | 12.50              |

!!! example "Retrieve the maximum value of 'time_to_detect' column in the `alerts` table"

    === "Query"

        ``` shell
        alerts
        | where created_at > ago(1h)
        | aggregate max(time_to_detect)
        | limit 100

        ```

    === "Results"

        | max_time_to_detect |
        | ------------------ |
        | 7284.00            |

!!! example "Calculate the average value of 'time_to_detect' column in the `alerts` table"

    === "Query"

        ``` shell
        alerts
        | where created_at > ago(1h)
        | aggregate avg(time_to_detect)
        | limit 100

        ```

    === "Results"

        | avg_time_to_detect |
        | ------------------ |
        | 1035.66            |


!!! example "Count unique values of 'source.ip' column in the `events` table"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | aggregate count_distinct(source.ip)
        | limit 100

        ```

    === "Results"

        | count_distinct_source.ip |
        | ------------------------ |
        | 47                       |

!!! example "Create an array of the set of distinct values of 'source.ip' column in the `events` table"
    Note that `null` values are ignored.

    === "Query"

        ``` shell
        events
        | where created_at > ago(1h)
        | aggregate make_set(source.ip)
        | limit 100

        ```

    === "Results"

        | make_set_source.ip                                      |
        | ------------------------------------------------------- |
        | ["192.168.2.10", "192.168.2.22", "10.0.0.45", "1.5.178.82"] |

!!! example "Count allowed and denied network events per destination port using `countif`"

    === "Query"

        ``` shell
        events
        | where timestamp >= ago(24h) and event.category == 'network'
        | aggregate allowed = countif(action.outcome == 'success'), denied = countif(action.outcome == 'failure') by destination.port
        | order by denied desc
        | limit 100

        ```

    === "Results"

        | destination.port | allowed | denied |
        | ---------------- | ------- | ------ |
        | 443              | 8412    | 124    |
        | 80               | 3201    | 87     |
        | 22               | 145     | 63     |

## Render results in chart

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

!!! example "Count the number of events per asset in the events table and render it in a bar chart"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
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

## Join tables

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

!!! example "Join the tables events and intakes"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(24h)
        | limit 100
        | inner join intakes on sekoiaio.intake.uuid == uuid   // sekoiaio.intake.uuid belongs to events table and uuid belongs to intakes table
        | distinct intake.name

        ```

    === "Results"

        | intake.name  |
        | ------------ |
        | Sekoia Agent |
        | Zscaler      |
        | Zscaler ZIA  |

    The `model` object default name is related to the table name it is originating from. In this case, the model name is `intake` since the join was performed on the `intakes` table.

!!! example "Join the tables alerts and entities"

    === "Query"

        ``` shell
        alerts
        | where created_at > ago(24h)
        | limit 100
        | inner join entities on entity_uuid == uuid   // entity_uuid belongs to alerts table and uuid belongs to entities table
        | distinct entity.name

        ```

    === "Results"

        | entity.name        |
        | ------------------ |
        | HQ - London Office |
        | Cambridge Campus   |

    The `model` object default name is related to the table name it is originating from. In this case, the model name is `entity` since the join was performed on the `entities` table.

!!! example "Join the tables alerts and assets"

    === "Query"

        ``` shell
        alerts
        | join assets on assets.uuid == uuid
        | select short_id, rule_name, asset.name, asset.type
        | limit 10

        ```

    === "Results"

        | short_id     | rule_name                                                     | asset.name      | asset.type |
        | ------------ | ------------------------------------------------------------- | --------------- | ---------- |
        | ALqUHCbZMbnY | Mshta Suspicious Child Process                                | desktop-4932-vm | host       |
        | ALS5mN68LpbB | Mshta Command From A Scheduled Task                           | desktop-4932-vm | host       |
        | ALWzDs9pcVVb | CrowdStrike Falcon Intrusion Detection                        | root            | account    |
        | ALQbzwMvo1Aj | CrowdStrike Falcon Intrusion Detection Informational Severity | root            | account    |
        | ALTwu5cU16LK | PsExec Process                                                | root            | account    |
        | ALHGJU7tcoGb | CrowdStrike Falcon Intrusion Detection                        | root            | account    |
        | ALqPWeuUow4p | CrowdStrike Falcon Intrusion Detection High Severity          | root            | account    |

    The `model` object default name is related to the table name it is originating from. In this case, the model name is `asset` since the join was performed on the `assets` table.

!!! example "Define model object name"

    In this example, we define a specific name for the model object with the into operator.

    === "Query"

        ``` shell
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

## Lookup



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


## Compare


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



## In

Use the `in` operator to filter the rows based on a set of case-sensitive strings.
Use `in~` to filter on a set of case-insensitive strings.

``` shell
<table name>
| where <column name> in [<value 1>, <value 2>]

```

!!! example "Find events where `client.ip` equals to theses values: 192.168.0.1, 192.168.0.2."

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where client.ip in ['192.168.0.1', '192.168.0.2']
        | limit 100

        ```

    === "Results"

        | timestamp                | client.ip   |
        | ------------------------ | ----------- |
        | 2026-03-26T14:22:03.120Z | 192.168.0.1 |
        | 2026-03-26T14:19:47.883Z | 192.168.0.2 |
        | 2026-03-26T14:17:31.554Z | 192.168.0.1 |

!!! example "Find events where `process.name` equals to theses values ignoring case-sensitivity: powershell.exe, powershell_ise.exe"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where process.name in~ ['powershell.exe', 'powershell_ise.exe']
        | limit 100

        ```

    === "Results"

        | timestamp                | process.name      |
        | ------------------------ | ----------------- |
        | 2026-03-26T14:20:15.441Z | powershell.exe    |
        | 2026-03-26T14:18:52.007Z | PowerShell.exe    |
        | 2026-03-26T14:15:33.229Z | powershell_ise.exe |

## Contains

Use the `contains` operator to filter the rows that contains a case-sensitive string.
Use `contains~` to switch to case-insensitive strings.

``` shell
<table name>
| where <column name> contains <value 1>

```
!!! example "Find events where `user.full_name` contains the string `Admin` (case sensitive)"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where user.full_name contains 'Admin'
        | limit 100

        ```

    === "Results"

        | timestamp                | user.full_name      |
        | ------------------------ | ------------------- |
        | 2026-03-26T14:22:03.120Z | Admin User          |
        | 2026-03-26T14:19:47.883Z | AdminSecOps         |
        | 2026-03-26T14:17:31.554Z | John Admin          |

!!! example "Find events where `user.full_name` contains the string `ADMIN` (case insensitive)"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where user.full_name contains~ 'ADMIN'
        | limit 100

        ```

    === "Results"

        | timestamp                | user.full_name      |
        | ------------------------ | ------------------- |
        | 2026-03-26T14:22:03.120Z | Admin User          |
        | 2026-03-26T14:20:15.441Z | admin-svc           |
        | 2026-03-26T14:19:47.883Z | AdminSecOps         |

## Starts with

Use the `startswith` operator to filter rows that starts with a case-sensitive string.
Use `startswith~` to switch to case-insensitive strings.

``` shell
<table name>
| where <column name> startswith <pattern>

```

!!! example "Find events where `url.domain` starts with the string `api.prod`"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where url.domain startswith 'api.prod'
        | limit 100

        ```

    === "Results"

        | timestamp                | url.domain               |
        | ------------------------ | ------------------------ |
        | 2026-03-26T14:22:03.120Z | api.prod.example.com     |
        | 2026-03-26T14:19:47.883Z | api.prod-eu.example.com  |
        | 2026-03-26T14:17:31.554Z | api.prod.internal        |

!!! example "Find events where `process.command_line` starts with the string `Invoke` ignoring case-sensitivity"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where process.command_line startswith~ 'Invoke'
        | limit 100

        ```

    === "Results"

        | timestamp                | process.command_line                                  |
        | ------------------------ | ----------------------------------------------------- |
        | 2026-03-26T14:22:03.120Z | Invoke-Expression -Command "IEX (New-Object Net...)"  |
        | 2026-03-26T14:19:47.883Z | invoke-webrequest -Uri http://malicious.example.com   |
        | 2026-03-26T14:17:31.554Z | Invoke-Mimikatz -DumpCreds                            |

## Ends with

Use the `endswith` operator to filter rows that ends with a case-sensitive string.
Use `endswith~` to switch to case-insensitive strings.

``` shell
<table name>
| where <column name> endswith <pattern>

```

!!! example "Find events where `url.path` ends with the string `/admin`"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where url.path endswith '/admin'
        | limit 100

        ```

    === "Results"

        | timestamp                | url.path              |
        | ------------------------ | --------------------- |
        | 2026-03-26T14:22:03.120Z | /dashboard/admin      |
        | 2026-03-26T14:19:47.883Z | /api/v1/admin         |
        | 2026-03-26T14:17:31.554Z | /admin                |

!!! example "Find events where `process.command_line` ends with the string `.DLl` ignoring case-sensitivity"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where process.command_line endswith~ '.DLl'
        | limit 100

        ```

    === "Results"

        | timestamp                | process.command_line                            |
        | ------------------------ | ----------------------------------------------- |
        | 2026-03-26T14:22:03.120Z | rundll32.exe C:\Windows\System32\shell32.dll    |
        | 2026-03-26T14:19:47.883Z | regsvr32.exe /s C:\Temp\malicious.DLL           |
        | 2026-03-26T14:17:31.554Z | C:\Windows\System32\svchost.exe kernel32.DLl    |

## Not

Use the `not` operator to negate any comparison.

``` shell
<table name>
| where not <column name> <comparison operator> <pattern>

```
!!! example "Find events where `client.ip` does not equal to theses values: 192.168.0.1, 192.168.0.2"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where not client.ip in ['192.168.0.1', '192.168.0.2']
        | limit 100

        ```

    === "Results"

        | timestamp                | client.ip     |
        | ------------------------ | ------------- |
        | 2026-03-26T14:22:03.120Z | 192.168.2.10  |
        | 2026-03-26T14:20:15.441Z | 10.0.0.45     |
        | 2026-03-26T14:19:47.883Z | 1.5.178.82    |

!!! example "Find events where `user.full_name` does not contain the string `Admin` (case sensitive)"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where not user.full_name contains 'Admin'
        | limit 100

        ```

    === "Results"

        | timestamp                | user.full_name  |
        | ------------------------ | --------------- |
        | 2026-03-26T14:22:03.120Z | john.doe        |
        | 2026-03-26T14:20:15.441Z | alice.smith     |
        | 2026-03-26T14:19:47.883Z | bob.jones       |

!!! example "Find events where `process.command_line` does not start with the string `Invoke` ignoring case-sensitivity"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where not process.command_line startswith~ 'Invoke'
        | limit 100

        ```

    === "Results"

        | timestamp                | process.command_line                         |
        | ------------------------ | -------------------------------------------- |
        | 2026-03-26T14:22:03.120Z | C:\Windows\System32\svchost.exe -k netsvcs   |
        | 2026-03-26T14:20:15.441Z | chrome.exe --type=renderer                   |
        | 2026-03-26T14:19:47.883Z | python.exe script.py                         |

!!! example "Find events where `process.command_line` does not end with the string `.DLl` ignoring case-sensitivity"

    === "Query"

        ``` shell
        events
        | where timestamp > ago(1h)
        | where not process.command_line endswith~ '.DLl'
        | limit 100

        ```

    === "Results"

        | timestamp                | process.command_line                         |
        | ------------------------ | -------------------------------------------- |
        | 2026-03-26T14:22:03.120Z | powershell.exe -ExecutionPolicy Bypass       |
        | 2026-03-26T14:20:15.441Z | cmd.exe /c whoami                            |
        | 2026-03-26T14:19:47.883Z | python.exe -c "import os; os.system('id')"   |

## Regex

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

!!! example "Find events where `file.name` contains '.sh'"

    === "Query"

        ``` shell
        let StartTime = ago(1h);
        let EndTime = now();

        events
        | where timestamp between (StartTime .. EndTime)
        | where file.name matches regex '.*\.sh'
        | limit 100

        ```

    === "Results"

        | timestamp                | file.name           |
        | ------------------------ | ------------------- |
        | 2026-03-26T14:22:03.120Z | deploy.sh           |
        | 2026-03-26T14:19:47.883Z | cleanup.sh          |
        | 2026-03-26T14:17:31.554Z | install_agent.sh    |

## Variables

Use the `let` operator to define variables.

``` shell
let <variable name> = <string | integer>;

<table name>
| where <column name> == <variable name>

```

!!! example "Count the number of events in the last 24 hours"

    === "Query"

        ``` shell
        let StartTime = ago(24h);
        let EndTime = now();

        events
        | where event.created > StartTime and event.created <= EndTime
        | count

        ```

    === "Results"

        | count |
        | ----- |
        | 8924  |

## Comments

Use `//` to add comments in the query.

!!! example
``` shell
// Comment the filtering condition

<table name>
//| where <column name> = <variable name>
| limit 100

```

## Related articles

### Getting Started & Overview
* [SOL Overview](/xdr/features/investigate/sol_overview.md): Sekoia Operating Language overview.
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
