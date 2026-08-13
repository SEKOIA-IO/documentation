# Explore a location

Use a Location page to review a geographic area, understand its associated threat activity, inspect related objects, and open the reports connected to it.

A **Location** is a geographic area, such as a country, region, or part of the world, associated with a threat’s origin or with the victims’ origin it targets. Locations are used to contextualize Threat Actors, Intrusion Sets, Campaigns, and other objects based on geographic targeting or provenance.

## Before you start

Make sure that:

- your community has the **Intelligence** plan;

No specific role is required. Users can open a Location and view its reports and relationships when their community has the required plan and permissions.

## Open a Location

1. Open **Intelligence**.
2. Search for the Location by name. For a country, you can also search by its two-letter ISO 3166-1 country code, as described in the [Intelligence documentation](https://docs.sekoia.io/cti/features/consume/intelligence/#search-for-a-country).
3. Select the Location from the search results.

The page opens with the object header and the **Overview** tab.

## Review the header

The header displays the Location icon or flag and the Location name. The available actions depend on your community type:

- In a Sekoia community, the header can include **See the Json** **Edit**, **Revoke**, and **Export**.
- In a customer community, the header can include **See the Json**, **Request revocation**, and **Export**.

### Edit a Location

Select the edit action to open the edit form. Depending on the object, the form can include:

- name;
- region;
- country;
- description;
- object type;
- TLP;
- confidence;
- sources;
- external references.

The confidence control displays both a value and its meaning. For example, `1` is displayed as **Confirmed by other sources**. Source reliability is shown separately, using a letter rating such as `A`.

Select **Save** to apply the changes.

### Revoke a Location

1. On the top right corner of the page, select **Revoke** to open the confirmation dialog. The dialog warns that the object will no longer trigger detections because it will be permanently revoked, and that the action cannot be reversed.
2. Select **Cancel** to close the dialog, or **Revoke** to confirm.

### Export related objects

Select **Export** to open the **Export related objects** dialog. Choose either:

- **All threat context**;
- **Selected categories**.

Then select an export format:

- CSV;
- JSON lines;
- Text.

Select **Export** to download the selected data. For more information, see [Data Export](https://docs.sekoia.io/cti/features/consume/export/).

## Review the Overview tab

### Review latest campaigns

In **Latest campaigns**, use the segmented control to switch between:

- **Targeting [Location]**;
- **Originating [Location]**.

The section displays up to ten campaigns for the selected view and the last 12 months. Review the campaign name, objective, associated intrusion set, malware, tools, and IOCs when available.

Select a linked campaign, intrusion set, or malware to pivot to its object page. Select **View all** to open the complete campaign list.

### Review latest reports

In the **Latest reports** section, review the reports associated with the Location. A report can show its TLP, title, publication date, and source.

Select a report title or source to open the related content when a link is available. Select **View all** to open the complete report list in the **Reports** tab.

The list can include [FLINT Reports](https://docs.sekoia.io/cti/features/consume/flints/) from the Sekoia TDR team and [External Reports](https://docs.sekoia.io/cti/features/consume/external_reports/) from curated third-party sources.

### Review the Threat Landscape

The **Threat Landscape** section contains three widgets. Use the timeframe selector to update them together:

- **Over the last 12 months**;
- **Over the last 24 months**;
- **Over the last 36 months**.

The delivered interface defaults to **Over the last 12 months**.

Review:

- **Most active Intrusions Set**, which ranks intrusion sets by campaign appearances and lets you switch between targeting and originating activity;
- **Most used Malware and Tools**, which ranks malware and tools by campaign appearances;
- **Most impacted sectors**, which displays sectors with proportional campaign bars.

A campaign can target multiple sectors, so sector percentages are not mutually exclusive.

## Inspect Threat Context

1. Select **Threat Context**.
2. Review the object-distribution cards to see the number of related objects by type.
3. Use **Filters** to restrict the results.
4. Use **Search objects** to find a specific related object.
5. Review the relationship table.

The table can include the source object, relationship, target object, confidence, sources, creation and editing dates, first-seen and last-seen dates, and validity dates.

Select a related object to pivot to its object page. For the general workflow, see [Threat Context in the Intelligence documentation](https://docs.sekoia.io/cti/features/consume/intelligence/#threat-context).

## Explore relationships

In the relationship view, relationships can be grouped by type, such as `originates-from`, `targets`, and `located-at`.

- Expand or collapse a relationship group.
- Select a related object to open it.
- Use **Items per page** to change the number of displayed objects.
- Use the pagination controls to move through the results.

## Explore the graph

1. Select **Graph exploration**.
2. Use the side panel to review the Location details or relationships.
3. Use the search field to find objects in the graph.
4. Use the layer, layout, zoom, fit-to-view, and fullscreen controls as needed.

For the general graph workflow, see [Graph Explorations](https://docs.sekoia.io/cti/features/consume/graph_explorations/).

## Browse all reports

1. Select **Reports**.
2. Review the columns **TLP**, **Name**, **Published at**, and **Sources**.
3. Select a report title or source to open it when a link is available.
4. Use **Items per page** and the pagination controls to browse the list.

The delivered interface displays publication dates with the date and time, for example `22/06/2026 - 12:00:00`.

## Related articles

- [Location pages](./location_pages.md): Overview of the Location page structure and visible data.
- [Intelligence](https://docs.sekoia.io/cti/features/consume/intelligence/): Search for Location objects and use Threat Context.
- [Data model](https://docs.sekoia.io/cti/features/data_model/): Understand objects, relationships, sources, and confidence.
- [Graph Explorations](https://docs.sekoia.io/cti/features/consume/graph_explorations/): Explore and save graph-based investigations.
- [Data Export](https://docs.sekoia.io/cti/features/consume/export/): Export related objects.
