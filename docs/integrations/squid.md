uuid: a0dbb8f3-ca1c-4c6b-aafa-595bd430c0cb
name: Squid

# Squid

![Squid Logo](../assets/integrations/squid.png)

Squid is a caching proxy for the Web. It reduces bandwidth and improves response times by caching and reusing frequently-requested web pages. The analysis of Squid logs by SEKOIA.IO can detect web threats along as in-progress intrusion and exfiltration attempts.

## Event Categories

The following Table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web logs`       | Squid logs provide information about the connected client and the requested resource

In details, the following Table denotes the type of events produced by this integration.

| Name | Values |
| ---- | -------- |
| Kind | `Event` |
| Category | `Web`, `Network` |
| Type | `Connection`, `Denied`, `Error` |


## Event Samples

Find below few samples of Squid events and how they are normalized by SEKOIA.IO.

=== "connect.json"

    ```json
	"message": "1564655684.277   3387 192.168.0.1 TCP_TUNNEL/200 19131 CONNECT example.org:443 - HIER_DIRECT/example.org -",
    "event": {
      "category": [
        "web",
        "network"
      ],
      "kind": "event",
      "duration": 3387,
      "start": "2019-08-01T10:34:44.277000+00:00"
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
	```
	
===	"get_user_agent.json"

	``` json
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
      "start": "2019-08-01T14:35:12.892000+00:00",
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
	```
	
===	"content_type.json"

	``` json
	"message": "1565598801.353     24 10.16.12.86 TCP_MISS/200 394 GET http://dt.adsafeprotected.com/dt?anId=929475&asId=f0fc9c04-7168-68e3-32ca-6cc17dd2223a&tv={c:l4fyeI,pingTime:-1,time:7884,type:u,clog:[{piv:100,vs:i,r:,w:1,h:1,t:78},{piv:0,vs:o,r:l,t:5971}],ndt:6,es:0,sc:1,ha:1,gm:1,slTimes:{i:5971,o:1913,n:0,pp:0,pm:0},slEvents:[{sl:i,t:78,wc:0.0.1920.1040,ac:952.74.1.1,am:i,cc:952.74.1.1,piv:100,obst:0,th:0,reas:,bkn:{piv:[5898~100],as:[5898~1.1]}},{sl:o,t:5971,wc:0.0.1920.1040,ac:952.-516.1.1,am:i,cc:952.-516.1.1,piv:0,obst:0,th:0,reas:l,bkn:{piv:[1914~0],as:[1914~1.1]}}],slEventCount:2,em:true,fr:true,e:,tt:jload,dtt:254,metricIdList:[publ1,grpm1],fm:ryV6ZcU+11|12|13|14*.929475|141|15.929475|151|152|16,idMap:14.c4c75fac-ccbe-9ba7-61b1-d1276709f9ec.31_289523-36779676|14*,rend:0,renddet:WINDOW,rmeas:0,lt:1}&br=c - HIER_DIRECT/dt.adsafeprotected.com image/gif",
    "event": {
      "category": [
        "web",
        "network"
      ],
      "kind": "event",
      "start": "2019-08-12T08:33:21.353000+00:00",
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
	
	```


## Configure

As of now, the main solution to collect Squid logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

In this Section, we detail how to configure Squid’s logging output for SEKOIA.IO by means of the Rsyslog transport. We hereby focus on the configuration of Squid and invite the reader to the [Rsyslog Transport](../transport/rsyslog/) documentation to forward these logs to SEKOIA.IO.

To configure Squid logging, you can create a new configuration `99-sekoiaio.conf` file in the `/etc/squid/conf.d/` directory of your server. With most of Squid configurations (including Debian, Red Hat Entreprise Linux, etc.), this file will automatically be used.

This file should contain two information:

- The log format used for SEKOIA.IO.
- The Syslog facility and priority we would like to use.

Content of `/etc/squid/conf.d/99-sekoiaio.conf` file:

```
logformat sekoiaio %ts.%03tu %6tr %>a %Ss/%03>Hs %<st %rm %ru %[un %Sh/%<a %mt "%{Referer}>h" "%{User-Agent}>h"
access_log syslog:local5.info sekoiaio
```

With this configuration, your Squid server leverages your local syslog protocol. You can latter [configure your local Rsyslog server](../transport/rsyslog/) to forward Squid logs to SEKOIA.IO.


## Extracted Fields

The following Table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
| `destination.domain` | `keyword` | The domain name of the destination. |
| `destination.ip` | `ip` | IP address of the destination. |
| `destination.port` | `long` | Port of the destination. |
| `event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
| `event.duration` | `long` | Duration of the event in nanoseconds. |
| `event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
| `event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
| `event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
| `http.request.method` | `keyword` | HTTP request method. |
| `http.request.referrer` | `keyword` | Referrer for this HTTP request. |
| `http.response.bytes` | `long` | Total size in bytes of the response (body and headers). |
| `http.response.mime_type` | `keyword` | Mime type of the body of the response. |
| `http.response.status_code` | `long` | HTTP response status code. |
| `network.direction` | `keyword` | Direction of the network traffic. |
| `network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
| `observer.product` | `keyword` | The product name of the observer. |
| `observer.type` | `keyword` | The type of the observer the data is coming from. |
| `observer.vendor` | `keyword` | Vendor name of the observer. |
| `source.ip` | `ip` | IP address of the source. |
| `url.full` | `wildcard` | Full unparsed URL. |
| `url.original` | `wildcard` | Unmodified original url as seen in the event source. |
| `user.name` | `keyword` | Short name or login of the user. |
| `user_agent.original` | `keyword` | Unparsed user_agent string. |


## Further Readings
- [Integration Source Code](https://github.com/SEKOIA-IO/intake-formats/tree/master/Squid)
- [Squid Wiki - Log configuration](https://wiki.squid-cache.org/SquidFaq/SquidLogs)
