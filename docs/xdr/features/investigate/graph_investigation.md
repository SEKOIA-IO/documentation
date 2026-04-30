# Graph investigation

The graph investigation tab provides an interactive visualization of a case's alerts and events. It enables threat analysis through visual correlation of security data and intelligence objects. This article describes the elements displayed in the graph and explains how to work with layers.

## Graph elements

The graph displays four types of elements:

| Element | Description |
|---|---|
| Observables | Security artifacts extracted from events, including IP addresses, domains, URLs, user accounts, file hashes, and other indicators of compromise. |
| Observable relationships | Directional connections between observables, extracted from events using Smart Description definitions. |
| CTI objects | STIX-compliant threat intelligence objects from the intelligence database that provide contextual threat information. |
| STIX relationships | Standardized connections between intelligence objects that reveal broader threat context. |

!!! note "Automatic saving"
    All changes in the graph are saved automatically. The graph updates dynamically on each visit as new events are associated with the case. New objects discovered through additional events are integrated into the existing graph structure automatically.

## Observable and CTI object panels

Click any node in the graph to open a detail panel on the right. The content of the panel depends on the type of node selected.

### Threat intelligence panel

Clicking a CTI object opens a panel that displays:

* Object descriptions and threat context.
* Relationship mappings with other intelligence objects.
* Options to expand the graph by adding related objects.

> 📸 [SCREENSHOT SUGGESTION: Graph investigation tab with a CTI object selected and the threat intelligence detail panel open on the right. | ALT TEXT: Threat intelligence detail panel in the graph investigation tab.]

### Observable analysis panel

Clicking an observable node opens a panel that displays:

* All events within the case that contain the selected observable, with Smart Description summaries.
* Access to full event details via the **Full events** button.
* A direct link to search for additional events containing the same value across your environment.

> 📸 [SCREENSHOT SUGGESTION: Graph investigation tab with an observable node selected and the observable analysis panel open showing related events. | ALT TEXT: Observable analysis panel in the graph investigation tab.]

## Work with layers

Layers organize complex graphs into logical groupings that you can display or hide independently. This lets you focus on a specific aspect of the investigation without losing the complete picture.

> 📸 [SCREENSHOT SUGGESTION: Graph investigation tab showing multiple named layers in the layer control panel at the top of the graph, with one layer hidden. | ALT TEXT: Layer control panel in the graph investigation tab.]

### Default layer

Every graph automatically creates a default layer on first access. This layer serves as the primary container for initial graph elements and automatically incorporates new objects as additional events are processed.

### Layer controls

The layer control panel is located at the top of the graph. It provides:

* Access to the full layer management interface.
* An indicator of the currently active layer, where new additions are placed.
* Controls to switch between layers.

### Create a layer

To create a new layer:

1. Click the name of the active layer at the top of the graph (for example, **Event Layer #1**).
2. Click **+** to add a new layer.
3. Enter a name for the layer.
4. Drag and drop objects or observables into the layer.

All changes are saved automatically.

### Show or hide a layer

To toggle the visibility of a layer, click the **Eye** icon next to the layer name. Hiding a layer reduces visual clutter and isolates data for deeper analysis without removing any information from the graph.

### Rename and reorganize layers

You can update layers at any time to keep your graph organized:

* To rename a layer, click the layer name and enter a new value.
* To move an object to a different layer, drag it from its current layer and drop it onto the target layer.
* To locate a specific object across large multi-layered graphs, use the built-in search.

## Layer organization strategies

Layers are especially useful for complex, multi-alert cases. The following strategies can help you structure your investigation:

| Strategy | Description |
|---|---|
| Alert-based organization | Create one layer per alert to focus analysis on individual attack phases. |
| Temporal analysis | Organize layers by time period to track attack progression across a campaign. |
| Attack vector segregation | Separate layers by technique, entry point, or affected system. |
| Threat actor attribution | Create distinct layers when multiple threat actors or campaigns are suspected. |

## Related articles

* [Case details](/xdr/features/investigate/case_details.md): Reference for every tab and field available on the case details page, including the Graph investigation tab entry point.
* [Cases](/xdr/features/investigate/cases.md): Overview of what cases are and how they are structured.
* [Events](/xdr/features/investigate/events.md): How to explore events and run contextual searches associated with a case.
* [AI Cases](/xdr/features/investigate/ai_cases.md): How Sekoia.io automatically correlates alerts into cases using AI.
