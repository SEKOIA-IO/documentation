
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `File monitoring` | Monitor files and devices activities |
| `Process monitoring` | Monitor process activities |
| `Process use of network` | Monitor network activities |
| `Anti-virus` | Analyse processes and files to prevent malicious actions |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `alert`, `event` |
| Category | `` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "test_antivirus_alert.json"

    ```json
	
    {
        "message": "{\n  \"rflId\": 1,\n  \"time\": \"2022-10-28T12:03:08.954602+00:00\",\n  \"lvl\": 4,\n  \"module\": \"das\",\n  \"eventName\": \"antivirusAlert\",\n  \"ipSrc\": \"1.2.3.4\",\n  \"ipDst\": \"5.6.7.8\",\n  \"egKBId\": 130161020000004,\n  \"domain__\": \"example.org\",\n  \"location\": \"Task: \\\\Microsoft\\\\Windows\\\\InstallService\\\\ScanForUpdates\",\n  \"atime\": \"2022-10-28T06:47:03.009122+00:00\",\n  \"sha256\": \"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\",\n  \"pid\": null,\n  \"description\": \"Antivirus detection: 1/65 (1%)\\nAutostart entry\",\n  \"username\": null,\n  \"hostname__\": \"MR11111\",\n  \"os_architecture__\": \"x86_64\",\n  \"os_release__\": \"10\",\n  \"hash_last_update\": \"2022-10-27T14:45:12.038340+00:00\",\n  \"tags\": \"\",\n  \"cmdline\": \"C:\\\\Windows\\\\System32\\\\InstallServiceTasks.dll\",\n  \"uid\": \"a262506e-3c9e-4afe-9233-f2335167ea86;windows;MR11111;example.org\",\n  \"total\": 65,\n  \"ppid\": null,\n  \"ctime\": \"2021-09-13T07:11:02.365029+00:00\",\n  \"os__\": \"windows\",\n  \"os_version__\": \"10.0.19041\",\n  \"positives\": 1,\n  \"os_server__\": false,\n  \"pCreateDatetime\": null,\n  \"uuid__\": \"a262506e-3c9e-4afe-9233-f2335167ea86\",\n  \"path\": \"C:\\\\WINDOWS\\\\System32\\\\InstallServiceTasks.dll\",\n  \"tag\": \"TRI_AAA_WIN\",\n  \"mtime\": \"2021-09-13T07:11:02.349390+00:00\",\n  \"id\": 999999999\n}\n",
        "event": {
            "kind": "alert",
            "reason": "Antivirus detection: 1/65 (1%)\nAutostart entry",
            "module": "das",
            "severity": 4,
            "type": [
                "info"
            ],
            "code": "130161020000004",
            "category": [
                "malware"
            ]
        },
        "@timestamp": "2022-10-28T12:03:08.954602Z",
        "agent": {
            "id": "a262506e-3c9e-4afe-9233-f2335167ea86"
        },
        "observer": {
            "type": "sensor",
            "vendor": "Tehtris",
            "product": "Tehtris EDR"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "address": "5.6.7.8"
        },
        "host": {
            "domain": "example.org",
            "hostname": "MR11111",
            "os": {
                "platform": "windows",
                "version": "10.0.19041"
            },
            "name": "MR11111"
        },
        "user": {
            "id": "a262506e-3c9e-4afe-9233-f2335167ea86;windows;MR11111;example.org"
        },
        "file": {
            "hash": {
                "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            }
        },
        "process": {
            "command_line": "C:\\Windows\\System32\\InstallServiceTasks.dll",
            "executable": "C:\\WINDOWS\\System32\\InstallServiceTasks.dll",
            "name": "InstallServiceTasks.dll"
        },
        "tehtris": {
            "edr": {
                "event": {
                    "id": "999999999",
                    "appliance": {
                        "id": "1"
                    },
                    "egKBId": "130161020000004",
                    "tag": "TRI_AAA_WIN",
                    "type": "antivirusAlert",
                    "location": "Task: \\Microsoft\\Windows\\InstallService\\ScanForUpdates"
                },
                "host": {
                    "os": {
                        "release": "10",
                        "architecture": "x86_64"
                    },
                    "is_server": false
                }
            }
        },
        "related": {
            "hash": [
                "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            ],
            "hosts": [
                "MR11111"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        }
    }
    	
	```


=== "test_heuristic_alert.json"

    ```json
	
    {
        "message": "{\n  \"rflId\": 1,\n  \"time\": \"2022-10-28T11:58:20.377350+00:00\",\n  \"lvl\": 5,\n  \"module\": \"das\",\n  \"eventName\": \"HeuristicAlert\",\n  \"ipSrc\": \"1.2.3.4\",\n  \"ipDst\": \"5.6.7.8\",\n  \"egKBId\": 130181011000003,\n  \"ppid\": 14172,\n  \"os_architecture__\": \"x86_64\",\n  \"description\": \"Suspect spawn tree detected\\n\u2500 (EXAMPLE-NT\\\\doe-j) C:\\\\Program Files (x86)\\\\Microsoft\\\\Edge\\\\Application\\\\msedge.exe (14172)\\n\u2500\u2500 (EXAMPLE-NT\\\\doe-j) C:\\\\Windows\\\\System32\\\\cmd.exe (10544)\\n\\nNo remediation taken\",\n  \"os_version__\": \"10.0.19041\",\n  \"pCreateDatetime\": \"2022-10-28T11:45:14.751830+00:00\",\n  \"path\": \"C:\\\\Windows\\\\System32\\\\cmd.exe\",\n  \"os_server__\": false,\n  \"os__\": \"windows\",\n  \"domain__\": \"example.org\",\n  \"sha256\": \"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\",\n  \"uuid__\": \"5c3ff0bc-5101-4152-a330-923e569c9229\",\n  \"os_release__\": \"10\",\n  \"username\": \"EXAMPLE-NT\\\\doe-j\",\n  \"cmdline\": \"C:\\\\WINDOWS\\\\system32\\\\cmd.exe /d /c \\\"C:\\\\Users\\\\doe-j\\\\AppData\\\\Local\\\\Programs\\\\Fake Company\\\\program.exe\\\" chrome-extension://aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ --parent-window=0 < \\\\\\\\.\\\\pipe\\\\LOCAL\\\\1111111111111111111111111111111111111111 > \\\\\\\\.\\\\pipe\\\\LOCAL\\\\11111111111111111111111111111111111111111\",\n  \"location\": \"\",\n  \"hostname__\": \"MR11111\",\n  \"uid\": \"5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org\",\n  \"tag\": \"TRI_AAA_WIN\",\n  \"pid\": 10544,\n  \"id\": 888888888\n}\n",
        "event": {
            "kind": "alert",
            "reason": "Suspect spawn tree detected\n\u2500 (EXAMPLE-NT\\doe-j) C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe (14172)\n\u2500\u2500 (EXAMPLE-NT\\doe-j) C:\\Windows\\System32\\cmd.exe (10544)\n\nNo remediation taken",
            "module": "das",
            "severity": 5,
            "type": [
                "info"
            ],
            "code": "130181011000003",
            "category": [
                "process"
            ]
        },
        "@timestamp": "2022-10-28T11:58:20.377350Z",
        "agent": {
            "id": "5c3ff0bc-5101-4152-a330-923e569c9229"
        },
        "observer": {
            "type": "sensor",
            "vendor": "Tehtris",
            "product": "Tehtris EDR"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "address": "5.6.7.8"
        },
        "host": {
            "domain": "example.org",
            "hostname": "MR11111",
            "os": {
                "platform": "windows",
                "version": "10.0.19041"
            },
            "name": "MR11111"
        },
        "user": {
            "name": "doe-j",
            "id": "5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org",
            "domain": "EXAMPLE-NT"
        },
        "file": {
            "hash": {
                "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            }
        },
        "process": {
            "pid": 10544,
            "command_line": "C:\\WINDOWS\\system32\\cmd.exe /d /c \"C:\\Users\\doe-j\\AppData\\Local\\Programs\\Fake Company\\program.exe\" chrome-extension://aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ --parent-window=0 < \\\\.\\pipe\\LOCAL\\1111111111111111111111111111111111111111 > \\\\.\\pipe\\LOCAL\\11111111111111111111111111111111111111111",
            "parent": {
                "pid": 14172
            },
            "executable": "C:\\Windows\\System32\\cmd.exe",
            "name": "cmd.exe"
        },
        "tehtris": {
            "edr": {
                "event": {
                    "id": "888888888",
                    "appliance": {
                        "id": "1"
                    },
                    "egKBId": "130181011000003",
                    "tag": "TRI_AAA_WIN",
                    "type": "HeuristicAlert"
                },
                "host": {
                    "os": {
                        "release": "10",
                        "architecture": "x86_64"
                    },
                    "is_server": false
                }
            }
        },
        "related": {
            "hash": [
                "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            ],
            "hosts": [
                "MR11111"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ],
            "user": [
                "doe-j"
            ]
        }
    }
    	
	```


=== "test_oletools.json"

    ```json
	
    {
        "message": "{\n  \"rflId\": 1,\n  \"time\": \"2022-10-28T15:23:27.128665+00:00\",\n  \"lvl\": 5,\n  \"module\": \"das\",\n  \"eventName\": \"oletools\",\n  \"ipSrc\": \"1.2.3.4\",\n  \"ipDst\": \"5.6.7.8\",\n  \"egKBId\": 130181040000001,\n  \"domain__\": \"example.org\",\n  \"uid\": \"5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org\",\n  \"sha256\": \"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\",\n  \"os__\": \"windows\",\n  \"maliciousMacro\": null,\n  \"firstTimeMacro\": null,\n  \"unknownMacro\": null,\n  \"description\": \"URLs detected in a document file\\n\\nRemediation: no remediation taken\\n\\nSuspicious URLs:\\n- http://www.google.com\",\n  \"os_version__\": \"10.0.19041\",\n  \"os_architecture__\": \"x86_64\",\n  \"os_server__\": false,\n  \"hostname__\": \"MR11111\",\n  \"uuid__\": \"5c3ff0bc-5101-4152-a330-923e569c9229\",\n  \"os_release__\": \"10\",\n  \"path\": \"C:\\\\Users\\\\doe-j\\\\AppData\\\\Local\\\\Microsoft\\\\Windows\\\\INetCache\\\\Content.Outlook\\\\AAAAA\\\\suspicious.docx\",\n  \"tag\": \"TRI_AAA_WIN\",\n  \"report\": \"\",\n  \"id\": 555555555\n}\n",
        "event": {
            "kind": "event",
            "reason": "URLs detected in a document file\n\nRemediation: no remediation taken\n\nSuspicious URLs:\n- http://www.google.com",
            "module": "das",
            "severity": 5,
            "type": [
                "info"
            ],
            "code": "130181040000001",
            "category": [
                "process"
            ]
        },
        "@timestamp": "2022-10-28T15:23:27.128665Z",
        "agent": {
            "id": "5c3ff0bc-5101-4152-a330-923e569c9229"
        },
        "observer": {
            "type": "sensor",
            "vendor": "Tehtris",
            "product": "Tehtris EDR"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "address": "5.6.7.8"
        },
        "host": {
            "domain": "example.org",
            "hostname": "MR11111",
            "os": {
                "platform": "windows",
                "version": "10.0.19041"
            },
            "name": "MR11111"
        },
        "user": {
            "id": "5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org"
        },
        "file": {
            "path": "C:\\Users\\doe-j\\AppData\\Local\\Microsoft\\Windows\\INetCache\\Content.Outlook\\AAAAA\\suspicious.docx",
            "name": "suspicious.docx",
            "directory": "C:\\Users\\doe-j\\AppData\\Local\\Microsoft\\Windows\\INetCache\\Content.Outlook\\AAAAA",
            "hash": {
                "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            }
        },
        "url": {
            "original": "http://www.google.com",
            "domain": "www.google.com",
            "top_level_domain": "com",
            "subdomain": "www",
            "registered_domain": "google.com",
            "scheme": "http",
            "port": 80
        },
        "tehtris": {
            "edr": {
                "event": {
                    "id": "555555555",
                    "appliance": {
                        "id": "1"
                    },
                    "egKBId": "130181040000001",
                    "tag": "TRI_AAA_WIN",
                    "type": "oletools",
                    "remediation_status": "no remediation taken"
                },
                "host": {
                    "os": {
                        "release": "10",
                        "architecture": "x86_64"
                    },
                    "is_server": false
                }
            }
        },
        "related": {
            "hash": [
                "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            ],
            "hosts": [
                "MR11111"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        }
    }
    	
	```


=== "test_oletools2.json"

    ```json
	
    {
        "message": "{\n  \"rflId\": 1,\n  \"time\": \"2022-11-02T08:13:10.566734+00:00\",\n  \"lvl\": 6,\n  \"module\": \"das\",\n  \"eventName\": \"oletools\",\n  \"ipSrc\": \"1.2.3.4\",\n  \"ipDst\": \"5.6.7.8\",\n  \"egKBId\": 130181041000003,\n  \"os_server__\": false,\n  \"tag\": \"TRI_AAA_WIN\",\n  \"report\": \"Document file sha256: 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\",\n  \"uid\": \"5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org\",\n  \"sha256\": \"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\",\n  \"hostname__\": \"MR11111\",\n  \"maliciousMacro\": 1,\n  \"os__\": \"windows\",\n  \"domain__\": \"example.org\",\n  \"os_version__\": \"10.0.19041\",\n  \"uuid__\": \"5c3ff0bc-5101-4152-a330-923e569c9229\",\n  \"description\": \"Potential malicious VBA code detected in a document file\\n- Suspicious macros detected (1)\\n\\nRemediation: no remediation taken\\n\\nBehaviors:\\n- Suspicious | May run PowerShell commands\\n\\nSuspicious macros sha1:\\n- adc83b19e793491b1c6ea0fd8b46cd9f32e592fc\",\n  \"os_release__\": \"10\",\n  \"os_architecture__\": \"x86_64\",\n  \"firstTimeMacro\": 0,\n  \"unknownMacro\": 28,\n  \"path\": \"C:\\\\Users\\\\doe-j\\\\AppData\\\\Local\\\\Analysis\\\\FUNCRES.XLAM\",\n  \"id\": 837562963\n}\n",
        "event": {
            "kind": "event",
            "reason": "Potential malicious VBA code detected in a document file\n- Suspicious macros detected (1)\n\nRemediation: no remediation taken\n\nBehaviors:\n- Suspicious | May run PowerShell commands\n\nSuspicious macros sha1:\n- adc83b19e793491b1c6ea0fd8b46cd9f32e592fc",
            "module": "das",
            "severity": 6,
            "type": [
                "info"
            ],
            "code": "130181041000003",
            "category": [
                "process"
            ]
        },
        "@timestamp": "2022-11-02T08:13:10.566734Z",
        "agent": {
            "id": "5c3ff0bc-5101-4152-a330-923e569c9229"
        },
        "observer": {
            "type": "sensor",
            "vendor": "Tehtris",
            "product": "Tehtris EDR"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "address": "5.6.7.8"
        },
        "host": {
            "domain": "example.org",
            "hostname": "MR11111",
            "os": {
                "platform": "windows",
                "version": "10.0.19041"
            },
            "name": "MR11111"
        },
        "user": {
            "id": "5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org"
        },
        "file": {
            "path": "C:\\Users\\doe-j\\AppData\\Local\\Analysis\\FUNCRES.XLAM",
            "name": "FUNCRES.XLAM",
            "directory": "C:\\Users\\doe-j\\AppData\\Local\\Analysis",
            "hash": {
                "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            }
        },
        "tehtris": {
            "edr": {
                "event": {
                    "id": "837562963",
                    "appliance": {
                        "id": "1"
                    },
                    "egKBId": "130181041000003",
                    "tag": "TRI_AAA_WIN",
                    "type": "oletools",
                    "remediation_status": "no remediation taken"
                },
                "host": {
                    "os": {
                        "release": "10",
                        "architecture": "x86_64"
                    },
                    "is_server": false
                },
                "file": {
                    "macro": {
                        "is_malicious": true,
                        "sha1": "adc83b19e793491b1c6ea0fd8b46cd9f32e592fc",
                        "behavior_status": "Suspicious | May run PowerShell commands",
                        "detection_status": "Suspicious macros detected (1)"
                    }
                }
            }
        },
        "related": {
            "hash": [
                "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            ],
            "hosts": [
                "MR11111"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        }
    }
    	
	```


=== "test_policy_alert.json"

    ```json
	
    {
        "message": "{\n  \"rflId\": 1,\n  \"time\": \"2022-10-28T14:49:14.869905+00:00\",\n  \"lvl\": 6,\n  \"module\": \"das\",\n  \"eventName\": \"HeuristicAlert\",\n  \"ipSrc\": \"1.2.3.4\",\n  \"ipDst\": \"5.6.7.8\",\n  \"egKBId\": 130171010000001,\n  \"ppid\": 12296,\n  \"os_architecture__\": \"x86_64\",\n  \"description\": \"Application policy: COPS WINDOWS v2 ([I] T1204.001 User Execution: Web requests from unusual sources)\",\n  \"os_version__\": \"10.0.19041\",\n  \"pCreateDatetime\": \"2022-10-28T14:31:26.157008+00:00\",\n  \"path\": \"C:\\\\Program Files (x86)\\\\Microsoft\\\\Edge\\\\Application\\\\106.0.1370.52\\\\identity_helper.exe\",\n  \"os_server__\": false,\n  \"os__\": \"windows\",\n  \"domain__\": \"example.org\",\n  \"sha256\": \"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\",\n  \"uuid__\": \"5c3ff0bc-5101-4152-a330-923e569c9229\",\n  \"os_release__\": \"10\",\n  \"username\": \"EXAMPLE-NT\\\\doe-j\",\n  \"cmdline\": \"\\\"C:\\\\Program Files (x86)\\\\Microsoft\\\\Edge\\\\Application\\\\106.0.1370.52\\\\identity_helper.exe\\\" --type=utility --utility-sub-type=winrt_app_id.mojom.WinrtAppIdService --lang=fr --service-sandbox-type=none --unsafely-treat-insecure-origin-as-secure=http://astgedgecp.region.local,http://astgedgecq.region.local,http://astgedrheq.region.local,http://astgedrhep.region.local --mojo-platform-channel-handle=3564 --field-trial-handle=2140,i,6139612544440408755,5345815150035985187,131072 /prefetch:8\",\n  \"location\": \"\",\n  \"hostname__\": \"MR11111\",\n  \"uid\": \"5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org\",\n  \"tag\": \"TRI_AAA_WIN\",\n  \"pid\": 2424,\n  \"id\": 666666666\n}\n",
        "event": {
            "kind": "alert",
            "reason": "Application policy: COPS WINDOWS v2 ([I] T1204.001 User Execution: Web requests from unusual sources)",
            "module": "das",
            "severity": 6,
            "type": [
                "info"
            ],
            "code": "130171010000001",
            "category": [
                "process"
            ]
        },
        "@timestamp": "2022-10-28T14:49:14.869905Z",
        "agent": {
            "id": "5c3ff0bc-5101-4152-a330-923e569c9229"
        },
        "observer": {
            "type": "sensor",
            "vendor": "Tehtris",
            "product": "Tehtris EDR"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "address": "5.6.7.8"
        },
        "host": {
            "domain": "example.org",
            "hostname": "MR11111",
            "os": {
                "platform": "windows",
                "version": "10.0.19041"
            },
            "name": "MR11111"
        },
        "user": {
            "name": "doe-j",
            "id": "5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org",
            "domain": "EXAMPLE-NT"
        },
        "file": {
            "hash": {
                "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            }
        },
        "rule": {
            "name": "COPS WINDOWS v2"
        },
        "process": {
            "pid": 2424,
            "command_line": "\"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\106.0.1370.52\\identity_helper.exe\" --type=utility --utility-sub-type=winrt_app_id.mojom.WinrtAppIdService --lang=fr --service-sandbox-type=none --unsafely-treat-insecure-origin-as-secure=http://astgedgecp.region.local,http://astgedgecq.region.local,http://astgedrheq.region.local,http://astgedrhep.region.local --mojo-platform-channel-handle=3564 --field-trial-handle=2140,i,6139612544440408755,5345815150035985187,131072 /prefetch:8",
            "parent": {
                "pid": 12296
            },
            "executable": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\106.0.1370.52\\identity_helper.exe",
            "name": "identity_helper.exe"
        },
        "threat": {
            "technique": {
                "id": "T1204.001",
                "name": "User Execution: Web requests from unusual sources"
            },
            "framework": "MITRE ATT&CK"
        },
        "tehtris": {
            "edr": {
                "event": {
                    "id": "666666666",
                    "appliance": {
                        "id": "1"
                    },
                    "egKBId": "130171010000001",
                    "tag": "TRI_AAA_WIN",
                    "type": "HeuristicAlert"
                },
                "host": {
                    "os": {
                        "release": "10",
                        "architecture": "x86_64"
                    },
                    "is_server": false
                }
            }
        },
        "related": {
            "hash": [
                "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            ],
            "hosts": [
                "MR11111"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ],
            "user": [
                "doe-j"
            ]
        }
    }
    	
	```


=== "test_sandbox_alert.json"

    ```json
	
    {
        "message": "{\n  \"rflId\": 1,\n  \"time\": \"2022-10-28T11:58:20.778323+00:00\",\n  \"lvl\": 5,\n  \"module\": \"das\",\n  \"eventName\": \"sandboxAlert\",\n  \"ipSrc\": \"1.2.3.4\",\n  \"ipDst\": \"5.6.7.8\",\n  \"egKBId\": 130181030000003,\n  \"ppid\": 3520,\n  \"os_architecture__\": \"x86_64\",\n  \"description\": \"Sandbox detection: 45%\",\n  \"os_version__\": \"10.0.19041\",\n  \"pCreateDatetime\": \"2022-10-28T11:48:08.373808+00:00\",\n  \"path\": \"C:\\\\Program Files\\\\Vendor\\\\Product\\\\program.exe\",\n  \"os_server__\": false,\n  \"os__\": \"windows\",\n  \"domain__\": \"example.org\",\n  \"sha256\": \"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\",\n  \"uuid__\": \"64a2fa85-0852-4745-81d6-0815eb2d5248\",\n  \"os_release__\": \"10\",\n  \"username\": \"EXAMPLE-NT\\\\doe-j\",\n  \"cmdline\": \"program.exe\",\n  \"hostname__\": \"MR11111\",\n  \"signatures\": \"45%\",\n  \"uid\": \"64a2fa85-0852-4745-81d6-0815eb2d5248;windows;MR11111;example.org\",\n  \"tag\": \"TRI_AAA_WIN\",\n  \"pid\": 3920,\n  \"id\": 777777777\n}\n",
        "event": {
            "kind": "alert",
            "reason": "Sandbox detection: 45%",
            "module": "das",
            "severity": 5,
            "type": [
                "info"
            ],
            "code": "130181030000003",
            "category": [
                "process"
            ]
        },
        "@timestamp": "2022-10-28T11:58:20.778323Z",
        "agent": {
            "id": "64a2fa85-0852-4745-81d6-0815eb2d5248"
        },
        "observer": {
            "type": "sensor",
            "vendor": "Tehtris",
            "product": "Tehtris EDR"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "address": "5.6.7.8"
        },
        "host": {
            "domain": "example.org",
            "hostname": "MR11111",
            "os": {
                "platform": "windows",
                "version": "10.0.19041"
            },
            "name": "MR11111"
        },
        "user": {
            "name": "doe-j",
            "id": "64a2fa85-0852-4745-81d6-0815eb2d5248;windows;MR11111;example.org",
            "domain": "EXAMPLE-NT"
        },
        "file": {
            "hash": {
                "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            }
        },
        "process": {
            "pid": 3920,
            "command_line": "program.exe",
            "parent": {
                "pid": 3520
            },
            "executable": "C:\\Program Files\\Vendor\\Product\\program.exe",
            "name": "program.exe"
        },
        "tehtris": {
            "edr": {
                "event": {
                    "id": "777777777",
                    "appliance": {
                        "id": "1"
                    },
                    "egKBId": "130181030000003",
                    "tag": "TRI_AAA_WIN",
                    "type": "sandboxAlert"
                },
                "host": {
                    "os": {
                        "release": "10",
                        "architecture": "x86_64"
                    },
                    "is_server": false
                }
            }
        },
        "related": {
            "hash": [
                "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            ],
            "hosts": [
                "MR11111"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ],
            "user": [
                "doe-j"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`agent.id` | `keyword` | Unique identifier of this agent. |
|`destination.ip` | `ip` | IP address of the destination. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.module` | `keyword` | Name of the module this data is coming from. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.severity` | `long` | Numeric severity of the event. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.created` | `date` | File creation time. |
|`file.ctime` | `date` | Last time the file attributes or metadata changed. |
|`file.directory` | `keyword` | Directory where the file is located. |
|`file.hash.sha256` | `keyword` | SHA256 hash. |
|`file.mtime` | `date` | Last time the file content was modified. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`host.domain` | `keyword` | Name of the directory the group is a member of. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.os.platform` | `keyword` | Operating system platform (such centos, ubuntu, windows). |
|`host.os.version` | `keyword` | Operating system version as a raw string. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.name` | `keyword` | Process name. |
|`process.parent.pid` | `long` | Process id. |
|`process.pid` | `long` | Process id. |
|`process.start` | `date` | The time the process started. |
|`rule.name` | `keyword` | Rule name |
|`source.ip` | `ip` | IP address of the source. |
|`tehtris.edr.event.appliance.id` | `keyword` | The identifier of the Event Appliance |
|`tehtris.edr.event.egKBId` | `keyword` | The identifier in the Event Knowledge Base |
|`tehtris.edr.event.id` | `keyword` | The identifier of the event (from the Tehtris side) |
|`tehtris.edr.event.location` | `keyword` | The location associated to the event |
|`tehtris.edr.event.remediation_status` | `keyword` | The remediation applied on the cause of the event |
|`tehtris.edr.event.tag` | `keyword` | The tag associated to the event |
|`tehtris.edr.event.type` | `keyword` | The type of the Event |
|`tehtris.edr.file.macro.behavior_status` | `keyword` | The detected behaviour of the macro |
|`tehtris.edr.file.macro.detection_status` | `keyword` | The detection status of the macro |
|`tehtris.edr.file.macro.is_malicious` | `boolean` | Is the macro malicious |
|`tehtris.edr.file.macro.sha1` | `keyword` | The SHA1 hashsum of the macro |
|`tehtris.edr.host.is_server` | `boolean` | Is the host operating as a server |
|`tehtris.edr.host.os.architecture` | `keyword` | The cpu architecture of the operating system |
|`tehtris.edr.host.os.release` | `keyword` | The release of the operating system |
|`threat.framework` | `keyword` | Threat classification framework. |
|`threat.technique.id` | `keyword` | Threat technique id. |
|`threat.technique.name` | `keyword` | Threat technique name. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.id` | `keyword` | Unique identifier of the user. |
|`user.name` | `keyword` | Short name or login of the user. |

