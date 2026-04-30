# Use custom fields in cases

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

Custom fields let you attach structured metadata to individual cases. This article explains how to add custom field values to a case and how to update them during an investigation.

## Prerequisites

Custom field definitions must exist in your workspace before you can use them on cases. If no fields are available, ask your administrator to create definitions in **Settings > Custom fields**.

## Add a custom field to a case

> 📸 [SCREENSHOT SUGGESTION: Case details page with the Custom Fields section expanded, showing an empty field and the + Add button. | ALT TEXT: Custom fields section on the case details page.]

To add a custom field value to a case:

1. Open the case details page.
2. Locate the **Custom fields** section.
3. Click **+ Add**.
4. Select the field from the dropdown.
5. Enter or select the appropriate value.
6. Click **Save**.

!!! note "Auto-added fields"
    Fields configured with **Auto-add to new cases** appear automatically on every new case. You only need to fill in their values.

## Edit a custom field value

To update an existing custom field value on a case:

1. Open the case details page.
2. In the **Custom fields** section, click the field you want to edit.
3. Modify the value.
4. Click **Save**.

All changes to custom field values are recorded in the case history, providing a complete audit trail of modifications.

## Related articles

* [Case custom fields](/xdr/features/investigate/case_custom_fields.md): Overview of custom field types, multi-tenancy behavior, and workspace limits.
* [Manage custom field definitions](/xdr/features/investigate/manage_custom_field_definitions.md): How to create, edit, and delete custom field definitions in workspace settings.
* [Query custom fields](/xdr/features/investigate/query_custom_fields.md): SOL syntax and examples for filtering and aggregating cases by custom field values.
* [Case details](/xdr/features/investigate/case_details.md): Reference for every tab and field available on the case details page.
* [Manage cases](/xdr/features/investigate/manage_cases.md): How to filter cases by custom field values from the cases listing page.
