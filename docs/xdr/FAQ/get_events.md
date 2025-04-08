### 1. **How to Export Events?**

- **From the Interface:**
    - Go to the **Events** section.
    - Create your query in the search bar.
    - Click **Export events** at the top right of the logs table.
    - Select the fields to export or choose to export all fields.
    - **Available Formats:** CSV (ideal for spreadsheets) and JSON (useful for technical integration).
    - **Export Limits:** 
        - Maximum of 500 events per export. Refine your search to get complete results if this limit is reached.
        - The description field is dynamic and therefore excluded from extraction, as its structure may vary across events.

- **Via API:**
    - Use the Event Search API to automate event exports through jobs.
    - Events are retrieved in JSON format.
    - **API Limits:** Please refer to [API recommendations and best practices](/xdr/FAQ.md#4-recommendations-and-best-practices).


### 2. **How to Perform Statistics on Events?**

- [**Query Builder**](/xdr/features/investigate/query_builder.md):
    - Create complex queries to visualize event statistics as tables or graphs. These analyses can be integrated into dashboards.
    - **Known Limits:** Maximum of 10,000 rows per query, up to 10 queries per minute, and a 10-minute timeout. If these limits are reached, results may be partial, requiring more restrictive searches.


### 3. **How to Automate Actions Based on Events?**

- **Playbooks:**
    - Use the **Get Events** module in a playbook to automate event retrieval based on a custom query.
    - This module simplifies the creation of automated queries to monitor specific events.


### 4. **How to Find Events Related to a Specific Alert or Case?**

- **Via API:**
    - Filter events associated with an alert or case using the Event Search API with appropriate criteria.
    - For instance, to filter by an alert’s short ID, use the following query:

        ```json
        {
            "term": "",
            "filters": [
               {
                  "field": "alert_short_id",
                  "operator": "contains",
                  "value": "YOUR_ALERT_SHORT_IDS",
                  "disabled": false,
                  "excluded": false
               }
            ],
            "earliest_time": "2024-08-15T09:38:04.715Z",
            "latest_time": "2024-08-22T09:38:04.715Z",
            "visible": true,
            "community_uuids": [
               "YOUR_COMMUNITY_ID"
            ]
        }
        ```

    - Adapt the filters in this query to specifically target events related to your alerts or cases.
