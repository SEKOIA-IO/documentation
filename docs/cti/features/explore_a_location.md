# Explore a location

Use the Location page to review a country profile, inspect associated reports, and analyze relationships with other intelligence objects. In Sekoia’s data model, a country is represented as a `Location` object. The page provides details, relationship data, a graph view, and a complete report list from the same object. For general Intelligence search guidance, see the [Intelligence documentation](https://docs.sekoia.io/cti/features/consume/intelligence/).

## Prerequisites

Before you start, make sure that:

- you can access **Intelligence**;
- you can open the Location object you want to review;
- your role includes access to the reports and relationship data you need.

## Review the Location

1. Open the country’s Location object from **Intelligence**. You can search by the country name or by its two-letter ISO 3166-1 country code, as described in the [Intelligence documentation](https://docs.sekoia.io/cti/features/consume/intelligence/#search-for-a-country).

    The page opens with the object header and the **Details** tab.

2. Review the object header.

    Confirm the country name, TLP label, object type, confidence value, creation date, and modification date. The header also shows the object actions available to you, including edit, **Revoke**, and **Export**.

3. Read the country description.

    Use the description to establish the initial context for the country. The text can include formatted sections covering cyber posture, operations, defensive capabilities, sectors, geopolitical context, or associated intrusion sets.

4. Review the latest reports.

    In the **Latest reports** panel, review the report titles, relative publication dates, and sources. The list can include [FLINT Reports](https://docs.sekoia.io/cti/features/consume/flints/) from the Sekoia TDR team and [External Reports](https://docs.sekoia.io/cti/features/consume/external_reports/) from curated third-party sources.

5. Open the complete report list.

    To review all reports associated with the Location, click **View more**.

6. Open the threat context.

    To review related objects and their relationships, click **Threat Context**. See [Threat Context in the Intelligence documentation](https://docs.sekoia.io/cti/features/consume/intelligence/#threat-context) for the general workflow.

7. Review object distribution.

    Use the distribution cards to see how many related objects are available for categories such as Campaigns, Intrusion Sets, Malware, Threat Actors, Identities, and Attack Patterns.

8. Filter the relationships.

    To narrow the relationship table, click **Filters** and select the filters you need.

9. Search for an object.

    To find a specific object in the current threat context, enter its name in the object search field.

10. Inspect a relationship.

    Review the source object, relationship, target object, confidence, and supporting sources. Relationship values can include `targets`, `originates-from`, and `located-at`.

11. Open graph exploration.

    To view the Location and its relationships as a graph, click **Graph exploration**. For the full graph workflow, see [Graph Explorations](https://docs.sekoia.io/cti/features/consume/graph_explorations/).

12. Search or adjust the graph.

    Use the graph search field and the graph controls to change the layout, zoom, fit the graph to the available space, or expand the view.

13. Review related objects in the side panel.

    Use the **Details** and **Relationships** sub-tabs to inspect the selected object and its relationship groups. Select a related object when you want to continue the investigation from that object.

14. Open the Reports tab.

    To work with the complete report list directly, click **Reports**.

15. Change the number of displayed reports.

    Select a value from **Items per page**.

16. Move between report pages.

    Use the pagination controls to display the next or previous set of reports.

!!! note "Confidence values"
    Confidence values use the Admiralty Credibility scale described in the [Sekoia data model](https://docs.sekoia.io/cti/features/data_model/). A value of `1` means **confirmed by other sources**. Source reliability uses a separate letter-based scale.

## Result

You can use the Location page to establish country context, identify related intelligence objects, inspect supporting sources, and review the complete set of associated reports without leaving the Location object.

## Related articles

- [Location pages](./location_pages.md): Overview of the Location page structure and its visible data.
- [Intelligence](https://docs.sekoia.io/cti/features/consume/intelligence/): Search for Location objects and use Threat Context.
- [Data model](https://docs.sekoia.io/cti/features/data_model/): Understand STIX objects, relationships, sources, and confidence.
- [Graph Explorations](https://docs.sekoia.io/cti/features/consume/graph_explorations/): Explore and save graph-based investigations.
- [Data Export](https://docs.sekoia.io/cti/features/consume/export/): Export related items from an object page.
