# Custom fields

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

Custom fields extend the standard alert and case properties with typed, structured metadata specific to your organization. They provide a consistent way to capture and query information across all alerts and cases, enabling better filtering, reporting, and dashboard creation.

## Supported data types

Custom fields support the following data types:

| Type | Description |
|---|---|
| Text | Free-form text values. |
| Single select | One option chosen from a predefined list. |
| Multi select | Multiple options chosen from a predefined list. |
| Integer | Numeric values. |
| Boolean | True or false values. |

## Shared definitions

Alerts and cases share the same custom field definitions. You create a definition once in **Settings > Custom fields**, then attach it to alerts, to cases, or to both. This keeps the vocabulary of your organization consistent across the whole investigation workflow, from the alert that raises a signal to the case that resolves it.

Each definition carries two independent options:

| Option | Effect |
|---|---|
| Auto-add to new alerts | The field appears automatically on every alert created after the option is enabled. |
| Auto-add to new cases | The field appears automatically on every case created after the option is enabled. |

Enabling one option does not enable the other. A field can be auto-added to alerts only, to cases only, to both, or to neither.

## How custom fields appear

Custom fields appear in the **Custom fields** section of the alert details page and the case details page. This section displays all fields added to the alert or the case along with their current values. Fields configured with **Auto-add to new alerts** or **Auto-add to new cases** appear without any manual action, and you only need to fill in their values.

All changes to custom field values on a case are recorded in the case history, providing a complete audit trail of modifications.

## Multi-tenancy

In multi-tenant environments, custom field definitions are managed at the parent workspace level. Child tenants can use the fields defined by the parent but cannot create, edit, or delete field definitions themselves. This approach ensures consistency across your organization while centralizing field management.

## Limits

The following limits apply to custom fields:

| Limit | Value |
|---|---|
| Custom field definitions per workspace | 100 |
| Options per single select or multi select field | 50 |
| Custom field name length | 50 characters |
| Custom field description length | 100 characters |
| Custom field value length | 50 characters |
| Custom fields per alert or per case | 25 |

## Related articles

* [Manage custom field definitions](/xdr/features/investigate/manage_custom_field_definitions.md): How to create, edit, and delete custom field definitions in your workspace settings.
* [Use custom fields](/xdr/features/investigate/use_custom_fields.md): How to add and edit custom field values on individual alerts and cases.
* [Query custom fields](/xdr/features/investigate/query_custom_fields.md): SOL syntax and examples for filtering, aggregating, and building dashboards from custom field data.
* [Alerts](/xdr/features/investigate/alerts.md): Overview of what alerts are, how they are triaged, and how to filter the alerts listing.
* [Cases](/xdr/features/investigate/cases.md): Overview of what cases are and how they are structured.
* [Case details](/xdr/features/investigate/case_details.md): Reference for every tab and field available on the case details page.
