# Filtering

Many API methods accept filtering and matching parameters. A client can request specific content from the Sekoia.io API by specifying a set of filters.

## Match

The `match[<field>]` field parameter can be used to filter documents given the value of a specific `field`. A filter parameter can be specified any number of times, where all filter fields are handed together.

It should be noted that each `field` must not occur more than once. Multiple values of a match parameter are separated by a comma (U+002C COMMA, “,”) without any spaces. If multiple values are present, the match is treated as a logical OR.

**Examples of match parameters**

```
# list alerts triggered on entity entity1 or entity2
/alerts?match[entity_name]=entity1,entity2

# list alerts triggered on entity1 with rule named rule1 or rule2
/alerts?match[entity_name]=entity1&match[rule_name]=rule1,rule2
```

## Date ranges

The `date[field]` parameter can be used to filter documents given a date range on a specific `field`. The value of the parameter must be two dates separated by a comma (U+002C COMMA, ",") without any spaces. The first date is the start date and the second date is the end date.

Example of date range parameter: `date[created_at]=2025-09-22T01:20:00.000Z,2025-09-22T23:59:59.999Z`.

## Pagination

Many Sekoia.io API endpoints return large collections (alerts, assets, rules, events, intelligence objects, …). These endpoints are paginated. Depending on the product area, two main styles are used:

* **Offset / page-based pagination** (most XDR and Operations Center endpoints)
    * Use the `limit` query parameter to control how many items are returned in a single response.
    * Use either a `page` parameter (starting at `page=1`) or an `offset` parameter (starting at `offset=0`) as documented in each endpoint.
    * If you do not specify a `limit`, many endpoints default to **100 items per page**.
    * Each endpoint may define its own **maximum** allowed `limit` (commonly 100 or 1000); requesting more will either be rejected or silently capped by the API.

* **Cursor-based pagination** (Intelligence Center feeds)
    * Endpoints such as `GET /v2/inthreat/collections/{feed_id}/objects` use a **cursor**.
    * The request accepts a `limit` parameter. It returns STIX objects in an `items` field and a pagination cursor in `next_cursor`.
    * To fetch the next page, pass the cursor back using the `cursor` query parameter: `cursor={next_cursor}`.
    * By default, these endpoints return **100 objects** per request, and you can increase this up to **2000 objects** with `limit`.
    * You can safely stop when `items` is empty or when fewer than `limit` items are returned.

For both styles, the safest way to iterate over a complete collection is to **loop until the API returns fewer items than requested**, rather than assuming a fixed number of pages.

**Example – iterating 1,000 items across pages (offset/page-based)**

The example below illustrates how to retrieve up to 1,000 items using `limit=100` and a `page` parameter, stopping early if fewer results are returned:

```python
import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.sekoia.io/v1"

def list_items():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    endpoint = f"{BASE_URL}/sic/conf/rules-catalog/rules"

    all_items = []
    limit = 100
    max_items = 1000

    page = 1
    while len(all_items) < max_items:
        params = {"limit": limit, "page": page}
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        items = data.get("items", data)

        all_items.extend(items)

        # Stop if the API returned less than requested (no more pages)
        if len(items) < limit:
            break

        page += 1

    return all_items[:max_items]

if __name__ == "__main__":
    results = list_items()
    print(f"Fetched {len(results)} items")
```

For cursor-based endpoints, the same pattern applies, but you replace the `page`/`offset` parameter with a `cursor` parameter and update it with the `next_cursor` value returned by the API on each iteration.
