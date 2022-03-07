
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web proxy` | Proxy logs show the requests made by users and applications on your network. |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "traffic-http-transaction.json"

    ```json
	
    {
        "destination": {
            "address": "example.com",
            "domain": "example.com",
            "ip": "1.1.1.1",
            "port": 443,
            "registered_domain": "example.com",
            "top_level_domain": "com"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "http-transaction",
            "duration": 100,
            "kind": "traffic",
            "start": "2021-09-09T13:01:23Z"
        },
        "fortinet": {
            "devid": "OIDL03VZRZEDKKD",
            "level": "notice",
            "logid": "1000234512",
            "policyid": "1",
            "reqtime": "2021-09-09T10:14:43Z",
            "respfinishtime": "2021-09-09T10:14:43Z",
            "resptime": "2021-09-09T10:14:43Z",
            "vd": "root"
        },
        "http": {
            "request": {
                "bytes": 100
            },
            "response": {
                "bytes": 200,
                "status_code": 200
            }
        },
        "message": "time=15:01:23 devname=\"fortiproxyunit\" devid=\"OIDL03VZRZEDKKD\" logid=\"1000234512\" type=\"traffic\" subtype=\"http-transaction\" level=\"notice\" vd=\"root\" eventtime=1631192483 srcip=192.168.1.2 dstip=1.1.1.1 scheme=\"https\" srcport=123456 dstport=443 hostname=\"example.com\" url=\"https://example.com/foo.html?id=123\" policyid=1 reqlength=100 resplength=200 resptype=\"normal\" statuscode=200 reqtime=1631182483 resptime=1631182483 respfinishtime=1631182483 duration=100",
        "observer": {
            "hostname": "fortiproxyunit",
            "product": "FortiProxy",
            "type": "proxy",
            "vendor": "Fortinet"
        },
        "related": {
            "hosts": [
                "fortiproxyunit",
                "example.com"
            ],
            "ip": [
                "1.1.1.1",
                "192.168.1.2"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "fortiproxy",
                "dialect_uuid": "270777d7-0c5a-42fb-b901-b7fadfb00000"
            }
        },
        "source": {
            "address": "192.168.1.2",
            "ip": "192.168.1.2",
            "port": 123456
        },
        "url": {
            "domain": "example.com",
            "full": "https://example.com/foo.html?id=123",
            "original": "https://example.com/foo.html?id=123",
            "path": "/foo.html",
            "query": "id=123",
            "scheme": "https"
        }
    }
    	
	```


=== "webfilter.json"

    ```json
	
    {
        "action": {
            "name": "passthrough",
            "type": "ftgd_allow"
        },
        "destination": {
            "address": "example.fr",
            "domain": "example.fr",
            "ip": "1.1.1.1",
            "port": 443,
            "registered_domain": "example.fr",
            "top_level_domain": "fr"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "webfilter",
            "kind": "utm",
            "start": "2021-09-09T09:32:39Z"
        },
        "fortinet": {
            "devid": "OIDL03VZRZEDKKD",
            "dstintfrole": "undefined",
            "group": "groupname",
            "level": "notice",
            "logid": "1000234512",
            "policyid": "5",
            "proto": "6",
            "reqtype": "referral",
            "sessionid": "10000000",
            "srcintfrole": "undefined",
            "vd": "root"
        },
        "message": "time=14:19:19 devname=\"fortiproxyunit\" devid=\"OIDL03VZRZEDKKD\" logid=\"1000234512\" type=\"utm\" subtype=\"webfilter\" eventtype=\"ftgd_allow\" level=\"notice\" vd=\"root\" eventtime=1631179959 policyid=5 sessionid=10000000 user=\"john\" group=\"groupname\" srcip=192.168.1.2 srcport=10000 srcintf=\"eth\" srcintfrole=\"undefined\" dstip=1.1.1.1 dstport=443 dstintf=\"eth\" dstintfrole=\"undefined\" proto=6 service=\"HTTPS\" hostname=\"example.fr\" profile=\"standard\" action=\"passthrough\" reqtype=\"referral\" url=\"/foo/bar.html?id=1\"",
        "network": {
            "protocol": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "eth"
                }
            },
            "hostname": "fortiproxyunit",
            "ingress": {
                "interface": {
                    "name": "eth"
                }
            },
            "product": "FortiProxy",
            "type": "proxy",
            "vendor": "Fortinet"
        },
        "related": {
            "hosts": [
                "example.fr",
                "fortiproxyunit"
            ],
            "ip": [
                "1.1.1.1",
                "192.168.1.2"
            ],
            "user": [
                "john"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "fortiproxy",
                "dialect_uuid": "270777d7-0c5a-42fb-b901-b7fadfb00000"
            }
        },
        "service": {
            "name": "https"
        },
        "source": {
            "address": "192.168.1.2",
            "ip": "192.168.1.2",
            "port": 10000
        },
        "url": {
            "domain": "example.fr",
            "full": "example.fr/foo/bar.html?id=1",
            "original": "/foo/bar.html?id=1",
            "path": "/foo/bar.html",
            "query": "id=1"
        },
        "user": {
            "name": "john"
        }
    }
    	
	```


=== "dlp.json"

    ```json
	
    {
        "action": {
            "name": "log-only",
            "type": "dlp"
        },
        "destination": {
            "address": "example.fr",
            "domain": "example.fr",
            "ip": "2.2.2.2",
            "port": 443,
            "registered_domain": "example.fr",
            "top_level_domain": "fr"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "dlp",
            "kind": "utm",
            "start": "2021-09-09T12:29:04Z"
        },
        "file": {
            "name": "picture.png",
            "size": 100,
            "type": "png"
        },
        "fortinet": {
            "devid": "OIDL03VZRZEDKKD",
            "direction": "incoming",
            "dstintfrole": "undefined",
            "eventid": "0",
            "filtercat": "none",
            "filteridx": "0",
            "filtertype": "none",
            "group": "GROUPNAME",
            "level": "notice",
            "logid": "1000234512",
            "policyid": "6",
            "profile": "profile_name",
            "proto": "6",
            "sessionid": "000000001",
            "severity": "medium",
            "srcintfrole": "undefined",
            "vd": "root"
        },
        "message": "time=14:29:04 devname=\"fortiproxyunit\" devid=\"OIDL03VZRZEDKKD\" logid=\"1000234512\" type=\"utm\" subtype=\"dlp\" eventtype=\"dlp\" level=\"notice\" vd=\"root\" eventtime=1631190544 filteridx=0 filtertype=\"none\" filtercat=\"none\" severity=\"medium\" policyid=6 sessionid=000000001 epoch=402874927 eventid=0 user=\"USERNAME\" group=\"GROUPNAME\" srcip=192.168.1.2 srcport=12345 srcintf=\"eth\" srcintfrole=\"undefined\" dstip=2.2.2.2 dstport=443 dstintf=\"eth\" dstintfrole=\"undefined\" proto=6 service=\"HTTPS\" filetype=\"png\" direction=\"incoming\" action=\"log-only\" hostname=\"example.fr\" url=\"/rmn.png?foo=bar\" agent=\"Custom Useragent\" filename=\"picture.png\" filesize=100 profile=\"profile_name\"",
        "network": {
            "direction": "inbound",
            "protocol": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "eth"
                }
            },
            "hostname": "fortiproxyunit",
            "ingress": {
                "interface": {
                    "name": "eth"
                }
            },
            "product": "FortiProxy",
            "type": "proxy",
            "vendor": "Fortinet"
        },
        "related": {
            "hosts": [
                "example.fr",
                "fortiproxyunit"
            ],
            "ip": [
                "192.168.1.2",
                "2.2.2.2"
            ],
            "user": [
                "USERNAME"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "fortiproxy",
                "dialect_uuid": "270777d7-0c5a-42fb-b901-b7fadfb00000"
            }
        },
        "service": {
            "name": "https"
        },
        "source": {
            "address": "192.168.1.2",
            "ip": "192.168.1.2",
            "port": 12345
        },
        "url": {
            "domain": "example.fr",
            "full": "example.fr/rmn.png?foo=bar",
            "original": "/rmn.png?foo=bar",
            "path": "/rmn.png",
            "query": "foo=bar"
        },
        "user": {
            "name": "USERNAME"
        },
        "user_agent": {
            "original": "Custom Useragent"
        }
    }
    	
	```


=== "event-system.json"

    ```json
	
    {
        "action": {
            "name": "transfer"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "system",
            "kind": "event",
            "start": "2021-09-16T07:44:52Z"
        },
        "fortinet": {
            "devid": "OIDL03VZRZEDKKD",
            "level": "warning",
            "logdesc": "File dropped due to poor network connection",
            "logid": "1000234512",
            "msg": "1 file were dropped by quard to FortiSandbox: 0 reached max retries, 1 reached TTL.",
            "reason": "poor-network-condition",
            "status": "drop",
            "vd": "root"
        },
        "message": "time=09:44:52 devname=\"fortiproxyunit\" devid=\"OIDL03VZRZEDKKD\" logid=\"1000234512\" type=\"event\" subtype=\"system\" level=\"warning\" vd=\"root\" eventtime=1631778292 logdesc=\"File dropped due to poor network connection\" count=6 action=\"transfer\" status=\"drop\" reason=\"poor-network-condition\" msg=\"1 file were dropped by quard to FortiSandbox: 0 reached max retries, 1 reached TTL.\"",
        "observer": {
            "hostname": "fortiproxyunit",
            "product": "FortiProxy",
            "type": "proxy",
            "vendor": "Fortinet"
        },
        "related": {
            "hosts": [
                "fortiproxyunit"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "fortiproxy",
                "dialect_uuid": "270777d7-0c5a-42fb-b901-b7fadfb00000"
            }
        }
    }
    	
	```


=== "app-ctrl.json"

    ```json
	
    {
        "action": {
            "name": "pass",
            "type": "app-ctrl-all"
        },
        "destination": {
            "address": "example.com",
            "domain": "example.com",
            "ip": "1.2.3.4",
            "port": 443,
            "registered_domain": "example.com",
            "top_level_domain": "com"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "app-ctrl",
            "kind": "utm",
            "start": "2021-09-09T13:01:22Z"
        },
        "network": {
            "direction": "inbound",
            "protocol": "tcp"
        },
        "fortinet": {
            "app": "HTTPS.BROWSER",
            "applist": "standard",
            "apprisk": "medium",
            "appcat": "Web.Client",
            "devid": "OIDL03VZRZEDKKD",
            "dstintfrole": "undefined",
            "group": "ADM",
            "level": "information",
            "logid": "1000234512",
            "policyid": "01",
            "sessionid": "000000001",
            "direction": "incoming",
            "srcintfrole": "undefined",
            "vd": "root",
            "incidentserialno": "123456789",
            "proto": "6"
        },
        "message": "time=15:01:22 devname=\"fortiproxyunit\" devid=\"OIDL03VZRZEDKKD\" logid=\"1000234512\" type=\"utm\" subtype=\"app-ctrl\" eventtype=\"app-ctrl-all\" level=\"information\" vd=\"root\" eventtime=1631192482 appid=65432 user=\"jean@SEKOIANETWORK.EXAMPLE.FR\" group=\"ADM\" srcip=192.168.1.2 dstip=1.2.3.4 srcport=43564 dstport=443 srcintf=\"port01\" srcintfrole=\"undefined\" dstintf=\"port01\" dstintfrole=\"undefined\" proto=6 service=\"HTTPS\" direction=\"incoming\" policyid=01 sessionid=000000001 applist=\"standard\" appcat=\"Web.Client\" app=\"HTTPS.BROWSER\" action=\"pass\" hostname=\"example.com\" incidentserialno=123456789 url=\"/\" msg=\"Web.Client: HTTPS.BROWSER,\" apprisk=\"medium\"",
        "observer": {
            "egress": {
                "interface": {
                    "name": "port01"
                }
            },
            "hostname": "fortiproxyunit",
            "ingress": {
                "interface": {
                    "name": "port01"
                }
            },
            "product": "FortiProxy",
            "type": "proxy",
            "vendor": "Fortinet"
        },
        "process": {
            "pid": 65432
        },
        "related": {
            "hosts": [
                "fortiproxyunit",
                "example.com"
            ],
            "ip": [
                "192.168.1.2",
                "1.2.3.4"
            ],
            "user": [
                "jean@SEKOIANETWORK.EXAMPLE.FR"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "fortiproxy",
                "dialect_uuid": "270777d7-0c5a-42fb-b901-b7fadfb00000"
            }
        },
        "service": {
            "name": "https"
        },
        "source": {
            "address": "192.168.1.2",
            "ip": "192.168.1.2",
            "port": 43564
        },
        "url": {
            "domain": "example.com",
            "full": "example.com/",
            "original": "/",
            "path": "/"
        },
        "user": {
            "name": "jean@SEKOIANETWORK.EXAMPLE.FR"
        }
    }
    	
	```


=== "forward.json"

    ```json
	
    {
        "action": {
            "name": "accept",
            "type": "allow"
        },
        "destination": {
            "address": "1.2.3.4",
            "bytes": 1000,
            "geo": {
                "country_name": "France"
            },
            "ip": "1.2.3.4",
            "port": 443
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "forward",
            "duration": 100,
            "kind": "traffic",
            "start": "2021-09-08T07:40:24Z"
        },
        "fortinet": {
            "appcat": "appcat1",
            "devid": "OIDL03VZRZEDKKD",
            "dstintfrole": "undefined",
            "lanout": "5000",
            "level": "notice",
            "logid": "1000234512",
            "policyid": "1",
            "policytype": "policy",
            "proto": "6",
            "sessionid": "000000001",
            "srcintfrole": "undefined",
            "vd": "root",
            "wanin": "01",
            "wanout": "2000"
        },
        "message": "time=09:40:24 devname=\"fortiproxyunit\" devid=\"OIDL03VZRZEDKKD\" logid=\"1000234512\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" eventtime=1631086824 srcip=192.168.1.2 srcport=11111 srcintf=\"eth\" srcintfrole=\"undefined\" dstip=1.2.3.4 dstport=443 dstintf=\"eth\" dstintfrole=\"undefined\" sessionid=000000001 dstcountry=\"France\" srccountry=\"Reserved\" service=\"HTTPS\" wanoptapptype=\"web\" proto=6 action=\"accept\" duration=100 policyid=1 policytype=\"policy\" wanin=01 rcvdbyte=1000 wanout=2000 lanin=3000 sentbyte=4000 lanout=5000 appcat=\"appcat1\" utmaction=\"allow\" countweb=4",
        "network": {
            "protocol": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "eth"
                }
            },
            "hostname": "fortiproxyunit",
            "ingress": {
                "interface": {
                    "name": "eth"
                }
            },
            "product": "FortiProxy",
            "type": "proxy",
            "vendor": "Fortinet"
        },
        "related": {
            "hosts": [
                "fortiproxyunit"
            ],
            "ip": [
                "1.2.3.4",
                "192.168.1.2"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "fortiproxy",
                "dialect_uuid": "270777d7-0c5a-42fb-b901-b7fadfb00000"
            }
        },
        "service": {
            "name": "https"
        },
        "source": {
            "address": "192.168.1.2",
            "bytes": 4000,
            "geo": {
                "country_name": "Reserved"
            },
            "ip": "192.168.1.2",
            "port": 11111
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`client.packets` | `long` | Packets sent from the client to the server. |
|`destination.bytes` | `long` | Bytes sent from the destination to the source. |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.geo.country_name` | `keyword` | Country name. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.packets` | `long` | Packets sent from the destination to the source. |
|`destination.port` | `long` | Port of the destination. |
|`email.from` | `keyword` | None |
|`email.to` | `keyword` | None |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.duration` | `long` | Duration of the event in nanoseconds. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.size` | `long` | File size in bytes. |
|`file.type` | `keyword` | File type (file, dir, or symlink). |
|`fortinet.app` | `keyword` | None |
|`fortinet.appcat` | `keyword` | None |
|`fortinet.applist` | `keyword` | None |
|`fortinet.apprisk` | `keyword` | None |
|`fortinet.authproto` | `keyword` | None |
|`fortinet.collectedemail` | `keyword` | None |
|`fortinet.comment` | `keyword` | None |
|`fortinet.countapp` | `keyword` | None |
|`fortinet.devcategory` | `keyword` | None |
|`fortinet.devid` | `keyword` | None |
|`fortinet.direction` | `keyword` | None |
|`fortinet.dlpextra` | `keyword` | keyword |
|`fortinet.docsource` | `keyword` | None |
|`fortinet.dstcollectedemail` | `keyword` | None |
|`fortinet.dstdevcategory` | `keyword` | None |
|`fortinet.dstdevtype` | `keyword` | None |
|`fortinet.dstintfrole` | `keyword` | None |
|`fortinet.dstosname` | `keyword` | None |
|`fortinet.dstosversion` | `keyword` | None |
|`fortinet.dstserver` | `keyword` | None |
|`fortinet.dstssid` | `keyword` | None |
|`fortinet.dstunauthuser` | `keyword` | None |
|`fortinet.dstuuid` | `keyword` | None |
|`fortinet.eventid` | `keyword` | None |
|`fortinet.fctuid` | `keyword` | None |
|`fortinet.filtercat` | `keyword` | None |
|`fortinet.filteridx` | `keyword` | None |
|`fortinet.filtername` | `keyword` | None |
|`fortinet.filtertype` | `keyword` | None |
|`fortinet.forwardedfor` | `keyword` | None |
|`fortinet.group` | `keyword` | None |
|`fortinet.incidentserialno` | `keyword` | None |
|`fortinet.lanin` | `keyword` | None |
|`fortinet.lanout` | `keyword` | None |
|`fortinet.level` | `keyword` | None |
|`fortinet.logdesc` | `keyword` | None |
|`fortinet.logid` | `keyword` | None |
|`fortinet.masterdstmac` | `keyword` | None |
|`fortinet.mastersrcmac` | `keyword` | None |
|`fortinet.msg` | `keyword` | None |
|`fortinet.osversion` | `keyword` | None |
|`fortinet.policyid` | `keyword` | None |
|`fortinet.policymode` | `keyword` | None |
|`fortinet.policytype` | `keyword` | None |
|`fortinet.poluuid` | `keyword` | None |
|`fortinet.profile` | `keyword` | None |
|`fortinet.proto` | `keyword` | None |
|`fortinet.reason` | `keyword` | None |
|`fortinet.recipient` | `keyword` | None |
|`fortinet.reqtime` | `keyword` | None |
|`fortinet.reqtype` | `keyword` | None |
|`fortinet.respfinishtime` | `keyword` | None |
|`fortinet.resptime` | `keyword` | None |
|`fortinet.resptype` | `keyword` | None |
|`fortinet.sender` | `keyword` | None |
|`fortinet.sessionid` | `keyword` | None |
|`fortinet.severity` | `keyword` | None |
|`fortinet.shaperdroprcvdbyte` | `keyword` | None |
|`fortinet.shaperdropsentbyte` | `keyword` | None |
|`fortinet.shaperperipdropbyte` | `keyword` | None |
|`fortinet.shaperperipname` | `keyword` | None |
|`fortinet.shaperrcvdname` | `keyword` | None |
|`fortinet.shapersentname` | `keyword` | None |
|`fortinet.srcintfrole` | `keyword` | None |
|`fortinet.srcserver` | `keyword` | None |
|`fortinet.srcssid` | `keyword` | None |
|`fortinet.srcuuid` | `keyword` | None |
|`fortinet.status` | `keyword` | None |
|`fortinet.subject` | `keyword` | None |
|`fortinet.trandisp` | `keyword` | None |
|`fortinet.tranip` | `keyword` | None |
|`fortinet.trueclntip` | `keyword` | None |
|`fortinet.unauthuser` | `keyword` | None |
|`fortinet.unauthusersource` | `keyword` | None |
|`fortinet.utmref` | `keyword` | None |
|`fortinet.vd` | `keyword` | None |
|`fortinet.vpn` | `keyword` | None |
|`fortinet.vpntype` | `keyword` | None |
|`fortinet.vrf` | `keyword` | None |
|`fortinet.vwpvlanid` | `keyword` | None |
|`fortinet.wanin` | `keyword` | None |
|`fortinet.wanout` | `keyword` | None |
|`host.name` | `keyword` | Name of the host. |
|`host.os.platform` | `keyword` | Operating system platform (such centos, ubuntu, windows). |
|`host.type` | `keyword` | Type of host. |
|`http.request.bytes` | `long` | Total size in bytes of the request (body and headers). |
|`http.response.bytes` | `long` | Total size in bytes of the response (body and headers). |
|`http.response.status_code` | `long` | HTTP response status code. |
|`observer.egress.interface.name` | `keyword` | Interface name |
|`observer.hostname` | `keyword` | Hostname of the observer. |
|`observer.ingress.interface.name` | `keyword` | Interface name |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`process.pid` | `long` | Process id. |
|`server.nat.ip` | `ip` | Server NAT ip |
|`server.nat.port` | `long` | Server NAT port |
|`service.name` | `keyword` | Name of the service. |
|`source.bytes` | `long` | Bytes sent from the source to the destination. |
|`source.geo.country_name` | `keyword` | Country name. |
|`source.ip` | `ip` | IP address of the source. |
|`source.mac` | `keyword` | MAC address of the source. |
|`source.port` | `long` | Port of the source. |
|`url.domain` | `keyword` | Domain of the url. |
|`url.full` | `wildcard` | Full unparsed URL. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

