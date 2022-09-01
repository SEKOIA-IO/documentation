# Navigate playbooks' interface

## Playbooks listing

In the playbooks’ homepage are listed all playbooks created within your community. These playbooks are listed by order of **last edited** and there are multiple filters made available to navigate this page with ease. 

![playbooks-listing](/assets/operation_center/playbooks/playbook-listing.png){: style="max-width:100%"}

From this page, you can: 

- Create a new playbook
- Search for available playbooks
- Filter available playbooks by status (enabled/disabled)
- Enable and disable playbooks directly from the listing using the toggle button
- Access playbook runs

### Details panel

When clicking on a playbook from the list, a side panel appears with the main details about the playbook.
![details-panel](/assets/operation_center/playbooks/details-panel.png){align=right, style="max-width:50%"}

In this panel, you can: 

- Enable or disable the playbook with the toggle at the top
- Edit playbook using the `edit` button
- Access the `description` of the playbook
- See how many runs have been going as well as their status (`in progress`, `succeeded`, `error`)
- Quickly access last performed runs and filter them by status
- Restart runs

----

## Playbook details

To access the detailed view of a playbook, you have to open the side panel that details the playbook in the listing page then click on the `Edit` button in the upper right side of the panel. 

### Graphical view

The graphical view is composed of three main sections: 

#### Actions library

Accessible in a side panel that appears when clicking on the `+` on the left of the screen, this library provides you with a set of [triggers](https://docs.sekoia.io/xdr/features/automate/triggers/), [actions](https://docs.sekoia.io/xdr/features/automate/actions/) and [operators](https://docs.sekoia.io/xdr/features/automate/operators/) to help automate your workflow. 

These actions are regrouped in apps and services that are interconnected with SEKOIA.IO. 

To find actions in the listing, you can either: 

- Use the search bar inside the panel
- Use filters to list only Actions or Triggers

To add these actions to your graph, click on the dots next to the action name and drag it to the graph area. Dropping actions into this area will form a **block**. 

!!!note 
  Configuration for each of these blocks is detailed in the [Library section](https://docs.sekoia.io/xdr/features/automate/library/aws/) of this documentation. 

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

| Section | Content |
| --- | --- |
| Build | Lists the Module Configuration and the Trigger Configuration as well as Variables and their values |
| Logs | Lists all logs to help understand errors. Details of the error can be accessed by clicking on a log  |

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
| Add form | A form with 3 main items to fill: `key`, `type` and `value` (more details here) |

##### Action

| Section | Content |
| --- | --- |
| Name | The name of your action that can be edited  |
| Module Configuration | Lists existing configuration that may apply to your action. If no configuration is available, you can create a new one by clicking on `Create new configuration` OR edit an existing one  |
| Configuration | Varies depending on the selected action. Contains a search bar as well as all configuration steps. The height of fields in this section can be extended by dragging the mouse on the lower right of the field  |
| Variables | Lists all variables related to the action. Contains name and description of the variable as well as a copy button to easily copy the value of the variable  |

!!! note 
    You can manually resize the configuration panel by clicking on the left edge of the panel and dragging the mouse left or right; the width of the panel  will change accordingly. Once your panel is set at a preferable width, let go of the mouse. The chosen size will be remembered for the next configurations.

  
### Playbook code

The code section is a page where you can write and edit your playbooks using a code editor. Playbooks in [SEKOIA.IO](http://SEKOIA.IO) are written using the language [JINJA 3.](https://jinja.palletsprojects.com/en/3.0.x/templates/) 

It is possible to test your JINJA code on a JSON file:

- Copy/paste the CODE of your playbook
- Remove the nodes with this Python script:

```
import json
from jinja2 import Template

file_json = open("file.json", "r")
loading = json.load(file_json)

# The JINJA partern to be tested
jinja_patern = "{{urgency.value}}"

tm = Template(jinja_patern)

msg = tm.render(urgency=loading["urgency"])
print(msg)

```

### Playbook details 

The tab `Details` lists all information related to the playbook. 

- The community where the playbook was created
- The user who created the playbook
- The user who last updated the playbook
- Date of creation
- Date of last update
- Name of the last user who activated the playbook
- Date of the last activation of the playbook
- Description of the playbook

!!! tip
    You can edit the name and the description of the playbook by clicking on the `Edit` button next to the activation toggle.
  
---

## Playbook runs
The tab `Playbook runs` lists all runs that happened in the **last week**.

The header points at the total number of playbook runs in the last week, the ones in progress, have succeeded and have failed. 

Under these stats lays a table with the following information:

- The event (the run)
- When it started
- Its status
- The duration of the run
- A RErun button to restart the run

To access the details of a run, just click on the run and you’ll be redirected to the graph view with the status of each block. 

From the graph view, click on the block of interest and the panel `Run results` will show. 

### Run results

Run results are accessible either from the tab `Runs` in the playbook or in the panel that details a [playbook's details](#details-panel). 

This panel contains the following information:

- The status of the run
- Its timeline (when it started, how long the run lasted, when it ended)
- Arguments
- Results (logs and errors)

To switch to the block’s settings, click on the `edit` button on the top right of the panel. 

To switch back to run results, click on the button `Switch to run results` button.
