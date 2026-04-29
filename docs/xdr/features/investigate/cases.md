# Cases

Cases let you group investigation findings across multiple perimeters, alerts, and analysts, and share results with your end-users in a structured and traceable way. You can create a case from an existing alert or add alerts to a case at any point during your investigation.

## Cases listing

The listing page displays all cases across your community. You can filter cases by:

* Asset
* Assignee
* Creator
* Custom fields
* Priority
* Status
* Tag
* Verdict

You can sort cases by:

* Last edition (default)
* Creation date
* By highest priority

![Case listing with filter](/assets/operation_center/cases/cases-filter.png){: style="max-width:100%"}

## Create a case

To create a new case:

1. Navigate to the **Cases** page.
2. Click **+ Case**.
3. Enter a **Title** and a **Description** (both fields are mandatory).
4. Select an **Assignee**.
5. Set a **Priority**.
6. Add **Tags** if needed.
7. Click **Create**.

## Bulk actions on cases

Sekoia.io lets you perform actions on multiple cases simultaneously from the cases listing page. This is useful for triaging large volumes of cases or reassigning incidents at scale.

### Select multiple cases

You can build a selection using three methods:

1. **Individual selection**: Click the checkbox on the left side of each case row.
2. **Page selection**: Click the checkbox in the table header to select all cases visible on the current page (up to 25, 50, or 100 cases).
3. **Global selection**: After activating page selection, a banner appears at the top of the list. Use it to extend your selection to all cases matching your active filters, up to the platform limit.

![Case listing with bulk actions](/assets/operation_center/cases/cases-bulk-actions.png){: style="max-width:100%"}

### Selection limits

!!! note "Selection limit"
    Mass selections are capped at 5,000 cases at a time to maintain platform performance. If your filtered results exceed 5,000 cases, a tooltip informs you: "Selections are limited to 5,000 cases at a time for performance reasons. You can select the remaining cases afterward." Use the **Clear selection** button in the action banner to deselect all cases and reset the view.

### Available bulk actions

Once you select at least one case, the bulk action toolbar appears at the top of the list. The **Filters** tool bar is temporarily replaced during an active selection.

| Action | Description |
|---|---|
| Change priority | Update the priority (e.g., High, Medium, Low) for all selected cases. |
| Change status | Update the status (e.g., New, In progress, Closed) for all selected cases. |
| Change verdict | Update the verdict (e.g., True positive: Confirmed attack, False positive: Detection error) for all selected cases. |
| Change assignee | Reassign all selected cases to a specific user. |

## Case custom statuses and verdicts

Cases support the same custom status and verdict system as alerts, enabling consistent terminology and workflows across your SOC.

### Custom statuses for cases

Custom statuses let you define case lifecycle stages that match your organization's investigation processes. Each status belongs to one of three stages:

* **Open**: Cases that are active and require attention.
* **In progress**: Cases under active investigation.
* **Closed**: Cases that have been resolved or dismissed.

You can configure custom statuses to apply exclusively to cases, exclusively to alerts, or to both. Enabling a status for both contexts ensures consistent terminology across your investigation workflows.

!!! note "Status history"
    Case history preserves the original status name even if a custom status is modified later. Historical records always reflect the status names that were in use at the time of each change.

### Custom verdicts for cases

Custom verdicts provide standardized classification of case outcomes. Each verdict belongs to either the **True Positive** or **False Positive** category, allowing your team to document investigation conclusions with organization-specific terminology.

Like custom statuses, you can enable verdicts for cases, alerts, or both.

## Edit a case

To edit a case, click on the case to open the details view, then click **Edit**.

!!! warning "Editing restriction"
    You can only edit cases with a status in the **Open** or **In progress** stage. Cases with a **Closed** status cannot be edited.

## Case details

The case details page is organized into a header and five tabs.

The header displays the case name, creator, last edition date, case ID (click to copy), priority, and status.

The five tabs are: **Details**, **Alerts**, **Tasks**, **Events**, and **Graph Investigation**.

### Details tab

The **Details** tab contains:

* Authors, community, and creation and edition dates.
* A Markdown-enabled description field.
* A timeline of comments.

### Alerts tab

The **Alerts** tab lists all alerts added to the case.

To add alerts to the case, you can:

* Click **Add alerts** from this tab.
* Click **Add to case** from the detailed page of any alert.

!!! tip "Adding multiple alerts to a case"
    Copy the case ID from the case details page and paste it into the search bar on the alerts page. Select the case from the results, then click **Add to alerts**.

!!! tip "Adding an alert to multiple cases"
    Copy the alert ID from the alert details page and paste it into the search bar. Select the alert from the results, or scroll and select all the alerts you need, then click **Add to case**.

### Tasks tab

The **Tasks** tab lets you create and manage tasks and subtasks associated with the case.

### Events tab

The **Events** tab lists all events associated with the case, using the same display as the [Events page](xdr/features/investigate/events.md).

![Events tab inside a case](/assets/operation_center/cases/case-events-tab.png){: style="max-width:100%"}

Events appear in this tab when they:

* Raised an alert that was added to the case.
* Were [directly added to the case](../events/#adding-events-to-cases).

When you interact with individual values in the event list, you can:

* **Filter for**: restricts the view to events matching that value within the case.
* **Filter out**: excludes events matching that value within the case.
* **Search events with this value**: runs a broader search (see below).

To work with multiple values at once, click **Toggle value selection** at the top of the event list. You can then select multiple values and use them to:

* Create a Sigma rule.
* Search events with these values.

#### Search events with this value

This feature searches all events that occurred within the case's timeframe (plus or minus one hour). The search query is built automatically from your selected values.

To search events with a value:

1. Navigate to the **Events** tab of the case.
2. Click **Toggle value selection** at the top of the event list.
3. Select the values you want to search for by clicking them in the list.
4. Click **Perform a search**.

A side panel opens with the search results so you can investigate without leaving the case page.

![Search events in side panel](/assets/operation_center/cases/case-side-panel.png){: style="max-width:100%"}

### Graph investigation tab

The **Graph Investigation** tab provides an interactive visualization of the case's alerts and events, enabling threat analysis through visual correlation of security data and intelligence.

!!! note "Automatic saving"
    All changes in the graph are saved automatically. The graph updates dynamically on each visit as new events are associated with the case. New objects discovered through additional events are integrated into the existing graph structure automatically.

The graph displays the following elements:

* **Observables**: Security artifacts extracted from events, including IP addresses, domains, URLs, user accounts, file hashes, and other indicators of compromise.
* **Observable relationships**: Directional connections between observables, extracted from events using Smart Description definitions.
* **CTI objects**: STIX-compliant threat intelligence objects from the intelligence database that provide contextual threat information.
* **STIX relationships**: Standardized connections between intelligence objects that reveal broader threat context.

**Threat intelligence panel**

Click any CTI object in the graph to open a detail panel displaying:

* Object descriptions and threat context.
* Relationship mappings with other intelligence objects.
* Options to expand the graph by adding related objects.

**Observable analysis panel**

Click any observable node to open a detail panel displaying:

* All events within the case that contain the selected observable, with Smart Description summaries.
* Access to full event details via the **Full Events** button.
* A direct link to search for additional events containing the same value across your environment.

#### Layers

Layers organize complex graphs into logical groupings that you can display or hide independently. This lets you focus on a specific aspect of the investigation without losing the complete picture.

**Default layer**

Every graph automatically creates a default layer on first access. This layer serves as the primary container for initial graph elements and automatically incorporates new objects as additional events are processed.

**Layer controls**

The layer control panel is located at the top of the graph. It provides:

* Access to the full layer management interface.
* An indicator of the currently active layer, where new additions are placed.
* Controls to switch between layers instantly.

##### Create and manage layers

To create a new layer:

1. Click the name of the default layer at the top of the graph (for example, **Event Layer #1**).
2. Click **+** to add a new layer.
3. Enter a name for the layer.
4. Drag and drop objects or observables into the layer.

All changes are saved automatically.

To focus on a specific layer, click the **Eye** icon next to the layer name to toggle its visibility. This reduces visual clutter and isolates data for deeper analysis.

##### Layer organization strategies

Use layers to structure complex, multi-alert cases:

* **Alert-based organization**: Create one layer per alert to focus analysis on individual attack phases.
* **Temporal analysis**: Organize layers by time period to track attack progression across a campaign.
* **Attack vector segregation**: Separate layers by technique, entry point, or affected system.
* **Threat actor attribution**: Create distinct layers when multiple threat actors or campaigns are suspected.

You can rename layers at any time, move objects between layers, and use the built-in search to locate specific objects within large multi-layered graphs.

## Related articles

* [Alerts](/xdr/features/investigate/alerts): Understand how alerts are created and how to manage them before grouping them into cases.
* [AI Cases](/xdr/features/investigate/ai_cases.md): Learn how Sekoia.io automatically correlates alerts into cases using AI.
* [Events](/xdr/features/investigate/events.md): Explore the events associated with your cases and run contextual searches.
* [Playbooks](/xdr/features/automate.md): Automate case workflows and trigger actions based on case updates.
* [Dashboards](/xdr/features/report/dashboards.md): Monitor case activity and investigation KPIs across your community.
