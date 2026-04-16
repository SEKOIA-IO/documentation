# Find Observables

Use the search to find indicators and other observable values in the Intelligence database. This page explains how the search engine works, how it handles hashes and IP CIDRs, how to distinguish known vs unknown observables, and how to filter and take bulk actions on them.

### Search basics <a href="#how-the-search-engine-works" id="how-the-search-engine-works"></a>

When you search for observables, Sekoia uses the custom attribute `x_inthreat_short_display`. This field contains the main value of the observable, such as the IP address for an IP, the name for an organization, and so on.

#### Searching for hashes <a href="#searching-for-hashes" id="searching-for-hashes"></a>

If your search term is a hash, the engine checks the number of characters and matches the appropriate hash type based on the following reference:

| Type of hash | Characters |
| ------------ | ---------- |
| MD5          | 32         |
| SHA‑1        | 40         |
| SHA‑256      | 64         |
| SHA‑512      | 128        |

For example, a 32‑character string is interpreted as an MD5 hash, a 40‑character string as SHA‑1, and so on.

#### Searching for IP CIDRs <a href="#searching-for-ip-cidrs" id="searching-for-ip-cidrs"></a>

If your search term is an IP CIDR, Sekoia returns all IPs contained in that range.

{% hint style="info" %}
Searching for `185.213.83.0/24` will return observables such as `185.213.83.102`, `185.213.83.106`, etc.
{% endhint %}

### Known and unknown observables <a href="#known-and-unknown-observables" id="known-and-unknown-observables"></a>

When you paste a list of observables in the search bar, Sekoia may recognize some of them, while others may be unknown.

A **Known / Unknown** tab helps you distinguish which observables are already in the database and which ones are not:

* **Known** observables are entries that exist in the Intelligence database.
* **Unknown** observables are not (yet) in the database.

Use this distinction to quickly see which observables can be immediately investigated and which ones may need further enrichment.

***

### Filters <a href="#filters" id="filters"></a>

You can refine the list of observables with filters. Each filter appears as a tag above the table.

The table below lists the available observable filters:

<table><thead><tr><th width="136">Filter</th><th>Description</th></tr></thead><tbody><tr><td>By type</td><td>Multiselect filter to choose which types of observables to show (e.g., IP addresses, domains, URLs, file hashes).</td></tr><tr><td>By tags</td><td>Autocomplete filter to show only observables with specific tags.</td></tr><tr><td>By sources</td><td>Search across more than 200 sources. This field includes autocomplete to help you select sources.</td></tr></tbody></table>

{% hint style="info" %}
To remove a filter, click the **X** on the tag. To remove all filters, click **Clear filters** next to the tag list or at the bottom of the filters panel.
{% endhint %}

***

### Bulk actions <a href="#bulk-actions" id="bulk-actions"></a>

When the search returns a list of observables, you can:

1. Select two or more observables by ticking the checkbox on the left of each value.
2. Use the **Copy** button that appears above the table to copy the values of all selected observables.

This is useful for:

* Sharing observables with other teams.
* Copying indicators into playbooks, detection rules, or external tools.

### Tags on observables <a href="#tags-on-observables" id="tags-on-observables"></a>

The validity of observables is determined by our analysts and indicated by validity dates:

* **Valid from**
* **Valid until**

You can see these dates in the `.json` file associated with the observable and on the observable’s detailed page.

### Validity status <a href="#validity-status" id="validity-status"></a>

On the table, observables are visually marked as:

* **Blue tag**: The observable is currently valid.
* **Orange tag**: The validity period has passed; the observable is no longer considered valid.

Use these tags to prioritize actions on observables that are still relevant and to understand which ones should be treated as historical.

