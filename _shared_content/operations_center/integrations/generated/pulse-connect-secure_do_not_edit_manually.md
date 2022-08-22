
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Authentication logs` | Events are produced when a user authenticate on services of the company my means of the VPN |
| `Web logs` | Events are produced on web service access |
| `Network device logs` | Events are produced on VPN connection |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "host_checker_policy_failed.json"

    ```json
	
    {
        "message": "id=firewall time=\"2021-01-28 13:46:08\" pri=6 fw=172.16.128.22 vpn=CB2XXPCS02 ivs=Root user=bob realm=\"SEKOIA_User\" roles=\"VDI-Pulse_User_Role\" proto=auth src=176.134.164.62 dst= dstname= type=vpn op= arg=\"\" result= sent= rcvd= agent=\"\" duration= msg=\"AUT24804: Host Checker policy 'Sekoia_Host Checker' failed on host '176.134.164.62' address '00-d8-61-35-80-81' for user 'bob' reason 'Rule-Antivirus_Check:Le logiciel antivirus indiqu\u00e9 dans les exigences de s\u00e9curit\u00e9 n'est pas install\u00e9.'.\"",
        "event": {
            "code": "AUT24804",
            "provider": "auth"
        },
        "action": {
            "name": "AUT24804"
        },
        "network": {
            "forwarded_ip": "172.16.128.22"
        },
        "service": {
            "name": "CB2XXPCS02",
            "type": "vpn"
        },
        "user": {
            "name": "bob",
            "domain": "SEKOIA_User",
            "roles": [
                "VDI-Pulse_User_Role"
            ]
        },
        "source": {
            "ip": "176.134.164.62",
            "address": "176.134.164.62"
        },
        "related": {
            "ip": [
                "176.134.164.62"
            ],
            "user": [
                "bob"
            ]
        }
    }
    	
	```


=== "host_checker_policy_success.json"

    ```json
	
    {
        "message": "id=firewall time=\"2021-01-28 13:46:05\" pri=6 fw=172.16.128.22 vpn=CB2XXPCS02 ivs=Root user=alice realm=\"SEKOIA_User\" roles=\"SEKOIA_User_Role\" proto=auth src=19.160.74.9 dst= dstname= type=vpn op= arg=\"\" result= sent= rcvd= agent=\"\" duration= msg=\"AUT24803: Host Checker policy 'Sekoia_Host Checker' passed on host '19.160.74.9' address '60-f2-62-ea-2d-a1' for user 'alice'.\"",
        "event": {
            "code": "AUT24803",
            "provider": "auth"
        },
        "action": {
            "name": "AUT24803"
        },
        "network": {
            "forwarded_ip": "172.16.128.22"
        },
        "service": {
            "name": "CB2XXPCS02",
            "type": "vpn"
        },
        "user": {
            "name": "alice",
            "domain": "SEKOIA_User",
            "roles": [
                "SEKOIA_User_Role"
            ]
        },
        "source": {
            "ip": "19.160.74.9",
            "address": "19.160.74.9"
        },
        "related": {
            "ip": [
                "19.160.74.9"
            ],
            "user": [
                "alice"
            ]
        }
    }
    	
	```


=== "login_failed.json"

    ```json
	
    {
        "message": "id=firewall time=\"2021-01-28 14:14:04\" pri=6 fw=172.16.128.22 vpn=CB2XXPCS02 ivs=Default Network user=bob realm=\"SEKOIA_User\" roles=\"\" proto=auth src=176.168.192.159 dst= dstname= type=vpn op= arg=\"\" result= sent= rcvd= agent=\"\" duration= msg=\"AUT23457: Login failed using auth server RSA (ACE Server).  Reason: Failed\"",
        "event": {
            "code": "AUT23457",
            "provider": "auth"
        },
        "action": {
            "name": "AUT23457"
        },
        "network": {
            "forwarded_ip": "172.16.128.22"
        },
        "service": {
            "name": "CB2XXPCS02",
            "type": "vpn"
        },
        "user": {
            "name": "bob",
            "domain": "SEKOIA_User"
        },
        "source": {
            "ip": "176.168.192.159",
            "address": "176.168.192.159"
        },
        "related": {
            "ip": [
                "176.168.192.159"
            ],
            "user": [
                "bob"
            ]
        }
    }
    	
	```


=== "unauthenticated_request.json"

    ```json
	
    {
        "message": "id=firewall time=\"2021-03-04 17:05:15\" pri=6 fw=172.16.128.22 vpn=CB2XXPCS02 ivs=Default Network user=System realm=\"\" roles=\"\" proto= src=93.19.66.118 dst= dstname= type=vpn op= arg=\"\" result= sent= rcvd= agent=\"\" duration= msg=\"AUT31556: Unauthenticated request url /dana/js?prot=1&svc=4 came from IP 93.19.66.118.\"",
        "event": {
            "code": "AUT31556",
            "provider": "auth"
        },
        "action": {
            "name": "AUT31556"
        },
        "network": {
            "forwarded_ip": "172.16.128.22"
        },
        "service": {
            "name": "CB2XXPCS02",
            "type": "vpn"
        },
        "user": {
            "name": "System"
        },
        "source": {
            "ip": "93.19.66.118",
            "address": "93.19.66.118"
        },
        "url": {
            "path": "/dana/js?prot=1&svc=4"
        },
        "related": {
            "ip": [
                "93.19.66.118"
            ],
            "user": [
                "System"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`event.code` | `keyword` | Identification code for this event. |
|`event.provider` | `keyword` | Source of the event. |
|`network.forwarded_ip` | `ip` | Host IP address when the source IP address is the proxy. |
|`service.name` | `keyword` | Name of the service. |
|`service.type` | `keyword` | The type of the service. |
|`source.ip` | `ip` | IP address of the source. |
|`url.path` | `wildcard` | Path of the request, such as "/search". |
|`user.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user.roles` | `keyword` | Array of user roles at the time of the event. |

