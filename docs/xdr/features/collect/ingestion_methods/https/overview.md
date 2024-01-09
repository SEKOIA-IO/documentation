# Forward Logs to Sekoia.io using HTTPS

## Overview 

To push your events to Sekoia.io, you can use the HTTPS procotol. It's the simpler way to send us your logs, especially for non-syslog system.

Before processing, you have to:

- Connect to [Sekoia.io Operations Center](https://app.sekoia.io/operations/)
- Add an Intake to the relevant Entity
- Keep trace of the automatically generated Intake key

## Forwarding methods

To forward events using HTTPS to Sekoia.io, you have to send a `POST` request to `https://intake.sekoia.io` and to supply your intake key as header. Many formats are available, check the [Formation options section](#formating-options) to have more details

You can choose many option to forward logs: 

- Manually, either by utilizing the documented endpoints or through the use of custom scripts.
- Many technologies support forwarding logs directly from your equipment through HTTPS. Be sure to respect the Sekoia collection endpoint expected format (e.g., using the intake key as a header). 
- Utilize a third-party technology (e.g. [Graylog](./graylog.md) or [Logstash](./logstash.md) for example) responsible for collecting data from your equipment and forwarding events to Sekoia.io. You will find some samples in the next section.

## Formating options

For the forwarding, several options are available:

- Send your events as line-oriented records
- Send your events in a JSON array
- Send your events as a structured JSON payload

For each option, we will have to supply an intake key. The collector endpoint of Sekoia.io will provide event identifiers within the Sekoia.io detection workflow in the form of a JSON payload.

### Push our events to Sekoia.io as line-oriented records

To forward events, you can use the `/plain` endpoint.

The following headers are handled by Sekoia.io’S HTTPS log collector:

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

=== "With the intake key through query string"

    ```python
    import requests

    params = {"intake_key": "YOUR_INTAKE_KEY"}
    content = "[764008:0] info: 198.51.100.10 example.org. A IN"
    response = requests.post("https://intake.sekoia.io/plain", data=content, params=params)
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

=== "With the intake key through query string"

    ```python
    import requests

    params = {"intake_key": "YOUR_INTAKE_KEY"}
    events = ["[764008:0] info: 198.51.100.10 example.org. A IN", "[764023:0] info: 2.34.100.56 text.org. A IN"]
    content = "\n".join(events)
    response = requests.post("https://intake.sekoia.io/plain/batch", data=content, params=params)
    print(response.text) # (1)
    ```

    1. Will print  `{"event_ids": ["uuid1", "uuid2"]}`

### Push our events to Sekoia.io as JSON List

To send us events as JSON list, you should set `Content-Type` HTTP header to `application/json`.

The following headers are handled by Sekoia.io’S HTTPS log collector:

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

=== "With the intake key through query string"

    ```python
    import requests

    params = {"intake_key": "YOUR_INTAKE_KEY"}
    events = ["[764008:0] info: 198.51.100.10 example.org. A IN", "[764023:0] info: 2.34.100.56 text.org. A IN"]
    response = requests.post("https://intake.sekoia.io/jsons", json=events, params=params)
    print(response.text) # (1)
    ```

    1. Will print  `{"event_ids": ["uuid1", "uuid2"]}`


### Push our events to Sekoia.io as JSON Array

To send us events as JSON array, with the ability to send in the same batch several events from distinct intake keys, you should set `Content-Type` HTTP header to `application/json`. Intake key can only be sent in the JSON payload.

Use the endpoint `/array`. This endpoint accepts a set of events:

```python
import requests

events = [
    {
        "timestamp": "2021-04-05T21:33:31+02:00", # (1)
        "intake_key": "YOUR_INTAKE_KEY",
        "json": "[764008:0] info: 198.51.100.10 example.org. A IN",
    },
    {
        "intake_key": "ANOTHER_INTAKE_KEY",
        "json": "[764023:0] info: 2.34.100.56 text.org. A IN",
    },
]
response = requests.post("https://intake.sekoia.io/array", json=events)
print(response.text) # (2)
```

1. Optional.
2. Will print `{"event_ids":["ba2098cc-5fcf-4ad1-8d1d-af55750220ec","921b214c-fb89-4e27-a1fd-266f1837ea31"]}`

### Push our events to Sekoia.io as structured content

To send us events, you should set `Content-Type` HTTP header to `application/json`.

The following fields are currently handled by Sekoia.io’S HTTPS log collector:

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

To push structured data to Sekoia.io, you can push your payload as quoted JSON in the `POST`ed payload:

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