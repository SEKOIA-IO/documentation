
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `DNS records` | BIND provides detailed logs on handled DNS queries |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "query_log.json"

    ```json
	
    {
        "message": "client @0x7f62b80115d0 192.168.101.70#55575 (docs.sekoia.io): query: docs.sekoia.io IN AAAA + (192.168.100.102)",
        "source": {
            "address": "192.168.101.70",
            "ip": "192.168.101.70",
            "port": 55575
        },
        "related": {
            "ip": [
                "192.168.101.70"
            ]
        },
        "dns": {
            "type": "query",
            "question": {
                "type": "AAAA",
                "class": "IN",
                "name": "docs.sekoia.io"
            },
            "header_flags": [
                "RD"
            ]
        }
    }
    	
	```


=== "query_log_cd.json"

    ```json
	
    {
        "message": "client 192.168.101.70#55575 (docs.sekoia.io): query: docs.sekoia.io IN AAAA +TC (192.168.100.102)",
        "source": {
            "address": "192.168.101.70",
            "ip": "192.168.101.70",
            "port": 55575
        },
        "related": {
            "ip": [
                "192.168.101.70"
            ]
        },
        "dns": {
            "type": "query",
            "question": {
                "type": "AAAA",
                "class": "IN",
                "name": "docs.sekoia.io"
            },
            "header_flags": [
                "RD",
                "CD"
            ]
        },
        "network": {
            "transport": "tcp"
        }
    }
    	
	```


=== "query_log_dnssec.json"

    ```json
	
    {
        "message": "client 192.168.103.66#42811 (ipv6.google.com): query: ipv6.google.com IN A +EDC (192.168.100.102)",
        "source": {
            "address": "192.168.103.66",
            "ip": "192.168.103.66",
            "port": 42811
        },
        "related": {
            "ip": [
                "192.168.103.66"
            ]
        },
        "dns": {
            "type": "query",
            "question": {
                "type": "A",
                "class": "IN",
                "name": "ipv6.google.com"
            },
            "header_flags": [
                "RD",
                "CD"
            ]
        }
    }
    	
	```


=== "query_log_edns_version.json"

    ```json
	
    {
        "message": "client @0x7f4f8003d9e0 192.168.101.61#38251 (global.vortex.data.trafficmanager.net): query: global.vortex.data.trafficmanager.net IN AAAA +E(0) (192.168.100.102)",
        "source": {
            "address": "192.168.101.61",
            "ip": "192.168.101.61",
            "port": 38251
        },
        "related": {
            "ip": [
                "192.168.101.61"
            ]
        },
        "dns": {
            "type": "query",
            "question": {
                "type": "AAAA",
                "class": "IN",
                "name": "global.vortex.data.trafficmanager.net"
            },
            "header_flags": [
                "RD"
            ]
        }
    }
    	
	```


=== "query_log_no_recursion.json"

    ```json
	
    {
        "message": "client 192.168.103.66#57980 (ipv6.google.com): query: ipv6.google.com IN AAAA - (192.168.100.102)",
        "source": {
            "address": "192.168.103.66",
            "ip": "192.168.103.66",
            "port": 57980
        },
        "related": {
            "ip": [
                "192.168.103.66"
            ]
        },
        "dns": {
            "header_flags": [],
            "type": "query",
            "question": {
                "type": "AAAA",
                "class": "IN",
                "name": "ipv6.google.com"
            }
        }
    }
    	
	```


=== "query_log_reverse.json"

    ```json
	
    {
        "message": "client 192.168.103.66#45041 (107.100.168.192.in-addr.arpa): query: 107.100.168.192.in-addr.arpa IN PTR +E (192.168.100.102)",
        "source": {
            "address": "192.168.103.66",
            "ip": "192.168.103.66",
            "port": 45041
        },
        "related": {
            "ip": [
                "192.168.103.66"
            ]
        },
        "dns": {
            "type": "query",
            "question": {
                "type": "PTR",
                "class": "IN",
                "name": "107.100.168.192.in-addr.arpa"
            },
            "header_flags": [
                "RD"
            ]
        }
    }
    	
	```


=== "query_log_tcp.json"

    ```json
	
    {
        "message": "client 192.168.101.70#55575 (docs.sekoia.io): query: docs.sekoia.io IN AAAA +ET (192.168.100.102)",
        "source": {
            "address": "192.168.101.70",
            "ip": "192.168.101.70",
            "port": 55575
        },
        "related": {
            "ip": [
                "192.168.101.70"
            ]
        },
        "dns": {
            "type": "query",
            "question": {
                "type": "AAAA",
                "class": "IN",
                "name": "docs.sekoia.io"
            },
            "header_flags": [
                "RD"
            ]
        },
        "network": {
            "transport": "tcp"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`dns.header_flags` | `keyword` | Array of DNS header flags. |
|`dns.question.class` | `keyword` | The class of records being queried. |
|`dns.question.name` | `keyword` | The name being queried. |
|`dns.question.type` | `keyword` | The type of record being queried. |
|`dns.type` | `keyword` | The type of DNS event captured, query or answer. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |

