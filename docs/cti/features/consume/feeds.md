# Outgoing Feeds
A feed allows you to filter CTI objects from your database.

## Feeds listing

The feeds’ page is accessible in the main menu. The page lists all feeds that are available to your community and the table has columns based on our available filters.

The available filters are:

- Types
- TLPs
- Targeted sectors of activity
- Targeted locations
- Sources
- Observable types

A feed can be consumed by all users belonging to the community that creates it.

## Consume a feed

To consume a feed, you have to click on the dropdown icon next to the name of the feed in the first column of the table.

You can then:

- Copy the feed ID
- Copy the API URL
- Copy the TAXII URL

## Feed format

When creating a feed, you have different formats to choose from.

The available formats are:

- **JSON**: The default format
- **CSV**: It is possible to choose which attributes you want to see in the feed
- **Text**: The content for this format will be a raw text with, on each line, either the name of the object or the observable from the pattern.
- **Custom**: A template string is needed to specify the way the data must be formatted.
    - The template variables must follow the format: `$name` where `name` is the name of the attribute
    - Example: `ID: $id, name: $name, Observables: $observables`

### Default Feed

A default feed with no filters is available in all communities without having to create it.

The special feed ID to use is `d6092c37-d8d7-45c3-8aff-c4dc26030608`.

### Create new feed

There are two ways to create a feed: either from the TIP interface or by using the `POST /api/v2/inthreat/feeds` API endpoint.

To create a new feed:

1. Click on the `+ Feed` button on the right of the page
2. Provide a title (mandatory)
3. Select objects type, observables type, sectors, TLP, sources, etc... based on your preferences
4. Choose a feed format
5. Save your changes

!!! note
    Filter categories are combined together with a logical AND. Different values in the same filter category are combined together with a logical OR. This means you can define a feed with values matching ((Locations: France OR Germany) AND (Sectors: Financial Services OR Industrial).

### Edit a feed

To edit an existing feed:

1. Go to the feeds’ listing page
2. Select the feed you want to edit or delete
3. Click on the `edit` button in the right of the table
4. Edit your feed
5. Save your changes

### Delete a feed

To delete an existing feed:

1. Go to the feeds’ listing page
2. Select the feed you want to delete
3. Click on the `delete` button in the right of the table
4. Confirm deletion in the modal

!!! note
    Beware, deleting a feed is a permanent action as you will not be able to access or edit it afterwards.
