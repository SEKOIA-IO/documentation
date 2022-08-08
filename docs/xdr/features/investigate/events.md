# Events

The events page enables investigation in the latest events received by SEKOIA.IO using a log list, a search bar and multiple filters.

## Log listing

The events page displays a list of the latest events received by [SEKOIA.IO](http://sekoia.io/).

The default columns are:

- `Timestamp`: Event date
- `Event.dialect`: Type of intake that sent the event
- `Description`: Smart description with clickable links formatted by [SEKOIA.IO](http://sekoia.io/) to show the most important elements and make them easily accessible, such as IP Address, Type or Name

It is possible to add or remove other columns using the  `Show fields`  tab by:

- Selecting the desired field in the `Available field` section using the "+" button
- Selecting the field to remove in `Selected fields` section using the "-" button
- Typing the desired field name in the `search bar` at the top of `Selected fields`

### Log lines

Each line of log can be unrolled to show:

- `Details`: Detailed information retrieved from the log about the event once parsed and elements related to the intake and community. These information can be used in the search bar
- `STIX`: Event as a STIX bundle that will be used by detection engines
- `Raw event`: Event as received by [SEKOIA.IO](http://sekoia.io/)

## Search bar

You can search among the list of events by using the `Dork Query Langage`. A complete documentation on how to use this langage is available [here]( dork_language.md).  At most 100k events can be returned by a search, if this number is reached the search has to be narrowed.

### Filters

It is possible to use and combine filters in the search bar. You can do so by:

- Adding `Smart description`:  click on the "+" button
- Adding `Details`: The query is made on the existing fields in the "details" section by clicking on the "+" button for one of the items

To go back to the list of logs shown, you need to clear filters and select "Current events"

### Save filters

It is possible to save a query by clicking on the star icon next to the search bar. The period of time is not saved with it.
To check it out, you can click on "Saved queries" then select the wanted period of time and press enter to see the events found.

### Date

It is possible to select the period of time to be taken into consideration when using a filter. You can use:

- `Presets`: Recommended predefined dates
- `Date relatives`: Select earliest and latest moments
- `Date ranges`: Gap between two dates

Click on the `Apply` button to start your search based on these filters.

### Search history

Each search result lasts 10 min by default and it’s possible to configure the retention to reach one day (24 hours). When the result is expired, you still have the possibility of replaying it using the saved relative date or a new one.

### Sharing a search

Search job have IDs that are available in the browser address bar.

```
<https://app.sekoia.io/operations/events?jobId=2b5ce17f-517e-4dd3-8253-1495a6ba538b>
```

You can share your researches with colleagues by sending them these job IDs, which are accessible within your community.

## Log table
    
### Events enrichment
Event enrichment consists of adding contextualisation data to the standardized event. The objective is to increase the reliability of detection and qualification.

Two sources are used by SEKOIA.IO XDR to systematically enrich each event: [Observables](https://docs.sekoia.io/cti/features/consume/observables/) and the CMDB.

The first source gathers all the technical artefacts, also called observables, collected by SEKOIA.IO analysts during their investigations. Consisting of tens of millions of objects, this database allows us to provide legitimate and/or malicious context to each event. For example, observables are used to geolocate public IP addresses and recognize all legitimate binaries according to Microsoft Windows.

The second source of enrichment relies on a configuration management database (i.e. a CMDB) to provide organization-specific context. The user is invited to consolidate a list of key resources such as brands, users, applications, or hardware present in the organisation. The CMDB is used continuously to contextualise events with information from the associated resources. This contextualisation greatly increases the effectiveness of qualification. 

For example, this enrichment allows you to identify the nature of the legitimate actions expected on an office workstation associated with a specific team in your community. 

You can enable or disable enrichment in logs by clicking on the enable/disable enrichment` in the upper right of the logs table. Depending on your entities, assets and other data, you’ll be able to make sense of your events more efficiently.

### Export the results of a search

You can easily export the results of a search in `CSV` or `JSON` format and choose the fields you want to export.
To do so, click on the button `download`on the upper right of the logs' table.
You can either export all the fiels or export only selected fields.
The export will be made to the default folder defined for downloads. Name of the file is optional, if not provided, the file will be named with the UUID of the job search.

!!! note
    The 'description' field will not be exported.
    
### Toggle value selection

You can toggle values in your logs by clicking on the button `Toggle value selection` in the upper right side of the logs table. 

Go through your events and select values of interest. All similar values will be selected and highlighted in the events list. 

Once you’ve selected these values, you can either perform a search on these values OR create a [Sigma Rule](https://docs.sekoia.io/xdr/features/detect/sigma/) with a pattern based on selected values.

## Aggregation

Aggregation is a new (beta) feature on SEKOIA.IO! 

By using line charts, you can now visualize change in your logs over a continuous range. Visualizing change with a line chart allows the overall trend to be displayed at once, and multiple trends to be compared simultaneously. This new view on the events page can be useful to visualize events during a hunting phase or incident response. 

The aggregation-based hunting feature is often the first step in the journey path taken by the user to [create an anomaly detection rule.](https://docs.sekoia.io/xdr/features/detect/anomaly/) 

Users can now compute aggregations on the results of any search query in the events list. The aggregated values will be displayed over time, depending on the date range chosen. 

To compute aggregations on a list of events, you’ll have to: 

1. Search in your log list by following this [documentation](https://docs.sekoia.io/xdr/features/investigate/events/) 
2. Open the new tab `Aggregation (Beta)` that is accessible on the upper left of the page 
3. Select an aggregation method from the list
4. Select an aggregation field if needed 
5. Click on the `Search` button on the upper right of the page 

### Aggregation methods

- `Average` (only for numerical data): aggregate average of field values per bucket
- `Cardinality` (only for string data): count cardinality of values per bucket
- `Count`: count events per bucket (for a specific filter or field set to a value)
- `Min` (only for numerical data): aggregate min of field values per bucket
- `Max` (only for numerical data): aggregate max of field values per bucket
- `Sum` (only for numerical data): aggregate sum of field values per bucket

### Aggregation graph

Depending on which methods and fields have been selected, a line graph is presented with the event values on the y-axis and the date as defined by the date range on the x-axis. 

For each aggregate the chart displays the first value, last value, minimum, and maximum sorted by timestamp and connects them by one line per variable.

You can hover on the line graph to see the actual value of each point as well as the exact date of the point.

### Create Anomaly Detection rule from the aggregation view

You can create anomaly detection rules directly from this view. 

If you select `count` as aggregation method, a `Create new ruleù button shows up next to the fields and the Rule Creation panel opens up with detection patterns automatically set to Anomaly, and with your events’ query and the chosen aggregation method.
