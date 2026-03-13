# Create an optimization rule

You can create optimization rules via the Sekoia.io API to automate the filtering and cleaning of your incoming security data.

## Prerequisites

To manage optimization rules via the API, you must have an API key with the following permissions:

* **View intakes**
* **Manage intakes**
* **Manage all communities** (required for global administrators)

## Create a rule via API

To create a new optimization rule, send a POST request to the configuration endpoint.

1. Open your terminal or API client.
2. [cite_start]Prepare your JSON payload including a **description** and an **action**[cite: 56, 57].
3. [cite_start]Define the scope using **community_uuid** and optionally **dialect_uuid** or **intake_uuid**[cite: 55, 58].
4. [cite_start]Add your criteria in the **filters** array using a **field**, **operator**, and **value**[cite: 62, 63, 64].
5. [cite_start]Send the request to `https://api.sekoia.io/v1/sic/conf/intakes/optimization_rules`[cite: 52].

!!! warning "Respect field types"

    You must match the value type to the field definition to avoid runtime errors.
    * If the field is an Integer, do not use quotes (e.g., "value": 4624).
    * If the field is a String, use quotes (e.g., "value": "netflow").
    
    Using quotes for an integer field will cause the filter to fail.

??? example "Example: Ignore events with specific IP tags"
    This command ignores events where both source and destination IPs are private for the netflow dataset.
    ```bash
    curl --request POST \
    --url [https://api.sekoia.io/v1/sic/conf/intakes/optimization_rules](https://api.sekoia.io/v1/sic/conf/intakes/optimization_rules) \
    --header 'Authorization: Bearer YOUR_TOKEN' \
    --header 'Content-Type: application/json' \
    --data '{
      "action": 1,
      "description": "Remove private / private events",
      "community_uuid": "YOUR_COMMUNITY_ID",
      "filters": [
        { "field": "event.dataset", "operator": "==", "value": "netflow" },
        { "field": "sekoiaio.tags.source.ip", "operator": "in", "value": ["rfc5735", "rfc1918"] },
        { "field": "sekoiaio.tags.destination.ip", "operator": "in", "value": ["rfc5735", "rfc1918"] }
      ]
    }'
    ```

## Result

Once created, the rule is applied to matching incoming events immediately. [cite_start]You can verify the reduction of ingestion volume on the platform's usage page if you used the **Ignore Event** action[cite: 42]. There is no limit to the number of rules you can create.

## See also
* [Optimization rules overview](/xdr/features/collect/optimization_rules_overview.md)
* [Optimization rules technical reference](/xdr/features/collect/optimization_rules_reference.md) to learn more about filter operators, action bitmask values and more. 
* [Investigate fair use overusage](/xdr/features/collect/investigate_overusage.md) to align your rules on your usage.
