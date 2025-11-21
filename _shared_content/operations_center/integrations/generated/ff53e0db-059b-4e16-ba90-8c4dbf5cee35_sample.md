
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_event_1"


    ```json
	{
        "attack_vector": "NetworkSecurity",
        "backend_last_updated": "02/02/2025 02:22:20",
        "details": "Domain:bb[.]caf\u00e9",
        "device_id": "2",
        "device_rooted": false,
        "email": "Blocked",
        "event": "Info",
        "event_timestamp": "02/22/2023 02:22:20",
        "id": 22,
        "mdm_uuid": "00000000-0000-0000-0000-0000000000",
        "name": "TestDevice",
        "number": "+13045555555",
        "severity": "Critical",
        "threat_factors": "Phishing",
        "device_model": "Android",
        "client_version": "2.73-SNAPSHOT/2,089"
    }
    ```



=== "test_event_2"


    ```json
	{
        "attack_vector": "NetworkSecurity",
        "backend_last_updated": "02/02/2025 02:22:20",
        "details": "Domain:bb[.]caf\u00e9",
        "device_id": "2",
        "device_rooted": false,
        "email": "Blocked",
        "event": "Info",
        "id": 22,
        "mdm_uuid": "00000000-0000-0000-0000-0000000000",
        "name": "TestDevice",
        "number": "+13045555555",
        "severity": "Critical",
        "threat_factors": "Phishing",
        "device_model": "Android",
        "client_version": "2.73-SNAPSHOT/2,089"
    }
    ```



=== "test_event_3"


    ```json
	{
        "attack_vector": "NetworkSecurity",
        "details": "Domain:bb[.]caf\u00e9",
        "device_id": "2",
        "device_rooted": false,
        "email": "Blocked",
        "event": "Info",
        "event_timestamp": "02/22/2023 02:22:20",
        "id": 22,
        "mdm_uuid": "00000000-0000-0000-0000-0000000000",
        "name": "TestDevice",
        "number": "+13045555555",
        "severity": "Critical",
        "threat_factors": "Phishing",
        "device_model": "Android",
        "client_version": "2.73-SNAPSHOT/2,089"
    }
    ```



=== "test_event_4"


    ```json
	{
        "attack_vector": "NetworkSecurity",
        "details": "Domain:bb[.]caf\u00e9",
        "device_id": "2",
        "device_rooted": false,
        "email": "Blocked",
        "event": "Info",
        "id": 22,
        "mdm_uuid": "00000000-0000-0000-0000-0000000000",
        "name": "TestDevice",
        "number": "+13045555555",
        "severity": "Critical",
        "threat_factors": "Phishing",
        "device_model": "Android",
        "client_version": "2.73-SNAPSHOT/2,089"
    }
    ```



=== "test_event_5"


    ```json
	{
        "attack_vector": "Device",
        "backend_last_updated": "2025-10-02T10:53:26+00:00",
        "details": "",
        "device_id": 8,
        "device_rooted": "False",
        "email": "john.doe@example.com",
        "event": "Compliant",
        "event_timestamp": null,
        "id": 16,
        "mdm_uuid": "00000000-0000-0000-0000-0000000000",
        "name": "my Iphone",
        "number": "0123 4567890",
        "policy_name": "Global",
        "severity": "Information",
        "threat_factors": "Network Protection (VPN)",
        "device_model": "Apple / iPhone 15 Pro",
        "client_version": "5.0.1.15281",
        "os_version": "26.0.1"
    }
    ```



