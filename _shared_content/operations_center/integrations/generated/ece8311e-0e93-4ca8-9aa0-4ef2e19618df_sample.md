
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_alert_with_domain"


    ```json
	{
        "alertName": "Alert Name",
        "content": "content",
        "domain": "domain",
        "score": "1.0",
        "timestamp": "2026-03-24T10:09:27Z",
        "title": "Title",
        "url": "url"
    }
    ```



=== "test_alert_with_url"


    ```json
	{
        "alertName": "Alert Name",
        "content": "content",
        "domain": "",
        "score": "1.0",
        "timestamp": "2026-03-24T10:09:27Z",
        "title": "Title",
        "url": "url"
    }
    ```



