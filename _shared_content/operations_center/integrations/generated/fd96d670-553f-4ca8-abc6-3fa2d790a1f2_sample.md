
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_alert_generic"


    ```json
	{
        "date": "2026-06-30T12:30:00+00:00",
        "identifier": "490bf983-6dcc-4536-b56b-72cf458c7016",
        "source": "Vigidomaine",
        "subject": "example.com",
        "severity": "MEDIUM",
        "type": "SECURITY_HEADER_MISSING_ESSENTIALS",
        "title": "Improveable header configuration",
        "description": "The header configuration could be improved. This would increase security or more closely follow conventions and best practices.",
        "status": "CREATED",
        "dateFirstSeen": "2026-06-30T12:10:00+00:00",
        "dateLastSeen": "2026-07-01T00:10:00+00:00",
        "functionality": "SECURITY_HEADER",
        "url": "https://example.com/alert/490bf983-6dcc-4536-b56b-72cf458c7016"
    }
    ```



=== "test_alert_typosquatting"


    ```json
	{
        "date": "2026-06-30T12:30:00+00:00",
        "identifier": "490bf983-6dcc-4536-b56b-72cf458c7016",
        "source": "Vigidomaine",
        "subject": "example.com",
        "severity": "MEDIUM",
        "type": "TYPOSQUATTING_DOMAIN_DETECTED",
        "title": "Detection",
        "description": "Probable typosquatting has been detected on the domain.",
        "status": "CREATED",
        "dateFirstSeen": "2026-06-30T12:10:00+00:00",
        "dateLastSeen": "2026-07-01T00:10:00+00:00",
        "functionality": "TYPOSQUATTING",
        "url": "https://example.com/alert/490bf983-6dcc-4536-b56b-72cf458c7016",
        "typoDetection": "example.org",
        "typoDetectionStrategies": [
            "TLD"
        ],
        "typoRegistrarName": "Example Registrar",
        "typoRegisteredAt": "2020-01-01T01:01:01+01:01",
        "typoIps": [
            "198.51.100.10",
            "203.0.113.20",
            "2001:db8::10",
            "2001:db8::20"
        ],
        "typoNameServers": [
            "ns1.example.org",
            "ns2.example.org"
        ],
        "typoSimilarityPercentage": 96,
        "typoDomainAgeDays": 500,
        "typoHasTxtRecord": true,
        "typoHasMxRecord": true
    }
    ```



