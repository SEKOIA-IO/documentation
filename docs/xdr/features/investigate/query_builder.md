# Query Builder (beta)

Start exploring your data with the Query Builder. Hunt for threats, get analytics, create reports. The Query Builder is a simple form which allows you to build queries to explore your data. 
Using this form, you can now aggregate your data to extract new insights. The Query Builder also offers the possibility to visualize data through different kinds of charts.

At the moment, only the `Events` table is available but more tables are coming.

![query builder](/assets/operation_center/events/qb-run.gif){: style="max-width:100%"}

## Build your query

Select a table to query in the `From` clause and use `Add clause` button to refine your query.

![clauses](/assets/operation_center/events/qb-clauses.gif){: style="max-width:100%"}

The Query Builder comes with the following clauses:

| Clause | Description |
| --- | --- |
| SELECT | Choose columns you want to display |
| AGGREGATION | Aggregate rows with `average` / `count` / `min` / `max` / `sum` / `unique count` |
| WHERE | Define query conditions |
| GROUP BY | Group rows by identical data |
| ORDER BY | Order rows by a specific value |
| LIMIT | Limit the number of rows in results |

### Aggregation

Create an aggregation by using the `Aggregate` clause. Select a type of aggregation, a column and a label for your aggregation.

![aggregation](/assets/operation_center/events/qb-aggregation.gif){: style="max-width:100%"}

The following aggregation types are available.

| Aggregation type | Description |
| --- | --- |
| Average | Average of a set |
| Count | Count the number of rows in a set |
| Min | Find the minimum value in a set |
| Max | Find the maximum value in a set |
| Sum | Sum of a set|
| Unique count | Count unique values of a set |

### Operators

Use the following operators to define your conditions in the `WHERE` clause.

| Operator | Description |
| --- | --- |
| is | Equals (case-sensitive) |
| is not | Not equals (case-sensitive) |
| starts with | Starts with the specified value (case-sensitive) |
| does not start with | Does not start with the specified value (case-sensitive) |
| ends with | Ends with the specified value (case-sensitive) |
| does not end with | Does not end with the specified value (case-sensitive) |
| contains | Contains the specified value (case-sensitive) |
| does not contain | Does not contain the specified value (case-sensitive) |
| exists | Has a value |
| does not exists | Does not have a value |
| within | Within the specified date range |
| < | Strictly less than |
| <= | Less than or equal to |
| > | Strictly more than |
| >= | More than or equal to |

## Run your query

Click on `Run query` to perform a search.

![results](/assets/operation_center/events/qb-results.png){: style="max-width:100%"}

You can display your results in a table or select a chart type (Pie chart or Vertical bar chart).

!!! warning
    Due to the important amount of logs ingested, the Query Builder has **rate limits** to protect the platform's health.

    There are 3 **rate limits**:

    1. **Maximum number of processed rows:** At the moment the maximum value is 10 000.
    2. **Maximum number of query:** 10 query executions are allowed per minute.
    3. **Query timeout:** A query will timeout automatically after 10 minutes.

    About the **maximum number of processed rows** limit, the Query Builder will display partial results in case this limit is reached.

## Chart visualization

### Pie chart

![pie chart](/assets/operation_center/events/qb-pie-chart.png){: style="max-width:100%"}

Use the pie chart to show how a total amount is divided between distinct groups. We have limited the max number of values in pie chart to 40 to ensure a correct display.

- In `Label` field, select the column you want to use as a label.
- In `Value` field, select the column you want to use as a value.

If possible, we will try to automatically select adequate columns.

### Vertical chart

![bar chart](/assets/operation_center/events/qb-bar-chart.png){: style="max-width:100%"}

Use the vertical bar chart to compare values between different groups. We have limited the max number of values in vertical chart to 80 to ensure a correct display.

- In `X-axis`, select the column you want to use. This column can be of any type.
- In `Y-axis`, select the column you want to use. This column must be a numeric value.

## Save your query

You can save your query to re-execute it later.
Choose a title for your query and click on the `Save` button.

Your last result is also saved and will be displayed when you open your saved query.

!!! note 
    - Saved queries are visible to all users of your community.<br/>
    - In MSSP multi-tenancy, saved queries are not visible in sub-communities.

## Export your results

You can export your results in JSON Lines format. Export file will have `.jsonl` extension.

![export](/assets/operation_center/events/qb-export.png){: style="max-width:100%"}

JSON Lines is a convenient format for storing structured data that may be processed one record at a time. It works well with unix-style text processing tools and shell pipelines.

See [JSON Lines documentation](https://jsonlines.org/) for more details.