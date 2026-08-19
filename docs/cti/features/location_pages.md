# Location page

A **Location** is a geographic area, such as a country, region, or part of the world, associated with a threat’s origin or with the origin of the victims it targets. Locations contextualize Threat Actors, Intrusion Sets, Campaigns, and other objects according to geographic targeting or provenance.

The Location page brings together the profile of a geographic area, related campaigns, threat-landscape information, reports, relationships, and graph exploration. The examples in this article use Spain, but the same interface applies to any Location available in Sekoia Intelligence.

## Use cases

Use the Location page to:

- prepare a briefing about activity associated with a country or region;
- review campaigns that target or originate from a geographic area;
- identify the most active intrusion sets, malware, tools, and sectors linked to that activity;
- find reports associated with a Location;
- inspect relationships and pivot to related objects;
- export related objects for further analysis.

For general object search, see [Intelligence](/cti/features/consume/intelligence.md). For the object and relationship model, see the [Data model](/cti/features/data_model.md).

## Page structure

A Location page contains the following tabs:

| Tab | Purpose |
|---|---|
| **Overview** | Review the Location profile, latest campaigns, latest reports, and threat-landscape widgets. |
| **Threat Context** | Review related objects, relationships, metadata, and sources. |
| **Graph exploration** | Explore the Location and its relationships in a visual graph. |
| **Reports** | Browse the complete list of reports associated with the Location. |

Counts, campaigns, reports, sectors, and dates vary according to the selected Location and timeframe.

> 📸 [SCREENSHOT SUGGESTION: Location page for Spain with the Overview tab selected. Show the header, Latest campaigns section, and Threat Landscape section. | ALT TEXT: Spain Location page showing latest campaigns and threat-landscape widgets.]

## Header and object actions

The header displays the Location icon or flag and the Location name. It also contains the actions available for the object.

**Edit** and **Revoke** are only available for objects that your community has created. These actions are not available for an object created by Sekoia.

Depending on the community and your permissions, the header can also include:

- **See the Json**;
- **Request revocation**;
- **Export**.

### Export related objects

Select **Export** to open the **Export related objects** dialog. Choose the scope of the export:

- **All threat context**;
- **Selected categories**.

Then select a format:

- **CSV**;
- **JSON lines**;
- **Text**.

Select **Export** to download the selected data. For more information, see [Data Export](/cti/features/consume/export.md).

### Edit a Location

Select the edit action to open the **Edit an object** form. The form shown in the delivered interface contains:

| Field | Description |
|---|---|
| **Name** | The name of the Location. |
| **Region** | The geographic region associated with the Location. |
| **Country** | The country associated with the Location, when applicable. |
| **Description** | A rich-text description of the Location. |
| **Object type** | The object type, shown as **Location**. |
| **TLP** | The Traffic Light Protocol level. |
| **Confidence** | A value and its corresponding credibility description. |
| **Sources** | The sources that support the object, including source reliability. |
| **External references** | References with a name, description, and URL. |

The confidence control displays the value and its meaning. For example, the value `1` is displayed as **Confirmed by other sources**. Source reliability is shown separately, using a letter rating such as `A` with a description such as **Completely reliable**.

Select **Save** to apply the changes.

For more information about confidence and source reliability, see the [Data model](/cti/features/data_model.md).

### Revoke an object

Select **Revoke** to open the confirmation dialog. Revocation is permanent. The dialog warns that the object will no longer trigger detections and that the action cannot be reversed.

Select **Cancel** to close the dialog without revoking the object. Select **Revoke** to confirm.

## Overview

The **Overview** tab provides the main intelligence summary for the Location.

### Latest campaigns

The **Latest campaigns** section lists recent campaigns associated with the Location. The section displays activity for the last 12 months and includes a segmented control with two views:

- **Targeting [Location]**, for campaigns targeting the Location;
- **Originating [Location]**, for campaigns originating from the Location.

The delivered interface displays up to ten campaigns for the selected view. A campaign row can include:

- the campaign name;
- the campaign objective;
- the associated intrusion set;
- the associated malware;
- the number of tools;
- the number of IOCs.

Select a linked campaign, intrusion set, or malware to open its object page when a link is available. Select **View all** to open the complete campaign list.

### Latest reports

The **Latest reports** section lists reports associated with the Location. A report row can show its TLP, title, publication date, and source.

Select a report title or source to open the related content when a link is available. Select **View all** to open the complete report list in the **Reports** tab.

The list can include [FLINT Reports](/cti/features/consume/flints.md) from the Sekoia TDR team and [External Reports](/cti/features/consume/external_reports.md) from curated third-party sources.

### Threat Landscape

The **Threat Landscape** section summarizes activity associated with the Location. Use the timeframe selector to update the widgets together. The available options are:

- **Over the last 12 months**;
- **Over the last 24 months**;
- **Over the last 36 months**.

The delivered interface selects **Over the last 12 months** by default.

#### Most active Intrusions Set

This widget ranks intrusion sets by their appearances in campaigns associated with the Location.

Use the segmented control to switch between **Targeting [Location]** and **Originating [Location]**. Each row can show the intrusion-set name, the number of campaigns, and how long ago the activity was observed.

The footer indicates that the list is ordered by campaign appearances for the selected timeframe.

#### Most used Malware and Tools

This widget lists the malware and tools most frequently associated with campaigns targeting the Location. Each row can show the object name, its type icon, the number of campaigns, and how long ago the activity was observed.

The ranking is based on campaign appearances. A malware or tool can be used in multiple campaigns.

#### Most impacted sectors

This widget shows the sectors most frequently associated with campaigns targeting the Location. Each row displays a sector, its campaign count, and a proportional horizontal bar.

A campaign can target multiple sectors. The footer explains that sector percentages represent the share of the total campaigns and are not mutually exclusive categories.

> 📸 [SCREENSHOT SUGGESTION: Overview tab showing Latest campaigns, the Threat Landscape timeframe selector, and the three threat-landscape widgets. | ALT TEXT: Location overview showing campaigns, active intrusion sets, malware and tools, and impacted sectors.]

## Threat Context

The **Threat Context** tab shows the objects and relationships associated with the Location. See [Threat Context in the Intelligence documentation](/cti/features/consume/intelligence.md#threat-context) for the general workflow.

### Object distribution

The object-distribution cards summarize the number of related objects by type. The available categories can include:

- Identities;
- Threat Actors;
- Intrusion Sets;
- Attack Patterns;
- Campaigns;
- Malware.

### Relationships table

Use **Filters** to restrict the displayed relationships. Use **Search objects** to find a specific object.

The table can include:

| Column | Description |
|---|---|
| Source object | The object at the start of the relationship. |
| Relationship | The relationship type, such as `targets`, `originates-from`, or `located-at`. |
| Target object | The object at the end of the relationship. |
| Confidence | The confidence value associated with the relationship. |
| Sources | The sources supporting the relationship. |
| Created at | When the relationship was created. |
| Last edited | When the relationship was last edited. |
| First seen | When the relationship was first observed. |
| Last seen | When the relationship was most recently observed. |
| Valid from | When the relationship became valid, when available. |
| Valid until | When the relationship stops being valid, when available. |

Select an object name to pivot to the related object when a link is available.

The relationship view can group entries by relationship type. Expand or collapse a group to review its related objects. Use **Items per page** and the pagination controls to change the displayed results.

> 📸 [SCREENSHOT SUGGESTION: Threat Context tab showing object-distribution cards, the expanded relationship table, filters, search, metadata columns, and pagination. | ALT TEXT: Spain Threat Context showing related object counts and detailed campaign relationships.]

## Graph exploration

The **Graph exploration** tab displays the Location and its relationships as a visual graph. A side panel provides object details or relationships, while the main area displays the graph.

The graph interface can include:

- layer selection;
- object search;
- layout and graph controls;
- zoom controls;
- fit-to-view;
- fullscreen mode.

The side panel includes **Details** and **Relationships**. Relationship groups can include `originates-from`, `targets`, and `located-at`. Use the group pagination controls when a relationship group contains multiple entries.

For the general graph workflow, see [Graph Explorations](/cti/features/consume/graph_explorations.md).

> 📸 [SCREENSHOT SUGGESTION: Graph exploration tab showing the Location in the graph canvas and the Relationships side panel with grouped relationship types. | ALT TEXT: Spain graph exploration view with relationship groups in the side panel.]

## Reports

The **Reports** tab displays the complete list of reports associated with the Location.

The table includes:

| Column | Description |
|---|---|
| **TLP** | The report’s Traffic Light Protocol level. |
| **Name** | The report title. |
| **Published at** | The publication date and time. |
| **Sources** | The source or sources associated with the report. |

Report titles and sources are clickable when a destination is available. Use **Items per page** and the pagination controls to browse the list.

The delivered interface displays publication dates with the date and time, for example `22/06/2026 - 12:00:00`.

## Related articles

[Intelligence](/cti/features/consume/intelligence.md): How to search for intelligence objects and use Threat Context.

[Data model](/cti/features/data_model.md): Reference for objects, relationships, sources, and confidence.

[Graph Explorations](/cti/features/consume/graph_explorations.md): How to explore and save graph-based investigations.

[Data Export](/cti/features/consume/export.md): How to export related objects.

[FLINT Reports](/cti/features/consume/flints.md): Overview of Sekoia FLINT reports.

[External Reports](/cti/features/consume/external_reports.md): Overview of reports from external sources.
