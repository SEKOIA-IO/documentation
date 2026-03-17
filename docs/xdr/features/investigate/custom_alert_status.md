# Configure custom alert statuses

Custom statuses allow you to tailor the alert lifecycle to your SOC team's specific processes. You can create, edit, and organize statuses to match your organization's workflow requirements.

## Prerequisites

!!! warning "Access required"
    You must have administrative access to the configuration pages.

## Status stages

Each custom status belongs to one of three stages that define its position in the alert lifecycle:

| Stage | Description |
|---|---|
| **Open** | Initial stage for new or unprocessed alerts. |
| **In Progress** | Intermediate stage for alerts under investigation or awaiting action. |
| **Closed** | Final stage for alerts that have been resolved or dismissed. |

These stages determine the overall state of an alert and affect features such as search filters and similarity grouping.

## Create a custom status

1. Navigate to the **Custom Statuses** configuration page.
2. Click **+** to create a new custom status in the appropriate stage.
3. Enter a **Name** (e.g., "Awaiting User Response").
4. Enter a **Description** about when this status should be used.
5. Use the checkboxes in the **Alert** and **Case** columns to enable the status for each context.
6. Click **Save**.

> [SCREENSHOT SUGGESTION: The Custom Statuses configuration page showing the stage columns, checkboxes, and the + button. | ALT TEXT: Custom Statuses configuration page with Alert and Case columns.]

## Enable a status for alerts and cases

A custom status can be shared across both alerts and cases, ensuring consistent terminology throughout your SOC platform.

!!! tip
    Enabling the same status for both alerts and cases reduces the number of statuses to manage and improves communication across investigation contexts.

1. In the **Custom Statuses** configuration page, locate the status you want to configure.
2. Select the checkbox in the **Alert** column, the **Case** column, or both.

## Edit a custom status

1. Click the status you want to modify.
2. Update the **Name** or **Description**.
3. Click **Save**.

!!! note
    Modifying a status name or description does not affect historical data. Previously recorded status changes continue to display the original values in alert timelines and case histories.

## Reorder statuses

1. On the **Custom Statuses** configuration page, locate the drag handle on the status you want to move.
2. Drag and drop the status to your preferred position.

The new order is immediately reflected in all status dropdowns across the platform.

## Delete a custom status

!!! warning "Status in use cannot be deleted"
    You can only delete a status if it is not currently applied to any alert or case. Reassign all affected items to a different status before proceeding.

1. Reassign all alerts and cases using the status to a different status.
2. Return to the **Custom Statuses** configuration page.
3. Click the delete icon next to the status.

## Related articles

* [Configure custom verdicts](/xdr/features/investigate/configure_custom_verdicts.md): Standardize how your team classifies alert outcomes.
* [Alerts](/xdr/features/investigate/alerts.md): Understand the underlying logic of alert stages and lifecycles.
* [Manage alerts](/xdr/features/investigate/manage_alerts.md): Learn how to process alerts using custom statuses.
