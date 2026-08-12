# Location pages

A **Location** is a geographic area, such as a country, region, or part of the world, associated with a threat’s origin or with the victims’ origin it targets. Locations are used to contextualize Threat Actors, Intrusion Sets, Campaigns, and other objects based on geographic targeting or provenance.

Location pages give you a consolidated view of a Location in [Sekoia Intelligence](https://docs.sekoia.io/cti/features/consume/intelligence/). They combine object metadata, a geographic profile, related reports, threat-context relationships, and graph exploration in one place.

## Purpose

A Location page helps you build an initial understanding of a geographic area without opening several separate views. You can review the Location profile, inspect reports linked to it, examine related objects, and explore relationships in the knowledge graph.

This view supports CTI analysts who prepare briefings and MSSP operators who need a sourced starting point for a client deliverable.

## Page structure

A Location page contains the following areas:

| Area | What it contains |
|---|---|
| Header | The Location name, object type, TLP, confidence, creation date, modification date, and object actions |
| **Details** | The Location profile and a preview of the latest reports |
| **Threat Context** | Counts and relationships for objects associated with the Location |
| **Graph exploration** | A graph view of the Location and its relationships |
| **Reports** | The complete paginated list of reports associated with the Location |

> 📸 [SCREENSHOT SUGGESTION: Location page with the France object header and the Details tab selected. Show the description and Latest reports panel. | ALT TEXT: France Location page displaying object metadata, a country description, and recent reports.]

## Header

The header identifies the Location and provides access to object actions. It displays:

- the geographic icon or flag, when available;
- the Location name;
- the Traffic Light Protocol (TLP) label, such as **WHITE**;
- the object type, shown as **Location**;
- the confidence value;
- the creation date;
- the modification date.

The header also contains object actions, including edit, **Revoke**, and **Export**. The actions available to you depend on the object state and your permissions.

!!! note "Confidence values"
    Confidence values use the Admiralty Credibility scale documented in the [Sekoia data model](https://docs.sekoia.io/cti/features/data_model/). A value of `1` means **confirmed by other sources**. This is different from source reliability, which uses a letter scale.

TLP labels are displayed as color-coded badges throughout the page. Sekoia documents TLP as an indication of information sensitivity, with White, Green, Amber, and Red levels. See the [Intelligence page](https://docs.sekoia.io/cti/features/consume/intelligence/) for the object table and TLP conventions. The same visual treatment appears in the report list.

## Details

The **Details** tab provides the Location profile and a short list of recent reports.

### Location profile

The profile provides geographic and threat context about the Location. For a country, it can cover the country’s cyber posture, known operations, defensive capabilities, sectors of interest, geopolitical context, or associated intrusion sets.

The description can contain headings and formatted text. Use it as the starting point for understanding the Location before reviewing relationships or reports.

### Latest reports

The **Latest reports** panel provides a short preview of reports associated with the Location. Each entry shows the report title, a relative publication date, and its source. Select **View more** to open the complete report list.

The preview can contain [Sekoia FLINTs](https://docs.sekoia.io/cti/features/consume/flints/) and [External Reports](https://docs.sekoia.io/cti/features/consume/external_reports/). FLINTs are produced by the Sekoia TDR team, while External Reports come from curated third-party sources. The report source is shown below the title, for example **Sekoia** or an external website.

## Threat Context

The **Threat Context** tab shows how the Location relates to other objects in Sekoia Intelligence. Its object distribution and relationship table follow the concepts described in the [Intelligence documentation](https://docs.sekoia.io/cti/features/consume/intelligence/#threat-context) and the [STIX-based data model](https://docs.sekoia.io/cti/features/data_model/).

### Object distribution

The object distribution cards summarize the number of related objects by type. The interface can display counts for categories such as:

- Identities;
- Threat Actors;
- Campaigns;
- Intrusion Sets;
- Attack Patterns;
- Malware.

The counts are specific to the selected Location and can change as the underlying intelligence changes.

### Relationship table

The relationship table lists the links between the Location and related objects. The visible columns are:

| Column | Description |
|---|---|
| Source object | The object at the start of the relationship |
| Relationship | The relationship type, such as `targets`, `originates-from`, or `located-at` |
| Target object | The object at the end of the relationship |
| Confidence | The confidence value associated with the relationship |
| Sources | The sources supporting the relationship |

Use **Filters** to limit the displayed relationships. Use the object search field to find a specific object in the current context.

> 📸 [SCREENSHOT SUGGESTION: Threat Context tab showing object distribution cards, Filters, the object search field, and the relationship table. | ALT TEXT: Threat Context for France showing related object counts and campaign relationships.]

## Graph exploration

The **Graph exploration** tab presents the Location and its relationships as a visual graph. For the broader graph workflow, see [Graph Explorations](https://docs.sekoia.io/cti/features/consume/graph_explorations/).

The view contains:

- a side panel with the selected object;
- **Details** and **Relationships** sub-tabs in the side panel;
- a graph canvas containing the selected object and related objects;
- a layer control;
- a graph search field;
- controls for layout, zoom, fitting the graph to the available space, and expanding the view.

The side panel can list relationship groups such as `originates-from`, `located-at`, and `targets`. Select a related object to continue the investigation from that object.

> 📸 [SCREENSHOT SUGGESTION: Graph exploration tab showing France in the graph canvas and the Relationships sub-tab in the side panel. | ALT TEXT: Graph exploration view for France with related objects listed in the side panel.]

## Reports

The **Reports** tab provides the complete list of reports associated with the Location.

The table contains:

| Column | Description |
|---|---|
| TLP | The report’s Traffic Light Protocol label |
| Name | The report title |
| Published at | The publication date and time |
| Sources | The source or sources associated with the report |

Report names and sources are presented as links when a destination is available. The list supports pagination. Use **Items per page** to change the number of entries shown, then use the pagination controls to move between result pages. For exporting related objects from an object page, see [Data Export](https://docs.sekoia.io/cti/features/consume/export/).

The Reports tab displays publication timestamps in the format shown by the interface, for example `05/06/2026 - 07:09:59`.

> 📸 [SCREENSHOT SUGGESTION: Reports tab showing TLP badges, report names, publication timestamps, sources, and pagination controls. | ALT TEXT: Paginated report list for France with TLP, publication date, and source columns.]

## Related articles

- [Explore a location](./explore_a_location.md): How to review a Location, its reports, relationships, and graph.
- [Intelligence](https://docs.sekoia.io/cti/features/consume/intelligence/): Search for Location objects and use Threat Context.
- [Data model](https://docs.sekoia.io/cti/features/data_model/): Understand STIX objects, relationships, sources, and confidence.
- [Graph Explorations](https://docs.sekoia.io/cti/features/consume/graph_explorations/): Build and save graph-based investigations.
- [Data Export](https://docs.sekoia.io/cti/features/consume/export/): Export related items from an object page.
- [FLINT Reports](https://docs.sekoia.io/cti/features/consume/flints/) and [External Reports](https://docs.sekoia.io/cti/features/consume/external_reports/): Learn more about the report types shown on a Location page.
