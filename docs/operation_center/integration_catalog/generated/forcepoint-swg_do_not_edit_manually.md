
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web proxy` | Forcepoint Secure Web Gateway logs provide information about the connected client and the requested resource |
| `Web logs` | Forcepoint Secure Web Gateway logs provide information about the connected client and the requested resource |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network` |
| Type | `` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "test_transaction_blocked.json"

    ```json
	
    {
        "@timestamp": "2022-05-26T09:26:53.000000Z",
        "message": "0|Forcepoint|Security|8.5.4|9|Transaction blocked|7| act=blocked app=http dvc=9.8.7.6 dst=5.6.7.8 dhost=ctldl.windowsupdate.com dpt=80 src=1.2.3.4 spt=62062 suser=- loginID=- destinationTranslatedPort=0 rt=1653557213000 in=0 out=0 requestMethod=GET requestClientApplication=Microsoft-CryptoAPI/10.0 reason=- cs1Label=Policy cs1=SupAd**_O365_ cs2Label=DynCat cs2=0 cs3Label=ContentType cs3=- cn1Label=DispositionCode cn1=1025 cn2Label=ScanDuration cn2=5 request=http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/disallowedcertstl.cab logRecordSource=OnPrem",
        "source": {
            "ip": "1.2.3.4",
            "port": 62062
        },
        "destination": {
            "ip": "5.6.7.8",
            "domain": "ctldl.windowsupdate.com",
            "port": 80
        },
        "event": {
            "severity": 7,
            "code": "1025",
            "kind": "event",
            "type": [
                "access",
                "denied"
            ],
            "category": [
                "network"
            ],
            "action": "Transaction blocked",
            "duration": 5,
            "reason": "Category blocked"
        },
        "observer": {
            "version": "8.5.4",
            "product": "Secure Web Gateway",
            "vendor": "Forcepoint"
        },
        "host": {
            "ip": "9.8.7.6"
        },
        "url": {
            "original": "http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/disallowedcertstl.cab"
        },
        "user_agent": {
            "original": "Microsoft-CryptoAPI/10.0"
        },
        "network": {
            "protocol": "http"
        },
        "rule": {
            "id": "9",
            "ruleset": "Information Technology"
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "forcepoint": {
            "cef": {
                "version": "0"
            },
            "webgateway": {
                "category": "0",
                "log": {
                    "source": "OnPrem"
                },
                "policies": [
                    "SupAd**_O365_"
                ]
            }
        }
    }
    	
	```


=== "test_transaction_permitted.json"

    ```json
	
    {
        "@timestamp": "2022-05-26T08:58:41.000000Z",
        "message": "0|Forcepoint|Security|8.5.4|222|Transaction permitted|1| act=permitted app=https dvc=9.8.7.6 dst=5.6.7.8 dhost=outlook.office365.com dpt=443 src=1.2.3.4 spt=50345 suser=LDAP://4.3.2.1 OU\\=MyOrg,OU\\=Users,DC\\=Domain,DC\\=LOCAL/User 1 loginID=n_nini destinationTranslatedPort=47486 rt=1653555521000 in=1038458 out=3967 requestMethod=POST requestClientApplication=Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.10386; Pro) reason=- cs1Label=Policy cs1=SupAd**1,SupAd**2 cs2Label=DynCat cs2=0 cs3Label=ContentType cs3=application/mapi-http cn1Label=DispositionCode cn1=1026 cn2Label=ScanDuration cn2=31 request=https://outlook.office365.com/ logRecordSource=OnPrem",
        "source": {
            "ip": "1.2.3.4",
            "port": 50345
        },
        "destination": {
            "ip": "5.6.7.8",
            "domain": "outlook.office365.com",
            "port": 443,
            "nat": {
                "port": 47486
            }
        },
        "event": {
            "severity": 1,
            "code": "1026",
            "kind": "event",
            "type": [
                "access",
                "allowed"
            ],
            "category": [
                "network"
            ],
            "action": "Transaction permitted",
            "duration": 31,
            "reason": "Category permitted"
        },
        "observer": {
            "version": "8.5.4",
            "product": "Secure Web Gateway",
            "vendor": "Forcepoint"
        },
        "host": {
            "ip": "9.8.7.6"
        },
        "url": {
            "original": "https://outlook.office365.com/",
            "path": "/"
        },
        "user_agent": {
            "original": "Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.10386; Pro)"
        },
        "user": {
            "name": "LDAP://4.3.2.1 OU\\=MyOrg,OU\\=Users,DC\\=Domain,DC\\=LOCAL/User 1",
            "id": "n_nini"
        },
        "network": {
            "protocol": "https"
        },
        "rule": {
            "id": "222",
            "ruleset": "Collaboration - Office"
        },
        "http": {
            "request": {
                "method": "POST",
                "bytes": 3967,
                "mime_type": "application/mapi-http"
            },
            "response": {
                "bytes": 1038458
            }
        },
        "forcepoint": {
            "cef": {
                "version": "0"
            },
            "webgateway": {
                "category": "0",
                "log": {
                    "source": "OnPrem"
                },
                "policies": [
                    "SupAd**1",
                    "SupAd**2"
                ]
            }
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.nat.port` | `long` | Destination NAT Port |
|`destination.port` | `long` | Port of the destination. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.duration` | `long` | Duration of the event in nanoseconds. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.severity` | `long` | Numeric severity of the event. |
|`forcepoint.cef.version` | `keyword` | None |
|`forcepoint.webgateway.category` | `keyword` | None |
|`forcepoint.webgateway.log.source` | `keyword` | None |
|`forcepoint.webgateway.policies` | `keyword` | None |
|`host.ip` | `ip` | Host ip addresses. |
|`http.request.bytes` | `long` | Total size in bytes of the request (body and headers). |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.mime_type` | `keyword` | Mime type of the body of the request. |
|`http.response.bytes` | `long` | Total size in bytes of the response (body and headers). |
|`network.protocol` | `keyword` | Application protocol name. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`observer.version` | `keyword` | Observer version. |
|`rule.id` | `keyword` | Rule ID |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.id` | `keyword` | Unique identifier of the user. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

