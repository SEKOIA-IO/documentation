
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Anti-virus` | Symantec Endpoint Protection analyses processes and files to prevent malicious actions. |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `intrusion_detection`, `malware`, `network`, `process` |
| Type | `` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "test_activity_logs.json"

    ```json
	
    {
        "message": "Site: OSTAM,Server Name: STR04,Domain Name: MyDomain,The client has downloaded the content package successfully,STV02,ADMIN,stv02.local",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "reason": "The client has downloaded the content package successfully",
            "type": [
                "info"
            ]
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "hostname": "STV02",
            "name": "stv02.local"
        },
        "user": {
            "name": "ADMIN"
        },
        "broadcom": {
            "endpoint_protection": {
                "server": {
                    "domain": "MyDomain",
                    "name": "STR04"
                }
            }
        },
        "related": {
            "hosts": [
                "STV02"
            ],
            "user": [
                "ADMIN"
            ]
        }
    }
    	
	```


=== "test_behavior_logs.json"

    ```json
	
    {
        "message": "INT23456,,Blocked,C:\\Program Files (x86)\\Symantec\\Symantec Endpoint Protection\\14.3.4615.2000.105\\Bin64\\ccSvcHst.exe,,Begin: 2022-08-29 11:58:20,End Time: 2022-08-29 11:58:20,Rule: ,4428,C:\\PROGRAM FILES\\SMART-X\\CONTROLUPAGENT\\VERSION 8.1.5.634\\CUAGENT.EXE,0,,C:\\Program Files (x86)\\Symantec\\Symantec Endpoint Protection\\14.3.4615.2000.105\\Bin64\\ccSvcHst.exe,User Name: Admin,Domain Name: ,Action Type: 55,File size (bytes): ,Device ID: ",
        "event": {
            "kind": "event",
            "category": [
                "process"
            ],
            "action": "Blocked",
            "start": "2022-08-29T11:58:20.000000Z",
            "type": [
                "denied"
            ]
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "hostname": "INT23456",
            "name": "INT23456"
        },
        "user": {
            "name": "Admin"
        },
        "process": {
            "pid": 4428,
            "executable": "C:\\PROGRAM FILES\\SMART-X\\CONTROLUPAGENT\\VERSION 8.1.5.634\\CUAGENT.EXE",
            "name": "CUAGENT.EXE",
            "working_directory": "C:\\PROGRAM FILES\\SMART-X\\CONTROLUPAGENT\\VERSION 8.1.5.634",
            "args": [
                "C:\\Program Files (x86)\\Symantec\\Symantec Endpoint Protection\f.3.4615.2000.105\\Bin64\\ccSvcHst.exe"
            ]
        },
        "related": {
            "hosts": [
                "INT23456"
            ],
            "user": [
                "Admin"
            ]
        }
    }
    	
	```


=== "test_control_ready.json"

    ```json
	
    {
        "message": "INT23456,1.2.3.4,Continue,Le contr\u00f4le des applications et des p\u00e9riph\u00e9riques est pr\u00eat.,Syst\u00e8me,Begin: 2022-10-19 06:45:39,End Time: 2022-10-19 06:45:39,Rule: R\u00e8gle int\u00e9gr\u00e9e,0,SysPlant,0,SysPlant,Aucun(e),User Name: Aucun(e),Domain Name: DOMAIN,Action Type: ,File size (bytes): 0,Device ID: ",
        "event": {
            "kind": "event",
            "category": [
                "process"
            ],
            "action": "Continue",
            "start": "2022-10-19T06:45:39.000000Z",
            "reason": "Le contr\u00f4le des applications et des p\u00e9riph\u00e9riques est pr\u00eat.",
            "type": [
                "info"
            ]
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "ip": [
                "1.2.3.4"
            ],
            "hostname": "INT23456",
            "name": "INT23456"
        },
        "file": {
            "size": 0
        },
        "process": {
            "pid": 0,
            "executable": "SysPlant",
            "name": "SysPlant"
        },
        "broadcom": {
            "endpoint_protection": {
                "server": {
                    "domain": "DOMAIN"
                }
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "hosts": [
                "INT23456"
            ]
        }
    }
    	
	```


=== "test_liveupdate.json"

    ```json
	
    {
        "message": "INT23456,Category: 2,LiveUpdate Manager,\"Event Description: L\u2019installation d\u2019une mise \u00e0 jour de Revocation Data a \u00e9chou\u00e9. Erreur : Echec de la correction de contenu (0xE0010005), DuResult: Succ\u00e8s (0).\",Event time: 2022-10-18 18:09:26,Group Name: MyDomain\\Servers",
        "event": {
            "kind": "event",
            "category": [
                "process"
            ],
            "reason": "L\u2019installation d\u2019une mise \u00e0 jour de Revocation Data a \u00e9chou\u00e9. Erreur : Echec de la correction de contenu (0xE0010005), DuResult: Succ\u00e8s (0).",
            "start": "2022-10-18T18:09:26.000000Z",
            "type": [
                "info"
            ]
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "hostname": "INT23456",
            "name": "INT23456"
        },
        "broadcom": {
            "endpoint_protection": {
                "source": "LiveUpdate Manager",
                "server": {
                    "group": "MyDomain\\Servers"
                }
            }
        },
        "related": {
            "hosts": [
                "INT23456"
            ]
        }
    }
    	
	```


=== "test_liveupdate_failed.json"

    ```json
	
    {
        "message": "INT23456,Category: 2,LiveUpdate Manager,\"Event Description: L\u2019installation d\u2019une mise \u00e0 jour de Virus and Spyware Definitions SDS Win64 (Reduced) a \u00e9chou\u00e9. Erreur : Echec de la correction de contenu (0xE0010005), DuResult: Succ\u00e8s (0).\",Event time: 2022-10-19 07:32:25,Group Name: MyDomain\\Servers",
        "event": {
            "kind": "event",
            "category": [
                "malware"
            ],
            "reason": "L\u2019installation d\u2019une mise \u00e0 jour de Virus and Spyware Definitions SDS Win64 (Reduced) a \u00e9chou\u00e9. Erreur : Echec de la correction de contenu (0xE0010005), DuResult: Succ\u00e8s (0).",
            "start": "2022-10-19T07:32:25.000000Z",
            "type": [
                "info"
            ]
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "hostname": "INT23456",
            "name": "INT23456"
        },
        "broadcom": {
            "endpoint_protection": {
                "source": "LiveUpdate Manager",
                "server": {
                    "group": "MyDomain\\Servers"
                }
            }
        },
        "related": {
            "hosts": [
                "INT23456"
            ]
        }
    }
    	
	```


=== "test_malicious_scan.json"

    ```json
	
    {
        "message": "INT23456,Event Description: [SID\u00a0: 32329] attaque de Audit: Malicious Scan Attempt 2 d\u00e9tect\u00e9e mais pas bloqu\u00e9e. Chemin d\u2019application\u00a0: SYSTEM,Event Type: ,Local Host IP: 1.2.3.4,Local Host MAC: 000000000000,Remote Host Name: ,Remote Host IP: 5.6.7.8,Remote Host MAC: 000000000000,Outbound,TCP,,Begin: 2022-10-19 09:25:40,End Time: 2022-10-19 09:25:40,Occurrences: 1,Application: SYSTEM,Location: Par d\u00e9faut,User Name: none,Domain Name: ,Local Port: 443,Remote Port: 14867,CIDS Signature ID: 32329,CIDS Signature string: Audit: Malicious Scan Attempt 2,CIDS Signature SubID: 68040,Intrusion URL: http://9.8.7.6:443/,Intrusion Payload URL: ,SHA-256: 0000000000000000000000000000000000000000000000000000000000000000,MD-5: ,Intensive Protection Level: N/A,URL Risk: N/A,URL Category: N/A",
        "event": {
            "kind": "event",
            "category": [
                "intrusion_detection"
            ],
            "reason": "attaque de Audit: Malicious Scan Attempt 2 d\u00e9tect\u00e9e mais pas bloqu\u00e9e. Chemin d\u2019application\u00a0: SYSTEM",
            "start": "2022-10-19T09:25:40.000000Z",
            "type": [
                "info"
            ]
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "ip": [
                "1.2.3.4"
            ],
            "hostname": "INT23456",
            "name": "INT23456"
        },
        "destination": {
            "ip": "5.6.7.8",
            "port": 14867,
            "address": "5.6.7.8"
        },
        "url": {
            "original": "http://9.8.7.6:443/",
            "domain": "9.8.7.6",
            "port": 443,
            "scheme": "http",
            "path": "/"
        },
        "network": {
            "direction": "outbound",
            "transport": "tcp"
        },
        "source": {
            "ip": "1.2.3.4",
            "port": 443,
            "address": "1.2.3.4"
        },
        "threat": {
            "enrichments": [
                {
                    "indicator": {
                        "type": "file",
                        "sightings": 1
                    }
                }
            ]
        },
        "broadcom": {
            "endpoint_protection": {
                "application": {
                    "name": "SYSTEM"
                },
                "cids": {
                    "signature": {
                        "id": 32329,
                        "label": "Audit: Malicious Scan Attempt 2",
                        "sub_id": 68040
                    }
                }
            }
        },
        "related": {
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ],
            "hosts": [
                "INT23456"
            ]
        }
    }
    	
	```


=== "test_scan.json"

    ```json
	
    {
        "message": "Scan ID: 1664847558,Begin: 2022-10-04 17:42:10,End Time: 2022-10-04 17:44:22,Completed,Duration (seconds): 132,User1: Syst\u00e8me,User2: Syst\u00e8me,Analyse lanc\u00e9e sur lecteurs et dossiers s\u00e9lectionn\u00e9s et toutes les extensions.,Analyse Installation standard : Risques : 0 Analys\u00e9s : 1553 Fichiers/Dossiers/Lecteurs omis : 0 Fichiers approuv\u00e9s ignor\u00e9s : 844,Command: Not a command scan (),Threats: 0,Infected: 0,Total files: 1553,Omitted: 0,Computer: DNHFF3453,IP Address: 1.2.3.4,Domain Name: MyDomain,Group Name: MyDomain\\Subdivision\\Citrix VDI persistants,Server Name: XXXXX01,Scan Type: DefWatch",
        "event": {
            "kind": "event",
            "category": [
                "malware"
            ],
            "reason": "Analyse lanc\u00e9e sur lecteurs et dossiers s\u00e9lectionn\u00e9s et toutes les extensions.",
            "start": "2022-10-04T17:42:10.000000Z",
            "type": [
                "info"
            ]
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "ip": [
                "1.2.3.4"
            ],
            "hostname": "DNHFF3453",
            "name": "DNHFF3453"
        },
        "user": {
            "name": "Syst\u00e8me"
        },
        "broadcom": {
            "endpoint_protection": {
                "server": {
                    "domain": "MyDomain",
                    "group": "MyDomain\\Subdivision\\Citrix VDI persistants",
                    "name": "XXXXX01"
                },
                "scan": {
                    "id": "1664847558",
                    "duration": 132,
                    "command": "Not a command scan ()",
                    "type": "DefWatch",
                    "result": {
                        "threats": 0,
                        "infections": 0,
                        "total": 1553,
                        "omitted": 0
                    },
                    "status": "completed"
                }
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "hosts": [
                "DNHFF3453"
            ],
            "user": [
                "Syst\u00e8me"
            ]
        }
    }
    	
	```


=== "test_sonar.json"

    ```json
	
    {
        "message": "SONAR detection now allowed,IP Address: 1.2.3.4,Computer name: DNHFF3453,Source: Auto-Protect scan,Risk name: WS.Reputation.1,Occurrences: 1,File path: c:\\program files (x86)\\visualxxxxxxxxxx\\vtomxvision.exe,Description: ,Actual action: Action invalid,Requested action: Process terminate pending restart,Secondary action: 102,Event time: 2022-07-07 17:01:05,Event Insert Time: 2022-07-07 17:24:14,End Time: 2022-07-07 17:01:05,Last update time: 2022-07-07 17:24:14,Domain Name: MyDomain,Group Name: MyDomain\\Subdivision\\Citrix VDI persistants,Server Name: XXXXX01,User Name: Doe,Source Computer Name: ,Source Computer IP: ,Disposition: Good,Download site: ,Web domain: ,Downloaded by: c:/windows/explorer.exe,Prevalence: This file has been seen by fewer than 50 Symantec users.,Confidence: There is some evidence that this file is trustworthy.,URL Tracking Status: On,First Seen: Symantec has known about this file approximately 2 days.,Sensitivity: ,Allowed application reason: User allow list,Application hash: E13D72DE479A65E6448C779B3B2BCE45DB7B5AE52B1BAA0FE915380A667D3C01,Hash type: SHA2,Company name: Absyss S.A.S,Application name: Visual TOM,Application version: 6.6.1 (FR),Application type: 127,File size (bytes): 67352,Category set: Malware,Category type: Insight Network Threat,Location: MyDomain,Intensive Protection Level: 0,Certificate issuer: Absyss,Certificate signer: Sectigo RSA Code Signing CA,Certificate thumbprint: D31433F4C8C0BE4846E7E90318CD0CF5046EE95C,Signing timestamp: 1649155201,Certificate serial number: 044541E287C90A879334BFD15D6A3ED3",
        "event": {
            "reason": "SONAR detection now allowed",
            "kind": "event",
            "category": [
                "process"
            ],
            "type": [
                "info"
            ],
            "action": "Process terminate pending restart"
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "ip": [
                "1.2.3.4"
            ],
            "hostname": "DNHFF3453",
            "name": "DNHFF3453"
        },
        "user": {
            "name": "Doe"
        },
        "related": {
            "hosts": [
                "DNHFF3453"
            ],
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "Doe"
            ]
        },
        "threat": {
            "enrichments": [
                {
                    "indicator": {
                        "type": "file",
                        "first_seen": "2022-07-07T17:01:05.000000Z",
                        "last_seen": "2022-07-07T17:01:05.000000Z",
                        "modified_at": "2022-07-07T17:24:14.000000Z",
                        "sightings": 1,
                        "description": "WS.Reputation.1",
                        "file": {
                            "path": "c:\\program files (x86)\\visualxxxxxxxxxx\\vtomxvision.exe",
                            "size": 67352
                        }
                    }
                }
            ]
        },
        "file": {
            "path": "c:\\program files (x86)\\visualxxxxxxxxxx\\vtomxvision.exe",
            "size": 67352
        },
        "broadcom": {
            "endpoint_protection": {
                "source": "Auto-Protect scan",
                "server": {
                    "domain": "MyDomain",
                    "group": "MyDomain\\Subdivision\\Citrix VDI persistants",
                    "name": "XXXXX01"
                },
                "threat": {
                    "type": "Insight Network Threat",
                    "category": "Malware"
                },
                "protection": {
                    "level": 0
                },
                "application": {
                    "code_signature": {
                        "digest_algorithm": "sha2",
                        "subject_name": "Absyss",
                        "signer": "Sectigo RSA Code Signing CA",
                        "timestamp": "2022-04-05T10:40:01.000000Z",
                        "certificate": {
                            "thumbprint": "D31433F4C8C0BE4846E7E90318CD0CF5046EE95C",
                            "serial_number": "044541E287C90A879334BFD15D6A3ED3"
                        }
                    },
                    "hash": {
                        "sha2": "E13D72DE479A65E6448C779B3B2BCE45DB7B5AE52B1BAA0FE915380A667D3C01"
                    },
                    "name": "Visual TOM",
                    "version": "6.6.1 (FR)"
                },
                "downloaded_by": {
                    "file": {
                        "path": "c:/windows/explorer.exe"
                    }
                },
                "action": {
                    "main": "Action invalid",
                    "secondary": "102"
                },
                "prevalence": "This file has been seen by fewer than 50 Symantec users.",
                "confidence": "There is some evidence that this file is trustworthy."
            }
        }
    }
    	
	```


=== "test_system_logs.json"

    ```json
	
    {
        "message": "OND345,Category: 2,REP,Event Description: Impossible d\u2019assigner un jeton d\u2019authentification client. Une erreur de communication g\u00e9n\u00e9rale est survenue.,Event time: 2022-08-29 11:35:29,Group Name: Company\\Own",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "reason": "Impossible d\u2019assigner un jeton d\u2019authentification client. Une erreur de communication g\u00e9n\u00e9rale est survenue.",
            "start": "2022-08-29T11:35:29.000000Z",
            "type": [
                "info"
            ]
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "hostname": "OND345",
            "name": "OND345"
        },
        "broadcom": {
            "endpoint_protection": {
                "source": "REP",
                "server": {
                    "group": "Company\\Own"
                }
            }
        },
        "related": {
            "hosts": [
                "OND345"
            ]
        }
    }
    	
	```


=== "test_virus_found.json"

    ```json
	
    {
        "message": "Virus found,IP Address: 1.2.3.4,Computer name: DNHFF3453,Source: Auto-Protect scan,Risk name: EICAR Test String,Occurrences: 1,File path: C:\\Users\\admin\\Desktop\\test.txt,Description: AP realtime deferred scanning,Actual action: Cleaned by deletion,Requested action: Cleaned,Secondary action: Quarantined,Event time: 2022-07-07 14:28:39,Event Insert Time: 2022-07-07 14:30:43,End Time: 2022-07-07 14:28:39,Last update time: 2022-07-07 14:30:43,Domain Name: MyDomain,Group Name: MyDomain\\Subdivision\\Citrix VDI persistants,Server Name: XXXXX01,User Name: ADMIN,Source Computer Name: ,Source Computer IP: ,Disposition: Bad,Download site: ,Web domain: ,Downloaded by: ,Prevalence: This file has been seen by millions of Symantec users.,Confidence: This file is untrustworthy.,URL Tracking Status: On,First Seen: Reputation was not used in this detection.,Sensitivity: ,Allowed application reason: Not on the allow list,Application hash: 275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F,Hash type: SHA2,Company name: ,Application name: Nouveau document texte.txt,Application version: ,Application type: 127,File size (bytes): 68,Category set: Malware,Category type: Virus,Location: MyDomain,Intensive Protection Level: 0,Certificate issuer: ,Certificate signer: ,Certificate thumbprint: ,Signing timestamp: ,Certificate serial number: ",
        "event": {
            "reason": "Virus found",
            "kind": "event",
            "category": [
                "malware"
            ],
            "type": [
                "info"
            ],
            "action": "Cleaned"
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "ip": [
                "1.2.3.4"
            ],
            "hostname": "DNHFF3453",
            "name": "DNHFF3453"
        },
        "user": {
            "name": "ADMIN"
        },
        "related": {
            "hosts": [
                "DNHFF3453"
            ],
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "ADMIN"
            ]
        },
        "threat": {
            "enrichments": [
                {
                    "indicator": {
                        "type": "file",
                        "first_seen": "2022-07-07T14:28:39.000000Z",
                        "last_seen": "2022-07-07T14:28:39.000000Z",
                        "modified_at": "2022-07-07T14:30:43.000000Z",
                        "sightings": 1,
                        "description": "EICAR Test String",
                        "file": {
                            "path": "C:\\Users\\admin\\Desktop\\test.txt",
                            "size": 68
                        }
                    }
                }
            ]
        },
        "file": {
            "path": "C:\\Users\\admin\\Desktop\\test.txt",
            "size": 68
        },
        "broadcom": {
            "endpoint_protection": {
                "source": "Auto-Protect scan",
                "server": {
                    "domain": "MyDomain",
                    "group": "MyDomain\\Subdivision\\Citrix VDI persistants",
                    "name": "XXXXX01"
                },
                "threat": {
                    "type": "Virus",
                    "category": "Malware"
                },
                "protection": {
                    "level": 0
                },
                "application": {
                    "code_signature": {
                        "digest_algorithm": "sha2"
                    },
                    "hash": {
                        "sha2": "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F"
                    },
                    "name": "Nouveau document texte.txt"
                },
                "action": {
                    "main": "Cleaned by deletion",
                    "secondary": "Quarantined"
                },
                "prevalence": "This file has been seen by millions of Symantec users.",
                "confidence": "This file is untrustworthy."
            }
        }
    }
    	
	```


=== "test_virus_found2.json"

    ```json
	
    {
        "message": "Virus found,IP Address: 1.2.3.4,Computer name: MyComputer,Source: Auto-Protect scan,Risk name: EICAR Test String,Occurrences: 1,File path: /tmp/eicar.txt,Description: ,Actual action: Quarantined,Requested action: Cleaned,Secondary action: Quarantined,Event time: 2022-10-04 19:10:48,Event Insert Time: 2022-10-04 19:15:22,End Time: 2022-10-04 19:10:48,Last update time: 2022-10-04 19:15:22,Domain Name: Par d\u00e9faut,Group Name: Mydomain\\\\Servers\\\\Linux,Server Name: XXXX01,User Name: user,Source Computer Name: ,Source Computer IP: ,Disposition: Reputation was not used in this detection.,Download site: ,Web domain: ,Downloaded by: ,Prevalence: Reputation was not used in this detection.,Confidence: Reputation was not used in this detection.,URL Tracking Status: N/A,First Seen: Reputation was not used in this detection.,Sensitivity: Low,Allowed application reason: Not on the allow list,Application hash: 131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267,Hash type: SHA2,Company name: ,Application name: Unknown,Application version: ,Application type: -1,File size (bytes): 69,Category set: Malware,Category type: Virus,Location: ,Intensive Protection Level: 0,Certificate issuer: ,Certificate signer: ,Certificate thumbprint: ,Signing timestamp: 0,Certificate serial number: ",
        "event": {
            "kind": "event",
            "category": [
                "malware"
            ],
            "reason": "Virus found",
            "action": "Cleaned",
            "type": [
                "info"
            ]
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "ip": [
                "1.2.3.4"
            ],
            "hostname": "MyComputer",
            "name": "MyComputer"
        },
        "user": {
            "name": "user"
        },
        "file": {
            "path": "/tmp/eicar.txt",
            "size": 69
        },
        "threat": {
            "enrichments": [
                {
                    "indicator": {
                        "type": "file",
                        "first_seen": "2022-10-04T19:10:48.000000Z",
                        "last_seen": "2022-10-04T19:10:48.000000Z",
                        "modified_at": "2022-10-04T19:15:22.000000Z",
                        "sightings": 1,
                        "description": "EICAR Test String",
                        "file": {
                            "path": "/tmp/eicar.txt",
                            "size": 69
                        }
                    }
                }
            ]
        },
        "broadcom": {
            "endpoint_protection": {
                "source": "Auto-Protect scan",
                "server": {
                    "domain": "Par d\u00e9faut",
                    "group": "Mydomain\\\\Servers\\\\Linux",
                    "name": "XXXX01"
                },
                "application": {
                    "hash": {
                        "sha2": "131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267"
                    },
                    "name": "Unknown",
                    "code_signature": {
                        "digest_algorithm": "sha2",
                        "timestamp": "1970-01-01T00:00:00.000000Z"
                    }
                },
                "protection": {
                    "level": 0
                },
                "action": {
                    "main": "Quarantined",
                    "secondary": "Quarantined"
                },
                "prevalence": "Reputation was not used in this detection.",
                "confidence": "Reputation was not used in this detection.",
                "threat": {
                    "type": "Virus",
                    "category": "Malware"
                }
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "hosts": [
                "MyComputer"
            ],
            "user": [
                "user"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`broadcom.endpoint_protection.action.main` | `keyword` |  |
|`broadcom.endpoint_protection.action.secondary` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.certificate.serial_number` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.certificate.thumbprint` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.digest_algorithm` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.signer` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.subject_name` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.timestamp` | `keyword` |  |
|`broadcom.endpoint_protection.application.hash.sha2` | `keyword` |  |
|`broadcom.endpoint_protection.application.name` | `keyword` |  |
|`broadcom.endpoint_protection.application.version` | `keyword` |  |
|`broadcom.endpoint_protection.cids.signature.id` | `number` | The identifier of the CIDS sgnature |
|`broadcom.endpoint_protection.cids.signature.label` | `string` | The label of the CIDS sgnature |
|`broadcom.endpoint_protection.cids.signature.sub_id` | `number` | The sub-identifier of the CIDS sgnature |
|`broadcom.endpoint_protection.confidence` | `keyword` |  |
|`broadcom.endpoint_protection.downloaded_by.file.path` | `keyword` |  |
|`broadcom.endpoint_protection.prevalence` | `keyword` |  |
|`broadcom.endpoint_protection.protection.level` | `number` | The level of intensve protection |
|`broadcom.endpoint_protection.scan.command` | `keyword` | The command scan |
|`broadcom.endpoint_protection.scan.duration` | `number` | The duration of the scan in seconds |
|`broadcom.endpoint_protection.scan.id` | `keyword` | The identifier of the scan |
|`broadcom.endpoint_protection.scan.result.infections` | `number` | The number of infected files |
|`broadcom.endpoint_protection.scan.result.omitted` | `number` | The number of omitted files |
|`broadcom.endpoint_protection.scan.result.threats` | `number` | The number of detected threats |
|`broadcom.endpoint_protection.scan.result.total` | `number` | The number of total files scanned |
|`broadcom.endpoint_protection.scan.status` | `keyword` | The status of the scan |
|`broadcom.endpoint_protection.scan.type` | `keyword` | The type of scan |
|`broadcom.endpoint_protection.server.domain` | `keyword` |  |
|`broadcom.endpoint_protection.server.group` | `keyword` |  |
|`broadcom.endpoint_protection.server.name` | `keyword` |  |
|`broadcom.endpoint_protection.source` | `keyword` |  |
|`broadcom.endpoint_protection.threat.category` | `keyword` |  |
|`broadcom.endpoint_protection.threat.payload` | `string` | The url of the intrusion payload |
|`broadcom.endpoint_protection.threat.risk` | `string` | The risk associated to the intrusion url |
|`broadcom.endpoint_protection.threat.type` | `keyword` |  |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.mac` | `keyword` | MAC address of the destination. |
|`destination.port` | `long` | Port of the destination. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.end` | `date` | event.end contains the date when the event ended or when the activity was last observed. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`file.hash.md5` | `keyword` | MD5 hash. |
|`file.hash.sha256` | `keyword` | SHA256 hash. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`file.size` | `long` | File size in bytes. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.ip` | `ip` | Host ip addresses. |
|`host.mac` | `keyword` | Host MAC addresses. |
|`host.name` | `keyword` | Name of the host. |
|`network.direction` | `keyword` | Direction of the network traffic. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`process.args` | `keyword` | Array of process arguments. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.name` | `keyword` | Process name. |
|`process.pid` | `long` | Process id. |
|`process.working_directory` | `keyword` | The working directory of the process. |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`threat.enrichments` | `array` |  |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.name` | `keyword` | Short name or login of the user. |

