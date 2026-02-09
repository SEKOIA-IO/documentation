# Create and manage queries

Let's dive into the process of building your first query. You can choose between a guided experience or a code-centric approach depending on your technical needs.

## Prerequisites

* You must have an active Sekoia.io account.
* You must have logs, alerts, or cases already ingested into your workspace.

## Build a query using the Form

The Form mode acts as a wizard to help you structure your request without writing code.

!!! tip "Discover the full potential of Form mode"

    To discover the all operators, clauses, and properties available within the Query Builder Form mode consult the [Query Form Reference article](/xdr/features/investigate/query_builder_form_reference.md).


1. Navigate to the **Query Builder** page: : Left panel > **Investigate** > **Queries**.
2. On the upper right corner, click **New Query**. 
3. Ensure the toggle is set to **Form**.
4. In the **From** clause, select the data source you want to query.
5. To refine your search, click the **Add clause** button.
6. Select a clause (e.g., **WHERE** or **AGGREGATION**) and enter your parameters.
7. To view the results, click **Run query**.

## Build a query using Code (SOL)

Code mode is the default interface. It uses the SOL language to provide higher precision for filters and complex queries.

!!! tip "Master the SOL Syntax"

    To learn how to write advanced queries and create custom filters for your dashboards, consult the [SOL Language Reference](/xdr/features/investigate/sekoia_operating_language.md).


1. Navigate to the **Query Builder** page.
2. Ensure the toggle is set to **Code**.
3. Enter your query using the SOL syntax in the editor.
4. To view the results, click **Run query**.


## Save and manage results

1. To filter your results, click the right end side of the filter button. A dropdown panel opens, allowing you to select your filtering options.
2. To save your configuration, enter a title in the **Title** field and click **Save**.
3. To export the data, click the **Export** button to download a `.jsonl` file.

!!! note "Visibility"
    Saved queries are visible to all users within your community. In MSSP multi-tenancy environments, saved queries are not visible in sub-communities.
