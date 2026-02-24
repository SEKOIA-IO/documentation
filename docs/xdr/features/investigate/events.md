# Events

The events page provides a centralized view of your events and enables in depth investigation in the latest logs sent to Sekoia.io.
With its query-based search bar, the possibility to easily add and remove filters and its new aggregation tool, this page lets you sort, filter, analyze and visualize logs in an efficient manner.

In this documentation, we will dive into the different parts that constitute the Events page:

- The [Search bar](#search-bar) and its filtering and sharing options
- The [list of events](#log-listing) and the detailed view of your parsed events
- The mechanism behind [events enrichment](#events-enrichment) or how events are contextualized in Sekoia.io
- The [aggregation](#aggregation) feature and how to create an [anomaly detection rule](#create-anomaly-detection-rule-from-the-aggregation-view) from your query

!!! note
    To send your logs to Sekoia.io, please refer to this [section](https://docs.sekoia.io/integration/ingestion_methods/).

## Search bar

You can search among the list of events by using the dedicated query language. A complete documentation on how to use this language is available [here](events_query_language.md).

Fields you can use to narrow down your events search are listed [here](https://docs.sekoia.io/xdr/features/investigate/querying_events/).

![search-bar-events](/assets/operation_center/events/events-search.png){: style="max-width:100%"}

### Filters

It is possible to further restrict the scope of your events search by using filters. Filters are combined together and with the search query with a logical AND.

You can easily add filters by using the icon buttons provided when hovering over a value inside a `Smart Description` or an event's `Details`:

- Use the `Filter for value` button to only see events with this value
- Use the `Filter out value` button to only see events that DO NOT have this value

You can also add filters manually by clicking on the "Add Filter" icon below the `Search Bar`. The following filter operators are available when creating filters manually:

| Operator | Description |
|----------|-------------|
| `=` | The field must exactly match the value. |
| `exists` | The field must exist. |
| `starts with` | The field must start with the value. *Only for text fields* |
| `ends with` | The field must end with the value. *Only for text fields* |
| `contains` | The field must contain the value. *Only for text fields* |
| `>` | The field must be greater than the specified number. *Only for numerical fields* |
| `>=` | The field must be greater than or equal to the specified number. *Only for numerical fields* |
| `<` | The field must be less than the specified number. *Only for numerical fields* |
| `<=` | The field must be less than or equal to the specified number. *Only for numerical fields* |


![event-filter](/assets/operation_center/events/events-filters.png){ align=right }

Each filter is added as a badge below the `Search Bar`. A filter can be removed by clicking on the `X` at the end of the badge. You can also click on a filter to access a menu that will allow you to:

* Edit the filter
* Invert the filter (filtering out instead of filtering for, or vice versa)
* Temporarily disable or re-enable a filter

To clear current filters, you can use the `Clear all` button at the end of the filters.

### Save search query

It is possible to save a query by clicking the `Star icon` in the search bar. The selected period of time is not saved with it.

![save_query](/assets/operation_center/events/event-save-query.png){ align=right }

To access your saved queries:

1. Click on `Saved queries`(the star button in the top right of the page)
2. Select a period of time
3. Click on `Search` to see your saved query events

    !!! Disclaimer
    The saved queries are stored locally on the user's browser. Ensure that you do not have a task or setting that cleans your browser cookies, as this will result in the loss of your favorite queries.

### Date

It is possible to select the period of time to be taken into consideration when using a filter. You can use:

- `Presets`: Recommended predefined dates
- `Date relatives`: Select earliest and latest moments
- `Date ranges`: Gap between two dates

Click on the `Apply` button to start your search based on these filters.

### Search history


Each events search performed is listed in the `Search History` for 30 days. You can use the search history to easily access past search results.

It is accessible by clicking on the following button (a panel will be displayed with the previous searches)

<!-- image à changer -->
<img width="58" alt="image" src="https://user-images.githubusercontent.com/101662967/187888092-84499da5-6fea-46e3-b21c-e6e859aed8e5.png">

When you are creating a new search, results are available instantly for 30 minutes by default.

![search-history](/assets/operation_center/events/events-search-history.png)

It is possible to configure the retention to reach up to one day (24 hours). After this retention period, you can still replay any events search available in the `Search History` by simply clicking on it. It will trigger a new search using exactly the same parameters (query, filters and date range).

By default, the `Search History` panel is only listing your events search. You can access all events search by clicking on `My Searches` at the top of the panel and selecting `All Searches`.

### Sharing a search

Search Results can be shared with your colleagues by sending them the unique search URL. All users that have access to your community can use this URL to access your search results.

To obtain the search URL, you can:

* Click on the `Share / Link` icon inside the `Search History` panel
* Copy the active URL from the browser address bar

### Histogram

Events histogram appears under the search bar when a query has been made and matches events in the list.

![histogram](/assets/operation_center/events/event-histogram.png){ align=right }

It gives a consolidated view of all matching events in a specific period of time and it highlights the number of events as well as events that are present in alerts.

You can select a date range by clicking on the histogram and dragging the cursor over events you are interested in. This will automatically create a new search and display filtered results. If you want to come back to the previous range, you can use the [search history](#search-history)

## Log listing

![log-listing](/assets/operation_center/events/log-listing.png){: style="max-width:100%"}

The columns by default are:

- `Timestamp`: Event date
- `Event.dialect`: Type of intake that sent the event
- `Description`: Smart description with clickable links formatted by Sekoia.io to show the most important elements and make them easily accessible, such as IP address, type or entity

!!! note
    At most 1 000 events can be displayed in the table. If this number is reached, the search has to be narrowed.

### Show and hide columns

It's possible to show or hide columns in your events table by clicking on the `Show fields & top values` button.

![show-hide-column](/assets/operation_center/events/show-hide-columns.png){: style="max-width:100%"}

Once open, you can add fields that are listed under `available fields` by simply clicking on the "+" button next to them. This will automatically add the column to your table.

If you need to remove a column, there are two ways to do so:

- Hover on the column and a "-" will appear. Click on it and the column will be hidden

- Click on `Show fields & top values` and hover your mouse on the `Selected fields` that you want to hide. Click the "-" that appears and they'll be hidden

You can always find these fields in the `Available fields` section.

!!! tip
    You can also change the order of your columns by dragging them using the icon next to the column's name.

### Log lines

Each line of log can be unrolled to show:

![line-details](/assets/operation_center/events/log-details.png){ align=right }


- `STIX`: Event as a STIX bundle that will be used by detection engines
- `Raw event`: Event as received by Sekoia.io
- `Detail`: Detailed information retrieved from the log after parsing with elements from the event related to the intake and the community.

This table explains the main actions that can be done for each of these fields:

| Action                        | Description                                     |
| ----------------------------- | ----------------------------------------------- |
| Filter for value              | Adds field in the query                         |
| Filter out value              | Removes field in the query                      |
| Toggle column in table        | Adds field as a column in the table             |
| Search events with this value | Opens right panel to search field in all events |
| Copy                          | Copy value of the field                         |

### Adding events to cases

When searching through your event logs, you will often find events valuable to your current investigation. You can add these events to a case to keep track of them and use them as potential pivots.

To add an event to a case:

1. Click on the `Add to Case` icon on the left of the event line.
2. Select the target case or create a new one.

![add-event-to-case](/assets/operation_center/add-event-to-case-events.png){: style="max-width:70%"}

![active-case](/assets/operation_center/cases-in-event.png){ align=right }

After adding an event to a case, you will notice that the selected case becomes active and appears at the top of the events table. Step 2 is no longer necessary: you can now add (or remove) an event to a case with a single click.

To deselect the active case, click on the `X` next to its name.


### Export the results of a search

You can easily export the results of a search in `CSV` or `JSON` format and choose the fields you want to export.
![export-logs](/assets/operation_center/events/export-logs.png){ align=right }

To do so:

1. Click on the button `Export events` on the upper right of the logs' table
2. Either export all fields or only a selection of fields

When you export all fields, even the fields that don't have a value will be exported in a table.

The export will be made to the default folder defined for downloads. Name of the file is optional, if not provided, the file will be named with the UUID of the job search.

!!! note
    The `description` field will not be exported.

!!! note
    At most 1 000 events can be exported if a filter or query is specified. Otherwise only 500 events will be exported. If this number is reached, the search has to be narrowed.

### Toggle value selection

You can toggle values in your logs by clicking on the button `Toggle value selection` in the upper right side of the logs table.

Go through your events and click on values of interest. All similar values will be selected and highlighted in the events list.

Once you’ve selected these values, you can either perform a search on these values OR create a [Sigma Rule](https://docs.sekoia.io/xdr/features/detect/sigma/) with a pattern based on selected values.

![toggle-value-selection](/assets/operation_center/events/toggle-value.png){: style="max-width:100%"}

## Events enrichment

Event enrichment consists of adding contextualization data to the standardized event. The objective is to increase the reliability of detection and qualification.

Two sources are used by Sekoia.io XDR to systematically enrich each event: [Observables](https://docs.sekoia.io/cti/features/consume/observables/) and [Assets](https://docs.sekoia.io/xdr/features/collect/assets/).

The first source gathers all the technical artefacts, also called observables, collected by Sekoia.io analysts during their investigations. Consisting of tens of millions of objects, this database allows us to provide legitimate and/or malicious context to each event. For example, observables are used to geolocate public IP addresses and recognize all legitimate binaries according to Microsoft Windows.

The second source of enrichment relies on a configuration management database (i.e. assets) to provide organization-specific context. The user is invited to consolidate a list of key resources such as brands, users, applications, or hardware present in the organisation. These assets are used continuously to contextualize events with information from the associated resources. This contextualization greatly increases the effectiveness of qualification.

For example, this enrichment allows you to identify the nature of the legitimate actions expected on an office workstation associated with a specific team in your community.

You can enable or disable enrichment in logs by clicking on the `enable/disable enrichment` in the upper right of the logs table.
Depending on your entities, assets and other data, you’ll be able to make sense of your events more efficiently.

To see the value of enriched values, click on the enriched field and you'll be provided with additional context.

!!! note
    If the value exists in the Intelligence Center, tags associated with the value in question will be added as additional context.


## Aggregation

Aggregation is a new (beta) feature on Sekoia.io!

By using line charts, you can now visualize change in your logs over a continuous range. Visualizing change with a line chart allows the overall trend to be displayed at once, and multiple trends to be compared simultaneously. This new view on the events page can be useful to visualize events during a hunting phase or incident response.

The aggregation-based hunting feature is often the first step in the journey path taken by the user to [create an anomaly detection rule.](https://docs.sekoia.io/xdr/features/detect/anomaly/)

Users can now compute aggregations on the results of any search query in the events list. The aggregated values will be displayed over time, depending on the date range chosen.

To compute aggregations on a list of events, you’ll have to:

1. Search in your log list by following this [documentation](https://docs.sekoia.io/xdr/features/investigate/events/)
2. Open the new tab `Aggregation (Beta)` that is accessible on the upper left of the page
3. Select an aggregation method from the list
4. Select an aggregation field if needed
5. Click on the `Search` button on the upper right of the page

!!! note
    Aggregation view feature does not support the field `alert_short_ids`.


### Aggregation methods

- `Average` (only for numerical data): aggregate average of field values per bucket
- `Cardinality` (only for string data): count cardinality of values per bucket
- `Count`: count events per bucket (for a specific filter or field set to a value)
- `Min` (only for numerical data): aggregate min of field values per bucket
- `Max` (only for numerical data): aggregate max of field values per bucket
- `Sum` (only for numerical data): aggregate sum of field values per bucket

### Aggregation graph

Depending on which methods and fields have been selected, a line graph is presented with the event values on the y-axis and the date as defined by the date range on the x-axis.

![aggregation-graph](/assets/operation_center/events/aggregation-graph.png){: style="max-width:100%"}

For each aggregate the chart displays the first value, last value, minimum, and maximum sorted by timestamp and connects them by one line per variable.

You can hover on the line graph to see the actual value of each point as well as the exact date of the point.

### Create Anomaly Detection rule from the aggregation view

![create-rule](/assets/operation_center/events/create-rule.png){ align=right }

You can create anomaly detection rules directly from this view.

If you select `count` as aggregation method, a `Create new rule` button shows up next to the fields and the Rule Creation panel opens up with detection patterns automatically set to Anomaly, and with your events’ query and the chosen aggregation method.

Learn more about Anomaly Detection rules in [this section](https://docs.sekoia.io/xdr/features/detect/anomaly/).
