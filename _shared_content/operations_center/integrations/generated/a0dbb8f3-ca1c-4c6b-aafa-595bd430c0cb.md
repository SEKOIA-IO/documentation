
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web logs` | Squid logs provide information about the connected client and the requested resource |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `` |
| Category | `network`, `web` |
| Type | `connection`, `denied`, `error` |




### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "common_log_format_1.json"

    ```json
	
    {
        "message": "1.2.3.4 - johndoe [05/02/2025 11:30:29] \"GET https://sub.example.com/1.png HTTP/1.1\" 200 - - 1000 Business Services",
        "event": {
            "category": [
                "network",
                "web"
            ]
        },
        "@timestamp": "2025-05-02T11:30:29Z",
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "status_code": 200
            }
        },
        "network": {
            "direction": "egress"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "johndoe"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "url": {
            "domain": "sub.example.com",
            "full": "https://sub.example.com/1.png",
            "original": "https://sub.example.com/1.png",
            "path": "/1.png",
            "port": 443,
            "registered_domain": "example.com",
            "scheme": "https",
            "subdomain": "sub",
            "top_level_domain": "com"
        },
        "user": {
            "name": "johndoe"
        }
    }
    	
	```


=== "common_log_format_2.json"

    ```json
	
    {
        "message": "5.6.7.8 - janedoe [05/02/2025 11:31:06] \"CONNECT https://example.com:443 HTTP/1.1\" 200 -",
        "event": {
            "category": [
                "network",
                "web"
            ]
        },
        "@timestamp": "2025-05-02T11:31:06Z",
        "destination": {
            "address": "example.com",
            "domain": "example.com",
            "port": 443,
            "registered_domain": "example.com",
            "top_level_domain": "com"
        },
        "http": {
            "request": {
                "method": "CONNECT"
            },
            "response": {
                "status_code": 200
            }
        },
        "network": {
            "direction": "egress"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "hosts": [
                "example.com"
            ],
            "ip": [
                "5.6.7.8"
            ],
            "user": [
                "janedoe"
            ]
        },
        "source": {
            "address": "5.6.7.8",
            "ip": "5.6.7.8"
        },
        "user": {
            "name": "janedoe"
        }
    }
    	
	```


=== "connect.json"

    ```json
	
    {
        "message": "1564655684.277   3387 192.168.0.1 TCP_TUNNEL/200 19131 CONNECT example.org:443 - HIER_DIRECT/example.org -",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 3387
        },
        "@timestamp": "2019-08-01T10:34:44.277000Z",
        "destination": {
            "address": "example.org",
            "domain": "example.org",
            "port": 443,
            "registered_domain": "example.org",
            "top_level_domain": "org"
        },
        "http": {
            "request": {
                "method": "CONNECT"
            },
            "response": {
                "bytes": 19131,
                "status_code": 200
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "hosts": [
                "example.org"
            ],
            "ip": [
                "192.168.0.1"
            ]
        },
        "server": {
            "domain": "example.org"
        },
        "source": {
            "address": "192.168.0.1",
            "ip": "192.168.0.1"
        },
        "squid": {
            "hierarchy_code": "HIER_DIRECT"
        }
    }
    	
	```


=== "connect2.json"

    ```json
	
    {
        "message": "1564576741.982   5756 192.168.0.1 TCP_TUNNEL/200 6295 CONNECT api42-api.example.com:443 - HIER_DIRECT/api42-api.example.com -",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 5756
        },
        "@timestamp": "2019-07-31T12:39:01.982000Z",
        "destination": {
            "address": "api42-api.example.com",
            "domain": "api42-api.example.com",
            "port": 443,
            "registered_domain": "example.com",
            "subdomain": "api42-api",
            "top_level_domain": "com"
        },
        "http": {
            "request": {
                "method": "CONNECT"
            },
            "response": {
                "bytes": 6295,
                "status_code": 200
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "hosts": [
                "api42-api.example.com"
            ],
            "ip": [
                "192.168.0.1"
            ]
        },
        "server": {
            "domain": "api42-api.example.com"
        },
        "source": {
            "address": "192.168.0.1",
            "ip": "192.168.0.1"
        },
        "squid": {
            "hierarchy_code": "HIER_DIRECT"
        }
    }
    	
	```


=== "connect3.json"

    ```json
	
    {
        "message": "1587042596.494   1717 192.168.224.39 TCP_TUNNEL/200 3512 CONNECT 193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.example.net:443 - HIER_DIRECT/193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.example.net -",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 1717
        },
        "@timestamp": "2020-04-16T13:09:56.494000Z",
        "destination": {
            "address": "193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.example.net",
            "domain": "193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.example.net",
            "port": 443,
            "registered_domain": "example.net",
            "subdomain": "193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s",
            "top_level_domain": "net"
        },
        "http": {
            "request": {
                "method": "CONNECT"
            },
            "response": {
                "bytes": 3512,
                "status_code": 200
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "hosts": [
                "193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.example.net"
            ],
            "ip": [
                "192.168.224.39"
            ]
        },
        "server": {
            "domain": "193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.example.net"
        },
        "source": {
            "address": "192.168.224.39",
            "ip": "192.168.224.39"
        },
        "squid": {
            "hierarchy_code": "HIER_DIRECT"
        }
    }
    	
	```


=== "connect4.json"

    ```json
	
    {
        "message": "1737983758.627 207 1.2.3.4 TCP_TUNNEL/200 4047 CONNECT test.example.org:443 - HIER_DIRECT/5.6.7.8 - ",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 207
        },
        "@timestamp": "2025-01-27T13:15:58.627000Z",
        "destination": {
            "address": "test.example.org",
            "domain": "test.example.org",
            "port": 443,
            "registered_domain": "example.org",
            "subdomain": "test",
            "top_level_domain": "org"
        },
        "http": {
            "request": {
                "method": "CONNECT"
            },
            "response": {
                "bytes": 4047,
                "status_code": 200
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "hosts": [
                "test.example.org"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        },
        "server": {
            "ip": "5.6.7.8"
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "squid": {
            "hierarchy_code": "HIER_DIRECT"
        }
    }
    	
	```


=== "connect5.json"

    ```json
	
    {
        "message": "1737983750.078 61 1.2.3.4 TCP_TUNNEL/200 8811 CONNECT safebrowsing.example.com:443 - HIER_DIRECT/5.6.7.8 -",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 61
        },
        "@timestamp": "2025-01-27T13:15:50.078000Z",
        "destination": {
            "address": "safebrowsing.example.com",
            "domain": "safebrowsing.example.com",
            "port": 443,
            "registered_domain": "example.com",
            "subdomain": "safebrowsing",
            "top_level_domain": "com"
        },
        "http": {
            "request": {
                "method": "CONNECT"
            },
            "response": {
                "bytes": 8811,
                "status_code": 200
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "hosts": [
                "safebrowsing.example.com"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        },
        "server": {
            "ip": "5.6.7.8"
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "squid": {
            "hierarchy_code": "HIER_DIRECT"
        }
    }
    	
	```


=== "connect_ip.json"

    ```json
	
    {
        "message": "1642667037.129      0 10.0.4.4 TCP_DENIED/403 3868 CONNECT 1.2.3.4:80 - HIER_NONE/- text/html \"-\" \"-\"",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 0,
            "type": [
                "connection",
                "denied",
                "error"
            ]
        },
        "@timestamp": "2022-01-20T08:23:57.129000Z",
        "destination": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4",
            "port": 80
        },
        "http": {
            "request": {
                "method": "CONNECT"
            },
            "response": {
                "bytes": 3868,
                "mime_type": "text/html",
                "status_code": 403
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "ip": [
                "1.2.3.4",
                "10.0.4.4"
            ]
        },
        "source": {
            "address": "10.0.4.4",
            "ip": "10.0.4.4"
        },
        "squid": {
            "cache_status": "denied",
            "hierarchy_code": "HIER_NONE"
        }
    }
    	
	```


=== "content_type.json"

    ```json
	
    {
        "message": "1565598801.353     24 10.16.12.86 TCP_MISS/200 394 GET http://dt.example.com/dt123456 - HIER_DIRECT/dt.example.com image/gif",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 24
        },
        "@timestamp": "2019-08-12T08:33:21.353000Z",
        "destination": {
            "address": "dt.example.com",
            "domain": "dt.example.com",
            "registered_domain": "example.com",
            "subdomain": "dt",
            "top_level_domain": "com"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "bytes": 394,
                "mime_type": "image/gif",
                "status_code": 200
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "hosts": [
                "dt.example.com"
            ],
            "ip": [
                "10.16.12.86"
            ]
        },
        "source": {
            "address": "10.16.12.86",
            "ip": "10.16.12.86"
        },
        "squid": {
            "cache_status": "miss",
            "hierarchy_code": "HIER_DIRECT"
        },
        "url": {
            "domain": "dt.example.com",
            "full": "http://dt.example.com/dt123456",
            "original": "http://dt.example.com/dt123456",
            "path": "/dt123456",
            "port": 80,
            "registered_domain": "example.com",
            "scheme": "http",
            "subdomain": "dt",
            "top_level_domain": "com"
        }
    }
    	
	```


=== "error.json"

    ```json
	
    {
        "message": "1761121144.919      0 1.2.3.4 NONE_NONE/000 0 - error:transaction-end-before-headers - HIER_NONE/- - \"-\" \"-\"",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 0,
            "reason": "error:transaction-end-before-headers"
        },
        "@timestamp": "2025-10-22T08:19:04.919000Z",
        "http": {
            "response": {
                "bytes": 0,
                "status_code": 0
            }
        },
        "network": {
            "direction": "egress"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "squid": {
            "hierarchy_code": "HIER_NONE"
        }
    }
    	
	```


=== "get.json"

    ```json
	
    {
        "message": "1564670112.892   5007 192.168.95.17 TCP_HIT_ABORTED/000 0 GET http://smex10-2-en.url.example.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA== - HIER_DIRECT/smex10-2-en.url.example.com -",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 5007,
            "type": [
                "connection",
                "error"
            ]
        },
        "@timestamp": "2019-08-01T14:35:12.892000Z",
        "destination": {
            "address": "smex10-2-en.url.example.com",
            "domain": "smex10-2-en.url.example.com",
            "registered_domain": "example.com",
            "subdomain": "smex10-2-en.url",
            "top_level_domain": "com"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "bytes": 0,
                "status_code": 0
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "hosts": [
                "smex10-2-en.url.example.com"
            ],
            "ip": [
                "192.168.95.17"
            ]
        },
        "source": {
            "address": "192.168.95.17",
            "ip": "192.168.95.17"
        },
        "squid": {
            "cache_status": "hit",
            "hierarchy_code": "HIER_DIRECT"
        },
        "url": {
            "domain": "smex10-2-en.url.example.com",
            "full": "http://smex10-2-en.url.example.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "original": "http://smex10-2-en.url.example.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "path": "/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "port": 80,
            "registered_domain": "example.com",
            "scheme": "http",
            "subdomain": "smex10-2-en.url",
            "top_level_domain": "com"
        }
    }
    	
	```


=== "get2.json"

    ```json
	
    {
        "message": "1565600128.411      0 192.168.0.1 TCP_DENIED/407 3980 GET http://api.example.org/api/v2/check - HIER_NONE/- text/html",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 0,
            "type": [
                "connection",
                "denied",
                "error"
            ]
        },
        "@timestamp": "2019-08-12T08:55:28.411000Z",
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "bytes": 3980,
                "mime_type": "text/html",
                "status_code": 407
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "ip": [
                "192.168.0.1"
            ]
        },
        "source": {
            "address": "192.168.0.1",
            "ip": "192.168.0.1"
        },
        "squid": {
            "cache_status": "denied",
            "hierarchy_code": "HIER_NONE"
        },
        "url": {
            "domain": "api.example.org",
            "full": "http://api.example.org/api/v2/check",
            "original": "http://api.example.org/api/v2/check",
            "path": "/api/v2/check",
            "port": 80,
            "registered_domain": "example.org",
            "scheme": "http",
            "subdomain": "api",
            "top_level_domain": "org"
        }
    }
    	
	```


=== "get_dalid.json"

    ```json
	
    {
        "message": "1628084203.491     82 192.168.2.2 TCP_MISS/200 318399 GET http://download.example.com/c/msdownload/update/others/2019/07/29477140_324519a81d0af914f765c56a1dc7141a5759ad4c.cab - HIER_DIRECT/1.2.3.4 application/vnd.ms-cab-compressed",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 82
        },
        "@timestamp": "2021-08-04T13:36:43.491000Z",
        "destination": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "bytes": 318399,
                "mime_type": "application/vnd.ms-cab-compressed",
                "status_code": 200
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "ip": [
                "1.2.3.4",
                "192.168.2.2"
            ]
        },
        "source": {
            "address": "192.168.2.2",
            "ip": "192.168.2.2"
        },
        "squid": {
            "cache_status": "miss",
            "hierarchy_code": "HIER_DIRECT"
        },
        "url": {
            "domain": "download.example.com",
            "full": "http://download.example.com/c/msdownload/update/others/2019/07/29477140_324519a81d0af914f765c56a1dc7141a5759ad4c.cab",
            "original": "http://download.example.com/c/msdownload/update/others/2019/07/29477140_324519a81d0af914f765c56a1dc7141a5759ad4c.cab",
            "path": "/c/msdownload/update/others/2019/07/29477140_324519a81d0af914f765c56a1dc7141a5759ad4c.cab",
            "port": 80,
            "registered_domain": "example.com",
            "scheme": "http",
            "subdomain": "download",
            "top_level_domain": "com"
        }
    }
    	
	```


=== "get_tcp_hit.json"

    ```json
	
    {
        "message": "1628150510.448    549 192.168.0.1 TCP_HIT/206 2055995 GET http://edgedl.me.example.com/edgedl/release2/chrome_component/adbzvrjxj3ir3yvy5lknhgbxo6tq_92.267.200/gkmgaooipdjhmangpemjhigmamcehddo_92.267.200_win64_ac37t7snjqk4qthomil6kwgo54hq.crx3 - HIER_NONE/- application/octet-stream",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 549
        },
        "@timestamp": "2021-08-05T08:01:50.448000Z",
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "bytes": 2055995,
                "mime_type": "application/octet-stream",
                "status_code": 206
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "ip": [
                "192.168.0.1"
            ]
        },
        "source": {
            "address": "192.168.0.1",
            "ip": "192.168.0.1"
        },
        "squid": {
            "cache_status": "hit",
            "hierarchy_code": "HIER_NONE"
        },
        "url": {
            "domain": "edgedl.me.example.com",
            "full": "http://edgedl.me.example.com/edgedl/release2/chrome_component/adbzvrjxj3ir3yvy5lknhgbxo6tq_92.267.200/gkmgaooipdjhmangpemjhigmamcehddo_92.267.200_win64_ac37t7snjqk4qthomil6kwgo54hq.crx3",
            "original": "http://edgedl.me.example.com/edgedl/release2/chrome_component/adbzvrjxj3ir3yvy5lknhgbxo6tq_92.267.200/gkmgaooipdjhmangpemjhigmamcehddo_92.267.200_win64_ac37t7snjqk4qthomil6kwgo54hq.crx3",
            "path": "/edgedl/release2/chrome_component/adbzvrjxj3ir3yvy5lknhgbxo6tq_92.267.200/gkmgaooipdjhmangpemjhigmamcehddo_92.267.200_win64_ac37t7snjqk4qthomil6kwgo54hq.crx3",
            "port": 80,
            "registered_domain": "example.com",
            "scheme": "http",
            "subdomain": "edgedl.me",
            "top_level_domain": "com"
        }
    }
    	
	```


=== "get_user_agent.json"

    ```json
	
    {
        "message": "1564670112.892   5007 192.168.95.17 TCP_HIT_ABORTED/000 0 GET http://smex10-2-en.url.example.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA== - HIER_DIRECT/smex10-2-en.url.example.com - \"http://www.example.org\" \"TMUFE\"",
        "event": {
            "category": [
                "network",
                "web"
            ],
            "duration": 5007,
            "type": [
                "connection",
                "error"
            ]
        },
        "@timestamp": "2019-08-01T14:35:12.892000Z",
        "destination": {
            "address": "smex10-2-en.url.example.com",
            "domain": "smex10-2-en.url.example.com",
            "registered_domain": "example.com",
            "subdomain": "smex10-2-en.url",
            "top_level_domain": "com"
        },
        "http": {
            "request": {
                "method": "GET",
                "referrer": "http://www.example.org"
            },
            "response": {
                "bytes": 0,
                "status_code": 0
            }
        },
        "network": {
            "direction": "egress",
            "transport": "tcp"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "hosts": [
                "smex10-2-en.url.example.com"
            ],
            "ip": [
                "192.168.95.17"
            ]
        },
        "source": {
            "address": "192.168.95.17",
            "ip": "192.168.95.17"
        },
        "squid": {
            "cache_status": "hit",
            "hierarchy_code": "HIER_DIRECT"
        },
        "url": {
            "domain": "smex10-2-en.url.example.com",
            "full": "http://smex10-2-en.url.example.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "original": "http://smex10-2-en.url.example.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "path": "/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "port": 80,
            "registered_domain": "example.com",
            "scheme": "http",
            "subdomain": "smex10-2-en.url",
            "top_level_domain": "com"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Other",
            "original": "TMUFE",
            "os": {
                "name": "Other"
            }
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.port` | `long` | Port of the destination. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.duration` | `long` | Duration of the event in nanoseconds. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`http.response.bytes` | `long` | Total size in bytes of the response (body and headers). |
|`http.response.mime_type` | `keyword` | Mime type of the body of the response. |
|`http.response.status_code` | `long` | HTTP response status code. |
|`network.direction` | `keyword` | Direction of the network traffic. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`server.domain` | `keyword` | The domain name of the server. |
|`server.ip` | `ip` | IP address of the server. |
|`source.ip` | `ip` | IP address of the source. |
|`squid.cache_status` | `keyword` | Cache status for the request |
|`squid.hierarchy_code` | `keyword` | Hierarchy used by Squid for this connection. |
|`url.full` | `wildcard` | Full unparsed URL. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Squid/squid).