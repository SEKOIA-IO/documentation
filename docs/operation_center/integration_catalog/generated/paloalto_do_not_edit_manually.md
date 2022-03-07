
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network device logs` | Palo Alto can record traffic events flowing through their firewall |
| `Network protocol analysis` | Palo Alto firewall does traffic analysis at physical/data/transport layers |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "User_id_2.json"

    ```json
	
    {
        "action": {
            "type": "login"
        },
        "destination": {
            "port": 0
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "userid"
        },
        "log": {
            "hostname": "hostname_example",
            "logger": "srv1.example.local"
        },
        "message": "1,2020/12/04 16:00:02,01640103000,USERID,login,2200,2020/12/04 16:00:02,vsys,10.0.0.2,user1,srv1.example.local,0,1,13000,0,0,active-directory,,968700000,0x8000000000000000,12,0,0,0,,hostname_example,1,,2020/12/04 16:00:02,1,0x0,user1",
        "related": {
            "ip": [
                "10.0.0.2"
            ],
            "user": [
                "user1"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "Palo Alto",
                "dialect_uuid": "903ec1b8-f206-4ba5-8563-db21da09cafd"
            }
        },
        "source": {
            "address": "10.0.0.2",
            "ip": "10.0.0.2",
            "port": 0
        },
        "user": {
            "name": "user1"
        }
    }
    	
	```


=== "globalprotect.json"

    ```json
	
    {
        "action": {
            "outcome": "success",
            "type": "0"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "globalprotect"
        },
        "geo": {
            "country_iso_code": "FR"
        },
        "message": "1,2020/12/08 14:30:55,011111114444,GLOBALPROTECT,0,2305,2020/12/08 13:30:55,vsys1,gw-auth,login,Other,,user,FR,AAAABBBBB,1.2.3.4,0.0.0.0,0.0.0.0,0.0.0.0,aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee,ABCDEFG,5.1.4,Windows,\"Microsoft Windows 10 Pro , 64-bit\",1,,,\"\",success,,0,user-logon,0,gw1,1234567,0x8000000000000000",
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "user"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "Palo Alto",
                "dialect_uuid": "903ec1b8-f206-4ba5-8563-db21da09cafd"
            }
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "name": "user"
        },
        "user_agent": {
            "os": {
                "name": "Windows",
                "version": "Microsoft Windows 10 Pro , 64-bit"
            }
        }
    }
    	
	```


=== "icmp_allow.json"

    ```json
	
    {
        "action": {
            "name": "allow",
            "outcome": "success",
            "type": "start"
        },
        "destination": {
            "address": "4.3.2.1",
            "bytes": 0,
            "ip": "4.3.2.1",
            "nat": {
                "ip": "10.0.1.2",
                "port": 0
            },
            "packets": 0,
            "port": 0
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "traffic",
            "duration": 0
        },
        "message": "<14>Sep 16 10:00:02 PP 1,9/16/19 10:00,1801017000,TRAFFIC,start,2049,9/16/19 10:00,1.2.3.4,4.3.2.1,1.2.3.4,10.0.1.2,PING,,,ping,vsys,AAAAA,Zone1,ethernet1/1,ae2.11,Secure,9/16/19 10:00,24100,3,0,0,0,0,0x500000,icmp,allow,222,222,0,3,9/16/19 10:00,0,any,0,50660388939,0x0,Spain,France,0,3,0,n/a,0,0,0,0,,PA,from-policy,,,0,,0,,N/A,0,0,0,0",
        "network": {
            "bytes": 222,
            "packets": 3,
            "transport": "icmp"
        },
        "related": {
            "ip": [
                "1.2.3.4",
                "10.0.1.2",
                "4.3.2.1"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "Palo Alto",
                "dialect_uuid": "903ec1b8-f206-4ba5-8563-db21da09cafd"
            }
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 222,
            "ip": "1.2.3.4",
            "nat": {
                "ip": "1.2.3.4",
                "port": 0
            },
            "packets": 3,
            "port": 0
        }
    }
    	
	```


=== "system.json"

    ```json
	
    {
        "action": {
            "outcome_reason": "authenticated for user 'user1'.   auth profile 'GP', vsys 'vsys123', server profile 'LDAP', server address 'srv01.entreprise.local', From: 1.2.3.4.",
            "type": "auth"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "system"
        },
        "log": {
            "hostname": "fw1",
            "level": "informational"
        },
        "message": "1,2020/12/08 13:44:55,11111114444,SYSTEM,auth,0,2020/12/08 13:44:55,,auth-success,GP,0,0,general,informational,\"authenticated for user 'user1'.   auth profile 'GP', vsys 'vsys123', server profile 'LDAP', server address 'srv01.entreprise.local', From: 1.2.3.4.\",5211100,0x8000000000000000,0,0,0,0,,fw1",
        "sekoiaio": {
            "intake": {
                "dialect": "Palo Alto",
                "dialect_uuid": "903ec1b8-f206-4ba5-8563-db21da09cafd"
            }
        }
    }
    	
	```


=== "udp_deny.json"

    ```json
	
    {
        "action": {
            "name": "reset-both",
            "outcome": "success",
            "type": "deny"
        },
        "destination": {
            "address": "1.2.3.4",
            "bytes": 0,
            "ip": "1.2.3.4",
            "nat": {
                "ip": "5.4.3.2",
                "port": 53
            },
            "packets": 0,
            "port": 53
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "traffic",
            "duration": 0
        },
        "message": "<14>Sep 16 10:00:00 PA 1,9/16/19 10:00,1801017000,TRAFFIC,deny,2049,9/16/19 10:00,10.0.0.2,1.2.3.4,5.4.4.3,5.4.3.2,DENYALL,,,protection,vsys1,DNS,AAAAA,ae2.503,ethernet1/1,Secure,9/16/19 10:00,11111,1,130000,53,6379,53,0x400000,udp,reset-both,284,284,0,1,9/16/19 10:00,0,any,0,50660381851,0x0,10.0.0.0-10.255.255.255,Spain,0,1,0,policy-deny,0,0,0,0,,PA-1,from-application,,,0,,0,,N/A,0,0,0,0",
        "network": {
            "bytes": 284,
            "packets": 1,
            "transport": "udp"
        },
        "related": {
            "ip": [
                "5.4.3.2",
                "5.4.4.3",
                "10.0.0.2",
                "1.2.3.4"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "Palo Alto",
                "dialect_uuid": "903ec1b8-f206-4ba5-8563-db21da09cafd"
            }
        },
        "source": {
            "address": "10.0.0.2",
            "bytes": 284,
            "ip": "10.0.0.2",
            "nat": {
                "ip": "5.4.4.3",
                "port": 6379
            },
            "packets": 1,
            "port": 130000
        }
    }
    	
	```


=== "User_id_1.json"

    ```json
	
    {
        "action": {
            "type": "login"
        },
        "destination": {
            "port": 0
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "userid"
        },
        "log": {
            "hostname": "hostexample",
            "logger": "srv1.example.local"
        },
        "message": "1,2020/12/04 16:00:02,016401002222,USERID,login,2305,2020/12/04 16:00:02,vsys,1.2.3.4,user1,srv1.example.local,0,1,12000,0,0,active-directory,,968683723,0x8000000000000000,12,0,0,0,,hostexample,1,,2020/12/04 16:00:02,1,0x80,user1",
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "user1"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "Palo Alto",
                "dialect_uuid": "903ec1b8-f206-4ba5-8563-db21da09cafd"
            }
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4",
            "port": 0
        },
        "user": {
            "name": "user1"
        }
    }
    	
	```


=== "threat.json"

    ```json
	
    {
        "action": {
            "name": "alert",
            "outcome": "success",
            "type": "vulnerability"
        },
        "destination": {
            "address": "10.2.0.1",
            "ip": "10.2.0.1",
            "nat": {
                "ip": "0.0.0.0",
                "port": 0
            },
            "port": 80
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "code-execution",
            "category": "threat",
            "reason": "PDF Exploit Evasion Found(34805)"
        },
        "file": {
            "path": "EXAMPLE.PDF"
        },
        "log": {
            "hostname": "FW",
            "level": "informational"
        },
        "message": "1,2021/08/31 14:00:02,001701000000,THREAT,vulnerability,2049,2021/08/31 14:00:02,10.0.0.2,10.2.0.1,0.0.0.0,0.0.0.0,abcd,,,web-browsing,vsys,env,zone2,a1.1,aec.2,podl,2021/08/31 14:00:02,279429,2,12345,80,0,0,0x2000,tcp,alert,\"EXAMPLE.PDF\",PDF Exploit Evasion Found(34805),any,informational,server-to-client,1320000,0x2000000000000000,10.0.0.0-10.255.255.255,10.0.0.0-10.255.255.255,0,,0,,,1,,,,,,,,0,0,0,0,0,,FW,,,,,0,,0,,N/A,code-execution,AppThreat-0000-1111,0x0,0,422342342,",
        "network": {
            "transport": "tcp"
        },
        "related": {
            "ip": [
                "10.0.0.2",
                "10.2.0.1",
                "0.0.0.0"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "Palo Alto",
                "dialect_uuid": "903ec1b8-f206-4ba5-8563-db21da09cafd"
            }
        },
        "source": {
            "address": "10.0.0.2",
            "ip": "10.0.0.2",
            "nat": {
                "ip": "0.0.0.0",
                "port": 0
            },
            "port": 12345
        }
    }
    	
	```


=== "tcp_allow.json"

    ```json
	
    {
        "action": {
            "name": "allow",
            "outcome": "success",
            "type": "start"
        },
        "destination": {
            "address": "4.3.2.1",
            "bytes": 70,
            "ip": "4.3.2.1",
            "nat": {
                "ip": "0.0.0.0",
                "port": 0
            },
            "packets": 1,
            "port": 80
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "traffic",
            "duration": 0
        },
        "message": "<14>Sep 16 10:00:02 PA-1 1,9/16/19 10:00,1801016000,TRAFFIC,start,2049,9/16/19 10:00,1.2.3.4,4.3.2.1,0.0.0.0,0.0.0.0,proxy1,,,web-browsing,vsys1234,v10213,zone1,a.1,b.2,Secure,9/16/19 10:00,60000,1,61000,80,0,0,0x0,tcp,allow,800,700,70,2,9/16/19 10:00,0,any,0,50660381839,0x0,10.0.0.0-10.255.255.255,10.0.0.0-10.255.255.255,0,2,1,n/a,0,0,0,0,,PP,from-policy,,,0,,0,,N/A,0,0,0,0",
        "network": {
            "bytes": 800,
            "packets": 2,
            "transport": "tcp"
        },
        "related": {
            "ip": [
                "1.2.3.4",
                "4.3.2.1",
                "0.0.0.0"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "Palo Alto",
                "dialect_uuid": "903ec1b8-f206-4ba5-8563-db21da09cafd"
            }
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 700,
            "ip": "1.2.3.4",
            "nat": {
                "ip": "0.0.0.0",
                "port": 0
            },
            "packets": 2,
            "port": 61000
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`destination.address` | `keyword` | Destination network address. |
|`destination.bytes` | `long` | Bytes sent from the destination to the source. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.nat.ip` | `ip` | Destination NAT ip |
|`destination.nat.port` | `long` | Destination NAT Port |
|`destination.packets` | `long` | Packets sent from the destination to the source. |
|`destination.port` | `long` | Port of the destination. |
|`email.from.address` | `keyword` | None |
|`email.subject` | `keyword` | None |
|`email.to.address` | `keyword` | None |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.duration` | `long` | Duration of the event in nanoseconds. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`geo.country_iso_code` | `keyword` | None |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`log.level` | `keyword` | Log level of the log event. |
|`log.logger` | `keyword` | Name of the logger. |
|`network.bytes` | `long` | Total bytes transferred in both directions. |
|`network.packets` | `long` | Total packets transferred in both directions. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`paloalto.content_type` | `keyword` | None |
|`source.address` | `keyword` | Source network address. |
|`source.bytes` | `long` | Bytes sent from the source to the destination. |
|`source.ip` | `ip` | IP address of the source. |
|`source.nat.ip` | `ip` | Source NAT ip |
|`source.nat.port` | `long` | Source NAT port |
|`source.packets` | `long` | Packets sent from the source to the destination. |
|`source.port` | `long` | Port of the source. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.name` | `keyword` | Name of the user agent. |
|`user_agent.os.name` | `keyword` | Operating system name, without the version. |
|`user_agent.os.version` | `keyword` | Operating system version as a raw string. |

