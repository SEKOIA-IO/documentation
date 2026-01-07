
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "livelog-dns"


    ```json
	{
        "user_id": "00000000-0000-0000-0000-000000000001",
        "client_id": "00000000-0000-0000-0000-000000000002",
        "external_id": "00000000-0000-0000-0000-000000000003",
        "display_name": "User Test",
        "category_id": "1235",
        "category_label": "CDN et Non D\u00e9finissable",
        "url": "",
        "action": "allow",
        "domain": "merchandise.opera-api2.com",
        "src_ip": "",
        "src_port": "",
        "timestamp": 1742292307674,
        "threat": "Type=0; Resolution=2; Threat=Win.Test.EICAR_HDB-1;",
        "policy_id": "",
        "rule_id": "",
        "dest_ip": "6.5.4.3",
        "http_method": "",
        "http_version": "",
        "user_response_time_ms": "",
        "user_received_bytes": "",
        "user_sent_bytes": "",
        "user_status_code": "",
        "cache_status": "",
        "peer_response_time_ms": "",
        "peer_status_code": "",
        "theme_label": "Autres",
        "groups_id": [
            "00000000-0000-0000-0000-000000000004"
        ],
        "groups_name": [
            "Test Group 1",
            "Test Group 2"
        ],
        "directory_id": "00000000-0000-0000-0000-000000000005",
        "directory_name": "Test Directory",
        "policy_name": "None",
        "type": "dns",
        "dns_answer": "merchandise.opera-api2.com.\t3600\tIN\tA\t185.26.182.112",
        "applications": null
    }
    ```



=== "livelog-proxy-missing-dns-answer"


    ```json
	{
        "user_id": "00000000-0000-0000-0000-000000000001",
        "client_id": "00000000-0000-0000-0000-000000000002",
        "external_id": "00000000-0000-0000-0000-000000000003",
        "display_name": "Test User",
        "category_id": "1000",
        "category_label": "Services aux Entreprises",
        "url": "https://safebrowsing.googleapis.com/v4/threatListUpdates:fetch?",
        "action": "allow",
        "domain": "safebrowsing.googleapis.com",
        "src_ip": "1.2.3.4",
        "src_port": "27275",
        "timestamp": 1737373729852,
        "threat": "Type=0; Resolution=2; Threat=Win.Test.EICAR_HDB-1;",
        "policy_id": "-",
        "rule_id": "-",
        "dest_ip": "4.3.2.1",
        "http_method": "GET",
        "http_version": "1.1",
        "user_response_time_ms": "84",
        "user_received_bytes": "4664",
        "user_sent_bytes": "836",
        "user_status_code": "200",
        "cache_status": "TCP_MISS",
        "peer_response_time_ms": "9",
        "peer_status_code": "200",
        "theme_label": "Autres",
        "groups_id": null,
        "groups_name": null,
        "directory_id": "00000000-0000-0000-0000-000000000000",
        "directory_name": "Test Directory",
        "policy_name": "None",
        "type": "proxy",
        "applications": null
    }
    ```



=== "livelog-proxy"


    ```json
	{
        "user_id": "00000000-0000-0000-0000-000000000001",
        "client_id": "00000000-0000-0000-0000-000000000002",
        "external_id": "00000000-0000-0000-0000-000000000003",
        "display_name": "Test User",
        "category_id": "1000",
        "category_label": "Services aux Entreprises",
        "url": "https://safebrowsing.googleapis.com/v4/threatListUpdates:fetch?",
        "action": "allow",
        "domain": "safebrowsing.googleapis.com",
        "src_ip": "1.2.3.4",
        "src_port": "27275",
        "timestamp": 1737373729852,
        "threat": "Type=0; Resolution=2; Threat=Win.Test.EICAR_HDB-1;",
        "policy_id": "-",
        "rule_id": "-",
        "dest_ip": "4.3.2.1",
        "http_method": "GET",
        "http_version": "1.1",
        "user_response_time_ms": "84",
        "user_received_bytes": "4664",
        "user_sent_bytes": "836",
        "user_status_code": "200",
        "cache_status": "TCP_MISS",
        "peer_response_time_ms": "9",
        "peer_status_code": "200",
        "theme_label": "Autres",
        "groups_id": null,
        "groups_name": null,
        "directory_id": "00000000-0000-0000-0000-000000000000",
        "directory_name": "Test Directory",
        "policy_name": "None",
        "type": "proxy",
        "dns_answer": "",
        "applications": null
    }
    ```



