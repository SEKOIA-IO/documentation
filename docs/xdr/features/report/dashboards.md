# Dashboards

Dashboards provide a powerful and intuitive way to visualize and monitor key metrics and data in real-time.
Users can create customized views by combining various widgets, offering insights into different aspects of their operations, security posture, or other critical areas.

A key aspect of dashboards within Sekoia is the ability to use queries, which enable users to create custom data queries directly within the dashboard. This allows for highly tailored data analysis and visualization, empowering users to explore specific datasets and derive insights that are most relevant to their needs.

With features like time range configuration, manual and automatic data refresh, and the flexibility to add and customize widgets, dashboards are designed to deliver actionable information at a glance. Whether you need to track trends, spot anomalies, or perform detailed data analysis, dashboards offer a versatile and user-friendly solution.

## Dashboards listing 
The Dashboards Listing page is your central hub for managing and accessing all your dashboards. Designed for clarity and efficiency, it provides a comprehensive overview of every dashboard you or your community has created.
On this page, you'll see a table with the following information for each dashboard:

- Name: The title of the dashboard
- Last Edition: The date and time the dashboard was last modified
- Modified By: The user who last made changes to the dashboard
- Created By: The user who originally created the dashboard
- Number of Widgets: The total count of widgets included in the dashboard

### Filtering and sorting
To help you quickly find the dashboards you need, the Dashboards Listing page offers robust filtering and sorting options:

**Filters**

- All community dashboards: View every dashboard accessible within your Sekoia community
- Personal dashboards (Created by me): Filter to only display dashboards you have personally created

**Sort**

- A-Z: Arrange dashboards alphabetically by name
- Last edition: Sort dashboards by their most recent modification date (newest to oldest)

### Create new dashboard 
You can easily create a new dashboard directly from the Dashboards Listing page. Look for a `+New Dashboard` button and start building your custom view. 

Note that dashboards you create will be available to all members of your community.

### Duplicate dashboard 
To duplicate a dashboard:

1. Navigate to the Dashboards Listing page
2. Locate the dashboard you wish to duplicate
3. Click on `...` button and select "Duplicate" action associated with that dashboard
4. This will automatically duplicate the dashboard with all the queries within it

### Delete dashboard 
To delete a dashboard:

1. Navigate to the Dashboards Listing page
2. Locate the dashboard you wish to delete
3. Click on `...` button and select "Delete" action associated with that dashboard
4. This will automatically the dashboard for all members of the community


### Set dashboard as homepage 
You can set any dashboard from your listing as your default Sekoia homepage. This means that every time you log in, you'll land directly on your preferred dashboard, giving you instant access to the information most critical to your role.

To set a dashboard as your homepage:

1. Navigate to the Dashboards Listing page
2. Locate the dashboard you wish to set as your homepage
3. Click on `...` button and select "Set as Homepage" action associated with that dashboard
4. Once set, this dashboard will load automatically upon your next login. You can change your default homepage at any time

## Default Dashboard
Accounts on Sekoia.io come with a preconfigured dashboard that gives a synthetic view of the current community activity, either from an operational security perspective (risk level, number of alerts, etc.) or from an activity perspective (list of last posted comments, last created alerts, etc.).

## Time Range
Managing the time range for data displayed in your dashboard is essential for analyzing trends and patterns over specific periods.
The dashboard offers flexible options for configuring the time range for each widget and the overall dashboard.

**Widget-Specific Time Range**

By default, each widget on the dashboard can be configured to display data for its own specific time period. This allows for detailed analysis where different widgets may focus on different time frames simultaneously.
Each widget clearly shows the time range it is considering, ensuring transparency in the data being presented.

**Dashboard Date Range**

For built-in widgets, there's an option to synchronize the widget's time range with the overall dashboard's date range. This feature is particularly useful when you want multiple widgets to reflect data over the same period.
The dashboard's overall date range can be set using the range selector, which is prominently displayed at the top of the dashboard. Adjusting this selector updates the time range for all built-in widgets that are configured to follow the dashboard's date range.

By configuring these settings, you can ensure that your dashboard provides the most relevant and consistent view of data, tailored to the specific time periods that matter most to your analysis.

## Refreshing Data
Ensuring that the data displayed on your dashboard is up-to-date is critical for accurate monitoring and analysis.
The dashboard provides several options for refreshing the data presented in the widgets.

By default, the dashboard shows data that was computed during the last refresh. This means that when you first view a dashboard, the information is based on the most recent refresh that occurred.

To manually refresh the data across all widgets on the current dashboard, click the `Refresh` button located near the top of the dashboard.
Note that you can only trigger a manual refresh once every minute.

The date and time of the last successful refresh are displayed next to the `Refresh` button, allowing you to quickly verify when the data was last updated.

If you prefer to have your dashboard's data updated automatically, you can enable the auto-refresh option in the dashboard settings.
When auto-refresh is enabled, all widgets on the dashboard will automatically refresh every 30 minutes. This ensures that your data stays current without the need for manual intervention.

These options allow you to maintain the most relevant data on your dashboard, whether you prefer manual control or automated updates.



## Add, edit and organize widgets

Dashboards can be easily customized using a variety of widgets, allowing users to tailor the interface to their specific needs.

### Add widgets

To add widgets to your dashboard, click on the `Add New Widget` button located in the top right corner of the screen. From the panel, select the desired widgets from the available queries and presets.

### Edit widgets

To edit an existing widget, click the `three dots` in the upper right corner of the widget, and then select **Edit Widget**.

- If the widget is a **query visualization**, you will be redirected to the query settings page, where you can edit the query parameters as needed.
- If the widget is a **preset** from the widgets' library, the editing panel will appear, allowing you to adjust options such as the time range or visualization type.

### Reorganize widgets

To reorganize the layout of widgets on your dashboard, click the `Edit button` in the top right corner of the screen. This mode enables you to change both the position and size of each widget. You can easily drag and drop widgets to your preferred locations. Don’t forget to click `Save` to apply your changes!

### Remove widgets
To remove widgets from your dashboard, click the `three dots` and select **Delete from dashboard**.

## Query Builders Widgets

Query builders can be inserted into dashboards to streamline data visualization and management. It allows you to easily integrate existing query builders into multiple dashboards, ensuring that any updates made to a query on the query page are automatically reflected across all dashboards where it is used. By leveraging this integration, you maintain consistency and reduce the need for manual updates, enhancing the efficiency and accuracy of your data visualizations.

The Query widget in the dashboard utilizes the visualization settings saved with the query builder on the query page. For detailed information on how visualizations are managed, refer to the [documentation of Query Builders](/xdr/features/investigate/query_builder.md).

Changes made to a query builder on the query builder page are automatically propagated to all dashboards that use that query builder. It ensures that updates are reflected without requiring manual intervention.
On the query builder’s edit page, you can view a list of all dashboards utilizing the query builder. This helps track where changes will take effect.

![insert_qb_in_dashboard](/assets/xdr/dashboards/insert_qb_in_dashboard.gif){: style="max-width:100%"}

!!! Note
    The time period in a query is defined by the Query itself, which is influenced by the retention period of the data. If no specific time filter is applied in the Query, it will default to 'all time'.


## Filters in Dashboards

Filters make dashboards interactive and dynamic, allowing analysts to adjust displayed data without editing the underlying queries.
They act as shared controls that can instantly update multiple widgets and queries across a dashboard.

With filters, dashboards become context-aware, focusing on a specific time range, entity, process name, or other investigation criteria with a single click.

### What Are Filters

Filters are dynamic inputs that allow users to modify the behavior of queries in real time.
Each filter is referenced in a SOL query using the syntax:

```shell
?filter_name
```

For example

```shell
events
| where timestamp between (?time.start .. ?time.end)
| where entity_uuid == ?entity_uuid
| where process.name == ?process_name
```

In this example:

* `?time.start` and `?time.end` are predefined time filters
* `?entity_uuid` and `?process_name` are custom filters defined by the query author

All these filters appear automatically in the dashboard, allowing users to modify them and instantly refresh the results.


### Pinning Filters to the Dashboard

When a widget’s query includes filters (for example `?entity_uuid` or `?process_name`), you can pin those filters to the dashboard so that all widgets referencing the same filter name stay synchronized.

Pinned filters appear in the dashboard filter bar, allowing users to interact with them directly from the dashboard view.

#### How to Pin a Filter

To pin a filter to a dashboard:

1. Open your dashboard.
2. Click the Edit dashboard button in the top-right corner to enter edit mode.
3. In the widget's panel, locate and click on the pin icon next to the filter you want to pin.
4. Save the dashboard and exit edit mode.

Once pinned, the filter appears at the top of the dashboard as a shared input control.

#### Behavior of Pinned Filters

* A pinned filter automatically synchronizes all widgets using the same filter name.
* When a user changes the pinned filter’s value, all linked widgets refresh instantly.
* If a widget uses a filter that isn’t pinned, it retains its own local filter configuration.
* Unpinning a filter removes it from the dashboard’s filter bar but keeps widgets functional with their local values.


## Built-in Widgets

Dashboards come equipped with a variety of built-in widgets designed to provide immediate access to critical data and insights.
These widgets are pre-configured for common use cases, allowing users to quickly add valuable information to their dashboards without the need for custom queries or extensive configuration.

The built-in widgets are organized into categories to help users easily find the tools they need:

* **Investigate**: These widgets focus on exploring specific data points, threats, or entities, helping users drill down into detailed analyses.
* **Observe**: These widgets are designed for monitoring and tracking ongoing activities, trends, and metrics across the threat landscape.

### List of Built-in Widgets

Here is an overview of the built-in widgets available:

* `Alerts` displays the number and details of alerts.
* `Number of Alerts` shows the total count of alerts over a specified time period.
* `Risk Level` provides a summary of the current risk levels based on recent data.
* `Last Comments`
    lists the most recent comments associated with alerts.
* `Top Observed Threats`
    highlights the most frequently observed threats.
* `Top Observed Adversaries`
    displays a list of the most prominent adversaries identified.
* `Cases`
    provides an overview of cases being tracked.
* `Number of Cases`
    shows the total count of cases.
* `Assets`
    displays data related to assets being monitored.
* `Events by Data Sources`
    breaks down events according to their data sources.
* `Events Activity`
    reports the overall number of collected events
* `Entities`
    Provides information about entities involved in alerts or cases.
* `Entities Overview`
    Offers a high-level summary of all tracked entities and their metrics.
* `Statistic by Entity`
    Displays statistical data for each entitiy.
* `Latest Intelligence`
    Shows the most recent intelligence reports and findings.
* `Adversaries Activity Trend`
    Tracks trends in adversary activities over time.
* `Object Count`
    Provides a count of intelligence objects in the intelligence database.
* `Top 5 Known Exploited Vulnerabilities`
    Lists the most critical vulnerabilities currently being exploited.
* `Latest FLINTs Reports`
    Displays the latest FLINTs (threat intelligence reports) produced by Sekoia.
* `Malware Prevalence Trends`
    Tracks trends in malware prevalence.
* `Top Objects`
    Shows the most frequently referenced intelligence objects.
* `Top Sectors`
    Highlights the sectors most referenced in the intelligence database.
* `Top Locations`
    Displays geographic locations most referenced in the intelligence database.
* `Global Top Threats`
    Lists the most referenced threats in the intelligence database.

These built-in widgets allow users to quickly assemble a comprehensive dashboard that reflects key aspects of their environment, making it easier to monitor, investigate, and respond to critical data points.

### Risk Level Widget

The Risk Level Widget shows the risk level of your infrastructure based on your alerts.

The risk level is computed by entity. The maximum risk level is then considered to be the community risk level.

All the opened (i.e. in status pending, acknowledged, or ongoing) alerts seen in the last 30 days are taken into consideration to calculate the risk level.
Then, for each alert, we apply some weighting based on the urgency, occurrence, and date of the alert.
The goal is to give more importance to the more recent, urgent, and recurrent alerts.

The Risk Level value is normalized to provide a number between 0 and 100.
