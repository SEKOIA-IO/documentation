
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Social media monitoring` | Digital Shadows monitors Twitter, Youtube, Facebook |
| `File monitoring` | Digital Shadows monitors open file storage (Public NAS, Public AWS S3 Buckets, Public FTP/SMB, RSYNC) |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `alert` |
| Category | `threat` |
| Type | `indicator` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "searchlight_alerts.json"

    ```json
	
    {
        "event": {
            "category": "threat",
            "end": "2022-03-03T13:03:51.044370Z",
            "kind": "alert",
            "outcome": "success",
            "action": "impersonating-domain-alert",
            "start": "2019-12-05T21:03:10.433Z",
            "type": "indicator",
            "reason": "Impersonating Domain example.info"
        },
        "digital_shadows_searchlight": {
            "event": {
                "id": "00a8bc91-bd77-45d5-bf45-213c6b7fee19"
            },
            "risk_factors": [
                "Has assets in content",
                "Hosting content",
                "Has a DNS record",
                "Newly registered when raised"
            ],
            "portal_id": "XXXXXX",
            "description": "A domain that is possibly impersonating your assets was detected.\n\nRisk Level: Low\nImpersonating Domain: example.info\nLast Registered: \n\nRisk Factors:\n* Has assets in content\n* Hosting content\n* Has a DNS record\n* Newly registered when raised\n\nMatched Assets:\n* example\n* example.biz\n* example.eu\n* example.fr\n\n\nWHOIS records provide the following information:\nRegistrar: Epik, Inc.\nRegistrar abuse contact email: donuts@epik.com\nRegistrar abuse contact phone: 425-765-0077\nCreated: 19 Feb 2021 16:35\nLast updated: 21 Feb 2022 09:35\nRegistrar registration expiration date: 19 Feb 2023 16:35\n\nDNS Record\nA - 185.255.121.5\nNS - ns3.epik.com.\nNS - ns4.epik.com.\nSOA - ns3.epik.com. support.epik.com. 2022022101 10800 3600 604800 3600\nTXT - \"841f65603f47f3a7c35da7caf0f2ceaee92a1ed6\"\nTXT - \"dan-ownership-verification=54z0h1kj\"\nTXT - \"godaddyverification=Q8293uVVCXS1ttOuxPoOKg==\"\n\nAlert Raised: 05 Dec 2019 21:03\nAlert Updated: 03 Mar 2022 13:03\n\nSearchlight Portal ID: XXXXX\nSearchlight Portal Link: https://portal-digitalshadows.com/triage/alerts/XXXXX\n",
            "risk_level": "low"
        }
    }
    	
	```


=== "searchlight_incident.json"

    ```json
	
    {
        "event": {
            "category": "threat",
            "end": "2022-03-15T19:16:06.981Z",
            "kind": "alert",
            "outcome": "success",
            "action": "exposed-port-incident",
            "start": "2022-03-15T19:16:06.981Z",
            "type": "indicator",
            "reason": "Exposed open port"
        },
        "digital_shadows_searchlight": {
            "event": {
                "id": "8484455"
            },
            "impact_description": "Port 123: Port 123 (Network Time Protocol) can be abused to cause a denial-of-service attack and should not be exposed to the public Internet.\n",
            "mitigation": "Port 123: This port should ideally not be reachable from the public Internet and so should be firewalled off. In cases where this is not feasible, a technical compensating control could be the introduction of IP allowlisting of known IPs to prevent unauthorized access.\t\n",
            "description": "The following ports have been detected on IP 11.22.33.44\nPort 123\n",
            "risk_level": "low"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`digital_shadows_searchlight.description` | `text` | None |
|`digital_shadows_searchlight.event.id` | `keyword` | None |
|`digital_shadows_searchlight.impact_description` | `keyword` | None |
|`digital_shadows_searchlight.mitigation` | `keyword` | None |
|`digital_shadows_searchlight.portal_id` | `keyword` | None |
|`digital_shadows_searchlight.risk_factors` | `text` | None |
|`digital_shadows_searchlight.risk_level` | `keyword` | None |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.end` | `date` | event.end contains the date when the event ended or when the activity was last observed. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.outcome` | `keyword` | The outcome of the event. The lowest level categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |

