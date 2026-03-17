# Configure custom alert statuses

Custom statuses allow you to tailor the alert lifecycle to your SOC team's specific processes. You can create, edit, and organize statuses to match your organization's workflow requirements.


## Prerequisites

You must have administrative access to the configuration pages.


## Status stages

Each custom status belongs to one of three stages:

| Stage | Description |
|---|---|
| **Open** | Initial stage for new alerts. |
| **In Progress** | Intermediate stage for investigation or action. |
| **Closed** | Final stage for resolved or dismissed alerts. |


## Create a custom status

1. On the left panel, navigate to **Settings** > **Configuration** > **Custom Statuses** page.
2. In the appropriate stage, click **+** to create a new custom status.
3. Enter a **Name** (e.g., "Awaiting User Response").
4. Enter a **Description** for context.
5. Use the checkboxes in the **Alert** and **Case** columns to enable the status for each context.
6. Click **Save**.

## Manage statuses

- **Edit**: Click on a status to update the name or description. Modifying these does not affect historical data in timelines.
- **Reorder**: Use the drag handle on each status to drag and drop them into your desired order.
- **Delete**: Click the delete icon. You can only delete a status if it is not currently applied to any alert or case.

## Related articles

* [Configure custom verdicts](/xdr/features/investigate/configure_custom_verdicts.md): Standardize how your team classifies alert outcomes.
* [Alerts](/xdr/features/investigate/alerts.md): Understand the underlying logic of alert stages and lifecycles.
* [Manage alerts](/xdr/features/investigate/manage_alerts.md): Learn how to filter and process alerts in the Operations Center.
