# Built-in widgets reference

A comprehensive catalog of pre-configured Widgets available in Sekoia.io and details on the Risk Level calculation.

## Widget categories

Built-in Widgets are designed to provide immediate access to critical data without custom configuration. They are organized into:

* **Investigate:** For exploring specific data points, threats, or entities.
* **Observe:** For monitoring ongoing activities, trends, and metrics.

## List of built-in widgets

### Alerts and cases
* **Alerts / Cases:** Displays the list and details of alerts or cases.
* **Number of alerts / Cases:** Shows the total count over a specified period.
* **Last comments:** Lists the most recent comments associated with alerts.
* **Risk level:** Summarizes current risk (see calculation below).

### Threat Intelligence
* **Top observed threats / Adversaries:** Highlights frequently observed threats and prominent adversaries.
* **Adversaries activity trend:** Tracks adversary activities over time.
* **Latest intelligence / FLINTs:** Shows recent intelligence reports and FLINTs produced by Sekoia.
* **Malware prevalence trends:** Tracks trends in malware prevalence.
* **Global top threats:** Lists the most referenced threats in the intelligence database.
* **Object count / Top objects:** Counts and references for intelligence objects.

### Entities and context
* **Entities overview:** High-level summary of all tracked entities and metrics.
* **Statistics by entity:** Displays statistical data for each entity.
* **Events by data sources:** Breaks down events by their source.
* **Events activity:** Reports the overall number of collected events.
* **Top sectors / Locations:** Highlights sectors and geographic locations referenced in the intelligence database.
* **Top 5 known exploited vulnerabilities:** Lists critical vulnerabilities currently being exploited.

## Risk Level calculation

The **Risk level widget** shows the Risk Level of your infrastructure (normalized between 0 and 100).

1.  **Scope:** It considers all **opened** alerts (pending, acknowledged, or ongoing) from the last **30 days**.
2.  **Weighting:** Each alert is weighted based on **urgency**, **occurrence**, and **date** (giving more importance to recent, urgent, and recurrent alerts).
3.  **Aggregation:** The Risk Level is computed **by entity**.
4.  **Community level:** The maximum Risk Level among all entities is displayed as the community Risk Level.

---
**Next steps**

* Go back to [Understanding Dashboards](/xdr/features/report/dashboards.md) for a refresher on concepts.
