# Quickstart
API stands for Application Programming Interface and is the code that governs the server's access point.

When to use the Sekoia.io API?

* **Data sharing**: when you want an application to get data from Sekoia.io
* **Integration**: when you want an application to perform actions on Sekoia.io
* **Automation**: when you want to build a script to automate actions with Sekoia.io

Sekoia.io offers a public REST API to interact with the platform.

!!!note
    The Sekoia.io GUI is based on that API

Here are some characteristics of a REST API:

* **Client/Server architecture**: based on HTTP requests (GET, POST, PUT, DELETE...)
* **Stateless**: no connection is maintained between two requests
* **Identification of actions**: each action corresponds to a specific url

![API Overview](/assets/develop/api_overview.png){: style="max-width:100%"}

## Authentication
The whole API is available through `https://api.sekoia.io`.

Authentication is done by Bearer Token which means that in all requests, the header `Authorization: Bearer <YOUR_API_KEY>` is needed.

**Example using curl**:
```bash
curl -XGET -H "Authorization: Bearer YOUR_API_KEY" https://api.sekoia.io/v1/sic/conf/rules-catalog/rules
```

To create an API key, follow our guide [here](https://docs.sekoia.io/getting_started/manage_api_keys/).
The roles needed for your key will depend on what you want to achieve. If you plan to only get information from Sekoia.io, read only permissions will be enough. If you want to perform actions on Sekoia.io, you will also need to add write permissions.

Our documentation provides information on each endpoint and specifies the required permissions.

## Documentation organization

### Guides

The documentation offers a few guides:

* A small page on [filtering](/xdr/develop/guides/filtering/)
* A guide on [how to create automation modules](/xdr/develop/guides/automation/overview/)

### APIs

Our API documentation is divided according to the different functionalities the platform offers:

* [Authentication and Community](/xdr/develop/rest_api/community/)
* [Dashboard](/xdr/develop/rest_api/dashboard/)
* [Configuration](/xdr/develop/rest_api/configuration/)
* [Parser](/xdr/develop/rest_api/parser/)
* [Alert](/xdr/develop/rest_api/alert/)
* [Assets](/xdr/develop/rest_api/assets/)
* [Playbooks](/xdr/develop/rest_api/playbooks/)
* [Telemetry](/xdr/develop/rest_api/telemetry/)

In each of these categories, you will find the different actions available.

#### Structure
Each action is described and contains the following information:

* Action name
* Permission required
* Data required and optional
* Endpoint URL
* Query and response example

![Documentation overview](/assets/develop/documentation_overview.png){: style="max-width:100%"}

Depending of the endpoint, the data passed through the API is done as `query parameters` or in an `application/json` body. `Query parameters` means the data is passed in the URL.

**Two differents uses cases**

1. URL parameters are a way to pass data directly in the URL.

They come after the question mark (?) in the URL and are separated by an ampersand (&).
For example, in the following request, "match[name]=Suspicious%20Windows%20Defender%20Exclusion%20Command" and "limit=10" are the URL parameters.

```bash
curl -XGET -H "Authorization: Bearer YOUR_API_KEY" https://api.sekoia.io/v1/sic/conf/rules-catalog/rules?match[name]=Suspicious%20Windows%20Defender%20Exclusion%20Command&limit=10
```

These parameters are often used for simple requests like **search queries**, where the data being passed is short and simple, such as **`GET`  requests**.

2. Use the request body to send JSON payload.

JSON is a data format that is easy for both humans and machines to read and write. To send data as JSON, you will need to include a "Content-Type" header in your request, and the request body should be a JSON object.

This is often used for more complex requests like **creating or updating resources on the server**, such as **`POST` or `PUT` requests** for instance.

The following example uses the action `Invite a user` which is a `POST` request with an `application/json` body:
```bash
curl -X POST https://api.sekoia.io/v1/invitations \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer <YOUR_API_KEY>" \
   -d '{"email": "john.doe@example.com","communities": {"88dcb0c6-4efe-4256-95f1-40d2c4fefefd": ["44aaa41f-24ee-41d3-a7c1-4677da8b9243"]}}'

   # ["44aaa41f-24ee-41d3-a7c1-4677da8b9243"] corresponds to the UUID of the role assigned to the user.
   # This information is retrieved with the action "List the roles of a community"
```

!!! Note
    Such requests that create or update resources on the server may request to **ALSO** add parameters in the URL to specify the object one wants to have action on. With Sekoia.io API you will often pass through the URL the UUID of the specific object you are expecting to be modified.

## Python scripts
Python is a language that can be used to interact with the Sekoia.io API. Please find bellow two examples, one with a `GET` request with `query parameters` and another with a `POST` request and an `application/json` body.


### Get request with query parameters
In this example, we want to get information about the rule "Suspicious Windows Defender Exclusion Command".
We can get this information using the endpoint [List Rules](https://docs.sekoia.io/develop/rest_api/operation_center/configuration/#tag/rules-catalog/operation/get_rules_resource). As you can see in this documentation no parameter is mandatory (otherwise it will explicitly be written "required" in red color) for this request to be successfully executed but to fit our need we chose to use the `match[name]` parameter defined as "Match rules by their name (separated by commas).".
The following script will try to retrieve this information and print the result to STDOUT.

```python
import json
import logging

import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.sekoia.io/v1"

def get_request():

    url = f"{BASE_URL}/sic/conf/rules-catalog/rules?match[name]=Suspicious Windows Defender Exclusion Command"
    res = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})

    # In case of a success, the status code 200 is returned by the API
    if res.status_code == 200:
        data = res.json()

        # We print the result using the library JSON to get a pretty display
        logging.info(f"This is the result of the request:")
        logging.info(json.dumps(data, indent=4))
    # In case of authentication failed
    elif res.status_code == 401:
        logging.error(f"Cannot invite the user. Authentication failed: {res.status_code}")
        logging.error(res.text)
    # In case of insufficient permissions
    elif res.status_code == 403:
        logging.error(f"Insufficient permissions: {res.status_code}")
        logging.error(res.text)
    # In case of another status code
    else:
        logging.error(f"Error during the API request.")
        logging.error(res.text)

if __name__ == '__main__':
    get_request()
```

### Post request with JSON body

In this example, we will create a simple SIGMA rule nammed "My custom SIGMA rule", so it will be a `POST` request. According to [this documentation](https://docs.sekoia.io/xdr/develop/rest_api/configuration/#tag/rules-catalog/operation/post_rules_resource) in order to create a new rule we must provide the request with a minimum of mandatory fields. You will find in the following table what we will use in the Python script:

| Fields | Value for the example |
| --- | --- |
| name | "My custom SIGMA rule" |
| type | "sigma" |
| description | "Detect spawn of Powershell" |
| payload | "detection:\\n  selection:\\n    process.command\_line\|contains: 'powershell'\\n  condition: selection" |
| severity | 40 |
| effort | 3 |
| alert\_type\_uuid | "599f4b1a-dd60-43fe-8ee9-07d3c5d00ded" |
| enabled | True |

```python
import logging
import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.sekoia.io/v1"

def post_request():

    url = f"{BASE_URL}/sic/conf/rules-catalog/rules"
    body = {
      "name": "My custom SIGMA rule",
      "type": "sigma",
      "description": "Detect spawn of Powershell",
      "payload": "detection:\n  selection:\n    process.command_line|contains: 'powershell'\n  condition: selection",
      "severity": 40,
      "effort": 3,
      "alert_type_uuid": "599f4b1a-dd60-43fe-8ee9-07d3c5d00ded",
      "enabled": True
    }

    # The body is passed as a parameter of the post method.
    res = requests.post(url, json=body, headers={"Authorization": f"Bearer {API_KEY}"})

    # In case of a success, the status code 204 is returned by the API
    if res.status_code == 200:
        logging.info(f"The rule has been created on your community")
    # In case of authentication failed
    elif res.status_code == 401:
        logging.error(f"Cannot create the rule. Authentication failed: {res.status_code}")
        logging.error(res.text)
    # In case of another status code
    else:
        logging.error(f"Error during the API request.")
        logging.error(res.text)

if __name__ == '__main__':
    post_request()
```

### Another example - Search events
It is possible to search in your events by using the Sekoia.io API. Search for events can request some time to be processed and as a reminder, the API is stateless, that means no connection is maintained between two requests.

For this reason, Sekoia.io offers a solution to answer to this asynchronous problematic: the notion of search job.

3 steps are needed:

* [Create an event search job](https://docs.sekoia.io/xdr/develop/rest_api/configuration/#tag/events/operation/post_event_search_resource) - This step requires to provide the search query and the time window. The endpoint return a `job UUID` which will be used in the next steps.
* [Get an event search job](https://docs.sekoia.io/xdr/develop/rest_api/configuration/#tag/events/operation/get_event_search_job_info_resource) - This step is used to get information about the status of a job by providing its UUID. Jobs can have 5 statuses:
    * `0`: the job is not started
    * `1`: the job is in progress
    * `2`: the job is done (events can be retrieved)
    * `3`: the job is canceled
    * `4`: the job has failed
* [Get the events found by an event search job in descending order](https://docs.sekoia.io/xdr/develop/rest_api/configuration/#tag/events/operation/get_event_search_job_events_resource) - This steps is used to retrieved the events when the job is done (status `2`). It gives you the events in descending order (latest events first) and by default the limit is set to 100 events (up to 1000). An offset can be specified to get more of them.

#### Python3 script
This Python script uses these 3 actions to perform a search and print the events to STDOUT. Only the latest 100 are printed.

!!! Note
    You need at least Python 3.10 to run this script.

```python
#!/usr/bin/env python3
"""
This script uses the Sekoia.io API to search events
and print the last 100 events to STDOUT
"""

import argparse
import logging
import json
from time import sleep

import requests

BASE_URL = "https://api.sekoia.io/v1"


def create_search_job(apikey: str, dates: str, query: str) -> str:
    """
    Function create a event search job based on a query and a time windows
    """

    # Parsing the dates
    earliest_time = dates.split(",")[0]
    latest_time = dates.split(",")[1]
    body = {
        "term": query,
        "earliest_time": earliest_time,
        "latest_time": latest_time,
        "term_lang": "dork",
    }
    logging.debug(f"Search query: {query}")
    logging.debug("Creating a new search job:")
    response = requests.post(
        f"{BASE_URL}/sic/conf/events/search/jobs", headers={"Authorization": f"Bearer {apikey}"}, json=body
    )

    # In case of a success, the status code 200 is returned by the API
    if response.status_code == 200:
        data = response.json()
        logging.debug(json.dumps(data, indent=4))
        return data["uuid"]

    # In case of authentication failed
    elif response.status_code == 401:
        logging.error(f"Cannot create the search job. Authentication failed: {response.status_code}")
        logging.error(response.text)
        exit()
    # In case of insufficient permissions
    elif response.status_code == 403:
        logging.error(f"Insufficient permissions: {response.status_code}")
        logging.error(response.text)
        exit()
    # In case of another status code
    else:
        logging.error(f"Error during the API request.")
        logging.error(response.text)
        exit()


def get_search_job_status(
    apikey: str,
    job_uuid: str,
):
    """
    Function that get the status of a search job
    """

    logging.debug(f"Checking the status of job {job_uuid}...")
    response = requests.get(
        f"{BASE_URL}/sic/conf/events/search/jobs/{job_uuid}",
        headers={"Authorization": f"Bearer {apikey}"},
    )

    # In case of a success, the job status is returned
    if response.status_code == 200:
        data = response.json()
        logging.debug(json.dumps(data, indent=4))
        return data["status"]

    # In case of authentication failed
    elif response.status_code == 401:
        logging.error(f"Cannot get the search job status. Authentication failed: {response.status_code}")
        logging.error(response.text)
        exit()
    # In case of insufficient permissions
    elif response.status_code == 403:
        logging.error(f"Insufficient permissions: {response.status_code}")
        logging.error(response.text)
        exit()
    # In case of another status code
    else:
        logging.error(f"Error during the API request.")
        logging.error(response.text)
        exit()


def get_events_search_job(
    apikey: str,
    job_uuid: str,
) -> str:
    """
    Function that get the events found by an event search job in descending order
    """

    response = requests.get(
        f"{BASE_URL}/sic/conf/events/search/jobs/{job_uuid}/events",
        headers={"Authorization": f"Bearer {apikey}"},
    )

    # In case of a success, the status code 200 is returned by the API
    if response.status_code == 200:
        data = response.json()
        return data

    # In case of authentication failed
    elif response.status_code == 401:
        logging.error(f"Cannot get the search job. Authentication failed: {response.status_code}")
        logging.error(response.text)
        exit()
    # In case of insufficient permissions
    elif response.status_code == 403:
        logging.error(f"Insufficient permissions: {response.status_code}")
        logging.error(response.text)
        exit()
    # In case of another status code
    else:
        logging.error(f"Error during the API request.")
        exit()


def main(
    apikey: str,
    dates: str,
    query: str,
    verbose: bool,
):
    """
    Main function
    """

    # If verbose mode is set, setting logging config to DEBUG
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # Creation of the search job
    search_job_uuid = create_search_job(
        apikey=apikey,
        dates=dates,
        query=query,
    )

    # Check the status of the search job.
    # 10 attempts are made with 1 second sleep between each try
    attempts = 0
    while attempts < 10:
        status = get_search_job_status(apikey=apikey, job_uuid=search_job_uuid)

        # If status is not started or is in progress we wait 1 second
        if status == 0 or status == 1:
            # Sleep 1 second before trying again.
            sleep(1)
            attempts += 1

        # If the job is done, get the events
        elif status == 2:
            data = get_events_search_job(apikey=apikey, job_uuid=search_job_uuid)

            # Print the events to STDOUT (maximum 100 events)
            logging.info(json.dumps(data, indent=4))
            break

        # If the job is cancel or failed
        else:
            logging.error("Job is failed or canceled.")
            break


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "APIKEY",
        help="Sekoia.io API key with the SIC_READ_INTAKES permission",
    )
    parser.add_argument(
        "--dates",
        help="The time window over which you want to search for your events. The format must be 'date_from,date_to'",
        required=True,
    )
    parser.add_argument("--query", help="Search filter in Dork format", required=True)
    parser.add_argument("-v", action=argparse.BooleanOptionalAction, help="Verbose mode")

    args = parser.parse_args()

    main(
        apikey=args.APIKEY,
        dates=args.dates,
        query=args.query,
        verbose=args.v,
    )
```

#### How to use the script
Here is how to use the script:
```bash
search_events.py [-h] --dates DATES --query QUERY [-v] APIKEY
```

* `--dates` is used to specify to the time windows. The format used is `earliest_time,latest_time`. Dates can be in ISO8601 or relative format.
* `--query` is the query in Dork format (same langage as the Sekoia.io event page)
* `-v` to get verbose mode
* `APIKEY` is the Sekoia.io key with the `SIC_READ_INTAKES` permission

**Example**:

To get events with source IP `1.2.3.4` in the last 30 days:
```bash
search_events.py [-h] --dates="-30d,now" --query='source.ip: \"1.2.3.4\"' YOUR_API_KEY
```

## Best Practices for Development and Interaction with Our Product to Avoid Being Blocked by Our WAF

Web Application Firewalls (WAF) are crucial components for the security of web applications. They protect against various threats by filtering and monitoring HTTP traffic between a web application and the Internet. Our AI-based WAF uses a credibility score to determine the reliability of users and their interactions with our product. This article explores why we use a WAF, the specifics of our AI WAF, the main types of anomalies clients may encounter, and provides recommendations and best practices for interacting with our product without getting blocked.

### 1. Why Use a WAF?

A WAF is an indispensable security tool for protecting web applications against common attacks such as SQL injections, cross-site scripting (XSS), DDoS attacks, and other web-based threats. By using a WAF, we can:

- Prevent attacks by filtering malicious requests before they reach the application.
- Monitor traffic in real-time to detect and quickly respond to suspicious behavior.
- Protect sensitive data by preventing unauthorized access.
- Ensure application availability by minimizing interruptions due to attacks.

### 2. Specifics of an AI-Based WAF

Our AI-based WAF goes beyond traditional security rules by using machine learning algorithms to evaluate user credibility. The credibility score is calculated based on various behaviors and interactions. Here are some specifics:

- **Credibility Score Calculation**: The AI analyzes user behavior over periods of about ten seconds. Repeated anomalies lower the user's credibility.
- **Reputation Update Cycles**: The user's reputation is updated in cycles, averaging every 30 seconds. If suspicious behaviors persist, the user will be blocked.
- **Types of Anomalies**: The WAF detects security anomalies (scans, SSRF, injections, exploits, protocol manipulations), and behaviors exceeding fixed and dynamic (AI based) thresholds.

### 3. Main Types of Anomalies Clients May Encounter

Anomalies are evaluated in real-time and can impact the user's credibility. Here are the main types of anomalies:

- **Security Anomalies**:
  - Security scans, SSRF, injections, exploitation of vulnerabilities, protocol manipulations.

- **Anomalies Relative to Fixed Thresholds**:
  - **Response Time**: Requests taking more than 10 seconds of CPU/memory processing.
  - **Request Frequency**: More than 200 requests per second.
  - **Authentication**: Strengthened mechanisms on authentication management pages.

- **Anomalies Relative to Smart Thresholds**:
  - **Response Time**: Limit requests to less than 100 ms per second over a 10-second period.
  - **Error Requests**: Do not exceed 20% errors (4XX or 5XX codes) on 20 requests per 10-second period.
    * **Error Code 429**: Indicates rate limiting when too many requests are received in a short time.

### 4. Recommendations and Best Practices

To avoid being blocked by our WAF, it is important to follow these best practices when interacting with our API and the product UI in general:

- **Optimize Requests**: Avoid requests that consume too many resources (no more than 100 ms per request).
- **Limit Request Frequency**: Do not exceed 5 requests per second.
- **Handle Errors**: Pause scripts if the return code is 4XX or 5XX for 2 requests within a 10-second period.
- **Impact Duration**: In case of blocking, the user will be impacted for between 30 seconds and 5 minutes (randomized duration).

!!! Note
    Users sharing the same VPN exit point will be considered as a single user. Ensure that multiple users accessing the service through the same VPN do not collectively exceed the recommended limits.

By following these recommendations, you can improve the user experience and ensure smooth interaction with our product while respecting the security measures implemented by our WAF.
