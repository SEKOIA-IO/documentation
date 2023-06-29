# Forward Logs to SEKOIA.IO via HTTPS

To push your events to SEKOIA.IO, you can use our HTTPS log collector. It's the simpler way to send us your logs, especially for non-syslog system.

For the forwarding, several options are available:

- Send your events as line-oriented records
- Send your events in a JSON array
- Send your events as a structured JSON payload

For each option, we will have to supply an intake key. The collector will return the events' identifiers in the SEKOIA.IO detection workflow, as a JSON payload.

## Push our events to SEKOIA.IO as line-oriented records

To forward events, you can use the `/plain` endpoint.

The following headers are handled by SEKOIA.IO’S HTTPS log collector:

| Header                       | Mandatory? | Type     | Description                                                                            |
|------------------------------|------------|----------|----------------------------------------------------------------------------------------|
| `X-SEKOIAIO-INTAKE-KEY`      | No         | String   | Intake to which you would like to push events to                                       |
| `X-SEKOIAIO-EVENT-TIMESTAMP` | No         | Datetime | Event date if you want to push your own date (fallback is to use the reception’s date) |


Supply the intake key as the header `X-SEKOIAIO-INTAKE-KEY` or as password in the HTTP Basic authentication mechanism.

To push one event, just POST content to `https://intake.sekoia.io/plain`

=== "With the intake key as header"

    ```python
    import requests

    headers = {"X-SEKOIAIO-INTAKE-KEY": "YOUR_INTAKE_KEY"}
    content = "[764008:0] info: 198.51.100.10 example.org. A IN"
    response = requests.post("https://intake.sekoia.io/plain", data=content, headers=headers)
    print(response.text) # (1)
    ```

    1. Will print  `{"event_id": "uuid"}`

=== "With the intake key through the HTTP Basic Auth"

    ```python
    import requests

    auth = request.auth.HTTPBasicAuth(None, "YOUR_INTAKE_KEY")
    content = "[764008:0] info: 198.51.100.10 example.org. A IN"
    response = requests.post("https://intake.sekoia.io/plain", data=content, auth=auth)
    print(response.text) # (1)
    ```

    1. Will print  `{"event_id": "uuid"}`

For numerous events, you can use the alternative endpoint `/batch`. The events should be separated by the line feed character (`U+000A` or `\n`):

=== "With the intake key as header"

    ```python
    import requests

    headers = {"X-SEKOIAIO-INTAKE-KEY": "YOUR_INTAKE_KEY"}
    events = ["[764008:0] info: 198.51.100.10 example.org. A IN", "[764023:0] info: 2.34.100.56 text.org. A IN"]
    content = "\n".join(events)
    response = requests.post("https://intake.sekoia.io/plain/batch", data=content, headers=headers)
    print(response.text) # (1)
    ```

    1. Will print  `{"event_ids": ["uuid1", "uuid2"]}`

=== "With the intake key through the HTTP Basic Auth"

    ```python
    import requests

    auth = request.auth.HTTPBasicAuth(None, "YOUR_INTAKE_KEY")
    events = ["[764008:0] info: 198.51.100.10 example.org. A IN", "[764023:0] info: 2.34.100.56 text.org. A IN"]
    content = "\n".join(events)
    response = requests.post("https://intake.sekoia.io/plain/batch", data=content, auth=auth)
    print(response.text) # (1)
    ```

    1. Will print  `{"event_ids": ["uuid1", "uuid2"]}`

## Push our events to SEKOIA.IO as JSON array

To send us events as JSON array, you should set `Content-Type` HTTP header to `application/json`.

The following headers are handled by SEKOIA.IO’S HTTPS log collector:

| Header                       | Mandatory? | Type     | Description                                                                            |
|------------------------------|------------|----------|----------------------------------------------------------------------------------------|
| `X-SEKOIAIO-INTAKE-KEY`      | No         | String   | Intake to which you would like to push events to                                       |
| `X-SEKOIAIO-EVENT-TIMESTAMP` | No         | Datetime | Event date if you want to push your own date (fallback is to use the reception’s date) |


Supply the intake key as the header `X-SEKOIAIO-INTAKE-KEY` or as password in the HTTP Basic authentication mechanism.

Use the endpoint `/jsons`. This endpoint accepts a set of events:

=== "With the intake key as header"

    ```python
    import requests

    headers = {"X-SEKOIAIO-INTAKE-KEY": "YOUR_INTAKE_KEY"}
    events = ["[764008:0] info: 198.51.100.10 example.org. A IN", "[764023:0] info: 2.34.100.56 text.org. A IN"]
    response = requests.post("https://intake.sekoia.io/jsons", json=events, headers=headers)
    print(response.text) # (1)
    ```

    1. Will print  `{"event_ids": ["uuid1", "uuid2"]}`

=== "With the intake key through the HTTP Basic Auth"

    ```python
    import requests

    auth = request.auth.HTTPBasicAuth(None, "YOUR_INTAKE_KEY")
    events = ["[764008:0] info: 198.51.100.10 example.org. A IN", "[764023:0] info: 2.34.100.56 text.org. A IN"]
    response = requests.post("https://intake.sekoia.io/jsons", json=events, auth=auth)
    print(response.text) # (1)
    ```

    1. Will print  `{"event_ids": ["uuid1", "uuid2"]}`

## Push our events to SEKOIA.IO as structured content

To send us events, you should set `Content-Type` HTTP header to `application/json`.

The following fields are currently handled by SEKOIA.IO’S HTTPS log collector:

| Field         | Mandatory? | Type     | Description                                                                                            |
|---------------|------------|----------|--------------------------------------------------------------------------------------------------------|
| `intakey_key` | Yes        | String   | Intake to which you would like to push events to                                                       |
| `json`        | Yes        | String   | The actual log payload. If you want to push structured JSON logs, please send them as quoted JSON here |
| `@timestamp`  | No         | Datetime | Event date if you want to push your own date (fallback is to use the reception’s date)                 |


To push text events, one can just `POST` content to `https://intake.sekoia.io`:

```python
import requests

content = {"intake_key": "YOUR_INTAKE_KEY", "json": "[764008:0] info: 198.51.100.10 example.org. A IN"}
response = requests.post("https://intake.sekoia.io", json=content)
print(response.text) # (1)
```

1. Will print  `{"event_id": "uuid"}`

To push structured data to SEKOIA.IO, you can push your payload as quoted JSON in the `POST`ed payload:

```python
import requests
import json

structured_log = {"key": "value"}
content = {"intake_key": "YOUR_INTAKE_KEY", "json": json.dumps(structured_log)}
response = requests.post("https://intake.sekoia.io", json=content)
print(response.text) # (1)
```

1. Will print  `{"event_id": "uuid"}`

For numerous events, you can use the alternative endpoint `/batch`. This endpoint accepts a set of events:

```python
import requests

content = {"intake_key": "YOUR_INTAKE_KEY", "jsons": ["[764008:0] info: 198.51.100.10 example.org. A IN", "[764023:0] info: 2.34.100.56 text.org. A IN"]}
response = requests.post("https://intake.sekoia.io/batch", json=content)
print(response.text) # (1)
```

1. Will print  `{"event_ids": ["uuid1", "uuid2"]}`
