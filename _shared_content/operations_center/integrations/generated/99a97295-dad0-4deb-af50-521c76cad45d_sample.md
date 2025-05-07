
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_1"


    ```json
	{
        "time": "2025-04-30T09:07:40.986182+00:00",
        "flowLogVersion": 4,
        "flowLogGUID": "flowLogGUID1",
        "macAddress": "112233445566",
        "operationName": "FlowLogFlowEvent",
        "aclID": "aclID1",
        "rule": "DefaultRule_AllowInternetOutBound",
        "flow.0": "1663146003599,1.2.3.4,192.0.2.180,23956,443,6,O,B,NX,0,0,0,0"
    }
    ```



=== "test_2"


    ```json
	{
        "time": "2025-04-30T09:07:40.986182+00:00",
        "flowLogVersion": 4,
        "flowLogGUID": "flowLogGUID1",
        "macAddress": "112233445566",
        "operationName": "FlowLogFlowEvent",
        "aclID": "aclID1",
        "rule": "DefaultRule_AllowInternetOutBound",
        "flow.0": "1663146003606,1.2.3.4,192.0.2.180,23956,443,6,O,E,NX,3,767,2,1580"
    }
    ```



=== "test_3"


    ```json
	{
        "time": "2025-04-30T09:07:40.986182+00:00",
        "flowLogVersion": 4,
        "flowLogGUID": "flowLogGUID1",
        "macAddress": "112233445566",
        "operationName": "FlowLogFlowEvent",
        "aclID": "aclID2",
        "rule": "BlockHighRiskTCPPortsFromInternet",
        "flow.0": "1663145998065,8.7.6.5,1.2.3.4,55188,22,6,I,D,NX,0,0,0,0"
    }
    ```



=== "test_4"


    ```json
	{
        "time": "2025-04-30T09:07:40.986182+00:00",
        "flowLogVersion": 4,
        "flowLogGUID": "flowLogGUID1",
        "macAddress": "112233445566",
        "operationName": "FlowLogFlowEvent",
        "aclID": "aclID2",
        "rule": "BlockHighRiskTCPPortsFromInternet",
        "flow.0": "1663146005503,2.3.4.5,1.2.3.4,35276,119,6,I,D,NX,0,0,0,0"
    }
    ```



=== "test_5"


    ```json
	{
        "time": "2025-04-30T09:07:40.986182+00:00",
        "flowLogVersion": 4,
        "flowLogGUID": "flowLogGUID1",
        "macAddress": "112233445566",
        "operationName": "FlowLogFlowEvent",
        "aclID": "aclID2",
        "rule": "Internet",
        "flow.0": "1663145989563,3.4.5.6,1.2.3.4,50557,44357,6,I,D,NX,0,0,0,0"
    }
    ```



=== "test_6"


    ```json
	{
        "time": "2025-04-30T09:07:40.986182+00:00",
        "flowLogVersion": 4,
        "flowLogGUID": "flowLogGUID1",
        "macAddress": "112233445566",
        "operationName": "FlowLogFlowEvent",
        "aclID": "aclID2",
        "rule": "Internet",
        "flow.0": "1663145989679,1.2.3.81,1.2.3.4,62797,35945,6,I,D,NX,0,0,0,0"
    }
    ```



