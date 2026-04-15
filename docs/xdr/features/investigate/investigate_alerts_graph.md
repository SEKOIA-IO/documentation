# Investigate alerts with Graph

The Graph Investigation tab provides an interactive graphical visualization of an alert, enabling threat analysis through visual correlation of events and intelligence data.

!!! note
    All changes in the Graph Investigation are saved automatically. The graph updates dynamically as new events are associated with the alert, and any new objects discovered through additional events are automatically integrated into the existing graph structure.

## Graph elements

| Element | Description |
|---|---|
| **Observables** | Security artifacts extracted from events, including IP addresses, domain names, URLs, user accounts, and file hashes. |
| **Observable relationships** | Directional connections between observables, extracted from events using Smart Description definitions. |
| **CTI objects** | STIX-compliant threat intelligence objects from the Intelligence Database. |
| **STIX relationships** | Standardized connections between threat intelligence objects. |

## Pivot on data

### Threat intelligence

Click a CTI object in the graph to view the following in the left panel:

- Detailed object descriptions and threat context
- Complete relationship mappings with other intelligence objects
- Options to expand the graph by adding related objects

This allows you to pivot through the threat intelligence database and explore the full scope of related threats and campaigns.

### Observable analysis

Click an observable node in the graph to view the following in the left panel:

- **Event context** - All events within the alert that contain the selected observable, presented with Smart Description summaries.
- **Full event details** - Complete event information accessible via the **Full Events** button in the right panel.
- **Extended search** - Direct access to search for additional events containing the same observable value across your environment.

## Manage layers

Layers organize complex graphs into manageable, focused sections. Every investigation starts with a default layer that automatically incorporates new objects as additional events are processed.

### Create a layer

1. Click the name of the current layer in the top-left of the graph (e.g., "Event Layer #1").
2. Click **+** to add a new layer.
3. Enter a name for the layer.
4. Drag and drop objects into the new layer.

### Control layer visibility

To focus on the contents of a specific layer, click the **Eye** icon next to its name to toggle visibility.


## Layer strategies

Use layers to organize your investigation by analytical focus:

| Strategy | Description |
|---|---|
| **Observable type segregation** | Create separate layers for different observable categories (network indicators, file artifacts, user activities). |
| **Temporal analysis** | Organize layers by time period to understand attack progression across phases. |
| **Threat actor attribution** | Use separate layers for different suspected threat actors or techniques when multiple threats are identified. |

## Advanced layer features

- **Cross-layer movement** - Drag and drop objects between layers to maintain optimal organization as your investigation evolves.
- **Dynamic renaming** - Update layer names at any time to reflect your evolving understanding.
- **Intelligent search** - Use the built-in search to quickly locate specific objects within large, multi-layered graphs.

## Related articles

* [Investigate an alert](/xdr/features/investigate/investigate_an_alert.md): Navigate the alert detail page, tasks, similar alerts, and events.
* [Manage alerts](/xdr/features/investigate/manage_alerts.md): Perform bulk actions and status updates on alerts.
* [Alerts](/xdr/features/investigate/alerts.md): Understand the threat categories and similarity logic behind graph data.
