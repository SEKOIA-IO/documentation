# Find Objects

Use the Intelligence page to search and filter cyber threat intelligence objects. This page explains how the search engine works, how to target specific sectors and countries, and how to customize the table layout and filters.

### Search basics <a href="#search-basics" id="search-basics"></a>

When you search for one or more terms, Sekoia lists objects whose fields match the query. The search engine uses the following fields:

* Name.
* Description.
* Aliases.
* Content of a report.
* External references.
* Location country code (if the search term contains 2 characters).

Results are sorted by pertinence by default. You can also sort by the last edition date.

### Exact matching <a href="#exact-matching" id="exact-matching"></a>

If your search contains multiple words, wrap the query in quotes to find objects containing the exact term in one of their fields.

Example: `"FLINT 2026-04"`

### Tokenized search <a href="#tokenized-search" id="tokenized-search"></a>

The search bar is tokenized. For example, `FLINT 2026-04` is split into `FLINT`, `2026`, and `04`. The engine then scores results based on where each term is found and how often it appears.

To return only the item whose name starts with `FLINT 2022-05`, use this dork:

`name:^"FLINT 2026-04"`

### Targeting specific data <a href="#targeting-specific-data" id="targeting-specific-data"></a>

#### Search for specific sectors <a href="#search-for-specific-sectors" id="search-for-specific-sectors"></a>

In STIX, a **Sector** is an Identity object representing a business sector or industry. It is used to contextualize threat actors, campaigns, and other CTI entities by their targeting.

Examples include Finance, Healthcare, and Government.

The table below lists the sectors and their sub‑types.

| Sector                      | Sub‑types                                                                                                                                                                                                                                                       |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Defence                     | Defence‑Military, Defence‑Industry                                                                                                                                                                                                                              |
| Education                   | Education‑R\&D, Education‑Institutions                                                                                                                                                                                                                          |
| Energy                      | Energy‑Electricity, Energy‑Renewable, Energy‑Gas, Energy‑Nuclear, Energy‑Transportation, Energy‑Oil                                                                                                                                                             |
| Entertainment               | Entertainment‑Gaming, Entertainment‑Culture, Entertainment‑Gambling, Entertainment‑Sport                                                                                                                                                                        |
| Financial‑Services          | Financial‑Services‑Real Estate, Financial‑Services‑Cryptocurrencies, Financial‑Services‑Insurance                                                                                                                                                               |
| Government                  | Government‑Education, Government‑Interior, Government‑Local, Government‑Regional, Government‑Foreign Affairs, Government‑Justice, Government‑Intelligence and Security Services, Government‑National, Government‑Defence                                        |
| Healthcare                  | Healthcare‑Pharmaceuticals, Healthcare‑R\&D, Healthcare‑Equipment, Healthcare‑Hospital                                                                                                                                                                          |
| Hospitality                 | Hospitality‑Leisure                                                                                                                                                                                                                                             |
| Industry                    | Industry‑Semiconductor, Industry‑Food and Beverage, Industry‑Pharmacy, Industry‑Agrobusiness, Industry‑Agriculture, Industry‑Wholesale, Industry‑Manufacturing, Industry‑Mining, Industry‑Construction, Industry‑Retail, Industry‑Chemical, Industry‑Automotive |
| Infrastructure              | Infrastructure‑Critical                                                                                                                                                                                                                                         |
| Legal                       | —                                                                                                                                                                                                                                                               |
| Media                       | Media‑Social Network, Media‑Individual, Media‑TV Channel, Media‑Radio, Media‑Newspaper                                                                                                                                                                          |
| NGO/Civil‑Society/Political | NGO/Civil‑Society/Political‑Dissident, NGO/Civil‑Society/Political‑Activist                                                                                                                                                                                     |
| Professional services       | Professional services‑Consulting, Professional services‑Management, Professional services‑Printing, Professional services‑Marketing                                                                                                                             |
| Technology                  | Technology‑High‑Tech, Technology‑Services                                                                                                                                                                                                                       |
| Telecommunications          | Telecommunications‑Satellite, Telecommunications‑Phone, Telecommunications‑Internet                                                                                                                                                                             |
| Transportation              | Transportation‑Shipping, Transportation‑Air, Transportation‑Road, Transportation‑Maritime, Transportation‑Rail                                                                                                                                                  |

{% hint style="info" %}
Media is a subtype of Entertainment.
{% endhint %}

{% hint style="info" %}
Select **Identity** in the **By object type** filter at the top of the Intelligence table to show only Identity objects.
{% endhint %}

#### Search for a country <a href="#search-for-a-country" id="search-for-a-country"></a>

In STIX, a **Country** is a Location object representing a geographical region, civic address, or latitude/longitude. Countries are used to contextualize threat actors, campaigns, and other CTI entities by their geographic targeting.

You can search for country‑related intelligence in two ways:

* Search by the country name in English.
* Use the 2‑letter country code from the ISO 3166‑1 reference, such as `FR` for France, `AE` for United Arab Emirates, or `NG` for Nigeria.

### Reading and organizing results <a href="#reading-and-organizing-results" id="reading-and-organizing-results"></a>

#### Table columns <a href="#table-columns" id="table-columns"></a>

Search results appear in a table with multiple columns. You can show or hide columns via the filters panel and change their order by dragging the column handle.

By default, the table shows:

| Column              | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| TLP                 | Sensitivity level (White, Green, Amber, Red).                         |
| Type                | Type of object. Hover the icon to see the object type.                |
| Name                | Name of the object. Hover to read the full name.                      |
| Sub‑types           | Some objects have sub‑types, such as indicators, malware, or reports. |
| Confidence          | Confidence level assigned by Sekoia.                                  |
| Sources             | Source of the object.                                                 |
| Last edited         | Date of last edition.                                                 |
| Created             | Date of creation.                                                     |
| Labels              | Custom labels added from Sekoia.                                      |
| Global telemetry    | Observed telemetry in all Sekoia clients.                             |
| Workspace telemetry | Observed telemetry in the actual Workspace.                           |

{% hint style="info" %}
To s**how or hide columns**, click the column icon at the top right of the table and select the ones you need.
{% endhint %}

#### Pagination <a href="#pagination" id="pagination"></a>

The table is set to **25 results per page** by default. You can change it to **10, 15, 50, or 100** depending on your screen size and needs.

#### Revoked objects <a href="#revoked-objects" id="revoked-objects"></a>

If an object name appears in **red**, the object has been revoked.

***

### Filtering objects <a href="#filtering-objects" id="filtering-objects"></a>

You can refine results in the Intelligence table with multiple filters. Each filter appears as a tag above the table.

The table below lists the available object filters.

| Filter           | Description                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------- |
| Type             | Multiselect filter to choose which object types to display.                                                |
| Source           | Search across more than 200 sources (with autocomplete).                                                   |
| Feed             | Show only objects that match a feed created in the Feeds page.                                             |
| Confidence level | Show only objects equal to, higher than, lower than, or within a range of confidence levels.               |
| Observable type  | Restrict indicators to those whose pattern contains the selected observable types.                         |
| Is a source      | Show only identities that are sources of other objects.                                                    |
| Last update      | Filter objects updated in the last hour, last 24 hours, last 7 days, last 30 days, this year, or all time. |
| Creation date    | Filter objects created in the last hour, last 24 hours, last 7 days, last 30 days, this year, or all time. |
| TLP              | Show only objects with a certain TLP.                                                                      |

{% hint style="info" %}
To remove a filter, click the **X** on the tag. To remove all filters, click **Clear filters** next to the tag list or at the bottom of the filters panel.
{% endhint %}
