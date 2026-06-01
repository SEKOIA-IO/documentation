# Attack Path Visualization

Attack Path Visualization displays a graph of hosts and users connected to a selected asset through observed authentication relationships. It helps analysts assess whether a compromised or exposed asset provides a path to a more sensitive target, and where remediation would have the greatest effect.

The graph is available in the asset context panel under the **Attack Path Visualization** tab.

## How Attack Path Visualization works

Reveal builds the graph from authentication event data ingested into Sekoia. Each authentication event between two assets creates a directed relationship in the graph. The resulting graph shows which assets can be reached from the selected asset based on observed activity.

!!! note "Data requirement"
    Attack Path Visualization requires authentication event data. Without it, the graph does not display relationships. See [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md) for the full data source requirements.

## Graph elements

### Nodes

Each node in the graph represents an asset. Node appearance reflects the following properties:

| Property | Visual indicator |
|---|---|
| Asset criticality | Node color, from low (cool) to high (warm) based on configured criticality score |
| Asset type | Node icon (host, user, or account) |

### Satellite indicators

Each node displays satellite indicators that summarize active security signals without requiring the analyst to open each asset individually.

| Indicator | Description |
|---|---|
| Alerts | Number of active alerts associated with the asset |
| Cases | Number of open cases involving the asset |
| Vulnerabilities | Number of open CVE exposures on the asset |
| Hygiene issues | Number of active misconfigurations on the asset |

### Edges

Edges represent observed authentication relationships between assets. The direction of an edge indicates the direction of the observed authentication.

> 📸 [SCREENSHOT SUGGESTION: Attack Path Visualization graph showing five nodes of varying colors connected by directed edges, with satellite indicators visible on two nodes. | ALT TEXT: Attack path graph showing connected assets with criticality colors and satellite indicators.]

## Navigate the graph

| Action | How to perform |
|---|---|
| Pan | Click and drag on the graph background |
| Zoom | Scroll or use the zoom controls |
| Select a node | Click the node to highlight its direct connections |
| Open asset context | Double-click a node to open its asset context panel |
| Reset the view | Select the reset button to return to the default layout |

## How to use Attack Path Visualization during an investigation

**Assess blast radius:** start from the alerted or compromised asset and identify which high-criticality assets it connects to. High-criticality nodes reachable in one or two hops represent the highest-priority targets for containment.

**Identify chokepoints:** look for nodes that appear on multiple paths. Remediating or isolating a chokepoint asset may block several potential lateral movement routes simultaneously.

**Prioritize remediation:** use the satellite indicators to identify nodes that are both highly connected and have open vulnerabilities or hygiene issues. These represent the highest combined risk.

??? example "Lateral movement assessment after an endpoint compromise"
    A workstation involved in a credential dumping alert is selected in the graph. The Attack Path Visualization shows that the workstation has an authenticated relationship with a build server and a domain controller. The domain controller node has a high criticality score and satellite indicators showing two open critical CVEs. Containment of the workstation is prioritized, and the domain controller is flagged for immediate patching before the attack progresses further.

## Related links

- [Asset context panel: Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md): How to open the Attack Path Visualization tab from the asset context panel.
- [Vulnerability enrichment](/xdr/features/modules/reveal_vulnerabilities.md): How CVE data is surfaced on nodes in the graph.
- [Endpoint Hygiene](/xdr/features/modules/reveal_hygiene.md): How hygiene signals are surfaced on nodes in the graph.
- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md): How to configure the authentication event data required for Attack Path Visualization.
- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md): Data source requirements for Attack Path Visualization and other Reveal capabilities.
