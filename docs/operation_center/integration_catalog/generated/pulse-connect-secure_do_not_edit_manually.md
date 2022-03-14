
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
        "action": {
            "name": "AUT24804"
        },
        "event": {
            "provider": "auth",
            "code": "AUT24804"
        }
    }
    	
	```


=== "host_checker_policy_success.json"

    ```json
	
    {
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
        "action": {
            "name": "AUT24803"
        },
        "event": {
            "provider": "auth",
            "code": "AUT24803"
        }
    }
    	
	```


=== "login_failed.json"

    ```json
	
    {
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
        "action": {
            "name": "AUT23457"
        },
        "event": {
            "provider": "auth",
            "code": "AUT23457"
        }
    }
    	
	```


=== "unauthenticated_request.json"

    ```json
	
    {
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
        "action": {
            "name": "AUT31556"
        },
        "event": {
            "provider": "auth",
            "code": "AUT31556"
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

