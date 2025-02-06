# Sekoia Operating Language (SOL)

## Power and Simplicity in Security Analytics

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

### Alerts properties

| **Alert Property**        | **Description**                                                                              |
|---------------------------|----------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the alert.                                                           |
| short_ID                  | A concise identifier for quick reference to the alert.                                       |
| community_uuid            | A unique identifier for the community the alert belongs to.                                  |
| entity_uuid               | A unique identifier representing the entity associated with the alert.                       |
| entity_name               | The name of the entity linked to the alert.                                                  |
| rule_name                 | The name assigned to the rule that triggered the alert.                                      |
| rule_pattern              | The detection pattern of the alert.                                                          |
| detection_type            | The method by which the alert was detected.                                                  |
| alert_type_category       | The category of the alert.                                                                   |
| alert_type_value          | The type of the alert.                                                                       |
| status                    | The current state of the alert (e.g., open, acknowledged, resolved).                         |
| urgency                   | The level of urgency assigned to the alert.                                                  |
| created_at                | The date and time when the alert was initially created.                                      |
| update_at                 | The date and time when the alert was last updated.                                           |
| first_seen_at             | The date and time of the first alert occurrence.                                             |
| last_seen_at              | The date and time of the last alert occurrence.                                              |
| time_to_detect            | Duration taken to identify the alert from its occurrence in seconds.                         |
| time_to_acknowledge       | Time elapsed from detection to official acknowledgment of the alert in seconds.              |
| time_to_respond           | Duration taken to take action after acknowledgment in seconds.                               |
| time_to_resolve           | The total time taken to completely resolve the alert in seconds.                             |
| time_to_ingest            | The duration from alert generation to its final ingestion into the system in seconds.        |
| occurrences               | The number of alert occurrences                                                              |
| rule_instance_uuid        | A unique identifier for the rule that generated the alert.                                   |
| cases                     | List of cases associated to the alert.                                                       |
| assets                    | List of assets associated to the alert.                                                      |
| threats                   | List of threats associated the alert.                                                        |

### Cases properties

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the case.                                                          |
| short_id                  | A concise identifier for quick reference to the case.                                      |
| community_uuid            | A unique identifier for the community related to the case.                                 |
| title                     | The title or subject line of the case.                                                     |
| description               | A detailed description outlining the case's context or issues.                             |
| priority                  | The importance level assigned to the case, indicating its urgency.                         |
| created_at                | The date and time when the case was created.                                               |
| created_by                | The user or system that created the case.                                                  |
| created_by_type           | The type of entity that created the case (e.g., user, automated system).                   |
| updated_at                | The date and time when the case was last updated.                                          |
| updated_by                | The user or system that last updated the case.                                             |
| updated_by_type           | The type of user that last updated the case.                                               |
| first_seen_at             | The date and time when the case was first detected.                                        |
| last_seen_at              | The date and time when the case was last observed or updated.                              |

### Entities properties

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the entity.                                                        |
| name                      | The name of the entity.                                                                    |
| alerts_generation         | The alert generation mode of the entity.                                                   |
| description               | The description of the entity.                                                             |
| entity_id                 | The ID of the entity.                                                                      |
| community_uuid            | A unique identifier for the community related to the entity.                               |
| created_at                | The date and time when the entity was created.                                             |
| updated_at                | The date and time when the entity was last updated.                                        |

### Intakes properties

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the intake.                                                        |
| name                      | The name of the intake.                                                                    |
| community_uuid            | A unique identifier for the community related to the intake.                               |
| entity_uuid               | A unique identifier for the entity related to the intake.                                  |
| format_uuid               | A unique identifier for the format related to the intake.                                  |
| intake_key                | The intake key of the intake.                                                              |
| created_at                | The date and time when the intake was created.                                             |
| created_by                | The user or system that created the intake.                                                |
| created_by_type           | The type of entity that created the intake (e.g., avatar, apikey).                         |
| updated_at                | The date and time when the intake was last updated.                                        |
| updated_by                | The user or system that last updated the intake.                                           |
| updated_by_type           | The type of user that last updated the intake.                                             |
| is_custom_format          | Indicate if the intake uses a custom format.                                               |
| connector_configuration_uuid    | A unique identifier for the connector configuration related to the intake.           |

### Communities properties

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the community.                                                     |
| name                      | The name of the community.                                                                 |
| description               | The description of the community.                                                          |
| homepage_url              | The homepage url of the community.                                                         |
| picture_mode              | The picture mode of the community.                                                         |
| intake_key                | The intake key of the community.                                                           |
| created_at                | The date and time when the community was created.                                          |
| created_by                | The user or system that created the community.                                             |
| created_by_type           | The type of entity that created the community (e.g., avatar, apikey).                      |
| updated_at                | The date and time when the community was last updated.                                     |
| company_size              | The size of the company.                                                                   |
| company_security_team_size  | The size of the security team.                                                           |
| company_sector            | The sector of the company.                                                                 |
| company_location          | The location of the company.                                                               |
| is_parent                 | Indicate if the community is a parent community.                                           |
| parent_uuid               | A unique identifier of the parent community.                                               |
| subcommunities            | Indicate if the community has subcommunities.                                              |
| is_mfa_enforced           | Indicate if MFA is enforced at the community level.                                        |
| session_timeout           | The duration before users are automatically logged after inactivity.                       |
| disable_inactive_avatars  | Indicate if users are disabled after 90 days of inactivity.                                |
| disabled                  | Indicate if the community is disabled.                                                     |

## Operators

The next sections describe the different operators supported by Sekoia Operating Language (`SOL`).

### Count rows
    
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

### Select columns
    
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

### Distinct
    
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

### Where
    
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
| where timestamp > ago(5d) and user_agent.device.name == “Mac”
| limit 100

```

**Example 2**

Filter the query by excluding events older than `5 days` and retrieving only user agent from `Mac` or `Android`

``` shell
events
| where timestamp > ago(5d) and (user_agent.device.name == “Mac” or user_agent.device.name == “Android”)
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

### Sort results
    
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
| order by urgency desc, first_seen_at asc
| select short_id, rule_name, urgency, first_seen_at
| limit 100

```

---

### Limit results

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

### Get the Top n rows 

**Description**

Use the `top` operator to returns the first n rows sorted by the specified column.

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

### Create calculated columns

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

### Aggregate rows

**Description**

Use the `aggregate` operator to group rows by a column and perform aggregations with a chosen function: `count`, `sum`, `min`, `max`, `avg`, `count_distinct`, `make_set`.

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
| where timestamp >= ago(24h) and event.category == "authentication"
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

---

### Render results in chart

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

### Join tables

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
| inner join intakes on sekoiaio.intake.uuid == uuid   // sekoiaio.intake.uuid belongs to events table and uuid belongs to intakes table
| select intake.name

```

The `model` object default name is related to the table name it is originating from. In this case, the model name is `intake` since the join was performed on the `intakes` table.

**Example 2**

Join the tables alerts and entities

``` shell
alerts
| where created_at > ago(24h)
| inner join entities on entity_uuid == uuid   // entity_uuid belongs to alerts table and uuid belongs to entities table
| select entity.name

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

### Lookup

**Description**

Use the `lookup` operator to extend a table. Extends the current table with values looked-up in another table.
Prefer the `lookup` operator over `join` when the right table is small enough to fit into memory to improve query performance.

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

---

### Compare

**Description**

Use the following operators to compare values.

| Comparator | Description | Examples |
| --- | --- | --- |
| == | Equals | `1 == 1` |
| != | Not equals | `1 != 0` |
| < | Less | `1 < 10` |
| <= | Less or equals | `4 <= 5` |
| > | Greater | `20 > 10` |
| >= | Greater or equals | `5 >= 4` |

---

### In

**Description**

Use the `in` operator to filter the rows based on a set of case-sensitive strings.

``` shell
<table name>
| where <column name> in (<value 1>, <value 2>)

```

**Example**

Find events where `client.ip` equals to theses values: 192.168.0.1, 192.168.0.2.

``` shell
events
| where client.ip in ('192.168.0.1', '192.168.0.2')
| limit 100

```

---

### Contains

**Description**

Use the `contains` operator to filter the rows that contains a case-sensitive string.

``` shell
<table name>
| where <column name> contains <value 1>

```

**Example**

Find events where `user.full_name` contains the string `Admin`.

``` shell
events
| where user.full_name contains 'Admin'
| limit 100

```

---

### Starts with

**Description**

Use the `startswith` operator to filter rows that starts with a case-sensitive string.

``` shell
<table name>
| where <column name> startswith <pattern>

```

**Example**

Find events where `url.domain` starts with the string `api.prod`.

``` shell
events
| where url.domain startswith 'api.prod'
| limit 100

```

---

### Ends with

**Description**

Use the `endswith` operator to filter rows that ends with a case-sensitive string.

``` shell
<table name>
| where <column name> endswith <pattern>

```

**Example**

Find events where `url.path` ends with the string `/admin`.

``` shell
events
| where url.path endswith '/admin'
| limit 100

```

---

### Variables

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

### Comments

**Description**

Use `//` to add comments in the query.

**Example**

``` shell
// Comment the filtering condition

<table name>
//| where <column name> = <variable name>
| limit 100

```

## Functions

### Datetime: now()

**Description**

Returns the current **UTC** time, optionally offset by a given timespan.

**Example**

``` shell
let time = now();

let time_earlier = now(-2d);

```

---

### Datetime: ago()

**Description**

Returns a datetime value equal to the current UTC time minus the timespan.

| Syntax | Description | Example | Length of time |
| --- | --- | --- | --- |
| d | day time interval | `2d` | 2 days |
| h | hour time interval | `1h` | 1 hour |
| m | minute time interval | `30m` | 30 minutes |
| s | second time interval | `10s` | 10 seconds |

**Example**

``` shell
let time = ago(1h);

```

---

### Timestamp: bin()

**Description**

Rounds values down to an integer multiple of a given bin size.

**Example**

``` shell
events
| aggregate count() by bin(timestamp, 1d)

```

---

### Year
    
**Description**

Returns the year by a given date in the following format: `YYYY`.

**Example**

``` shell
let time = year(now());

```

---

### Month
    
**Description**

Returns the year and month by a given date in the following format: `YYYY-MM`.

**Example**

``` shell
let time = month(now());

```

---

### Week
    
**Description**

Returns the year and month by a given date in the following format: `YYYY - Week {week number}`.

**Example**

``` shell
let time = week(now());

```

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
| where timestamp >= ago(24h) and event.category == "authentication"
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

---

### host.os.type per Sekoia endpoint agent

``` shell
events
| where sekoiaio.intake.dialect == "sekoia.io endpoint agent"
| aggregate count() by host.os.type
| limit 100

```

---