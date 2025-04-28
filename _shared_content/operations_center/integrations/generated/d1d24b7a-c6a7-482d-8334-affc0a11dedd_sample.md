
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_app_event"


    ```json
	{
        "@timestamp": "2025-04-23T08:01:30.194581713Z",
        "_id": "-7246427294948959060",
        "_visitor_id": "fbeecefaceeeeae8b1598beeefeeeeee",
        "action": "block",
        "api_endpoint": "UNKNOWN",
        "app": "test_app",
        "app_firewall_name": "demo-app-firwall",
        "app_type": "demo-app",
        "as_number": "27888",
        "as_org": "test_as_org",
        "asn": "test_asn",
        "attack_types": [
            {
                "name": "ATTACK_TYPE_SERVER_SIDE_CODE_INJECTION"
            },
            {
                "name": "ATTACK_TYPE_CROSS_SITE_SCRIPTING"
            }
        ],
        "authority": "test.tenant.f5demos.com",
        "bot_info": {
            "classification": "suspicious",
            "name": "curl",
            "type": "HTTP Library"
        },
        "browser_type": "curl",
        "city": "Santiago",
        "cluster_name": "test_cluster",
        "content-type": "text/plain",
        "country": "CL",
        "detections": [],
        "device_type": "Other",
        "domain": "test.tenant.f5demos.com",
        "dst": "",
        "dst_instance": "",
        "dst_ip": "7.1.3.1",
        "dst_port": "0",
        "dst_site": "",
        "enforcement_mode": "Blocking",
        "excluded_threat_campaigns": [],
        "host": "1.5.5.1",
        "hostname": "test-1",
        "http_version": "HTTP/1.1",
        "ja4_tls_fingerprint": "",
        "kubernetes": {
            "container_name": "test_container",
            "host": "hosttest-1",
            "labels": {
                "app": "test_app"
            },
            "namespace_name": "test-system",
            "pod_id": "2e7f9ccc-eeee-49a2-9333-edcd0eae6aa8",
            "pod_name": "test_pod_name"
        },
        "latitude": "-33.450001",
        "longitude": "-70.650002",
        "messageid": "c122227e-dddd-5555-b495-71bf4217a9f6",
        "method": "POST",
        "namespace": "demo-app-waap",
        "network": "1.7.7.2",
        "no_active_detections": false,
        "original_path": "/api/2.0/services/usermgmt/password/test",
        "recommended_action": "block",
        "region": "CL-RM",
        "req_headers": "{\"Accept\":\"*/*\",\"Content-Length\":\"474\",\"Content-Type\":\"text/plain\",\"Cookie\":\"_imp_apg_r_=1999000666803999\",\"Host\":\"test.tenant.f5demos.com\",\"Method\":\"POST\",\"Scheme\":\"https\",\"User-Agent\":\"curl/7.68.0\",\"X-Envoy-External-Address\":\"5.1.8.1\",\"X-F5-Request-Id\":\"e4366678-4999-4222-9999-f3999aaaae6\",\"X-Forwarded-For\":\"5.1.8.1\",\"X-Forwarded-Proto\":\"https\",\"X-Request-Id\":\"e4367778-4999-4222-9999-f39d7aaaaae6\",\"Xff\":\"1.7.7.2\"}",
        "req_headers_size": 363,
        "req_id": "e4337777-4222-4222-9999-f99daaab4116",
        "req_params": "",
        "req_path": "/api/2.0/services/usermgmt/password/test",
        "req_size": "837",
        "rsp_code": "200",
        "rsp_code_class": "2xx",
        "rsp_size": "0",
        "sec_event_name": "WAF",
        "sec_event_type": "waf_sec_event",
        "severity": "info",
        "signatures": [
            {
                "accuracy": "high_accuracy",
                "attack_type": "ATTACK_TYPE_CROSS_SITE_SCRIPTING",
                "context": "body",
                "id": "200001862",
                "id_name": "200001862, Vulnerability tool listener - Interactsh (Parameter)",
                "matching_info": "Matched 10 characters on offset 27 against value: 'ff88a000010gj.test.site</string>\n        </comman'. ",
                "name": "Vulnerability tool listener - Interactsh (Parameter)",
                "risk": "Medium",
                "state": "Enabled"
            },
            {
                "accuracy": "medium_accuracy",
                "attack_type": "ATTACK_TYPE_SERVER_SIDE_CODE_INJECTION",
                "context": "body",
                "id": "200004472",
                "id_name": "200000072, Java code injection - ProcessBuilder (Parameter)",
                "matching_info": "Matched 24 characters on offset 20 against value: '     <target class=\"java.lang.ProcessBuilder\">\n        <command'. ",
                "name": "Java code injection - ProcessBuilder (Parameter)",
                "risk": "High",
                "state": "Enabled"
            }
        ],
        "site": "test-site",
        "sni": "test.tenant.f5demos.com",
        "src": "N:public",
        "src_instance": "CC",
        "src_ip": "1.7.7.2",
        "src_port": "0",
        "src_site": "test-site",
        "stream": "test",
        "tag": "test.tag",
        "tenant": "f5-test-tenant",
        "threat_campaigns": [
            {
                "attack_type": "ATTACK_TYPE_SERVER_SIDE_CODE_INJECTION",
                "id": "cmp555555555555555555cc72845e59c5a4",
                "id_name": "cmp555555555555555555cc72845e59c5a4, VMWare NSX Manager 'XStream' Remote Code Execution - test",
                "name": "VMWare NSX Manager 'XStream' Remote Code Execution - test",
                "state": "Enabled"
            }
        ],
        "time": "2025-04-23T08:01:30.194Z",
        "tls_fingerprint": "f436b9416f37d134cadd00000000000e8",
        "user": "Cookie-_imp_apg_r_-00000000080396b",
        "user_agent": "curl/7.68.0",
        "vh_name": "ves-io-http-loadbalancer-arcadia-re-ce",
        "vhost_id": "c3333333-1111-4444-bbbb-f9139229bcda",
        "violation_rating": "5",
        "violations": [],
        "waf_mode": "block",
        "x_forwarded_for": "5.1.8.1"
    }
    ```



=== "test_openapi_failure_event"


    ```json
	{
        "@timestamp": "2025-04-23T08:01:08.481975167Z",
        "_id": "5765504561525734669",
        "_visitor_id": "9b88292873332155956246853111",
        "action": "allow",
        "api_endpoint": "/api/locations",
        "app": "test_app",
        "app_type": "demo-app-sentence-api",
        "asn": "PRIVATE",
        "authority": "test.sentence.f5.com",
        "browser_type": "curl",
        "city": "PRIVATE",
        "cluster_name": "test_cluster_name",
        "country": "PRIVATE",
        "device_type": "Other",
        "domain": "test.f5demos.com",
        "dst": "S:sentence.test.com",
        "dst_instance": "2.7.2.5",
        "dst_ip": "2.7.2.5",
        "dst_port": "80",
        "dst_site": "test_dst_site",
        "host": "1.5.5.2",
        "hostname": "test_hostname",
        "http_version": "",
        "jwt_action": "",
        "jwt_missing_claim": "",
        "jwt_status": "",
        "kubernetes": {
            "container_name": "test_container_name",
            "host": "test_host",
            "labels": {
                "app": "test_app"
            },
            "namespace_name": "test_name_space",
            "pod_id": "5cc2748f-8999-4444-a777-352e9d555555",
            "pod_name": "test_pod_name"
        },
        "latitude": "PRIVATE",
        "longitude": "PRIVATE",
        "messageid": "308a7550-c6ed-1111-9999-0000ac000002",
        "method": "GET",
        "namespace": "test_namespace",
        "network": "PRIVATE",
        "no_active_detections": false,
        "oas_req_status": "OpenAPIViolation",
        "oas_rsp_status": "OpenAPIValidationSuccessful",
        "policy_hits": {
            "policy_hits": []
        },
        "recommended_action": "",
        "region": "PRIVATE",
        "req_headers": "{\":authority\":\"test.f5se.com\",\":method\":\"GET\",\":path\":\"/api/locations\",\":scheme\":\"https\",\"accept\":\"*/*\",\"cookie\":\"_imp_apg_r_=bbd188330192000\",\"user-agent\":\"curl/7.68.0\",\"x-envoy-external-address\":\"5.1.8.1\",\"x-envoy-original-authority\":\"test.f5demos.com\",\"x-forwarded-for\":\"5.1.8.1\",\"x-forwarded-proto\":\"https\",\"x-request-id\":\"c3334487-ffff-4666-dddd-042222474747\",\"x-volterra-truncated-hdr\":\"false\",\"xff\":\"2.1.2.1\"}",
        "req_headers_size": 0,
        "req_id": "c3338787-f444-6666-dddd-042222474747",
        "req_params": "",
        "req_path": "/api/locations",
        "req_size": "347",
        "rsp_code": "200",
        "rsp_code_class": "2xx",
        "rsp_size": "565656",
        "sec_event_name": "OpenAPI Validation Failure",
        "sec_event_type": "api_sec_event",
        "severity": "info",
        "signatures": [],
        "site": "test_site",
        "sni": "test_sni",
        "src": "N:public",
        "src_instance": "UNKNOWN",
        "src_ip": "2.1.2.1",
        "src_port": "0",
        "src_site": "test_src_site",
        "stream": "test_stream",
        "tag": "test_tag",
        "tenant": "test_tenant",
        "time": "2025-04-23T08:01:08.481Z",
        "tls_fingerprint": "f43339666f3333344444048863273338",
        "user": "Cookie-_imp_apg_r_-bbb11333009000ee",
        "user_agent": "curl/7.68.0",
        "vh_name": "vh-name-http-api",
        "vhost_id": "f6333233-3333-4333-8333-333342973524",
        "violations": [
            {
                "context": "Request",
                "description": "HTTP Authorization header not found",
                "field": "",
                "property": "Security Schema",
                "value": ""
            }
        ],
        "x_forwarded_for": "5.1.8.1"
    }
    ```



=== "test_user_event"


    ```json
	{
        "@timestamp": "2025-04-23T08:01:29.654864030Z",
        "_id": "760346923814373991",
        "apiep_anomaly": 0,
        "app": "test_app",
        "app_type": "test_app_type",
        "asn": "test_asn",
        "behavior_anomaly_score": 0.008055687709681115,
        "bot_defense_sec_event_count": 0,
        "bot_defense_suspicion_score": 0.0,
        "city": "New York",
        "cluster_name": "test_cluster_name",
        "country": "US",
        "end_time": 1755355222,
        "err_count": 0,
        "failed_login_count": 0,
        "failed_login_suspicion_score": 0.0,
        "feature_score": "{\"apiEntropyData\":0,\"errorRate\":0,\"requestRate\":0}",
        "forbidden_access_count": 0,
        "forbidden_access_suspicion_score": 0.0,
        "host": "1.5.5.1",
        "hostname": "test_hostname",
        "incremental_activity_info": "{\"bot_defense_sec_event_count\":0,\"err_count\":0,\"failed_login_count\":0,\"forbidden_access_count\":0,\"page_not_found_count\":0,\"rate_limiting_count\":0,\"req_count\":0,\"waf_sec_event_count\":0}",
        "ip_reputation_suspicion_score": 0.0,
        "kubernetes": {
            "container_name": "test_container",
            "host": "test_host",
            "labels": {
                "app": "test_app"
            },
            "namespace_name": "test_namespace",
            "pod_id": "6daaceeb-4222-4999-9999-559310825ee0",
            "pod_name": "test_pod_name"
        },
        "latitude": "40.740002",
        "longitude": "-74.000000",
        "message": "User Suspicion Score",
        "messageid": "666aaaaa-3333-4777-aeee-227763355777",
        "method_counts": "{\"CONNECT\":0,\"DELETE\":0,\"GET\":50,\"HEAD\":0,\"OPTIONS\":0,\"PATH\":0,\"POST\":300,\"PUT\":0,\"TRACE\":0}",
        "mitigation_activity_info": "{\"mum_captcha_challenge\":0,\"mum_js_challenge\":0,\"mum_temporarily_blocking\":0}",
        "namespace": "test_namespace",
        "network": "2.1.5.0",
        "page_not_found_count": 0,
        "rate_limit_suspicion_score": 0.0,
        "rate_limiting_count": 0,
        "region": "US-NY",
        "req_count": 32,
        "sec_event_type": "malicious_user_sec_event",
        "severity": "info",
        "site": "test_site",
        "src_ip": "2.1.5.6",
        "start_time": 1749999999,
        "stream": "test_stream",
        "summary_msg": "No activity in last 5 minutes.",
        "suspicion_log_type": "no_critical_activity",
        "suspicion_score": 0.833097360071607,
        "tag": "test_tag",
        "tenant": "test_tenant",
        "threat_level": "Medium",
        "time": "2025-04-23T08:01:29.654Z",
        "user": "Cookie-_imp_apg_r_-4c90999000006666",
        "vh_name": "test_vh_name",
        "waf_sec_event_count": 29,
        "waf_suspicion_score": 0.8250416723619258
    }
    ```



