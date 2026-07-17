
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network device logs` | None |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `` |
| Category | `network`, `web` |
| Type | `access`, `connection` |




### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "test_web.json"

    ```json
	
    {
        "message": "\"2025-01-06 13:39:24\",\"SIG2-Denver\",\"1.1.1.1\",\"4.4.4.4\",\"4.4.4.4\",\"\",\"ALLOWED\",\"https://example.com\",\"\",\"\",\"200\",\"1557\",\"6441\",\"\",\"\",\"Software/Technology,Allow List,Computers and Internet\",\"\",\"\",\"\",\"\",\"\",\"Network Tunnels\",\"\",\"SIG2-EX,RTO-XXXX-SIG\",\"Network Tunnels,Internal Networks\",\"CONNECT\",\"\",\"\",\"\",\"13368132\",\"610352\",\"9999583\",\"not_isolated\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"nginx-proxy-abc123.example.net\",\"DEN1\",\"true\",\"winatp-gw-eus.microsoft.com\",\"false\",\"false\",\"\",\"\",\"REDACTED\",\"\",\"\",\"3.3.3.3\",\"deepseek-v3\",\"Prohibited Suppliers, Copyleft License\",\"e846afe0f3c8a87f\"",
        "event": {
            "action": "allowed",
            "category": [
                "network",
                "web"
            ],
            "dataset": "web",
            "outcome": [
                "success"
            ],
            "type": [
                "access",
                "connection"
            ]
        },
        "@timestamp": "2025-01-06T13:39:24Z",
        "cisco_secure_access": {
            "web": {
                "ai_model_name": "deepseek-v3",
                "ai_supply_chain_categories": [
                    "Copyleft License",
                    "Prohibited Suppliers"
                ],
                "categories": [
                    "Allow List",
                    "Computers and Internet",
                    "Software/Technology"
                ],
                "data_center": "DEN1",
                "destination_list_ids": [
                    "9999583"
                ],
                "egress": true,
                "egress_ip": "3.3.3.3",
                "event_correlation_id": "e846afe0f3c8a87f",
                "identities": [
                    "RTO-XXXX-SIG",
                    "SIG2-EX"
                ],
                "identity_types": [
                    "Internal Networks",
                    "Network Tunnels"
                ],
                "isolate_action": "not_isolated",
                "policy_identity_label": "SIG2-Denver",
                "policy_identity_type": "Network Tunnels",
                "security_overridden": false,
                "time_based_rule": false
            }
        },
        "destination": {
            "address": "example.com",
            "domain": "example.com",
            "ip": "4.4.4.4",
            "registered_domain": "example.com",
            "top_level_domain": "com"
        },
        "host": {
            "hostname": "nginx-proxy-abc123.example.net",
            "name": "nginx-proxy-abc123.example.net"
        },
        "http": {
            "request": {
                "bytes": 1557,
                "method": "CONNECT"
            },
            "response": {
                "bytes": 6441,
                "status_code": 200
            }
        },
        "observer": {
            "product": "Secure Access",
            "type": "proxy",
            "vendor": "Cisco"
        },
        "organization": {
            "id": "REDACTED"
        },
        "related": {
            "hosts": [
                "example.com",
                "nginx-proxy-abc123.example.net"
            ],
            "ip": [
                "1.1.1.1",
                "4.4.4.4"
            ]
        },
        "rule": {
            "id": "610352",
            "ruleset": "13368132"
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "nat": {
                "ip": "4.4.4.4"
            }
        },
        "tls": {
            "client": {
                "server_name": "winatp-gw-eus.microsoft.com"
            }
        },
        "url": {
            "domain": "example.com",
            "full": "https://example.com",
            "original": "https://example.com",
            "port": 443,
            "registered_domain": "example.com",
            "scheme": "https",
            "top_level_domain": "com"
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`cisco_secure_access.web.ai_model_name` | `keyword` | Indicates the name of the AI model involved in the transaction or event. |
|`cisco_secure_access.web.ai_supply_chain_categories` | `keyword` | The list of AI supply chain categories associated with the event. |
|`cisco_secure_access.web.amp.disposition` | `keyword` | The status of the files proxied and scanned by Cisco Advanced Malware Protection (AMP) as part of the File Inspection feature. |
|`cisco_secure_access.web.amp.malware_name` | `keyword` | If Malicious, the name of the malware according to AMP. |
|`cisco_secure_access.web.amp.score` | `keyword` | The score of the malware from AMP. |
|`cisco_secure_access.web.application_entity_category` | `keyword` | It represents the classification grouping of application entities based on shared characteristics or functions. |
|`cisco_secure_access.web.application_entity_name` | `keyword` | It refers to the specific name of an application entity within a system. For example, the YouTube Channel "Cisco". |
|`cisco_secure_access.web.application_ids` | `keyword` | The ID of the destination application. |
|`cisco_secure_access.web.av_detections` | `keyword` | The detection name according to the antivirus engine used in file inspection. |
|`cisco_secure_access.web.blocked_categories` | `keyword` | The category that resulted in the destination being blocked. |
|`cisco_secure_access.web.categories` | `keyword` | The security categories for this request, such as Malware. |
|`cisco_secure_access.web.certificate_errors` | `keyword` | Any certificate or protocol errors in the request. |
|`cisco_secure_access.web.data_center` | `keyword` | The name of the data center that processed the user-generated traffic. |
|`cisco_secure_access.web.destination_list_ids` | `keyword` | The ID number assigned to a destination list. |
|`cisco_secure_access.web.detected_response_file_type` | `keyword` | The file type that resulted in a blocked response. |
|`cisco_secure_access.web.dlp_status` | `keyword` | If the request was Blocked for DLP. |
|`cisco_secure_access.web.egress` | `boolean` | TRUE indicates that the egress IP was a reserved IP. |
|`cisco_secure_access.web.egress_ip` | `ip` | The public IP address assigned to a session as it exits the Secure Access ZTA infrastructure en route to the destination application. |
|`cisco_secure_access.web.event_correlation_id` | `keyword` | A unique identifier generated for each network request, the Event Correlation ID stitches together all related events across various security services (Firewall, SWG, ZTNA) to provide a unified, end-to-end view of a single traffic flow. |
|`cisco_secure_access.web.file_action` | `keyword` | The action taken on a file in a remote browser isolation session. |
|`cisco_secure_access.web.forwarding_method` | `keyword` | The method used to forward the proxy events. |
|`cisco_secure_access.web.identities` | `keyword` | All identities associated with this request. |
|`cisco_secure_access.web.identity_types` | `keyword` | The type of identities that were associated with the request. |
|`cisco_secure_access.web.isolate_action` | `keyword` | The remote browser isolation state associated with the request. |
|`cisco_secure_access.web.msp_organization_id` | `keyword` | The Secure Access parent organization ID. |
|`cisco_secure_access.web.policy_identity_label` | `keyword` | The identity that made the request. |
|`cisco_secure_access.web.policy_identity_type` | `keyword` | The first identity type that made the request. |
|`cisco_secure_access.web.producer` | `keyword` | The producer of the proxy events. |
|`cisco_secure_access.web.puas` | `keyword` | A list of all potentially unwanted application (PUA) results for the proxied file as returned by the antivirus scanner. |
|`cisco_secure_access.web.security_overridden` | `boolean` | TRUE indicates that security filtering was explicitly overridden and not applied during enforcement. |
|`cisco_secure_access.web.time_based_rule` | `boolean` | TRUE indicates that a the rule was applied due to a time condition. |
|`cisco_secure_access.web.warn_categories` | `keyword` | The ID of one or more content categories in lists matched for a Warn action by the rule. |
|`cisco_secure_access.web.warn_status` | `keyword` | The Warn page's state associated with the request. |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.geo.country_iso_code` | `keyword` | Country ISO code. |
|`destination.ip` | `ip` | IP address of the destination. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.hash.sha256` | `keyword` | SHA256 hash. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.name` | `keyword` | Name of the host. |
|`http.request.bytes` | `long` | Total size in bytes of the request (body and headers). |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`http.response.body.bytes` | `long` | Size in bytes of the response body. |
|`http.response.bytes` | `long` | Total size in bytes of the response (body and headers). |
|`http.response.mime_type` | `keyword` | Mime type of the body of the response. |
|`http.response.status_code` | `long` | HTTP response status code. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`organization.id` | `keyword` | Unique identifier for the organization. |
|`rule.id` | `keyword` | Rule ID |
|`rule.ruleset` | `keyword` | Rule ruleset |
|`source.ip` | `ip` | IP address of the source. |
|`source.nat.ip` | `ip` | Source NAT ip |
|`tls.client.server_name` | `keyword` | Hostname the client is trying to connect to. Also called the SNI. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/CiscoSecureAccess/cisco-secure-access-web).