# Create a SIGMA rule

This tutorial shows how to create a detection rule programmatically using a `POST` request with a JSON body.

## Prerequisites

- A valid API key with the `SIC_WRITE_CONF` permission
- `curl` or Python 3 installed

## Endpoint

```
POST /v1/sic/conf/rules-catalog/rules
```

## Required fields

| Field | Description | Example value |
| --- | --- | --- |
| `name` | Name of the rule | `"My custom SIGMA rule"` |
| `type` | Rule type | `"sigma"` |
| `description` | Short description | `"Detect spawn of Powershell"` |
| `payload` | SIGMA detection logic (YAML as a string) | See below |
| `severity` | Severity score (0–100) | `40` |
| `effort` | Analyst effort level (1–5) | `3` |
| `alert_type_uuid` | UUID of the alert type | `"599f4b1a-dd60-43fe-8ee9-07d3c5d00ded"` |
| `enabled` | Whether the rule is active | `true` |

## Create the rule

=== "curl"

    ```bash
    curl -X POST https://api.sekoia.io/v1/sic/conf/rules-catalog/rules \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "My custom SIGMA rule",
        "type": "sigma",
        "description": "Detect spawn of Powershell",
        "payload": "detection:\n  selection:\n    process.command_line|contains: powershell\n  condition: selection",
        "severity": 40,
        "effort": 3,
        "alert_type_uuid": "599f4b1a-dd60-43fe-8ee9-07d3c5d00ded",
        "enabled": true
      }'
    ```

=== "Python"

    ```python
    import requests

    API_KEY = "YOUR_API_KEY"
    BASE_URL = "https://api.sekoia.io/v1"

    def create_sigma_rule():
        url = f"{BASE_URL}/sic/conf/rules-catalog/rules"
        body = {
            "name": "My custom SIGMA rule",
            "type": "sigma",
            "description": "Detect spawn of Powershell",
            "payload": "detection:\n  selection:\n    process.command_line|contains: powershell\n  condition: selection",
            "severity": 40,
            "effort": 3,
            "alert_type_uuid": "599f4b1a-dd60-43fe-8ee9-07d3c5d00ded",
            "enabled": True,
        }
        response = requests.post(url, json=body, headers={"Authorization": f"Bearer {API_KEY}"})
        response.raise_for_status()
        print("Rule created:", response.json().get("uuid"))

    if __name__ == "__main__":
        create_sigma_rule()
    ```

## Response

A successful request returns `200` with the created rule, including its generated `uuid`:

```json
{
  "uuid": "a1b2c3d4-...",
  "name": "My custom SIGMA rule",
  "type": "sigma",
  "enabled": true
}
```

## Next steps

Use the returned `uuid` to update the rule (`PUT`) or retrieve it individually (`GET /v1/sic/conf/rules-catalog/rules/{uuid}`). To search for existing rules before creating a new one, see [Search for rules](search_rules.md).
