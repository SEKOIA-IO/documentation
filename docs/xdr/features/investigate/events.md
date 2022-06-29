# Events

The events page enables investigation in the latest events received by SEKOIA.IO using a log list, a search bar and multiple filters.

## Log list

The events page displays a list of the latest events received by [SEKOIA.IO](http://sekoia.io/).

The default columns are:

- `Timestamp`: Event date
- `Event.dialect`: Type of intake that sent the event
- `Description`: Smart description with clickable links formatted by [SEKOIA.IO](http://sekoia.io/) to show the most important elements and make them easily accessible, such as IP Address, Type or Name

It is possible to add or remove other columns using the  `Show fields`  tab by:

- Selecting the desired field in the `Available field` section using the "+" button
- Selecting the field to remove in `Selected fields` section using the "-" button
- Typing the desired field name in the `search bar` at the top of `Selected fields`

## Log lines

Each line of log can be unrolled to show:

- `Details`: Detailed information retrieved from the log about the event once parsed and elements related to the intake and community. These information can be used in the search bar
- `STIX`: Event as a STIX bundle that will be used by detection engines
- `Raw event`: Event as received by [SEKOIA.IO](http://sekoia.io/)

## Search bar

You can search among the list of events by using the `Dork Query Langage`. A complete documentation on how to use this langage is available [here](https://docs.sekoia.io/searching/dork/).  

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

## Export the results of a search

You can easily export the results of a search in `CSV` or `JSON` format and choose the fields you want to export. 
To do so, click on the button `download`on the upper right of the logs' table. 
You can either export all the fiels or export only selected fields. 
The export will be made to the default folder defined for downloads. Name of the file is optional, if not provided, the file will be named with the UUID of the job search.

!!! note
    The 'description' field will not be exported.
