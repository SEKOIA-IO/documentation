# Manage custom statuses

This article explains how to create, edit, reorder and enable custom statuses from the configuration page, and how to set the default status of automatically generated alerts. All of it happens in **Settings > Custom Statuses**, under the **Status** section.

## Create a custom status

Statuses are grouped by stage, and you create a status directly inside the stage it belongs to.

1. Navigate to **Settings > Custom Statuses**.
2. Click `+` under the stage you want the status to belong to: **Open**, **In progress** or **Closed**.
3. Enter a **Name**, for example "Under investigation" or "Awaiting user response".
4. Enter a **Description** explaining when your team should use this status.
5. Save your changes.

![Custom statuses configuration](/assets/operation_center/alerts/custom-statuses-config.png){: style="max-width:100%"}

!!! tip "Choose the stage deliberately"
    The stage is not a label, it drives platform behavior. Alerts in the Open and In progress stages keep collecting similar occurrences, and cases in the Closed stage can no longer be edited. Pick the stage that matches what the status means operationally.

## Edit a custom status

1. Click the edit icon on the status you want to modify.
2. Update the name, the description, or both.
3. Save your changes.

!!! note "Renaming does not rewrite history"
    Alert timelines and case histories keep the status name that was in use at the time of each change, so renaming a status never alters past records.

## Reorder statuses

The order you set here is the order analysts see in every status menu across the platform.

1. Navigate to **Settings > Custom Statuses**.
2. Drag a status by its handle.
3. Drop it in the position you want.

## Enable a status for alerts and cases

A status can serve alerts, cases, or both. The **Alert** and **Case** columns control this, one checkbox per context.

1. Locate the status you want to configure.
2. Select the checkbox in the **Alert** column to make it available on alerts.
3. Select the checkbox in the **Case** column to make it available on cases.

Selecting both gives you a unified status, so your team uses the same vocabulary whether it is triaging an alert or investigating a case.

Clearing a checkbox on a status that alerts or cases already carry starts a migration, because those items need somewhere to go. See [Migrate custom statuses](/xdr/features/investigate/migrate_custom_statuses.md).

## Set the alert default status

When an entity uses the `automatic` alert generation mode, its new alerts are created directly in a status of the **In progress** stage. Because this stage can hold several statuses, you choose which one these alerts receive. Alerts from entities in `manual` mode stay in **Pending**.

The **Alert default status** section sits below the status table and is collapsed by default.

![Alert default status section collapsed](/assets/operation_center/alerts/alert-default-status-collapsed.png){: style="max-width:100%"}

1. Navigate to **Settings > Custom Statuses**.
2. Expand the **Alert default status** section.
3. In **Default status**, select a status. Only statuses of the **In progress** stage enabled for alerts are proposed.

![Alert default status section expanded](/assets/operation_center/alerts/alert-default-status-expanded.png){: style="max-width:100%"}

The generation mode is set per entity. See [Entities](/xdr/features/collect/entities.md#alert-generation-mode).

## Related articles

* [Custom statuses](/xdr/features/investigate/custom_statuses.md): What custom statuses are, the three stages, and how one status serves both alerts and cases.
* [Migrate custom statuses](/xdr/features/investigate/migrate_custom_statuses.md): How to disable or delete a status that is already in use by reassigning its alerts and cases.
* [Custom verdicts](/xdr/features/investigate/custom_verdicts.md): How to standardize the classification of alert and case outcomes.
* [Custom priorities](/xdr/features/investigate/custom_priorities.md): How case priority levels are configured and ordered.
* [Entities](/xdr/features/collect/entities.md): How to set the alert generation mode of an entity.
