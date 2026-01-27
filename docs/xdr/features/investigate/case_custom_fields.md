# Case Custom Fields

Case custom fields enable SOC analysts to classify cases with typed, structured data for better tracking, reporting, and automation. By defining custom fields tailored to your organization's needs, you can capture essential metadata that enhances case management workflows and supports data-driven decision-making.

## Overview

Custom fields extend the standard case properties with additional metadata specific to your organization. They provide a consistent way to capture and query information across all cases, enabling better filtering, reporting, and dashboard creation.

Custom fields support the following data types:

| Type | Description |
|------|-------------|
| Text | Free-form text values |
| Single select | Choose one option from a predefined list |
| Multi select | Choose multiple options from a predefined list |
| Integer | Numeric values |
| Boolean | True/false values |

## Manage custom field definitions

To access custom field management, navigate to **Settings > Custom Fields**.

!!! note
    By default, users with Admin and Analyst roles can manage custom field definitions. Check with your administrator if you need access to this feature.

![Custom Fields Settings](/assets/operation_center/cases/custom_fields_settings.png){: style="max-width:100%"}

### Create a custom field

To create a new custom field definition:

1. Go to **Settings > Custom Fields**
2. Click **+ Add**
3. Enter a **Name** for the field (required)
4. Add an optional **Description** to help users understand the field's purpose
5. Select the **Type** from the dropdown menu
6. Choose a **Color** for visual identification
7. Enable **Auto-add to new cases** if you want this field to appear automatically on all new cases
8. For single select and multi select types, define the available options
9. Click **Save**

!!! tip
    Use descriptive names that clearly indicate what data the field should capture. For example, "Number of impacted users" is clearer than "User count".

### Edit a custom field

To modify an existing custom field definition:

1. Go to **Settings > Custom Fields**
2. Click on the field you want to edit
3. Update the desired properties
4. Click **Save**

!!! note
    The **Type** of a custom field cannot be changed after creation. To use a different type, delete the existing field and create a new one.

### Delete a custom field

To remove a custom field definition:

1. Go to **Settings > Custom Fields**
2. Click on the field you want to delete
3. Click **Delete**
4. Confirm the deletion

!!! warning
    Deleting a custom field definition removes the field and its values from all cases. This action cannot be undone.

## Multi-tenancy

In multi-tenant environments, custom field definitions are managed at the parent workspace level. Child tenants can use the custom fields defined by the parent but cannot create, edit, or delete field definitions themselves.

This approach ensures consistency across your organization while allowing centralized management of field definitions.

## Use custom fields in cases

Custom fields appear in the **Custom Fields** section on the case details page. This section displays all fields that have been added to the case along with their current values.

![Custom Fields in Case Details](/assets/operation_center/cases/custom_fields_case_details.png){: style="max-width:100%"}

### Add a custom field to a case

To add a custom field value to a case:

1. Open the case details page
2. Locate the **Custom Fields** section
3. Click **+ Add** to add a new field
4. Select the field from the dropdown
5. Enter or select the appropriate value
6. Click **Save**

### Edit a custom field value

To update a custom field value:

1. Open the case details page
2. In the **Custom Fields** section, click on the field you want to edit
3. Modify the value
4. Click **Save**

!!! note
    All changes to custom field values are tracked in the case **Updates** tab, providing a complete audit trail of modifications.

## Query custom fields with SOL

Custom fields can be queried using the [Sekoia Operating Language (SOL)](sekoia_operating_language.md) in the [Query Builder](query_builder.md). This enables you to filter cases, create aggregations, and build dashboards based on custom field values.

### Column naming convention

Custom fields are accessible through the `custom_fields` prefix, with the field name converted to snake_case:

- Field name: "Number of impacted users" → Column: `custom_fields.number_of_impacted_users`
- Field name: "Impacted teams" → Column: `custom_fields.impacted_teams`

### Query examples

Filter cases where a numeric custom field has a value:

```
cases
| where custom_fields.number_of_impacted_users > 2
```

Filter cases by a multi-select custom field value:

```
cases
| where custom_fields.impacted_teams in ["HR"]
```

Aggregate cases by a custom field:

```
cases
| aggregate count() by custom_fields.impacted_teams
```

![SOL Query with Custom Fields](/assets/operation_center/cases/custom_fields_sol_query.png){: style="max-width:100%"}

!!! tip
    The query editor provides autocomplete support for custom field columns. Start typing `custom_fields.` to see available fields.

![Custom Fields Autocomplete](/assets/operation_center/cases/custom_fields_autocomplete.png){: style="max-width:100%"}

For creating visualizations based on custom field queries, see the [dashboards documentation](/xdr/features/report/add_widgets_dashboards.md).

## Limits

The following limits apply to custom fields:

| Limit | Value |
|-------|-------|
| Custom field definitions per workspace | 100 |
| Options per single/multi select field | 50 |
| Custom field name length | 50 characters |
| Custom field description length | 100 characters |
| Custom field value length | 50 characters |
| Custom fields per case | 25 |
