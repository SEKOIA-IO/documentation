# Query Builder reference

This page provides a detailed reference for all operators, clauses, and properties available within the Query Builder **Form mode**. Use these tables to look up specific parameters for your hunting sessions.

### Query clauses

| Clause | Description |
| :--- | :--- |
| **SELECT** | Choose the specific columns you want to display in the result table. |
| **AGGREGATION** | Aggregate rows using functions like average, count, min, max, sum, or unique count. |
| **WHERE** | Define the specific conditions the data must meet. |
| **GROUP BY** | Group rows by identical data points. |
| **ORDER BY** | Sort the resulting rows by a specific value. |
| **LIMIT** | Restrict the number of rows returned in the results. |

### Operators

Use these operators within the **WHERE** clause to define your conditions.

| Operator | Description |
| :--- | :--- |
| **is** / **is not** | Equals / Not equals (case-sensitive). |
| **starts with** / **ends with** | Value starts or ends with the specified string. |
| **contains** | The field contains the specified value. |
| **exists** / **does not exists** | Checks if the field has a value or is empty. |
| **within** | Filters data within a specified date range. |
| **< , <= , > , >=** | Standard mathematical comparisons. |

### System limits

!!! warning "Platform rate limits"
    To protect platform health, the following limits are enforced:
    * **Processed rows**: Maximum 10,000. Results will be partial if this limit is reached.
    * **Query frequency**: 10 executions per minute per user.
    * **Query timeout**: Queries automatically time out after 10 minutes.

### Query table columns

| Column | Description |
| :--- | :--- |
| **Author** | The original creator of the query. |
| **Edited by** | The last user who modified the query. |
| **Created by** | The user who first saved the query. |
| **Available in...** | The number of dashboards currently using this query. |
| **Shared by** | The workspace or entity that shared the query. |
