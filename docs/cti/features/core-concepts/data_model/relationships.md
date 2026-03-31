# Relationships

STIX Relationship Objects (SROs) are typed, directional links between two STIX objects. They are what transforms a flat collection of threat entities into a connected, queryable knowledge graph.

Every relationship connects:

* A **source object** (e.g. a Threat Actor)
* A **relationship type** (e.g. `uses`)
* A **target object** (e.g. a Malware)

Relationships are first-class STIX objects. They carry their own metadata: a creation date, a confidence score, and source references.

### Exploring relationships <a href="#exploring-relationships" id="exploring-relationships"></a>

Every Object page in the Intelligence module exposes the full set of relationships associated with that object. Relationships are navigable: clicking on a related object takes you directly to its detail page, letting you traverse the threat graph step by step.

For a broader view, relationships can be visualized as a connected graph in [Graph Explorations →](../../graph_explorations.md).

### Exporting threat context <a href="#exporting-threat-context" id="exporting-threat-context"></a>

From any Object page, the **Export threat context** button lets you export an object together with all or a selection of its relationships as a STIX bundle. This is useful when you need to share a scoped, self-contained picture of a specific threat with another team or tool.

For details on export formats and options, see [Data Export →.](../../export/export-stix-objects.md)
