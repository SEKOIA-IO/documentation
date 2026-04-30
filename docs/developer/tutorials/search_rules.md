# Search for rules

This tutorial shows how to search for detection rules using the Sekoia.io API. It uses a `GET` request with query parameters to filter results by name.

## Prerequisites

- A valid API key with the `SIC_READ_CONF` permission
- `curl` or Python 3 installed

## Endpoint

```
GET /v1/sic/conf/rules-catalog/rules
```

## Filter by name

Use the `match[name]` parameter to find a rule by its name.

=== "curl"

    ```bash
    curl -X GET \
      "https://api.sekoia.io/v1/sic/conf/rules-catalog/rules?match[name]=Suspicious%20Windows%20Defender%20Exclusion%20Command" \
      -H "Authorization: Bearer YOUR_API_KEY"
    ```

=== "Python"

    ```python
    import json
    import requests

    API_KEY = "YOUR_API_KEY"
    BASE_URL = "https://api.sekoia.io/v1"

    def search_rules(name: str):
        url = f"{BASE_URL}/sic/conf/rules-catalog/rules"
        params = {"match[name]": name}
        response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"}, params=params)
        response.raise_for_status()
        return response.json()

    if __name__ == "__main__":
        results = search_rules("Suspicious Windows Defender Exclusion Command")
        print(json.dumps(results, indent=4))
    ```

## Filter by multiple values

Separate values with a comma to match any of them (logical OR):

```
/v1/sic/conf/rules-catalog/rules?match[name]=rule1,rule2
```

You can combine multiple `match` parameters (logical AND):

```
/v1/sic/conf/rules-catalog/rules?match[name]=rule1&match[severity]=high
```

## Response

A successful request returns `200` with a list of matching rules:

```json
{
  "items": [
    {
      "uuid": "...",
      "name": "Suspicious Windows Defender Exclusion Command",
      "type": "sigma",
      "severity": 80,
      "enabled": true
    }
  ],
  "total": 1
}
```

## Next steps

Once you have found a rule, you can update or delete it using its `uuid` with the corresponding `PUT` or `DELETE` endpoints. You can also [create a new rule](create_sigma_rule.md) from scratch.
