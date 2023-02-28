
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web application firewall logs` | AWS protect web application with its web application firewall |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network` |
| Type | `access` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "Block1.json"

    ```json
	
    {
        "message": "{\"timestamp\":1669549802503,\"formatVersion\":1,\"webaclId\":\"arn:aws:wafv2:us-east-1:582598250481:global/webacl/ACME/41f0e583-5098\",\"terminatingRuleId\":\"XSS-Detection-URL\",\"terminatingRuleType\":\"REGULAR\",\"action\":\"BLOCK\",\"terminatingRuleMatchDetails\":[{\"conditionType\":\"XSS\",\"location\":\"QUERY_STRING\",\"matchedData\":[\"REDACTED\"]}],\"httpSourceName\":\"CF\",\"httpSourceId\":\"E2S4G6AQPVW9DQ\",\"ruleGroupList\":[],\"rateBasedRuleList\":[],\"nonTerminatingMatchingRules\":[],\"requestHeadersInserted\":null,\"responseCodeSent\":null,\"httpRequest\":{\"clientIp\":\"84.46.249.194\",\"country\":\"DE\",\"headers\":[{\"name\":\"Host\",\"value\":\"login.ACME.com\"},{\"name\":\"User-Agent\",\"value\":\"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36\"},{\"name\":\"Connection\",\"value\":\"close\"},{\"name\":\"Accept\",\"value\":\"*/*\"},{\"name\":\"Accept-Language\",\"value\":\"en\"},{\"name\":\"Accept-Encoding\",\"value\":\"gzip\"}],\"uri\":\"/config/postProcessing/testNaming\",\"args\":\"REDACTED\",\"httpVersion\":\"HTTP/1.1\",\"httpMethod\":\"GET\",\"requestId\":\"hZV7g-jjDydLm1cVp7MhsMVf20NcU_pe0x55txifIcdG5VZxKJ78zw==\"}}",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "access"
            ],
            "module": "aws.waf",
            "action": "BLOCK",
            "reason": [
                "XSS"
            ]
        },
        "@timestamp": "2022-11-27T11:50:02.503000Z",
        "action": {
            "target": "network-traffic"
        },
        "cloud": {
            "provider": "aws",
            "service": {
                "name": "waf"
            },
            "region": "us-east-1"
        },
        "observer": {
            "type": "waf"
        },
        "aws": {
            "waf": {
                "rule": {
                    "arn": "arn:aws:wafv2:us-east-1:582598250481:global/webacl/ACME/41f0e583-5098"
                }
            }
        },
        "destination": {
            "domain": "login.ACME.com",
            "address": "login.ACME.com",
            "top_level_domain": "com",
            "subdomain": "login",
            "registered_domain": "ACME.com"
        },
        "http": {
            "request": {
                "id": "hZV7g-jjDydLm1cVp7MhsMVf20NcU_pe0x55txifIcdG5VZxKJ78zw==",
                "method": "GET"
            },
            "version": "HTTP/1.1"
        },
        "rule": {
            "category": "REGULAR",
            "name": "XSS-Detection-URL"
        },
        "source": {
            "geo": {
                "country_iso_code": "DE"
            },
            "ip": "84.46.249.194",
            "address": "84.46.249.194"
        },
        "url": {
            "original": "/config/postProcessing/testNaming",
            "path": "/config/postProcessing/testNaming"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
            "device": {
                "name": "Other"
            },
            "name": "Chrome",
            "version": "35.0.2117"
        },
        "related": {
            "hosts": [
                "login.ACME.com"
            ],
            "ip": [
                "84.46.249.194"
            ]
        },
        "os": {
            "name": "Windows",
            "version": "XP"
        }
    }
    	
	```


=== "SQL_injection.json"

    ```json
	
    {
        "message": "{\"timestamp\":1669547932510,\"formatVersion\":1,\"webaclId\":\"arn:aws:wafv2:us-east-1:582598250481:global/webacl/ACME/41f0e583-5098\",\"terminatingRuleId\":\"SQL-injection-Detection-URL\",\"terminatingRuleType\":\"REGULAR\",\"action\":\"BLOCK\",\"terminatingRuleMatchDetails\":[{\"conditionType\":\"SQL_INJECTION\",\"location\":\"BODY\",\"matchedData\":[\"email\",\"=\",\"=''or\",\"email.com\",\"=\"],\"sensitivityLevel\":\"LOW\"}],\"httpSourceName\":\"CF\",\"httpSourceId\":\"E2S4G6AQPVW9DQ\",\"ruleGroupList\":[],\"rateBasedRuleList\":[],\"nonTerminatingMatchingRules\":[],\"requestHeadersInserted\":null,\"responseCodeSent\":null,\"httpRequest\":{\"clientIp\":\"84.46.249.194\",\"country\":\"DE\",\"headers\":[{\"name\":\"Host\",\"value\":\"login.ACME.com\"},{\"name\":\"User-Agent\",\"value\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36\"},{\"name\":\"Connection\",\"value\":\"close\"},{\"name\":\"Content-Length\",\"value\":\"74\"},{\"name\":\"Accept\",\"value\":\"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\"},{\"name\":\"Content-Type\",\"value\":\"application/x-www-form-urlencoded\"},{\"name\":\"Cookie\",\"value\":\"REDACTED\"},{\"name\":\"Referer\",\"value\":\"https://login.ACME.com/login.php\"},{\"name\":\"Accept-Encoding\",\"value\":\"gzip\"}],\"uri\":\"/login.php\",\"args\":\"REDACTED\",\"httpVersion\":\"HTTP/1.1\",\"httpMethod\":\"POST\",\"requestId\":\"mVzg_KS6DmSRrKCDEA4cdK6WXSB6mVDo1z0ak8THDjiNdoOpC0yOqA==\"}}",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "access"
            ],
            "module": "aws.waf",
            "action": "BLOCK",
            "reason": [
                "SQL_INJECTION"
            ]
        },
        "@timestamp": "2022-11-27T11:18:52.510000Z",
        "action": {
            "target": "network-traffic"
        },
        "cloud": {
            "provider": "aws",
            "service": {
                "name": "waf"
            },
            "region": "us-east-1"
        },
        "observer": {
            "type": "waf"
        },
        "aws": {
            "waf": {
                "rule": {
                    "arn": "arn:aws:wafv2:us-east-1:582598250481:global/webacl/ACME/41f0e583-5098"
                }
            }
        },
        "destination": {
            "domain": "login.ACME.com",
            "address": "login.ACME.com",
            "top_level_domain": "com",
            "subdomain": "login",
            "registered_domain": "ACME.com"
        },
        "http": {
            "request": {
                "body": {
                    "bytes": 74
                },
                "id": "mVzg_KS6DmSRrKCDEA4cdK6WXSB6mVDo1z0ak8THDjiNdoOpC0yOqA==",
                "method": "POST",
                "mime_type": "application/x-www-form-urlencoded"
            },
            "version": "HTTP/1.1"
        },
        "rule": {
            "category": "REGULAR",
            "name": "SQL-injection-Detection-URL"
        },
        "source": {
            "geo": {
                "country_iso_code": "DE"
            },
            "ip": "84.46.249.194",
            "address": "84.46.249.194"
        },
        "url": {
            "original": "/login.php",
            "path": "/login.php"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            "device": {
                "name": "Other"
            },
            "name": "Chrome",
            "version": "70.0.3538"
        },
        "related": {
            "hosts": [
                "login.ACME.com"
            ],
            "ip": [
                "84.46.249.194"
            ]
        },
        "os": {
            "name": "Windows",
            "version": "10"
        }
    }
    	
	```


=== "XSS_Detection_HTML.json"

    ```json
	
    {
        "message": "{\"timestamp\":1669544590505,\"formatVersion\":1,\"webaclId\":\"arn:aws:wafv2:us-east-1:582598250481:global/webacl/ACME/41f0e583-5098\",\"terminatingRuleId\":\"XSS-Detection-HTML-tags\",\"terminatingRuleType\":\"REGULAR\",\"action\":\"BLOCK\",\"terminatingRuleMatchDetails\":[{\"conditionType\":\"XSS\",\"location\":\"QUERY_STRING\",\"matchedData\":[\"REDACTED\"]}],\"httpSourceName\":\"CF\",\"httpSourceId\":\"E2S4G6AQPVW9DQ\",\"ruleGroupList\":[],\"rateBasedRuleList\":[],\"nonTerminatingMatchingRules\":[],\"requestHeadersInserted\":null,\"responseCodeSent\":null,\"httpRequest\":{\"clientIp\":\"84.46.249.194\",\"country\":\"DE\",\"headers\":[{\"name\":\"Host\",\"value\":\"login.ACME.com\"},{\"name\":\"User-Agent\",\"value\":\"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36\"},{\"name\":\"Connection\",\"value\":\"close\"},{\"name\":\"Accept\",\"value\":\"*/*\"},{\"name\":\"Accept-Language\",\"value\":\"en\"},{\"name\":\"Accept-Encoding\",\"value\":\"gzip\"}],\"uri\":\"/wp-admin/options-general.php\",\"args\":\"REDACTED\",\"httpVersion\":\"HTTP/1.1\",\"httpMethod\":\"GET\",\"requestId\":\"n1nt9-sFYbgTvL2v6xKUDAn4GpFxtycHepSjN4bcZAB7ipZRCOijSw==\"}}",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "access"
            ],
            "module": "aws.waf",
            "action": "BLOCK",
            "reason": [
                "XSS"
            ]
        },
        "@timestamp": "2022-11-27T10:23:10.505000Z",
        "action": {
            "target": "network-traffic"
        },
        "cloud": {
            "provider": "aws",
            "service": {
                "name": "waf"
            },
            "region": "us-east-1"
        },
        "observer": {
            "type": "waf"
        },
        "aws": {
            "waf": {
                "rule": {
                    "arn": "arn:aws:wafv2:us-east-1:582598250481:global/webacl/ACME/41f0e583-5098"
                }
            }
        },
        "destination": {
            "domain": "login.ACME.com",
            "address": "login.ACME.com",
            "top_level_domain": "com",
            "subdomain": "login",
            "registered_domain": "ACME.com"
        },
        "http": {
            "request": {
                "id": "n1nt9-sFYbgTvL2v6xKUDAn4GpFxtycHepSjN4bcZAB7ipZRCOijSw==",
                "method": "GET"
            },
            "version": "HTTP/1.1"
        },
        "rule": {
            "category": "REGULAR",
            "name": "XSS-Detection-HTML-tags"
        },
        "source": {
            "geo": {
                "country_iso_code": "DE"
            },
            "ip": "84.46.249.194",
            "address": "84.46.249.194"
        },
        "url": {
            "original": "/wp-admin/options-general.php",
            "path": "/wp-admin/options-general.php"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
            "device": {
                "name": "Other"
            },
            "name": "Chrome",
            "version": "37.0.2049"
        },
        "related": {
            "hosts": [
                "login.ACME.com"
            ],
            "ip": [
                "84.46.249.194"
            ]
        },
        "os": {
            "name": "Windows",
            "version": "8.1"
        }
    }
    	
	```


=== "allow1.json"

    ```json
	
    {
        "message": "{\"timestamp\":1669449723944,\"formatVersion\":1,\"webaclId\":\"arn:aws:wafv2:us-east-1:global/webacl/ACME/41f0e583-5098\",\"terminatingRuleId\":\"Default_Action\",\"terminatingRuleType\":\"REGULAR\",\"action\":\"ALLOW\",\"terminatingRuleMatchDetails\":[],\"httpSourceName\":\"CF\",\"httpSourceId\":\"E2R57GJ4AQX5UR\",\"ruleGroupList\":[{\"ruleGroupId\":\"AWS#AWSManagedRulesAmazonIpReputationList\",\"terminatingRule\":null,\"nonTerminatingMatchingRules\":[],\"excludedRules\":null,\"customerConfig\":null}],\"rateBasedRuleList\":[],\"nonTerminatingMatchingRules\":[],\"requestHeadersInserted\":null,\"responseCodeSent\":null,\"httpRequest\":{\"clientIp\":\"30.255.150.197\",\"country\":\"IE\",\"headers\":[{\"name\":\"accept\",\"value\":\"*/*\"},{\"name\":\"content-type\",\"value\":\"application/json\"},{\"name\":\"x-client-origin\",\"value\":\"atf.team.ACME.com\"},{\"name\":\"Content-Length\",\"value\":\"183\"},{\"name\":\"User-Agent\",\"value\":\"node-fetch/1.0 (+https://github.com/bitinn/node-fetch)\"},{\"name\":\"Accept-Encoding\",\"value\":\"gzip,deflate\"},{\"name\":\"Host\",\"value\":\"api.ACME.com\"},{\"name\":\"Connection\",\"value\":\"keep-alive\"}],\"uri\":\"/graphql\",\"args\":\"REDACTED\",\"httpVersion\":\"HTTP/1.1\",\"httpMethod\":\"POST\",\"requestId\":\"e6Hwr9m4uRtjSPXu2C2K4mmiFk0n7Ubqu0EUf0CqI0uxPbUE2qWiKA==\"}}",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "access"
            ],
            "module": "aws.waf",
            "action": "ALLOW"
        },
        "@timestamp": "2022-11-26T08:02:03.944000Z",
        "action": {
            "target": "network-traffic"
        },
        "cloud": {
            "provider": "aws",
            "service": {
                "name": "waf"
            },
            "region": "us-east-1"
        },
        "observer": {
            "type": "waf"
        },
        "aws": {
            "waf": {
                "rule": {
                    "arn": "arn:aws:wafv2:us-east-1:global/webacl/ACME/41f0e583-5098"
                }
            }
        },
        "destination": {
            "domain": "api.ACME.com",
            "address": "api.ACME.com",
            "top_level_domain": "com",
            "subdomain": "api",
            "registered_domain": "ACME.com"
        },
        "http": {
            "request": {
                "body": {
                    "bytes": 183
                },
                "id": "e6Hwr9m4uRtjSPXu2C2K4mmiFk0n7Ubqu0EUf0CqI0uxPbUE2qWiKA==",
                "method": "POST",
                "mime_type": "application/json",
                "referrer": "atf.team.ACME.com"
            },
            "version": "HTTP/1.1"
        },
        "rule": {
            "category": "REGULAR",
            "name": "Default_Action"
        },
        "source": {
            "geo": {
                "country_iso_code": "IE"
            },
            "ip": "30.255.150.197",
            "address": "30.255.150.197"
        },
        "url": {
            "original": "/graphql",
            "path": "/graphql"
        },
        "user_agent": {
            "original": "node-fetch/1.0 (+https://github.com/bitinn/node-fetch)",
            "device": {
                "name": "Other"
            },
            "name": "Other"
        },
        "related": {
            "hosts": [
                "api.ACME.com"
            ],
            "ip": [
                "30.255.150.197"
            ]
        },
        "os": {
            "name": "Other"
        }
    }
    	
	```


=== "allow2.json"

    ```json
	
    {
        "message": "{\"timestamp\":1669441143965,\"formatVersion\":1,\"webaclId\":\"arn:aws:wafv2:us-east-1:global/webacl/ACME/41f0e583-5098\",\"terminatingRuleId\":\"Default_Action\",\"terminatingRuleType\":\"REGULAR\",\"action\":\"ALLOW\",\"terminatingRuleMatchDetails\":[],\"httpSourceName\":\"CF\",\"httpSourceId\":\"E2R57GJ4AQX5UR\",\"ruleGroupList\":[{\"ruleGroupId\":\"AWS#AWSManagedRulesAmazonIpReputationList\",\"terminatingRule\":null,\"nonTerminatingMatchingRules\":[],\"excludedRules\":null,\"customerConfig\":null}],\"rateBasedRuleList\":[],\"nonTerminatingMatchingRules\":[],\"requestHeadersInserted\":null,\"responseCodeSent\":200,\"httpRequest\":{\"clientIp\":\"2600:4040:2974:1c00:5404:1cac:9f62:ffff\",\"country\":\"US\",\"headers\":[{\"name\":\"Host\",\"value\":\"api.ACME.com\"},{\"name\":\"Connection\",\"value\":\"Upgrade\"},{\"name\":\"Pragma\",\"value\":\"no-cache\"},{\"name\":\"Cache-Control\",\"value\":\"no-cache\"},{\"name\":\"User-Agent\",\"value\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36\"},{\"name\":\"Upgrade\",\"value\":\"websocket\"},{\"name\":\"Origin\",\"value\":\"https://app.ACME.com\"},{\"name\":\"Sec-WebSocket-Version\",\"value\":\"13\"},{\"name\":\"Accept-Encoding\",\"value\":\"gzip, deflate, br\"},{\"name\":\"Accept-Language\",\"value\":\"en-US,en;q=0.9\"},{\"name\":\"Cookie\",\"value\":\"REDACTED\"},{\"name\":\"Sec-WebSocket-Key\",\"value\":\"QUKS5ot19xG6kMaXl0FbIg==\"},{\"name\":\"Sec-WebSocket-Extensions\",\"value\":\"permessage-deflate; client_max_window_bits\"},{\"name\":\"Sec-WebSocket-Protocol\",\"value\":\"graphql-ws\"}],\"uri\":\"/subscriptions\",\"args\":\"REDACTED\",\"httpVersion\":\"HTTP/1.1\",\"httpMethod\":\"GET\",\"requestId\":\"XNSlGmCpHQABja00TCTI294jyGl26K_7qsJ2-L3Iu1UmeQtJwUgJIg==\"}}",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "access"
            ],
            "module": "aws.waf",
            "action": "ALLOW"
        },
        "@timestamp": "2022-11-26T05:39:03.965000Z",
        "action": {
            "target": "network-traffic"
        },
        "cloud": {
            "provider": "aws",
            "service": {
                "name": "waf"
            },
            "region": "us-east-1"
        },
        "observer": {
            "type": "waf"
        },
        "aws": {
            "waf": {
                "rule": {
                    "arn": "arn:aws:wafv2:us-east-1:global/webacl/ACME/41f0e583-5098"
                }
            }
        },
        "destination": {
            "domain": "api.ACME.com",
            "address": "api.ACME.com",
            "top_level_domain": "com",
            "subdomain": "api",
            "registered_domain": "ACME.com"
        },
        "http": {
            "request": {
                "id": "XNSlGmCpHQABja00TCTI294jyGl26K_7qsJ2-L3Iu1UmeQtJwUgJIg==",
                "method": "GET"
            },
            "response": {
                "status_code": 200
            },
            "version": "HTTP/1.1"
        },
        "rule": {
            "category": "REGULAR",
            "name": "Default_Action"
        },
        "source": {
            "geo": {
                "country_iso_code": "US"
            },
            "ip": "2600:4040:2974:1c00:5404:1cac:9f62:ffff",
            "address": "2600:4040:2974:1c00:5404:1cac:9f62:ffff"
        },
        "url": {
            "original": "/subscriptions",
            "path": "/subscriptions"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "device": {
                "name": "Mac"
            },
            "name": "Chrome",
            "version": "107.0.0"
        },
        "related": {
            "hosts": [
                "api.ACME.com"
            ],
            "ip": [
                "2600:4040:2974:1c00:5404:1cac:9f62:ffff"
            ]
        },
        "os": {
            "name": "Mac OS X",
            "version": "10.15.7"
        }
    }
    	
	```


=== "user_agent.json"

    ```json
	
    {
        "message": "{\"timestamp\":1669639359431,\"formatVersion\":1,\"webaclId\":\"arn:aws:wafv2:us-east-1:582598250481:global/webacl/ACME/41f0e583-5098\",\"terminatingRuleId\":\"Default_Action\",\"terminatingRuleType\":\"REGULAR\",\"action\":\"ALLOW\",\"terminatingRuleMatchDetails\":[],\"httpSourceName\":\"CF\",\"httpSourceId\":\"E2R57GJ4AQX5UR\",\"ruleGroupList\":[{\"ruleGroupId\":\"AWS#AWSManagedRulesAmazonIpReputationList\",\"terminatingRule\":null,\"nonTerminatingMatchingRules\":[],\"excludedRules\":null,\"customerConfig\":null}],\"rateBasedRuleList\":[],\"nonTerminatingMatchingRules\":[],\"requestHeadersInserted\":null,\"responseCodeSent\":null,\"httpRequest\":{\"clientIp\":\"36.37.214.134\",\"country\":\"KH\",\"headers\":[{\"name\":\"host\",\"value\":\"api.ACME.com\"},{\"name\":\"content-length\",\"value\":\"182\"},{\"name\":\"sec-ch-ua\",\"value\":\"\\\"Google Chrome\\\";v=\\\"107\\\", \\\"Chromium\\\";v=\\\"107\\\", \\\"Not=A?Brand\\\";v=\\\"24\\\"\"},{\"name\":\"x-client-version\",\"value\":\"2.214.1\"},{\"name\":\"sec-ch-ua-mobile\",\"value\":\"?0\"},{\"name\":\"authorization\",\"value\":\"REDACTED\"},{\"name\":\"user-agent\",\"value\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36\"},{\"name\":\"content-type\",\"value\":\"application/json\"},{\"name\":\"accept\",\"value\":\"*/*\"},{\"name\":\"x-client-origin\",\"value\":\"app.ACME.com\"},{\"name\":\"sec-ch-ua-platform\",\"value\":\"\\\"Windows\\\"\"},{\"name\":\"origin\",\"value\":\"https://app.ACME.com\"},{\"name\":\"sec-fetch-site\",\"value\":\"same-site\"},{\"name\":\"sec-fetch-mode\",\"value\":\"cors\"},{\"name\":\"sec-fetch-dest\",\"value\":\"empty\"},{\"name\":\"referer\",\"value\":\"https://app.ACME.com/\"},{\"name\":\"accept-encoding\",\"value\":\"gzip, deflate, br\"},{\"name\":\"accept-language\",\"value\":\"en-US,en;q=0.9\"}],\"uri\":\"/graphql\",\"args\":\"REDACTED\",\"httpVersion\":\"HTTP/2.0\",\"httpMethod\":\"POST\",\"requestId\":\"Cs2c_cKDiRUpviG8OWN--0CZVO32-LajujdsNebKbTzMFDaOBEF1sw==\"}}",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "access"
            ],
            "module": "aws.waf",
            "action": "ALLOW"
        },
        "@timestamp": "2022-11-28T12:42:39.431000Z",
        "action": {
            "target": "network-traffic"
        },
        "cloud": {
            "provider": "aws",
            "service": {
                "name": "waf"
            },
            "region": "us-east-1"
        },
        "observer": {
            "type": "waf"
        },
        "aws": {
            "waf": {
                "rule": {
                    "arn": "arn:aws:wafv2:us-east-1:582598250481:global/webacl/ACME/41f0e583-5098"
                }
            }
        },
        "destination": {
            "domain": "api.ACME.com",
            "address": "api.ACME.com",
            "top_level_domain": "com",
            "subdomain": "api",
            "registered_domain": "ACME.com"
        },
        "http": {
            "request": {
                "body": {
                    "bytes": 182
                },
                "id": "Cs2c_cKDiRUpviG8OWN--0CZVO32-LajujdsNebKbTzMFDaOBEF1sw==",
                "method": "POST",
                "mime_type": "application/json",
                "referrer": "app.ACME.com"
            },
            "version": "HTTP/2.0"
        },
        "rule": {
            "category": "REGULAR",
            "name": "Default_Action"
        },
        "source": {
            "geo": {
                "country_iso_code": "KH"
            },
            "ip": "36.37.214.134",
            "address": "36.37.214.134"
        },
        "url": {
            "original": "/graphql",
            "path": "/graphql"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "device": {
                "name": "Other"
            },
            "name": "Chrome",
            "version": "107.0.0"
        },
        "related": {
            "hosts": [
                "api.ACME.com"
            ],
            "ip": [
                "36.37.214.134"
            ]
        },
        "os": {
            "name": "Windows",
            "version": "10"
        }
    }
    	
	```


=== "web-socket.json"

    ```json
	
    {
        "message": "{\"timestamp\":1669449735564,\"formatVersion\":1,\"webaclId\":\"arn:aws:wafv2:us-east-1:global/webacl/ACME/41f0e583-5098\",\"terminatingRuleId\":\"Whitelist-Header-Cookie\",\"terminatingRuleType\":\"REGULAR\",\"action\":\"ALLOW\",\"terminatingRuleMatchDetails\":[],\"httpSourceName\":\"CF\",\"httpSourceId\":\"E2R57GJ4AQX5UR\",\"ruleGroupList\":[],\"rateBasedRuleList\":[],\"nonTerminatingMatchingRules\":[],\"requestHeadersInserted\":null,\"responseCodeSent\":null,\"httpRequest\":{\"clientIp\":\"140.161.225.89\",\"country\":\"GB\",\"headers\":[{\"name\":\"Host\",\"value\":\"api.ACME.com\"},{\"name\":\"Connection\",\"value\":\"Upgrade\"},{\"name\":\"Pragma\",\"value\":\"no-cache\"},{\"name\":\"Cache-Control\",\"value\":\"no-cache\"},{\"name\":\"User-Agent\",\"value\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36\"},{\"name\":\"Upgrade\",\"value\":\"websocket\"},{\"name\":\"Origin\",\"value\":\"https://app.ACME.com\"},{\"name\":\"Sec-WebSocket-Version\",\"value\":\"13\"},{\"name\":\"Accept-Encoding\",\"value\":\"gzip, deflate, br\"},{\"name\":\"Accept-Language\",\"value\":\"en-GB,en-US;q=0.9,en;q=0.8\"},{\"name\":\"Cookie\",\"value\":\"REDACTED\"},{\"name\":\"Sec-WebSocket-Key\",\"value\":\"Fl+0IdBjmYwtjTGcoMneOQ==\"},{\"name\":\"Sec-WebSocket-Extensions\",\"value\":\"permessage-deflate; client_max_window_bits\"},{\"name\":\"Sec-WebSocket-Protocol\",\"value\":\"graphql-ws\"}],\"uri\":\"/subscriptions\",\"args\":\"REDACTED\",\"httpVersion\":\"HTTP/1.1\",\"httpMethod\":\"GET\",\"requestId\":\"rS38BhqsbkL36wW_M5wAKI2TJHZ9CXIlefVf5-yfJQ-TA5oYq9n8yA==\"}}",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "access"
            ],
            "module": "aws.waf",
            "action": "ALLOW"
        },
        "@timestamp": "2022-11-26T08:02:15.564000Z",
        "action": {
            "target": "network-traffic"
        },
        "cloud": {
            "provider": "aws",
            "service": {
                "name": "waf"
            },
            "region": "us-east-1"
        },
        "observer": {
            "type": "waf"
        },
        "aws": {
            "waf": {
                "rule": {
                    "arn": "arn:aws:wafv2:us-east-1:global/webacl/ACME/41f0e583-5098"
                }
            }
        },
        "destination": {
            "domain": "api.ACME.com",
            "address": "api.ACME.com",
            "top_level_domain": "com",
            "subdomain": "api",
            "registered_domain": "ACME.com"
        },
        "http": {
            "request": {
                "id": "rS38BhqsbkL36wW_M5wAKI2TJHZ9CXIlefVf5-yfJQ-TA5oYq9n8yA==",
                "method": "GET"
            },
            "version": "HTTP/1.1"
        },
        "rule": {
            "category": "REGULAR",
            "name": "Whitelist-Header-Cookie"
        },
        "source": {
            "geo": {
                "country_iso_code": "GB"
            },
            "ip": "140.161.225.89",
            "address": "140.161.225.89"
        },
        "url": {
            "original": "/subscriptions",
            "path": "/subscriptions"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "device": {
                "name": "Other"
            },
            "name": "Chrome",
            "version": "107.0.0"
        },
        "related": {
            "hosts": [
                "api.ACME.com"
            ],
            "ip": [
                "140.161.225.89"
            ]
        },
        "os": {
            "name": "Windows",
            "version": "10"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`action.target` | `keyword` | The target of the action |
|`aws.waf.rule.arn` | `keyword` | The GUID of the web ACL |
|`cloud.provider` | `keyword` | Name of the cloud provider. |
|`cloud.region` | `keyword` | Region in which this host, resource, or service is located. |
|`cloud.service.name` | `keyword` | The cloud service name. |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.module` | `keyword` | Name of the module this data is coming from. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`http.request.body.bytes` | `long` | Size in bytes of the request body. |
|`http.request.id` | `keyword` | HTTP request ID. |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.mime_type` | `keyword` | Mime type of the body of the request. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`http.response.status_code` | `long` | HTTP response status code. |
|`http.version` | `keyword` | HTTP version. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`rule.category` | `keyword` | Rule category |
|`rule.description` | `keyword` | Rule description |
|`rule.name` | `keyword` | Rule name |
|`source.geo.country_iso_code` | `keyword` | Country ISO code. |
|`source.ip` | `ip` | IP address of the source. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

