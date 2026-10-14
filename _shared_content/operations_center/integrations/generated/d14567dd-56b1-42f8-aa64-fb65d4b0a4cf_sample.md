
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_network"


    ```json
	{
        "AccountID": "00000000-0000-0000-0000-000000000000",
        "Action": "allowedOnNoRuleMatch",
        "Datetime": "2023-02-24T16:33:05Z",
        "DestinationIP": "198.51.100.40",
        "DestinationPort": 443,
        "DeviceID": "",
        "DeviceName": "",
        "Email": "",
        "OverrideIP": "",
        "OverridePort": 0,
        "PolicyID": "",
        "PolicyName": "",
        "SNI": "host.example.com",
        "SessionID": "1725de7a2d0000215517735400000001",
        "SourceIP": "198.51.100.34",
        "SourcePort": 34080,
        "Transport": "tcp",
        "UserID": ""
    }
    ```



=== "test_network_device"


    ```json
	{
        "AccountID": "00000000-0000-0000-0000-000000000000",
        "Action": "allowedOnNoRuleMatch",
        "Datetime": "2023-05-02T16:24:20Z",
        "DestinationIP": "198.51.100.39",
        "DestinationPort": 443,
        "DeviceID": "b72ac397-e5c3-913e-11ed-03face9f2b6b",
        "DeviceName": "host.example.com",
        "Email": "john.doe@test.com",
        "OverrideIP": "",
        "OverridePort": 0,
        "PolicyID": "",
        "PolicyName": "",
        "SNI": "host.example.com",
        "SessionID": "187ee08b7d00003d0d8e47f400000001",
        "SourceIP": "198.51.100.34",
        "SourceInternalIP": "",
        "SourcePort": 54945,
        "Transport": "tcp",
        "UserID": "00000000-0000-0000-0000-000000000000"
    }
    ```



=== "test_network_no_sni"


    ```json
	{
        "AccountID": "00000000-0000-0000-0000-000000000000",
        "Action": "allowedOnNoRuleMatch",
        "Datetime": "2023-02-24T16:33:05Z",
        "DestinationIP": "198.51.100.40",
        "DestinationPort": 443,
        "DeviceID": "",
        "DeviceName": "",
        "Email": "",
        "OverrideIP": "",
        "OverridePort": 0,
        "PolicyID": "",
        "PolicyName": "",
        "SNI": "",
        "SessionID": "1725de7a2d0000215517735400000001",
        "SourceIP": "198.51.100.34",
        "SourcePort": 34080,
        "Transport": "tcp",
        "UserID": ""
    }
    ```



