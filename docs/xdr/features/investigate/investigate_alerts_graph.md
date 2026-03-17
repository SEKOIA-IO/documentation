# Investigate alerts with Graph

The Graph Investigation tab provides an interactive graphical visualization of an alert, enabling threat analysis through visual correlation of events and intelligence data.


## Graph elements

| Element | Description |
|---|---|
| **Observables** | Artifacts like IP addresses, domains, and file hashes. |
| **Observable Relationships** | Connections parsed via Smart Descriptions. |
| **CTI Objects** | Threat intelligence from the Intelligence Database. |
| **STIX Relationships** | Standardized connections between threat objects. |


## Manage layers

Layers organize complex graphs into manageable sections. Every investigation starts with a default layer.

1. Click the name of the current layer in the top-left of the graph.
2. Click **+** to add a new layer and enter a name.
3. Drag and drop objects into your preferred layer.
4. Toggle visibility by clicking the **Eye** icon next to a layer name.

!!! note
    All changes in the Graph Investigation are saved automatically. The graph updates dynamically as new events are associated with the alert.


## Pivot on data

- **Threat Intelligence**: Click a CTI object to view descriptions and relationship mappings in the left panel.
- **Observable Analysis**: Click an observable node to view event context, full event details, or perform an extended search.


## Related articles

* [Manage alerts](/xdr/features/investigate/alerts.mdmanage_alerts.md): Perform bulk actions and status updates on investigated alerts.
* [Alerts](/xdr/features/investigate/alerts.mdalerts.md): Understand the threat categories and similarity logic behind the graph data.
