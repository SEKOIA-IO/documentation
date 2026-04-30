# Manage custom field definitions

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

Custom field definitions determine which structured metadata fields are available across all cases in your workspace. This article explains how to create, edit, and delete those definitions from the workspace settings.

## Prerequisites

By default, users with the **Admin** or **Analyst** role can manage custom field definitions. Contact your administrator if you need access to this section.

## Access custom field settings

To open the custom field management page, navigate to **Settings > Custom fields**.

> 📸 [SCREENSHOT SUGGESTION: Settings > Custom Fields page showing the list of existing field definitions with the + Add button visible. | ALT TEXT: Custom fields settings page.]

## Create a custom field

!!! tip "Naming custom fields"
    Use descriptive names that clearly indicate what data the field should capture. For example, "Number of impacted users" is clearer than "User count".

To create a new custom field definition:

1. Navigate to **Settings > Custom fields**.
2. Click **+ Add**.
3. Enter a **Name** for the field.
4. Enter an optional **Description** to help users understand the field's purpose.
5. Select a **Type** from the dropdown menu.
6. Choose a **Color** for visual identification.
7. Enable **Auto-add to new cases** if you want this field to appear automatically on all new cases.
8. For **Single select** and **Multi select** types, define the available options.
9. Click **Save**.

## Edit a custom field

!!! note "Type cannot be changed"
    The **Type** of a custom field cannot be changed after creation. To use a different type, delete the existing field and create a new one.

To modify an existing custom field definition:

1. Navigate to **Settings > Custom fields**.
2. Click the field you want to edit.
3. Update the desired properties.
4. Click **Save**.

## Delete a custom field

!!! warning "Permanent data loss"
    Deleting a custom field definition removes the field and all its values from every case in your workspace. This action cannot be undone.

To remove a custom field definition:

1. Navigate to **Settings > Custom fields**.
2. Click the field you want to delete.
3. Click **Delete**.
4. Confirm the deletion.

## Related articles

* [Case custom fields](/xdr/features/investigate/case_custom_fields.md): Overview of custom field types, multi-tenancy behavior, and workspace limits.
* [Use custom fields in cases](/xdr/features/investigate/use_custom_fields_in_cases.md): How to add and edit custom field values on individual cases.
* [Query custom fields](/xdr/features/investigate/query_custom_fields.md): SOL syntax and examples for filtering and aggregating cases by custom field values.
* [Case details](/xdr/features/investigate/case_details.md): Reference for every tab and field available on the case details page.
