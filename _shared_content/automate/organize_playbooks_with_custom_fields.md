# Organize playbooks with custom fields

Custom fields let you attach your own metadata to playbooks, such as an owner team, a use case or a criticality level. This article explains how to add custom fields to a playbook and how to group the playbooks list by activation, by community or by custom field.

## Prerequisites

- Custom field definitions exist in **Settings > Custom fields**. Playbooks use the same definitions as alerts and cases. See [Manage custom field definitions](/xdr/features/investigate/manage_custom_field_definitions.md).
- To see the custom fields of a playbook, you need the permission to read custom fields.
- To add or edit custom fields on a playbook, you need the permission to edit playbooks.

!!! tip "Prepare a field for grouping"
    You can group playbooks by a **Single select** field with at least one option, or by a **Boolean** field. Other field types appear on playbooks but cannot be used to group them. For example, create a "Team" single select field with one option per team.

## Add a custom field to a playbook

The **Custom fields** section is in the **Overview** tab of the playbook. Until you add a field, it shows **No custom fields**.

![Empty Custom fields section in the Overview tab of a playbook](/assets/operation_center/playbooks/playbook_custom_fields.png){: style="max-width:100%"}

To add a custom field to a playbook:

1. Navigate to **Playbooks**.
2. Click the name of the playbook.
3. Open the **Overview** tab.
4. In the **Custom fields** section, click **Add**.
5. Select the field.
6. Enter or select the value.

The value is saved immediately, without clicking **Save**, and recorded in the [version history](/xdr/features/automate/restore_a_playbook_version.md) of the playbook.

![Custom fields section with a boolean and a single select value](/assets/operation_center/playbooks/playbook_select_custom_fields.png){: style="max-width:100%"}

## Show custom fields in the playbooks table

The **Custom fields** column is displayed by default in the playbooks table. If you hid it:

1. Navigate to **Playbooks**.
2. Click **Show/Hide table columns**.
3. Select **Custom fields**.

## Group the playbooks list

Grouping is available in the table view of the playbooks list.

To group the playbooks list:

1. Navigate to **Playbooks**.
2. Click **Group by**.
3. Select a grouping option.

![Playbooks table grouped by a single select custom field, with the Group by menu open](/assets/operation_center/playbooks/playbook_group_by_custom_field.png){: style="max-width:100%"}

| Option | Groups |
|---|---|
| **Ungrouped** | One list with every playbook. This is the default. |
| **By activation** | **Activated** and **Deactivated**. Playbooks that are starting, stopping or in error are in **Deactivated**. |
| **By community** | One group per community. Available in multi-tenant parent communities only. A meta-playbook appears in the group of each community it runs in. |
| A custom field | One group per option of a single select field, or one group for true and one for false for a boolean field. Custom fields are listed under **Custom fields** in the menu. |

!!! note "Playbooks without a value"
    When you group by a custom field, playbooks that have no value for this field do not appear in any group. To see every playbook, select **Ungrouped**.

Each group shows the number of playbooks it contains, and the first group is expanded. To expand or collapse a group, click its name. A group loads 100 playbooks at a time: to load the next ones, click **Show X of Y** at the end of the group.

Search, filters and sort apply inside each group. Sekoia.io remembers your grouping choice for the current community in your browser.

## Related articles

* [Navigate playbooks](/xdr/features/automate/navigate_playbooks.md): Reference for the playbooks list and every tab of a playbook.
* [Custom fields](/xdr/features/investigate/custom_fields.md): Overview of custom field types, shared definitions, multi-tenancy behavior and workspace limits.
* [Manage custom field definitions](/xdr/features/investigate/manage_custom_field_definitions.md): How to create, edit and delete custom field definitions in workspace settings.
