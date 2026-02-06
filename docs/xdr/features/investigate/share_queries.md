# Share a query with a community

Individual queries created in a workspace can be shared with sub-communities to facilitate threat hunting and log analysis without sharing an entire dashboard. 

## Prerequisites

* You must have an existing query saved in your workspace.
* You must have the necessary permissions to manage access for the target communities.

## Share a query

To make a query available to other communities:

1. Navigate to the **Queries** page.
2. Open the query you wish to share or create a new one.
3. Click **Manage Access**.
4. In the list provided, select the communities you want to share the query with.
5. Click **Save**.

!!! note "Read-only mode"

    Shared queries are available to users in the destination community in read-only mode. Users in these communities can execute the query but cannot modify the original version.


## Duplicate a shared query

If you need to edit a query that has been shared with your community, you must duplicate it first. The original shared query remains in read-only mode, while your duplicated version is fully customizable.

1. Navigate to the **Queries** page.
2. Locate the shared query you wish to modify.
3. Click the **...** (three dots) icon associated with the query.
4. Select **Duplicate**.
5. Enter a new name for the duplicated query.
6. Click **Save**.

!!! tip "Customization"

    Once duplicated, the query is considered a **Personal** type query. You can freely modify the SOL code, filters, or visualization settings.
