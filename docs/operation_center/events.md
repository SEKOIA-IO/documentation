# Events Page

The events page enables investigation in the latest events received by SEKOIA.IO using the log list, search bar and filters.

## Log list:

The events page displays a list of latest events received by SEKOIA.IO.

The default columns are:

- Timestamp: Event date
- Event.dialect: Type of intake that sent the event.
- Description: Smart description with clickable links formatted by SEKOIA.IO to show the most important elements and make them easily accessible, such as IP Address, Type or Name.

It is possible to add or remove other columns using the "Show fields" tab by:

- Selecting the desired field in the "Available field" section using the "+" button.
- Selecting the field to remove in "Selected fields" section using the "-" button.
- Typing the desired field name in search bar at the top of "Selected fields".

## Log lines:

Each line of log can be unrolled to show:

- Details: Detailed information retrieved from the log about event once parsed and elements related to the intake and community. These information can be used in the search bar.
- STIX: Event as a STIX bundle that will be used by detection engines.
- Raw event: Event as received by SEKOIA.IO.

## Search bar:

You can search among the list of events by using Dork query langage, for which you can find more information [here](../searching/dork.md).

### Filters:

It is possible to use and combine filters in the search bar by using:

- Smart description: By clicking on the "+" button.
- Details: The query is made on the existing fields in the "details" section by clicking on the "+" button for one of the items.

To go back to the list of logs shown, you need to clear filters and select "Current events"

### Save filters:

It is possible to save a query by clicking on the star icon. 
To check it out, you can click on "Saved queries" then select the wanted period of time and press enter to see the events found.

### Date:

It is possible to select the period of time to be taken in consideration for the search by using:

- Presets: Recommended predefined dates.
- Dates relatives: Earliest and latest moments to select.
- Date ranges: Gap between 2 dates.

### Search history:

Each search has a duration in which the results will be saved in the relative date but when it is expired, you still have the possibility of replaying it using the saved relative date.
