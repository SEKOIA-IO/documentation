# Reveal feature enablement matrix

This reference describes which data sources are required or optional for each Reveal capability. Use it to identify which sources to configure based on the features you need.

Each column represents a data source. Each row represents a Reveal capability.

| Capability | Passive Asset Discovery | Event data | Asset Connectors | Sekoia Endpoint Agent |
|---|---|---|---|---|
| **Asset context panel** | Displays lightly enriched assets | Adds activity, alerts, cases, and timeline context | Creates, merges, and enriches assets with identity, inventory, vulnerability, posture, and ownership context | Creates, merges, and enriches endpoint assets with endpoint context and hygiene data |
| **Asset timeline** | Provides assets and lightweight activity-derived context | Required | Adds source-specific context when available | Adds endpoint-specific context when available |
| **Points of Interest** | Not applicable | Required | Not applicable | Adds endpoint context where relevant |
| **Attack Path Visualization** | Enriches assets shown in the graph | Required | Enriches assets shown in the graph | Enriches assets shown in the graph |
| **Endpoint Hygiene** | Not applicable | Not applicable | Possible when supported by the source | Primary source when supported |
| **Vulnerability enrichment** | Not applicable | Not applicable | Primary source when supported | Possible depending on enabled capabilities |
| **Asset creation, enrichment, and unification** | Lightweight creation, merging, and enrichment from observed identifiers | Required for Passive Asset Discovery | Deep creation, merging, and enrichment from external systems | Deep creation, merging, and enrichment from external systems |
| **Defense Coverage** | Populates "Seen by" | Not applicable | Populates "Asset Connectors" | Populates "Seen by" |

## Related links

- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md)
- [Troubleshoot Reveal](/xdr/features/modules/reveal_troubleshoot.md)
- [Asset context panel - Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md)
- [Attack Path Visualization](/xdr/features/investigate/attack_path_visualization.md)
- [Points of Interest](/xdr/features/detect/points_of_interest.md)
