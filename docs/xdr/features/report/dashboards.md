# Understanding Dashboards: Widgets, data, and Filters

Discover how Dashboards centralize your security data through Widgets and how to manipulate views using time ranges and refresh controls.

## What is a Dashboard?

Dashboards provide a powerful and intuitive way to visualize and monitor key metrics and data in real-time. Users can create customized views by combining various Widgets, offering insights into different aspects of their operations, security posture, or other critical areas.

### Default Dashboard
Accounts on Sekoia.io come with a preconfigured Dashboard that gives a synthetic view of the current community activity, either from:
* **Operational security perspective:** Risk Level, number of alerts, etc.
* **Activity perspective:** List of last posted comments, last created alerts, etc.

## The building blocks: Widgets

A key aspect of Dashboards is the ability to use **Widgets**. These are the individual containers that display data. There are two main types:

* **Built-in Widgets:** Pre-configured tools for common use cases (e.g., Risk Level, Top Threats).
* **Query Builder Widgets:** These enable users to create custom data queries directly within the Dashboard. This allows for highly tailored data analysis and visualization, empowering users to explore specific datasets.

## Interacting with data

### Time range configuration
Managing the time range is essential for analyzing trends.

* **Dashboard date range:** You can synchronize Built-in Widgets with the overall Dashboard's date range using the range selector at the top of the page.
* **Widget-specific time range:** By default, each Widget can display data for its own specific time period. This allows different Widgets to focus on different time frames simultaneously.

> !!! note
    The time period in a custom Query Widget is defined by the Query itself (influenced by data retention). If no specific time filter is applied in the Query, it defaults to 'all time'.

### Refreshing data
By default, the Dashboard shows data computed during the last refresh. The date and time of the last successful refresh are displayed next to the Refresh button.

* **Manual refresh:** Click the **Refresh** button to update all Widgets. (Trigger limit: once every minute).
* **Auto-refresh:** Enable this option in settings to automatically refresh all Widgets every **30 minutes**.

## Sharing Dashboards

Dashboards support collaboration between Managed Security Service Providers (MSSPs) and End Users.
* **For MSSPs:** Custom Dashboards can be shared with End Users directly during the creation or edition process.
* **For End Users:** Shared Dashboards are visible in the community. Users can view them, duplicate them for personalization, and inspect or run the underlying queries.

---
**Next steps**
* Now that you understand the concepts, learn how to [Create and manage Dashboards](#).
* Ready to build? Go to [Configuring Widgets and layout](#).
