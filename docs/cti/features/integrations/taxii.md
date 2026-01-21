# TAXII

The Intelligence Center also exposes a TAXII 2.1 server that conforms to [the specification](https://docs.oasis-open.org/cti/taxii/v2.1/csprd03/taxii-v2.1-csprd03.html).

The discovery endpoint of the TAXII server is located at `https://app.sekoia.io/api/v2/inthreat/taxii-server/taxii2`.
The API root of the TAXII server is located at `https://app.sekoia.io/api/v2/inthreat/taxii-server`.
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
