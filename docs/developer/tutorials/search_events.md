# Search events

Event searches can take time to process. The Sekoia.io API handles this with an asynchronous **search job**: you create a job, poll its status, and retrieve results once it is done.

## Prerequisites

- A valid API key with the `SIC_READ_INTAKES` permission
- Python 3.10 or later

## How it works

The workflow involves three steps:

1. **Create a search job** — submit your query and time window, get back a job `uuid`
2. **Poll the job status** — check until the job is done
3. **Retrieve the events** — fetch results when status is `2` (done)

Job statuses:

| Status | Meaning |
| --- | --- |
| `0` | Not started |
| `1` | In progress |
| `2` | Done |
| `3` | Canceled |
| `4` | Failed |

## Python script

```python
#!/usr/bin/env python3
import argparse
import json
import logging
from time import sleep

import requests

BASE_URL = "https://api.sekoia.io/v1"


def create_search_job(apikey: str, earliest: str, latest: str, query: str) -> str:
    body = {
        "term": query,
        "earliest_time": earliest,
        "latest_time": latest,
        "term_lang": "dork",
    }
    response = requests.post(
        f"{BASE_URL}/sic/conf/events/search/jobs",
        headers={"Authorization": f"Bearer {apikey}"},
        json=body,
    )
    response.raise_for_status()
    return response.json()["uuid"]


def wait_for_job(apikey: str, job_uuid: str, retries: int = 10) -> int:
    for _ in range(retries):
        response = requests.get(
            f"{BASE_URL}/sic/conf/events/search/jobs/{job_uuid}",
            headers={"Authorization": f"Bearer {apikey}"},
        )
        response.raise_for_status()
        status = response.json()["status"]
        if status in (2, 3, 4):
            return status
        sleep(1)
    return -1


def get_events(apikey: str, job_uuid: str) -> list:
    response = requests.get(
        f"{BASE_URL}/sic/conf/events/search/jobs/{job_uuid}/events",
        headers={"Authorization": f"Bearer {apikey}"},
    )
    response.raise_for_status()
    return response.json()


def main(apikey: str, earliest: str, latest: str, query: str, verbose: bool):
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)

    logging.info("Creating search job...")
    job_uuid = create_search_job(apikey, earliest, latest, query)
    logging.info(f"Job created: {job_uuid}")

    status = wait_for_job(apikey, job_uuid)
    if status != 2:
        logging.error(f"Job ended with status {status}.")
        return

    events = get_events(apikey, job_uuid)
    print(json.dumps(events, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search Sekoia.io events")
    parser.add_argument("APIKEY", help="Sekoia.io API key")
    parser.add_argument("--earliest", required=True, help="Start of the time window (ISO8601 or relative, e.g. -30d)")
    parser.add_argument("--latest", required=True, help="End of the time window (ISO8601 or relative, e.g. now)")
    parser.add_argument("--query", required=True, help="Search query in Dork format")
    parser.add_argument("-v", action="store_true", help="Verbose mode")
    args = parser.parse_args()

    main(args.APIKEY, args.earliest, args.latest, args.query, args.v)
```

## Usage

```bash
python search_events.py YOUR_API_KEY \
  --earliest="-30d" \
  --latest="now" \
  --query='source.ip: "1.2.3.4"'
```

## Notes

- By default the API returns up to **100 events**. Pass `?limit=1000` on the results endpoint to retrieve more (maximum 1000).
- Dates can be in ISO8601 format (`2025-01-01T00:00:00Z`) or relative format (`-30d`, `now`).
- The script retries up to 10 times with a 1-second delay between attempts. For long-running searches, increase `retries`.
