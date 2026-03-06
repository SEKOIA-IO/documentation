
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_usta_atp_incident"


    ```json
	{
        "company": {
            "id": 0,
            "name": "string"
        },
        "content": {
            "is_corporate": true,
            "password": "string",
            "password_complexity": {
                "contains": {
                    "lowercase": 0,
                    "numbers": 0,
                    "other": 0,
                    "punctuation": 0,
                    "separators": 0,
                    "symbols": 0,
                    "uppercase": 0
                },
                "length": 0,
                "score": "very_weak"
            },
            "source": "malware",
            "url": "http://example.com",
            "username": "username",
            "victim_detail": {
                "computer_name": "string",
                "country": "string",
                "cpu": "string",
                "gpu": "string",
                "infection_date": "string",
                "ip": "127.0.0.1",
                "language": "string",
                "malware": "string",
                "memory": "string",
                "phone_number": "string",
                "username": "username",
                "victim_os": "string",
                "victim_uid": "9eee4f4d-714d-402f-b9c1-17d4442e0901"
            }
        },
        "content_type": "string",
        "created": "2019-08-24T14:15:22Z",
        "id": 0,
        "status": "in_progress",
        "status_timestamp": "2019-08-24T14:15:22Z"
    }
    ```



