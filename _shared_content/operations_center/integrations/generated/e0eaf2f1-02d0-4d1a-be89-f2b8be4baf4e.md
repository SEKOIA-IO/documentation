
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Email gateway` | Proofpoint PoD inspect, classify and detect threats targetting people through email. |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `` |
| Category | `email`, `network` |
| Type | `info` |




### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "test_maillog.json"

    ```json
	
    {
        "message": "{\"data\":\"2022-08-25T17:06:21.935763-07:00 m0169160 sendmail[22003]: 27PNO8ta032355: to=REDACTED, ctladdr=<user@example.org> (8/0), delay=00:00:00, xdelay=00:00:00, mailer=*file*, tls_verify=NONE, tls_version=NONE, cipher=NONE, pri=32434, dsn=2.0.0, stat=Sent\",\"tls\":{\"version\":\"NONE\",\"verify\":\"NONE\",\"cipher\":\"NONE\"},\"sm\":{\"delay\":\"00:00:00\",\"to\":[\"REDACTED\"],\"pri\":\"32434\",\"dsn\":\"2.0.0\",\"ctladdr\":\"<user@example.org> (8/0)\",\"qid\":\"27PNO8ta032355\",\"xdelay\":\"00:00:00\",\"stat\":\"Sent\",\"mailer\":\"*file*\"},\"pps\":{\"cid\":\"proofpointdemo_cloudadminuidemo_hosted\",\"agent\":\"m0169160.ppops.net\"},\"ts\":\"2022-08-25T17:06:21.935763-0700\",\"id\":\"41K7tSNsqcyiZCuOX1wmnQ\",\"metadata\":{\"origin\":{\"schemaVersion\":\"20200420\",\"data\":{\"cid\":\"proofpointdemo_cloudadminuidemo_hosted\",\"agent\":\"m0169160.ppops.net\"}},\"customerId\":\"6ae809da-7151-354f-8d3c-40fe90ec6eca\"},\"type\":\"maillog\"}\n",
        "event": {
            "category": [
                "email"
            ],
            "dataset": "maillog",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2022-08-26T00:06:21.935763Z",
        "email": {
            "local_id": "27PNO8ta032355",
            "to": {
                "address": [
                    "REDACTED"
                ]
            },
            "x_mailer": "*file*"
        },
        "error": {
            "code": "2.0.0"
        },
        "network": {
            "transport": "tcp"
        },
        "observer": {
            "product": "ProofPoint On Demand",
            "vendor": "ProofPoint"
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
        "message": "{\"connection\":{\"protocol\":\"smtp:smtp\",\"ip\":\"1.2.3.4\",\"host\":\"n35.grp.scd.example.com\",\"sid\":\"3j6jew035h\",\"resolveStatus\":\"ok\",\"helo\":\"n35.grp.scd.example.com\",\"country\":\"us\"},\"filter\":{\"delivered\":{\"rcpts\":[\"amartinez@thopedia.com\"]},\"qid\":\"27Q0O7ss000303\",\"modules\":{\"spam\":{\"version\":{\"definitions\":\"main-2208250092\",\"engine\":\"8.19.0-2204280000\"},\"langs\":[\"en\",\"pt\",\"es\"],\"scores\":{\"classifiers\":{\"malware\":0,\"lowpriority\":0,\"adult\":0,\"mlx\":0,\"bulk\":0,\"spam\":0,\"phish\":0,\"mlxlog\":372,\"impostor\":0,\"suspect\":0},\"overall\":0,\"engine\":0}}},\"routes\":[\"allow_relay\",\"firewallsafe\",\"internalnet\",\"outbound\"],\"durationSecs\":0.169678,\"suborgs\":{\"sender\":\"0\",\"rcpts\":[\"0\"]},\"verified\":{\"rcpts\":[\"amartinez@thopedia.com\"]},\"disposition\":\"continue\",\"actions\":[{\"module\":\"av\",\"rule\":\"clean\",\"action\":\"add-header\"},{\"module\":\"av\",\"isFinal\":true,\"action\":\"continue\",\"rule\":\"clean\"},{\"module\":\"spam\",\"action\":\"add-header\",\"rule\":\"notspam\"}],\"msgSizeBytes\":4857,\"routeDirection\":\"outbound\"},\"guid\":\"rkuzwIede_tYDQ-P7qUoNlwm6Hz3u1R5\",\"msg\":{\"header\":{\"return-path\":[\"<sentto-4328378-18698-1074787260-gboja=proofpoint.com@returns.groups.yahoo.com>\"],\"to\":[\"\\\"wmoms\\\" <user2@example.org>\"],\"message-id\":[\"<111111111111111111111@example.com>\"],\"from\":[\"\\\"Schweigert, Wendy\\\" <user1@example.com>\"],\"reply-to\":[\"user2@example.org\"],\"subject\":[\"REDACTED\"]},\"sizeBytes\":4275,\"normalizedHeader\":{\"subject\":[\"REDACTED\"],\"reply-to\":[\"user2@example.org\"],\"to\":[\"\\\"wmoms\\\" <user2@example.org>\"],\"message-id\":[\"111111111111111111111@example.com\"],\"from\":[\"\\\"Schweigert, Wendy\\\" <user1@example.com>\"],\"return-path\":[\"<sentto-4328378-18698-1074787260-gboja=proofpoint.com@returns.groups.yahoo.com>\"]},\"parsedAddresses\":{\"from\":[\"user1@example.com\"],\"to\":[\"user2@example.org\"],\"reply-to\":[\"user2@example.org\"],\"fromDisplayNames\":[\"Schweigert, Wendy\"]},\"lang\":\"en\"},\"ts\":\"2022-08-25T17:25:21.071953-0700\",\"metadata\":{\"origin\":{\"data\":{\"agent\":\"m0169160.ppops.net\",\"version\":\"8.19.0.1216\",\"cid\":\"proofpointdemo_cloudadminuidemo_hosted\"}}},\"envelope\":{\"rcpts\":[\"amartinez@thopedia.com\"],\"from\":\"kpereira@cloudadminuidemo.com\"},\"type\":\"message\"}\n",
        "event": {
            "action": "continue",
            "category": [
                "email",
                "network"
            ],
            "dataset": "message",
            "type": [
                "allowed"
            ]
        },
        "@timestamp": "2022-08-26T00:25:21.071953Z",
        "email": {
            "from": {
                "address": [
                    "user1@example.com"
                ]
            },
            "local_id": "rkuzwIede_tYDQ-P7qUoNlwm6Hz3u1R5",
            "message_id": "111111111111111111111@example.com",
            "reply_to": {
                "address": [
                    "user2@example.org"
                ]
            },
            "subject": "REDACTED",
            "to": {
                "address": [
                    "user2@example.org"
                ]
            }
        },
        "network": {
            "protocol": "smtp",
            "transport": "tcp"
        },
        "observer": {
            "product": "ProofPoint On Demand",
            "vendor": "ProofPoint"
        },
        "proofpoint": {
            "pod": {
                "cluster": {
                    "id": "proofpointdemo_cloudadminuidemo_hosted"
                },
                "modules": [
                    "spam"
                ],
                "routes": [
                    "allow_relay",
                    "firewallsafe",
                    "internalnet",
                    "outbound"
                ],
                "smtp": {
                    "recipients": [
                        "amartinez@thopedia.com"
                    ],
                    "sender": "kpereira@cloudadminuidemo.com"
                },
                "threat": {
                    "scores": {
                        "adult": 0,
                        "bulk": 0,
                        "impostor": 0,
                        "lowpriority": 0,
                        "malware": 0,
                        "mlx": 0,
                        "mlxlog": 372,
                        "phish": 0,
                        "spam": 0,
                        "suspect": 0
                    }
                }
            }
        },
        "related": {
            "hosts": [
                "n35.grp.scd.example.com"
            ],
            "ip": [
                "1.2.3.4"
            ]
        },
        "source": {
            "address": "n35.grp.scd.example.com",
            "domain": "n35.grp.scd.example.com",
            "ip": "1.2.3.4",
            "registered_domain": "example.com",
            "subdomain": "n35.grp.scd",
            "top_level_domain": "com"
        }
    }
    	
	```


=== "test_message2.json"

    ```json
	
    {
        "message": "{\"metadata\":{\"origin\":{\"data\":{\"cid\":\"proofpointdemo_cloudadminuidemo_hosted\",\"agent\":\"m0169161.ppops.net\",\"version\":\"8.19.0.1216\"}}},\"ts\":\"2022-09-11T18:28:19.902627-0700\",\"envelope\":{\"from\":\"user1@example.net\",\"rcpts\":[\"ceo@exec.vogon.science\"]},\"connection\":{\"host\":\"1-2-3-4.example.com\",\"ip\":\"5.6.7.8\",\"sid\":\"3jgptm9dux\",\"tls\":{\"inbound\":{\"version\":\"TLSv1.2\",\"cipherBits\":256,\"cipher\":\"ECDHE-RSA-AES256-GCM-SHA384\"}},\"country\":\"us\",\"protocol\":\"smtp:smtp\",\"resolveStatus\":\"ok\",\"helo\":\"selabfork.ppslab.net\"},\"msg\":{\"lang\":\"ja\",\"normalizedHeader\":{\"to\":[\"<user2@example.org>\"],\"subject\":[\"ANONYMIZED\"],\"message-id\":[\"20220912092800466772@example.net\"],\"x-mailer\":[\"Xwstoxzpk 1\"],\"from\":[\"\\\"Amazon\\\" <user1@example.net>\"]},\"parsedAddresses\":{\"fromDisplayNames\":[\"Amazon\"],\"from\":[\"user1@example.net\"],\"to\":[\"user2@example.org\"]},\"header\":{\"from\":[\"\\\"Amazon\\\" <user1@example.net>\"],\"message-id\":[\"<20220912092800466772@example.net>\"],\"x-mailer\":[\"Xwstoxzpk 1\"],\"subject\":[\"REDACTED\"],\"to\":[\"<user2@example.org>\"]},\"sizeBytes\":33366},\"filter\":{\"actions\":[{\"rule\":\"clean\",\"action\":\"add-header\",\"module\":\"av\"},{\"rule\":\"clean\",\"action\":\"continue\",\"module\":\"av\"},{\"action\":\"add-header\",\"module\":\"spam\",\"rule\":\"phish\"},{\"rule\":\"phish\",\"action\":\"copy\",\"module\":\"spam\"},{\"rule\":\"phish\",\"module\":\"spam\",\"action\":\"quarantine\"},{\"module\":\"spam\",\"action\":\"discard\",\"rule\":\"phish\",\"isFinal\":true}],\"modules\":{\"urldefense\":{\"counts\":{\"total\":5,\"unique\":2,\"rewritten\":5},\"version\":{\"engine\":\"15\"}},\"spam\":{\"langs\":[\"en\",\"jp\",\"pt\"],\"triggeredClassifier\":\"phish\",\"scores\":{\"overall\":100,\"engine\":100,\"classifiers\":{\"adult\":0,\"mlx\":100,\"impostor\":0,\"spam\":100,\"malware\":0,\"mlxlog\":-1000,\"phish\":100,\"suspect\":0,\"lowpriority\":0,\"bulk\":0}},\"version\":{\"definitions\":\"main-2209120003\",\"engine\":\"8.19.0-2204280000\"}},\"spf\":{\"domain\":\"yokm.net\",\"result\":\"none\"},\"dmarc\":{\"records\":[{\"error\":\"NXDOMAIN\",\"query\":\"_dmarc.yokm.net\"}],\"filterdResult\":\"none\",\"authResults\":[{\"method\":\"spf\",\"emailIdentities\":{\"smtp.mailfrom\":\"user1@example.net\"},\"result\":\"none\"},{\"method\":\"dmarc\",\"result\":\"none\"}],\"srvid\":\"ppops.net\"}},\"suborgs\":{\"sender\":\"0\",\"rcpts\":[\"0\"]},\"isMsgInDigest\":true,\"routeDirection\":\"internal\",\"verified\":{\"rcpts\":[\"ceo@exec.vogon.science\"]},\"msgSizeBytes\":33278,\"routes\":[\"allow_relay\",\"default_inbound\",\"firewallsafe\",\"internalnet\"],\"durationSecs\":0.356614,\"delivered\":{\"rcpts\":[\"ceo@exec.vogon.science\"]},\"disposition\":\"discard\",\"qid\":\"3jgptm9dux-1\",\"quarantine\":{\"module\":\"spam\",\"folderId\":\"phish\",\"type\":\"quarantine\",\"folder\":\"Phish\",\"rule\":\"phish\"}},\"guid\":\"5PVdahx3PMGFONShVUQ19uni34-uVQRm\",\"type\":\"message\"}\n",
        "event": {
            "action": "discard",
            "category": [
                "email",
                "network"
            ],
            "dataset": "message",
            "type": [
                "denied"
            ]
        },
        "@timestamp": "2022-09-12T01:28:19.902627Z",
        "email": {
            "from": {
                "address": [
                    "user1@example.net"
                ]
            },
            "local_id": "5PVdahx3PMGFONShVUQ19uni34-uVQRm",
            "message_id": "20220912092800466772@example.net",
            "subject": "ANONYMIZED",
            "to": {
                "address": [
                    "user2@example.org"
                ]
            }
        },
        "network": {
            "protocol": "smtp",
            "transport": "tcp"
        },
        "observer": {
            "product": "ProofPoint On Demand",
            "vendor": "ProofPoint"
        },
        "proofpoint": {
            "pod": {
                "cluster": {
                    "id": "proofpointdemo_cloudadminuidemo_hosted"
                },
                "modules": [
                    "dmarc",
                    "spam",
                    "spf",
                    "urldefense"
                ],
                "quarantine": {
                    "folder": "Phish",
                    "module": "spam",
                    "rule": "phish",
                    "type": "quarantine"
                },
                "routes": [
                    "allow_relay",
                    "default_inbound",
                    "firewallsafe",
                    "internalnet"
                ],
                "smtp": {
                    "recipients": [
                        "ceo@exec.vogon.science"
                    ],
                    "sender": "user1@example.net"
                },
                "threat": {
                    "scores": {
                        "adult": 0,
                        "bulk": 0,
                        "impostor": 0,
                        "lowpriority": 0,
                        "malware": 0,
                        "mlx": 100,
                        "mlxlog": -1000,
                        "phish": 100,
                        "spam": 100,
                        "suspect": 0
                    }
                }
            }
        },
        "related": {
            "hosts": [
                "1-2-3-4.example.com"
            ],
            "ip": [
                "5.6.7.8"
            ]
        },
        "source": {
            "address": "1-2-3-4.example.com",
            "domain": "1-2-3-4.example.com",
            "ip": "5.6.7.8",
            "registered_domain": "example.com",
            "subdomain": "1-2-3-4",
            "top_level_domain": "com"
        },
        "tls": {
            "cipher": "ECDHE-RSA-AES256-GCM-SHA384",
            "version": "TLSv1.2"
        }
    }
    	
	```


=== "test_message3.json"

    ```json
	
    {
        "message": "{\"connection\":{\"resolveStatus\":\"[unknown]\",\"host\":\"hostname\",\"country\":\"**\",\"ip\":\"127.0.0.1\",\"helo\":\"outbound.proofpointdemo\",\"protocol\":\"smtp:smtp\",\"sid\":\"3jryreg677\"},\"ts\":\"2022-09-22T17:06:53.370514-0700\",\"metadata\":{\"origin\":{\"data\":{\"agent\":\"m0169160.ppops.net\",\"cid\":\"proofpointdemo_cloudadminuidemo_hosted\",\"version\":\"8.19.0.1216\"}}},\"msg\":{\"header\":{\"message-id\":[\"<user11@example.net>\"],\"subject\":[\"\"]},\"lang\":\"und\",\"parsedAddresses\":{},\"normalizedHeader\":{\"message-id\":[\"user11@example.net\"],\"subject\":[\"\"]},\"sizeBytes\":203},\"envelope\":{\"from\":\"user3@example.org\",\"rcpts\":[\"user2@example.net\"]},\"guid\":\"xjin0zM1KZbSWy8mUJvOxTV7WqFRrbd1\",\"filter\":{\"durationSecs\":0.096616,\"disposition\":\"continue\",\"suborgs\":{\"rcpts\":[\"0\"],\"sender\":\"0\"},\"routeDirection\":\"outbound\",\"msgSizeBytes\":728,\"modules\":{\"spam\":{\"langs\":[\"en\"],\"scores\":{\"overall\":40,\"engine\":40,\"classifiers\":{\"lowpriority\":4,\"mlxlog\":18,\"suspect\":0,\"adult\":8,\"spam\":40,\"malware\":0,\"phish\":1,\"bulk\":4,\"impostor\":0,\"mlx\":40}},\"version\":{\"definitions\":\"main-2209220155\",\"engine\":\"8.19.0-2209130001\"}}},\"verified\":{\"rcpts\":[\"user2@example.net\"]},\"routes\":[\"allow_relay\",\"firewallsafe\",\"internalnet\",\"outbound\"],\"actions\":[{\"module\":\"av\",\"action\":\"add-header\",\"rule\":\"clean\"},{\"module\":\"av\",\"action\":\"continue\",\"rule\":\"clean\",\"isFinal\":true},{\"module\":\"spam\",\"action\":\"add-header\",\"rule\":\"notspam\"}],\"delivered\":{\"rcpts\":[\"user2@example.net\"]},\"qid\":\"28MNsFLm006936\"},\"type\":\"message\"}\n",
        "event": {
            "action": "continue",
            "category": [
                "email",
                "network"
            ],
            "dataset": "message",
            "type": [
                "allowed"
            ]
        },
        "@timestamp": "2022-09-23T00:06:53.370514Z",
        "email": {
            "local_id": "xjin0zM1KZbSWy8mUJvOxTV7WqFRrbd1",
            "message_id": "user11@example.net"
        },
        "network": {
            "protocol": "smtp",
            "transport": "tcp"
        },
        "observer": {
            "product": "ProofPoint On Demand",
            "vendor": "ProofPoint"
        },
        "proofpoint": {
            "pod": {
                "cluster": {
                    "id": "proofpointdemo_cloudadminuidemo_hosted"
                },
                "modules": [
                    "spam"
                ],
                "routes": [
                    "allow_relay",
                    "firewallsafe",
                    "internalnet",
                    "outbound"
                ],
                "smtp": {
                    "recipients": [
                        "user2@example.net"
                    ],
                    "sender": "user3@example.org"
                },
                "threat": {
                    "scores": {
                        "adult": 8,
                        "bulk": 4,
                        "impostor": 0,
                        "lowpriority": 4,
                        "malware": 0,
                        "mlx": 40,
                        "mlxlog": 18,
                        "phish": 1,
                        "spam": 40,
                        "suspect": 0
                    }
                }
            }
        },
        "related": {
            "hosts": [
                "hostname"
            ],
            "ip": [
                "127.0.0.1"
            ]
        },
        "source": {
            "address": "hostname",
            "domain": "hostname",
            "ip": "127.0.0.1"
        }
    }
    	
	```


=== "test_msgpart_url.json"

    ```json
	
    {
        "message": "{\"guid\":\"1234567890\",\"ts\":\"2023-04-12T06:00:05.289102-0700\",\"type\":\"msgPartsUrl\",\"part_uuid\":\"607330be-4eb6-4f6e-9f74-0cbcab2e1ad4\",\"url\":\"http://www.example.org/\",\"src\":[\"filter\"],\"disposition\":\"continue\"}\n",
        "event": {
            "action": "continue",
            "category": [
                "email"
            ],
            "dataset": "msgPartsUrl",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-04-12T13:00:05.289102Z",
        "email": {
            "local_id": "1234567890"
        },
        "observer": {
            "product": "ProofPoint On Demand",
            "vendor": "ProofPoint"
        },
        "proofpoint": {
            "pod": {
                "msgpart": {
                    "id": "607330be-4eb6-4f6e-9f74-0cbcab2e1ad4"
                }
            }
        },
        "url": {
            "domain": "www.example.org",
            "original": "http://www.example.org/",
            "path": "/",
            "port": 80,
            "registered_domain": "example.org",
            "scheme": "http",
            "subdomain": "www",
            "top_level_domain": "org"
        }
    }
    	
	```


=== "test_msgparts.json"

    ```json
	
    {
        "message": "{\"msgParts\":{\"structureId\":\"0\",\"isVirtual\":false,\"labeledName\":\"text.html\",\"isCorrupted\":false,\"md5\":\"f3226e81da52c0cb05d4a7599827b70c\",\"disposition\":\"inline\",\"detectedSizeBytes\":2118,\"detectedExt\":\"HTML\",\"detectedMime\":\"text/html\",\"labeledMime\":\"text/html\",\"textExtracted\":\"U0NBTEFSKDB4N2YxMDhhNzQ3ZDM4KQ==n\",\"isTimedOut\":false,\"isDeleted\":false,\"isArchive\":false,\"sizeDecodedBytes\":2118,\"detectedName\":\"text.html\",\"labeledCharset\":\"US-ASCII\",\"labeledExt\":\"html\",\"dataBase64\":\"U0NBTEFSKDB4N2YxMDVlMzNmNzA4KQ==n\",\"metadata\":{},\"detectedCharset\":\"US-ASCII\",\"isProtected\":false,\"urls\":[{\"url\":\"http://us.adserver.example.com/?REDACTED\",\"src\":[\"filter\"]},{\"url\":\"http://servedby.advertising.com/site=552006/size=300250/bnum=1074787264333730/bins=1/rich=0\",\"src\":[\"filter\"]},{\"url\":\"http://docs.yahoo.com/info/terms/\",\"src\":[\"filter\"]},{\"url\":\"http://groups.yahoo.com/group/wmoms/\",\"src\":[\"filter\"]},{\"src\":[\"filter\"],\"url\":\"http://rd.yahoo.com/SIG=12co2at1q/M=243273.4326031.5516772.1261774/D=egroupweb/S=1705042054:HM/EXP=1074873664/A=1750744/R=0/*http://servedby.advertising.com/click/site=552006/bnum=1074787264333730\"},{\"src\":[\"filter\"],\"url\":\"mailto:wmoms-unsubscribe@yahoogroups.com?subject=Unsubscribe\"}],\"sha256\":\"3b9778951a276e13059b1d2254cc93ab9744b6e71081c29918ba20ccaa80db9d\"}, \"type\": \"msgParts\", \"guid\": \"1234567890\", \"uuid\": \"eb99b626-c278-4af3-96f8-5a194e016a43\",\"disposition\":\"continue\"}",
        "event": {
            "action": "continue",
            "category": [
                "email"
            ],
            "dataset": "msgParts",
            "type": [
                "info"
            ]
        },
        "email": {
            "attachments": [
                {
                    "file": {
                        "extension": "html",
                        "hash": {
                            "md5": "f3226e81da52c0cb05d4a7599827b70c",
                            "sha256": "3b9778951a276e13059b1d2254cc93ab9744b6e71081c29918ba20ccaa80db9d"
                        },
                        "mime_type": "text/html",
                        "name": "text.html",
                        "size": 2118
                    }
                }
            ],
            "local_id": "1234567890"
        },
        "file": {
            "hash": {
                "md5": "f3226e81da52c0cb05d4a7599827b70c",
                "sha256": "3b9778951a276e13059b1d2254cc93ab9744b6e71081c29918ba20ccaa80db9d"
            },
            "name": "text.html"
        },
        "observer": {
            "product": "ProofPoint On Demand",
            "vendor": "ProofPoint"
        },
        "proofpoint": {
            "pod": {
                "msgpart": {
                    "id": "eb99b626-c278-4af3-96f8-5a194e016a43"
                },
                "urls": [
                    "http://docs.yahoo.com/info/terms/",
                    "http://groups.yahoo.com/group/wmoms/",
                    "http://rd.yahoo.com/SIG=12co2at1q/M=243273.4326031.5516772.1261774/D=egroupweb/S=1705042054:HM/EXP=1074873664/A=1750744/R=0/*http://servedby.advertising.com/click/site=552006/bnum=1074787264333730",
                    "http://servedby.advertising.com/site=552006/size=300250/bnum=1074787264333730/bins=1/rich=0",
                    "http://us.adserver.example.com/?REDACTED",
                    "mailto:wmoms-unsubscribe@yahoogroups.com?subject=Unsubscribe"
                ]
            }
        },
        "related": {
            "hash": [
                "3b9778951a276e13059b1d2254cc93ab9744b6e71081c29918ba20ccaa80db9d",
                "f3226e81da52c0cb05d4a7599827b70c"
            ]
        },
        "url": {
            "domain": "us.adserver.example.com",
            "original": "http://us.adserver.example.com/?REDACTED",
            "path": "/",
            "port": 80,
            "query": "REDACTED",
            "registered_domain": "example.com",
            "scheme": "http",
            "subdomain": "us.adserver",
            "top_level_domain": "com"
        }
    }
    	
	```


=== "test_msgparts_metadata.json"

    ```json
	
    {
        "message": "{\"msgParts\": {\"sha256\": \"741d139c90f3db2f790cdb31d3ed9716fd0eebd504114a0e269127f09e5b0479\", \"labeledName\": \"dlp - template.xlsx\", \"isTimedOut\": false, \"isDeleted\": false, \"detectedName\": \"dlp - template.xlsx\", \"detectedExt\": \"XLSX\", \"detectedCharset\": \"\", \"textExtracted\": \"U0NBTEFSKDB4N2YyNjE5NTViYTM4KQ==\\n\", \"metadata\": {\"codepage\": 65001, \"create_dtm\": \"2025-11-20 21:38:41\", \"modified\": \"2025-11-20 21:38:41\", \"lastauthor\": \"MOMENZADEH Thomas (EXT)\", \"appversion\": \"16.0300\", \"application\": \"Microsoft Excel Online\", \"created\": \"2025-11-20 21:38:41\", \"appname\": \"Microsoft Excel Online\", \"lastsave_dtm\": \"2025-11-20 21:38:41\"}, \"isArchive\": false, \"labeledExt\": \"xlsx\", \"isCorrupted\": false, \"dataBase64\": \"U0NBTEFSKDB4N2YyODMxZTcxYTM4KQ==\\n\", \"structureId\": \"1\", \"labeledCharset\": \"\", \"sizeDecodedBytes\": 23741, \"detectedMime\": \"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\", \"detectedSizeBytes\": 23741, \"isProtected\": false, \"isVirtual\": false, \"disposition\": \"attached\", \"labeledMime\": \"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\", \"md5\": \"596a2fe42e0af1b90e5427f706bfb745\"}, \"guid\": \"2X6R0Z9mr_zQhgw_6glhAZc-dw9_iFKk\", \"type\": \"msgParts\", \"ts\": \"2025-11-20T21:39:14.304430+0000\", \"uuid\": \"8ea3df61-8b18-4ec6-a0af-743321e08b50\", \"disposition\": \"continue\"}",
        "event": {
            "action": "continue",
            "category": [
                "email"
            ],
            "dataset": "msgParts",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2025-11-20T21:39:14.304430Z",
        "email": {
            "attachments": [
                {
                    "file": {
                        "extension": "xlsx",
                        "hash": {
                            "md5": "596a2fe42e0af1b90e5427f706bfb745",
                            "sha256": "741d139c90f3db2f790cdb31d3ed9716fd0eebd504114a0e269127f09e5b0479"
                        },
                        "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        "name": "dlp - template.xlsx",
                        "size": 23741
                    }
                }
            ],
            "local_id": "2X6R0Z9mr_zQhgw_6glhAZc-dw9_iFKk"
        },
        "file": {
            "hash": {
                "md5": "596a2fe42e0af1b90e5427f706bfb745",
                "sha256": "741d139c90f3db2f790cdb31d3ed9716fd0eebd504114a0e269127f09e5b0479"
            },
            "name": "dlp - template.xlsx"
        },
        "observer": {
            "product": "ProofPoint On Demand",
            "vendor": "ProofPoint"
        },
        "proofpoint": {
            "pod": {
                "file_metadata": {
                    "appname": "Microsoft Excel Online",
                    "create_dtm": "2025-11-20 21:38:41",
                    "lastauthor": "MOMENZADEH Thomas (EXT)",
                    "lastsave_dtm": "2025-11-20 21:38:41",
                    "modified": "2025-11-20 21:38:41"
                },
                "msgpart": {
                    "id": "8ea3df61-8b18-4ec6-a0af-743321e08b50"
                },
                "urls": []
            }
        },
        "related": {
            "hash": [
                "596a2fe42e0af1b90e5427f706bfb745",
                "741d139c90f3db2f790cdb31d3ed9716fd0eebd504114a0e269127f09e5b0479"
            ]
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`email.attachments` | `nested` | List of objects describing the attachments. |
|`email.cc.address` | `keyword` | Email address of CC recipient |
|`email.from.address` | `keyword` | The sender's email address. |
|`email.local_id` | `keyword` | Unique identifier given by the source. |
|`email.message_id` | `wildcard` | Value from the Message-ID header. |
|`email.reply_to.address` | `keyword` | Address replies should be delivered to. |
|`email.subject` | `keyword` | The subject of the email message. |
|`email.to.address` | `keyword` | Email address of recipient |
|`email.x_mailer` | `keyword` | Application that drafted email. |
|`error.code` | `keyword` | Error code describing the error. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.hash.md5` | `keyword` | MD5 hash. |
|`file.hash.sha256` | `keyword` | SHA256 hash. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`network.protocol` | `keyword` | Application protocol name. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`proofpoint.pod.cluster.id` | `keyword` | The name of the cluster which processed the message |
|`proofpoint.pod.file_metadata.appname` | `keyword` |  |
|`proofpoint.pod.file_metadata.author` | `keyword` |  |
|`proofpoint.pod.file_metadata.create_dtm` | `keyword` |  |
|`proofpoint.pod.file_metadata.lastauthor` | `keyword` |  |
|`proofpoint.pod.file_metadata.lastsave_dtm` | `keyword` |  |
|`proofpoint.pod.file_metadata.modified` | `keyword` |  |
|`proofpoint.pod.file_metadata.wordcount` | `keyword` |  |
|`proofpoint.pod.modules` | `array` | The list of modules which processed the message |
|`proofpoint.pod.msgpart.id` | `keyword` | The identifier of the message part |
|`proofpoint.pod.routes` | `array` | The policy route triggered by the message |
|`proofpoint.pod.smtp.recipients` | `array` | The SMTP recipients |
|`proofpoint.pod.smtp.sender` | `keyword` | The SMTP sender |
|`proofpoint.pod.urls` | `array` | A list of urls detected in the message |
|`source.domain` | `keyword` | The domain name of the source. |
|`source.ip` | `ip` | IP address of the source. |
|`tls.cipher` | `keyword` | String indicating the cipher used during the current connection. |
|`tls.version` | `keyword` | Numeric part of the version parsed from the original string. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/ProofPoint/proofpoint-pod).