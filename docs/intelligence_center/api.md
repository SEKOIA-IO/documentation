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

A feed can be consumed by all the users belonging to the community that created it.

### Default Feed

A default feed with no filters is available in all communities without having to create it.

The special feed ID to use is `d6092c37-d8d7-45c3-8aff-c4dc26030608`.

### Feed Creation

The easiest way to create feed configurations is to use the Intelligence Center interface, by clicking on `Feeds` in the left menu. The dropdown next to the feed's name will allow you to copy the ID or the consumption URLs of the feed.

![SEKOIA.IO Intelligence Center Feeds](/assets/intelligence_center/feeds.png){: style="width: 100%; max-width: 100%"}

If you would prefer creating the feed with the API, you can use the [feeds](https://docs.sekoia.io/api/threat%20intelligence%20database#operation/post_feeds_resource) endpoint.

The result should contain the feed `id` that may be used to consume the feed.

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

It is possible to look for a specific indicator of compromise in the Intelligence Center and get its context with the `GET v2/inthreat/indicators/context` endpoint (see [documentation](https://docs.sekoia.io/api/threat%20intelligence%20database#operation/get_indicator_context_resource)).

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

## TAXII

The Intelligence Center also exposes a TAXII 2.1 server that conforms to [the specification](https://docs.oasis-open.org/cti/taxii/v2.1/csprd03/taxii-v2.1-csprd03.html).

The discovery endpoint of the TAXII server is located at `https://app.sekoia.io/api/v2/inthreat/taxii-server/taxii`.
TAXII relies on HTTP Basic Authentication. To authenticate to the TAXII server, you should use your Intelligence Center API key as the Basic Authentication password (you can use any username).

Here is an example of a script using the TAXII endpoints to iterate over objects:

```python
import dbm
import requests
from basicauth import encode as basicauth_encode

# Replace with Intelligence Center API Key
APIKEY = "APIKEY"

# Replace with the TAXII URL copied from the "feeds" page
FEED_URL = "https://app.sekoia.io/api/v2/inthreat/taxii-server/collections/d6092c37-d8d7-45c3-8aff-c4dc26030608/objects"

CURSOR_FILE = "cursor.db"


def get_new_objects(feed_url=FEED_URL, limit=2000, version="2.1"):
    has_more = True
    headers = {
        "Accept": "application/taxii+json",
        "Authorization": basicauth_encode("api", APIKEY),
    }
    parameters = {"match[spec_version]": version, "limit": limit}

    # Use the builtin dbm module to save the cursors to disk
    with dbm.open(CURSOR_FILE, "c") as cursors:
        while has_more:
            # If a cursor exists for this feed, add it to the parameters
            if feed_url in cursors:
                parameters["next"] = cursors[feed_url].decode("ascii")

            # Request the next batch of objects from the API, authenticate with the APIKEY
            response = requests.get(feed_url, headers=headers, params=parameters)
            response.raise_for_status()
            data = response.json()

            has_more = data["more"]
            cursors[feed_url] = data["next"]

            yield from data["objects"]
```
