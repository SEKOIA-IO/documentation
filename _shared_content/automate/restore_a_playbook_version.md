# Restore a playbook version

Sekoia.io keeps a history of the versions of each playbook, so you can see who changed what and roll back a change that broke your automation. This article explains how to open the version history of a playbook, preview and compare a version, and restore it.

A new version is saved when the playbook is created, then each time you save a change to its name, description, workflow or custom fields. Activating or deactivating a playbook does not create a version.

!!! note "Retention"
    Sekoia.io keeps the last 30 versions of each playbook and deletes older versions automatically. Version history covers playbooks saved at least once since August 1, 2026.

## Prerequisites

- To view the version history, you need the permission to read playbooks.
- To restore a version, you need the permission to edit playbooks.

## Open the version history

To open the version history of a playbook:

1. Navigate to **Playbooks**.
2. Click the name of the playbook.
3. In the playbook header, click the **...** menu.
4. Select **Version history**.

The **Version history** panel lists the **Current version** and the **Saved versions**, each with its date, time and author.

## Preview a version

To see the workflow of a saved version:

1. Open the **Version history** panel.
2. Click a version.

The **Version preview** window shows the workflow of that version in read-only mode, with its save date. To see the configuration of a node, click the node.

![Version history panel and Version preview window of a playbook](/assets/operation_center/playbooks/playbook_version_history.png){: style="max-width:100%"}

## Compare a version with the current one

The **Code** tab shows the JSON of the selected version next to the JSON of the current version, with the differences highlighted.

To compare a version with the current one:

1. Open the **Code** tab of the playbook.
2. Open the **Version history** panel.
3. Click a version.

To display the selected version alone, turn off the **diff** toggle.

## Restore a version

!!! warning "Restoring applies immediately"
    Sekoia.io does not ask for confirmation. If the playbook is activated, its next runs use the restored workflow.

To restore a version:

1. Open the **Version history** panel.
2. Click the version you want to restore.
3. In the **Version preview** window, click **Restore this version**.

The restored workflow replaces the current one and is saved as a new version. The version you replaced stays in the history, so you can restore it later. Restoring a version does not change the name, the description or the custom fields of the playbook.

## Related articles

* [Navigate playbooks](/xdr/features/automate/navigate_playbooks.md): Reference for the playbooks list and every tab of a playbook.
* [Build playbooks](/xdr/features/automate/build_playbooks.md): How to create a playbook from a template or from scratch.
* [Debug playbooks](/xdr/features/automate/debug-playbooks.md): How to investigate failed runs and trigger errors.
