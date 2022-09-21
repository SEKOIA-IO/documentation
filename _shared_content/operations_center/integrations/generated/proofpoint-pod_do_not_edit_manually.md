
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Email gateway` | Proofpoint PoD inspect, classify and detect threats targetting people through email. |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `email` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "test_maillog.json"

    ```json
	
    {
        "message": "{\"data\":\"2022-08-25T17:06:21.935763-07:00 m0169160 sendmail[22003]: 27PNO8ta032355: to=/dev/null, ctladdr=<jcarpenter@bobsbank.ca> (8/0), delay=00:00:00, xdelay=00:00:00, mailer=*file*, tls_verify=NONE, tls_version=NONE, cipher=NONE, pri=32434, dsn=2.0.0, stat=Sent\",\"tls\":{\"version\":\"NONE\",\"verify\":\"NONE\",\"cipher\":\"NONE\"},\"sm\":{\"delay\":\"00:00:00\",\"to\":[\"/dev/null\"],\"pri\":\"32434\",\"dsn\":\"2.0.0\",\"ctladdr\":\"<jcarpenter@bobsbank.ca> (8/0)\",\"qid\":\"27PNO8ta032355\",\"xdelay\":\"00:00:00\",\"stat\":\"Sent\",\"mailer\":\"*file*\"},\"pps\":{\"cid\":\"proofpointdemo_cloudadminuidemo_hosted\",\"agent\":\"m0169160.ppops.net\"},\"ts\":\"2022-08-25T17:06:21.935763-0700\",\"id\":\"41K7tSNsqcyiZCuOX1wmnQ\",\"metadata\":{\"origin\":{\"schemaVersion\":\"20200420\",\"data\":{\"cid\":\"proofpointdemo_cloudadminuidemo_hosted\",\"agent\":\"m0169160.ppops.net\"}},\"customerId\":\"6ae809da-7151-354f-8d3c-40fe90ec6eca\"},\"type\":\"maillog\"}\n",
        "event": {
            "kind": "event",
            "type": [
                "info"
            ],
            "category": [
                "email"
            ],
            "dataset": "maillog"
        },
        "@timestamp": "2022-08-26T00:06:21.935763Z",
        "observer": {
            "vendor": "ProofPoint",
            "product": "ProofPoint On Demand"
        },
        "error": {
            "code": "2.0.0"
        },
        "email": {
            "local_id": "27PNO8ta032355",
            "x_mailer": "*file*",
            "to": {
                "address": [
                    "/dev/null"
                ]
            }
        },
        "network": {
            "transport": "tcp"
        },
        "proofpoint": {
            "pod": {
                "cluster": {
                    "id": "proofpointdemo_cloudadminuidemo_hosted"
                }
            }
        }
    }
    	
	```


=== "test_message.json"

    ```json
	
    {
        "message": "{\"connection\":{\"protocol\":\"smtp:smtp\",\"ip\":\"66.218.66.103\",\"host\":\"n35.grp.scd.yahoo.com\",\"sid\":\"3j6jew035h\",\"resolveStatus\":\"ok\",\"helo\":\"n35.grp.scd.yahoo.com\",\"country\":\"us\"},\"filter\":{\"delivered\":{\"rcpts\":[\"amartinez@thopedia.com\"]},\"qid\":\"27Q0O7ss000303\",\"modules\":{\"spam\":{\"version\":{\"definitions\":\"main-2208250092\",\"engine\":\"8.19.0-2204280000\"},\"langs\":[\"en\",\"pt\",\"es\"],\"scores\":{\"classifiers\":{\"malware\":0,\"lowpriority\":0,\"adult\":0,\"mlx\":0,\"bulk\":0,\"spam\":0,\"phish\":0,\"mlxlog\":372,\"impostor\":0,\"suspect\":0},\"overall\":0,\"engine\":0}}},\"routes\":[\"allow_relay\",\"firewallsafe\",\"internalnet\",\"outbound\"],\"durationSecs\":0.169678,\"suborgs\":{\"sender\":\"0\",\"rcpts\":[\"0\"]},\"verified\":{\"rcpts\":[\"amartinez@thopedia.com\"]},\"disposition\":\"continue\",\"actions\":[{\"module\":\"av\",\"rule\":\"clean\",\"action\":\"add-header\"},{\"module\":\"av\",\"isFinal\":true,\"action\":\"continue\",\"rule\":\"clean\"},{\"module\":\"spam\",\"action\":\"add-header\",\"rule\":\"notspam\"}],\"msgSizeBytes\":4857,\"routeDirection\":\"outbound\"},\"guid\":\"rkuzwIede_tYDQ-P7qUoNlwm6Hz3u1R5\",\"msg\":{\"header\":{\"return-path\":[\"<sentto-4328378-18698-1074787260-gboja=proofpoint.com@returns.groups.yahoo.com>\"],\"to\":[\"\\\"wmoms\\\" <wmoms@yahoogroups.com>\"],\"message-id\":[\"<1C30CBDA666538428B33679A1FB67AFDBA380B@bumail.bradley.edu>\"],\"from\":[\"\\\"Schweigert, Wendy\\\" <wendy@bumail.bradley.edu>\"],\"reply-to\":[\"wmoms@yahoogroups.com\"],\"subject\":[\"[wmoms] ctts\"]},\"sizeBytes\":4275,\"normalizedHeader\":{\"subject\":[\"[wmoms] ctts\"],\"reply-to\":[\"wmoms@yahoogroups.com\"],\"to\":[\"\\\"wmoms\\\" <wmoms@yahoogroups.com>\"],\"message-id\":[\"1C30CBDA666538428B33679A1FB67AFDBA380B@bumail.bradley.edu\"],\"from\":[\"\\\"Schweigert, Wendy\\\" <wendy@bumail.bradley.edu>\"],\"return-path\":[\"<sentto-4328378-18698-1074787260-gboja=proofpoint.com@returns.groups.yahoo.com>\"]},\"parsedAddresses\":{\"from\":[\"wendy@bumail.bradley.edu\"],\"to\":[\"wmoms@yahoogroups.com\"],\"reply-to\":[\"wmoms@yahoogroups.com\"],\"fromDisplayNames\":[\"Schweigert, Wendy\"]},\"lang\":\"en\"},\"msgParts\":[{\"structureId\":\"0\",\"isVirtual\":false,\"labeledName\":\"text.html\",\"isCorrupted\":false,\"md5\":\"f3226e81da52c0cb05d4a7599827b70c\",\"disposition\":\"inline\",\"detectedSizeBytes\":2118,\"detectedExt\":\"HTML\",\"detectedMime\":\"text/html\",\"labeledMime\":\"text/html\",\"textExtracted\":\"U0NBTEFSKDB4N2YxMDhhNzQ3ZDM4KQ==\\n\",\"isTimedOut\":false,\"isDeleted\":false,\"isArchive\":false,\"sizeDecodedBytes\":2118,\"detectedName\":\"text.html\",\"labeledCharset\":\"US-ASCII\",\"labeledExt\":\"html\",\"dataBase64\":\"U0NBTEFSKDB4N2YxMDVlMzNmNzA4KQ==\\n\",\"metadata\":{},\"detectedCharset\":\"US-ASCII\",\"isProtected\":false,\"urls\":[{\"url\":\"http://us.adserver.yahoo.com/l?M=243273.4326031.5516772.1261774/D=egroupmail/S=:HM/A=1750744/rand=299818046\",\"src\":[\"filter\"]},{\"url\":\"http://servedby.advertising.com/site=552006/size=300250/bnum=1074787264333730/bins=1/rich=0\",\"src\":[\"filter\"]},{\"url\":\"http://docs.yahoo.com/info/terms/\",\"src\":[\"filter\"]},{\"url\":\"http://groups.yahoo.com/group/wmoms/\",\"src\":[\"filter\"]},{\"src\":[\"filter\"],\"url\":\"http://rd.yahoo.com/SIG=12co2at1q/M=243273.4326031.5516772.1261774/D=egroupweb/S=1705042054:HM/EXP=1074873664/A=1750744/R=0/*http://servedby.advertising.com/click/site=552006/bnum=1074787264333730\"},{\"src\":[\"filter\"],\"url\":\"mailto:wmoms-unsubscribe@yahoogroups.com?subject=Unsubscribe\"}],\"sha256\":\"3b9778951a276e13059b1d2254cc93ab9744b6e71081c29918ba20ccaa80db9d\"}],\"ts\":\"2022-08-25T17:25:21.071953-0700\",\"metadata\":{\"origin\":{\"data\":{\"agent\":\"m0169160.ppops.net\",\"version\":\"8.19.0.1216\",\"cid\":\"proofpointdemo_cloudadminuidemo_hosted\"}}},\"envelope\":{\"rcpts\":[\"amartinez@thopedia.com\"],\"from\":\"kpereira@cloudadminuidemo.com\"},\"type\":\"message\"}\n",
        "event": {
            "kind": "event",
            "type": [
                "info"
            ],
            "category": [
                "email"
            ],
            "dataset": "message"
        },
        "@timestamp": "2022-08-26T00:25:21.071953Z",
        "observer": {
            "vendor": "ProofPoint",
            "product": "ProofPoint On Demand"
        },
        "email": {
            "local_id": "rkuzwIede_tYDQ-P7qUoNlwm6Hz3u1R5",
            "message_id": "1C30CBDA666538428B33679A1FB67AFDBA380B@bumail.bradley.edu",
            "subject": "[wmoms] ctts",
            "from": {
                "address": [
                    "wendy@bumail.bradley.edu"
                ]
            },
            "to": {
                "address": [
                    "wmoms@yahoogroups.com"
                ]
            },
            "reply_to": {
                "address": [
                    "wmoms@yahoogroups.com"
                ]
            },
            "attachments": [
                {
                    "file": {
                        "mime_type": "text/html",
                        "name": "text.html",
                        "extension": "html",
                        "size": "2118",
                        "hash": {
                            "md5": "f3226e81da52c0cb05d4a7599827b70c",
                            "sha256": "3b9778951a276e13059b1d2254cc93ab9744b6e71081c29918ba20ccaa80db9d"
                        }
                    }
                }
            ]
        },
        "source": {
            "ip": "66.218.66.103",
            "domain": "n35.grp.scd.yahoo.com",
            "geo": {
                "country_iso_code": "us"
            },
            "address": "n35.grp.scd.yahoo.com",
            "top_level_domain": "com",
            "subdomain": "n35.grp.scd",
            "registered_domain": "yahoo.com"
        },
        "network": {
            "transport": "tcp",
            "protocol": "smtp"
        },
        "proofpoint": {
            "pod": {
                "cluster": {
                    "id": "proofpointdemo_cloudadminuidemo_hosted"
                },
                "threat": {
                    "scores": {
                        "malware": 0,
                        "lowpriority": 0,
                        "adult": 0,
                        "mlx": 0,
                        "bulk": 0,
                        "spam": 0,
                        "phish": 0,
                        "mlxlog": 372,
                        "impostor": 0,
                        "suspect": 0
                    }
                },
                "urls": [
                    "http://us.adserver.yahoo.com/l?M=243273.4326031.5516772.1261774/D=egroupmail/S=:HM/A=1750744/rand=299818046",
                    "http://servedby.advertising.com/site=552006/size=300250/bnum=1074787264333730/bins=1/rich=0",
                    "http://docs.yahoo.com/info/terms/",
                    "http://groups.yahoo.com/group/wmoms/",
                    "http://rd.yahoo.com/SIG=12co2at1q/M=243273.4326031.5516772.1261774/D=egroupweb/S=1705042054:HM/EXP=1074873664/A=1750744/R=0/*http://servedby.advertising.com/click/site=552006/bnum=1074787264333730",
                    "mailto:wmoms-unsubscribe@yahoogroups.com?subject=Unsubscribe"
                ],
                "modules": [
                    "spam"
                ]
            }
        },
        "related": {
            "hosts": [
                "n35.grp.scd.yahoo.com"
            ],
            "ip": [
                "66.218.66.103"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`email.attachments` | `array` | A list of objects describing the attachment files sent along with an email message |
|`email.cc.address` | `keyword` | The email address of CC recipient |
|`email.from.address` | `keyword` | The email address of the sender, typically from the RFC 5322 From: header field |
|`email.local_id` | `keyword` | Unique identifier given to the email by the source that created the event |
|`email.message_id` | `keyword` | Identifier from the RFC 5322 Message-ID: email header that refers to a particular email message |
|`email.reply_to.address` | `keyword` | The address that replies should be delivered to based on the value in the RFC 5322 Reply-To: header |
|`email.subject` | `keyword` | A brief summary of the topic of the message |
|`email.to.address` | `keyword` | The email address of recipient |
|`email.x_mailer` | `keyword` | The mailer that send the message |
|`error.code` | `keyword` | Error code describing the error. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`network.protocol` | `keyword` | Application protocol name. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`proofpoint.pod.cluster.id` | `keyword` | The name of the cluster which processed the message |
|`proofpoint.pod.modules` | `array` | The list of the activated modules |
|`proofpoint.pod.urls` | `array` | A list of urls detected in the message |
|`source.domain` | `keyword` | The domain name of the source. |
|`source.geo.country_iso_code` | `keyword` | Country ISO code. |
|`source.ip` | `ip` | IP address of the source. |
|`tls.cipher` | `keyword` | String indicating the cipher used during the current connection. |
|`tls.version` | `keyword` | Numeric part of the version parsed from the original string. |

