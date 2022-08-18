
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web logs` | Squid logs provide information about the connected client and the requested resource |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network`, `web` |
| Type | `connection`, `denied`, `error` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "connect.json"

    ```json
	
    {
        "message": "1564655684.277   3387 192.168.0.1 TCP_TUNNEL/200 19131 CONNECT example.org:443 - HIER_DIRECT/example.org -",
        "event": {
            "category": [
                "web",
                "network"
            ],
            "kind": "event",
            "duration": 3387,
            "start": "2019-08-01T10:34:44.277000Z"
        },
        "source": {
            "address": "192.168.0.1",
            "ip": "192.168.0.1"
        },
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
            "transport": "tcp",
            "direction": "egress"
        },
        "related": {
            "ip": [
                "192.168.0.1"
            ]
        },
        "squid": {
            "hierarchy_code": "HIER_DIRECT"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        }
    }
    	
	```


=== "connect2.json"

    ```json
	
    {
        "message": "1564576741.982   5756 192.168.0.1 TCP_TUNNEL/200 6295 CONNECT api42-api.example.com:443 - HIER_DIRECT/api42-api.example.com -",
        "event": {
            "category": [
                "web",
                "network"
            ],
            "kind": "event",
            "duration": 5756,
            "start": "2019-07-31T12:39:01.982000Z"
        },
        "source": {
            "address": "192.168.0.1",
            "ip": "192.168.0.1"
        },
        "destination": {
            "address": "api42-api.example.com",
            "domain": "api42-api.example.com",
            "port": 443,
            "registered_domain": "example.com",
            "top_level_domain": "com",
            "subdomain": "api42-api"
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
            "transport": "tcp",
            "direction": "egress"
        },
        "related": {
            "hosts": [
                "api42-api.example.com"
            ],
            "ip": [
                "192.168.0.1"
            ]
        },
        "squid": {
            "hierarchy_code": "HIER_DIRECT"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        }
    }
    	
	```


=== "connect3.json"

    ```json
	
    {
        "message": "1587042596.494   1717 192.168.224.39 TCP_TUNNEL/200 3512 CONNECT 193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.akamaihd.net:443 - HIER_DIRECT/193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.akamaihd.net -",
        "event": {
            "category": [
                "web",
                "network"
            ],
            "kind": "event",
            "duration": 1717,
            "start": "2020-04-16T13:09:56.494000Z"
        },
        "source": {
            "address": "192.168.224.39",
            "ip": "192.168.224.39"
        },
        "destination": {
            "address": "193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.akamaihd.net",
            "domain": "193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.akamaihd.net",
            "port": 443,
            "registered_domain": "akamaihd.net",
            "top_level_domain": "net",
            "subdomain": "193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s"
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
            "transport": "tcp",
            "direction": "egress"
        },
        "related": {
            "ip": [
                "192.168.224.39"
            ]
        },
        "squid": {
            "hierarchy_code": "HIER_DIRECT"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        }
    }
    	
	```


=== "connect_ip.json"

    ```json
	
    {
        "message": "1564655684.277   3387 192.168.0.1 TCP_TUNNEL/200 19131 CONNECT example.org:443 - HIER_DIRECT/example.org -",
        "event": {
            "category": [
                "web",
                "network"
            ],
            "kind": "event",
            "duration": 0,
            "start": "2022-01-20T08:23:57.129000Z",
            "type": [
                "connection",
                "denied",
                "error"
            ]
        },
        "source": {
            "address": "10.0.4.4",
            "ip": "10.0.4.4"
        },
        "destination": {
            "address": "45.138.98.34",
            "ip": "45.138.98.34",
            "port": 80
        },
        "http": {
            "request": {
                "method": "CONNECT"
            },
            "response": {
                "bytes": 3868,
                "status_code": 403,
                "mime_type": "text/html"
            }
        },
        "network": {
            "transport": "tcp",
            "direction": "egress"
        },
        "related": {
            "ip": [
                "10.0.4.4"
            ]
        },
        "squid": {
            "hierarchy_code": "HIER_NONE",
            "cache_status": "denied"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        }
    }
    	
	```


=== "content_type.json"

    ```json
	
    {
        "message": "1565598801.353     24 10.16.12.86 TCP_MISS/200 394 GET http://dt.adsafeprotected.com/dt?anId=929475&asId=f0fc9c04-7168-68e3-32ca-6cc17dd2223a&tv={c:l4fyeI,pingTime:-1,time:7884,type:u,clog:[{piv:100,vs:i,r:,w:1,h:1,t:78},{piv:0,vs:o,r:l,t:5971}],ndt:6,es:0,sc:1,ha:1,gm:1,slTimes:{i:5971,o:1913,n:0,pp:0,pm:0},slEvents:[{sl:i,t:78,wc:0.0.1920.1040,ac:952.74.1.1,am:i,cc:952.74.1.1,piv:100,obst:0,th:0,reas:,bkn:{piv:[5898~100],as:[5898~1.1]}},{sl:o,t:5971,wc:0.0.1920.1040,ac:952.-516.1.1,am:i,cc:952.-516.1.1,piv:0,obst:0,th:0,reas:l,bkn:{piv:[1914~0],as:[1914~1.1]}}],slEventCount:2,em:true,fr:true,e:,tt:jload,dtt:254,metricIdList:[publ1,grpm1],fm:ryV6ZcU+11|12|13|14*.929475|141|15.929475|151|152|16,idMap:14.c4c75fac-ccbe-9ba7-61b1-d1276709f9ec.31_289523-36779676|14*,rend:0,renddet:WINDOW,rmeas:0,lt:1}&br=c - HIER_DIRECT/dt.adsafeprotected.com image/gif",
        "event": {
            "category": [
                "web",
                "network"
            ],
            "kind": "event",
            "start": "2019-08-12T08:33:21.353000Z",
            "duration": 24
        },
        "source": {
            "address": "10.16.12.86",
            "ip": "10.16.12.86"
        },
        "destination": {
            "address": "dt.adsafeprotected.com",
            "domain": "dt.adsafeprotected.com",
            "registered_domain": "adsafeprotected.com",
            "top_level_domain": "com",
            "subdomain": "dt"
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
            "transport": "tcp",
            "direction": "egress"
        },
        "url": {
            "domain": "dt.adsafeprotected.com",
            "original": "http://dt.adsafeprotected.com/dt?anId=929475&asId=f0fc9c04-7168-68e3-32ca-6cc17dd2223a&tv={c:l4fyeI,pingTime:-1,time:7884,type:u,clog:[{piv:100,vs:i,r:,w:1,h:1,t:78},{piv:0,vs:o,r:l,t:5971}],ndt:6,es:0,sc:1,ha:1,gm:1,slTimes:{i:5971,o:1913,n:0,pp:0,pm:0},slEvents:[{sl:i,t:78,wc:0.0.1920.1040,ac:952.74.1.1,am:i,cc:952.74.1.1,piv:100,obst:0,th:0,reas:,bkn:{piv:[5898~100],as:[5898~1.1]}},{sl:o,t:5971,wc:0.0.1920.1040,ac:952.-516.1.1,am:i,cc:952.-516.1.1,piv:0,obst:0,th:0,reas:l,bkn:{piv:[1914~0],as:[1914~1.1]}}],slEventCount:2,em:true,fr:true,e:,tt:jload,dtt:254,metricIdList:[publ1,grpm1],fm:ryV6ZcU+11|12|13|14*.929475|141|15.929475|151|152|16,idMap:14.c4c75fac-ccbe-9ba7-61b1-d1276709f9ec.31_289523-36779676|14*,rend:0,renddet:WINDOW,rmeas:0,lt:1}&br=c",
            "full": "http://dt.adsafeprotected.com/dt?anId=929475&asId=f0fc9c04-7168-68e3-32ca-6cc17dd2223a&tv={c:l4fyeI,pingTime:-1,time:7884,type:u,clog:[{piv:100,vs:i,r:,w:1,h:1,t:78},{piv:0,vs:o,r:l,t:5971}],ndt:6,es:0,sc:1,ha:1,gm:1,slTimes:{i:5971,o:1913,n:0,pp:0,pm:0},slEvents:[{sl:i,t:78,wc:0.0.1920.1040,ac:952.74.1.1,am:i,cc:952.74.1.1,piv:100,obst:0,th:0,reas:,bkn:{piv:[5898~100],as:[5898~1.1]}},{sl:o,t:5971,wc:0.0.1920.1040,ac:952.-516.1.1,am:i,cc:952.-516.1.1,piv:0,obst:0,th:0,reas:l,bkn:{piv:[1914~0],as:[1914~1.1]}}],slEventCount:2,em:true,fr:true,e:,tt:jload,dtt:254,metricIdList:[publ1,grpm1],fm:ryV6ZcU+11|12|13|14*.929475|141|15.929475|151|152|16,idMap:14.c4c75fac-ccbe-9ba7-61b1-d1276709f9ec.31_289523-36779676|14*,rend:0,renddet:WINDOW,rmeas:0,lt:1}&br=c",
            "path": "/dt",
            "query": "anId=929475&asId=f0fc9c04-7168-68e3-32ca-6cc17dd2223a&tv={c:l4fyeI,pingTime:-1,time:7884,type:u,clog:[{piv:100,vs:i,r:,w:1,h:1,t:78},{piv:0,vs:o,r:l,t:5971}],ndt:6,es:0,sc:1,ha:1,gm:1,slTimes:{i:5971,o:1913,n:0,pp:0,pm:0},slEvents:[{sl:i,t:78,wc:0.0.1920.1040,ac:952.74.1.1,am:i,cc:952.74.1.1,piv:100,obst:0,th:0,reas:,bkn:{piv:[5898~100],as:[5898~1.1]}},{sl:o,t:5971,wc:0.0.1920.1040,ac:952.-516.1.1,am:i,cc:952.-516.1.1,piv:0,obst:0,th:0,reas:l,bkn:{piv:[1914~0],as:[1914~1.1]}}],slEventCount:2,em:true,fr:true,e:,tt:jload,dtt:254,metricIdList:[publ1,grpm1],fm:ryV6ZcU+11|12|13|14*.929475|141|15.929475|151|152|16,idMap:14.c4c75fac-ccbe-9ba7-61b1-d1276709f9ec.31_289523-36779676|14*,rend:0,renddet:WINDOW,rmeas:0,lt:1}&br=c",
            "scheme": "http"
        },
        "squid": {
            "cache_status": "miss",
            "hierarchy_code": "HIER_DIRECT"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "ip": [
                "10.16.12.86"
            ]
        }
    }
    	
	```


=== "get.json"

    ```json
	
    {
        "message": "1564670112.892   5007 192.168.95.17 TCP_HIT_ABORTED/000 0 GET http://smex10-2-en.url.trendmicro.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA== - HIER_DIRECT/smex10-2-en.url.trendmicro.com -",
        "event": {
            "category": [
                "web",
                "network"
            ],
            "kind": "event",
            "duration": 5007,
            "start": "2019-08-01T14:35:12.892000Z",
            "type": [
                "connection",
                "error"
            ]
        },
        "source": {
            "address": "192.168.95.17",
            "ip": "192.168.95.17"
        },
        "destination": {
            "address": "smex10-2-en.url.trendmicro.com",
            "domain": "smex10-2-en.url.trendmicro.com",
            "registered_domain": "trendmicro.com",
            "top_level_domain": "com",
            "subdomain": "smex10-2-en.url"
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
            "transport": "tcp",
            "direction": "egress"
        },
        "url": {
            "domain": "smex10-2-en.url.trendmicro.com",
            "full": "http://smex10-2-en.url.trendmicro.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "original": "http://smex10-2-en.url.trendmicro.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "path": "/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "scheme": "http"
        },
        "squid": {
            "cache_status": "hit",
            "hierarchy_code": "HIER_DIRECT"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "ip": [
                "192.168.95.17"
            ]
        }
    }
    	
	```


=== "get2.json"

    ```json
	
    {
        "message": "1565600128.411      0 192.168.0.1 TCP_DENIED/407 3980 GET http://api.example.org/api/v2/check - HIER_NONE/- text/html",
        "event": {
            "category": [
                "web",
                "network"
            ],
            "kind": "event",
            "type": [
                "connection",
                "denied",
                "error"
            ],
            "duration": 0,
            "start": "2019-08-12T08:55:28.411000Z"
        },
        "source": {
            "address": "192.168.0.1",
            "ip": "192.168.0.1"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "mime_type": "text/html",
                "status_code": 407,
                "bytes": 3980
            }
        },
        "network": {
            "transport": "tcp",
            "direction": "egress"
        },
        "url": {
            "domain": "api.example.org",
            "full": "http://api.example.org/api/v2/check",
            "original": "http://api.example.org/api/v2/check",
            "path": "/api/v2/check",
            "scheme": "http"
        },
        "squid": {
            "cache_status": "denied",
            "hierarchy_code": "HIER_NONE"
        },
        "related": {
            "ip": [
                "192.168.0.1"
            ]
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        }
    }
    	
	```


=== "get_dalid.json"

    ```json
	
    {
        "message": "1628084203.491     82 192.168.2.2 TCP_MISS/200 318399 GET http://download.windowsupdate.com/c/msdownload/update/others/2019/07/29477140_324519a81d0af914f765c56a1dc7141a5759ad4c.cab - HIER_DIRECT/13.107.4.50 application/vnd.ms-cab-compressed",
        "event": {
            "category": [
                "web",
                "network"
            ],
            "kind": "event",
            "duration": 82,
            "start": "2021-08-04T13:36:43.491000Z"
        },
        "destination": {
            "address": "13.107.4.50",
            "ip": "13.107.4.50"
        },
        "source": {
            "address": "192.168.2.2",
            "ip": "192.168.2.2"
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
            "transport": "tcp",
            "direction": "egress"
        },
        "url": {
            "domain": "download.windowsupdate.com",
            "full": "http://download.windowsupdate.com/c/msdownload/update/others/2019/07/29477140_324519a81d0af914f765c56a1dc7141a5759ad4c.cab",
            "original": "http://download.windowsupdate.com/c/msdownload/update/others/2019/07/29477140_324519a81d0af914f765c56a1dc7141a5759ad4c.cab",
            "path": "/c/msdownload/update/others/2019/07/29477140_324519a81d0af914f765c56a1dc7141a5759ad4c.cab",
            "scheme": "http"
        },
        "squid": {
            "cache_status": "miss",
            "hierarchy_code": "HIER_DIRECT"
        },
        "observer": {
            "product": "Squid",
            "type": "proxy",
            "vendor": "Squid"
        },
        "related": {
            "ip": [
                "13.107.4.50",
                "192.168.2.2"
            ]
        }
    }
    	
	```


=== "get_tcp_hit.json"

    ```json
	
    {
        "message": "1628150510.448    549 192.168.0.1 TCP_HIT/206 2055995 GET http://edgedl.me.gvt1.com/edgedl/release2/chrome_component/adbzvrjxj3ir3yvy5lknhgbxo6tq_92.267.200/gkmgaooipdjhmangpemjhigmamcehddo_92.267.200_win64_ac37t7snjqk4qthomil6kwgo54hq.crx3 - HIER_NONE/- application/octet-stream",
        "event": {
            "category": [
                "web",
                "network"
            ],
            "kind": "event",
            "duration": 549,
            "start": "2021-08-05T08:01:50.448000Z"
        },
        "source": {
            "address": "192.168.0.1",
            "ip": "192.168.0.1"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "bytes": 2055995,
                "status_code": 206,
                "mime_type": "application/octet-stream"
            }
        },
        "network": {
            "transport": "tcp",
            "direction": "egress"
        },
        "url": {
            "domain": "edgedl.me.gvt1.com",
            "full": "http://edgedl.me.gvt1.com/edgedl/release2/chrome_component/adbzvrjxj3ir3yvy5lknhgbxo6tq_92.267.200/gkmgaooipdjhmangpemjhigmamcehddo_92.267.200_win64_ac37t7snjqk4qthomil6kwgo54hq.crx3",
            "original": "http://edgedl.me.gvt1.com/edgedl/release2/chrome_component/adbzvrjxj3ir3yvy5lknhgbxo6tq_92.267.200/gkmgaooipdjhmangpemjhigmamcehddo_92.267.200_win64_ac37t7snjqk4qthomil6kwgo54hq.crx3",
            "path": "/edgedl/release2/chrome_component/adbzvrjxj3ir3yvy5lknhgbxo6tq_92.267.200/gkmgaooipdjhmangpemjhigmamcehddo_92.267.200_win64_ac37t7snjqk4qthomil6kwgo54hq.crx3",
            "scheme": "http"
        },
        "squid": {
            "cache_status": "hit",
            "hierarchy_code": "HIER_NONE"
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
        }
    }
    	
	```


=== "get_user_agent.json"

    ```json
	
    {
        "message": "1564670112.892   5007 192.168.95.17 TCP_HIT_ABORTED/000 0 GET http://smex10-2-en.url.trendmicro.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA== - HIER_DIRECT/smex10-2-en.url.trendmicro.com - \"http://www.example.org\" \"TMUFE\"",
        "source": {
            "address": "192.168.95.17",
            "ip": "192.168.95.17"
        },
        "squid": {
            "cache_status": "hit",
            "hierarchy_code": "HIER_DIRECT"
        },
        "url": {
            "domain": "smex10-2-en.url.trendmicro.com",
            "full": "http://smex10-2-en.url.trendmicro.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "original": "http://smex10-2-en.url.trendmicro.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "path": "/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA==",
            "scheme": "http"
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
                "smex10-2-en.url.trendmicro.com"
            ],
            "ip": [
                "192.168.95.17"
            ]
        },
        "destination": {
            "address": "smex10-2-en.url.trendmicro.com",
            "domain": "smex10-2-en.url.trendmicro.com",
            "registered_domain": "trendmicro.com",
            "top_level_domain": "com",
            "subdomain": "smex10-2-en.url"
        },
        "event": {
            "category": [
                "web",
                "network"
            ],
            "duration": 5007,
            "kind": "event",
            "outcome": "success",
            "start": "2019-08-01T14:35:12.892000Z",
            "type": [
                "connection",
                "error"
            ]
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
        "user_agent": {
            "original": "TMUFE"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.port` | `long` | Port of the destination. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.duration` | `long` | Duration of the event in nanoseconds. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
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
|`source.ip` | `ip` | IP address of the source. |
|`squid.cache_status` | `keyword` | Cache status for the request |
|`squid.hierarchy_code` | `keyword` | Hierarchy used by Squid for this connection. |
|`url.full` | `wildcard` | Full unparsed URL. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

