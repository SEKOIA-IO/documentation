uuid: 6c2a44e3-a86a-4d98-97a6-d575ffcb29f7
name: Apache HTTP Server
type: intake

## Overview
The Apache HTTP Server, colloquially called Apache, is free and open-source cross-platform web server software, released under the terms of Apache License 2.0. Apache is developed and maintained by an open community of developers under the auspices of the Apache Software Foundation.

!!! info
    Access logs from Tomcat are compatible with existing format Apache HTTP server. Catalina logs are not supported.

{!_shared_content/operations_center/detection/generated/suggested_rules_6c2a44e3-a86a-4d98-97a6-d575ffcb29f7_do_not_edit_manually.md!}


{!_shared_content/operations_center/integrations/generated/6c2a44e3-a86a-4d98-97a6-d575ffcb29f7.md!}

## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "access_combined.json"

    ```json
	
	{
	    "input": {
	        "event": {
	            "created": "2020-06-12T09:43:30.348",
	            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d777"
	        },
	        "log": {
	            "hostname": "B74f1GJTxDUKbh2l"
	        },
	        "message": "127.0.0.1 - Dora [10/Oct/2000:13:55:36 -0700] \"GET /apache_pb.gif HTTP/1.0\" 200 2326 \"http://www.example.com/start.html\" \"Mozilla/4.08 [en] (Win98; I ;Nav)\""
	    },
	    "expected": {
	        "event": {
	            "created": "2020-06-12T09:43:30.348",
	            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d777"
	        },
	        "message": "127.0.0.1 - Dora [10/Oct/2000:13:55:36 -0700] \"GET /apache_pb.gif HTTP/1.0\" 200 2326 \"http://www.example.com/start.html\" \"Mozilla/4.08 [en] (Win98; I ;Nav)\"",
	        "action": {
	            "name": "GET",
	            "outcome": "success"
	        },
	        "http": {
	            "request": {
	                "method": "GET",
	                "referrer": "\"http://www.example.com/start.html\""
	            },
	            "response": {
	                "bytes": 2326,
	                "status_code": 200
	            },
	            "version": "1.0"
	        },
	        "source": {
	            "address": "127.0.0.1",
	            "ip": "127.0.0.1"
	        },
	        "url": {
	            "original": "/apache_pb.gif",
	            "path": "/apache_pb.gif"
	        },
	        "user": {
	            "name": "frank"
	        },
	        "user_agent": {
	            "original": "\"Mozilla/4.08 [en] (Win98; I ;Nav)\""
	        },
	        "type": "kafka",
	        "log": {
	            "hostname": "B74f1GJTxDUKbh2l"
	        },
	        "related": {
	            "user": [
	                "Dora"
	            ],
	            "ip": [
	                "127.0.0.1"
	            ]
	        },
	        "sekoiaio": {
	            "intake": {
	                "parsing_status": "success"
	            }
	        }
	    }
	}

	```


=== "error.json"

    ```json
	
	    {
	    "input": {
	        "event": {
	            "created": "2020-06-12T09:43:30.348",
	            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d777"
	        },
	        "log": {
	            "hostname": "B78f1GJTxDUKbh2l"
	        },
	        "message": "[Wed Oct 11 14:32:52 2000] [error] [client 127.0.0.1] client denied by server configuration: /export/home/live/test"
	    },
	    "expected": {
	        "event": {
	            "created": "2020-06-12T09:43:30.348",
	            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d777"
	        },
	        "message": "[Wed Oct 11 14:32:52 2000] [error] [client 127.0.0.1] client denied by server configuration: /export/home/live/test",
	        "action": {
	            "name": "error",
	            "outcome_reason": "client denied by server configuration: /export/home/live/test",
	            "outcome": "failure"
	        },
	        "source": {
	            "address": "127.0.0.1",
	            "ip": "127.0.0.1"
	        },
	        "type": "kafka",
	        "log": {
	            "hostname": "B78f1GJTxDUKbh2l"
	        },
	        "related": {
	            "ip": [
	                "127.0.0.1"
	            ]
	        },
	        "sekoiaio": {
	            "intake": {
	                "parsing_status": "success"
	            }
	        }
	    }
	  }
    	
	```

=== "modsecurity.json"

    ```json
	
	    {
	    "input": {
	        "event": {
	            "created": "2020-06-12T09:43:30.348",
	            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d777"
	        },
	        "log": {
	            "hostname": "B96f1GJTxDUKb777"
	        },
	        "message": "[security2:error] [pid 11852:tid 4036848777] [client 111.5.222.49:35323] [client 111.5.222.49] ModSecurity: Warning. Pattern match \"(?i)((?:=|U\\\\\\\\s*R\\\\\\\\s*L\\\\\\\\s*\\\\\\\\()\\\\\\\\s*[^>]*\\\\\\\\s*S\\\\\\\\s*C\\\\\\\\s*R\\\\\\\\s*I\\\\\\\\s*P\\\\\\\\s*T\\\\\\\\s*:|&colon;|[\\\\\\\\s\\\\\\\\S]allowscriptaccess[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]src[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]data:text\\\\\\\\/html[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]xlink:href[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]base64[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]xmlns[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]xht ...\" at ARGS:__EVENTVALIDATION. [file \"/usr/apache/conf/waf/crs_xss_attacks.conf\"] [line \"28\"] [id \"973338\"] [rev \"1\"] [msg \"XSS Filter - Category 3: Javascript URI Vector\"] [data \"Matched Data: kSrcX found within ARGS:__EVENTVALIDATION: /wEWZgKXrrj77gKCwsjDDAKgoeW1DwKBkN74CAKv/cWX77gK//Oz1DQKM77IdApW x44CAon4rvAGAq/9xZ77GAr/87PUNAoz77kh0Cr/3Fl77Cv/zs977CjOmSHQKv/cW77gK//Oz1DQKM677dAq/9xZc77r/87PUNAozpk77Cr/3Flw77v/zs9Q0CjOmS77Kv/cWX77K//Oz1DQKM6ZI77q/9xZc77r/87PUNAozp770Cr/3Fl77Cv/zs9Q0CjO77HQKv/cW77gK//Oz1DQKM677dAq/9xZc77r/87PUNAozpk77Cr/3Flw77v/zs9Q0CjOm77QKv/cW77gK//Oz1DQKM6ZId77/9xZc77r/87PUNAozp770Cr/3Fl77Cv/zs9Q0CjOmS77Kv/cW77gK//Oz1DQKM77IdAq/9xZc77r/87PUNAozp77Cr/3FlwY77/zs...\"] [severity \"CRITICAL\"] [ver \"OWASP_CRS/ [hostname \" aa.xyz.com\"] [uri \"/Liste.aspx\"] [unique_id \"Xt2vlKC-777FovDc0GkwZZZs\"], referer: http://trafic.com/Liste.aspx?ECRAN=REEL_MIXTE"
	    },
	    "expected": {
	        "event": {
	            "created": "2020-06-12T09:43:30.348",
	            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d777"
	        },
	        "message": "[security2:error] [pid 11852:tid 4036848777] [client 61.5.222.49:35323] [client 61.5.222.49] ModSecurity: Warning. Pattern match \"(?i)((?:=|U\\\\\\\\s*R\\\\\\\\s*L\\\\\\\\s*\\\\\\\\()\\\\\\\\s*[^>]*\\\\\\\\s*S\\\\\\\\s*C\\\\\\\\s*R\\\\\\\\s*I\\\\\\\\s*P\\\\\\\\s*T\\\\\\\\s*:|&colon;|[\\\\\\\\s\\\\\\\\S]allowscriptaccess[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]src[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]data:text\\\\\\\\/html[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]xlink:href[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]base64[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]xmlns[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]xht ...\" at ARGS:__EVENTVALIDATION. [file \"/usr/apache/conf/waf/crs_xss_attacks.conf\"] [line \"28\"] [id \"973338\"] [rev \"1\"] [msg \"XSS Filter - Category 3: Javascript URI Vector\"] [data \"Matched Data: kSrcX found within ARGS:__EVENTVALIDATION: /wEWZgKXrrj77gKCwsjDDAKgoeW1DwKBkN74CAKv/cWX77gK//Oz1DQKM77IdApW x44CAon4rvAGAq/9xZ77GAr/87PUNAoz77kh0Cr/3Fl77Cv/zs977CjOmSHQKv/cW77gK//Oz1DQKM677dAq/9xZc77r/87PUNAozpk77Cr/3Flw77v/zs9Q0CjOmS77Kv/cWX77K//Oz1DQKM6ZI77q/9xZc77r/87PUNAozp770Cr/3Fl77Cv/zs9Q0CjO77HQKv/cW77gK//Oz1DQKM677dAq/9xZc77r/87PUNAozpk77Cr/3Flw77v/zs9Q0CjOm77QKv/cW77gK//Oz1DQKM6ZId77/9xZc77r/87PUNAozp770Cr/3Fl77Cv/zs9Q0CjOmS77Kv/cW77gK//Oz1DQKM77IdAq/9xZc77r/87PUNAozp77Cr/3FlwY77/zs...\"] [severity \"CRITICAL\"] [ver \"OWASP_CRS/ [hostname \" aa.xyz.com\"] [uri \"/Liste.aspx\"] [unique_id \"Xt2vlKC-777FovDc0GkwZZZs\"], referer: http://trafic.com/Liste.aspx?ECRAN=REEL_MIXTE",
	        "action": {
	            "type": "warning",
	            "name": "error",
	            "outcome_reason": "XSS Filter - Category 3: Javascript URI Vector",
	            "outcome": "failure",
	            "properties": [
	                {
	                    "modsecmessage": "Pattern match \"(?i)((?:=|U\\\\\\\\s*R\\\\\\\\s*L\\\\\\\\s*\\\\\\\\()\\\\\\\\s*[^>]*\\\\\\\\s*S\\\\\\\\s*C\\\\\\\\s*R\\\\\\\\s*I\\\\\\\\s*P\\\\\\\\s*T\\\\\\\\s*:|&colon;|[\\\\\\\\s\\\\\\\\S]allowscriptaccess[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]src[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]data:text\\\\\\\\/html[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]xlink:href[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]base64[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]xmlns[\\\\\\\\s\\\\\\\\S]|[\\\\\\\\s\\\\\\\\S]xht ...\" at ARGS:__EVENTVALIDATION.",
	                    "ruledata": "Matched Data: kSrcX found within ARGS:__EVENTVALIDATION: /wEWZgKXrrj77gKCwsjDDAKgoeW1DwKBkN74CAKv/cWX77gK//Oz1DQKM77IdApW x44CAon4rvAGAq/9xZ77GAr/87PUNAoz77kh0Cr/3Fl77Cv/zs977CjOmSHQKv/cW77gK//Oz1DQKM677dAq/9xZc77r/87PUNAozpk77Cr/3Flw77v/zs9Q0CjOmS77Kv/cWX77K//Oz1DQKM6ZI77q/9xZc77r/87PUNAozp770Cr/3Fl77Cv/zs9Q0CjO77HQKv/cW77gK//Oz1DQKM677dAq/9xZc77r/87PUNAozpk77Cr/3Flw77v/zs9Q0CjOm77QKv/cW77gK//Oz1DQKM6ZId77/9xZc77r/87PUNAozp770Cr/3Fl77Cv/zs9Q0CjOmS77Kv/cW77gK//Oz1DQKM77IdAq/9xZc77r/87PUNAozp77Cr/3FlwY77/zs...",
	                    "rulefile": "/usr/apache/conf/waf/crs_xss_attacks.conf",
	                    "ruleid": "973338",
	                    "ruleline": "28",
	                    "rulerev": "1",
	                    "ruleseverity": "CRITICAL",
	                    "uniqueid": "Xt2vlKC-777FovDc0GkwZZZs"
	                }
	            ]
	        },
	        "process": {
	            "id": 11852,
	            "pid": 11852,
	            "thread": {
	                "id": 4036848777
	            }
	        },
	        "source": {
	            "address": "111.5.222.49",
	            "ip": "111.5.222.49",
	            "port": 35323
	        },
	        "destination": {
	            "domain": " aa.xyz.com",
	            "size_in_char": 13
	        },
	        "url": {
	            "original": "/Liste.aspx",
	            "path": "/Liste.aspx"
	        },
	        "type": "kafka",
	        "log": {
	            "hostname": "B96f1GJTxDUKb777"
	        },
	        "related": {
	            "ip": [
	                "111.5.222.49"
	            ]
	        },
	        "sekoiaio": {
	            "intake": {
	                "parsing_status": "success"
	            }
	        }
	    }
	  }
    	
	```

## Configure

As of now, the main solution to collect Apache logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Forward logs to Sekoia.io

This setup guide will show you how to forward both your access and error logs to Sekoia.io by means of an rsyslog transport channel. The reader is also invited to consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io.

At the beginning of your rsyslog configuration file for the Apache logs,  paste the following instruction to order the rsyslog server to load the module `imfile`:
```bash
$ModLoad imfile
```

Then use the following configuration to leverage this module to monitor apache httpd access and error output files (please note that the path to the log file may change depending on the OS and your configuration):
```bash
# error log
$InputFileName /var/log/apache2/error.log
$InputFileTag apache:
$InputFileStateFile stat-apache-error
$InputFileSeverity error
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor

# access log
$InputFileName /var/log/apache2/access.log
$InputFileTag apache:
$InputFileStateFile stat-apache-access
$InputFileSeverity notice
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor
```

## Further Reading
- [Apache documentation](http://httpd.apache.org/docs/)
- [Rsyslog IMFile module](https://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html)
