# Forward Logs to SEKOIA.IO via HTTPS

To push your events through our HTTPS log collector, you have to `POST` your logs in the JSON format. To send us events, you should set `Content-Type` HTTP header to `application/json`.

The following fields are currently handled by SEKOIA.IO’S HTTPS log collector:

| Field         | Mandatory? | Type     | Description                                                                                            |
|---------------|------------|----------|--------------------------------------------------------------------------------------------------------|
| `intakey_key` | Yes        | String   | Intake to which you would like to push events to                                                       |
| `json`        | Yes        | String   | The actual log payload. If you want to push structured JSON logs, please send them as quoted JSON here |
| `@timestamp`  | No         | Datetime | Event date if you want to push your own date (fallback is to use the reception’s date)                 |

## Push Events to SEKOIA.IO Using Python

To push text events, one can just `POST` content to `https://intake.sekoia.io`:

```python
import requests

content = {"intake_key": "YOUR_INTAKE_KEY", "json": "[764008:0] info: 198.51.100.10 example.org. A IN"}
requests.post("https://intake.sekoia.io", json=content)
```

To push structured JSON data to SEKOIA.IO, you can push your payload as quoted JSON in the `POST`ed payload:

```python
import requests
import json

structured_log = {"key": "value"}
content = {"intake_key": "YOUR_INTAKE_KEY", "json": json.dumps(structured_log)}
requests.post("https://intake.sekoia.io", json=content)
```

For numerous events, you can use the alternative endpoint `/batch`. This endpoint accepts a set of events:

```python
import requests

content = {"intake_key": "YOUR_INTAKE_KEY", "jsons": ["[764008:0] info: 198.51.100.10 example.org. A IN", "[764023:0] info: 2.34.100.56 text.org. A IN"]}
requests.post("https://intake.sekoia.io/batch", json=content)
```

