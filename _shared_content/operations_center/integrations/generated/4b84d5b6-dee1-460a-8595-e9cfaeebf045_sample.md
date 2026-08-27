
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_api_audit_1"

    ```
	INFO  2020-05-29 06:27:13,742 clientType=External||userName=00000000-0000-0000-0000-000000000000||NutanixApiVersion=1.0||httpMethod=GET||restEndpoint=/v1/users/details||entityUuid=||queryParams=kind=admin||payload=
    ```



=== "test_audit_1"

    ```
	{
        "affectedEntityList": [
            {
                "entityType": "cluster",
                "name": "Unnamed",
                "uuid": "00000000-0000-0000-0000-000000000000"
            }
        ],
        "alertUid": "PairingAudit",
        "creationTimestampUsecs": "1590479209937393",
        "defaultMsg": "Failed to pair with remote prism central None: Internal Server Error. Could not create remote connection. Skip pairing",
        "opEndTimestampUsecs": "1590479209649077",
        "opStartTimestampUsecs": "1590479209649077",
        "operationType": "Create",
        "originatingClusterUuid": "44444444-4444-4444-4444-444444444444",
        "params": {
            "remote_cluster_url": ""
        },
        "recordType": "Audit",
        "severity": "Audit",
        "tenantUuid": "org-12345678",
        "userName": "j.doe@example.com",
        "userUuid": "22222222-2222-2222-2222-222222222222",
        "uuid": "11111111-1111-1111-1111-111111111111"
    }
    ```



=== "test_flow_service_1"

    ```
	INFO:2020/06/03 12:12:18  [00000000-0000-0000-0000-000000000000] dt_isolation [Update] SRC=192.0.2.10 DST=192.0.2.20 PROTO=TCP SPORT=22 DPORT=40726 ACTION=DROP ORIG: PKTS=9 BYTES=468 REPLY: PKTS=0 BYTES=0
    ```



=== "test_security_policy_hit_1"

    ```
	INFO:2020/06/03 12:12:18  [00000000-0000-0000-0000-000000000001] isolation-policy [Update] SRC=192.0.2.30 DST=192.0.2.40 PROTO=TCP SPORT=22 DPORT=40726 ACTION=DROP ORIG: PKTS=9 BYTES=468 REPLY: PKTS=0 BYTES=0
    ```



