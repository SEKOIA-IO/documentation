
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_network"


    ```json
	{
        "AccountID": "1d1e650b3385b95db72bba7cfb1287e9",
        "Action": "allowedOnNoRuleMatch",
        "Datetime": "2023-02-24T16:33:05Z",
        "DestinationIP": "104.244.42.193",
        "DestinationPort": 443,
        "DeviceID": "",
        "DeviceName": "",
        "Email": "",
        "OverrideIP": "",
        "OverridePort": 0,
        "PolicyID": "",
        "PolicyName": "",
        "SNI": "www.twitter.com",
        "SessionID": "1725de7a2d0000215517735400000001",
        "SourceIP": "15.188.186.81",
        "SourcePort": 34080,
        "Transport": "tcp",
        "UserID": ""
    }
    ```



=== "test_network_device"


    ```json
	{
        "AccountID": "1d1e650b3385b95db72bba7cfb1287e9",
        "Action": "allowedOnNoRuleMatch",
        "Datetime": "2023-05-02T16:24:20Z",
        "DestinationIP": "104.18.5.35",
        "DestinationPort": 443,
        "DeviceID": "b72ac397-e5c3-913e-11ed-03face9f2b6b",
        "DeviceName": "DESKTOP-ABCDEF",
        "Email": "john.doe@test.com",
        "OverrideIP": "",
        "OverridePort": 0,
        "PolicyID": "",
        "PolicyName": "",
        "SNI": "commandandcontrolandbotnet.testcategory.com",
        "SessionID": "187ee08b7d00003d0d8e47f400000001",
        "SourceIP": "15.188.186.81",
        "SourceInternalIP": "",
        "SourcePort": 54945,
        "Transport": "tcp",
        "UserID": "2c46cdd9-92e3-5e5f-b3cf-67965d7c33e3"
    }
    ```



=== "test_network_no_sni"


    ```json
	{
        "AccountID": "1d1e650b3385b95db72bba7cfb1287e9",
        "Action": "allowedOnNoRuleMatch",
        "Datetime": "2023-02-24T16:33:05Z",
        "DestinationIP": "104.244.42.193",
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
        "SourceIP": "15.188.186.81",
        "SourcePort": 34080,
        "Transport": "tcp",
        "UserID": ""
    }
    ```



