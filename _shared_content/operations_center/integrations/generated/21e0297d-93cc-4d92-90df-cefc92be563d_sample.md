
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "conn"


    ```json
	{
        "_path": "conn",
        "_system_name": "sensor",
        "uid": "CGAXp90w9BVzA9KJf",
        "ts": "2025-03-06T20:20:18.552640Z",
        "id.orig_h": "10.10.199.202",
        "id.orig_p": 59694,
        "id.resp_h": "203.0.113.125",
        "id.resp_p": 5222,
        "proto": "tcp",
        "duration": 14.604184,
        "orig_bytes": 24,
        "resp_bytes": 23,
        "conn_state": "OTH",
        "local_orig": true,
        "local_resp": false,
        "missed_bytes": 0,
        "history": "DadA",
        "enrichment_orig.role": "Developer",
        "enrichment_orig.user": "John Doe",
        "enrichment_orig.city_location": "Arlington, VA",
        "enrichment_orig.building": "Workstation Hotel",
        "community_id": "1:mKFqUrNZNgj9CY71jy3UIDILWs4="
    }
    ```



=== "dns"


    ```json
	{
        "_path": "dns",
        "_system_name": "sensor",
        "ts": "2025-03-06T20:20:18.552640Z",
        "uid": "CdnsTest123456",
        "id.orig_h": "10.0.35.10",
        "id.orig_p": 51000,
        "id.resp_h": "203.0.113.198",
        "id.resp_p": 53,
        "query": "abcdef0123456789.tunnel.example.com",
        "qtype_name": "NULL",
        "rcode_name": "NOERROR",
        "answers": [
            "10.0.0.1"
        ]
    }
    ```



=== "files"


    ```json
	{
        "_path": "files",
        "_system_name": "sensor",
        "ts": "2025-03-06T20:23:38.591404Z",
        "uid": "CfilesTest123",
        "id.orig_h": "10.0.35.10",
        "id.resp_h": "203.0.113.198",
        "source": "HTTP",
        "md5": "0cea15a1205bcfa2b91de90fcc566d6c",
        "sha1": "caf07a8bdbd1c9ad3474fd6a31fefdcdc8964c5f",
        "sha256": "75475fb40984ddb7c83638cb1f4a79827396ba7b638e501f7aff6293adb8cf51",
        "mime_type": "application/x-dosexec",
        "seen_bytes": 539136
    }
    ```



=== "http"


    ```json
	{
        "_path": "http",
        "_system_name": "sensor",
        "ts": "2025-03-06T20:20:18.552640Z",
        "uid": "CbsaT01N3Llhz2HRoa",
        "id.orig_h": "10.1.146.99",
        "id.orig_p": 51000,
        "id.resp_h": "203.0.113.131",
        "id.resp_p": 80,
        "host": "c.example.com",
        "method": "GET",
        "uri": "/r/r4.crl",
        "request_body_len": 0,
        "response_body_len": 0,
        "status_code": 304,
        "status_msg": "Not Modified",
        "user_agent": "Microsoft-CryptoAPI/10.0"
    }
    ```



=== "intel"


    ```json
	{
        "_path": "intel",
        "_system_name": "sensor",
        "ts": "2018-05-21T20:58:18.214197Z",
        "uid": "CintelTest12",
        "id.orig_h": "10.0.0.1",
        "id.orig_p": 55552,
        "id.resp_h": "203.0.113.94",
        "id.resp_p": 53,
        "seen.indicator": "evil.example.com",
        "seen.indicator_type": "Intel::DOMAIN",
        "seen.where": "DNS::IN_REQUEST",
        "matched": [
            "Intel::DOMAIN"
        ],
        "sources": [
            "MyList"
        ]
    }
    ```



=== "notice"


    ```json
	{
        "_path": "notice",
        "_system_name": "sensor",
        "ts": "2025-03-06T20:20:18.552640Z",
        "uid": "CnoticeTest1",
        "id.orig_h": "10.0.35.10",
        "id.resp_h": "192.168.100.10",
        "note": "ATTACK::Lateral_Movement",
        "msg": "SMB::FILE_WRITE to admin file share",
        "sub": "Saved a copy of the file written to SMB admin file share"
    }
    ```



=== "ssl"


    ```json
	{
        "_path": "ssl",
        "_system_name": "sensor",
        "ts": "2025-03-06T20:26:09.490256Z",
        "uid": "Cx0XUo11iFOMEEz2Ck",
        "id.orig_h": "10.1.75.180",
        "id.orig_p": 54122,
        "id.resp_h": "203.0.113.32",
        "id.resp_p": 443,
        "version": "TLSv13",
        "cipher": "TLS_AES_256_GCM_SHA384",
        "curve": "secp384r1",
        "established": true,
        "ja3": "d76a5a80b4bb0c75ac45782b0b53da91",
        "ja3s": "15af977ce25de452b96affa2addb1036",
        "server_name": "westus-0.in.applicationinsights.azure.com",
        "validation_status": "self signed certificate"
    }
    ```



=== "suricata_corelight"


    ```json
	{
        "_path": "suricata_corelight",
        "_system_name": "sensor.lan",
        "_write_ts": "2020-04-20T18:47:54.345633Z",
        "ts": "2020-04-20T18:47:54.339051Z",
        "uid": "CoO6zA3B7cX7KT6v07",
        "id.orig_h": "10.3.11.194",
        "id.orig_p": 50136,
        "id.resp_h": "203.0.113.98",
        "id.resp_p": 447,
        "suri_id": "SYy9Irj5XdH2",
        "service": "tls",
        "flow_id": 504752850478551,
        "tx_id": 0,
        "alert.action": "allowed",
        "alert.gid": 1,
        "alert.signature_id": 2810654,
        "alert.rev": 4,
        "alert.signature": "ETPRO POLICY Possibly Suspicious example.com SSL Cert",
        "alert.category": "A Network Trojan was detected",
        "alert.severity": 1,
        "community_id": "1:q5mSw5JpjV6tvM5dzM00Y0AQDlc="
    }
    ```



