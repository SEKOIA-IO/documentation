
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network device logs` | Fortigates can record traffic logs flowing through their firewall. |
| `Network intrusion detection system` | Security logs provided by Fortigates include intrusion prevention related records. |
| `Web application firewall logs` | Fortiweb appliances and virtual appliances record WAF information. |
| `Web logs` | WAF information produces by Fortiweb units can record permited URL access. |
| `DNS records` | Both DNS queries and responses handled by the Fortigate domain name servers can be recorded. |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "Configuration_changed.CEF.json"

    ```json
	
    {
        "event": {
            "code": "0100032102",
            "outcome": "success",
            "dialect": "fortigate",
            "severity": "7",
            "reason": "Configuration is changed in the admin session",
            "category": "event",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "message": "CEF:0|Fortinet|Fortigate|v6.2.9|32102|event:system|7|deviceExternalId=FGVM2V0000171868 FortinetFortiGatelogid=0100032102 cat=event:system FortinetFortiGatesubtype=system FortinetFortiGatelevel=alert FortinetFortiGatevd=root FortinetFortiGateeventtime=1637681708541881380 FortinetFortiGatetz=+0100 FortinetFortiGatelogdesc=Configuration changed duser= sproc=console msg=Configuration is changed in the admin session",
        "observer": {
            "type": "Fortigate",
            "vendor": "Fortinet",
            "version": "v6.2.9"
        },
        "action": {
            "outcome": "success",
            "type": "system"
        },
        "log": {
            "level": "alert"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "IP_SEC.STANDARD.json"

    ```json
	
    {
        "event": {
            "code": "0101037130",
            "outcome": "success",
            "dialect": "fortigate",
            "reason": "progress IPsec phase 2",
            "category": "event",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "error"
        },
        "message": "time=17:24:16 devname=\"abc\" devid=\"1\" logid=\"0101037130\" type=\"event\" subtype=\"vpn\" level=\"error\" vd=\"root\" eventtime=1580142256 logdesc=\"Progress IPsec phase 2\" msg=\"progress IPsec phase 2\" action=\"negotiate\" remip=1.1.1.1 locip=93.187.43.9 remport=500 locport=500 outintf=\"N/A\" cookies=\"07f928d94dd975ea/89b1d990f54f0b82\" user=\"N/A\" group=\"N/A\" xauthuser=\"N/A\" xauthgroup=\"N/A\" assignip=N/A vpntunnel=\"VPN-ACCENTURE\" status=\"failure\" init=\"local\" exch=\"CREATE_CHILD\" dir=\"inbound\" role=\"initiator\" result=\"ERROR\" version=\"IKEv2\"",
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "user": {
                "name": "N/A"
            }
        },
        "action": {
            "name": "negotiate",
            "outcome": "failure",
            "type": "vpn"
        },
        "related": {
            "ip": [
                "1.1.1.1"
            ],
            "user": [
                "N/A"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "LOGOUT.STANDARD.json"

    ```json
	
    {
        "action": {
            "name": "logout",
            "outcome": "success",
            "type": "system"
        },
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2"
        },
        "event": {
            "category": "event",
            "code": "0100032003",
            "reason": "Administrator test logged out from jsconsole",
            "action": "exit",
            "created": "2021-04-26T05:31:28.317798Z",
            "original": "7SWUWw0hIzFir8RNBlQmV40jtrt8wZG9nE38nymazmLyCGCdfpiNw6JDavRaSt6R",
            "dialect_uuid": "7f69d51f-c863-4347-8fdb-6201b763ce12",
            "id": "7a0c0ade-d30f-4b10-933b-abf4a7b459ee",
            "outcome": "success",
            "provider": "jsconsole",
            "dialect": "fortigate",
            "kind": "event"
        },
        "log": {
            "level": "information"
        },
        "message": "time=16:48:00 devname=\"abc\" devid=\"1\" logid=\"0100032003\" type=\"event\" subtype=\"system\" level=\"information\" vd=\"root\" eventtime=1619621280 logdesc=\"Admin logout successful\" sn=\"1619620402\" user=\"test\" ui=\"jsconsole\" method=\"jsconsole\" srcip=1.1.1.1 dstip=2.2.2.2 action=\"logout\" status=\"success\" duration=878 reason=\"exit\" msg=\"Administrator test logged out from jsconsole\"",
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "user": {
                "name": "test"
            }
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ],
            "user": [
                "test"
            ]
        },
        "http": {
            "request": {
                "method": "jsconsole"
            }
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "ROLL-LOG.STANDARD.json"

    ```json
	
    {
        "action": {
            "name": "roll-log",
            "outcome": "success",
            "type": "system"
        },
        "event": {
            "category": "event",
            "code": "0100032011",
            "reason": "Disk log has rolled.",
            "action": "file-size",
            "created": "2021-04-26T05:03:41.964860Z",
            "original": "cdb5bxPLGIua7HGZV17aRAr3oU4q8HDxTCcWwbHXjL1xIeiPefRmfZNwDmmblhpM",
            "dialect_uuid": "d9baa40e-09c4-45d4-83db-d655e99288eb",
            "id": "f6536ec3-038f-4fe4-a252-45aae61257a6",
            "outcome": "success",
            "dialect": "fortigate",
            "kind": "event"
        },
        "log": {
            "level": "notice"
        },
        "message": "time=16:23:50 devname=\"abc\" devid=\"1\" logid=\"0100032011\" type=\"event\" subtype=\"system\" level=\"notice\" vd=\"PRX1-AA\" eventtime=1619619830 logdesc=\"Disk log rolled\" action=\"roll-log\" reason=\"file-size\" log=\"tlog\" msg=\"Disk log has rolled.\"",
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "WAD.STANDARD.json"

    ```json
	
    {
        "action": {
            "name": "send",
            "outcome": "success",
            "type": "wad"
        },
        "destination": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "port": 8002
        },
        "event": {
            "category": "event",
            "code": "0105048039",
            "reason": "SSL Alert sent",
            "created": "2021-04-26T04:17:39.492286Z",
            "original": "CO0Bc1MbjbOwVYPYTY69yQWWHIKOI8wbccbfhTNgD35U8qHRdBl0E8x0SYR7PAFp",
            "dialect_uuid": "a948028d-8e9c-48e3-9f3a-193f2c42e9d1",
            "id": "3b43476c-40d8-45de-91a9-4ee0312bec21",
            "outcome": "success",
            "dialect": "fortigate",
            "kind": "event"
        },
        "fortinet": {
            "event": {
                "desc": "illegal parameter"
            }
        },
        "log": {
            "level": "error"
        },
        "message": "time=15:29:39 devname=\"abc\" devid=\"1\" logid=\"0105048039\" type=\"event\" subtype=\"wad\" level=\"error\" vd=\"PRX1-AA\" eventtime=1619616579 logdesc=\"SSL fatal alert sent\" session_id=473f963d policyid=0 srcip=2.2.2.2 srcport=47782 dstip=1.1.1.1 dstport=8002 action=\"send\" alert=\"2\" desc=\"illegal parameter\" msg=\"SSL Alert sent\"",
        "source": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "port": 47782
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "anomaly.CEF.json"

    ```json
	
    {
        "event": {
            "code": "0720018433",
            "outcome": "success",
            "dialect": "fortigate",
            "category": "anomaly",
            "severity": "7",
            "reason": "anomaly: icmp_flood, 34 > threshold 25, repeats 306 times",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "5702ae4e-7d8a-455f-a47b-ef64dd87c981",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "message": "CEF:0|Fortinet|Fortigate|v5.6.0|18433|anomaly:anomaly clear_ session|7|FTNTFGTlogid=0720018433 cat=anomaly:anomaly FTNTFGTsubtype=anomaly FTNTFGTlevel=alert FTNTFGTvd=vdom1 FTNTFGTseverity=critical src=1.1.1.1 dst=2.2.2.2 deviceInboundInterface=port15 externalId=0 act=clear_session proto=1 app=icmp/146/81 cnt=306 FTNTFGTattack=icmp_flood dpt=20882 FTNTFGTicmptype=0x92 FTNTFGTicmpcode=0x51 FTNTFGTattackid=16777316 FTNTFGTprofile=DoS-policy1 cs2=http://www.fortinet.com/ids/VID16777316 cs2Label=Reference msg=anomaly: icmp_flood, 34 > threshold 25, repeats 306 times FTNTFGTcrscore=50 FTNTFGTcrlevel=critical",
        "source": {
            "ip": "1.1.1.1",
            "address": "1.1.1.1"
        },
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "port": 20882
        },
        "network": {
            "transport": "icmp",
            "application": "icmp/146/81"
        },
        "action": {
            "name": "clear_session",
            "outcome": "success",
            "type": "anomaly"
        },
        "observer": {
            "type": "Fortigate",
            "vendor": "Fortinet",
            "version": "v5.6.0"
        },
        "log": {
            "level": "alert"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "anomaly.CSV.json"

    ```json
	
    {
        "message": "date=2016-02-12,time=14:10:42,logid=0720018433,type=anomaly,subtype=anomaly,level=alert,vd=\"vdom1\",severity=critical,srcip=1.1.1.1,dstip=2.2.2.2,srcintf=\"port15\",sessionid=0,action=clear_session,proto=1,service=\"icmp/146/81\",count=306,attack=\"icmp_ flood\",dstport=20882,icmptype=0x92,icmpcode=0x51,attackid=16777316,profile=\"DoS-policy1\",ref=\"http://www.fortinet.com/ids/VID16777316\",msg=\"anomaly: icmp_flood, 34 > threshold 25, repeats 306 times\",crscore=50,crlevel=critical",
        "event": {
            "category": "anomaly",
            "code": "0720018433",
            "reason": "anomaly: icmp_flood, 34 > threshold 25, repeats 306 times",
            "dialect": "fortigate",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "kind": "event",
            "severity": "critical"
        },
        "action": {
            "name": "clear_session",
            "outcome": "success",
            "type": "anomaly"
        },
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "port": 20882
        },
        "log": {
            "level": "alert"
        },
        "network": {
            "protocol": "icmp/146/81",
            "transport": "icmp"
        },
        "observer": {
            "ingress": {
                "interface": {
                    "name": "port15"
                }
            }
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        },
        "icmp": {
            "request": {
                "type": "0x92",
                "code": "0x51"
            }
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        }
    }
    	
	```


=== "anomaly.STANDARD.json"

    ```json
	
    {
        "message": "date=2016-02-12 time=14:10:42 logid=0720018433 type=anomaly subtype=anomaly level=alert vd=\"vdom1\" severity=critical srcip=1.1.1.1 dstip=2.2.2.2 srcintf=\"port15\" sessionid=0 action=clear_session proto=1 service=\"icmp/146/81\" count=306 attack=\"icmp_ flood\" dstport=20882 icmptype=0x92 icmpcode=0x51 attackid=16777316 profile=\"DoS-policy1\" ref=\"http://www.fortinet.com/ids/VID16777316\" msg=\"anomaly: icmp_flood, 34 > threshold 25, repeats 306 times\" crscore=50 crlevel=critical",
        "event": {
            "category": "anomaly",
            "code": "0720018433",
            "reason": "anomaly: icmp_flood, 34 > threshold 25, repeats 306 times",
            "dialect": "fortigate",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "kind": "event",
            "severity": "critical"
        },
        "action": {
            "name": "clear_session",
            "outcome": "success",
            "type": "anomaly"
        },
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "port": 20882
        },
        "log": {
            "level": "alert"
        },
        "network": {
            "protocol": "icmp/146/81",
            "transport": "icmp"
        },
        "observer": {
            "ingress": {
                "interface": {
                    "name": "port15"
                }
            }
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        },
        "icmp": {
            "request": {
                "type": "0x92",
                "code": "0x51"
            }
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        }
    }
    	
	```


=== "antivirus.CEF.json"

    ```json
	
    {
        "event": {
            "code": "0211008192",
            "reason": "File is infected",
            "outcome": "success",
            "severity": "4",
            "dialect": "fortigate",
            "category": "utm",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "message": "CEF:0|Fortinet|Fortigate|v5.6.0|08192|utm:virus infected blocked|4|FTNTFGTlogid=0211008192 cat=utm:virus FTNTFGTsubtype=virus FTNTFGTeventtype=infected FTNTFGTlevel=warning FTNTFGTvd=vdom1 msg=File is infected act=blocked app=HTTP externalId=56633 src=1.1.1.1 dst=2.2.2.2 spt=45719 dpt=80 deviceInboundInterface=port15 deviceOutboundInterface=port19 proto=6 deviceDirection=0 fname=eicar.com FTNTFGTchecksum=1dd02bdb FTNTFGTquarskip=No-skip cs1=EICAR_TEST_FILE cs1Label=Virus FTNTFGTdtype=Virus cs2=http://www.fortinet.com/ve?vn\\=EICAR_TEST_FILE cs2Label=Reference FTNTFGTvirusid=2172 request=http://2.2.2.2/eicar.com FTNTFGTprofile=default duser= requestClientApplication=Wget/1 10 2 FTNTFGTanalyticscksum=131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267 FTNTFGTanalyticssubmit=false FTNTFGTcrscore=50 FTNTFGTcrlevel=critical",
        "source": {
            "ip": "1.1.1.1",
            "address": "1.1.1.1",
            "port": 45719
        },
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "port": 80
        },
        "url": {
            "domain": "2.2.2.2",
            "full": "http://2.2.2.2/eicar.com",
            "original": "http://2.2.2.2/eicar.com",
            "port": 80,
            "scheme": "http",
            "path": "/eicar.com"
        },
        "action": {
            "name": "blocked",
            "outcome": "success",
            "type": "virus"
        },
        "log": {
            "level": "warning"
        },
        "network": {
            "application": "HTTP",
            "transport": "tcp"
        },
        "file": {
            "name": "eicar.com"
        },
        "observer": {
            "type": "Fortigate",
            "vendor": "Fortinet",
            "version": "v5.6.0"
        },
        "user_agent": {
            "original": "Wget/1 10 2"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "dns.CSV.json"

    ```json
	
    {
        "event": {
            "code": "1501054802",
            "outcome": "success",
            "dialect": "fortigate",
            "reason": "Domain is monitored",
            "category": "dns",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "notice"
        },
        "message": "date=2018-12-27,time=14:45:26,logid=\"1501054802\",type=\"dns\",subtype=\"dns-response\",level=\"notice\",vd=\"vdom1\",eventtime=1545950726,policyid=1,sessionid=13355,user=\"bob\",srcip=1.1.1.1,srcport=54621,srcintf=\"port12\",srcintfrole=\"lan\",dstip=2.2.2.2,dstport=53,dstintf=\"port11\",dstintfrole=\"wan\",proto=17,profile=\"default\",srcmac=\"00:00:00:00:00:00\",xid=5137,qname=\"detectportal.firefox.com\",qtype=\"A\",qtypeval=1,qclass=\"IN\",ipaddr=\"104.80.89.26, 104.80.89.24\",msg=\"Domain is monitored\",action=\"pass\",cat=52,catdesc=\"Information Technology\"",
        "source": {
            "ip": "1.1.1.1",
            "address": "1.1.1.1",
            "port": 54621,
            "mac": "00:00:00:00:00:00",
            "user": {
                "name": "bob"
            }
        },
        "destination": {
            "ip": "2.2.2.2",
            "address": "2.2.2.2",
            "port": 53
        },
        "network": {
            "transport": "udp"
        },
        "dns": {
            "question": {
                "name": "detectportal.firefox.com",
                "type": "A"
            }
        },
        "action": {
            "name": "pass",
            "outcome": "success",
            "type": "dns-response"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "port11"
                }
            },
            "ingress": {
                "interface": {
                    "name": "port12"
                }
            }
        },
        "rule": {
            "category": "Information Technology"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ],
            "user": [
                "bob"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "hostname.STANDARD.json"

    ```json
	
    {
        "event": {
            "code": "1059028704",
            "outcome": "success",
            "dialect": "fortigate",
            "reason": "Web.Client: HTTPS.BROWSER,",
            "category": "utm",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "message": "time=11:09:50 devname=\"abc\" devid=\"1\" logid=\"1059028704\" type=\"utm\" subtype=\"app-ctrl\" eventtype=\"app-ctrl-all\" level=\"information\" vd=\"root\" eventtime=1579860590 appid=40568 srcip=1.1.1.1 dstip=2.2.2.2 srcport=33345 dstport=443 srcintf=\"test\" srcintfrole=\"undefined\" dstintf=\"port1\" dstintfrole=\"undefined\" proto=6 service=\"HTTPS\" direction=\"outgoing\" policyid=1 sessionid=1508480438 applist=\"default\" appcat=\"Web.Client\" app=\"HTTPS.BROWSER\" action=\"pass\" hostname=\"abcd\" incidentserialno=455926217 url=\"/\" msg=\"Web.Client: HTTPS.BROWSER,\" apprisk=\"medium\"",
        "source": {
            "address": "1.1.1.1",
            "port": 33345,
            "ip": "1.1.1.1"
        },
        "destination": {
            "address": "2.2.2.2",
            "port": 443,
            "ip": "2.2.2.2",
            "domain": "abcd"
        },
        "network": {
            "protocol": "HTTPS",
            "transport": "tcp",
            "application": "HTTPS.BROWSER"
        },
        "action": {
            "name": "pass",
            "outcome": "success",
            "type": "app-ctrl"
        },
        "url": {
            "original": "/",
            "full": "/",
            "path": "/"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "port1"
                }
            },
            "ingress": {
                "interface": {
                    "name": "test"
                }
            }
        },
        "fortinet": {
            "apprisk": "medium"
        },
        "rule": {
            "category": "Web.Client",
            "ruleset": "default"
        },
        "related": {
            "hosts": [
                "abcd"
            ],
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "log": {
            "level": "information"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "icmp.json"

    ```json
	
    {
        "event": {
            "code": "0000000011",
            "outcome": "success",
            "dialect": "fortigate",
            "category": "traffic",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "warning"
        },
        "message": " time=15:22:43 devname=\"abc\" devid=\"1\" logid=\"0000000011\" type=\"traffic\" subtype=\"forward\" level=\"warning\" vd=\"root\" eventtime=1602591763587868496 tz=\"+0300\" srcip=1.1.1.1 identifier=256 srcintf=\"internal\" srcintfrole=\"lan\" dstip=2.2.2.2 dstintf=\"wan1\" dstintfrole=\"wan\" srcuuid=\"b22e6ef4-2e38-51ea-72c9-53b2da2e20f5\" dstuuid=\"052bdbce-823a-51e9-eb23-7a3e819fea4f\" poluuid=\"1520e1aa-823a-51e9-984f-a55e1f39b3c7\" sessionid=706677975 proto=1 action=\"ip-conn\" policyid=1 policytype=\"policy\" service=\"icmp/0/8\" dstcountry=\"Netherlands\" srccountry=\"Reserved\" appcat=\"unscanned\" crscore=5 craction=262144 crlevel=\"low\"",
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2"
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        },
        "network": {
            "transport": "icmp",
            "protocol": "icmp/0/8"
        },
        "action": {
            "name": "ip-conn",
            "outcome": "success",
            "type": "forward"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "wan1"
                }
            },
            "ingress": {
                "interface": {
                    "name": "internal"
                }
            }
        },
        "rule": {
            "category": "unscanned",
            "ruleset": "policy"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "icmp6.json"

    ```json
	
    {
        "event": {
            "code": "0001000014",
            "outcome": "success",
            "dialect": "fortigate",
            "category": "traffic",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "notice"
        },
        "message": " time=13:02:14 devname=\"abc\" devid=\"1\" logid=\"0001000014\" type=\"traffic\" subtype=\"local\" level=\"notice\" vd=\"root\" eventtime=1602586934900309053 tz=\"+0200\" srcip=00::00:00:00:00 identifier=0 srcintf=\"AVR-GUEST-AP\" srcintfrole=\"lan\" dstip=12::16 dstintf=\"unknown0\" dstintfrole=\"undefined\" sessionid=1395131 proto=58 action=\"accept\" policyid=0 policytype=\"local-in-policy6\" service=\"icmp6/143/0\" trandisp=\"noop\" app=\"icmp6/143/0\" duration=60 sentbyte=76 rcvdbyte=0 sentpkt=1 rcvdpkt=0 appcat=\"unscanned\"",
        "source": {
            "ip": "00::00:00:00:00",
            "address": "00::00:00:00:00",
            "bytes": 76,
            "packets": 1
        },
        "destination": {
            "address": "12::16",
            "ip": "12::16",
            "bytes": 0,
            "packets": 0
        },
        "network": {
            "transport": "ipv6-icmp",
            "protocol": "icmp6/143/0",
            "application": "icmp6/143/0"
        },
        "action": {
            "name": "accept",
            "outcome": "success",
            "type": "local"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "unknown0"
                }
            },
            "ingress": {
                "interface": {
                    "name": "AVR-GUEST-AP"
                }
            }
        },
        "rule": {
            "category": "unscanned",
            "ruleset": "local-in-policy6"
        },
        "related": {
            "ip": [
                "00::00:00:00:00",
                "12::16"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "icmp_CEF.json"

    ```json
	
    {
        "event": {
            "code": "0001000014",
            "outcome": "success",
            "dialect": "fortigate",
            "severity": "3",
            "category": "traffic",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "notice"
        },
        "message": "CEF:0|Fortinet|Fortigate|v6.0.10|00014|traffic:local accept|3|deviceExternalId=FGVM2V0000171868 FortinetFortiGatelogid=0001000014 cat=traffic:local FortinetFortiGatesubtype=local FortinetFortiGatelevel=notice FortinetFortiGatevd=root FortinetFortiGateeventtime=1602663098 src=1.1.1.1 deviceInboundInterface=port1 FortinetFortiGatesrcintfrole=undefined dst=2.2.2.2 deviceOutboundInterface=root FortinetFortiGatedstintfrole=undefined externalId=4887198 proto=1 FortinetFortiGateaction=accept FortinetFortiGatepolicyid=0 FortinetFortiGatepolicytype=local-in-policy app=icmp/8/0 FortinetFortiGatedstcountry=Reserved FortinetFortiGatesrccountry=China FortinetFortiGatetrandisp=noop FortinetFortiGateapp=icmp/8/0 FortinetFortiGateduration=61 out=84 in=84 FortinetFortiGatesentpkt=1 FortinetFortiGatercvdpkt=1 FortinetFortiGateappcat=unscanned",
        "source": {
            "ip": "1.1.1.1",
            "address": "1.1.1.1",
            "bytes": 84,
            "packets": 1
        },
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "bytes": 84,
            "packets": 1
        },
        "network": {
            "transport": "icmp",
            "application": "icmp/8/0"
        },
        "observer": {
            "type": "Fortigate",
            "vendor": "Fortinet",
            "version": "v6.0.10"
        },
        "action": {
            "name": "accept",
            "outcome": "success",
            "type": "local"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "ping.json"

    ```json
	
    {
        "event": {
            "code": "0000000013",
            "outcome": "success",
            "dialect": "fortigate",
            "category": "traffic",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "notice"
        },
        "message": " time=14:22:37 devname=\"abc\" devid=\"1\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"ROUTER\" eventtime=1602591758311908837 tz=\"+0200\" srcip=1.1.1.1 identifier=29027 srcintf=\"test1\" srcintfrole=\"undefined\" dstip=2.2.2.2 dstintf=\"test\" dstintfrole=\"undefined\" sessionid=3558919660 proto=1 action=\"accept\" policyid=637 policytype=\"policy\" poluuid=\"b23818a6-8f49-51ea-9db7-4e4965a3483c\" service=\"PING\" dstcountry=\"Reserved\" srccountry=\"Reserved\" trandisp=\"noop\" duration=64 sentbyte=420 rcvdbyte=420 sentpkt=5 rcvdpkt=5 appcat=\"unscanned\"",
        "source": {
            "ip": "1.1.1.1",
            "address": "1.1.1.1",
            "bytes": 420,
            "packets": 5
        },
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "bytes": 420,
            "packets": 5
        },
        "network": {
            "transport": "icmp",
            "protocol": "PING"
        },
        "action": {
            "name": "accept",
            "outcome": "success",
            "type": "forward"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "test"
                }
            },
            "ingress": {
                "interface": {
                    "name": "test1"
                }
            }
        },
        "rule": {
            "category": "unscanned",
            "ruleset": "policy"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "ssh_access.CEF.json"

    ```json
	
    {
        "event": {
            "code": "0100032021",
            "outcome": "success",
            "dialect": "fortigate",
            "severity": "7",
            "reason": "Login disabled from IP 1.1.1.1 for 60 seconds because of 3 bad attempts",
            "category": "event",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event",
            "action": "exceed_limit"
        },
        "log": {
            "level": "alert"
        },
        "message": "CEF:0|Fortinet|Fortigate|v6.0.4|32021|event:system login failed|7|deviceExternalId=FGVM2V0000171868 FortinetFortiGatelogid=0100032021 cat=event:system FortinetFortiGatesubtype=system FortinetFortiGatelevel=alert FortinetFortiGatevd=root FortinetFortiGateeventtime=1579172447 FortinetFortiGatelogdesc=Admin login disabled sproc=1.1.1.1 FortinetFortiGateaction=login outcome=failed reason=exceed_limit msg=Login disabled from IP 1.1.1.1 for 60 seconds because of 3 bad attempts",
        "observer": {
            "type": "Fortigate",
            "vendor": "Fortinet",
            "version": "v6.0.4"
        },
        "action": {
            "name": "login",
            "outcome": "success",
            "type": "system"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "ssl_new_con.CEF.json"

    ```json
	
    {
        "event": {
            "category": "event",
            "code": "0101039943",
            "created": "2021-11-19T16:35:03.634246Z",
            "original": "bpcAGOBBHg55aIDKhq5WlL3JM3ZEsHEQxDvgssFqMLvOjShdp8dgfMABGg8n12Aq",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "9825c6ce-619b-4988-b423-d6ee88d1712e",
            "outcome": "success",
            "dialect": "fortigate",
            "severity": "2",
            "reason": "SSL new connection",
            "kind": "event",
            "action": "N/A"
        },
        "log": {
            "level": "information"
        },
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2"
        },
        "message": "CEF - LOG [SEKOIA@53288 intake_key=\"evkyRoUM7fNpYA2MVNDDmQ1kZJWLvLnt\"] CEF:0|Fortinet|Fortigate|v6.0.10|39943|event:vpn ssl-new-con|2|deviceExternalId=FGT3HD3916803645 FTNTFGTlogid=0101039943 cat=event:vpn FTNTFGTsubtype=vpn FTNTFGTlevel=information FTNTFGTvd=root FTNTFGTeventtime=1637338258 FTNTFGTlogdesc=SSL VPN new connection act=ssl-new-con FTNTFGTtunneltype=ssl FTNTFGTtunnelid=0 dst=2.2.2.2 duser=N/A FTNTFGTgroup=N/A FTNTFGTdst_host=N/A reason=N/A msg=SSL new connection",
        "observer": {
            "type": "Fortigate",
            "version": "v6.0.10",
            "vendor": "Fortinet"
        },
        "action": {
            "type": "vpn",
            "outcome": "success",
            "name": "ssl-new-con"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        },
        "related": {
            "ip": [
                "2.2.2.2"
            ]
        }
    }
    	
	```


=== "traffic_forward.CEF-Axens.json"

    ```json
	
    {
        "event": {
            "code": "0000000013",
            "outcome": "success",
            "dialect": "fortigate",
            "severity": "3",
            "category": "traffic",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "notice"
        },
        "message": "CEF:0|Fortinet|Fortigate|v6.0.4|00013|traffic:forward timeout|3|deviceExternalId=FGVM2V0000171868 FortinetFortiGatelogid=0000000013 cat=traffic:forward FortinetFortiGatesubtype=forward FortinetFortiGatelevel=notice FortinetFortiGatevd=root FortinetFortiGateeventtime=1572471876 src=1.1.1.1 spt=49260 deviceInboundInterface=port1 FortinetFortiGatesrcintfrole=undefined dst=3.3.3.3 dpt=80 deviceOutboundInterface=port2 FortinetFortiGatedstintfrole=undefined FortinetFortiGatepoluuid=bafe134e-c0ad-51e8-ed9c-52f798dd69d4 externalId=12812952 proto=6 FortinetFortiGateaction=timeout FortinetFortiGatepolicyid=1 FortinetFortiGatepolicytype=policy app=HTTP FortinetFortiGatedstcountry=Reserved FortinetFortiGatesrccountry=United States FortinetFortiGatetrandisp=dnat destinationTranslatedAddress=2.2.2.2 destinationTranslatedPort=80 FortinetFortiGateduration=20 out=48 in=144 FortinetFortiGatesentpkt=1 FortinetFortiGatercvdpkt=3 FortinetFortiGateappcat=unscanned FortinetFortiGatecrscore=5 FortinetFortiGatecraction=262144 FortinetFortiGatecrlevel=low",
        "source": {
            "ip": "1.1.1.1",
            "address": "1.1.1.1",
            "port": 49260,
            "bytes": 144,
            "packets": 1
        },
        "destination": {
            "nat": {
                "ip": "2.2.2.2",
                "port": 80
            },
            "address": "3.3.3.3",
            "ip": "3.3.3.3",
            "port": 80,
            "bytes": 48,
            "packets": 3
        },
        "network": {
            "transport": "tcp",
            "application": "HTTP"
        },
        "observer": {
            "type": "Fortigate",
            "vendor": "Fortinet",
            "version": "v6.0.4"
        },
        "action": {
            "name": "timeout",
            "outcome": "success",
            "type": "forward"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2",
                "3.3.3.3"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "traffic_forward.CEF.json"

    ```json
	
    {
        "event": {
            "code": "0000000013",
            "outcome": "success",
            "dialect": "fortigate",
            "severity": "3",
            "category": "traffic",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "message": "CEF:0|Fortinet|Fortigate|v5.6.0|00013|traffic:forward close|3|FTNTFGTlogid=0000000013 cat=traffic:forward FTNTFGTsubtype=forward FTNTFGTlevel=notice FTNTFGTvd=vdom1 src=2.2.2.2 shost=2.2.2.2 spt=45719 deviceInboundInterface=port15 dst=3.3.3.3 dhost=3.3.3.3 dpt=80 deviceOutboundInterface=port19 FTNTFGTpoluuid=61c4243a-34ba-51e5-c32a-3859389a5162 externalId=56633 proto=6 act=close cs5=10 cs5Label=Policy Id FTNTFGTdstcountry=Reserved FTNTFGTsrccountry=Reserved FTNTFGTtrandisp=snat sourceTranslatedAddress=1.1.1.1 sourceTranslatedPort=45719 app=HTTP FTNTFGTappid=38783 FTNTFGTapp=Wget.Like FTNTFGTappcat=General.Interest FTNTFGTapprisk=low FTNTFGTapplist=default FTNTFGTappact=detected cn1=7 cn1Label=Duration out=398 in=1605 cn2=5 cn2Label=Packets Sent cn3=5 cn3Label=Packets Received FTNTFGTutmaction=block FTNTFGTcountav=1 FTNTFGTcountapp=1 FTNTFGTcrscore=50 FTNTFGTcraction=2",
        "source": {
            "nat": {
                "ip": "1.1.1.1",
                "port": 45719
            },
            "ip": "2.2.2.2",
            "address": "2.2.2.2",
            "port": 45719,
            "bytes": 1605,
            "packets": 5
        },
        "destination": {
            "address": "3.3.3.3",
            "ip": "3.3.3.3",
            "port": 80,
            "bytes": 398,
            "packets": 5
        },
        "network": {
            "transport": "tcp",
            "application": "HTTP"
        },
        "observer": {
            "type": "Fortigate",
            "vendor": "Fortinet",
            "version": "v5.6.0"
        },
        "action": {
            "name": "close",
            "outcome": "success",
            "type": "forward"
        },
        "log": {
            "level": "notice"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2",
                "3.3.3.3"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "traffic_forward.CSV.json"

    ```json
	
    {
        "event": {
            "code": "0000000013",
            "outcome": "success",
            "dialect": "fortigate",
            "category": "traffic",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "notice"
        },
        "message": "date=2018-07-26,time=16:51:36,logid=\"0000000013\",type=\"traffic\",subtype=\"forward\",level=\"notice\",vd=\"root\",eventtime=1532616695,srcip=1.1.1.1,srcport=10016,srcintf=\"test\",srcintfrole=\"undefined\",dstip=2.2.2.2,dstport=20,dstintf=\"dmz1\",dstintfrole=\"dmz\",sessionid=10006,proto=6,action=\"accept\",policyid=1,policytype=\"policy\",service=\"tcp/20\",dstcountry=\"France\",srccountry=\"United States\",trandisp=\"noop\",appid=35421,app=\"application\",appcat=\"Storage.Backup\",apprisk=\"medium\",applist=\"default\",duration=10,sentbyte=2000,rcvdbyte=1000,sentpkt=0,rcvdpkt=0,utmaction=\"allow\",countapp=1,devtype=\"iPad\",osname=\"Apple\",osversion=\"ver\",mastersrcmac=\"01:01:01:01:01:01\",srcmac=\"01:01:01:01:01:01\",srcserver=0,dstdevtype=\"Android Phone\",dstosname=\"Android\",dstosversion=\"ver\",masterdstmac=\"00:00:00:00:00:00\",dstmac=\"00:00:00:00:00:00\",dstserver=0,utmref=65491-194",
        "source": {
            "ip": "1.1.1.1",
            "address": "1.1.1.1",
            "port": 10016,
            "bytes": 2000,
            "packets": 0,
            "mac": "01:01:01:01:01:01"
        },
        "destination": {
            "address": "2.2.2.2",
            "ip": "2.2.2.2",
            "port": 20,
            "bytes": 1000,
            "packets": 0,
            "mac": "00:00:00:00:00:00"
        },
        "network": {
            "application": "application",
            "protocol": "tcp/20",
            "transport": "tcp"
        },
        "action": {
            "name": "accept",
            "outcome": "success",
            "type": "forward"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "dmz1"
                }
            },
            "ingress": {
                "interface": {
                    "name": "test"
                }
            }
        },
        "fortinet": {
            "apprisk": "medium"
        },
        "rule": {
            "category": "Storage.Backup",
            "ruleset": "default"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "traffic_forward.STANDARD.json"

    ```json
	
    {
        "event": {
            "code": "0000000013",
            "outcome": "success",
            "dialect": "fortigate",
            "category": "traffic",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "message": "date=2018-07-26 time=16:51:36 logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" eventtime=1532616695 srcip=1.1.1.1 srcport=10016 srcintf=\"test\" srcintfrole=\"undefined\" dstip=2.2.2.2 dstport=20 dstintf=\"test1\" dstintfrole=\"dmz\" sessionid=10006 proto=6 action=\"accept\" policyid=1 policytype=\"policy\" service=\"tcp/20\" dstcountry=\"France\" srccountry=\"United States\" trandisp=\"noop\" appid=35421 app=\"Dropbox_File.Download\" appcat=\"Storage.Backup\" apprisk=\"medium\" applist=\"default\" duration=10 sentbyte=2000 rcvdbyte=1000 sentpkt=0 rcvdpkt=0 utmaction=\"allow\" countapp=1 devtype=\"iPad\" osname=\"Apple\" osversion=\"ver\" mastersrcmac=\"01:01:01:01:01:01\" srcmac=\"01:01:01:01:01:01\" srcserver=0 dstdevtype=\"Android Phone\" dstosname=\"Android\" dstosversion=\"ver\" masterdstmac=\"00:00:00:00:00:00\" dstmac=\"00:00:00:00:00:00\" dstserver=0 utmref=65491-194",
        "source": {
            "ip": "1.1.1.1",
            "address": "1.1.1.1",
            "port": 10016,
            "bytes": 2000,
            "packets": 0,
            "mac": "01:01:01:01:01:01"
        },
        "destination": {
            "ip": "2.2.2.2",
            "address": "2.2.2.2",
            "port": 20,
            "bytes": 1000,
            "packets": 0,
            "mac": "00:00:00:00:00:00"
        },
        "network": {
            "protocol": "tcp/20",
            "transport": "tcp",
            "application": "Dropbox_File.Download"
        },
        "action": {
            "name": "accept",
            "outcome": "success",
            "type": "forward"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "test1"
                }
            },
            "ingress": {
                "interface": {
                    "name": "test"
                }
            }
        },
        "fortinet": {
            "apprisk": "medium"
        },
        "rule": {
            "category": "Storage.Backup",
            "ruleset": "default"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "log": {
            "level": "notice"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "traffic_forward.STANDARD_STET.json"

    ```json
	
    {
        "event": {
            "code": "0000000010",
            "outcome": "success",
            "dialect": "fortigate",
            "category": "traffic",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "notice"
        },
        "message": "date=2021-06-21  time=09:38:29 devname=\"abc\" devid=\"1\" logid=\"0000000010\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"PRX1-AA\" eventtime=1624261109 srcip=1.1.1.1 srcport=50592 srcintf=\"port2\" srcintfrole=\"dmz\" dstip=2.2.2.2 dstport=443 dstintf=\"test\" dstintfrole=\"wan\" sessionid=1224900441 poluuid=\"1eb429d4-ff52-51ea-d119-d1db60e409a6\" dstcountry=\"United Kingdom\" srccountry=\"Reserved\" service=\"HTTPS\" wanoptapptype=\"web-proxy\" proto=6 action=\"accept\" duration=37 policyid=1 policytype=\"proxy-policy\" wanin=5851 rcvdbyte=5851 wanout=2523 lanin=2769 sentbyte=2769 lanout=5923 appcat=\"unscanned\" utmaction=\"allow\" countweb=1",
        "source": {
            "ip": "1.1.1.1",
            "address": "1.1.1.1",
            "port": 50592,
            "bytes": 2769
        },
        "destination": {
            "ip": "2.2.2.2",
            "address": "2.2.2.2",
            "port": 443,
            "bytes": 5851
        },
        "network": {
            "protocol": "HTTPS",
            "transport": "tcp"
        },
        "action": {
            "name": "accept",
            "outcome": "success",
            "type": "forward"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "test"
                }
            },
            "ingress": {
                "interface": {
                    "name": "port2"
                }
            }
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ]
        },
        "rule": {
            "category": "unscanned",
            "ruleset": "proxy-policy"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "traffic_nat.STANDARD.json"

    ```json
	
    {
        "action": {
            "name": "server-rst",
            "outcome": "success",
            "type": "forward"
        },
        "destination": {
            "address": "3.3.3.3",
            "bytes": 40,
            "ip": "3.3.3.3",
            "mac": "00:00:00:00:00:00",
            "nat": {
                "ip": "2.2.2.2"
            },
            "packets": 1,
            "port": 3727
        },
        "event": {
            "code": "0000000013",
            "outcome": "success",
            "dialect": "fortigate",
            "category": "traffic",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "notice"
        },
        "message": "date=2018-07-26 time=14:56:21 devname=\"abc\" devid=\"1\" logid=\"0000000013\" type=\"traffic\" subtype=\"forward\" level=\"notice\" vd=\"root\" eventtime=1609941381 srcip=1.1.1.1 srcport=52125 srcintf=\"port9\" srcintfrole=\"undefined\" dstip=3.3.3.3 dstport=3727 dstintf=\"port10\" dstintfrole=\"undefined\" poluuid=\"d77c53b2-a3c6-51e9-49b2-61c9e68c1f7e\" sessionid=578033623 proto=6 action=\"server-rst\" policyid=207 policytype=\"policy\" service=\"tcp/3727\" dstcountry=\"France\" srccountry=\"Netherlands\" trandisp=\"dnat\" tranip=2.2.2.2 tranport=3727 duration=5 sentbyte=80 rcvdbyte=40 sentpkt=2 rcvdpkt=1 appcat=\"unscanned\" dstdevtype=\"Router/NAT Device\" dstdevcategory=\"Windows Device\" masterdstmac=\"00:00:00:00:00:00\" dstmac=\"00:00:00:00:00:00\" dstserver=1",
        "source": {
            "address": "1.1.1.1",
            "bytes": 80,
            "ip": "1.1.1.1",
            "packets": 2,
            "port": 52125
        },
        "network": {
            "protocol": "tcp/3727",
            "transport": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "name": "port10"
                }
            },
            "ingress": {
                "interface": {
                    "name": "port9"
                }
            }
        },
        "rule": {
            "category": "unscanned",
            "ruleset": "policy"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2",
                "3.3.3.3"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "tunnel.json"

    ```json
	
    {
        "event": {
            "code": "0101039949",
            "outcome": "success",
            "dialect": "fortigate",
            "reason": "SSL tunnel statistics",
            "category": "event",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "information"
        },
        "message": "logver=60 timestamp=1566916060 tz=\"UTC+2\" devname=\"abc\" devid=\"1\" vd=\"IPSEC\" date=2019-08-27 time=16:27:40 logid=\"0101039949\" type=\"event\" subtype=\"vpn\" level=\"information\" eventtime=1566916060 logdesc=\"SSL VPN statistics\" action=\"tunnel-stats\" tunneltype=\"ssl-tunnel\" tunnelid=1995 remip=1.1.1.1 tunnelip=2.2.2.2 user=\"test\" group=\"GRP_Generic_JAIL_VPN\" dst_host=\"N/A\" nextstat=600 duration=8437 sentbyte=71524041 rcvdbyte=6151809 msg=\"SSL tunnel statistics\"\n",
        "source": {
            "bytes": 71524041,
            "ip": "1.1.1.1",
            "address": "1.1.1.1",
            "nat": {
                "ip": "2.2.2.2"
            },
            "user": {
                "name": "test"
            }
        },
        "destination": {
            "bytes": 6151809
        },
        "action": {
            "name": "tunnel-stats",
            "outcome": "success",
            "type": "vpn"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2.2.2.2"
            ],
            "user": [
                "test"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "tunnel_statistics.CSV.json"

    ```json
	
    {
        "event": {
            "code": "0101037141",
            "outcome": "success",
            "dialect": "fortigate",
            "reason": "IPsec tunnel statistics",
            "category": "event",
            "created": "2021-04-23T20:02:05.017771Z",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
            "kind": "event"
        },
        "log": {
            "level": "notice"
        },
        "message": " time=12:02:57 devname=\"abc\" devid=\"1\" logid=\"0101037141\" type=\"event\" subtype=\"vpn\" level=\"notice\" vd=\"root\" eventtime=1614855777 logdesc=\"IPsec tunnel statistics\" msg=\"IPsec tunnel statistics\" action=\"tunnel-stats\" remip=1.1.1.1 locip=93.187.43.9 remport=500 locport=500 outintf=\"N/A\" cookies=\"9b064274e0648c03/662c2b1264a2295e\" user=\"N/A\" group=\"N/A\" xauthuser=\"N/A\" xauthgroup=\"N/A\" assignip=N/A vpntunnel=\"VPN-HELPLINE\" tunnelip=N/A tunnelid=0 tunneltype=\"ipsec\" duration=102908570 sentbyte=7649 rcvdbyte=0 nextstat=600",
        "source": {
            "bytes": 7649,
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "nat": {
                "ip": "N/A"
            },
            "user": {
                "name": "N/A"
            }
        },
        "destination": {
            "bytes": 0
        },
        "action": {
            "name": "tunnel-stats",
            "outcome": "success",
            "type": "vpn"
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "N/A"
            ],
            "user": [
                "N/A"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "vpn.STANDARD.json"

    ```json
	
    {
        "action": {
            "name": "CRL_1",
            "outcome": "success",
            "type": "vpn"
        },
        "event": {
            "category": "event",
            "code": "0101041987",
            "created": "2021-03-11T15:53:56.988590Z",
            "dialect": "fortigate",
            "dialect_uuid": "418b5714-cddd-4ac3-8eea-d4aa7d37f99d",
            "id": "b0f4e7f4-c807-4656-8ce4-ce6d254146ba",
            "reason": "A certificate is updated",
            "original": "Xxzvh5M2kuKGZtZnGQCn2YSy7Jx6Qng3Bo97HaKNydZTDl5Wub0okUtb4ww7Y0jA",
            "outcome": "success",
            "action": "N/A",
            "kind": "event"
        },
        "http": {
            "request": {
                "method": "HTTP"
            }
        },
        "log": {
            "level": "information"
        },
        "message": " time=14:38:46 devname=\"abc\" devid=\"1\" logid=\"0101041987\" type=\"event\" subtype=\"vpn\" level=\"information\" vd=\"root\" eventtime=1615469926 logdesc=\"Certificate updated\" action=\"info\" cert-type=\"CRL\" status=\"success\" name=\"CRL_1\" method=\"HTTP\" reason=\"N/A\" msg=\"A certificate is updated\"",
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`destination.address` | `keyword` | Destination network address. |
|`destination.bytes` | `long` | Bytes sent from the destination to the source. |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.mac` | `keyword` | MAC address of the destination. |
|`destination.nat.ip` | `ip` | Destination NAT ip |
|`destination.nat.port` | `long` | Destination NAT Port |
|`destination.packets` | `long` | Packets sent from the destination to the source. |
|`destination.port` | `long` | Port of the destination. |
|`dns.question.name` | `keyword` | The name being queried. |
|`dns.question.type` | `keyword` | The type of record being queried. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.severity` | `long` | Numeric severity of the event. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`fortinet.apprisk` | `keyword` | Risk level of the application. |
|`fortinet.event.desc` | `keyword` | Type of log. |
|`http.request.method` | `keyword` | HTTP request method. |
|`icmp.request.code` | `keyword` | The request code. |
|`icmp.request.type` | `keyword` | The request type. |
|`log.level` | `keyword` | Log level of the log event. |
|`network.application` | `keyword` | Application level protocol name. |
|`network.protocol` | `keyword` | Application protocol name. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`observer.egress.interface.name` | `keyword` | Interface name |
|`observer.ingress.interface.name` | `keyword` | Interface name |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`observer.version` | `keyword` | Observer version. |
|`rule.category` | `keyword` | Rule category |
|`rule.ruleset` | `keyword` | Rule ruleset |
|`source.address` | `keyword` | Source network address. |
|`source.bytes` | `long` | Bytes sent from the source to the destination. |
|`source.ip` | `ip` | IP address of the source. |
|`source.mac` | `keyword` | MAC address of the source. |
|`source.nat.ip` | `ip` | Source NAT ip |
|`source.nat.port` | `long` | Source NAT port |
|`source.packets` | `long` | Packets sent from the source to the destination. |
|`source.port` | `long` | Port of the source. |
|`source.user.name` | `keyword` | Short name or login of the user. |
|`url.full` | `wildcard` | Full unparsed URL. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

