
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web proxy` | Imperva WAF logs provide information about the connected client and the requested resource |
| `Web logs` | Imperva WAF logs provide information about the connected client and the requested resource |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network` |
| Type | `["connection", "access"]`, `["connection", "allowed"]`, `["connection", "denied"]`, `["connection", "error"]` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "access.json"

    ```json
	
    {
        "message": "CEF:0|Incapsula|SIEMintegration|1|1|Normal|0| sourceServiceName=site123.abcd.info siteid=1509732 suid=50005477 requestClientApplication=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0 deviceFacility=mia ccode=IL tag=www.elvis.com cicode=Rehovot cs7=31.8969 cs7Label=latitude cs8=34.8186 cs8Label=longitude Customer=CEFcustomer123 siteTag=my-site-tag start=123456789 request=site123.abcd.info/main.css ref=www.incapsula.com/lama requestmethod=GET cn1=200 app=HTTP deviceExternalID=33411452762204224 in=54 xff=44.44.44.44 cpt=443 src=12.12.12.12 ver=TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 end=223456789 additionalReqHeaders=[{\"Accept\":\"*/*\"},{\"x-v\":\"1\"},{\"x-fapi-interaction-id\":\"10.10.10.10\"}] additionalResHeaders=[{\"Content-Type\":\"text/html; charset\\=UTF-8\"}]",
        "event": {
            "start": "2009-02-13T23:31:30.000000Z",
            "end": "2040-10-23T01:18:10.000000Z",
            "duration": 100000000.0,
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "connection",
                "access"
            ],
            "dataset": "imperva-waf",
            "module": "imperva.waf"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "device": {
                "name": "Other"
            },
            "name": "Firefox",
            "version": "40.0"
        },
        "client": {
            "geo": {
                "country_iso_code": "IL",
                "city_name": "Rehovot",
                "location": {
                    "lat": 31.8969,
                    "lon": 34.8186
                }
            }
        },
        "url": {
            "full": "site123.abcd.info/main.css",
            "original": "site123.abcd.info/main.css",
            "path": "site123.abcd.info/main.css"
        },
        "http": {
            "request": {
                "referrer": "www.incapsula.com/lama",
                "method": "GET",
                "bytes": 54,
                "id": "33411452762204224"
            },
            "response": {
                "status_code": 200
            }
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 443,
            "ip": "12.12.12.12",
            "address": "12.12.12.12"
        },
        "@timestamp": "2009-02-13T23:31:30.000000Z",
        "observer": {
            "vendor": "Imperva",
            "type": "firewall",
            "product": "Web Application Firewall"
        },
        "tls": {
            "version": "1.2",
            "version_protocol": "tls",
            "cipher": "ECDHE-RSA-AES128-GCM-SHA256"
        },
        "imperva": {
            "pop": "mia",
            "request": {
                "headers": [
                    {
                        "Accept": "*/*"
                    },
                    {
                        "x-v": "1"
                    },
                    {
                        "x-fapi-interaction-id": "10.10.10.10"
                    }
                ],
                "x_forwarded_for": "44.44.44.44"
            },
            "response": {
                "headers": [
                    {
                        "Content-Type": "text/html; charset\\=UTF-8"
                    }
                ]
            }
        },
        "related": {
            "ip": [
                "12.12.12.12"
            ]
        },
        "os": {
            "name": "Windows",
            "version": "7"
        }
    }
    	
	```


=== "access_security_bad.json"

    ```json
	
    {
        "message": "CEF:0|Incapsula|SIEMintegration|1|1|Blocked country|-1| fileId=393000630126853202 sourceServiceName=www.test.com siteid=38097258 suid=1928034 requestClientApplication=Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0 deviceFacility=cdg cs2=true cs2Label=Javascript Support cs3=true cs3Label=CO Support cs1=NA cs1Label=Cap Support cs4=a99e6166-5092-4cce-8fb6-afae61ef7493 cs4Label=VID cs5=438c978a6198632a5439b8bce551a3bc5e29598526d64adcd1c8a12e289a7edd09b13fde8d8fb77e7dfff3e3d29526a3b01fcc9ec47ce2cedf1ab6630a8eab5ffc328c910a566d653fc81ae43248023b662d6a84849da3688453b98caa60947a cs5Label=clappsig dproc=Browser cs6=Webkit Browser cs6Label=clapp ccode=FR cicode=Strasbourg cs7=48.34 cs7Label=latitude cs8=7.4508 cs8Label=longitude Customer=mycustomer@example.org start=1649772598763 request=www.test.com/ requestMethod=GET app=HTTP act=REQ_BAD_PARSE_ERROR deviceExternalId=195557299895996363 cpt=45208 src=1.2.3.4 end=1649772598765",
        "event": {
            "action": "REQ_BAD_PARSE_ERROR",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "connection",
                "error"
            ],
            "dataset": "imperva-waf",
            "module": "imperva.waf",
            "reason": "The HTTP request was malformated"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Firefox",
            "device": {
                "name": "Other"
            },
            "version": "99.0"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/",
            "path": "www.test.com/"
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z",
        "observer": {
            "vendor": "Imperva",
            "type": "firewall",
            "product": "Web Application Firewall"
        },
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        },
        "os": {
            "name": "Linux"
        }
    }
    	
	```


=== "access_security_blacklisted.json"

    ```json
	
    {
        "message": "CEF:0|Incapsula|SIEMintegration|1|1|Blocked country|-1| fileId=393000630126853202 sourceServiceName=www.test.com siteid=38097258 suid=1928034 requestClientApplication=Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0 deviceFacility=cdg cs2=true cs2Label=Javascript Support cs3=true cs3Label=CO Support cs1=NA cs1Label=Cap Support cs4=a99e6166-5092-4cce-8fb6-afae61ef7493 cs4Label=VID cs5=438c978a6198632a5439b8bce551a3bc5e29598526d64adcd1c8a12e289a7edd09b13fde8d8fb77e7dfff3e3d29526a3b01fcc9ec47ce2cedf1ab6630a8eab5ffc328c910a566d653fc81ae43248023b662d6a84849da3688453b98caa60947a cs5Label=clappsig dproc=Browser cs6=Webkit Browser cs6Label=clapp ccode=FR cicode=Strasbourg cs7=48.34 cs7Label=latitude cs8=7.4508 cs8Label=longitude Customer=mycustomer@example.org start=1649772598763 request=www.test.com/ requestMethod=GET app=HTTP act=REQ_DOMAIN_BLACKLISTED deviceExternalId=195557299895996363 cpt=45208 src=1.2.3.4 end=1649772598765",
        "event": {
            "action": "REQ_DOMAIN_BLACKLISTED",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "connection",
                "denied"
            ],
            "dataset": "imperva-waf",
            "module": "imperva.waf",
            "reason": "The destination was blacklisted"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Firefox",
            "device": {
                "name": "Other"
            },
            "version": "99.0"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/",
            "path": "www.test.com/"
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z",
        "observer": {
            "vendor": "Imperva",
            "type": "firewall",
            "product": "Web Application Firewall"
        },
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        },
        "os": {
            "name": "Linux"
        }
    }
    	
	```


=== "access_security_blocked.json"

    ```json
	
    {
        "message": "CEF:0|Incapsula|SIEMintegration|1|1|Blocked country|-1| fileId=393000630126853202 sourceServiceName=www.test.com siteid=38097258 suid=1928034 requestClientApplication=Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0 deviceFacility=cdg cs2=true cs2Label=Javascript Support cs3=true cs3Label=CO Support cs1=NA cs1Label=Cap Support cs4=a99e6166-5092-4cce-8fb6-afae61ef7493 cs4Label=VID cs5=438c978a6198632a5439b8bce551a3bc5e29598526d64adcd1c8a12e289a7edd09b13fde8d8fb77e7dfff3e3d29526a3b01fcc9ec47ce2cedf1ab6630a8eab5ffc328c910a566d653fc81ae43248023b662d6a84849da3688453b98caa60947a cs5Label=clappsig dproc=Browser cs6=Webkit Browser cs6Label=clapp ccode=FR cicode=Strasbourg cs7=48.34 cs7Label=latitude cs8=7.4508 cs8Label=longitude Customer=mycustomer@example.org start=1649772598763 request=www.test.com/ requestMethod=GET app=HTTP act=REQ_BLOCKED_VISITOR deviceExternalId=195557299895996363 cpt=45208 src=1.2.3.4 end=1649772598765",
        "event": {
            "action": "REQ_BLOCKED_VISITOR",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "connection",
                "denied"
            ],
            "dataset": "imperva-waf",
            "module": "imperva.waf",
            "reason": "The request was blocked based on WAF settings"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Firefox",
            "device": {
                "name": "Other"
            },
            "version": "99.0"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/",
            "path": "www.test.com/"
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z",
        "observer": {
            "vendor": "Imperva",
            "type": "firewall",
            "product": "Web Application Firewall"
        },
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        },
        "os": {
            "name": "Linux"
        }
    }
    	
	```


=== "access_security_cached.json"

    ```json
	
    {
        "message": "CEF:0|Incapsula|SIEMintegration|1|1|Accepted country|-1| fileId=393000630126853202 sourceServiceName=www.test.com siteid=38097258 suid=1928034 requestClientApplication=Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0 deviceFacility=cdg cs2=true cs2Label=Javascript Support cs3=true cs3Label=CO Support cs1=NA cs1Label=Cap Support cs4=a99e6166-5092-4cce-8fb6-afae61ef7493 cs4Label=VID cs5=438c978a6198632a5439b8bce551a3bc5e29598526d64adcd1c8a12e289a7edd09b13fde8d8fb77e7dfff3e3d29526a3b01fcc9ec47ce2cedf1ab6630a8eab5ffc328c910a566d653fc81ae43248023b662d6a84849da3688453b98caa60947a cs5Label=clappsig dproc=Browser cs6=Webkit Browser cs6Label=clapp ccode=FR cicode=Strasbourg cs7=48.34 cs7Label=latitude cs8=7.4508 cs8Label=longitude Customer=mycustomer@example.org start=1649772598763 request=www.test.com/ requestMethod=GET app=HTTP act=REQ_CACHED_WEBSITE deviceExternalId=195557299895996363 cpt=45208 src=1.2.3.4 end=1649772598765",
        "event": {
            "action": "REQ_CACHED_WEBSITE",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "connection",
                "allowed"
            ],
            "dataset": "imperva-waf",
            "module": "imperva.waf"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Firefox",
            "device": {
                "name": "Other"
            },
            "version": "99.0"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/",
            "path": "www.test.com/"
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z",
        "observer": {
            "vendor": "Imperva",
            "type": "firewall",
            "product": "Web Application Firewall"
        },
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        },
        "os": {
            "name": "Linux"
        }
    }
    	
	```


=== "access_security_challenged.json"

    ```json
	
    {
        "message": "CEF:0|Incapsula|SIEMintegration|1|1|Illegal Resource Access|3| fileid=3412341160002518171 sourceServiceName=site123.abcd.info siteid=1509732 suid=50005477 requestClientApplication=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0 deviceFacility=mia cs2=true cs2Label=Javascript Support cs3=true cs3Label=CO Support ccode=IL tag=www.elvis.com cn1=200 in=54 xff=44.44.44.44 cs1=NOT_SUPPORTED cs1Label=Cap Support cs4=c2e72124-0e8a-4dd8-b13b-3da246af3ab2 cs4Label=VID cs5=de3c633ac428e0678f3aac20cf7f239431e54cbb8a17e8302f53653923305e1835a9cd871db32aa4fc7b8a9463366cc4 cs5Label=clappsig dproc=Browser cs6=Firefox cs6Label=clapp ccode=IL cicode=Rehovot cs7=31.8969 cs7Label=latitude cs8=34.8186 cs8Label=longitude Customer=CEFcustomer123 siteTag=my-site-tag start=123456789 request=site123.abcd.info/ requestMethod=GET qstr=p\\=%2fetc%2fpasswd app=HTTP act=REQ_CHALLENGED_CAPTCHA deviceExternalId=33411452762204224 cpt=443 src=12.12.12.12 ver=TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 end=223456789 additionalReqHeaders=[{\"Accept\":\"*/*\"},{\"x-v\":\"1\"},{\"x-fapi-interaction-id\":\"10.10.10.10\"}] additionalResHeaders=[{\"Content-Type\":\"text/html; charset\\=UTF-8\"}] filetype=30037,1001, filepermission=2,1, cs9=Block Malicious User,High Risk Resources, cs9Label=Rule name cs11=,,[{\"api_specification_violation_type\":\"INVALID_PARAM_NAME\",\"parameter_name\":\"somename\"}] cs11Label=Rule Additional Info",
        "event": {
            "action": "REQ_CHALLENGED_CAPTCHA",
            "start": "2009-02-13T23:31:30.000000Z",
            "end": "2040-10-23T01:18:10.000000Z",
            "duration": 100000000.0,
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "connection",
                "denied"
            ],
            "dataset": "imperva-waf",
            "module": "imperva.waf",
            "reason": "A challenge was submitted to the client"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "name": "Firefox",
            "device": {
                "name": "Other"
            },
            "version": "40.0"
        },
        "client": {
            "geo": {
                "country_iso_code": "IL",
                "city_name": "Rehovot",
                "location": {
                    "lat": 31.8969,
                    "lon": 34.8186
                }
            }
        },
        "url": {
            "full": "site123.abcd.info/",
            "original": "site123.abcd.info/",
            "query": "p\\=%2fetc%2fpasswd",
            "path": "site123.abcd.info/"
        },
        "http": {
            "request": {
                "method": "GET",
                "bytes": 54,
                "id": "33411452762204224"
            },
            "response": {
                "status_code": 200
            }
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 443,
            "ip": "12.12.12.12",
            "address": "12.12.12.12"
        },
        "rule": {
            "name": "Block Malicious User,High Risk Resources,"
        },
        "@timestamp": "2009-02-13T23:31:30.000000Z",
        "observer": {
            "vendor": "Imperva",
            "type": "firewall",
            "product": "Web Application Firewall"
        },
        "tls": {
            "version": "1.2",
            "version_protocol": "tls",
            "cipher": "ECDHE-RSA-AES128-GCM-SHA256"
        },
        "imperva": {
            "pop": "mia",
            "request": {
                "headers": [
                    {
                        "Accept": "*/*"
                    },
                    {
                        "x-v": "1"
                    },
                    {
                        "x-fapi-interaction-id": "10.10.10.10"
                    }
                ],
                "x_forwarded_for": "44.44.44.44"
            },
            "response": {
                "headers": [
                    {
                        "Content-Type": "text/html; charset\\=UTF-8"
                    }
                ]
            },
            "session": {
                "id": 3412341160002518171
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NOT_SUPPORTED"
            },
            "visitor": {
                "id": "c2e72124-0e8a-4dd8-b13b-3da246af3ab2"
            },
            "user_agent": {
                "type": "Browser"
            },
            "attack": {
                "type": "30037,1001,",
                "id": "2,1,"
            },
            "rule": {
                "additional_info": ",,[{\"api_specification_violation_type\":\"INVALID_PARAM_NAME\",\"parameter_name\":\"somename\"}]",
                "names": [
                    "Block Malicious User",
                    "High Risk Resources"
                ]
            }
        },
        "related": {
            "ip": [
                "12.12.12.12"
            ]
        },
        "os": {
            "name": "Windows",
            "version": "7"
        }
    }
    	
	```


=== "access_security_ipv6_not_supported.json"

    ```json
	
    {
        "message": "CEF:0|Incapsula|SIEMintegration|1|1|Accepted country|-1| fileId=393000630126853202 sourceServiceName=www.test.com siteid=38097258 suid=1928034 requestClientApplication=Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0 deviceFacility=cdg cs2=true cs2Label=Javascript Support cs3=true cs3Label=CO Support cs1=NA cs1Label=Cap Support cs4=a99e6166-5092-4cce-8fb6-afae61ef7493 cs4Label=VID cs5=438c978a6198632a5439b8bce551a3bc5e29598526d64adcd1c8a12e289a7edd09b13fde8d8fb77e7dfff3e3d29526a3b01fcc9ec47ce2cedf1ab6630a8eab5ffc328c910a566d653fc81ae43248023b662d6a84849da3688453b98caa60947a cs5Label=clappsig dproc=Browser cs6=Webkit Browser cs6Label=clapp ccode=FR cicode=Strasbourg cs7=48.34 cs7Label=latitude cs8=7.4508 cs8Label=longitude Customer=mycustomer@example.org start=1649772598763 request=www.test.com/ requestMethod=GET app=HTTP act=REQ_IPV6_NOT_SUPPORTED deviceExternalId=195557299895996363 cpt=45208 src=1.2.3.4 end=1649772598765",
        "event": {
            "action": "REQ_IPV6_NOT_SUPPORTED",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "connection",
                "error"
            ],
            "dataset": "imperva-waf",
            "module": "imperva.waf",
            "reason": "The destination doesn't support IPv6 addresses"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Firefox",
            "device": {
                "name": "Other"
            },
            "version": "99.0"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/",
            "path": "www.test.com/"
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z",
        "observer": {
            "vendor": "Imperva",
            "type": "firewall",
            "product": "Web Application Firewall"
        },
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        },
        "os": {
            "name": "Linux"
        }
    }
    	
	```


=== "access_security_passed.json"

    ```json
	
    {
        "message": "CEF:0|Incapsula|SIEMintegration|1|1|Accepted country|-1| fileId=393000630126853202 sourceServiceName=www.test.com siteid=38097258 suid=1928034 requestClientApplication=Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0 deviceFacility=cdg cs2=true cs2Label=Javascript Support cs3=true cs3Label=CO Support cs1=NA cs1Label=Cap Support cs4=a99e6166-5092-4cce-8fb6-afae61ef7493 cs4Label=VID cs5=438c978a6198632a5439b8bce551a3bc5e29598526d64adcd1c8a12e289a7edd09b13fde8d8fb77e7dfff3e3d29526a3b01fcc9ec47ce2cedf1ab6630a8eab5ffc328c910a566d653fc81ae43248023b662d6a84849da3688453b98caa60947a cs5Label=clappsig dproc=Browser cs6=Webkit Browser cs6Label=clapp ccode=FR cicode=Strasbourg cs7=48.34 cs7Label=latitude cs8=7.4508 cs8Label=longitude Customer=mycustomer@example.org start=1649772598763 request=www.test.com/ requestMethod=GET app=HTTP act=REQ_PASSED deviceExternalId=195557299895996363 cpt=45208 src=1.2.3.4 end=1649772598765",
        "event": {
            "action": "REQ_PASSED",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "connection",
                "allowed"
            ],
            "dataset": "imperva-waf",
            "module": "imperva.waf"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Firefox",
            "device": {
                "name": "Other"
            },
            "version": "99.0"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/",
            "path": "www.test.com/"
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z",
        "observer": {
            "vendor": "Imperva",
            "type": "firewall",
            "product": "Web Application Firewall"
        },
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        },
        "os": {
            "name": "Linux"
        }
    }
    	
	```


=== "access_security_unresolved.json"

    ```json
	
    {
        "message": "CEF:0|Incapsula|SIEMintegration|1|1|Blocked country|-1| fileId=393000630126853202 sourceServiceName=www.test.com siteid=38097258 suid=1928034 requestClientApplication=Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0 deviceFacility=cdg cs2=true cs2Label=Javascript Support cs3=true cs3Label=CO Support cs1=NA cs1Label=Cap Support cs4=a99e6166-5092-4cce-8fb6-afae61ef7493 cs4Label=VID cs5=438c978a6198632a5439b8bce551a3bc5e29598526d64adcd1c8a12e289a7edd09b13fde8d8fb77e7dfff3e3d29526a3b01fcc9ec47ce2cedf1ab6630a8eab5ffc328c910a566d653fc81ae43248023b662d6a84849da3688453b98caa60947a cs5Label=clappsig dproc=Browser cs6=Webkit Browser cs6Label=clapp ccode=FR cicode=Strasbourg cs7=48.34 cs7Label=latitude cs8=7.4508 cs8Label=longitude Customer=mycustomer@example.org start=1649772598763 request=www.test.com/ requestMethod=GET app=HTTP act=REQ_UNRESOLVED_SITE_INVALID_CNAME deviceExternalId=195557299895996363 cpt=45208 src=1.2.3.4 end=1649772598765",
        "event": {
            "action": "REQ_UNRESOLVED_SITE_INVALID_CNAME",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "connection",
                "error"
            ],
            "dataset": "imperva-waf",
            "module": "imperva.waf",
            "reason": "The proxy failed to resolve the destination"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Firefox",
            "device": {
                "name": "Other"
            },
            "version": "99.0"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/",
            "path": "www.test.com/"
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z",
        "observer": {
            "vendor": "Imperva",
            "type": "firewall",
            "product": "Web Application Firewall"
        },
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        },
        "os": {
            "name": "Linux"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`client.geo.city_name` | `keyword` | City name. |
|`client.geo.country_iso_code` | `keyword` | Country ISO code. |
|`client.geo.location` | `geo_point` | Longitude and latitude. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.duration` | `long` | Duration of the event in nanoseconds. |
|`event.end` | `date` | event.end contains the date when the event ended or when the activity was last observed. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.module` | `keyword` | Name of the module this data is coming from. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`http.request.bytes` | `long` | Total size in bytes of the request (body and headers). |
|`http.request.id` | `keyword` | HTTP request ID. |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`http.response.status_code` | `long` | HTTP response status code. |
|`imperva.attack.id` | `keyword` | Imperva attack id. |
|`imperva.attack.type` | `keyword` | The type of attack. |
|`imperva.client.captcha_support` | `keyword` | Whether or not the client application supports Captcha. |
|`imperva.client.cookie_support` | `boolean` | Whether or not the client application supports cookies. |
|`imperva.client.js_support` | `boolean` | Whether or not the client application supports JavaScript. |
|`imperva.pop` | `keyword` | The Imperva PoP that handled the request. |
|`imperva.request.headers` | `array` | Request headers in JSON format, with each field represented as a name-value pair. |
|`imperva.request.x_forwarded_for` | `text` | The X-Forwarded-For request header. |
|`imperva.response.headers` | `array` | Response headers in JSON format, with each field represented as a name-value pair. |
|`imperva.rule.additional_info` | `text` | Additional information on the violation that triggered the rule, in JSON format. Used for API Specification Violation events. |
|`imperva.rule.names` | `array` | The threat rule name that this request triggered. For example, SQL Injection or Blocked IP (ACL). |
|`imperva.session.id` | `long` | The unique identification. |
|`imperva.user_agent.type` | `keyword` | The browser type. |
|`imperva.visitor.id` | `keyword` | The ID of the visitor. |
|`network.protocol` | `keyword` | Application protocol name. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`rule.name` | `keyword` | Rule name |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`tls.cipher` | `keyword` | String indicating the cipher used during the current connection. |
|`tls.version` | `keyword` | Numeric part of the version parsed from the original string. |
|`tls.version_protocol` | `keyword` | Normalized lowercase protocol name parsed from original string. |
|`url.full` | `wildcard` | Full unparsed URL. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`url.query` | `keyword` | Query string of the request. |
|`user_agent.name` | `keyword` | Name of the user agent. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

