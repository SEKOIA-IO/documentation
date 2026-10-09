# Manage cases

The cases listing page centralizes all cases across your community. This article explains how to filter and sort cases, perform bulk actions on multiple cases simultaneously, and edit individual cases.

## Filter and sort cases

![Case listing with filter](/assets/operation_center/cases/cases-filter.png){: style="max-width:100%"}

You can filter cases by the following criteria:

| Filter | Description |
|---|---|
| Asset | Shows cases linked to a specific asset. |
| Assignee | Shows cases assigned to a specific analyst. |
| Creator | Shows cases created by a specific user. |
| Custom fields | Filters by any custom field defined in your community. |
| Priority | Filters by priority level (for example, High, Medium, Low). |
| Status | Filters by lifecycle stage (for example, Open, In progress, Closed). |
| Tag | Filters by one or more tags. |
| Verdict | Filters by case outcome (for example, True positive, False positive). |

You can sort the listing by:

* **Last edition** (default)
* **Creation date**
* **Highest priority**

## Perform bulk actions on cases

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

You can act on multiple cases simultaneously from the listing page. This is useful for triaging large volumes of cases or reassigning incidents at scale.

![Case listing with bulk actions](/assets/operation_center/cases/cases-bulk-actions.png){: style="max-width:100%"}

### Select multiple cases

Three selection methods are available:

1. **Individual selection**: Click the checkbox on the left side of each case row.
2. **Page selection**: Click the checkbox in the table header to select all cases visible on the current page (up to 25, 50, or 100 cases depending on your page size setting).
3. **Global selection**: After activating page selection, a banner appears at the top of the list. Use it to extend your selection to all cases matching your active filters, up to the platform limit.

!!! note "Selection limit"
    Mass selections are capped at 5,000 cases at a time to maintain platform performance. If your filtered results exceed 5,000 cases, a tooltip informs you of this limit. Use the **Clear selection** button in the action banner to deselect all cases and reset the view.

### Available bulk actions

Once you select at least one case, the bulk action toolbar replaces the **Filters** toolbar at the top of the list. The following actions are available:

| Action | Description |
|---|---|
| Change priority | Updates the priority for all selected cases. |
| Change status | Updates the status for all selected cases. Opens the **Close cases** modal when the new status is in the **Closed** stage. |
| Change verdict | Updates the verdict for all selected cases. |
| Change assignee | Reassigns all selected cases to a specific user. |

### Close cases in bulk

When you change the status of the selected cases to a status in the **Closed** stage, the **Close cases** modal opens. If the new status belongs to another stage, the status is applied directly and no modal appears.

![Close cases modal](/assets/operation_center/cases/cases-bulk-close-modal.png){: style="max-width:60%"}

!!! warning
    Once closed, a case no longer receives alerts.

To close the selected cases:

1. In **Add comment**, optionally write a comment. It is added to each case being closed.
2. In **Verdict**, select the verdict for the cases. This field is required.
3. In **Apply a status to alerts**, select the status to apply to the alerts in the cases. Only custom statuses from the **Closed** stage are proposed. To leave the alert statuses unchanged, click the **X** in the field to clear it.
4. Click **Close**.

Each alert whose status changes receives a new comment in its timeline that records the change and the case it comes from, for example:

> This alert was Closed following a status change in case ID [CA55URAvSYLG], with the following message: User comment

The status name, the case ID and the message reflect your selection and the comment you entered.

## Edit a case

!!! warning "Editing restriction"
    You can only edit cases with a status in the **Open** or **In progress** stage. Cases with a **Closed** status cannot be edited.

To edit a case:

1. Click the case to open the details view.
2. Click **Edit**.
3. Update the fields you want to change.
4. Click **Save**.

## Related articles

* [Cases](/xdr/features/investigate/cases.md): Overview of what cases are and how they are structured.
* [Create a case](/xdr/features/investigate/create_a_case.md): Step-by-step instructions to open a new case and attach alerts to it.
* [Case details](/xdr/features/investigate/case_details.md): Reference for every tab and field available on the case details page.
* [Custom fields](/xdr/features/investigate/custom_fields.md): How to filter alerts and cases by custom field values and manage field definitions.
* [Alerts](/xdr/features/investigate/alerts.md): How alerts are created and how to manage them before grouping them into cases.
* [Playbooks](/xdr/features/automate/index.md): How to automate case workflows and trigger actions based on case updates.
* [Dashboards](/xdr/features/report/dashboards.md): How to monitor case activity and investigation KPIs across your community.
