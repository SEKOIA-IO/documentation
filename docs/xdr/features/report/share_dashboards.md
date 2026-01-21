# Share dashboards

Shared dashboards allow you to provide standardized data visualization across different environments and communities. This feature ensures consistency in monitoring by allowing sub-communities to benefit from centralized security expertise.

## Share a dashboard

A workspace can share a dashboard with one or several communities to maintain visibility across the organization.

Before you start make sure that:

* You have the **Write** permission for dashboards in your workspace.
* The dashboard does NOT contain queries with **SOL parameters** or specific **Parameters**, as these cannot be shared at the moment.

###
1. Navigate to the dashboard you want to share.
2. Click **Manage Access**.
3. Select the communities you want to share the dashboard with.
    
    !!! warning "Query validation"
        Review all queries within the dashboard to ensure the logic and data exposure are appropriate for the target communities.

4. Click **Save**.

## Manage shared dashboards

Shared dashboards provide specific access levels and visibility rules to maintain data integrity across communities.

### Query visibility and access

* **Read-only access**: Shared queries within a dashboard are available in read-only mode for the destination community.
* **Queries page**: Shared queries appear on the **Queries** page for all members of the receiving community.

### Dashboard organization

To track and organize shared content, use the dashboard listing tools:

* **Identify access**: View the **Accessible by** column in the dashboard listing to see which entities can access a specific dashboard.
* **Filter views**: Use the dashboard filters to sort by **Internal**, **Shared**, or **Personal** dashboards.

## Customize a shared dashboard

To modify a dashboard shared by another community, you must create a local copy.

!!!note "Internal query persistence"
    Duplicating a dashboard does not make the internal queries editable. To modify data visualizations, you must duplicate the individual queries within the dashboard separately.

1. Navigate to the shared dashboard you wish to edit.
2. Click **Duplicate**.
3. To modify the underlying data, follow the procedure to duplicate a shared query for each query in the dashboard.
