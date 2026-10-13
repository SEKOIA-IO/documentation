# Custom fields

Custom fields add typed, structured metadata specific to your organization to alerts, cases and playbooks. You define each field once for the whole workspace, then use it to filter, group, query and report on these objects.

## Where you can use custom fields

| Object | Where you set values | Automatic addition | In the listing | In SOL |
|---|---|---|---|---|
| Alerts | **Custom fields** section of the alert details page | **Auto-add to new alerts** option | Filter by custom field | `alerts` datasource |
| Cases | **Custom fields** section of the case details page | **Auto-add to new cases** option, or a case template | Filter by custom field | `cases` datasource |
| Playbooks | **Custom fields** section of the **Overview** tab | None, you add fields manually | **Custom fields** column, and grouping by custom field | Not available |

## Supported data types

Custom fields support the following data types:

| Type | Description | Groups the playbooks list |
|---|---|---|
| Text | Free-form text values. | No |
| Single select | One option chosen from a predefined list. | Yes, one group per option |
| Multi select | Multiple options chosen from a predefined list. | No |
| Integer | Numeric values. | No |
| Boolean | True or false values. | Yes, one group for true and one for false |

## Shared definitions

You create a definition once in **Settings > Custom fields**. The same definition is available on alerts, cases and playbooks, so a field such as "Business unit" means the same thing on the alert that raises a signal, the case that resolves it and the playbook that automates the response.

Each definition carries two independent options:

| Option | Effect |
|---|---|
| Auto-add to new alerts | The field appears automatically on every alert created after the option is enabled. |
| Auto-add to new cases | The field appears automatically on every case created after the option is enabled. |

Enabling one option does not enable the other. A field can be auto-added to alerts only, to cases only, to both, or to neither. Playbooks have no auto-add option.

A case template can also carry custom fields. When you apply the template, its fields are added to the case. See [Case templates](/xdr/features/investigate/case_templates.md).

## Change history

Changes to custom field values are tracked on cases and playbooks:

- On a case, every change is recorded in the case history.
- On a playbook, every change creates a new version in the version history of the playbook. See [Restore a playbook version](/xdr/features/automate/restore_a_playbook_version.md).

## Multi-tenancy

In multi-tenant environments, custom field definitions are managed at the parent workspace level. Child tenants use the fields defined by the parent on their alerts, cases and playbooks, but cannot create, edit, or delete field definitions themselves. This approach ensures consistency across your organization while centralizing field management.

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
| Custom fields per playbook | 50 |

## Related articles

* [Manage custom field definitions](/xdr/features/investigate/manage_custom_field_definitions.md): How to create, edit, and delete custom field definitions in your workspace settings.
* [Use custom fields](/xdr/features/investigate/use_custom_fields.md): How to add and edit custom field values on individual alerts and cases.
* [Organize playbooks with custom fields](/xdr/features/automate/organize_playbooks_with_custom_fields.md): How to add custom fields to playbooks and group the playbooks list by custom field.
* [Query custom fields](/xdr/features/investigate/query_custom_fields.md): SOL syntax and examples for filtering, aggregating, and building dashboards from custom field data.
* [Case templates](/xdr/features/investigate/case_templates.md): How case templates add predefined custom fields, tasks and a notebook to a case.
* [Alerts](/xdr/features/investigate/alerts.md): Overview of what alerts are, how they are triaged, and how to filter the alerts listing.
* [Cases](/xdr/features/investigate/cases.md): Overview of what cases are and how they are structured.
* [Case details](/xdr/features/investigate/case_details.md): Reference for every tab and field available on the case details page.
