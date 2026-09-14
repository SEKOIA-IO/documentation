# Intelligence

## Introduction

Looking for a threat actor? A specific malware? A report on a topic of interest? Or a URL that looks suspicious? The Intelligence page provides a search engine with filtering capabilities for millions of records. This threat knowledge base is updated on a daily basis by Sekoia analysts to make sure all kinds of threats are covered.

## How to search

### Search bars

You can find what you need in the knowledge base in two ways:

1. Use the search bar embedded in the menu. It’s accessible from any page of the app and enables a quick search in the database.
2. Click `Intelligence` from the app menu and use the main search bar to browse the knowledge you need.

![Intelligence-search](/assets/intelligence_center/intelligence%20search.png){: style="max-width:100%"}

You can search for **multiple items at the same time**. To skip a line and paste multiple items, press `Shift-Enter` and paste your content.


!!! tip
    You can easily open multiple search results in new tabs by right-clicking on an object and using your mouse, `option+click` (for Mac), or `shift+click` (for Windows).


### Tabs

After you’ve typed your search and clicked on `enter`, two or three tabs appear under the search bar: one for **objects**, one for **observables** and one for **unknown observables**.

You can refer to [the data model page](/cti/features/data_model.md) to understand what objects and observables are and how our data model works.

Each tab has a counter that informs users about the **number of items** in the database for each category.

For instance, if you search for `Google`, you will find numerous objects (reports, Intrusion sets, Indicators…) but only two observables.

!!! tip
    Always check all tabs to be sure to get all information needed on a topic. Observables may not be harmful but they can be helpful in an investigation.

## Search for objects

### How the search engine works

When searching for a term or multiple terms, Sekoia will list objects with fields that match the term(s).

The following fields are taken into consideration by the search engine:

- Name
- Description
- Aliases
- Content of a report
- External references
- The location’s country code (if the search term contains 2 characters)

By default, search results are sorted by **Pertinence**. Use the sort selector above the table to change the order, for example to the last edit date.

!!! Tip
    When the search contains multiple words, it can be useful to see the results matching exactly what has been entered. Putting the search between quotes (`" "`) will search for objects containing the exact term in one of their fields.

!!! note
    The search bar is **tokenized**. It means that if the user searches for `FLINT 2022-05` it will look for `FLINT`, `2022` and `05` and then apply scoring depending on the attribute the value was found in and the number of times it was found.

    To get only the item where the name starts with `FLINT 2022-05`, this dork search can be performed: `name:^"FLINT 2022-05"`

#### Search for specific sectors

In the STIX format, a Sector is an **Identity object** that represents a broad business sector or industry. Sectors are used to contextualize threat actors, campaigns, and other CTI entities based on their targeting of specific sectors. For example, a Sector object could represent the Finance sector, Healthcare sector, or Government sector.

The table below lists all sectors present in Sekoia as well as their sub-types:

| **Sector**                  | **Subtypes**                                  |
|-----------------------------|-----------------------------------------------|
| Defence                     | Defence-Military                              |
|                             | Defence-Industry                              |
| Education                   | Education-R&D                                 |
|                             | Education-Institutions                        |
| Energy                      | Energy-Electricity                            |
|                             | Energy-Renewable                              |
|                             | Energy-Gas                                    |
|                             | Energy-Nuclear                                |
|                             | Energy-Transportation                         |
|                             | Energy-Oil                                    |
| Entertainment               | Entertainment-Gaming                          |
|                             | Entertainment-Culture                         |
|                             | Entertainment-Gambling                        |
|                             | Entertainment-Sport                           |
| Financial-Services          | Financial-Services-Real Estate                |
|                             | Financial-Services-Cryptocurrencies           |
|                             | Financial-Services-Insurance                  |
| Government                  | Government-Education                          |
|                             | Government-Interior                           |
|                             | Government-Local                              |
|                             | Government-Regional                           |
|                             | Government-Foreign Affairs                    |
|                             | Government-Justice                            |
|                             | Government-Intelligence and Security Services |
|                             | Government-National                           |
|                             | Government-Defence                            |
| Healthcare                  | Healthcare-Pharmaceuticals                    |
|                             | Healthcare-R&D                                |
|                             | Healthcare-Equipment                          |
|                             | Healthcare-Hospital                           |
|                             | Hospitality-Leisure                           |
| Industry                    | Industry-Semiconductor                        |
|                             | Industry-Food and beverage                  |
|                             | Industry-Pharmacy                             |
|                             | Industry-Agrobusiness                         |
|                             | Industry-Agriculture                          |
|                             | Industry-Wholesale                            |
|                             | Industry-Manufacturing                        |
|                             | Industry-Mining                               |
|                             | Industry-Construction                         |
|                             | Industry-Retail                               |
|                             | Industry-Chemical                             |
|                             | Industry-Automotive                           |
| Infrastructure              | Infrastructure-Critical                       |
| Legal                       |                                               |
| Media                       | Media-Social network                          |
|                             | Media-Individual                              |
|                             | Media-TV channel                              |
|                             | Media-Radio                                   |
|                             | Media-Newspaper                               |
| NGO/Civil-Society/Political | NGO/Civil-Society/Political-Dissident         |
|                             | NGO/Civil-Society/Political-Activist          |
| Professional services       | Professional services-Consulting              |
|                             | Professional services-Management              |
|                             | Professional services-Printing                |
|                             | Professional services-Marketing               |
| Technology                  | Technology-High-Tech                          |
|                             | Technology-Services                           |
| Telecommunications          | Telecommunications-Satellite                  |
|                             | Telecommunications-Phone                      |
|                             | Telecommunications-Internet                   |
| Transportation              | Transportation-Shipping                       |
|                             | Transportation-Air                            |
|                             | Transportation-Road                           |
|                             | Transportation-Maritime                       |
|                             | Transportation-Rail                           |



!!! note
    Note that **Media** is a subtype of Entertainment.

!!! tip
    Select **Identity** in **Filters > Object types** to refine your search and list only Identity objects.

#### Search for a Location

A **Location** is a geographic area, such as a country, region, or part of the world, associated with a threat’s origin or with the origin of the victims it targets. Locations contextualize Threat Actors, Intrusion Sets, Campaigns, and other objects according to geographic targeting or provenance.

Search for a Location by entering its name. The results can include countries, regions, or larger geographic areas. For example, a search for `europe` can return **Europe**, **Southern Europe**, **Western Europe**, and other matching Locations.

For a country, you can also search by its two-letter country code, following the **[ISO 3166-1](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en)** reference. For example, use `FR` for France, `AE` for the United Arab Emirates, or `NG` for Nigeria.

### Table columns

Search results are listed in a table with multiple columns. These columns can be shown or hidden in the filters panel, and users can change their order by dragging them using the `:` icon.

By default, these columns are:

| Column | Description |
| --- | --- |
| TLP | How sensitive is the information. Types of TLP in Sekoia: White, green, amber, red |
| Type | Type of object. For a Location with a country field, the table displays the corresponding country flag. A Location without a country uses the Location icon. |
| Name | Name of object. Hover on the name to read the full name |
| Subtypes | Some objects have subtypes such as indicators, malware, reports, or tools. |
| Conf. | How confident Sekoia is about this object |
| Sources | Where this object came from |
| Last Edited | Date of last edit |
| Created | Date of creation |
| Labels | Custom labels added from Sekoia |

To show or hide these columns, click on the icon on the top right of the table and select the ones needed.

### Quick filters

On the **Objects** tab, the **Locations** and **Sectors** buttons provide shortcuts for filtering by object type. They appear next to **Filters**.

Select **Locations** or **Sectors** to apply the corresponding object-type filter directly. The resulting filter badge is the same as the badge created through **Filters > Object types**:

- `Object types is Location`;
- `Object types is Sector`.

When you reopen the filter menu, the selected object type is already checked. Select **Clear filters** or remove the filter from its badge to reset the results.

### Object icons

The Objects table uses dedicated icons for Location, Sector, and Source objects:

- Location objects without a country use the Location map-pin icon;
- Sector objects use the Sector icon;
- Source objects use the open-book icon.

Location objects with a country display the corresponding country flag in the **Type** column. Flags use rounded corners for consistent rendering.

### Pagination

Depending on your screen size, you can change the pagination of this data table. It is set to 25 results per page by default, but you can increase or decrease this number to 10, 15, 50 or 100.

### Revoked objects

When an object name is red in the table, it means that the object has been revoked.

### Filters for objects

To filter results in the Intelligence table, select **Filters**. When a filter is selected, a filter chip is added above the table. The filter menu includes:

| Filter | Description |
|---|---|
| **Object types** | Filter results by object type, such as Location, Sector, Source, Campaign, or Malware. |
| **IOC types** | Filter observable or indicator results by indicator type. |
| **Sources** | Search the sources associated with objects. |
| **Confidence level** | Filter objects by confidence level. |
| **Created at** | Filter objects by creation date. |
| **Feeds** | Show only objects matching a feed. |
| **Last update** | Filter objects by the time of their last update. |
| **TLP** | Filter objects by their Traffic Light Protocol level. |

Select **Clear filters** to remove all active filters. You can also remove an individual filter from its chip.

## Object details page

Opening an object from the search results displays its details page. Any user with permission to read objects can access object pages. No specific role is required, and guest users can view them when their community has the Intelligence plan.

### Page structure

An object details page contains the following tabs:

| Tab | Purpose |
|---|---|
| **Details** | Review the object's core STIX information. Shown for most object types. |
| **Overview** | Review the object profile, latest campaigns, latest reports, and threat-landscape widgets. Currently available for **Locations** and **Sectors**. |
| **Threat Context** | Review related objects, relationships, metadata, and sources. |
| **Graph exploration** | Explore the object and its relationships in a visual graph. |
| **Reports** | Browse the complete list of reports associated with the object. |

Counts, campaigns, reports, sectors, and dates vary according to the selected object and timeframe.

### Header and object actions

The header displays the object icon (or flag, for Locations) and the object name. It also contains the actions available for the object.

**Edit** and **Revoke** are available in any workspace, but only for objects you created yourself. These actions are not available for objects created by someone else.

Depending on the community and your permissions, the header can also include access to:

- **Raw STIX Object**;
- **Request revocation**;
- **Export**.

#### Export related objects

Select **Export** to open the **Export related objects** dialog. Choose the scope of the export:

- **All threat context**;
- **Selected categories**.

Then select a format:

- **CSV**;
- **JSON lines**;
- **Text**.

Select **Export** to download the selected data. For more information, see [Data Export](/cti/features/consume/export.md).

#### Edit an object

The edit action opens the **Edit an object** form. This action is available only for objects you created yourself. For a Location, the form contains:

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

#### Revoke an object

Select **Revoke** to open the confirmation dialog. Revocation is permanent. The dialog warns that the object will no longer trigger detections and that the action cannot be reversed.

Select **Cancel** to close the dialog without revoking the object. Select **Revoke** to confirm.

### Details tab

For object types other than Locations and Sectors, the first tab is **Details**. It shows the object's core information drawn from its STIX object, which can include:

- the description;
- the first-seen and last-seen dates;
- the sources;
- the confidence level and TLP;
- aliases and external references;
- other dedicated information. For example, campaign details can include the latest reports and indicators related to threats.

### Overview tab

The **Overview** tab provides the main intelligence summary for the object. It is currently available for **Locations** and **Sectors** only; other object types show the [Details tab](#details-tab) instead.

#### Latest campaigns

The **Latest campaigns** section lists recent campaigns associated with the object over the last 12 months. For Locations and Sectors, it includes a segmented control with two views:

- **Targeting [object]**, for campaigns targeting the object;
- **Originating [object]**, for campaigns originating from the object.

The section displays up to ten campaigns for the selected view. A campaign row can include:

- the campaign name;
- the campaign objective;
- the associated intrusion set;
- the associated malware;
- the number of tools;
- the number of IOCs.

Select a linked campaign, intrusion set, or malware to open its object page when a link is available. Select **View all** to open the complete campaign list.

#### Latest reports

The **Latest reports** section lists reports associated with the object. A report row can show its TLP, title, publication date, and source.

Select a report title or source to open the related content when a link is available. Select **View all** to open the complete report list in the **Reports** tab.

The list can include [FLINT Reports](/cti/features/consume/flints.md) from the Sekoia TDR team and [External Reports](/cti/features/consume/external_reports.md) from curated third-party sources.

#### Threat Landscape

The **Threat Landscape** section summarizes activity associated with the object. Use the timeframe selector to update the widgets together. The available options are:

- **Over the last 12 months**;
- **Over the last 24 months**;
- **Over the last 36 months**.

**Over the last 12 months** is selected by default.

The widgets shown in this section depend on the object type; see [Location pages](#location-pages) and [Sector pages](#sector-pages) for details.

> 📸 [SCREENSHOT SUGGESTION: Overview tab showing Latest campaigns, the Threat Landscape timeframe selector, and the threat-landscape widgets. | ALT TEXT: Object overview showing campaigns, active intrusion sets, malware and tools, and impacted sectors.]

### Threat Context tab

The **Threat Context** tab shows the objects and relationships associated with the object.

#### What you can do

**Search and filter**

- Use the **search bar** to find a related object by name without scrolling through large result sets
- **Filter by IOC type** to scope the view to a specific category (IP addresses, domains, file hashes, and more)
- Use the **Last updated** filter to limit results to relationships updated in the last 30 days

**Understand relationships at a glance**

The **object distribution cards** show how many objects are related to the current threat, what relationships exist, and what types they are (downloads, drops, uses, targets, and others). This gives you an immediate structural overview before you explore individual links. Click a card to filter by that relationship type.

**Manage columns**

- Add **First Seen** and **Last Seen** columns alongside the existing Valid From and Valid Until columns
- Reorder columns to match your workflow
- Column state persists across sessions

> 📸 [SCREENSHOT SUGGESTION: Threat Context tab showing object-distribution cards, the expanded relationship table, filters, search, metadata columns, and pagination. | ALT TEXT: Threat Context showing related object counts and detailed campaign relationships.]

### Graph exploration tab

The **Graph exploration** tab displays the object and its relationships as a visual graph. A side panel provides object details or relationships, while the main area displays the graph.

The graph interface can include:

- layer selection;
- object search;
- layout and graph controls;
- zoom controls;
- fit-to-view;
- fullscreen mode.

For the general graph workflow, see [Graph Explorations](/cti/features/consume/graph_explorations.md).

> 📸 [SCREENSHOT SUGGESTION: Graph exploration tab showing the object in the graph canvas and the Relationships side panel with grouped relationship types. | ALT TEXT: Graph exploration view with relationship groups in the side panel.]

### Reports tab

The **Reports** tab displays the complete list of reports associated with the object.

The table includes:

| Column | Description |
|---|---|
| **TLP** | The report’s Traffic Light Protocol level. |
| **Name** | The report title. |
| **Published at** | The publication date and time, for example `22/06/2026 - 12:00:00`. |
| **Sources** | The source or sources associated with the report. |

Report titles and sources are clickable when a destination is available. Use **Items per page** and the pagination controls to browse the list.

### Location pages

A **Location** is a geographic area, such as a country, region, or part of the world, associated with a threat’s origin or with the origin of the victims it targets. Locations contextualize Threat Actors, Intrusion Sets, Campaigns, and other objects according to geographic targeting or provenance.

Use the Location page to:

- prepare a briefing about activity associated with a country or region;
- review campaigns that target or originate from a geographic area;
- identify the most active intrusion sets, malware, tools, and sectors linked to that activity;
- find reports associated with a Location;
- inspect relationships and pivot to related objects;
- export related objects for further analysis.

Relationship groups for a Location can include `originates-from`, `targets`, and `located-at`.

In addition to the generic Overview sections, the **Threat Landscape** of a Location page includes the following widgets:

**Most active Intrusion Set** ranks intrusion sets by their appearances in campaigns associated with the Location. Use the segmented control to switch between **Targeting [Location]** and **Originating [Location]**. Each row can show the intrusion-set name, the number of campaigns, and how long ago the activity was observed. The list is ordered by campaign appearances for the selected timeframe.

**Most used Malware and Tools** lists the malware and tools most frequently associated with campaigns targeting the Location. Each row can show the object name, its type icon, the number of campaigns, and how long ago the activity was observed. A malware or tool can be used in multiple campaigns.

**Most impacted sectors** shows the sectors most frequently associated with campaigns targeting the Location. Each row displays a sector, its campaign count, and a proportional horizontal bar. A campaign can target multiple sectors, so sector percentages represent the share of total campaigns and are not mutually exclusive categories.

> 📸 [SCREENSHOT SUGGESTION: Location page for Spain with the Overview tab selected. Show the header, Latest campaigns section, and Threat Landscape section. | ALT TEXT: Spain Location page showing latest campaigns and threat-landscape widgets.]

### Sector pages

<!-- Placeholder: document the redesigned Sector page here when it ships. It follows the same structure as Location pages, with widgets for the most active intrusion sets, most used malware and tools, most used MITRE ATT&CK techniques, and recently exploited vulnerabilities. -->

## Search for observables

### How the search engine works

When searching for observables, Sekoia will investigate the field `x_inthreat_short_display`, a custom attribute that is equal to the main value of the observable (`value` for IP, `name` for organizations, ...).

If the search is a hash, the search engine will consider the number of characters and look for the right hashes.

| Type of Hash | Characters |
| --- | --- |
| MD5 | 32 |
| SHA-1 | 40 |
| SHA-256 | 64 |
| SHA-512 | 128 |

If the search is an IP CIDR, the search engine will look for the IPs contained in it: `185.213.83.0/24` will return `185.213.83.102`, `185.213.83.106`, ...


### Known and unknown observables

If you paste a list of observables in the search bar, chances are Sekoia will recognize some of them, but some may be unknown.

To differentiate between the two, a tab with `Known` and `Unknown` helps understand which observables are in the database and which ones are not.

### Filters

| Filter | Description |
| --- | --- |
| By type | A multiselect to choose types of observables to show in the listing |
| By tags | An autocomplete to filter observables list by tags |
| By sources | Search in more than 200 sources available. This field has autocomplete to help you select sources.  |

### Bulk actions

When you have a list of observables in your search results, you can select two or more of them by ticking the checkbox on the left of the value. Once selected, you can copy their values using the `copy` button that appears on top of the table.

### Tags on observables

The validity of observables is determined by our analysts and indicated by a specific date (valid from, valid until). You can locate this date in the .json file associated with the observable, as well as on the observable's detailed page.

When an observable is accompanied by a **blue tag**, it means that the observable is currently valid.

On the other hand, if an observable is marked with an **orange tag**, it means that the validity date has passed, rendering the observable invalid.
