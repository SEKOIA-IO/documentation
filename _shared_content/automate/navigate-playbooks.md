# Navigate playbooks' interface

## Playbooks list

The **Playbooks** page lists every playbook of your community in a table, sorted by last update. From this page, you can create playbooks, manage the accounts they use and follow their runs.

![Playbooks list in table view](/assets/operation_center/playbooks/playbook-listing.png){: style="max-width:100%"}

The page header gives access to the following buttons:

| Button | Action |
| --- | --- |
| **Local runners** | Manage the runners that execute playbook actions in your own infrastructure. See [Playbooks On-premises](/xdr/features/automate/playbooks-on-premises.md). |
| **Connected accounts** | Manage the accounts that playbooks use to connect to third-party services. See [Manage accounts](/xdr/features/automate/manage-accounts.md). |
| **New playbook** | Create a playbook. See [Build playbooks](/xdr/features/automate/build-playbooks.md). |

The **Playbooks** tab lists the playbooks. The **Runs** tab lists the runs of all playbooks.

### Table columns

| Column | Content |
| --- | --- |
| **Name** | Name of the playbook. Click it to open the playbook. |
| **Status** | Status badges of the playbook: `Ready to start`, `Configuration issues`, `Partially activated`, `Failed runs` and `Trigger crashed`. Click a badge to open the matching tab of the playbook. |
| **Runs**, **In progress**, **Succeeded**, **Failed** | Run counters of the playbook. |
| **Custom fields** | Custom field values of the playbook. See [Organize playbooks with custom fields](/xdr/features/automate/organize_playbooks_with_custom_fields.md). |
| **Communities** | Communities where the playbook runs. |
| **Author** | User who created the playbook. |
| **Updated at** | Date of the last change to the playbook. |
| **Activated** | Toggle to activate or deactivate the playbook. |
| **Actions** | The **...** menu, with **Duplicate playbook** and **Delete**. |

The **Name** and **Status** columns are always displayed, and the **Actions** column is always the last one. To choose and reorder the other columns, click **Show/Hide table columns**, then select the columns and drag them into the order you want. Sekoia.io saves your selection for the current community in your browser.

### Search, filter and sort

- To find a playbook by name, use the search bar.
- To filter the list, click **Filters** and select **Activation**, **Integrations used**, **Trigger** or **Updated at**. Active filters are kept in the URL, so you can bookmark or share a filtered view.
- To sort the list, click the **Name**, **Activated** or **Updated at** column header.

### Group playbooks

To group the table by activation, by community or by custom field, click **Group by**. See [Organize playbooks with custom fields](/xdr/features/automate/organize_playbooks_with_custom_fields.md).

### Activate, duplicate or delete a playbook

These actions require the permission to edit playbooks.

!!! warning "Deactivating a playbook"
    Deactivating a playbook stops it in all its communities and ends its runs in progress.

- To activate or deactivate a playbook, click the toggle in the **Activated** column.
- To duplicate a playbook, click **...** at the end of its row, then select **Duplicate playbook**.
- To delete a playbook, deactivate it first, then click **...** at the end of its row and select **Delete**.

### Card view

The playbooks list is also available as cards. To switch between the two views, click **Card view** or **Table view** next to the search bar. Sekoia.io remembers your choice in your browser. **Group by** and **Show/Hide table columns** are available in the table view only.

## Playbook details

To open a playbook, click its name in the playbooks list. Once on the playbook page, you should now see some ‘warning’ icons on tabs and inside configuration panel. These icons are here to guide you when there are some issues to resolve before the playbook can be activated.

You can also now save your playbook from any tab, the save button is now in the header part of the playbook

Some badges have been added to have a status about the playbook:

- Configuration issues: some/all communities have some configuration issues detected. By clicking on it you’ll be redirected to the Workflow tab with the issue panel opened
- Partially activated : some communities are running but not all of them. By clicking on it you’ll be redirected to the overview tab
- Ready to start: there are no configuration issues on any community, playbook can be activated
- Failed runs: some runs have failed. By clicking on it you’ll be redirected to the runs tab with a “failed” filter set
- Trigger crashed: there is a log with criticy level "critical” inside the “Trigger logs” tab. By clicking on it you’ll be redirected to the Trigger logs tab with a “critical” filter set

![playbooks-editing](/assets/operation_center/playbooks/playbook-editing.png){: style="max-width:100%"}

### Overview

This tab `Overview` lists all information related to the playbook:

- The community where the playbook was created
- The user who created the playbook
- The user who last updated the playbook
- Date of creation
- Date of last update
- Name of the last user who activated the playbook
- Date of the last activation of the playbook
- Description of the playbook
- Community details, including the ability to add or remove communities, activate or deactivate communities for a given playbook, and review playbook statuses by community (e.g. configuration issues, failed rules or crashed triggers)
- Custom fields of the playbook. See [Organize playbooks with custom fields](/xdr/features/automate/organize_playbooks_with_custom_fields.md)

![Overview tab of a playbook](/assets/operation_center/playbooks/playbook_custom_fields.png){: style="max-width:100%"}

### Workflow

The workflow view is composed of three main sections:

#### Module menu

The module menu gives access to the [triggers](/xdr/features/automate/triggers.md), [actions](/xdr/features/automate/actions.md) and [operators](/xdr/features/automate/operators.md) you can add to your workflow. It is a bar of buttons on the graph area: **Triggers**, **Actions**, **Integrations** and **Operators**. Click a button to open its panel, and click it again to close the panel.

| Panel | Content |
| --- | --- |
| **Triggers** | A search bar, the **Built-in** triggers such as Cron, then the triggers grouped by integration. |
| **Actions** | A search bar, then the actions grouped by integration, with the number of actions of each integration. |
| **Integrations** | The list of integrations connected to Sekoia.io. Click an integration to see its triggers and actions. |
| **Operators** | The Condition, Foreach, Store, All and Any operators. |

To add a module to your workflow, click it or drag it to the graph area. The module becomes a **block**.

To insert a block between two blocks, click the **+** on the link that connects them, then select **Add an action** or **Add an operator**. The matching panel opens.

![Module menu with the Actions panel open on an empty playbook](/assets/operation_center/playbooks/playbook_module_menu.png){: style="max-width:100%"}

!!! note
    Configuration for each of these blocks is detailed in the [Library section](/xdr/features/automate/library/aws.md) of this documentation.

#### Graph area

This is where you can add and connect your blocks to form a playbook.

Playbook blocks are visually composed of:

- The logo of the app/service
- The name of the action
- The type of block (Action, Operator, Trigger)
- The status of the block (Valid, In error)
- Connectors

| Actions | Description |
| --- | --- |
| Zoom in/out | Either using the mouse or the action buttons |
| Fit Diagram | Lets you see all your blocks |
| Undo | Undo last action |
| Redo | Redo action |

!!! note
    If blocks in the playbook have missing configuration, an alert stating the number of errors will show in the left of the graph area.

The playbook run view adds color to the playbook blocks and nodes to highlight the status of the run.

| Color | Meaning |
| --- | --- |
| Green | Playbook run went successfully |
| Orange | Playbook run left from this node |
| Red | Run ended in error |


#### Configuration panel

When clicking on a block in the graph area, the configuration panel opens on the right of the screen.

Depending on the type of blocks, the content of the configuration panel changes.

##### Triggers

You can edit the trigger name directly in the header part.

![playbooks-trigger-name](/assets/operation_center/playbooks/playbook-trigger-name.png){: style="max-width:100%"}

| Tabs | Content |
| --- | --- |
| Account | Lists the Module Configuration (possibility to create/edit/delete) - For MSSP : you’ll see one account by community |
| Configuration | Lists the available Trigger Configurations, you can add/edit/delete |
| Variables | Variables and their values  |

For MSSP, there is a section for each community added into playbook on the Account and Configuration parts for Triggers.

![playbooks-account-mssp](/assets/operation_center/playbooks/playbooks-account-mssp.png){: style="max-width:100%"}

You can also add a new community with “+ Community” button and choose between your remaining communities.

![playbooks-account-community](/assets/operation_center/playbooks/playbooks-account-community.png){: style="max-width:100%"}

Community selection is made by clicking on it.
To delete a community from a playbook, a “…” button can be found on community section header. By clicking on it, it will show a “Delete community” option.

![playbooks-account-delete](/assets/operation_center/playbooks/playbooks-account-delete.png){: style="max-width:100%"}

##### Operator

**Condition**

| Section | Content |
| --- | --- |
| Name | The name of your operator that can be edited  |
| Cases  | List of comparisons to be made (Either with a variable or by adding a form) |

**Foreach**

| Section | Content |
| --- | --- |
| Name | The name of your operator that can be edited  |
| Items | List of data that should be browsed  |
| Variables | Lists all variables related to the action. Contains name and description of the variable as well as a copy button to easily copy the value of the variable  |

**Store**

| Section | Content |
| --- | --- |
| Name | The name of your operator that can be edited  |
| Modifications | List of modifications to make. To add a modification, hover over the title and click on one of the buttons that appear (`Use variable`, `add one entry to array`) |
| Use a variable | Field where you can paste the value of a variable |
| Add form | A form with 3 main items to fill: `key`, `type` and `value` (more details [here](https://docs.sekoia.com/tip/features/automate/operators/#store)) |

##### Action

You can edit the action name directly in the header part.

![playbooks-action-name](/assets/operation_center/playbooks/playbooks-action-name.png){: style="max-width:100%"}

| Tabs | Content |
| --- | --- |
| Account | Lists existing configuration that may apply to your action. If no configuration is available, you can create a new one by clicking `on Create new configuration` OR edit an existing one - For MSSP : you’ll see one account by community |
| Configuration | Varies depending on the selected action. Contains a search bar as well as all configuration steps. The height of fields in this section can be extended by dragging the mouse on the lower right of the field |
| Variables | Lists all variables related to the action. Contains name and description of the variable as well as a copy button to easily copy the value of the variable  |

!!! note
    You can manually resize the configuration panel by clicking on the left edge of the panel and dragging the mouse left or right; the width of the panel  will change accordingly. Once your panel is set at a preferable width, let go of the mouse. The chosen size will be remembered for the next configurations.

For MSSP, there is a section for each community added into playbook on the Account tab.

![playbooks-action-mssp](/assets/operation_center/playbooks/playbooks-action-mssp.png){: style="max-width:100%"}

Please see above “Triggers” part to see how to add or delete a community from a playbook

#### Issue panel

The issue panel has been enhanced to give details about the configuration issues in playbook for each community (in a MSSP context). When clicking on the “Go to issues” button, you’ll redirected directly on the right module and tab (Account/Configuration) to resolve the issue.

![playbooks-issue-panel](/assets/operation_center/playbooks/playbooks-issue-panel.png){: style="max-width:100%"}

### Code

The code section is where you can find your playbook in JSON. You may use [JINJA 3.](https://jinja.palletsprojects.com/en/3.0.x/templates/) to fill variable fields.

From this tab, you can also compare the JSON of a previous version with the current one. See [Restore a playbook version](/xdr/features/automate/restore_a_playbook_version.md#compare-a-version-with-the-current-one).

It is possible to test your JINJA code on a JSON file:

- Copy/paste the code of your playbook
- Remove the nodes with this Python script:

```
import json
from jinja2 import Template

file_json = open("file.json", "r")
loading = json.load(file_json)

# The JINJA pattern to be tested
jinja_pattern = "{{urgency.value}}"

tm = Template(jinja_pattern)

msg = tm.render(urgency=loading["urgency"])
print(msg)

```

### Runs
The tab `Playbook runs` lists all runs that happened in the **last week**.

The header points at the total number of playbook runs in the last week, the ones in progress, have succeeded and have failed.

Under these stats lays a table with the following information:

- The event (the run)
- When it started
- Its status
- The duration of the run
- A rerun button to restart the run

To access the details of a run, just click on the run and you’ll be redirected to the graph view with the status of each block.

From the graph view, click on the block of interest and the panel `Run results` will show.

This tab includes filters for sorting by Status. Additionally, 'Meta-Playbooks' allows for filtering based on specific Communities.

#### Run results

Run results are accessible either from the tab `Runs` in the playbook or in the panel that details a [playbook's details](#playbook-details).

This panel contains the following information:

- The status of the run
- Its timeline (when it started, how long the run lasted, when it ended)
- Arguments
- Results (logs and errors)

To switch to the block’s settings, click on the `edit` button on the top right of the panel.

To switch back to run results, click on the button `Switch to run results` button.

### Trigger logs

This tab allows user to see all logs from a trigger configuration. It is usefull to quickly see configuration errors and to know why playbook is not working properly.

This tab includes filters for sorting by Level (e.g. Critical, Debug, Info, etc.). Additionally, 'Meta-Playbooks' allows for filtering based on specific Communities.

### Version history

The **...** menu of the playbook header gives access to **Version history**. This panel lists the last 30 saved versions of the playbook, with their date and author. You can preview a version, compare it with the current one and restore it. See [Restore a playbook version](/xdr/features/automate/restore_a_playbook_version.md).

## Related articles

* [Build playbooks](/xdr/features/automate/build-playbooks.md): How to create a playbook from a template or from scratch.
* [Organize playbooks with custom fields](/xdr/features/automate/organize_playbooks_with_custom_fields.md): How to add custom fields to playbooks and group the playbooks list.
* [Restore a playbook version](/xdr/features/automate/restore_a_playbook_version.md): How to preview, compare and restore a previous version of a playbook.
* [Debug playbooks](/xdr/features/automate/debug-playbooks.md): How to investigate failed runs and trigger errors.

