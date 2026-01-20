
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_maillog"


    ```json
	{
        "data": "2022-08-25T17:06:21.935763-07:00 m0169160 sendmail[22003]: 27PNO8ta032355: to=REDACTED, ctladdr=<user@example.org> (8/0), delay=00:00:00, xdelay=00:00:00, mailer=*file*, tls_verify=NONE, tls_version=NONE, cipher=NONE, pri=32434, dsn=2.0.0, stat=Sent",
        "tls": {
            "version": "NONE",
            "verify": "NONE",
            "cipher": "NONE"
        },
        "sm": {
            "delay": "00:00:00",
            "to": [
                "REDACTED"
            ],
            "pri": "32434",
            "dsn": "2.0.0",
            "ctladdr": "<user@example.org> (8/0)",
            "qid": "27PNO8ta032355",
            "xdelay": "00:00:00",
            "stat": "Sent",
            "mailer": "*file*"
        },
        "pps": {
            "cid": "proofpointdemo_cloudadminuidemo_hosted",
            "agent": "m0169160.ppops.net"
        },
        "ts": "2022-08-25T17:06:21.935763-0700",
        "id": "41K7tSNsqcyiZCuOX1wmnQ",
        "metadata": {
            "origin": {
                "schemaVersion": "20200420",
                "data": {
                    "cid": "proofpointdemo_cloudadminuidemo_hosted",
                    "agent": "m0169160.ppops.net"
                }
            },
            "customerId": "6ae809da-7151-354f-8d3c-40fe90ec6eca"
        },
        "type": "maillog"
    }
    ```



=== "test_message"


    ```json
	{
        "connection": {
            "protocol": "smtp:smtp",
            "ip": "1.2.3.4",
            "host": "n35.grp.scd.example.com",
            "sid": "3j6jew035h",
            "resolveStatus": "ok",
            "helo": "n35.grp.scd.example.com",
            "country": "us"
        },
        "filter": {
            "delivered": {
                "rcpts": [
                    "amartinez@thopedia.com"
                ]
            },
            "qid": "27Q0O7ss000303",
            "modules": {
                "spam": {
                    "version": {
                        "definitions": "main-2208250092",
                        "engine": "8.19.0-2204280000"
                    },
                    "langs": [
                        "en",
                        "pt",
                        "es"
                    ],
                    "scores": {
                        "classifiers": {
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
                        },
                        "overall": 0,
                        "engine": 0
                    }
                }
            },
            "routes": [
                "allow_relay",
                "firewallsafe",
                "internalnet",
                "outbound"
            ],
            "durationSecs": 0.169678,
            "suborgs": {
                "sender": "0",
                "rcpts": [
                    "0"
                ]
            },
            "verified": {
                "rcpts": [
                    "amartinez@thopedia.com"
                ]
            },
            "disposition": "continue",
            "actions": [
                {
                    "module": "av",
                    "rule": "clean",
                    "action": "add-header"
                },
                {
                    "module": "av",
                    "isFinal": true,
                    "action": "continue",
                    "rule": "clean"
                },
                {
                    "module": "spam",
                    "action": "add-header",
                    "rule": "notspam"
                }
            ],
            "msgSizeBytes": 4857,
            "routeDirection": "outbound"
        },
        "guid": "rkuzwIede_tYDQ-P7qUoNlwm6Hz3u1R5",
        "msg": {
            "header": {
                "return-path": [
                    "<sentto-4328378-18698-1074787260-gboja=proofpoint.com@returns.groups.yahoo.com>"
                ],
                "to": [
                    "\"wmoms\" <user2@example.org>"
                ],
                "message-id": [
                    "<111111111111111111111@example.com>"
                ],
                "from": [
                    "\"Schweigert, Wendy\" <user1@example.com>"
                ],
                "reply-to": [
                    "user2@example.org"
                ],
                "subject": [
                    "REDACTED"
                ]
            },
            "sizeBytes": 4275,
            "normalizedHeader": {
                "subject": [
                    "REDACTED"
                ],
                "reply-to": [
                    "user2@example.org"
                ],
                "to": [
                    "\"wmoms\" <user2@example.org>"
                ],
                "message-id": [
                    "111111111111111111111@example.com"
                ],
                "from": [
                    "\"Schweigert, Wendy\" <user1@example.com>"
                ],
                "return-path": [
                    "<sentto-4328378-18698-1074787260-gboja=proofpoint.com@returns.groups.yahoo.com>"
                ]
            },
            "parsedAddresses": {
                "from": [
                    "user1@example.com"
                ],
                "to": [
                    "user2@example.org"
                ],
                "reply-to": [
                    "user2@example.org"
                ],
                "fromDisplayNames": [
                    "Schweigert, Wendy"
                ]
            },
            "lang": "en"
        },
        "ts": "2022-08-25T17:25:21.071953-0700",
        "metadata": {
            "origin": {
                "data": {
                    "agent": "m0169160.ppops.net",
                    "version": "8.19.0.1216",
                    "cid": "proofpointdemo_cloudadminuidemo_hosted"
                }
            }
        },
        "envelope": {
            "rcpts": [
                "amartinez@thopedia.com"
            ],
            "from": "kpereira@cloudadminuidemo.com"
        },
        "type": "message"
    }
    ```



=== "test_message2"


    ```json
	{
        "metadata": {
            "origin": {
                "data": {
                    "cid": "proofpointdemo_cloudadminuidemo_hosted",
                    "agent": "m0169161.ppops.net",
                    "version": "8.19.0.1216"
                }
            }
        },
        "ts": "2022-09-11T18:28:19.902627-0700",
        "envelope": {
            "from": "user1@example.net",
            "rcpts": [
                "ceo@exec.vogon.science"
            ]
        },
        "connection": {
            "host": "1-2-3-4.example.com",
            "ip": "5.6.7.8",
            "sid": "3jgptm9dux",
            "tls": {
                "inbound": {
                    "version": "TLSv1.2",
                    "cipherBits": 256,
                    "cipher": "ECDHE-RSA-AES256-GCM-SHA384"
                }
            },
            "country": "us",
            "protocol": "smtp:smtp",
            "resolveStatus": "ok",
            "helo": "selabfork.ppslab.net"
        },
        "msg": {
            "lang": "ja",
            "normalizedHeader": {
                "to": [
                    "<user2@example.org>"
                ],
                "subject": [
                    "ANONYMIZED"
                ],
                "message-id": [
                    "20220912092800466772@example.net"
                ],
                "x-mailer": [
                    "Xwstoxzpk 1"
                ],
                "from": [
                    "\"Amazon\" <user1@example.net>"
                ]
            },
            "parsedAddresses": {
                "fromDisplayNames": [
                    "Amazon"
                ],
                "from": [
                    "user1@example.net"
                ],
                "to": [
                    "user2@example.org"
                ]
            },
            "header": {
                "from": [
                    "\"Amazon\" <user1@example.net>"
                ],
                "message-id": [
                    "<20220912092800466772@example.net>"
                ],
                "x-mailer": [
                    "Xwstoxzpk 1"
                ],
                "subject": [
                    "REDACTED"
                ],
                "to": [
                    "<user2@example.org>"
                ]
            },
            "sizeBytes": 33366
        },
        "filter": {
            "actions": [
                {
                    "rule": "clean",
                    "action": "add-header",
                    "module": "av"
                },
                {
                    "rule": "clean",
                    "action": "continue",
                    "module": "av"
                },
                {
                    "action": "add-header",
                    "module": "spam",
                    "rule": "phish"
                },
                {
                    "rule": "phish",
                    "action": "copy",
                    "module": "spam"
                },
                {
                    "rule": "phish",
                    "module": "spam",
                    "action": "quarantine"
                },
                {
                    "module": "spam",
                    "action": "discard",
                    "rule": "phish",
                    "isFinal": true
                }
            ],
            "modules": {
                "urldefense": {
                    "counts": {
                        "total": 5,
                        "unique": 2,
                        "rewritten": 5
                    },
                    "version": {
                        "engine": "15"
                    }
                },
                "spam": {
                    "langs": [
                        "en",
                        "jp",
                        "pt"
                    ],
                    "triggeredClassifier": "phish",
                    "scores": {
                        "overall": 100,
                        "engine": 100,
                        "classifiers": {
                            "adult": 0,
                            "mlx": 100,
                            "impostor": 0,
                            "spam": 100,
                            "malware": 0,
                            "mlxlog": -1000,
                            "phish": 100,
                            "suspect": 0,
                            "lowpriority": 0,
                            "bulk": 0
                        }
                    },
                    "version": {
                        "definitions": "main-2209120003",
                        "engine": "8.19.0-2204280000"
                    }
                },
                "spf": {
                    "domain": "example.net",
                    "result": "none"
                },
                "dmarc": {
                    "records": [
                        {
                            "error": "NXDOMAIN",
                            "query": "_dmarc.example.net"
                        }
                    ],
                    "filterdResult": "none",
                    "authResults": [
                        {
                            "method": "spf",
                            "emailIdentities": {
                                "smtp.mailfrom": "user1@example.net"
                            },
                            "result": "none"
                        },
                        {
                            "method": "dmarc",
                            "result": "none"
                        }
                    ],
                    "srvid": "ppops.net"
                }
            },
            "suborgs": {
                "sender": "0",
                "rcpts": [
                    "0"
                ]
            },
            "isMsgInDigest": true,
            "routeDirection": "internal",
            "verified": {
                "rcpts": [
                    "ceo@exec.vogon.science"
                ]
            },
            "msgSizeBytes": 33278,
            "routes": [
                "allow_relay",
                "default_inbound",
                "firewallsafe",
                "internalnet"
            ],
            "durationSecs": 0.356614,
            "delivered": {
                "rcpts": [
                    "ceo@exec.vogon.science"
                ]
            },
            "disposition": "discard",
            "qid": "3jgptm9dux-1",
            "quarantine": {
                "module": "spam",
                "folderId": "phish",
                "type": "quarantine",
                "folder": "Phish",
                "rule": "phish"
            }
        },
        "guid": "5PVdahx3PMGFONShVUQ19uni34-uVQRm",
        "type": "message"
    }
    ```



=== "test_message3"


    ```json
	{
        "connection": {
            "resolveStatus": "[unknown]",
            "host": "hostname",
            "country": "**",
            "ip": "127.0.0.1",
            "helo": "outbound.proofpointdemo",
            "protocol": "smtp:smtp",
            "sid": "3jryreg677"
        },
        "ts": "2022-09-22T17:06:53.370514-0700",
        "metadata": {
            "origin": {
                "data": {
                    "agent": "m0169160.ppops.net",
                    "cid": "proofpointdemo_cloudadminuidemo_hosted",
                    "version": "8.19.0.1216"
                }
            }
        },
        "msg": {
            "header": {
                "message-id": [
                    "<user11@example.net>"
                ],
                "subject": [
                    ""
                ]
            },
            "lang": "und",
            "parsedAddresses": {},
            "normalizedHeader": {
                "message-id": [
                    "user11@example.net"
                ],
                "subject": [
                    ""
                ]
            },
            "sizeBytes": 203
        },
        "envelope": {
            "from": "user3@example.org",
            "rcpts": [
                "user2@example.net"
            ]
        },
        "guid": "xjin0zM1KZbSWy8mUJvOxTV7WqFRrbd1",
        "filter": {
            "durationSecs": 0.096616,
            "disposition": "continue",
            "suborgs": {
                "rcpts": [
                    "0"
                ],
                "sender": "0"
            },
            "routeDirection": "outbound",
            "msgSizeBytes": 728,
            "modules": {
                "spam": {
                    "langs": [
                        "en"
                    ],
                    "scores": {
                        "overall": 40,
                        "engine": 40,
                        "classifiers": {
                            "lowpriority": 4,
                            "mlxlog": 18,
                            "suspect": 0,
                            "adult": 8,
                            "spam": 40,
                            "malware": 0,
                            "phish": 1,
                            "bulk": 4,
                            "impostor": 0,
                            "mlx": 40
                        }
                    },
                    "version": {
                        "definitions": "main-2209220155",
                        "engine": "8.19.0-2209130001"
                    }
                }
            },
            "verified": {
                "rcpts": [
                    "user2@example.net"
                ]
            },
            "routes": [
                "allow_relay",
                "firewallsafe",
                "internalnet",
                "outbound"
            ],
            "actions": [
                {
                    "module": "av",
                    "action": "add-header",
                    "rule": "clean"
                },
                {
                    "module": "av",
                    "action": "continue",
                    "rule": "clean",
                    "isFinal": true
                },
                {
                    "module": "spam",
                    "action": "add-header",
                    "rule": "notspam"
                }
            ],
            "delivered": {
                "rcpts": [
                    "user2@example.net"
                ]
            },
            "qid": "28MNsFLm006936"
        },
        "type": "message"
    }
    ```



=== "test_msgpart_url"


    ```json
	{
        "guid": "1234567890",
        "ts": "2023-04-12T06:00:05.289102-0700",
        "type": "msgPartsUrl",
        "part_uuid": "607330be-4eb6-4f6e-9f74-0cbcab2e1ad4",
        "url": "http://www.example.org/",
        "src": [
            "filter"
        ],
        "disposition": "continue"
    }
    ```



=== "test_msgparts"


    ```json
	{
        "msgParts": {
            "structureId": "0",
            "isVirtual": false,
            "labeledName": "text.html",
            "isCorrupted": false,
            "md5": "f3226e81da52c0cb05d4a7599827b70c",
            "disposition": "inline",
            "detectedSizeBytes": 2118,
            "detectedExt": "HTML",
            "detectedMime": "text/html",
            "labeledMime": "text/html",
            "textExtracted": "U0NBTEFSKDB4N2YxMDhhNzQ3ZDM4KQ==n",
            "isTimedOut": false,
            "isDeleted": false,
            "isArchive": false,
            "sizeDecodedBytes": 2118,
            "detectedName": "text.html",
            "labeledCharset": "US-ASCII",
            "labeledExt": "html",
            "dataBase64": "U0NBTEFSKDB4N2YxMDVlMzNmNzA4KQ==n",
            "metadata": {},
            "detectedCharset": "US-ASCII",
            "isProtected": false,
            "urls": [
                {
                    "url": "http://us.adserver.example.com/?REDACTED",
                    "src": [
                        "filter"
                    ]
                },
                {
                    "url": "http://servedby.advertising.com/site=552006/size=300250/bnum=1074787264333730/bins=1/rich=0",
                    "src": [
                        "filter"
                    ]
                },
                {
                    "url": "http://docs.yahoo.com/info/terms/",
                    "src": [
                        "filter"
                    ]
                },
                {
                    "url": "http://groups.yahoo.com/group/wmoms/",
                    "src": [
                        "filter"
                    ]
                },
                {
                    "src": [
                        "filter"
                    ],
                    "url": "http://rd.yahoo.com/SIG=12co2at1q/M=243273.4326031.5516772.1261774/D=egroupweb/S=1705042054:HM/EXP=1074873664/A=1750744/R=0/*http://servedby.advertising.com/click/site=552006/bnum=1074787264333730"
                },
                {
                    "src": [
                        "filter"
                    ],
                    "url": "mailto:wmoms-unsubscribe@yahoogroups.com?subject=Unsubscribe"
                }
            ],
            "sha256": "3b9778951a276e13059b1d2254cc93ab9744b6e71081c29918ba20ccaa80db9d"
        },
        "type": "msgParts",
        "guid": "1234567890",
        "uuid": "eb99b626-c278-4af3-96f8-5a194e016a43",
        "disposition": "continue"
    }
    ```



=== "test_msgparts_metadata"


    ```json
	{
        "msgParts": {
            "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
            "labeledName": "dlp - template.xlsx",
            "isTimedOut": false,
            "isDeleted": false,
            "detectedName": "dlp - template.xlsx",
            "detectedExt": "XLSX",
            "detectedCharset": "",
            "textExtracted": "dGVzdA==\n",
            "metadata": {
                "codepage": 65001,
                "create_dtm": "2025-11-20 21:38:41",
                "modified": "2025-11-20 21:38:41",
                "lastauthor": "DOE John (EXT)",
                "appversion": "16.0300",
                "application": "Microsoft Excel Online",
                "created": "2025-11-20 21:38:41",
                "appname": "Microsoft Excel Online",
                "lastsave_dtm": "2025-11-20 21:38:41"
            },
            "isArchive": false,
            "labeledExt": "xlsx",
            "isCorrupted": false,
            "dataBase64": "dGVzdA==\n",
            "structureId": "1",
            "labeledCharset": "",
            "sizeDecodedBytes": 23741,
            "detectedMime": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "detectedSizeBytes": 23741,
            "isProtected": false,
            "isVirtual": false,
            "disposition": "attached",
            "labeledMime": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "md5": "68b329da9893e34099c7d8ad5cb9c940"
        },
        "guid": "REDACTED",
        "type": "msgParts",
        "ts": "2025-11-20T21:39:14.304430+0000",
        "uuid": "11111111-1111-1111-1111-111111111111",
        "disposition": "continue"
    }
    ```



