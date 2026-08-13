# Location pages

A **Location** is a geographic area, such as a country, region, or part of the world, associated with a threat’s origin or with the victims’ origin it targets. Locations are used to contextualize Threat Actors, Intrusion Sets, Campaigns, and other objects based on geographic targeting or provenance.

A Location page brings together the profile of a geographic area, related campaigns, threat-landscape information, reports, relationships, and graph exploration in one place. The examples in this article use Spain, but the same interface applies to any Location available in Sekoia Intelligence.

For general object search, see [Intelligence](https://docs.sekoia.io/cti/features/consume/intelligence/). For the object and relationship model, see the [Data model](https://docs.sekoia.io/cti/features/data_model/).

## Page structure

A Location page contains the following tabs:

| Tab | Purpose |
| --- | --- |
| **Overview** | Review the Location profile, latest campaigns, latest reports, and threat-landscape widgets. |
| **Threat Context** | Review related objects, relationships, metadata, and sources. |
| **Graph exploration** | Explore the Location and its relationships in a visual graph. |
| **Reports** | Browse the complete list of reports associated with the Location. |

The content is dynamic. Counts, campaigns, reports, sectors, and dates vary according to the selected Location and the selected timeframe.

## Header

The header displays the Location icon or flag and the Location name. It also provides object actions.

The available actions depend on the community type:

- In a Sekoia community, the header can include edit, **Revoke**, and **Export**.
- In a customer community, the header can include **See the Json**, **Request revocation**, and **Export**.

### Edit

The edit form can include the following fields:

- **Name**;
- **Region**;
- **Country**;
- **Description**, with rich-text formatting controls;
- **Object type**;
- **TLP**;
- **Confidence**;
- **Sources**;
- **External references**, with a name, description, and URL.

The confidence control displays both the value and its meaning. For example, the value `1` is displayed as **Confirmed by other sources**. Source reliability is shown separately, using a letter rating such as `A`, with a corresponding label such as **Completely reliable**.

For more information about confidence and source reliability, see the [Sekoia data model](https://docs.sekoia.io/cti/features/data_model/).

### Revoke

**Revoke** permanently revokes the object. A confirmation dialog warns that the object will no longer trigger detections and that the action cannot be reversed.

Select **Cancel** to close the dialog without revoking the object, or **Revoke** to confirm.

### Export

**Export** opens the **Export related objects** dialog. You can choose to export:

- **All threat context**;
- **Selected categories**.

You can then select one of the following formats:

- CSV;
- JSON lines;
- Text.

For more information, see [Data Export](https://docs.sekoia.io/cti/features/consume/export/).

## Overview

The **Overview** tab provides the main intelligence summary for the Location.

### Latest campaigns

The **Latest campaigns** section lists recent campaigns associated with the Location.

Use the segmented control to switch between:

- **Targeting [Location]**, for campaigns targeting the Location;
- **Originating [Location]**, for campaigns originating from the Location.

The section displays up to ten campaigns for the selected view and the last 12 months. Each row can show:

- the campaign name;
- the campaign objective;
- the associated intrusion set;
- the associated malware;
- the number of tools;
- the number of IOCs.

Select a campaign, intrusion set, or malware name to open the corresponding object when it is available. Select **View all** to open the complete campaign list.

### Latest reports

The **Latest reports** section lists reports associated with the Location. A report row can show its TLP, title, publication date, and source.

Select a report title or source to open the related content when a link is available. Select **View all** to open the complete report list in the **Reports** tab.

The list can include [FLINT Reports](https://docs.sekoia.io/cti/features/consume/flints/) from the Sekoia TDR team and [External Reports](https://docs.sekoia.io/cti/features/consume/external_reports/) from curated third-party sources.

### Threat Landscape

The **Threat Landscape** section summarizes the activity associated with the Location. Use the timeframe selector to update the widgets together. The available options are:

- **Over the last 12 months**;
- **Over the last 24 months**;
- **Over the last 36 months**.

The default selection shown in the delivered interface is **Over the last 12 months**.

#### Most active Intrusions Set

This widget ranks intrusion sets by their appearances in campaigns associated with the Location.

Use the segmented control to switch between **Targeting [Location]** and **Originating [Location]**. Each row can show the intrusion-set name, the number of campaigns, and how long ago the activity was observed.

The widget is ordered by the most appearances among the campaigns in the selected timeframe.

#### Most used Malware and Tools

This widget lists the malware and tools most frequently associated with campaigns targeting the Location. Each row can show the object name, its type icon, the number of campaigns, and how long ago the activity was observed.

The ranking is based on campaign appearances. A malware or tool can be used in multiple campaigns.

#### Most impacted sectors

This widget shows the sectors most frequently associated with campaigns targeting the Location. Each row displays a sector, its campaign count, and a proportional bar.

A campaign can target multiple sectors. Percentages therefore represent the share of the total campaign appearances shown by the widget, not mutually exclusive categories.

## Threat Context

The **Threat Context** tab shows the objects and relationships associated with the Location. See [Threat Context in the Intelligence documentation](https://docs.sekoia.io/cti/features/consume/intelligence/#threat-context) for the general workflow.

### Object distribution

The object-distribution cards summarize the number of related objects by type. The available categories can include identities, threat actors, intrusion sets, attack patterns, campaigns, and malware.

### Relationships table

Use **Filters** to restrict the displayed relationships and **Search objects** to find a specific object.

The table can include:

- source object;
- relationship;
- target object;
- confidence;
- sources;
- created at;
- last edited;
- first seen;
- last seen;
- valid from;
- valid until.

Relationship names can include `targets`, `originates-from`, and `located-at`. Select an object name to pivot to the related object when a link is available.

The object relationship view can also group relationships by type. Expand or collapse a group to review its related objects, and use the pagination controls to change the number of items displayed.

## Graph exploration

The **Graph exploration** tab displays the Location and its relationships as a visual graph. A side panel provides object details or relationships, while the main area displays the graph.

The graph interface can include:

- layer selection;
- object search;
- layout and graph controls;
- zoom controls;
- fit-to-view;
- fullscreen mode.

For the general graph workflow, see [Graph Explorations](https://docs.sekoia.io/cti/features/consume/graph_explorations/).

## Reports

The **Reports** tab displays the complete list of reports associated with the Location.

The table includes:

- **TLP**;
- **Name**;
- **Published at**;
- **Sources**.

Report titles and sources are clickable when a destination is available. Use **Items per page** to change the number of rows displayed, then use the pagination controls to navigate through the results.

The delivered interface displays publication dates with the date and time, for example `22/06/2026 - 12:00:00`.

## Related articles

- [Explore a location](./explore_a_location.md): How to review a Location and use its tabs.
- [Intelligence](https://docs.sekoia.io/cti/features/consume/intelligence/): Search for Location objects and use Threat Context.
- [Data model](https://docs.sekoia.io/cti/features/data_model/): Understand objects, relationships, sources, and confidence.
- [Graph Explorations](https://docs.sekoia.io/cti/features/consume/graph_explorations/): Explore and save graph-based investigations.
- [Data Export](https://docs.sekoia.io/cti/features/consume/export/): Export related objects.
- [FLINT Reports](https://docs.sekoia.io/cti/features/consume/flints/) and [External Reports](https://docs.sekoia.io/cti/features/consume/external_reports/): Learn more about the report types shown on a Location page.
