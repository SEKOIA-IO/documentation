# Intelligence Center API

The API is reachable at `https://api.sekoia.io`. All Intelligence Center endpoints start with `https://api.sekoia.io/v2/inthreat/`.

## Authentication

Authentication is required for all API endpoints. Authentication is done with the `Authorization` header:

```
Authorization: Bearer <APIKEY>
```

## Feeds

A feed allows filtering the CTI Objects based on some filters.

The available filters are:

-   Types
-   TLPs
-   Targeted sectors of activity
-   Targeted locations
-   Sources
-   Observable types

A feed can be consumed by all the users belonging to the community that created it.

### Default Feed

A default feed with no filters is available in all communities without having to create it.

The special feed ID to use is `d6092c37-d8d7-45c3-8aff-c4dc26030608`.

### Feed Creation

The easiest way to create feed configurations is to use the Intelligence Center interface, by clicking on `Feeds` in the left menu. The dropdown next to the feed's name will allow you to copy the ID or the consumption URLs of the feed.

![Sekoia.io Intelligence Center Feeds](/assets/intelligence_center/feeds.png){: style="width: 100%; max-width: 100%"}

If you would prefer creating the feed with the API, you can use the `POST v2/inthreat/feeds` endpoint.

The result should contain the feed `id` that may be used to consume the feed.

#### Feed format

When creating a feed it is possible to choose its format.

The available formats are:

- JSON (the default)
- CSV: It is possible to choose which attributes we want to see in the feed
- Text: The content for this format will be a raw text with, on each line, either the name of the object or the observable from the pattern.
- Custom: A template string is needed to specify the way the data must be formatted.
    - The template variables must follow the format: `$name` where `name` is the name of the attribute
    - Example: `ID: $id, name: $name, Observables: $observables`


### Feed Consumption

To consume the objects from a feed the following endpoint may be used: `GET v2/inthreat/collections/{feed_id}/objects`.

i.e. `GET v2/inthreat/collections/d6092c37-d8d7-45c3-8aff-c4dc26030608/objects/`

Be aware that only the users belonging to the feed's community will be able to access it when using a custom feed.

#### Pagination

The `objects` endpoint returns only 100 objects by default but this value can be increased up to 2000 objects per request
with the `limit` parameter.

i.e. `GET v2/inthreat/collections/{feed_id}/objects?limit=2000`

The response contains the STIX Objects in `items` and a pagination cursor in `next_cursor`.
You can pass this cursor using the cursor parameter to get the next page of content.

i.e. `GET v2/inthreat/collections/{feed_id}/objects?limit=2000&cursor={next_cursor}`

For feed using a format that is not JSON (the default), the cursor is located in the `Cursor` HTTP header.

You can safely stop iterating when `items` is empty or less than the requested `limit`.

#### Incremental Updates

It is recommended to only fetch the full feed content the first time and then to use incremental updates.

To get only the records that were created and/or modified since your last request, simply use the last
`next_cursor` that was returned in your request.

#### Filtering by Object Type

It is possible to filter returned objects by type with the `match[type]` parameter.
Its value should be a comma-separated list of types.

i.e. `GET v2/inthreat/collections/{feed_id}/objects?match[type]=indicator`

Note that if the type is not available in the feed it will not be returned even if specified in the query.

#### Filtering on Last Modification Date

The feed entries are sorted by date from the oldest to the youngest. Since Sekoia.io started its default feed in 2019,
the consumer must download a massive amount of data before getting recent intelligence.
We introduced the `modified_after` parameter to help our users consume our feed when they are only interested in recent intelligence. When set, the `modified_after` filters intelligence entries that were created or modified after the specified value.

For example, with `modified_after="2016-04-14T13:07:49.812Z"` only intelligence created or modified after `2016-04-14T13:07:49.812` is returned.

#### Example Script

Here is a sample Python script to fetch STIX objects from the Intelligence Center:

```python
import dbm
import requests
from posixpath import join as urljoin

APIKEY = "APIKEY"

DEFAULT_FEED = "d6092c37-d8d7-45c3-8aff-c4dc26030608"
BASE_URL = "https://api.sekoia.io/v2/inthreat/"
CURSOR_FILE = "cursor.db"


def get_new_objects(feed_id=DEFAULT_FEED, limit=2000):
    url = urljoin(BASE_URL, "collections", feed_id, f"objects?limit={limit}")
    paginated_url = url

    # Use the builtin dbm module to save the cursors to disk
    with dbm.open(CURSOR_FILE, "c") as cursors:
        while True:
            # If a cursor exists for this feed, add it to the URL
            if feed_id in cursors:
                paginated_url = f"{url}&cursor={cursors[feed_id].decode('ascii')}"

            # Request the next batch of objects from the API, authenticate with the APIKEY
            response = requests.get(
                paginated_url, headers={"Authorization": f"Bearer {APIKEY}"}
            )
            response.raise_for_status()
            data = response.json()

            # Yield individual STIX Objects (SDO & SRO)
            for item in data["items"]:
                yield item

            # Update cursor to have incremental updates
            cursors[feed_id] = data["next_cursor"]

            # Stop current iteration if we reached the last updated object
            if not data["items"] or len(data["items"]) < limit:
                break
```

## Getting an indicator's context

When using indicators for detection, you might want to fetch all indicators by using a filter on the indicator type
and then only fetch additional context when an indicator matched.

The `v2/inthreat/objects/{indicator_id}/context` returns a STIX bundle containing:

-   The indicator
-   The first level relationships and related objects
-   Potential relevant Course-Of-Action objects
-   Referenced Sources and Object Markings

## Getting an object by its ID

It is possible to get a specific object by its ID by using the `GET v2/inthreat/objects/{object_id}` endpoint.

For relationships, use the `GET v2/inthreat/relationships/{relationship_id}` endpoint instead.

## Looking for an IOC

It is possible to look for a specific indicator of compromise in the Intelligence Center and get its context with the `GET v2/inthreat/indicators/context` endpoint.


```python
import json
import requests
from posixpath import join as urljoin

APIKEY = "APIKEY"
BASE_URL = "https://api.sekoia.io/v2/inthreat/"

HEADERS = {
    "Authorization": f"Bearer {APIKEY}"
}


def get_indicator_context(observable_type, observable_value):
    response = requests.get(
        urljoin(BASE_URL, "indicators/context"),
        params={"type": observable_type, "value": observable_value},
        headers=HEADERS)
    response.raise_for_status()

    return response.json()
```
