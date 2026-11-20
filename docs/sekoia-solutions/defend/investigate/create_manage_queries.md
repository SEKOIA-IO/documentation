# Create and manage queries

Let's dive into the process of building your first query. You can choose between a guided experience or a code-centric approach depending on your technical needs.

## Prerequisites

* You must have an active Sekoia.io account.
* You must have logs, alerts, or cases already ingested into your workspace.

## Build a query using the Form

The Form mode acts as a wizard to help you structure your request without writing code.

{% hint style="success" %}
**Discover the full potential of Form mode**


To discover the all operators, clauses, and properties available within the Query Builder Form mode, consult the [Query Form Reference article](query_builder_form_reference.md).
{% endhint %}


1. Navigate to the **Query Builder** page: : Left panel > **Investigate** > **Queries**.
2. On the upper right corner, click **New Query**. 
3. Ensure the toggle is set to **Form**.
4. In the **From** clause, select the data source you want to query.
5. To refine your search, click the **Add clause** button.
6. Select a clause (e.g., **WHERE** or **AGGREGATION**) and enter your parameters.
7. To view the results, click **Run query**.

## Build a query using Code (SOL)

Code mode is the default interface. It uses the SOL language to provide higher precision for filters and complex queries.

{% hint style="success" %}
**Master the SOL Syntax**


To learn how to write advanced queries and create custom filters for your dashboards, consult the [SOL Language Reference](sol_overview.md).
{% endhint %}


1. Navigate to the **Query Builder** page.
2. Ensure the toggle is set to **Code**.
3. Enter your query using the SOL syntax in the editor.
4. To view the results, click **Run query**.


## Save and manage results

1. To filter your results, click the right end side of the filter button. A dropdown panel opens, allowing you to select your filtering options.
2. To save your configuration, enter a title in the **Title** field and click **Save**.
3. To export the data, click the **Export** button to download a `.jsonl` file.

{% hint style="info" %}
**Visibility**

Saved queries are visible to all users within your community. In MSSP multi-tenancy environments, saved queries are not visible in sub-communities.
{% endhint %}

## Related articles

### Getting Started & Overview
* [SOL Overview](sol_overview.md): Sekoia Operating Language overview.
* [SOL Getting Started](sol_getting_started.md): This tutorial walks you through writing your first SOL queries. By the end, you'll be able to search events, filter results, and save queries for reuse.
* [SOL Best Practices](sol_best_practices.md): Best practices to use SOL effectively.

### User Guides
* [SOL How-to Guides](sol_how_to_guides.md): Learn how to use the main functions of SOL to reach your goals (aggregate data, join tables, use external data, build a query library...).
* [SOL Query Examples](sol_query_examples.md): Get inspiration from our examples.
* [SOL Datasets](sol_datasets.md): Discover the CSV import feature that enables SOC analysts to enrich security investigations by importing external data sources directly into the SOL query environment.

### Technical Reference
* [SOL Data Sources Reference](sol_ref_datasources.md): Technical references to access security data within the Sekoia platform thanks to SOL.
* [SOL Functions Reference](sol_ref_functions.md): Reference article regarding functions used in SOL.
* [SOL Operators Reference](sol_ref_operators.md): Reference article regarding operators used in the SOL language.
