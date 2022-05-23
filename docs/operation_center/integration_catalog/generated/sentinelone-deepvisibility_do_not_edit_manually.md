


## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "file_creation.json"

    ```json
	
    {
        "event": {
            "start": "2206-11-13T06:23:32.121+00:00",
            "action": "fileCreation"
        },
        "deepvisibility": {
            "true_context": {
                "key": "CCC43343435EABDF"
            },
            "event": {
                "type": "fileCreation"
            },
            "agent": {
                "seq_id": 35,
                "uuid": "4d311e18709146cba871111111111111",
                "trace_id": "BABABABABEEE43452345234523423423",
                "managment_url": "https://euce1-110-nfr.sentinelone.net"
            },
            "process": {
                "node": {
                    "key": "BAE25D38782A6941"
                },
                "user": {
                    "sid": "S-1-5-21-6562365326-8585787878-2021012021-6543"
                },
                "interactive": "E_FALSE",
                "excluded": "E_FALSE",
                "root": "E_TRUE",
                "session_id": 11,
                "integrity_level": "MEDIUM",
                "is_wow64": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "true_context": {
                    "key": "CCC43343435EABDF"
                },
                "family": "SYS_WIN32",
                "executable": {
                    "name": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "node": {
                        "key": "C8E88AA83F5B15B6"
                    },
                    "start": "2021-08-05T07:45:42.456+00:00",
                    "is_dir": "E_FALSE",
                    "size_bytes": "2442584",
                    "signature": {
                        "signed": {
                            "identity": "GOOGLE LLC"
                        }
                    }
                },
                "parent": {
                    "node": {
                        "key": "03267F6915111A61"
                    }
                },
                "counters": {
                    "model_child_process": 25,
                    "os_child_process": 25,
                    "cross_process": 1610,
                    "module_load": 245,
                    "file_creation": 148,
                    "file_deletion": 58,
                    "file_modification": 416,
                    "registry_modification": 32,
                    "cross_process_dup_thread_handle": 20,
                    "cross_process_dup_process_handle": 1590
                }
            },
            "file": {
                "node": {
                    "key": "737373ABCDEF7373"
                },
                "location": "Local"
            },
            "host": {
                "os": {
                    "revision": "88888"
                }
            }
        },
        "agent": {
            "version": "S1-WIN/2.2.11.333"
        },
        "host": {
            "name": "LAPTOP-COM13",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "process": {
            "name": "Google Chrome",
            "working_directory": "Local",
            "command_line": "\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\"",
            "pid": 14896,
            "start": "2021-08-09T13:28:53.321+00:00",
            "executable": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        },
        "user": {
            "name": "SNS\\a.hifumii",
            "id": "S-1-5-21-6562365326-8585787878-2021012021-6543"
        },
        "file": {
            "created": "2021-08-09T13:28:53.666+00:00",
            "path": "C:\\Users\\a.hifumii\\AppData\\Local\\Google\\Chrome\\User Data",
            "type": "dir"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "user": [
                "SNS\\a.hifumii"
            ]
        }
    }
    	
	```


=== "tcpv4.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.5.7.370"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "seq_id": 51,
                "trace_id": "620565A45ABA475FB419254BE2152CA4",
                "uuid": "19f22913365942f2afeed1463c96104b"
            },
            "event": {
                "type": "tcpv4"
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "process": {
                "counters": {
                    "dns_lookups": 108,
                    "file_creation": 136,
                    "file_deletion": 63,
                    "file_modification": 436,
                    "module_load": 1775,
                    "net_conn_out": 261,
                    "registry_modification": 7653
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
                    "node": {
                        "key": "88D134761AF47342"
                    },
                    "signature": {
                        "signed": {
                            "identity": "MICROSOFT CORPORATION"
                        }
                    },
                    "size_bytes": "64262984",
                    "start": "18446732429235951616"
                },
                "family": "SYS_WIN32",
                "integrity_level": "MEDIUM",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "CE27A4E72749E6F2"
                },
                "parent": {
                    "node": {
                        "key": "9C0BFCE246E832C2"
                    }
                },
                "root": "E_TRUE",
                "session_id": 10,
                "true_context": {
                    "key": "C5307F702A45841C"
                },
                "user": {
                    "sid": "S-1-5-21-3542462677-1213864171-2030164332-6168"
                }
            },
            "true_context": {
                "key": "C5307F702A45841C"
            }
        },
        "destination": {
            "address": "52.182.143.208",
            "ip": "52.182.143.208",
            "port": 443
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "start": "2021-09-14T14:41:58.385+00:00",
            "action": "tcpv4"
        },
        "host": {
            "name": "LAPTOP-COM11",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"seqId\": 51, \"uuid\": \"19f22913365942f2afeed1463c96104b\", \"traceId\": \"620565A45ABA475FB419254BE2152CA4\", \"agentVersion\": \"S1-WIN/21.5.7.370\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-COM11\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631630518385\"}, \"event_type\": \"tcpv4\", \"trueContext\": {\"key\": {\"value\": \"C5307F702A45841C\"}}, \"source\": {\"node\": {\"key\": {\"value\": \"CE27A4E72749E6F2\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"88D134761AF47342\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\Program Files\\\\Microsoft Office\\\\root\\\\Office16\\\\EXCEL.EXE\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"64262984\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT CORPORATION\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"c20704e15fa16fd333cf61c5611dc74299284d7d\", \"sha256\": \"02cbdab1431442fbaa216a9361d3127c1de5a247db279aba9a4df421b973bdf4\", \"md5\": \"3dcef51688df91a37bc07d8a261a9427\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"\\\"C:\\\\Program Files\\\\Microsoft Office\\\\root\\\\Office16\\\\EXCEL.EXE\\\" /vu \\\"C:\\\\Users\\\\l.maoui\\\\AppData\\\\Local\\\\Microsoft\\\\Windows\\\\INetCache\\\\Content.Outlook\\\\GMYOE03V\\\\S36 -2021.xlsx\\\"\", \"fullPid\": {\"pid\": 19376, \"startTime\": {\"millisecondsSinceEpoch\": \"1631603628039\"}}, \"user\": {\"name\": \"SNS\\\\l.maoui\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6168\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"9C0BFCE246E832C2\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Microsoft Excel\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 10, \"integrityLevel\": \"MEDIUM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"C5307F702A45841C\"}}, \"counters\": {\"moduleLoad\": 1775, \"fileCreation\": 136, \"fileDeletion\": 63, \"fileModification\": 436, \"netConnOut\": 261, \"registryModification\": 7653, \"dnsLookups\": 108}}, \"sourceAddress\": {\"address\": \"10.26.8.27\", \"port\": 50965}, \"destinationAddress\": {\"address\": \"52.182.143.208\", \"port\": 443}, \"direction\": \"OUTGOING\", \"status\": \"SUCCESS\"}",
        "network": {
            "direction": "outbound"
        },
        "process": {
            "command_line": "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE\" /vu \"C:\\Users\\l.maoui\\AppData\\Local\\Microsoft\\Windows\\INetCache\\Content.Outlook\\GMYOE03V\\S36 -2021.xlsx\"",
            "hash": {
                "md5": "3dcef51688df91a37bc07d8a261a9427",
                "sha1": "c20704e15fa16fd333cf61c5611dc74299284d7d",
                "sha256": "02cbdab1431442fbaa216a9361d3127c1de5a247db279aba9a4df421b973bdf4"
            },
            "name": "Microsoft Excel",
            "pid": 19376,
            "start": "2021-09-14T07:13:48.039+00:00",
            "working_directory": "Local",
            "executable": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        },
        "related": {
            "hash": [
                "02cbdab1431442fbaa216a9361d3127c1de5a247db279aba9a4df421b973bdf4",
                "c20704e15fa16fd333cf61c5611dc74299284d7d",
                "3dcef51688df91a37bc07d8a261a9427"
            ],
            "ip": [
                "10.26.8.27",
                "52.182.143.208"
            ],
            "user": [
                "SNS\\l.maoui"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "source": {
            "address": "10.26.8.27",
            "ip": "10.26.8.27",
            "port": 50965
        },
        "user": {
            "id": "S-1-5-21-3542462677-1213864171-2030164332-6168",
            "name": "SNS\\l.maoui"
        }
    }
    	
	```


=== "reg_key_security_changed.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.5.7.370"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "seq_id": 10,
                "trace_id": "7892FB424053407899299D5319FEB9C5",
                "uuid": "bfd21e8929fd49768299fae02a0557a6"
            },
            "event": {
                "type": "regKeySecurityChanged"
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "process": {
                "counters": {
                    "module_load": 52
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\Windows\\system32\\taskhostw.exe",
                    "node": {
                        "key": "61D0DBC75EA434C4"
                    },
                    "signature": {
                        "signed": {
                            "identity": "MICROSOFT WINDOWS"
                        }
                    },
                    "size_bytes": "97096",
                    "start": "18446732429235951616"
                },
                "family": "SYS_WIN32",
                "integrity_level": "HIGH",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "C02A3567256C6DE9"
                },
                "parent": {
                    "node": {
                        "key": "7A33A49AFDF1C571"
                    }
                },
                "root": "E_FALSE",
                "session_id": 15,
                "true_context": {
                    "key": "D1A7307582B51DFF"
                },
                "user": {
                    "sid": "S-1-5-21-3542462677-1213864171-2030164332-6186"
                }
            },
            "registry": {
                "security_information": 4
            },
            "true_context": {
                "key": "D1A7307582B51DFF"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "regKeySecurityChanged",
            "start": "2021-09-16T09:38:28.303+00:00"
        },
        "host": {
            "name": "LAPTOP-TECH19",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"seqId\": 10, \"uuid\": \"bfd21e8929fd49768299fae02a0557a6\", \"traceId\": \"7892FB424053407899299D5319FEB9C5\", \"agentVersion\": \"S1-WIN/21.5.7.370\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-TECH19\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631785108303\"}, \"event_type\": \"regKeySecurityChanged\", \"trueContext\": {\"key\": {\"value\": \"D1A7307582B51DFF\"}}, \"regKey\": {\"key\": {}, \"path\": \"MACHINE\\\\BCD00000000\\\\Objects\\\\{9dea862c-5cdd-4e70-acc1-f32b344d4795}\\\\Elements\\\\11000001\"}, \"securityInformation\": 4, \"source\": {\"node\": {\"key\": {\"value\": \"C02A3567256C6DE9\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"61D0DBC75EA434C4\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\Windows\\\\system32\\\\taskhostw.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"97096\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"fed4b4a753a9541389aa670c69e624be07569ccd\", \"sha256\": \"0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad\", \"md5\": \"564e4806ab18f93b93d551cd10c1598e\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"taskhostw.exe\", \"fullPid\": {\"pid\": 25104, \"startTime\": {\"millisecondsSinceEpoch\": \"1631775524677\"}}, \"user\": {\"name\": \"SNS\\\\s.delaunay\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6186\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"7A33A49AFDF1C571\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Host Process for Windows Tasks\", \"root\": \"E_FALSE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 15, \"integrityLevel\": \"HIGH\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"D1A7307582B51DFF\"}}, \"counters\": {\"moduleLoad\": 52}}}",
        "process": {
            "command_line": "taskhostw.exe",
            "executable": "C:\\Windows\\system32\\taskhostw.exe",
            "hash": {
                "md5": "564e4806ab18f93b93d551cd10c1598e",
                "sha1": "fed4b4a753a9541389aa670c69e624be07569ccd",
                "sha256": "0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad"
            },
            "name": "Host Process for Windows Tasks",
            "pid": 25104,
            "start": "2021-09-16T06:58:44.677+00:00",
            "working_directory": "Local"
        },
        "registry": {
            "path": "MACHINE\\BCD00000000\\Objects\\{9dea862c-5cdd-4e70-acc1-f32b344d4795}\\Elements\\11000001",
            "value": "11000001"
        },
        "related": {
            "hash": [
                "0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad",
                "564e4806ab18f93b93d551cd10c1598e",
                "fed4b4a753a9541389aa670c69e624be07569ccd"
            ],
            "user": [
                "SNS\\s.delaunay"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "id": "S-1-5-21-3542462677-1213864171-2030164332-6186",
            "name": "SNS\\s.delaunay"
        }
    }
    	
	```


=== "reg_value_create.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.5.7.370"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "seq_id": 10,
                "trace_id": "7892FB424053407899299D5319FEB9C5",
                "uuid": "bfd21e8929fd49768299fae02a0557a6"
            },
            "event": {
                "type": "regValueCreate"
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "process": {
                "counters": {
                    "module_load": 52
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\Windows\\system32\\taskhostw.exe",
                    "node": {
                        "key": "61D0DBC75EA434C4"
                    },
                    "signature": {
                        "signed": {
                            "identity": "MICROSOFT WINDOWS"
                        }
                    },
                    "size_bytes": "97096",
                    "start": "18446732429235951616"
                },
                "family": "SYS_WIN32",
                "integrity_level": "HIGH",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "C02A3567256C6DE9"
                },
                "parent": {
                    "node": {
                        "key": "7A33A49AFDF1C571"
                    }
                },
                "root": "E_FALSE",
                "session_id": 15,
                "true_context": {
                    "key": "D1A7307582B51DFF"
                },
                "user": {
                    "sid": "S-1-5-21-3542462677-1213864171-2030164332-6186"
                }
            },
            "registry": {
                "value_type": "1"
            },
            "true_context": {
                "key": "D1A7307582B51DFF"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "regValueCreate",
            "start": "2021-09-16T09:38:28.304+00:00"
        },
        "host": {
            "name": "LAPTOP-TECH19",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"seqId\": 10, \"uuid\": \"bfd21e8929fd49768299fae02a0557a6\", \"traceId\": \"7892FB424053407899299D5319FEB9C5\", \"agentVersion\": \"S1-WIN/21.5.7.370\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-TECH19\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631785108304\"}, \"event_type\": \"regValueCreate\", \"trueContext\": {\"key\": {\"value\": \"D1A7307582B51DFF\"}}, \"regValue\": {\"key\": {}, \"path\": \"MACHINE\\\\BCD00000000\\\\Objects\\\\{9dea862c-5cdd-4e70-acc1-f32b344d4795}\\\\Elements\\\\12000002\\\\Element\"}, \"valueType\": 1, \"source\": {\"node\": {\"key\": {\"value\": \"C02A3567256C6DE9\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"61D0DBC75EA434C4\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\Windows\\\\system32\\\\taskhostw.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"97096\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"fed4b4a753a9541389aa670c69e624be07569ccd\", \"sha256\": \"0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad\", \"md5\": \"564e4806ab18f93b93d551cd10c1598e\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"taskhostw.exe\", \"fullPid\": {\"pid\": 25104, \"startTime\": {\"millisecondsSinceEpoch\": \"1631775524677\"}}, \"user\": {\"name\": \"SNS\\\\s.delaunay\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6186\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"7A33A49AFDF1C571\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Host Process for Windows Tasks\", \"root\": \"E_FALSE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 15, \"integrityLevel\": \"HIGH\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"D1A7307582B51DFF\"}}, \"counters\": {\"moduleLoad\": 52}}}",
        "process": {
            "command_line": "taskhostw.exe",
            "executable": "C:\\Windows\\system32\\taskhostw.exe",
            "hash": {
                "md5": "564e4806ab18f93b93d551cd10c1598e",
                "sha1": "fed4b4a753a9541389aa670c69e624be07569ccd",
                "sha256": "0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad"
            },
            "name": "Host Process for Windows Tasks",
            "pid": 25104,
            "start": "2021-09-16T06:58:44.677+00:00",
            "working_directory": "Local"
        },
        "registry": {
            "data": {
                "type": "REG_SZ"
            },
            "path": "MACHINE\\BCD00000000\\Objects\\{9dea862c-5cdd-4e70-acc1-f32b344d4795}\\Elements\\12000002\\Element",
            "value": "Element"
        },
        "related": {
            "hash": [
                "fed4b4a753a9541389aa670c69e624be07569ccd",
                "564e4806ab18f93b93d551cd10c1598e",
                "0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad"
            ],
            "user": [
                "SNS\\s.delaunay"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "id": "S-1-5-21-3542462677-1213864171-2030164332-6186",
            "name": "SNS\\s.delaunay"
        }
    }
    	
	```


=== "http.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.5.7.370"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "seq_id": 1,
                "trace_id": "33AEAAEA73CD4989976C65DA8123C361",
                "uuid": "3d923fd8f09b44f4973579043a3c8df3"
            },
            "event": {
                "type": "http"
            },
            "host": {
                "os": {
                    "revision": "19043"
                }
            },
            "process": {
                "counters": {
                    "dns_lookups": 81,
                    "file_creation": 522,
                    "file_deletion": 441,
                    "file_modification": 1211,
                    "model_child_process": 4,
                    "module_load": 4102,
                    "net_conn_out": 235,
                    "os_child_process": 2,
                    "registry_modification": 7596
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE",
                    "node": {
                        "key": "96C577BBA6378545"
                    },
                    "signature": {
                        "signed": {
                            "identity": "MICROSOFT CORPORATION"
                        }
                    },
                    "size_bytes": "42156856",
                    "start": "18446732429235951616"
                },
                "family": "SYS_WIN32",
                "integrity_level": "MEDIUM",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "28C500988B415CA1"
                },
                "parent": {
                    "node": {
                        "key": "8299EFA6DE45855B"
                    }
                },
                "root": "E_TRUE",
                "session_id": 1,
                "true_context": {
                    "key": "A1FFB5A30161CDC0"
                },
                "user": {
                    "sid": "S-1-5-21-3542462677-1213864171-2030164332-6195"
                }
            },
            "true_context": {
                "key": "A1FFB5A30161CDC0"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "http"
        },
        "host": {
            "name": "LAPTOP-TECH10",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "message": "{\"meta\": {\"seqId\": 1, \"uuid\": \"3d923fd8f09b44f4973579043a3c8df3\", \"traceId\": \"33AEAAEA73CD4989976C65DA8123C361\", \"agentVersion\": \"S1-WIN/21.5.7.370\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19043\", \"computerName\": \"LAPTOP-TECH10\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631784929904\"}, \"event_type\": \"http\", \"trueContext\": {\"key\": {\"value\": \"A1FFB5A30161CDC0\"}}, \"source\": {\"node\": {\"key\": {\"value\": \"28C500988B415CA1\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"96C577BBA6378545\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\Program Files\\\\Microsoft Office\\\\root\\\\Office16\\\\OUTLOOK.EXE\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"42156856\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT CORPORATION\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"676b4e6a3c2c06fd7df3b83527a5570fd6687c8f\", \"sha256\": \"97564d2938bebaaf1741fe5f675366cf1d8d3b6328fe38a5cf8e7133fe533ed1\", \"md5\": \"bafa8a3a020648b57622e0b79104468a\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"\\\"C:\\\\Program Files\\\\Microsoft Office\\\\root\\\\Office16\\\\OUTLOOK.EXE\\\"\", \"fullPid\": {\"pid\": 14144, \"startTime\": {\"millisecondsSinceEpoch\": \"1631775730819\"}}, \"user\": {\"name\": \"SNS\\\\m.benyounes\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6195\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"8299EFA6DE45855B\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Microsoft Outlook\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 1, \"integrityLevel\": \"MEDIUM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"A1FFB5A30161CDC0\"}}, \"counters\": {\"modelChildProcess\": 4, \"osChildProcess\": 2, \"moduleLoad\": 4102, \"fileCreation\": 522, \"fileDeletion\": 441, \"fileModification\": 1211, \"netConnOut\": 235, \"registryModification\": 7596, \"dnsLookups\": 81}}, \"sourceType\": \"WININET\", \"url\": \"https://automation.alticap.com/media/images/1548943185788.jpg?foo=bar#frag\", \"method\": \"GET\"}",
        "process": {
            "command_line": "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE\"",
            "executable": "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE",
            "hash": {
                "md5": "bafa8a3a020648b57622e0b79104468a",
                "sha1": "676b4e6a3c2c06fd7df3b83527a5570fd6687c8f",
                "sha256": "97564d2938bebaaf1741fe5f675366cf1d8d3b6328fe38a5cf8e7133fe533ed1"
            },
            "name": "Microsoft Outlook",
            "pid": 14144,
            "start": "2021-09-16T07:02:10.819+00:00",
            "working_directory": "Local"
        },
        "related": {
            "hash": [
                "bafa8a3a020648b57622e0b79104468a",
                "676b4e6a3c2c06fd7df3b83527a5570fd6687c8f",
                "97564d2938bebaaf1741fe5f675366cf1d8d3b6328fe38a5cf8e7133fe533ed1"
            ],
            "user": [
                "SNS\\m.benyounes"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "url": {
            "domain": "automation.alticap.com",
            "fragment": "frag",
            "original": "https://automation.alticap.com/media/images/1548943185788.jpg?foo=bar#frag",
            "path": "/media/images/1548943185788.jpg",
            "port": 443,
            "query": "foo=bar",
            "registered_domain": "alticap.com",
            "scheme": "https",
            "subdomain": "automation",
            "top_level_domain": "com"
        },
        "user": {
            "id": "S-1-5-21-3542462677-1213864171-2030164332-6195",
            "name": "SNS\\m.benyounes"
        }
    }
    	
	```


=== "process_creation.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.5.7.370"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "seq_id": 51,
                "trace_id": "620565A45ABA475FB419254BE2152CA4",
                "uuid": "19f22913365942f2afeed1463c96104b"
            },
            "event": {
                "type": "processCreation"
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "process": {
                "counters": {
                    "module_load": 44
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\Windows\\System32\\taskhostw.exe",
                    "node": {
                        "key": "7543AA6F061EE014"
                    },
                    "signature": {
                        "signed": {
                            "identity": "MICROSOFT WINDOWS"
                        }
                    },
                    "size_bytes": "97096",
                    "start": "18446732429235951616"
                },
                "family": "SYS_WIN32",
                "integrity_level": "MEDIUM",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "F85B96F9DB3700A5"
                },
                "parent": {
                    "counters": {
                        "cross_process": 324,
                        "model_child_process": 2096,
                        "module_load": 80,
                        "os_child_process": 2096
                    },
                    "excluded": "E_FALSE",
                    "executable": {
                        "is_dir": "E_FALSE",
                        "name": "C:\\Windows\\System32\\svchost.exe",
                        "node": {
                            "key": "03708471A478DAC3"
                        },
                        "signature": {
                            "signed": {
                                "identity": "MICROSOFT WINDOWS PUBLISHER"
                            }
                        },
                        "size_bytes": "57360",
                        "start": "18446732429235951616"
                    },
                    "family": "SYS_WIN32",
                    "integrity_level": "SYSTEM",
                    "interactive": "E_FALSE",
                    "is_redirected_command_processor": "E_FALSE",
                    "is_wow64": "E_FALSE",
                    "node": {
                        "key": "BAA63DA271B07548"
                    },
                    "parent": {
                        "node": {
                            "key": "C36E5F6CB1EFE1FA"
                        }
                    },
                    "root": "E_TRUE",
                    "true_context": {
                        "key": "A27D4C3AA2A4C77B"
                    },
                    "user": {
                        "sid": "S-1-5-18"
                    }
                },
                "root": "E_TRUE",
                "session_id": 10,
                "true_context": {
                    "key": "03E80496A6DE3247"
                },
                "user": {
                    "sid": "S-1-5-21-3542462677-1213864171-2030164332-6168"
                }
            },
            "true_context": {
                "key": "03E80496A6DE3247"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "start": "2021-09-14T14:41:47.153+00:00",
            "action": "processCreation"
        },
        "host": {
            "name": "LAPTOP-COM11",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"seqId\": 51, \"uuid\": \"19f22913365942f2afeed1463c96104b\", \"traceId\": \"620565A45ABA475FB419254BE2152CA4\", \"agentVersion\": \"S1-WIN/21.5.7.370\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-COM11\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631630507153\"}, \"event_type\": \"processCreation\", \"trueContext\": {\"key\": {\"value\": \"03E80496A6DE3247\"}}, \"process\": {\"node\": {\"key\": {\"value\": \"F85B96F9DB3700A5\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"7543AA6F061EE014\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\Windows\\\\System32\\\\taskhostw.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"97096\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"fed4b4a753a9541389aa670c69e624be07569ccd\", \"sha256\": \"0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad\", \"md5\": \"564e4806ab18f93b93d551cd10c1598e\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"taskhostw.exe Install $(Arg0)\", \"fullPid\": {\"pid\": 15104, \"startTime\": {\"millisecondsSinceEpoch\": \"1631630506706\"}}, \"user\": {\"name\": \"SNS\\\\l.maoui\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6168\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"BAA63DA271B07548\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Host Process for Windows Tasks\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 10, \"integrityLevel\": \"MEDIUM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"03E80496A6DE3247\"}}, \"counters\": {\"moduleLoad\": 44}}, \"parent\": {\"node\": {\"key\": {\"value\": \"BAA63DA271B07548\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"03708471A478DAC3\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"57360\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS PUBLISHER\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"010db07461e45b41c886192df6fd425ba8d42d82\", \"sha256\": \"643ec58e82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7\", \"md5\": \"f586835082f632dc8d9404d83bc16316\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"C:\\\\Windows\\\\system32\\\\svchost.exe -k netsvcs -p -s Schedule\", \"fullPid\": {\"pid\": 1900, \"startTime\": {\"millisecondsSinceEpoch\": \"1630857368855\"}}, \"user\": {\"name\": \"AUTORITE NT\\\\Syst\\u00e8me\", \"sid\": \"S-1-5-18\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"C36E5F6CB1EFE1FA\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Host Process for Windows Services\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"integrityLevel\": \"SYSTEM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"A27D4C3AA2A4C77B\"}}, \"counters\": {\"modelChildProcess\": 2096, \"osChildProcess\": 2096, \"crossProcess\": 324, \"moduleLoad\": 80, \"crossProcessOutOfGroup\": 324, \"crossProcessOpenProcess\": 324}}, \"hashes\": {\"sha1\": \"fed4b4a753a9541389aa670c69e624be07569ccd\", \"sha256\": \"0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad\", \"md5\": \"564e4806ab18f93b93d551cd10c1598e\"}, \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS\", \"valid\": {}}}}",
        "process": {
            "code_signature": {
                "exists": true,
                "subject_name": "MICROSOFT WINDOWS",
                "valid": true
            },
            "command_line": "taskhostw.exe Install $(Arg0)",
            "hash": {
                "md5": "564e4806ab18f93b93d551cd10c1598e",
                "sha1": "fed4b4a753a9541389aa670c69e624be07569ccd",
                "sha256": "0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad"
            },
            "name": "Host Process for Windows Tasks",
            "parent": {
                "command_line": "C:\\Windows\\system32\\svchost.exe -k netsvcs -p -s Schedule",
                "executable": "C:\\Windows\\System32\\taskhostw.exe",
                "hash": {
                    "md5": "f586835082f632dc8d9404d83bc16316",
                    "sha1": "010db07461e45b41c886192df6fd425ba8d42d82",
                    "sha256": "643ec58e82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7"
                },
                "name": "Host Process for Windows Services",
                "pid": 1900,
                "working_directory": "Local",
                "start": "2021-09-05T15:56:08.855+00:00"
            },
            "pid": 15104,
            "working_directory": "Local",
            "start": "2021-09-14T14:41:46.706+00:00",
            "executable": "C:\\Windows\\System32\\taskhostw.exe"
        },
        "related": {
            "hash": [
                "010db07461e45b41c886192df6fd425ba8d42d82",
                "f586835082f632dc8d9404d83bc16316",
                "fed4b4a753a9541389aa670c69e624be07569ccd",
                "643ec58e82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7",
                "0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad",
                "564e4806ab18f93b93d551cd10c1598e"
            ],
            "user": [
                "SNS\\l.maoui"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "id": "S-1-5-21-3542462677-1213864171-2030164332-6168",
            "name": "SNS\\l.maoui"
        },
        "file": {
            "hash": {
                "md5": "564e4806ab18f93b93d551cd10c1598e",
                "sha1": "fed4b4a753a9541389aa670c69e624be07569ccd",
                "sha256": "0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad"
            }
        }
    }
    	
	```


=== "behavioral_indicators.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.7.1.240"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "trace_id": "01FFQB788MA7GG70KGC1DSQ6ZT",
                "uuid": "f63008e522ce40c9afd4348634b5ab3b"
            },
            "event": {
                "type": "behavioralIndicators"
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "indicator": {
                "category": "BI_EVASION",
                "classification": "PUA",
                "description": "Code injection to other process memory space during the target process' initialization",
                "id": "WD109",
                "metadata": "To Process[ Name: \"chrome.exe\", Pid: \"19720\", UID: \"7DC20CD7D1BEDF9F\", TrueContextID: \"6B188EE5E8C5F24F\", IntegrityLevel: \"Low\", RelationToSource: \"Child\" ], File Path: \"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\"",
                "name": "PreloadInjection",
                "tactics": [
                    {
                        "name": "Defense Evasion",
                        "source": "MITRE",
                        "techniques": [
                            {
                                "link": "https://attack.mitre.org/techniques/T1055/012/",
                                "name": "T1055.012"
                            }
                        ]
                    },
                    {
                        "name": "Privilege Escalation",
                        "source": "MITRE",
                        "techniques": [
                            {
                                "link": "https://attack.mitre.org/techniques/T1055/012/",
                                "name": "T1055.012"
                            }
                        ]
                    }
                ]
            },
            "process": {
                "counters": {
                    "module_load": 70,
                    "registry_modification": 1
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "node": {
                        "key": "05893E5943D0005C"
                    },
                    "signature": {
                        "signed": {
                            "identity": "GOOGLE LLC"
                        }
                    },
                    "size_bytes": "2465624",
                    "start": "2021-09-02T08:59:58.477+00:00"
                },
                "family": "SYS_WIN32",
                "integrity_level": "LOW",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "7DC20CD7D1BEDF9F"
                },
                "parent": {
                    "counters": {
                        "cross_process": 590449,
                        "cross_process_dup_process_handle": 585159,
                        "cross_process_dup_thread_handle": 5290,
                        "dns_lookups": 16,
                        "file_creation": 490788,
                        "file_deletion": 466017,
                        "file_modification": 1403458,
                        "model_child_process": 1804,
                        "module_load": 2112,
                        "net_conn_out": 12,
                        "os_child_process": 1804,
                        "registry_modification": 1847
                    },
                    "excluded": "E_FALSE",
                    "executable": {
                        "is_dir": "E_FALSE",
                        "name": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                        "node": {
                            "key": "05893E5943D0005C"
                        },
                        "signature": {
                            "signed": {
                                "identity": "GOOGLE LLC"
                            }
                        },
                        "size_bytes": "2465624",
                        "start": "1630573198477"
                    },
                    "family": "SYS_WIN32",
                    "integrity_level": "MEDIUM",
                    "interactive": "E_FALSE",
                    "is_redirected_command_processor": "E_FALSE",
                    "is_wow64": "E_FALSE",
                    "node": {
                        "key": "0D7A69B0C2C26E73"
                    },
                    "parent": {
                        "node": {
                            "key": "41CA3A862279A7BC"
                        }
                    },
                    "root": "E_TRUE",
                    "session_id": 1,
                    "true_context": {
                        "key": "6B188EE5E8C5F24F"
                    },
                    "user": {
                        "sid": "S-1-5-21-3542462677-1213864171-2030164332-6187"
                    }
                },
                "root": "E_FALSE",
                "session_id": 1,
                "true_context": {
                    "key": "6B188EE5E8C5F24F"
                },
                "user": {
                    "sid": "S-1-5-21-3542462677-1213864171-2030164332-6187"
                }
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "behavioralIndicators"
        },
        "host": {
            "name": "LAPTOP-TECH20",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"uuid\": \"f63008e522ce40c9afd4348634b5ab3b\", \"traceId\": \"01FFQB788MA7GG70KGC1DSQ6ZT\", \"agentVersion\": \"S1-WIN/21.7.1.240\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-TECH20\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631797347671\"}, \"event_type\": \"behavioralIndicators\", \"source\": {\"node\": {\"key\": {\"value\": \"7DC20CD7D1BEDF9F\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"05893E5943D0005C\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"1630573198477\"}, \"path\": \"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"2465624\", \"signature\": {\"signed\": {\"identity\": \"GOOGLE LLC\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"a82705f4f5d1408f7c14d16a9cbe26c509422b29\", \"sha256\": \"07832d5f6344bd4d68376a6ca3c5baabb9cef7166a3752268e73fadffb07ddff\", \"md5\": \"a766188d75e570ea3f9b09fb9d82cb54\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"\\\"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\\\" --type=utility --utility-sub-type=chrome.mojom.UtilReadIcon --field-trial-handle=1744,7600736140352570522,3112921143749416041,131072 --lang=fr --service-sandbox-type=icon_reader --mojo-platform-channel-handle=30744 /prefetch:8\", \"fullPid\": {\"pid\": 19720, \"startTime\": {\"millisecondsSinceEpoch\": \"1631797347668\"}}, \"user\": {\"name\": \"SNS\\\\d.semren\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6187\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"0D7A69B0C2C26E73\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"05893E5943D0005C\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"1630573198477\"}, \"path\": \"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"2465624\", \"signature\": {\"signed\": {\"identity\": \"GOOGLE LLC\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"a82705f4f5d1408f7c14d16a9cbe26c509422b29\", \"sha256\": \"07832d5f6344bd4d68376a6ca3c5baabb9cef7166a3752268e73fadffb07ddff\", \"md5\": \"a766188d75e570ea3f9b09fb9d82cb54\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"\\\"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\\\"\", \"fullPid\": {\"pid\": 26188, \"startTime\": {\"millisecondsSinceEpoch\": \"1631516876708\"}}, \"user\": {\"name\": \"SNS\\\\d.semren\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6187\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"41CA3A862279A7BC\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Google Chrome\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 1, \"integrityLevel\": \"MEDIUM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"6B188EE5E8C5F24F\"}}, \"counters\": {\"modelChildProcess\": 1804, \"osChildProcess\": 1804, \"crossProcess\": 590449, \"moduleLoad\": 2112, \"fileCreation\": 490788, \"fileDeletion\": 466017, \"fileModification\": 1403458, \"exeModification\": 1, \"netConnOut\": 12, \"registryModification\": 1847, \"crossProcessDupThreadHandle\": 5290, \"crossProcessDupProcessHandle\": 585159, \"dnsLookups\": 16}}, \"excluded\": \"E_FALSE\", \"name\": \"Google Chrome\", \"root\": \"E_FALSE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 1, \"integrityLevel\": \"LOW\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"6B188EE5E8C5F24F\"}}, \"counters\": {\"moduleLoad\": 70, \"registryModification\": 1}}, \"indicator\": \"WD109\", \"metadata\": \"To Process[ Name: \\\"chrome.exe\\\", Pid: \\\"19720\\\", UID: \\\"7DC20CD7D1BEDF9F\\\", TrueContextID: \\\"6B188EE5E8C5F24F\\\", IntegrityLevel: \\\"Low\\\", RelationToSource: \\\"Child\\\" ], File Path: \\\"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\\\"\", \"category\": \"BI_EVASION\", \"classification\": \"PUA\", \"description\": \"Code injection to other process memory space during the target process' initialization\", \"friendlyName\": \"PreloadInjection\", \"tactics\": [{\"name\": \"Defense Evasion\", \"source\": \"MITRE\", \"techniques\": [{\"name\": \"T1055.012\", \"link\": \"https://attack.mitre.org/techniques/T1055/012/\"}]}, {\"name\": \"Privilege Escalation\", \"source\": \"MITRE\", \"techniques\": [{\"name\": \"T1055.012\", \"link\": \"https://attack.mitre.org/techniques/T1055/012/\"}]}], \"longDescription\": \"Code injection to other process memory space during the target process' initialization MITRE: Defense Evasion {<a href=\\\"https://attack.mitre.org/techniques/T1055/012/\\\" target=\\\"_blank\\\">T1055.012</a>}, Privilege Escalation {<a href=\\\"https://attack.mitre.org/techniques/T1055/012/\\\" target=\\\"_blank\\\">T1055.012</a>}\"}",
        "process": {
            "command_line": "\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\" --type=utility --utility-sub-type=chrome.mojom.UtilReadIcon --field-trial-handle=1744,7600736140352570522,3112921143749416041,131072 --lang=fr --service-sandbox-type=icon_reader --mojo-platform-channel-handle=30744 /prefetch:8",
            "executable": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "hash": {
                "md5": "a766188d75e570ea3f9b09fb9d82cb54",
                "sha1": "a82705f4f5d1408f7c14d16a9cbe26c509422b29",
                "sha256": "07832d5f6344bd4d68376a6ca3c5baabb9cef7166a3752268e73fadffb07ddff"
            },
            "name": "Google Chrome",
            "parent": {
                "command_line": "\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\"",
                "hash": {
                    "md5": "a766188d75e570ea3f9b09fb9d82cb54",
                    "sha1": "a82705f4f5d1408f7c14d16a9cbe26c509422b29",
                    "sha256": "07832d5f6344bd4d68376a6ca3c5baabb9cef7166a3752268e73fadffb07ddff"
                },
                "name": "Google Chrome",
                "pid": 26188,
                "working_directory": "Local"
            },
            "pid": 19720,
            "start": "2021-09-16T13:02:27.668+00:00",
            "working_directory": "Local"
        },
        "related": {
            "hash": [
                "a82705f4f5d1408f7c14d16a9cbe26c509422b29",
                "a766188d75e570ea3f9b09fb9d82cb54",
                "07832d5f6344bd4d68376a6ca3c5baabb9cef7166a3752268e73fadffb07ddff"
            ],
            "user": [
                "SNS\\d.semren"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "id": "S-1-5-21-3542462677-1213864171-2030164332-6187",
            "name": "SNS\\d.semren"
        }
    }
    	
	```


=== "script.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.7.1.240"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "trace_id": "01FFQFVBJWAT35E5D075MQ1408",
                "uuid": "f63008e522ce40c9afd4348634b5ab3b"
            },
            "event": {
                "type": "scripts"
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "process": {
                "counters": {
                    "dns_lookups": 1,
                    "file_creation": 3,
                    "file_deletion": 3,
                    "file_modification": 33,
                    "module_load": 224,
                    "net_conn_out": 3,
                    "registry_modification": 1
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\ProgramData\\PCDr\\CSAW\\CSAW_Child.exe",
                    "node": {
                        "key": "FBFFF74AA755328C"
                    },
                    "signature": {
                        "signed": {
                            "identity": "PC-DOCTOR, INC."
                        }
                    },
                    "size_bytes": "5518152",
                    "start": "18446732429235951616"
                },
                "family": "SYS_WIN32",
                "integrity_level": "HIGH",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_TRUE",
                "node": {
                    "key": "35A565744E7A266A"
                },
                "parent": {
                    "counters": {
                        "cross_process": 2,
                        "cross_process_dup_process_handle": 2,
                        "file_creation": 1,
                        "file_deletion": 1,
                        "file_modification": 32,
                        "model_child_process": 1,
                        "module_load": 237,
                        "net_conn_out": 2,
                        "os_child_process": 1,
                        "registry_modification": 3
                    },
                    "excluded": "E_FALSE",
                    "executable": {
                        "is_dir": "E_FALSE",
                        "name": "C:\\Users\\d.semren.SNS\\AppData\\Roaming\\PCDr\\Update\\Binaries\\CSAW.exe",
                        "node": {
                            "key": "DED9F9357E5C5C30"
                        },
                        "signature": {
                            "signed": {
                                "identity": "PC-DOCTOR, INC."
                            }
                        },
                        "size_bytes": "5518152",
                        "start": "1631802160011"
                    },
                    "family": "SYS_WIN32",
                    "integrity_level": "HIGH",
                    "interactive": "E_FALSE",
                    "is_redirected_command_processor": "E_FALSE",
                    "is_wow64": "E_TRUE",
                    "node": {
                        "key": "04DEDAAF23E16398"
                    },
                    "parent": {
                        "node": {
                            "key": "EDA8D6AB348AAE7D"
                        }
                    },
                    "root": "E_FALSE",
                    "session_id": 1,
                    "true_context": {
                        "key": "6B21DD2505AAA5F2"
                    },
                    "user": {
                        "sid": "S-1-5-21-3542462677-1213864171-2030164332-6187"
                    }
                },
                "root": "E_FALSE",
                "session_id": 1,
                "true_context": {
                    "key": "6B21DD2505AAA5F2"
                },
                "user": {
                    "sid": "S-1-5-21-3542462677-1213864171-2030164332-6187"
                }
            },
            "script": {
                "app_name": "DotNet"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "scripts"
        },
        "file": {
            "size": 612864
        },
        "host": {
            "name": "LAPTOP-TECH20",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"uuid\": \"f63008e522ce40c9afd4348634b5ab3b\", \"traceId\": \"01FFQFVBJWAT35E5D075MQ1408\", \"agentVersion\": \"S1-WIN/21.7.1.240\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-TECH20\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631802162798\"}, \"event_type\": \"scripts\", \"source\": {\"node\": {\"key\": {\"value\": \"35A565744E7A266A\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"FBFFF74AA755328C\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\ProgramData\\\\PCDr\\\\CSAW\\\\CSAW_Child.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"5518152\", \"signature\": {\"signed\": {\"identity\": \"PC-DOCTOR, INC.\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"bb900fd4da5c72e3bb2c977dbbe2e3c02e1c387d\", \"sha256\": \"e5626a87403b5efbc0c1873059eeacd9ead8b046dcc7da32fbb4e87e9a5e8dfa\", \"md5\": \"423050654da76dab9c2866ba3c13ce38\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"\\\"C:\\\\ProgramData\\\\PCDr\\\\CSAW\\\\CSAW_Child.exe\\\" /child\", \"fullPid\": {\"pid\": 14832, \"startTime\": {\"millisecondsSinceEpoch\": \"1631802162671\"}}, \"user\": {\"name\": \"SNS\\\\d.semren\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6187\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"04DEDAAF23E16398\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"DED9F9357E5C5C30\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"1631802160011\"}, \"path\": \"C:\\\\Users\\\\d.semren.SNS\\\\AppData\\\\Roaming\\\\PCDr\\\\Update\\\\Binaries\\\\CSAW.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"5518152\", \"signature\": {\"signed\": {\"identity\": \"PC-DOCTOR, INC.\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"bb900fd4da5c72e3bb2c977dbbe2e3c02e1c387d\", \"sha256\": \"e5626a87403b5efbc0c1873059eeacd9ead8b046dcc7da32fbb4e87e9a5e8dfa\", \"md5\": \"423050654da76dab9c2866ba3c13ce38\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"\\\"C:\\\\Users\\\\d.semren.SNS\\\\AppData\\\\Roaming\\\\PCDr\\\\Update\\\\Binaries\\\\CSAW.exe\\\" /NA /noui\", \"fullPid\": {\"pid\": 1780, \"startTime\": {\"millisecondsSinceEpoch\": \"1631802161886\"}}, \"user\": {\"name\": \"SNS\\\\d.semren\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6187\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"EDA8D6AB348AAE7D\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \" \", \"root\": \"E_FALSE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 1, \"integrityLevel\": \"HIGH\", \"isWow64\": \"E_TRUE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"6B21DD2505AAA5F2\"}}, \"counters\": {\"modelChildProcess\": 1, \"osChildProcess\": 1, \"crossProcess\": 2, \"moduleLoad\": 237, \"fileCreation\": 1, \"fileDeletion\": 1, \"fileModification\": 32, \"exeModification\": 3, \"netConnOut\": 2, \"registryModification\": 3, \"crossProcessDupProcessHandle\": 2}}, \"excluded\": \"E_FALSE\", \"name\": \" \", \"root\": \"E_FALSE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 1, \"integrityLevel\": \"HIGH\", \"isWow64\": \"E_TRUE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"6B21DD2505AAA5F2\"}}, \"counters\": {\"moduleLoad\": 224, \"fileCreation\": 3, \"fileDeletion\": 3, \"fileModification\": 33, \"netConnOut\": 3, \"registryModification\": 1, \"dnsLookups\": 1}}, \"targetFile\": {\"node\": {\"key\": {}}, \"creationTime\": {}, \"owner\": {}, \"hashes\": {}}, \"content\": \"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BioAABMwBgA3AAAAEwAAESiPAAAGLC8UfvYCAAQCGY0EAAABCgYWA4wtAAAbogYXBIwuAAAbogYYBYwvAAAbogYogwAABio6An72AgAEAxQohQAABipqKI8AAAYsEgJ+9gIABANvagAAChQohQAABio6FH73AgAEAgMohQAABio6FH73AgAEAhQohQAABipqKJAAAAYsEhR+9wIABAJvagAAChQohQAABio6An73AgAEAwQohQAABioAAAATMAYAJQAAABMAABEokAAABiwdFH73AgAEAheNBAAAAQoGFgOMLQAAG6IGKIMAAAYqAAAAEzAGAC4AAAATAAARKJAAAAYsJhR+9wIABAIYjQQAAAEKBhYDjC0AABuiBhcEjC4AABuiBiiDAAAGKgAAEzAGADcAAAATAAARKJAAAAYsLxR+9wIABAIZjQQAAAEKBhYDjC0AABuiBhcEjC4AABuiBhgFjC8AABuiBiiDAAAGKjoCfvcCAAQDFCiFAAAGKmookAAABiwSAn73AgAEA29qAAAKFCiFAAAGKjoUfvgCAAQCAyiFAAAGKjoUfvgCAAQCFCiFAAAGKmookQAABiwSFH74AgAEAm9qAAAKFCiFAAAGKjoCfvgCAAQDBCiFAAAGKgAAABMwBgAlAAAAEwAAESiRAAAGLB0UfvgCAAQCF40EAAABCgYWA4wtAAAbogYogwAABioAAAATMAYALgAAABMAABEokQAABiwmFH74AgAEAhiNBAAAAQoGFgOMLQAAG6IGFwSMLgAAG6IGKIMAAAYqAAATMAYANwAAABMAABEokQAABiwvFH74AgAEAhmNBAAAAQoGFgOMLQAAG6IGFwSMLgAAG6IGGAWMLwAAG6IGKIMAAAYqOgJ++AIABAMUKIUAAAYqaiiRAAAGLBICfvgCAAQDb2oAAAoUKIUAAAYqOhR++QIABAIDKIUAAAYqOhR++QIABAIUKIUAAAYqaiiSAAAGLBIUfvkCAAQCb2oAAAoUKIUAAAYqOgJ++QIABAMEKIUAAAYqAAAAEzAGACUAAAATAAARKJIAAAYsHRR++QIABAIXjQQAAAEKBhYDjC0AABuiBiiDAAAGKgAAABMwBgAuAAAAEwAAESiSAAAGLCYUfvkCAAQCGI0EAAABCgYWA4wtAAAbogYXBIwuAAAbogYogwAABioAABMwBgA3AAAA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b4AMAAYHb6UAAApvpgAACgNvgAwABigyAAArByoAAAATMAMAQwAAACYAABHQHgEAAih+AAAKBG+2AQAKLQIUKgNyaCcAcBRvCwIABigwAgAGCgYtAhQqAigXAgAGb2gBAAYCBihMAgAGb7cBAAoqABswBABpAAAAdQAAEQMKAiitAQAGKDMAACsLB2+4AQAKEwQrNhIEKLkBAAoMEgIoPwEACg0JLCMGcp8uAHASAig+AQAKcqUuAHAonQAACglvwQgABm+3AAAKChIEKLoBAAotwd4OEgT+FooAABtvAwAACtwGKgAAAAEQAAACABYAQ1kADgAAAAA6AignAAAKAhYoVQIABioeAnvEAAAEKiICA33EAAAEKiICA29XAgAGKh4Ce8YAAAQqIgIDfcYAAAQqAAATMAIAIwAAAF0AABECKFgCAAYDb88AAAYKfsUAAAQGb5MAAAosBwIoVAIABioWKjIXjMwAAAGAxQAABCoeAihTAgAGKiICAyjyAAAGKh4CKFMCAAYqHgJ7zQAABCoiAgN9zQAABCoeAnvOAAAEKiICA33OAAAEKh4Ce88AAAQqIgIDfc8AAAQqEzADADEAAAB2AAARAihhAgAGLQMaKwEbCgIoXwIABgNvSAgABgIoYwIABgZvlQAAChYyBwIoVAIABioWKh4CKF4CAAYqHgJ70AAABCoiAgN90AAABCoeAnvRAAAEKiICA33RAAAEKgATMAMAMAAAAHYAABECKGcCAAYtAxorARsKAihfAgAGA29ICAAGAihpAgAGBm+UAAAKLAcCKFQCAAYqFioeAiheAgAGKh4Ce9IAAAQqIgIDfdIAAAQqHgJ70wAABCoiAgN90wAABCoAABMwAwAzAAAAdwAAEQIobwIABi0DGisBGwoCKF8CAAYDb0gIAAYLBwIobQIABgZvlQAAChYvBwIoVAIABioWKh4CKF4CAAYqHgIoXgIABioeAnvUAAAEKiICA33UAAAEKh4Ce9UAAAQqIgIDfdUAAAQqAAAAEzADADAAAAB2AAARAih2AgAGLQMaKwEbCgIoXwIABgNvSAgABgIodAIABgZvlAAACi0HAihUAgAGKhYqIgIDKIACAAYqMn71AgAEAiiAAgAGKjJ+9gIABAIogAIABioyfvcCAAQCKIACAAYqMn74AgAEAiiAAgAGKjJ++QIABAIogAIABioyfvoCAAQCKIACAAYqABMwAwBAAAAAeAAAEQMlLQYmflsAAAoovAEACgoGKL0BAAotCAYoSAsABisFftYAAAQLBwJzgwIABgwDLA0IcqkuAHADb48CAAYmCCouKEMLAAaA1gAABCo2AgN+9gIABCiDAgAGKgAAEzADAGAAAAB5AAARAignAAAKAy0LclsGAHBzIAEACnoEFCgjCwAGLAtyxy4AcHMgAQAKegIDfdgAAAQCc9QIAAYKBgRv3QgABgYDb7ACAAZv5wgABgYoMxAABm8yEAAGb9sIAAYGfdcAAAQqHgJ71wAABCo6AnvXAAAEA2/lCAAGAiqKAxQoIwsABiwLcscuAHBzIAEACnoCe9cAAAQDb90IAAYCKjoCe9cAAAQDb+cIAAYCKjoCe9cAAAQDb+oIAAYCKhMwBAAlAAAAEwAAEQJ71wAABANv6ggABgJ71wAABBeNBAAAAQoGFgSiBm/sCAAGAioAAAATMAQAKQAAABMAABECe9cAAAQDb+oIAAYCe9cAAAQYjQQAAAEKBhYEogYXBaIGb+wIAAYCKgAAABMwBAAuAAAAEwAAEQJ71wAABANv6ggABgJ71wAABBmNBAAAAQoGFgSiBhcFogYYDgSiBm/sCAAGAioAABMwBAAzAAAAEwAAEQJ71wAABANv6ggABgJ71wAABBqNBAAAAQoGFgSiBhcFogYYDgSiBhkOBaIGb+wIAAYCKmoCe9cAAAQDb+oIAAYCe9cAAAQEb+wIAAYCKpoCe9cAAAQDb+4IAAYCe9cAAAQEb+oIAAYCe9cAAAQFb+wIAAYCKooDLQtyrhYAcHMgAQAKegJ71wAABG/xCAAGAwRvvgEACgIqGzAEAFgAAAB6AAARAy0LctkuAHBzIAEACnoDb78BAApvAgAACgsrHwdvBQAACgoCe9cAAARv8QgABgYDBm/AAQAKb74BAAoHbyoAAAot2d4RB3UKAAABDAgsBghvAwAACtwCKgEQAAACABoAK0UAEQAAAAA6AnvXAAAEA2/bCAAGAio+AnvXAAAEAwRv/AgABgIqAAMwAwBHAAAAAAAAAAMsDQJy7y4AcAMojwIABiYELA0CcqkuAHAEKI8CAAYmBSwSAnIRLwBwBYzQAAABKI8CAAYmAnvYAAAEAnvXAAAEb7MCAAYqAAMwAwBVAAAAAAAAAAMsCANvwQEACi0BKgQsDQJy7y4AcAQojwIABiYFLA0CcqkuAHAFKI8CAAYmDgQsEwJyES8AcA4EjNAAAAEojwIABiYCe9gAAAQCe9cAAARvswIABioAAAADMAMATQAAAAAAAAADLQEqBCwNAnLvLgBwBCiPAgAGJgUsDQJyqS4AcAUojwIABiYOBCwTAnIRLwBwDgSM0AAAASiPAgAGJgJ72AAABAJ71wAABG+zAgAGKgAAABMwAgAKAAAAewAAEQIDc4MCAAYKBioAABMwAgAOAAAAewAAEQJ+9QIABHODAgAGCgYqAAATMAIADgAAAHsAABECfvYCAARzgwIABgoGKgAAEzACAA4AAAB7AAARAn73AgAEc4MCAAYKBioAABMwAgAOAAAAewAAEQJ++AIABHODAgAGCgYqAAATMAIADgAAAHsAABECfvkCAARzgwIABgoGKgAAEzACAA4AAAB7AAARAn76AgAEc4MCAAYKBioiAgMopAI=\", \"contentHash\": {\"sha256\": \"2d12874ce5eff797003e69815c70c9dce5876e4062e3162c3bad65d20831d5cb\"}, \"originalSize\": \"612864\", \"appName\": \"DotNet\", \"decodedContent\": \"\\u5a4d\\u0090\\u0003\\u0000\\u0004\\u0000\\uffff\\u0000\\u00b8\\u0000\\u0000\\u0000@\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0080\\u0000\\u1f0e\\u0eba\\ub400\\ucd09\\ub821\\u4c01\\u21cd\\u6854\\u7369\\u7020\\u6f72\\u7267\\u6d61\\u6320\\u6e61\\u6f6e\\u2074\\u6562\\u7220\\u6e75\\u6920\\u206e\\u4f44\\u2053\\u6f6d\\u6564\\u0d2e\\u0a0d$\\u0000\\u0000\\u0000\\u4550\\u0000\\u014c\\u0003\\ueb01\\u5a95\\u0000\\u0000\\u0000\\u0000\\u00e0\\u2102\\u010b\\u000b\\u5200\\t\\u0600\\u0000\\u0000\\u0000\\u70ae\\t\\u2000\\u0000\\u8000\\t\\u0000\\u1000\\u2000\\u0000\\u0200\\u0000\\u0004\\u0000\\u0000\\u0000\\u0006\\u0000\\u0000\\u0000\\uc000\\t\\u0200\\u0000\\u9006\\t\\u0003\\u8560\\u0000\\u0010\\u1000\\u0000\\u0000\\u0010\\u1000\\u0000\\u0000\\u0000\\u0010\\u0000\\u0000\\u0000\\u0000\\u0000\\u7058\\tS\\u0000\\u8000\\t\\u03f0\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\ua000\\t\\f\\u0000\\u6f20\\t\\u001c\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u2000\\u0000\\b\\u0000\\u0000\\u0000\\u0000\\u0000\\u2008\\u0000H\\u0000\\u0000\\u0000\\u0000\\u0000\\u742e\\u7865t\\u0000\\u50b4\\t\\u2000\\u0000\\u5200\\t\\u0200\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000 \\u6000\\u722e\\u7273c\\u0000\\u03f0\\u0000\\u8000\\t\\u0400\\u0000\\u5400\\t\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000@\\u4000\\u722e\\u6c65\\u636f\\u0000\\f\\u0000\\ua000\\t\\u0200\\u0000\\u5800\\t\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000@\\u4200\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u7090\\t\\u0000\\u0000H\\u0000\\u0002\\u0005\\uc3ac\\u0003\\uab74\\u0005\\t\\u0000\\u0000\\u0000\\ub900\\u0002\\u0aaa\\u0001\\u2050\\u0000\\u0080\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\ue6a3\\u8233\\ufffd\\uffc6\\ubf62\\u5231\\u2bf1\\uc246\\u28c3\\ua650\\ue501\\uc6a7\\uf8fd\\uba71\\u78c1\\u6a88\\u1eba\\u07ac\\u1acf\\u9528\\uc041\\u1735\\u105b\\ube12\\u6429\\ucc1c\\ubb66\\u725d\\ue31e\\u0462\\ub239\\uc676\\ubeee\\u4969\\ucdb5\\u5b42\\u25a9\\uc392\\u5d50\\u99c8\\ue5c4\\uba43\\u02db\\u6210\\u8997\\uc1db\\u05e3\\u0107\\u113d\\u05fc\\u6fc3\\ub335\\uf0be\\u171e\\ub204\\u565f\\u4bb8\\u1e51\\u3276\\u32f2\\ud6c2\\ufffd\\u7254\\u2e32\\u021e\\u2428\\u0000\\u2a0a\\u021e\\u2428\\u0000\\u2a0a\\u023a\\u2428\\u0000\\u020a\\u2803\\u0005\\u0600\\u1e2a\\u7b02\\u0001\\u0400\\u222a\\u0302\\u017d\\u0000\\u2a04\\u021e\\u2428\\u0000\\u2a0a\\u021e\\u2428\\u0000\\u2a0a\\u023a\\u2428\\u0000\\u020a\\u2803\\n\\u0600\\u1e2a\\u7b02\\u0002\\u0400\\u222a\\u0302\\u027d\\u0000\\u2a04\\u0226\\u1603\\u0c28\\u0000\\u2a06\\u0256\\u2428\\u0000\\u020a\\u2803\\u000e\\u0600\\u0402\\u1028\\u0000\\u2a06\\u021e\\u037b\\u0000\\u2a04\\u0222\\u7d03\\u0003\\u0400\\u1e2a\\u7b02\\u0004\\u0400\\u222a\\u0302\\u047d\\u0000\\u2a04\\u0222\\u2817\\u0012\\u0600\\u3a2a\\u2802$\\u0a00\\u0302\\u1428\\u0000\\u2a06\\u021e\\u057b\\u0000\\u2a04\\u0222\\u7d03\\u0005\\u0400\\u1e2a\\u2802$\\u0a00\\u3a2a\\u2802$\\u0a00\\u0302\\u1828\\u0000\\u2a06\\u021e\\u067b\\u0000\\u2a04\\u0222\\u7d03\\u0006\\u0400\\u262a\\u1d02\\u2817\\u001c\\u0600\\u262a\\u0302\\u2817\\u001c\\u0600\\u262a\\u1d02\\u2803\\u001c\\u0600\\u562a\\u2802$\\u0a00\\u0302\\u1e28\\u0000\\u0206\\u2804 \\u0600\\u1e2a\\u7b02\\u0007\\u0400\\u222a\\u0302\\u077d\\u0000\\u2a04\\u021e\\u087b\\u0000\\u2a04\\u0222\\u7d03\\b\\u0400\\u262a\\u1d02\\u2817$\\u0600\\u262a\\u0302\\u2817$\\u0600\\u262a\\u1d02\\u2803$\\u0600\\u562a\\u2802$\\u0a00\\u0302\\u2628\\u0000\\u0206\\u2804(\\u0600\\u1e2a\\u7b02\\t\\u0400\\u222a\\u0302\\u097d\\u0000\\u2a04\\u021e\\u0a7b\\u0000\\u2a04\\u0222\\u7d03\\n\\u0400\\u1e2a\\u2802$\\u0a00\\u3a2a\\u2802$\\u0a00\\u0302\\u2c28\\u0000\\u2a06\\u021e\\u167b\\u0000\\u2a04\\u0222\\u7d03\\u0016\\u0400\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802$\\u0a00\\u3a2a\\u2802$\\u0a00\\u0302\\u3228\\u0000\\u2a06\\u021e\\u177b\\u0000\\u2a04\\u0222\\u7d03\\u0017\\u0400\\u1e2a\\u2802$\\u0a00\\u3a2a\\u2802$\\u0a00\\u0302\\u3628\\u0000\\u2a06\\u021e\\u187b\\u0000\\u2a04\\u0222\\u7d03\\u0018\\u0400\\u1e2a\\u2802/\\u0600\\u3a2a\\u2802/\\u0600\\u0302\\u3a28\\u0000\\u2a06\\u021e\\u197b\\u0000\\u2a04\\u0222\\u7d03\\u0019\\u0400\\u1e2a\\u2802$\\u0a00\\u3a2a\\u2802$\\u0a00\\u0302\\u3e28\\u0000\\u2a06\\u021e\\u1a7b\\u0000\\u2a04\\u0222\\u7d03\\u001a\\u0400\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802/\\u0600\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802/\\u0600\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802$\\u0a00\\u3a2a\\u2802$\\u0a00\\u0302\\u4b28\\u0000\\u2a06\\u021e\\u1b7b\\u0000\\u2a04\\u0222\\u7d03\\u001b\\u0400\\u3a2a\\u2802$\\u0a00\\u0302\\u4e28\\u0000\\u2a06\\u021e\\u1c7b\\u0000\\u2a04\\u0222\\u7d03\\u001c\\u0400\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802'\\u0a00*\\u3003\\u0003L\\u0000\\u0000\\u0000\\u2c03\\u020d\\u287b\\u0000\\u030a\\u516f\\u0000\\u2a06\\u7b02)\\u0a00\\u2a6f\\u0000\\u2d0a\\u020d\\u287b\\u0000\\u140a\\u516f\\u0000\\u2a06\\u7b02+\\u0a00\\u7b02)\\u0a00\\u2c6f\\u0000\\u020a\\u2d7b\\u0000\\u280aZ\\u0600\\u2e6f\\u0000\\u2a0a\\u3013\\u0003W\\u0000\\u0001\\u1100\\u2f73\\u0000\\u0a0a\\u0306\\u307d\\u0000\\u060a\\u7d041\\u0a00\\u0606\\u317b\\u0000\\u280a\\u0001\\u2b00\\u317d\\u0000\\u060a\\u7d142\\u0a00\\u0206\\u336f\\u0000\\u7d0a4\\u0a00\\u0606\\u06fe5\\u0a00\\u5073\\u0000\\u7d062\\u0a00\\u7b062\\u0a00\\u6f14Q\\u0600\\u1e2a\\u2802'\\u0a00*\\u3013\\u0003H\\u0000\\u0002\\u1100\\u2c03\\u020d\\ufffd\\u0304\\u516f\\u0000\\u2a06\\u2502\\ufffd\\u2504\\u170a\\u7d59\\u04d9\\u0400\\u1606\\u0d30\\u7b02\\u04da\\u0400\\u6f14Q\\u0600\\u022a\\ufffd\\u0204\\ufffd\\u2804Z\\u0600\\u5f6f\\u0000\\u2a06\\u3013\\u0003R\\u0000\\u0003\\u1100\\u4b73\\u0010\\u0a06\\u0306\\ufffd\\u0604\\u7d04\\u04db\\u0400\\u0606\\ufffd\\u2804\\\\\\u0600\\ufffd\\u0604\\u7d14\\u04d8\\u0400\\u0206\\ufffd\\u0604\\ufe06\\u4c06\\u0010\\u7306P\\u0600\\ufffd\\u0604\\ufffd\\u1404\\u516f\\u0000\\u2a06\\u021e\\u2728\\u0000\\u2a0a\\u039e\\u0d2c\\u7b02\\u04dc\\u0400\\u6f03Q\\u0600\\u022a\\ufffd\\u0004\\u0204\\ufffd\\u0004\\u2804Z\\u0600\\u5f6f\\u0000\\u2a06\\u0000\\u3013\\u00024\\u0000\\u0004\\u1100\\u4d73\\u0010\\u0b06\\u0207\\ufffd\\u0004\\u0704\\u7d03\\u04dd\\u0400\\u0707\\ufffd\\u0004\\u2804\\\\\\u0600\\ufffd\\u0004\\u0704\\u06fe\\u104e\\u0600\\u5073\\u0000\\u0a06\\u2a06\\u024e\\u7303\\u0618\\u0600\\u06fe\\u0619\\u0600\\u5073\\u0000\\u2a06\\u021e\\u2728\\u0000\\u2a0a\\u021e\\u2728\\u0000\\u2a0a\\u301b\\u0002h\\u0000\\u0005\\u1100\\u0172\\u0000\\u0370\\u0228\\u0000\\u032b\\u292c\\u0b16\\u7b026\\u0a00\\u0c25\\u0112\\u3728\\u0000\\u020a\\u367b\\u0000\\u030a\\u386f\\u0000\\ufffd\\u070a\\u062c\\u28089\\u0a00\\u02dc\\u3a7c\\u0000\\u280a;\\u0a00\\u720a5\\u7000\\u2806\\u0003\\u2b00\\u2d06\\u0216\\u3c7b\\u0000\\u020a\\u367b\\u0000\\u280a[\\u0600\\u516f\\u0000\\u2a06\\u1001\\u0000\\u0002\\u0010\\u2d1d\\u0a00\\u0000\\u0000\\u301b\\u0003A\\u0000\\u0006\\u1100\\u7b02=\\u0a00\\u3e7b\\u0000\\u020a\\u3f7b\\u0000\\u020a\\u3d7b\\u0000\\u7b0a@\\u0a00\\u5a28\\u0000\\u6f06.\\u0a00\\u18de\\u060a\\u8f72\\u0000\\u2870\\u00bf\\u0600\\u2806\\u043f\\u0600\\u022c\\u1afe\\u00de*\\u0000\\u1001\\u0000\\u0000\\u0000\\u2828\\u1800\\u0006\\u0100\\u301b\\u0003\\u00cc\\u0000\\u0007\\u1100\\u4173\\u0000\\u0d0a\\u0309\\u427d\\u0000\\u090a\\u7d04C\\u0a00\\u0909\\u437b\\u0000\\u280a\\u0001\\u2b00\\u437d\\u0000\\u020a\\u4473\\u0000\\u0a0a\\u0609\\u456f\\u0000\\u7d0aF\\u0a00\\u7309G\\u0a00\\u487d\\u0000\\u720a\\u00e7\\u7000\\u6f06E\\u0a00\\u0328\\u0000\\u092b\\u467b\\u0000\\u2d0a\\u090d\\u427b\\u0000\\u140a\\u516f\\u0000\\u2a06\\u0909\\u06feI\\u0a00\\u5073\\u0000\\u7d06J\\u0a00\\u6f06K\\u0a00\\u0413\\u2e2b\\u0412\\u4c28\\u0000\\u0b0a\\u4d73\\u0000\\u0c0a\\u0908\\u4e7d\\u0000\\u080a\\u7d07O\\u0a00\\ufe08\\u5006\\u0000\\u730aQ\\u0a00\\u5228\\u0000\\u260a\\u0412\\u5328\\u0000\\u2d0a\\ufffd\\u120e\\ufe04\\u2316\\u0000\\u6f1b\\u0003\\u0a00\\u2adc\\u1001\\u0000\\u0002\\u0082\\ubd3b\\u0e00\\u0000\\u0000\\u021e\\u2728\\u0000\\u2a0a\\u0252\\u7d03\\u04e6\\u0400\\u7b02\\u04e5\\u0400\\u546f\\u0000\\u260a*\\u0000\\u3013\\u0003V\\u0000\\b\\u1100\\u5373\\u0010\\u0a06\\u1606\\u5573\\u0000\\u7d0a\\u04e5\\u0400\\u1406\\ue67d\\u0004\\u0204\\ufe06\\u5406\\u0010\\u7306P\\u0600\\u5a28\\u0000\\u6f06_\\u0600\\u7b06\\u04e5\\u0400\\u566f\\u0000\\u260a\\u7b06\\u04e6\\u0400\\u112c\\u2b72\\u0001\\u0670\\ue67b\\u0004\\u7304\\u0c5d\\u0600\\u2a7a\\u0286\\u576f\\u0000\\u750a\\u00b8\\u0200\\u022c\\u2a02\\u7302\\u05d3\\u0600\\u06fe\\u05d4\\u0600\\u5073\\u0000\\u2a06\\u301b\\u0002\\u0086\\u0000\\t\\u1100\\u6f02X\\u0a00\\u022d\\u2a14\\u6f02X\\u0a00\\u3317\\u0208\\u6f16Y\\u0a00\\u732aZ\\u0a00\\u7e0a[\\u0a00\\u280b\\u043a\\u0600\\u020c\\u5c6f\\u0000\\u130a\\u2b04\\u1127\\u6f04]\\u0a00\\u060d\\u6f07^\\u0a00\\u0626\\u6f09_\\u0a00\\u5e6f\\u0000\\u260a\\u0806\\u5e6f\\u0000\\u260a\\u0b08\\u0411\\u2a6f\\u0000\\u2d0a\\ufffd\\u110c\\u2c04\\u1107\\u6f04\\u0003\\u0a00\\u72dc\\u0175\\u7000\\u2806`\\u0a00\\u5b73\\f\\u2a06\\u0000\\u1001\\u0000\\u00025\\u6934\\u0c00\\u0000\\u0000\\u021e\\u2728\\u0000\\u2a0a\\u301b\\u0002#\\u0000\\u0006\\u1100\\u7b02\\u04e7\\u0400\\u6f03_\\u0600\\u14de\\u060a\\u3e28\\u0004\\u2c06\\ufe02\\u031a\\u6f06Q\\u0600\\u00de*\\u1001\\u0000\\u0000\\u0000\\u0e0e\\u1400\\u0006\\u0100\\u3013\\u0002\\u001a\\u0000\\n\\u1100\\u5573\\u0010\\u0a06\\u0206\\ue77d\\u0004\\u0604\\u06fe\\u1056\\u0600\\u5e73\\u0000\\u2a06\\u021e\\u2728\\u0000\\u2a0a\\u0000\\u301b\\u0003$\\u0000\\u0006\\u1100\\u7b02a\\u0a00\\u0403\\u2e6f\\u0000\\ufffd\\u0a14\\u2806\\u043e\\u0600\\u022c\\u1afe\\u0604\\u516f\\u0000\\ufffd\\u2a00\\u1001\\u0000\\u0000\\u0000\\u0f0f\\u1400\\u0006\\u0100\\u3013\\u0002\\u001a\\u0000\\u000b\\u1100\\u6273\\u0000\\u0a0a\\u0206\\u637d\\u0000\\u060a\\u06fed\\u0a00\\u6573\\u0000\\u2a0a\\u025a\\u15fe&\\u0200\\u0302\\u6828\\u0000\\u0206\\u2804j\\u0600\\u1e2a\\u7b02\\u001d\\u0400\\u222a\\u0302\\u1d7d\\u0000\\u2a04\\u021e\\u1e7b\\u0000\\u2a04\\u0222\\u7d03\\u001e\\u0400\\uae2a\\u000f\\u6928\\u0000\\u0f06\\u2801i\\u0600\\u6728\\u0000\\u2c0a\\u0f14\\u2800g\\u0600\\u010f\\u6728\\u0000\\u2806g\\u0a00\\u162a\\uba2a\\u000f\\u6928\\u0000\\u0f06\\u2801i\\u0600\\u6728\\u0000\\u2c0a\\u0f17\\u2800g\\u0600\\u010f\\u6728\\u0000\\u2806g\\u0a00\\ufe16\\u2a01\\u2a17\\u0000\\u3013\\u0002\\u0014\\u0000\\f\\u1100\\ua503&\\u0200\\u020a\\u2671\\u0000\\u0602\\u6b28\\u0000\\u2a06\\u0262\\u6728\\u0000\\u6f06h\\u0a00\\u2802i\\u0600\\u686f\\u0000\\u610a\\u5a2a\\u2773\\u0000\\u800a\\u001f\\u0400\\u8016!\\u0400\\u7028\\u0000\\u2a06\\u3003\\u0003\\u009d\\u0000\\u0000\\u0000\\uab72\\u0001\\u7270\\u01df\\u7000\\u2816\\u0004\\u2b00\\u7428\\u0000\\u7206\\u0219\\u7000\\u5772\\u0002\\u1670\\u0428\\u0000\\u282bv\\u0600\\u9d72\\u0002\\u7270\\u02c9\\u7000\\uf77e\\u0002\\u2804\\u008b\\u0600\\u7228\\u0000\\u7206\\u02f9\\u7000\\u2372\\u0003\\u7e70[\\u0a00\\u0528\\u0000\\u282bz\\u0600\\u5172\\u0003\\u7270\\u0381\\u7000\\u2816\\u0004\\u2b00\\u7828\\u0000\\u7206\\u03b7\\u7000\\uf972\\u0003\\u1770\\u0428\\u0000\\u282b~\\u0600\\u3972\\u0004\\u2870\\u00a7\\u0600\\u8016!\\u0400\\u2814|\\u0600\\u1a2a\\u227e\\u0000\\u2a04\\u021e\\u2280\\u0000\\u2a04\\u7e1a#\\u0400\\u1e2a\\u8002#\\u0400\\u1a2a\\u247e\\u0000\\u2a04\\u021e\\u2480\\u0000\\u2a04\\u7e1a%\\u0400\\u1e2a\\u8002%\\u0400\\u1a2a\\u207e\\u0000\\u2a04\\u0276\\u2080\\u0000\\u7e04 \\u0400\\u6928\\u0000\\u2d0a\\u7e0a \\u0400\\u8d28\\u0000\\u2a06\\u7e1a&\\u0400\\u1e2a\\u8002&\\u0400\\u1a2a\\u277e\\u0000\\u2a04\\u021e\\u2780\\u0000\\u2a04\\u142a\\u0302\\u2804\\u0085\\u0600\\u2a2a\\u0214\\u1403\\u8528\\u0000\\u2a06\\u0272\\u7128\\u0000\\u2806\\u0b26\\u0600\\u0e2c\\u0214\\u6f03j\\u0a00\\u2814\\u0085\\u0600\\u722a\\u2803q\\u0600\\u2628\\u000b\\u2c06\\u020e\\u0403\\u6a6f\\u0000\\u140a\\u8528\\u0000\\u2a06\\u022a\\u0403\\u2805\\u0085\\u0600\\u2a2a\\u0302\\u1404\\u8528\\u0000\\u2a06\\u0000\\u301b\\u0004\\u01a6\\u0000\\r\\u1100\\u2802\\u0086\\u0600\\u012c\\u032a\\u8728\\u0000\\u2d06\\u2a01\\u0a04\\u2c05\\u280dk\\u0a00\\u0504\\u6c28\\u0000\\u0a0a\\u6f04m\\u0a00\\u201f\\u7358n\\u0a00\\u280b}\\u0600\\u302c\\u2807\\u1033\\u0600\\u326f\\u0010\\u1306\\u120b\\u720b\\u047d\\u7000\\u6b28\\u0000\\u280ao\\u0a00\\u5e6f\\u0000\\u260a\\u7207\\u04af\\u7000\\u5e6f\\u0000\\u260a\\u0307\\u706f\\u0000\\u260a\\u7207\\u04af\\u7000\\u5e6f\\u0000\\u260a\\u0607\\u5e6f\\u0000\\u260a\\u2c02\\u021a\\u3c28\\u0004\\u0706\\ub372\\u0004\\u6f70^\\u0a00\\u0726\\u6f02p\\u0a00\\u0726\\u5f6f\\u0000\\u0c0a\\u7928\\u0000\\u0d06\\u2809i\\u0a00\\u3e2d\\u1316\\u7e05\\u001f\\u0400\\u1325\\u120c\\u28057\\u0a00\\u2809q\\u0a00\\u0413\\u0411\\u6f08r\\u0a00\\u0cde\\u0411\\u072c\\u0411\\u036f\\u0000\\ufffd\\u0cde\\u0511\\u072c\\u0c11\\u3928\\u0000\\ufffd\\u7b28\\u0000\\u1306\\u1106\\u2c06\\u1628\\u0713\\u1f7e\\u0000\\u2504\\u0d13\\u0712\\u3728\\u0000\\u110a\\u0806\\u726f\\u0000\\ufffd\\u110c\\u2c07\\u1107\\u280d9\\u0a00\\u28dcs\\u0600\\u262c\\u1316\\u7e08\\u001f\\u0400\\u1325\\u120e\\u28087\\u0a00\\u2808s\\u0a00\\u0cde\\u0811\\u072c\\u0e11\\u3928\\u0000\\ufffd\\u7528\\u0000\\u2c06\\u162b\\u0913\\u1f7e\\u0000\\u2504\\u0f13\\u0912\\u3728\\u0000\\u280at\\u0a00\\u6f08r\\u0a00\\u0cde\\u0911\\u072c\\u0f11\\u3928\\u0000\\ufffd\\u2808\\u0088\\u0600\\u15de\\u0a13\\u8017!\\u0400\\u0a11\\u3f28\\u0004\\u2c06\\ufe02\\ufffd\\u2a00\\u0000\\u9441\\u0000\\u0002\\u0000\\u00d2\\u0000\\n\\u0000\\u00dc\\u0000\\f\\u0000\\u0000\\u0000\\u0002\\u0000\\u00bb\\u0000/\\u0000\\u00ea\\u0000\\f\\u0000\\u0000\\u0000\\u0002\\u0000\\u0104\\u0000\\u0019\\u0000\\u011d\\u0000\\f\\u0000\\u0000\\u0000\\u0002\\u0000\\u0133\\u0000\\u0017\\u0000\\u014a\\u0000\\f\\u0000\\u0000\\u0000\\u0002\\u0000\\u0160\\u0000\\u001c\\u0000\\u017c\\u0000\\f\\u0000\\u0000\\u0000\\u0000\\u0000\\u0012\\u0000\\u017e\\u0000\\u0190\\u0000\\u0015\\u0000\\u0006\\u0100\\u0232\\u072c\\u2802\\u043f\\u0600\\u162a*\\u0000\\u3003\\u0002K\\u0000\\u0000\\u0000\\u7e02\\u02fb\\u0400\\u2328\\u000b\\u2d06\\u020d\\u7128\\u0000\\u2806\\u0b27\\u0600\\u022c\\u2a16\\u7928\\u0000\\u2806i\\u0a00\\u212c\\u7328\\u0000\\u2d06\\u281au\\u0600\\u132d\\u7728\\u0000\\u2d06\\u280c{\\u0600\\ufe14\\u1601\\u01fe\\u172a\\u522a\\u7728\\u0000\\u2d06\\u2a01\\u7202\\u04cd\\u7000\\u7528\\u0000\\u2a0a\\u301b\\u0005J\\u0000\\u000e\\u1100\\u6f02v\\u0a00\\u7728\\u0000\\u0a0a\\ud772\\u0004\\u0270\\u786f\\u0000\\u060a\\u796f\\u0000\\u060a\\u7a6f\\u0000\\u280a\\u0006\\u2b00\\u1fde\\u070b\\u3372\\u0005\\u1770\\u048d\\u0000\\u0c01\\u1608\\u6f02x\\u0a00\\u08a2\\ubb28\\u0000\\ufffd\\u2a00\\u0000\\u1001\\u0000\\u0000\\u0000\\u2a2a\\u1f00\\u0006\\u0100\\u301b\\u0002'\\u0000\\u000f\\u1100\\u7b28\\u0000\\u020a\\u7c6f\\u0000\\u0a0a\\u2d06\\u0316\\u7d28\\u0000\\u0a0a\\u0dde\\u070b\\u3f28\\u0004\\u2c06\\ufe02\\ufffd\\u0600*\\u1001\\u0000\\u0000\\u000f\\u1809\\u0d00\\u0006\\u0100\\u301b\\u0002'\\u0000\\u0010\\u1100\\u0302\\u8a28\\u0000\\u0a06\\u2d06\\u0402\\u062a\\u2a28\\u000b\\u0c06\\u0fde\\u070b\\u3f28\\u0004\\u2c06\\ufe02\\u041a\\ufffd\\u0800*\\u1001\\u0000\\u0000\\r\\u1609\\u0f00\\u0006\\u0100\\u301b\\u0003;\\u0000\\u0011\\u1100\\u0302\\u8a28\\u0000\\u0a06\\u2d06\\u0402\\u062a\\u2dd0\\u0000\\u281b~\\u0a00\\u6b28\\u0000\\u280a\\u007f\\u0a00\\u2da5\\u0000\\u0c1b\\u0fde\\u070b\\u3f28\\u0004\\u2c06\\ufe02\\u041a\\ufffd\\u0800*\\u1001\\u0000\\u0000\\r\\u2a1d\\u0f00\\u0006\\u0100\\u301b\\u0005P\\u0000\\u0012\\u1100\\u7128\\u0000\\u7e06\\u02fb\\u0400\\u2328\\u000b\\u2c06\\ufffd\\u023c\\u8028\\u0000\\u0a0a\\u2806i\\u0a00\\u072d\\u2806\\u0081\\u0a00\\ufffd\\u0b24\\u7207\\u0581\\u7000\\u8d17\\u0004\\u0100\\u080c\\u0216\\u08a2\\ubb28\\u0000\\u0706\\u3f28\\u0004\\u2c06\\ufe02\\ufffd\\u2a00\\u1001\\u0000\\u0000\\u0000\\u2b2b\\u2400\\u0006\\u0100\\u7e42\\u02f5\\u0400\\u7128\\u0000\\u2806\\u0b26\\u0600\\u422a\\uf67e\\u0002\\u2804q\\u0600\\u2628\\u000b\\u2a06\\u7e42\\u02f7\\u0400\\u7128\\u0000\\u2806\\u0b26\\u0600\\u422a\\uf87e\\u0002\\u2804q\\u0600\\u2628\\u000b\\u2a06\\u7e42\\u02f9\\u0400\\u7128\\u0000\\u2806\\u0b26\\u0600\\u422a\\ufa7e\\u0002\\u2804q\\u0600\\u2628\\u000b\\u2a06\\u143a\\uf57e\\u0002\\u0204\\u2803\\u0085\\u0600\\u3a2a\\u7e14\\u02f5\\u0400\\u1402\\u8528\\u0000\\u2a06\\u286a\\u008e\\u0600\\u122c\\u7e14\\u02f5\\u0400\\u6f02j\\u0a00\\u2814\\u0085\\u0600\\u3a2a\\u7e02\\u02f5\\u0400\\u0403\\u8528\\u0000\\u2a06\\u0000\\u3013\\u0006%\\u0000\\u0013\\u1100\\u8e28\\u0000\\u2c06\\u141d\\uf57e\\u0002\\u0204\\u8d17\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u2806\\u0083\\u0600*\\u0000\\u3013\\u0006.\\u0000\\u0013\\u1100\\u8e28\\u0000\\u2c06\\u1426\\uf57e\\u0002\\u0204\\u8d18\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u8328\\u0000\\u2a06\\u0000\\u3013\\u00067\\u0000\\u0013\\u1100\\u8e28\\u0000\\u2c06\\u142f\\uf57e\\u0002\\u0204\\u8d19\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u0518\\u2f8c\\u0000\\ua21b\\u2806\\u0083\\u0600\\u3a2a\\u7e02\\u02f5\\u0400\\u1403\\u8528\\u0000\\u2a06\\u286a\\u008e\\u0600\\u122c\\u7e02\\u02f5\\u0400\\u6f03j\\u0a00\\u2814\\u0085\\u0600\\u3a2a\\u7e14\\u02f6\\u0400\\u0302\\u8528\\u0000\\u2a06\\u143a\\uf67e\\u0002\\u0204\\u2814\\u0085\\u0600\\u6a2a\\u8f28\\u0000\\u2c06\\u1412\\uf67e\\u0002\\u0204\\u6a6f\\u0000\\u140a\\u8528\\u0000\\u2a06\\u023a\\uf67e\\u0002\\u0304\\u2804\\u0085\\u0600*\\u0000\\u3013\\u0006%\\u0000\\u0013\\u1100\\u8f28\\u0000\\u2c06\\u141d\\uf67e\\u0002\\u0204\\u8d17\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u2806\\u0083\\u0600*\\u0000\\u3013\\u0006.\\u0000\\u0013\\u1100\\u8f28\\u0000\\u2c06\\u1426\\uf67e\\u0002\\u0204\\u8d18\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u8328\\u0000\\u2a06\\u0000\\u3013\\u00067\\u0000\\u0013\\u1100\\u8f28\\u0000\\u2c06\\u142f\\uf67e\\u0002\\u0204\\u8d19\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u0518\\u2f8c\\u0000\\ua21b\\u2806\\u0083\\u0600\\u3a2a\\u7e02\\u02f6\\u0400\\u1403\\u8528\\u0000\\u2a06\\u286a\\u008f\\u0600\\u122c\\u7e02\\u02f6\\u0400\\u6f03j\\u0a00\\u2814\\u0085\\u0600\\u3a2a\\u7e14\\u02f7\\u0400\\u0302\\u8528\\u0000\\u2a06\\u143a\\uf77e\\u0002\\u0204\\u2814\\u0085\\u0600\\u6a2a\\u9028\\u0000\\u2c06\\u1412\\uf77e\\u0002\\u0204\\u6a6f\\u0000\\u140a\\u8528\\u0000\\u2a06\\u023a\\uf77e\\u0002\\u0304\\u2804\\u0085\\u0600*\\u0000\\u3013\\u0006%\\u0000\\u0013\\u1100\\u9028\\u0000\\u2c06\\u141d\\uf77e\\u0002\\u0204\\u8d17\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u2806\\u0083\\u0600*\\u0000\\u3013\\u0006.\\u0000\\u0013\\u1100\\u9028\\u0000\\u2c06\\u1426\\uf77e\\u0002\\u0204\\u8d18\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u8328\\u0000\\u2a06\\u0000\\u3013\\u00067\\u0000\\u0013\\u1100\\u9028\\u0000\\u2c06\\u142f\\uf77e\\u0002\\u0204\\u8d19\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u0518\\u2f8c\\u0000\\ua21b\\u2806\\u0083\\u0600\\u3a2a\\u7e02\\u02f7\\u0400\\u1403\\u8528\\u0000\\u2a06\\u286a\\u0090\\u0600\\u122c\\u7e02\\u02f7\\u0400\\u6f03j\\u0a00\\u2814\\u0085\\u0600\\u3a2a\\u7e14\\u02f8\\u0400\\u0302\\u8528\\u0000\\u2a06\\u143a\\uf87e\\u0002\\u0204\\u2814\\u0085\\u0600\\u6a2a\\u9128\\u0000\\u2c06\\u1412\\uf87e\\u0002\\u0204\\u6a6f\\u0000\\u140a\\u8528\\u0000\\u2a06\\u023a\\uf87e\\u0002\\u0304\\u2804\\u0085\\u0600*\\u0000\\u3013\\u0006%\\u0000\\u0013\\u1100\\u9128\\u0000\\u2c06\\u141d\\uf87e\\u0002\\u0204\\u8d17\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u2806\\u0083\\u0600*\\u0000\\u3013\\u0006.\\u0000\\u0013\\u1100\\u9128\\u0000\\u2c06\\u1426\\uf87e\\u0002\\u0204\\u8d18\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u8328\\u0000\\u2a06\\u0000\\u3013\\u00067\\u0000\\u0013\\u1100\\u9128\\u0000\\u2c06\\u142f\\uf87e\\u0002\\u0204\\u8d19\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u0518\\u2f8c\\u0000\\ua21b\\u2806\\u0083\\u0600\\u3a2a\\u7e02\\u02f8\\u0400\\u1403\\u8528\\u0000\\u2a06\\u286a\\u0091\\u0600\\u122c\\u7e02\\u02f8\\u0400\\u6f03j\\u0a00\\u2814\\u0085\\u0600\\u3a2a\\u7e14\\u02f9\\u0400\\u0302\\u8528\\u0000\\u2a06\\u143a\\uf97e\\u0002\\u0204\\u2814\\u0085\\u0600\\u6a2a\\u9228\\u0000\\u2c06\\u1412\\uf97e\\u0002\\u0204\\u6a6f\\u0000\\u140a\\u8528\\u0000\\u2a06\\u023a\\uf97e\\u0002\\u0304\\u2804\\u0085\\u0600*\\u0000\\u3013\\u0006%\\u0000\\u0013\\u1100\\u9228\\u0000\\u2c06\\u141d\\uf97e\\u0002\\u0204\\u8d17\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u2806\\u0083\\u0600*\\u0000\\u3013\\u0006.\\u0000\\u0013\\u1100\\u9228\\u0000\\u2c06\\u1426\\uf97e\\u0002\\u0204\\u8d18\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u8328\\u0000\\u2a06\\u0000\\u3013\\u00067\\u0000\\u0013\\u1100\\u9228\\u0000\\u2c06\\u142f\\uf97e\\u0002\\u0204\\u8d19\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u0518\\u2f8c\\u0000\\ua21b\\u2806\\u0083\\u0600\\u3a2a\\u7e02\\u02f9\\u0400\\u1403\\u8528\\u0000\\u2a06\\u286a\\u0092\\u0600\\u122c\\u7e02\\u02f9\\u0400\\u6f03j\\u0a00\\u2814\\u0085\\u0600\\u3a2a\\u7e14\\u02fa\\u0400\\u0302\\u8528\\u0000\\u2a06\\u143a\\ufa7e\\u0002\\u0204\\u2814\\u0085\\u0600\\u6a2a\\u9328\\u0000\\u2c06\\u1412\\ufa7e\\u0002\\u0204\\u6a6f\\u0000\\u140a\\u8528\\u0000\\u2a06\\u023a\\ufa7e\\u0002\\u0304\\u2804\\u0085\\u0600*\\u0000\\u3013\\u0006%\\u0000\\u0013\\u1100\\u9328\\u0000\\u2c06\\u141d\\ufa7e\\u0002\\u0204\\u8d17\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u2806\\u0083\\u0600*\\u0000\\u3013\\u0006.\\u0000\\u0013\\u1100\\u9328\\u0000\\u2c06\\u1426\\ufa7e\\u0002\\u0204\\u8d18\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u8328\\u0000\\u2a06\\u0000\\u3013\\u00067\\u0000\\u0013\\u1100\\u9328\\u0000\\u2c06\\u142f\\ufa7e\\u0002\\u0204\\u8d19\\u0004\\u0100\\u060a\\u0316\\u2d8c\\u0000\\ua21b\\u1706\\u8c04.\\u1b00\\u06a2\\u0518\\u2f8c\\u0000\\ua21b\\u2806\\u0083\\u0600\\u3a2a\\u7e02\\u02fa\\u0400\\u1403\\u8528\\u0000\\u2a06\\u286a\\u0093\\u0600\\u122c\\u7e02\\u02fa\\u0400\\u6f03j\\u0a00\\u2814\\u0085\\u0600\\ube2a\\u2802'\\u0a00\\u0402\\u287d\\u0000\\u0204\\u8d03&\\u0200\\u2a7d\\u0000\\u0204\\u7d05)\\u0400\\u1602\\u2b7d\\u0000\\u0204\\u7d16,\\u0400\\u262a\\u7b02*\\u0400\\u698e*\\u301b\\u0005\\u0100\\u0000\\u0014\\u1100\\u0c16\\u2502\\u0413\\u0212\\u3728\\u0000\\u020a\\u2d7b\\u0000\\u0204\\u2a7b\\u0000\\u8e04\\u3269\\u0267\\u287b\\u0000\\u2c04\\u0251\\u2a7b\\u0000\\u8e04\\u0269\\u297b\\u0000\\u2f04\\u0241\\u2a7b\\u0000\\u8e04\\u1869\\u0a5a\\u0206\\u297b\\u0000\\u3204\\u0207\\u297b\\u0000\\u0a04\\u8d06&\\u0200\\u020b\\u2a7b\\u0000\\u1604\\u1607\\u7b02*\\u0400\\u698e\\u8228\\u0000\\u020a\\u7d07*\\u0400\\u0e2b\\u0202\\u2b7b\\u0000\\u1704\\u7d58+\\u0400\\u0202\\u2c7b\\u0000\\u0204\\u2a7b\\u0000\\u8e04\\u5d69\\u2c7d\\u0000\\u0204\\u2a7b\\u0000\\u0204\\u2c7b\\u0000\\u8f04&\\u0200\\u8103&\\u0200\\u0202\\u2c7b\\u0000\\u1704\\u7d58,\\u0400\\u2502\\u2d7b\\u0000\\u1704\\u7d58-\\u0400\\u7b02-\\u0400\\u7b02*\\u0400\\u698e\\u0e32\\u0202\\u2a7b\\u0000\\u8e04\\u7d69-\\u0400\\u7b02-\\u0400\\ufffd\\u080b\\u072c\\u0411\\u3928\\u0000\\ufffd\\u2a09\\u1001\\u0000\\u0002\\u0002\\uf3f1\\u0b00\\u0000\\u0000\\u301b\\u0002\\u00a2\\u0000\\u0015\\u1100\\u1316\\u0205\\u1325\\u1207\\u28057\\u0a00\\u7b02-\\u0400\\u060a\\u092d\\u0728\\u0000\\u132b\\ufffd\\u067e\\u268d\\u0000\\u0b02\\u0c16\\u492b\\u7b02+\\u0400\\u5808\\u7b02*\\u0400\\u698e\\u0d5d\\u7b02*\\u0400\\u8f09&\\u0200\\u2671\\u0000\\u1302\\u0204\\u2a7b\\u0000\\u0904\\u268f\\u0000\\ufe02\\u2615\\u0000\\u0702\\u8f08&\\u0200\\u0411\\u2681\\u0000\\u0802\\u5817\\u080c\\u3206\\u02b3\\u7d16-\\u0400\\u1602\\u2b7d\\u0000\\u0204\\u7d16,\\u0400\\u1307\\ufffd\\u110c\\u2c05\\u1107\\u28079\\u0a00\\u11dc\\u2a06\\u0000\\u1001\\u0000\\u0002\\u0003\\u9390\\u0c00\\u0000\\u0000\\u021e\\u1628\\u0001\\u2a06\\u301b\\u0002.\\u0000\\u0016\\u1100\\u0302\\ud16f\\u0000\\u0b06\\u22de\\u060a\\ud772\\u0005\\u2870\\u00b6\\u0600\\u2806\\u043f\\u0600\\u022c\\u1afe\\ud772\\u0005\\u0670\\ufffd\\u0000\\u7a06\\u2a07\\u0000\\u1001\\u0000\\u0000\\u0000\\u0a0a\\u2200\\u0006\\u0100\\u021e\\u2728\\u0000\\u2a0a\\u0256\\ud228\\u0000\\u0206\\u2803\\u00d5\\u0600\\u0402\\ud728\\u0000\\u2a06\\u021e\\u307b\\u0000\\u2a04\\u0222\\u7d030\\u0400\\u1e2a\\u7b021\\u0400\\u222a\\u0302\\u317d\\u0000\\u2a04\\u3013\\u00038\\u0000\\u0013\\u1100\\u8d1b\\u0004\\u0100\\u060a\\u7216\\u0631\\u7000\\u06a2\\u0217\\ud428\\u0000\\ua206\\u1806\\u3572\\u0006\\ua270\\u1906\\u2802\\u00d6\\u0600\\u06a2\\u721a\\u0641\\u7000\\u06a2\\u8328\\u0000\\u2a0a\\u3013\\u0002<\\u0000\\u0017\\u1100\\u2802\\u00d4\\u0600\\u6f03\\u00cf\\u0600\\ucca5\\u0000\\u0a01\\u2d06\\u7e06.\\u0400\\u022a\\ud628\\u0000\\u0306\\ucf6f\\u0000\\ua506\\u00cc\\u0100\\u070b\\u062d\\u2e7e\\u0000\\u2a04\\u2f7e\\u0000\\u2a04\\u165e\\ucc8c\\u0000\\u8001.\\u0400\\u8c17\\u00cc\\u0100\\u2f80\\u0000\\u2a04\\u021e\\u8528\\u0000\\u2a0a\\u0222\\u2803\\u0086\\u0a00\\u262a\\u0302\\u2804\\u0087\\u0a00\\u262a\\u0302\\u2804\\u0088\\u0a00\\u3a2a\\u2802\\u00d2\\u0600\\u0302\\ue128\\u0000\\u2a06\\u021e\\u327b\\u0000\\u2a04\\u0222\\u7d032\\u0400\\u322a\\u2802\\u00e0\\u0600\\u5f6f\\u0000\\u2a0a\\u0236\\ue028\\u0000\\u0306\\u486f\\b\\u2a06\\u721a\\u0645\\u7000\\u1e2a\\u6f03\\u08dc\\u0600\\u1e2a\\u2802\\u00d2\\u0600\\u3a2a\\u2802\\u00d2\\u0600\\u0302\\ue928\\u0000\\u2a06\\u021e\\u337b\\u0000\\u2a04\\u0222\\u7d033\\u0400\\u7e2a\\u2802\\u00e8\\u0600\\u062d\\u5172\\u0006\\u2a70\\u2802\\u00e8\\u0600\\u6b28\\u0000\\u280a\\u0089\\u0a00\\u1e2a\\u2802\\u00e8\\u0600\\u1a2a\\u5b72\\u0006\\u2a70\\u031e\\ue66f\\b\\u2a06\\u021e\\ud228\\u0000\\u2a06\\u721a\\u0669\\u7000\\u1e2a\\u6f03\\u08ef\\u0600\\u1e2a\\u2802\\u00d2\\u0600\\u3a2a\\u2802$\\u0a00\\u0302\\uf428\\u0000\\u2a06\\u021e\\u347b\\u0000\\u2a04\\u0222\\u7d034\\u0400\\u222a\\u0302\\uf228\\u0000\\u2a06\\u0000\\u3013\\u0005\\u01bb\\u0000\\u0018\\u1100\\u2802\\u00d2\\u0600\\u0402\\uf828\\u0000\\u0206\\u7d036\\u0400\\u0502\\u8a73\\u0000\\u280a\\u008b\\u0a00\\ufa28\\u0000\\u0206\\uf728\\u0000\\u6f06\\u008c\\u0a00\\u060a\\u698e\\u3116\\u0620\\u9a16\\u8d6f\\u0000\\ud00a\\u012c\\u0200\\u7e28\\u0000\\u280a\\u008e\\u0a00\\u072c\\u1702\\u357d\\u0000\\u0204\\uf928\\u0000\\u6f06\\u008f\\u0a00\\u020b\\u357b\\u0000\\u2c04\\u0704\\u5817\\u160b\\u160c\\u060d\\u0813\\u1316\\u2b09\\u1120\\u1108\\u9a09\\u0413\\u0411\\u906f\\u0000\\u2c0a\\u0906\\u5817\\u2b0d\\u0804\\u5817\\u110c\\u1709\\u1358\\u1109\\u1109\\u8e08\\u3269\\u07d8\\u3208\\u0709\\u8e06\\u3e69\\u0089\\u0000\\u1609\\u4231\\u6b28\\u0000\\u720a\\u0679\\u7000\\u8d1a\\u0004\\u0100\\u0a13\\u0a11\\u0316\\u11a2\\u170a\\u8c08\\u00d0\\u0100\\u11a2\\u180a\\u8e06\\u8c69\\u00d0\\u0100\\u11a2\\u190a\\u8c07\\u00d0\\u0100\\u11a2\\u280al\\u0a00\\u0513\\u342b\\u6b28\\u0000\\u720a\\u071a\\u7000\\u8d19\\u0004\\u0100\\u0b13\\u0b11\\u0316\\u11a2\\u170b\\u8c08\\u00d0\\u0100\\u11a2\\u180b\\u8c07\\u00d0\\u0100\\u11a2\\u280bl\\u0a00\\u0513\\u0511\\ub928\\u0000\\u1106\\u7305\\u0112\\u0600\\u027a\\u2802\\u00f7\\u0600\\uba28\\u0005\\u7d067\\u0400\\u8e06\\u0269\\uf928\\u0000\\u6f06\\u008f\\u0a00\\u5931\\u0602\\u698e\\u2802\\u00f9\\u0600\\u8f6f\\u0000\\u590a\\u048d\\u0000\\u7d018\\u0400\\u2802\\u00f9\\u0600\\u8f6f\\u0000\\u130a\\u2b06\\u0628\\u0611\\u139a\\u0207\\u387b\\u0000\\u1104\\u0206\\uf928\\u0000\\u6f06\\u008f\\u0a00\\u1159\\u6f07\\u0091\\u0a00\\u11a2\\u1706\\u1358\\u1106\\u0606\\u698e\\ud132\\u022a\\u7d148\\u0400\\u1e2a\\u7b029\\u0400\\u222a\\u0302\\u397d\\u0000\\u2a04\\u021e\\u3a7b\\u0000\\u2a04\\u0222\\u7d03:\\u0400*\\u0000\\u3013\\u0002q\\u0000\\u0019\\u1100\\u5a73\\u0000\\u0a0a\\u0206\\u367b\\u0000\\u6f04^\\u0a00\\u0626\\u3172\\u0006\\u6f70^\\u0a00\\u7e26[\\u0a00\\u160b\\u2b0c\\u0227\\uf928\\u0000\\u0806\\u926f\\u0000\\u0d0a\\u0706\\u5e6f\\u0000\\u260a\\u0906\\u706f\\u0000\\u260a\\u9a72\\u0007\\u0b70\\u1708\\u0c58\\u0208\\uf928\\u0000\\u6f06\\u008f\\u0a00\\ucb32\\u7206\\u0641\\u7000\\u5e6f\\u0000\\u260a\\u6f06_\\u0a00*\\u0000\\u3013\\u0004\\u00b5\\u0000\\u001a\\u1100\\u7b025\\u0400\\u032d\\u2b16\\u1701\\u020a\\u387b\\u0000\\u2d04\\u1603\\u082b\\u7b028\\u0400\\u698e\\u020b\\uf928\\u0000\\u6f06\\u008f\\u0a00\\u5806\\u5807\\u048d\\u0000\\u0c01\\u0d16\\u1f2b\\u2802\\u00f9\\u0600\\u6f09\\u0092\\u0a00\\u0413\\u0908\\u5806\\u0411\\u6f03\\u00cf\\u0600\\u09a2\\u5817\\u090d\\u2802\\u00f9\\u0600\\u8f6f\\u0000\\u320a\\u02d3\\u357b\\u0000\\u2c04\\u0804\\u0316\\u02a2\\u387b\\u0000\\u2c04\\u022c\\u387b\\u0000\\u8e04\\u1769\\u1359\\u2b05\\u0819\\u8e08\\u1169\\u5905\\u5917\\u7b028\\u0400\\u0511\\ua29a\\u0511\\u5917\\u0513\\u0511\\u2f16\\u02e2\\u377b\\u0000\\u1404\\u6f08\\u05bc\\u0600\\u222a\\u0302\\u936f\\u0000\\u2a0a\\u0000\\u3013\\u0003\\u0011\\u0000\\u001b\\u1100\\u0a04\\u0302\\u2d06\\u1a03\\u012b\\u6f1b\\u0094\\u0a00*\\u0000\\u3013\\u0003\\u0017\\u0000\\u001b\\u1100\\u0a04\\u0302\\u2d06\\u1a03\\u012b\\u6f1b\\u0095\\u0a00\\ufe16\\u1604\\u01fe*\\u3013\\u0003\\u0011\\u0000\\u001b\\u1100\\u0a04\\u0302\\u2d06\\u1a03\\u012b\\u6f1b\\u0096\\u0a00*\\u0000\\u3013\\u0003\\u0011\\u0000\\u001b\\u1100\\u0a04\\u0302\\u2d06\\u1a03\\u012b\\u6f1b\\u0097\\u0a00\\u1e2a\\u6f02m\\u0a00\\u1e2a\\u2802$\\u0a00\\u3a2a\\u2802\\u00d2\\u0600\\u0302\\u0628\\u0001\\u2a06\\u021e\\u3b7b\\u0000\\u2a04\\u0222\\u7d03;\\u0400\\u5a2a\\ua072\\u0007\\u0270\\u0528\\u0001\\u7206\\u0641\\u7000\\u9828\\u0000\\u2a0a\\u026a\\u0528\\u0001\\u0306\\ucf6f\\u0000\\ua506\\u00cc\\u0100\\ufe16\\u8c01\\u00cc\\u0100\\u562a\\u2802\\u00d2\\u0600\\u0302\\u0b28\\u0001\\u0206\\u2804\\u010d\\u0600\\u1e2a\\u7b02>\\u0400\\u222a\\u0302\\u3e7d\\u0000\\u2a04\\u021e\\u3f7b\\u0000\\u2a04\\u0222\\u7d03?\\u0400*\\u3013\\u00038\\u0000\\u0013\\u1100\\u8d1b\\u0004\\u0100\\u060a\\u7216\\u0631\\u7000\\u06a2\\u0217\\u0a28\\u0001\\ua206\\u1806\\uac72\\u0007\\ua270\\u1906\\u2802\\u010c\\u0600\\u06a2\\u721a\\u0641\\u7000\\u06a2\\u8328\\u0000\\u2a0a\\u3013\\u0002<\\u0000\\u0017\\u1100\\u2802\\u010a\\u0600\\u6f03\\u00cf\\u0600\\ucca5\\u0000\\u0a01\\u2c06\\u7e06=\\u0400\\u022a\\u0c28\\u0001\\u0306\\ucf6f\\u0000\\ua506\\u00cc\\u0100\\u070b\\u062c\\u3d7e\\u0000\\u2a04\\u3c7e\\u0000\\u2a04\\u165e\\ucc8c\\u0000\\u8001<\\u0400\\u8c17\\u00cc\\u0100\\u3d80\\u0000\\u2a04\\u021e\\u8528\\u0000\\u2a0a\\u0222\\u2803\\u0086\\u0a00\\u262a\\u0302\\u2804\\u0087\\u0a00\\u262a\\u0302\\u2804\\u0088\\u0a00\\u6a2a\\u2802'\\u0a00\\u0402\\u417d\\u0000\\u0204\\u7303\\u0132\\u0600\\u407d\\u0000\\u2a04\\u0232\\u6028\\u0001\\u2806\\u0117\\u0600*\\u0000\\u3013\\u0002C\\u0000\\u001c\\u1100\\u2d02\\u1402\\u022a\\ucc73\\u0005\\u0306\\u1573\\u0001\\u0a06\\u6f06\\u0120\\u0600\\u060b\\u407b\\u0000\\u6f04\\u013d\\u0600\\u1b2d\\ub672\\u0007\\u0670\\u407b\\u0000\\u6f04\\u0137\\u0600\\u9928\\u0000\\u730a\\u0112\\u0600\\u077a*\\u3013\\u0002\\u0011\\u0000\\u001c\\u1100\\u0302\\u1573\\u0001\\u0a06\\u6f06\\u0120\\u0600\\u070b*\\u0000\\u301b\\u0005\\u00b2\\u0000\\u001d\\u1100\\u9a73\\u0000\\u0a0a\\u262b\\u0206\\u2028\\u0001\\u6f06\\u009b\\u0a00\\u7b02@\\u0400\\u356f\\u0001\\u1f06\\u3310\\u0227\\u407b\\u0000\\u6f04\\u0140\\u0600\\u7b02@\\u0400\\u3d6f\\u0001\\u2d06\\u020f\\u407b\\u0000\\u6f04\\u0135\\u0600\\u0e1f\\ube33\\u7b02@\\u0400\\u0e1f\\u3a6f\\u0001\\u0206\\u417b\\u0000\\u6f04\\u016d\\u0600\\u6f03\\u009c\\u0a00\\u030b\\u0607\\uf673\\u0000\\u0d06\\u3cde\\u080c\\ufffd\\u0007\\u1770\\u048d\\u0000\\u1301\\u1104\\u1604\\ua203\\u0411\\ub228\\u0000\\u0806\\u3f28\\u0004\\u2c06\\ufe02\\u721a\\u0818\\u7000\\u7203\\u084c\\u7000\\u9d28\\u0000\\u080a\\u1373\\u0001\\u7a06\\u2a09\\u0000\\u1001\\u0000\\u0000W\\u741d\\u3c00\\u0006\\u0100\\u3013\\u0003\\u0279\\u0000\\u001e\\u1100\\u7b02@\\u0400\\u0d1f\\u3f6f\\u0001\\u2c06\\u0221\\u407b\\u0000\\u6f04\\u0140\\u0600\\u2802\\u0120\\u0600\\u020a\\u407b\\u0000\\u1f04\\u6f0e\\u013a\\u0600\\u2a06\\u7b02@\\u0400\\u141f\\u3f6f\\u0001\\u3906\\u0088\\u0000\\u7b02@\\u0400\\u406f\\u0001\\u0206\\u407b\\u0000\\u6f04\\u013e\\u0600\\u202d\\u5072\\b\\u0270\\u407b\\u0000\\u6f04\\u0135\\u0600\\u3e8c\\u0000\\u2802`\\u0a00\\u1273\\u0001\\u7a06\\u7b02@\\u0400\\u376f\\u0001\\u0b06\\u7b02@\\u0400\\u406f\\u0001\\u0706\\u2e1f\\u9e6f\\u0000\\u160a\\u1732\\u2807k\\u0a00\\u9f28\\u0000\\u650a\\ud28c\\u0000\\u7301\\u00e7\\u0600\\u072a\\u6b28\\u0000\\u280a\\u00a0\\u0a00\\u8c65\\u00d0\\u0100\\ue773\\u0000\\u2a06\\u7b02@\\u0400\\u3e6f\\u0001\\u2c06\\u024e\\u407b\\u0000\\u6f04\\u0137\\u0600\\u020c\\u407b\\u0000\\u6f04\\u0140\\u0600\\u1f08\\u6f2e\\u009e\\u0a00\\u3216\\u0816\\u6b28\\u0000\\u280a\\u009f\\u0a00\\ud28c\\u0000\\u7301\\u00e7\\u0600\\u082a\\u6b28\\u0000\\u280a\\u00a0\\u0a00\\ud08c\\u0000\\u7301\\u00e7\\u0600\\u022a\\u407b\\u0000\\u6f04\\u0135\\u0600\\u3319\\u0229\\u407b\\u0000\\u6f04\\u0139\\u0600\\u7b02A\\u0400\\u4628\\b\\u7306\\u00df\\u0600\\u020d\\u407b\\u0000\\u6f04\\u0140\\u0600\\u2a09\\u7b02@\\u0400\\u356f\\u0001\\u1a06\\uf140\\u0000\\u0200\\u407b\\u0000\\u6f04\\u013b\\u0600\\u0413\\u0411\\u4572\\u0006\\u1b70\\ua128\\u0000\\u2d0a\\u7306\\u00e6\\u0600\\u112a\\u7204\\u065b\\u7000\\u281b\\u00a1\\u0a00\\u062d\\uee73\\u0000\\u2a06\\u0411\\u6972\\u0006\\u1b70\\ua128\\u0000\\u2d0a\\u7306\\u00f1\\u0600\\u112a\\u7204\\u087c\\u7000\\u281b\\u00a1\\u0a00\\u232d\\u7b02@\\u0400\\u0f1f\\u3a6f\\u0001\\u0206\\u407b\\u0000\\u6f04\\u013b\\u0600\\u2a28\\u000b\\u7306\\u00e7\\u0600\\u112a\\u7204\\u088e\\u7000\\u281b\\u00a1\\u0a00\\u0c2d\\u8c17\\u00cc\\u0100\\ue773\\u0000\\u2a06\\u0411\\u9872\\b\\u1b70\\ua128\\u0000\\u2d0a\\u160c\\ucc8c\\u0000\\u7301\\u00e7\\u0600\\u112a\\u7204\\u0651\\u7000\\u281b\\u00a1\\u0a00\\u072d\\u7314\\u00e7\\u0600\\u022a\\u407b\\u0000\\u6f04\\u0135\\u0600\\u0d1f\\u1833\\u7b02@\\u0400\\u406f\\u0001\\u0206\\u0411\\u1928\\u0001\\u1306\\u1105\\u2a05\\ub672\\u0007\\u0270\\u407b\\u0000\\u6f04\\u0137\\u0600\\u9928\\u0000\\u730a\\u0112\\u0600z\\u0000\\u3013\\u0003\\u00f7\\u0000\\u001f\\u1100\\u2802\\u011a\\u0600\\u020a\\u407b\\u0000\\u1f04\\u6f0b\\u013f\\u0600\\u192c\\u7b02@\\u0400\\u406f\\u0001\\u0606\\u2802\\u011a\\u0600\\u7316\\u0121\\u0600\\u022a\\u407b\\u0000\\u1f04\\u6f0c\\u013f\\u0600\\u192c\\u7b02@\\u0400\\u406f\\u0001\\u0606\\u2802\\u011a\\u0600\\u7317\\u0121\\u0600\\u022a\\u407b\\u0000\\u1d04\\u3f6f\\u0001\\u2c06\\u0219\\u407b\\u0000\\u6f04\\u0140\\u0600\\u0206\\u1a28\\u0001\\u1806\\u2173\\u0001\\u2a06\\u7b02@\\u0400\\u6f1e\\u013f\\u0600\\u192c\\u7b02@\\u0400\\u406f\\u0001\\u0606\\u2802\\u011a\\u0600\\u7319\\u0121\\u0600\\u022a\\u407b\\u0000\\u1f04\\u6f09\\u013f\\u0600\\u192c\\u7b02@\\u0400\\u406f\\u0001\\u0606\\u2802\\u011a\\u0600\\u731a\\u0121\\u0600\\u022a\\u407b\\u0000\\u1f04\\u6f0a\\u013f\\u0600\\u192c\\u7b02@\\u0400\\u406f\\u0001\\u0606\\u2802\\u011a\\u0600\\u731b\\u0121\\u0600\\u062a\\ufe2a\\u7b02@\\u0400\\ua472\\b\\u6f70\\u013c\\u0600\\u0f2d\\u7b02@\\u0400\\u111f\\u3f6f\\u0001\\u2c06\\u0217\\u407b\\u0000\\u6f04\\u0140\\u0600\\u2802\\u011c\\u0600\\u0473\\u0001\\u2a06\\u2802\\u011b\\u0600*\\u3013\\u0002D\\u0000\\u001f\\u1100\\u2802\\u011c\\u0600\\u2b0a\\u0218\\u407b\\u0000\\u6f04\\u0140\\u0600\\u0206\\u1c28\\u0001\\u7306\\u00d3\\u0600\\u020a\\u407b\\u0000\\u7204\\u08ac\\u7000\\u3c6f\\u0001\\u2d06\\u02d6\\u407b\\u0000\\u1f04\\u6f12\\u013f\\u0600\\uc72d\\u2a06\\u3013\\u0002D\\u0000\\u001f\\u1100\\u2802\\u011d\\u0600\\u2b0a\\u0218\\u407b\\u0000\\u6f04\\u0140\\u0600\\u0206\\u1d28\\u0001\\u7306\\u0109\\u0600\\u020a\\u407b\\u0000\\u7204\\u08b4\\u7000\\u3c6f\\u0001\\u2d06\\u02d6\\u407b\\u0000\\u1f04\\u6f13\\u013f\\u0600\\uc72d\\u2a06\\u021e\\u1e28\\u0001\\u2a06\\u021e\\u1f28\\u0001\\u2a06\\u0272\\ud228\\u0000\\u0206\\u2803\\u0123\\u0600\\u0402\\u2528\\u0001\\u0206\\u2805\\u0127\\u0600\\u1e2a\\u7b02C\\u0400\\u222a\\u0302\\u437d\\u0000\\u2a04\\u021e\\u447b\\u0000\\u2a04\\u0222\\u7d03D\\u0400\\u1e2a\\u7b02E\\u0400\\u222a\\u0302\\u457d\\u0000\\u2a04\\u3013\\u0003I\\u0000\\u0013\\u1100\\u8d1d\\u0004\\u0100\\u060a\\u7216\\u0631\\u7000\\u06a2\\u0217\\u2228\\u0001\\ua206\\u1806\\uaf72\\u0004\\ua270\\u1906\\u2802\\u0130\\u0600\\u06a2\\u721a\\u04af\\u7000\\u06a2\\u021b\\u2428\\u0001\\ua206\\u1c06\\u4172\\u0006\\ua270\\u2806\\u0083\\u0a00*\\u0000\\u3013\\u0003(\\u0000 \\u1100\\u2802\\u0122\\u0600\\u6f03\\u00cf\\u0600\\u020a\\u2428\\u0001\\u0306\\ucf6f\\u0000\\u0b06\\u0706\\u2802\\u0126\\u0600\\u2a28\\u0001\\u2a06\\u3013\\u0003\\u00bb\\u0000!\\u1100\\ua228\\u0000\\u0a0a\\u000f\\u010f\\u2b28\\u0001\\u0406\\u070b\\u0645\\u0000\\u0200\\u0000\\u1300\\u0000\\u6000\\u0000\\u2700\\u0000\\u4c00\\u0000\\u3800\\u0000\\u2b00\\u066f\\u0302\\ua36f\\u0000\\u160a\\u01fe\\ucc8c\\u0000\\u2a01\\u0206\\u6f03\\u00a3\\u0a00\\ufe16\\u1601\\u01fe\\ucc8c\\u0000\\u2a01\\u0206\\u6f03\\u00a3\\u0a00\\ufe16\\u8c02\\u00cc\\u0100\\u062a\\u0302\\ua36f\\u0000\\u160a\\u04fe\\ufe16\\u8c01\\u00cc\\u0100\\u062a\\u0302\\ua36f\\u0000\\u160a\\u02fe\\ufe16\\u8c01\\u00cc\\u0100\\u062a\\u0302\\ua36f\\u0000\\u160a\\u04fe\\ucc8c\\u0000\\u2a01\\uba72\\b\\u0470\\u3b8c\\u0000\\u7202\\u08e4\\u7000\\u9828\\u0000\\u730a\\u00a4\\u0a00z\\u3013\\u0004\\u0091\\u0000\\\"\\u1100\\u5002\\u042c\\u5003\\u012d\\u022a\\u6f50\\u00a5\\u0a00\\u030a\\u6f50\\u00a5\\u0a00\\u060b\\u2807\\u008e\\u0a00\\u012c\\u062a\\u2e28\\u0001\\u0c06\\u2807\\u012e\\u0600\\u080d\\u2f09\\u030c\\u0206\\u2807\\u012d\\u0600\\u0d2c\\u022a\\u0307\\u2806\\u012d\\u0600\\u012c\\u1b2a\\ubf8d\\u0000\\u1301\\u1104\\u1604\\u0a72\\t\\ua270\\u0411\\u0617\\ua66f\\u0000\\ua20a\\u0411\\u7218\\u0946\\u7000\\u11a2\\u1904\\u6f07\\u00a6\\u0a00\\u11a2\\u1a04\\u5672\\t\\ua270\\u0411\\ua728\\u0000\\u730a\\u00dc\\u0600z\\u0000\\u301b\\u0003\\u0177\\u0000\\u001b\\u1100\\ud0037\\u0100\\u7e28\\u0000\\u280a\\u008e\\u0a00\\u1a2c\\u0202\\u2850k\\u0a00\\ua828\\u0000\\u8c0a7\\u0100\\u1751\\ufffd\\u0149\\u0000\\ud003\\u00d2\\u0100\\u7e28\\u0000\\u280a\\u008e\\u0a00\\u1a2c\\u0202\\u2850k\\u0a00\\ua928\\u0000\\u8c0a\\u00d2\\u0100\\u1751\\ufffd\\u011d\\u0000\\ud003\\u00d6\\u0100\\u7e28\\u0000\\u280a\\u008e\\u0a00\\u1a2c\\u0202\\u2850k\\u0a00\\uaa28\\u0000\\u8c0a\\u00d6\\u0100\\u1751\\ufffd\\u00f1\\u0000\\ud0039\\u0100\\u7e28\\u0000\\u280a\\u008e\\u0a00\\u1a2c\\u0202\\u2850k\\u0a00\\uab28\\u0000\\u8c0a9\\u0100\\u1751\\ufffd\\u00c5\\u0000\\ud003\\u00d7\\u0100\\u7e28\\u0000\\u280a\\u008e\\u0a00\\u1a2c\\u0202\\u2850k\\u0a00\\uac28\\u0000\\u8c0a\\u00d7\\u0100\\u1751\\ufffd\\u0099\\u0000\\ud003\\u00d0\\u0100\\u7e28\\u0000\\u280a\\u008e\\u0a00\\u172c\\u0202\\u2850k\\u0a00\\uad28\\u0000\\u8c0a\\u00d0\\u0100\\u1751\\ufffd\\u0370\\uccd0\\u0000\\u2801~\\u0a00\\u8e28\\u0000\\u2c0a\\u0217\\u5002\\u6b28\\u0000\\u280a\\u00ae\\u0a00\\ucc8c\\u0000\\u5101\\u0a17\\u47de\\ud003\\u00bf\\u0100\\u7e28\\u0000\\u280a\\u008e\\u0a00\\u1c2c\\u0202\\u2850k\\u0a00\\u8928\\u0000\\u510a\\u5c72\\t\\u2870\\u009e\\u0600\\u0a17\\u19de\\u15de\\u7226\\u098e\\u7000\\u5002\\u6f03\\u00a6\\u0a00\\u0828\\u0000\\ufffd\\u1600\\u062a*\\u1c41\\u0000\\u0000\\u0000\\u0000\\u0000\\u015e\\u0000\\u015e\\u0000\\u0015\\u0000\\u0006\\u0100\\u024e\\u2803\\u012c\\u0600\\u022c\\u2a17\\u0504\\u2c28\\u0001\\u2a06\\u3013\\u0003\\u0019\\u0000#\\u1100\\u427e\\u0000\\u0204\\u0012\\uaf6f\\u0000\\u0b0a\\u2c07\\u0602\\u202a\\uffff\\u7fff*\\u0000\\u3013\\u0003\\u00b5\\u0000$\\u1100\\ub073\\u0000\\u0d0a\\ud0097\\u0100\\u7e28\\u0000\\u6f0a\\u00b1\\u0a00\\ud009\\u00d2\\u0100\\u7e28\\u0000\\u6f0a\\u00b1\\u0a00\\ud009\\u00d6\\u0100\\u7e28\\u0000\\u6f0a\\u00b1\\u0a00\\ud0099\\u0100\\u7e28\\u0000\\u6f0a\\u00b1\\u0a00\\ud009\\u00d7\\u0100\\u7e28\\u0000\\u6f0a\\u00b1\\u0a00\\ud009\\u00d0\\u0100\\u7e28\\u0000\\u6f0a\\u00b1\\u0a00\\ud009\\u00cc\\u0100\\u7e28\\u0000\\u6f0a\\u00b1\\u0a00\\ud009\\u00bf\\u0100\\u7e28\\u0000\\u6f0a\\u00b1\\u0a00\\u0a09\\u6f06\\u00b2\\u0a00\\ub373\\u0000\\u0b0a\\u0c16\\u122b\\u0607\\u6f08\\u00b4\\u0a00\\u6f08\\u00b5\\u0a00\\u1708\\u0c58\\u0608\\ub26f\\u0000\\u320a\\u07e5*\\u0000\\u3013\\u0003k\\u0000%\\u1100\\u2802\\u0126\\u0600\\u060a\\u0645\\u0000\\u0200\\u0000\\u0800\\u0000\\u1400\\u0000\\u0e00\\u0000\\u2000\\u0000\\u1a00\\u0000\\u2b00\\u7224\\u09ce\\u7000\\u722a\\u09d4\\u7000\\u722a\\u09da\\u7000\\u722a\\u09de\\u7000\\u722a\\u09e2\\u7000\\u722a\\u09e8\\u7000\\u722a\\u08ba\\u7000\\u2802\\u0126\\u0600\\u3b8c\\u0000\\u7202\\u08e4\\u7000\\u9828\\u0000\\u730a\\u00a4\\u0a00\\u2e7a\\u2f28\\u0001\\u8006B\\u0400\\u6e2a\\u2802'\\u0a00\\u0302\\u4e7d\\u0000\\u0204\\u2817\\u0136\\u0600\\u2802\\u0140\\u0600\\u1e2a\\u7b02O\\u0400\\u222a\\u0302\\u4f7d\\u0000\\u2a04\\u021e\\u507b\\u0000\\u2a04\\u0222\\u7d03P\\u0400\\u1e2a\\u7b02Q\\u0400\\u222a\\u0302\\u517d\\u0000\\u2a04\\u0000\\u3013\\u0004&\\u0000&\\u1100\\u2802\\u0137\\u0600\\u060a\\u0617\\u6d6f\\u0000\\u180a\\u6f59\\u00b6\\u0a00\\uee72\\t\\u7270\\u084c\\u7000\\ub76f\\u0000\\u2a0a\\u0000\\u3013\\u0003c\\u0000\\u0013\\u1100\\u2802\\u0135\\u0600\\u2e03\\u1d53\\u048d\\u0000\\u0a01\\u1606\\uf472\\t\\ua270\\u1706\\u8c03>\\u0200\\u06a2\\u7218\\u0a26\\u7000\\u06a2\\u0219\\u3528\\u0001\\u8c06>\\u0200\\u06a2\\u721a\\u0a34\\u7000\\u06a2\\u021b\\u3728\\u0001\\ua206\\u1c06\\u3a72\\n\\ua270\\u2806\\u0083\\u0a00\\u1273\\u0001\\u7a06\\u2802\\u0140\\u0600*\\u3013\\u0002#\\u0000&\\u1100\\u2802\\u0135\\u0600\\u2e1a\\u720b\\u0a40\\u7000\\u1273\\u0001\\u7a06\\u2802\\u0137\\u0600\\u020a\\u4028\\u0001\\u0606\\u7a2a\\u2802\\u0135\\u0600\\u2e1a\\u1602\\u022a\\u3728\\u0001\\u0306\\u6f1b\\u0094\\u0a00\\u022d\\u2a16\\u2a17\\u0232\\u3528\\u0001\\u2c06\\u1602\\u172a\\u2a2a\\u2802\\u0135\\u0600\\ufe18\\u2a01\\u022a\\u3528\\u0001\\u0306\\u01fe*\\u0000\\u3013\\u0003\\u0106\\u0000'\\u1100\\u2802\\u0135\\u0600\\u0b2d\\u6872\\n\\u7370\\u0112\\u0600\\u027a\\u4728\\u0001\\u0206\\u2802\\u0133\\u0600\\u3428\\u0001\\u0206\\u4828\\u0001\\u0a06\\u1506\\u0833\\u1602\\u3628\\u0001\\u2a06\\ud106\\u070b\\ub828\\u0000\\u2c0a\\u0208\\u2807\\u0146\\u0600\\u072a\\u271f\\u0833\\u0702\\u4428\\u0001\\u2a06\\u1f07\\u2e5f\\u0708\\ub928\\u0000\\u2c0a\\u0208\\u2807\\u0145\\u0600\\u072a\\u7d1f\\u052e\\u1f07\\u333a\\u0208\\u2816\\u0136\\u0600\\u022a\\u0112\\uba28\\u0000\\u280a\\u0138\\u0600\\u0702\\u4128\\u0001\\u0c06\\u2c08\\u2a01\\u0702\\u4228\\u0001\\u0c06\\u2c08\\u2a01\\u1f07\\u3220\\u0747\\u8020\\u0000\\u2f00\\u7e3fM\\u0400\\u9407\\u090d\\u161f\\u1c2e\\u0902\\u3628\\u0001\\u0206\\u1707\\ubb73\\u0000\\u280a\\u0138\\u0600\\u2802\\u0149\\u0600\\u2a26\\ua872\\n\\u0770\\ufffd\\u2801`\\u0a00\\u1273\\u0001\\u7a06\\ud472\\n\\u0770\\ufffd\\u2801`\\u0a00\\u1273\\u0001\\u7a06\\u0000\\u3013\\u0002\\u00b3\\u0000(\\u1100\\u1f03\\u333c\\u0264\\u4928\\u0001\\u2606\\u2802\\u0148\\u0600\\u060a\\u3e1f\\u1c33\\u1f02\\u280c\\u0136\\u0600\\u7202\\u0af4\\u7000\\u3828\\u0001\\u0206\\u4928\\u0001\\u2606\\u2a17\\u1f06\\u333d\\u021c\\u091f\\u3628\\u0001\\u0206\\ue872\\t\\u2870\\u0138\\u0600\\u2802\\u0149\\u0600\\u1726\\u022a\\u281d\\u0136\\u0600\\u7202\\u09de\\u7000\\u3828\\u0001\\u1706\\u032a\\u3e1f\\u4333\\u2802\\u0149\\u0600\\u0226\\u4828\\u0001\\u0b06\\u1f07\\u333d\\u021c\\u0a1f\\u3628\\u0001\\u0206\\ue272\\t\\u2870\\u0138\\u0600\\u2802\\u0149\\u0600\\u1726\\u022a\\u281e\\u0136\\u0600\\u7202\\u09da\\u7000\\u3828\\u0001\\u1706\\u162a*\\u3013\\u0002\\u0112\\u0000)\\u1100\\u1f03\\u3321\\u0244\\u4928\\u0001\\u2606\\u2802\\u0148\\u0600\\u060a\\u3d1f\\u1c33\\u1f02\\u280c\\u0136\\u0600\\u7202\\u09d4\\u7000\\u3828\\u0001\\u0206\\u4928\\u0001\\u2606\\u2a17\\u1f02\\u2811\\u0136\\u0600\\u7202\\u0afa\\u7000\\u3828\\u0001\\u1706\\u032a\\u261f\\u3a33\\u2802\\u0149\\u0600\\u0226\\u4828\\u0001\\u0b06\\u1f07\\u3326\\u021c\\u121f\\u3628\\u0001\\u0206\\ufe72\\n\\u2870\\u0138\\u0600\\u2802\\u0149\\u0600\\u1726\\u722a\\u0b04\\u7000\\u1273\\u0001\\u7a06\\u1f03\\u337c\\u023a\\u4928\\u0001\\u2606\\u2802\\u0148\\u0600\\u080c\\u7c1f\\u1c33\\u1f02\\u2813\\u0136\\u0600\\u7202\\u0b38\\u7000\\u3828\\u0001\\u0206\\u4928\\u0001\\u2606\\u2a17\\u3e72\\u000b\\u7370\\u0112\\u0600\\u037a\\u3d1f\\u4433\\u2802\\u0149\\u0600\\u0226\\u4828\\u0001\\u0d06\\u1f09\\u333d\\u021c\\u0b1f\\u3628\\u0001\\u0206\\uce72\\t\\u2870\\u0138\\u0600\\u2802\\u0149\\u0600\\u1726\\u022a\\u0b1f\\u3628\\u0001\\u0206\\u7272\\u000b\\u2870\\u0138\\u0600\\u2a17\\u2a16\\u0000\\u3013\\u0003\\u00e6\\u0000*\\u1100\\u8d1c=\\u0200\\u0413\\u0411\\u8f16=\\u0200\\u281f\\u0d1f\\u4b73\\u0001\\u8106=\\u0200\\u0411\\u8f17=\\u0200\\u291f\\u0e1f\\u4b73\\u0001\\u8106=\\u0200\\u0411\\u8f18=\\u0200\\u2e1f\\u0f1f\\u4b73\\u0001\\u8106=\\u0200\\u0411\\u8f19=\\u0200\\u2c1f\\u101f\\u4b73\\u0001\\u8106=\\u0200\\u0411\\u8f1a=\\u0200\\u211f\\u111f\\u4b73\\u0001\\u8106=\\u0200\\u0411\\u8f1b=\\u0200\\u2d1f\\u141f\\u4b73\\u0001\\u8106=\\u0200\\u0411\\u200a\\u0080\\u0000\\u3e8d\\u0000\\u0b02\\u0c16\\u092b\\u0807\\u161f\\u089e\\u5817\\u080c\\u8020\\u0000\\u3200\\u06ef\\u0513\\u1316\\u2b06\\u1125\\u1105\\u8f06=\\u0200\\u3d71\\u0000\\u0d02\\u1207\\u7b03R\\u0400\\u0312\\u537b\\u0000\\u9e04\\u0611\\u5817\\u0613\\u0611\\u0511\\u698e\\ud332\\u2a07\\u0000\\u3013\\u0002v\\u0000+\\u1100\\u1902\\u3628\\u0001\\u7306Z\\u0a00\\u070b\\u6f03\\u00bc\\u0a00\\u0226\\u4928\\u0001\\u2606\\u312b\\ud106\\u0110\\u0207\\u4928\\u0001\\ud106\\ubc6f\\u0000\\u260a\\u1f03\\u3327\\u021a\\u4828\\u0001\\u1f06\\u3327\\u071b\\u271f\\ubc6f\\u0000\\u260a\\u2802\\u0149\\u0600\\u0226\\u4828\\u0001\\u2506\\u150a\\uc433\\u1506\\u0b33\\u7672\\u000b\\u7370\\u0112\\u0600\\u027a\\u6f07_\\u0a00\\u3828\\u0001\\u2a06\\u0000\\u3013\\u0002Y\\u0000+\\u1100\\u1a02\\u3628\\u0001\\u7306Z\\u0a00\\u070b\\u6f03\\u00bc\\u0a00\\u0226\\u4928\\u0001\\u2606\\u232b\\ud106\\u5f1f\\u0f2e\\ud106\\u2d1f\\u092e\\ud106\\ubd28\\u0000\\u2c0a\\u0719\\u2802\\u0149\\u0600\\u6fd1\\u00bc\\u0a00\\u0226\\u4828\\u0001\\u2506\\u150a\\ud233\\u0702\\u5f6f\\u0000\\u280a\\u0138\\u0600*\\u0000\\u3013\\u0002U\\u0000+\\u1100\\u1802\\u3628\\u0001\\u7306Z\\u0a00\\u070b\\u6f03\\u00bc\\u0a00\\u0226\\u4928\\u0001\\u2606\\u1f2b\\ud106\\u0110\\u2803\\u00b8\\u0a00\\u052d\\u1f03\\u332e\\u0719\\u2802\\u0149\\u0600\\u6fd1\\u00bc\\u0a00\\u0226\\u4828\\u0001\\u2506\\u150a\\ud633\\u0702\\u5f6f\\u0000\\u280a\\u0138\\u0600*\\u0000\\u3013\\u0002\\u001f\\u0000\\u0002\\u1100\\u112b\\ud106\\ube28\\u0000\\u2d0a\\u2a01\\u2802\\u0149\\u0600\\u0226\\u4828\\u0001\\u2506\\u150a\\ue433\\u322a\\u7b02N\\u0400\\ud06f\\u0005\\u2a06\\u0232\\u4e7b\\u0000\\u6f04\\u05d1\\u0600\\u2e2a\\u4328\\u0001\\u8006M\\u0400\\u3e2a\\u0302\\u527d\\u0000\\u0204\\u7d04S\\u0400\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802$\\u0a00\\u562a\\u2802$\\u0a00\\u0302\\u5028\\u0001\\u0206\\u2804\\u0152\\u0600\\u1e2a\\u7b02q\\u0400\\u222a\\u0302\\u717d\\u0000\\u2a04\\u021e\\u727b\\u0000\\u2a04\\u0222\\u7d03r\\u0400\\u3a2a\\u2802\\u00c0\\u0a00\\u0302\\u5528\\u0001\\u2a06\\u021e\\u737b\\u0000\\u2a04\\u0222\\u7d03s\\u0400*\\u0000\\u301b\\u0002&\\u0000,\\u1100\\u6f04\\u0443\\u0600\\u030a\\u3574\\u0000\\u0601\\u2173\\u0002\\u0c06\\u0ede\\u070b\\ue072\\u000b\\u2870\\u00bf\\u0600\\u1afe\\u2a08\\u0000\\u1001\\u0000\\u0000\\u0000\\u1616\\u0e00\\u0006\\u0100\\u0236\\u2805\\u090d\\u0600\\u5628\\u0001\\u2a06\\u021e\\u2728\\u0000\\u2a0a\\u0000\\u3013\\u0003'\\u0000-\\u1100\\u7e7e\\u0000\\u0a04\\u0b06\\u0207\\uc128\\u0000\\u740a\\u0014\\u1b00\\u7f0c~\\u0400\\u0708\\u0928\\u0000\\u0a2b\\u0706\\ue033*\\u3013\\u0003'\\u0000-\\u1100\\u7e7e\\u0000\\u0a04\\u0b06\\u0207\\uc328\\u0000\\u740a\\u0014\\u1b00\\u7f0c~\\u0400\\u0708\\u0928\\u0000\\u0a2b\\u0706\\ue033*\\u3013\\u0003\\u00f3\\u0000.\\u1100\\u2802\\u0dac\\u0600\\u7d7d\\u0000\\u0204\\u2728\\u0000\\u020a\\ufe14\\u4106\\u0004\\u7306\\u0159\\u0600\\u6328\\u0001\\u0206\\u7302\\u00c4\\u0a00\\u767d\\u0000\\u0204\\u7302\\u00c5\\u0a00\\u777d\\u0000\\u0204\\u7302\\u0190\\u0600\\u787d\\u0000\\u0204\\u7302\\u00c6\\u0a00\\u797d\\u0000\\u0204\\uc773\\u0000\\u7d0az\\u0400\\u0202\\uc873\\u0000\\u7d0a{\\u0400\\u0202\\uc973\\u0000\\u7d0a|\\u0400\\u7302\\u00ca\\u0a00\\u070b\\u7b02v\\u0400\\ucb6f\\u0000\\u070a\\u7b02w\\u0400\\ucb6f\\u0000\\u070a\\u7b02x\\u0400\\ucb6f\\u0000\\u070a\\u7b02y\\u0400\\ucb6f\\u0000\\u070a\\u7b02z\\u0400\\ucb6f\\u0000\\u070a\\u7b02{\\u0400\\ucb6f\\u0000\\u070a\\u7b02|\\u0400\\ucb6f\\u0000\\u070a\\u757d\\u0000\\u0304\\u160c\\u2b0d\\u080f\\u9a09\\u020a\\u2806\\u016e\\u0600\\u1709\\u0d58\\u0809\\u698e\\ueb32\\u5e2a\\u747e\\u0000\\u2d04\\u280a\\u0174\\u0600\\u7480\\u0000\\u7e04t\\u0400\\u1e2a\\u8002t\\u0400\\u1e2a\\u7b02\\u007f\\u0400\\u222a\\u0302\\u7f7d\\u0000\\u2a04\\u021e\\u767b\\u0000\\u2a04\\u021e\\u777b\\u0000\\u2a04\\u021e\\u787b\\u0000\\u2a04\\u021e\\u787b\\u0000\\u2a04\\u021e\\u797b\\u0000\\u2a04\\u021e\\u7b7b\\u0000\\u2a04\\u021e\\u7d7b\\u0000\\u2a04\\u0246\\u2503\\u062d\\u2826\\u0dac\\u0600\\u7d7d\\u0000\\u2a04\\u021e\\u7c7b\\u0000\\u2a04\\u021e\\u7a7b\\u0000\\u2a04\\u0236\\u7e03[\\u0a00\\u6f28\\u0001\\u2a06\\u301b\\u0003\\u0088\\u0000/\\u1100\\u7e7e\\u0000\\u2c04\\u032c\\u5373\\u0001\\u0a06\\u7e7e\\u0000\\u0204\\u6f06\\u00cc\\u0a00\\u6f06\\u00cd\\u0a00\\u112c\\u1872\\f\\u0370\\u786f\\u0000\\u280a\\n\\u2b00\\u722a\\u0c5e\\u7000\\u6f03x\\u0a00\\u0b28\\u0000\\u032b\\ub828\\u0005\\u0b06\\u0702\\u7028\\u0001\\u0206\\u757b\\u0000\\u6f04\\u00ce\\u0a00\\u2b0d\\u0914\\ucf6f\\u0000\\u740aI\\u0200\\u080c\\u0407\\u816f\\u0001\\u0906\\u2a6f\\u0000\\u2d0a\\ufffd\\u090a\\u062c\\u6f09\\u0003\\u0a00\\u2adc\\u1001\\u0000\\u0002]\\u7d20\\u0a00\\u0000\\u0000\\u024a\\ua66f\\u0000\\u720a\\u0c86\\u7000\\u6f1b\\u0094\\u0a00*\\u301b\\u0003O\\u00000\\u1100\\u7e03\\u0080\\u0400\\u112d\\ufe14\\u7606\\u0001\\u7306\\u00d0\\u0a00\\u8080\\u0000\\u7e04\\u0080\\u0400\\u0c28\\u0000\\u0a2b\\u6f06\\u00d2\\u0a00\\u2b0c\\u080d\\ud36f\\u0000\\u0b0a\\u2807\\u0171\\u0600\\u6f08*\\u0a00\\ueb2d\\u0ade\\u2c08\\u0806\\u036f\\u0000\\ufffd*\\u1001\\u0000\\u0002+\\u4419\\u0a00\\u0000\\u0000\\u301b\\u0005\\u0099\\u00001\\u1100\\u1402\\ud428\\u0000\\u390a\\u008c\\u0000\\uaa72\\f\\u0270\\ud56f\\u0000\\u280a\\u000b\\u2b00\\u7202\\u0cd8\\u7000\\ud66f\\u0000\\u0a0a\\u1406\\ud728\\u0000\\u2c0a\\u0657\\ufffd\\u2c0a\\u7244\\u0ce8\\u7000\\u9e28\\u0000\\u0606\\u1414\\ufffd\\u260a\\u3c72\\r\\u0270\\ud56f\\u0000\\u280a\\u000b\\u2b00\\u3ade\\u070b\\u8872\\r\\u1770\\u048d\\u0000\\u0c01\\u1608\\u6f02\\u00d5\\u0a00\\u08a2\\ub228\\u0000\\ufffd\\u721b\\u0dcc\\u7000\\u9e28\\u0000\\u2a06\\u4872\\u000e\\u0270\\ud56f\\u0000\\u280a\\u000b\\u2b00*\\u0000\\u1001\\u0000\\u0000C\\u5e1b\\u1f00\\u0006\\u0100\\u301b\\u00015\\u00002\\u1100\\u7b02u\\u0400\\uce6f\\u0000\\u0b0a\\u122b\\u6f07\\u00cf\\u0a00\\u4974\\u0000\\u0a02\\u6f06\\u0180\\u0600\\u6f07*\\u0a00\\ue62d\\u0ade\\u2c07\\u0706\\u036f\\u0000\\ufffd*\\u0000\\u1001\\u0000\\u0002\\f\\u2a1e\\u0a00\\u0000\\u0000\\u301b\\u00037\\u00002\\u1100\\u7b02u\\u0400\\uce6f\\u0000\\u0b0a\\u142b\\u6f07\\u00cf\\u0a00\\u4974\\u0000\\u0a02\\u0306\\u6f04\\u0182\\u0600\\u6f07*\\u0a00\\ue42d\\u0ade\\u2c07\\u0706\\u036f\\u0000\\ufffd*\\u1001\\u0000\\u0002\\f\\u2c20\\u0a00\\u0000\\u0000\\u021e\\u2728\\u0000\\u2a0a\\u0242\\u8e72\\u000e\\u1b70\\u946f\\u0000\\u160a\\u01fe\\u422a\\u7202\\u0ea0\\u7000\\u6f1b\\u0094\\u0a00\\ufe16\\u2a01\\u0242\\uc672\\u000e\\u1b70\\u946f\\u0000\\u160a\\u01fe\\u362a\\u7b02\\u04e9\\u0400\\u2803\\u00da\\u0a00*\\u0000\\u301b\\u0005\\u022c\\u00003\\u1100\\u6ed0\\u0000\\u2802~\\u0a00\\ufffd\\u0a0a\\u8d17)\\u0100\\u0c13\\u0c11\\u0616\\u11a2\\u730c\\u015f\\u0600\\u070b\\u756f\\u0001\\u7306\\u1059\\u0600\\u0813\\u6f06\\u00dc\\u0a00\\u1216\\u2802\\u00dd\\u0a00\\u122d\\uea72\\u000e\\u2870\\u00b0\\u0600\\u1307\\ufffd\\u01d5\\u0000\\u0811\\u6f08\\u00de\\u0a00\\u8028\\u0000\\u7d0a\\u04e9\\u0400\\u0811\\ue97b\\u0004\\u2d04\\u7212\\u0f56\\u7000\\ub028\\u0000\\u0706\\u0b13\\ua8dd\\u0001\\u1100\\u7b08\\u04e9\\u0400\\ufffd\\u0000\\u2d0a\\u7219\\u0fc0\\u7000\\u0811\\ue97b\\u0004\\u2804\\r\\u2b00\\u1307\\ufffd\\u0181\\u0000\\u0811\\ue97b\\u0004\\u7204\\u101a\\u7000\\ue028\\u0000\\u140a\\u06fe\\u00e1\\u0a00\\ue273\\u0000\\u280a\\u000e\\u2b00\\u817e\\u0000\\u2d04\\u1411\\u06fe\\u0177\\u0600\\ue473\\u0000\\u800a\\u0081\\u0400\\u817e\\u0000\\u2804\\u000f\\u2b00\\u827e\\u0000\\u2d04\\u1411\\u06fe\\u0178\\u0600\\ue473\\u0000\\u800a\\u0082\\u0400\\u827e\\u0000\\u2804\\u000f\\u2b00\\u837e\\u0000\\u2d04\\u1411\\u06fe\\u0179\\u0600\\ue473\\u0000\\u800a\\u0083\\u0400\\u837e\\u0000\\u2804\\u000f\\u2b00\\u0811\\u06fe\\u105a\\u0600\\ue273\\u0000\\u280a\\u000e\\u2b00\\u720d\\u102e\\u7000\\u0811\\ue97b\\u0004\\u2804\\u000b\\u2b00\\u6f09\\u00e5\\u0a00\\u0d13\\u702b\\u0d11\\ue66f\\u0000\\u130a\\u7204\\u1072\\u7000\\u0411\\u0a28\\u0000\\u162b\\u0513\\u0411\\ue728\\u0000\\u130a\\u1106\\u2806\\u0089\\u0600\\u1107\\u6f06\\u016e\\u0600\\u1317\\ufffd\\u132b\\u1107\\u2807\\u043f\\u0600\\u022c\\u1afe\\u0711\\ub272\\u0010\\u1770\\u048d\\u0000\\u1301\\u110e\\u160e\\u0411\\u11a2\\u280e\\u00b2\\u0600\\u00de\\u0511\\u0c2c\\u2a72\\u0011\\u1170\\u2804\\n\\u2b00\\u0d11\\u2a6f\\u0000\\u2d0a\\ufffd\\u110c\\u2c0d\\u1107\\u6f0d\\u0003\\u0a00\\ufffd\\u1336\\u1109\\u7209\\u1180\\u7000\\ub628\\u0000\\u1106\\u2809\\u043e\\u0600\\u022c\\u1afe\\u1bde\\u0a13\\u0a11\\u8072\\u0011\\u2870\\u00b6\\u0600\\u0a11\\u3e28\\u0004\\u2c06\\ufe02\\ufffd\\u7200\\u11ca\\u7000\\u9e28\\u0000\\u0706\\u112a\\u2a0b\\u6441\\u0000\\u0000\\u0000\\u0176\\u0000\\u001d\\u0000\\u0193\\u0000+\\u0000\\u0006\\u0100\\u0002\\u0000\\u015c\\u0000}\\u0000\\u01d9\\u0000\\f\\u0000\\u0000\\u0000\\u0000\\u0000+\\u0000\\u01bc\\u0000\\u01e7\\u0000\\u001b\\u0000\\u00dc\\u0100\\u0000\\u0000+\\u0000\\u01bc\\u0000\\u0202\\u0000\\u001b\\u0000\\u00dd\\u0100\\u3013\\u0005\\u018b\\u00004\\u1100\\u6ed0\\u0000\\u2802~\\u0a00\\ue86f\\u0000\\u0a0a\\uee72\\u0011\\u0b70\\ufa72\\u0011\\u0c70\\u0706\\u6f1b\\u0095\\u0a00\\u090d\\u3f16\\u015e\\u0000\\u9a72\\u0007\\u0870\\u0906\\u6f07m\\u0a00\\u6f58\\u00e9\\u0a00\\u9d28\\u0000\\u0a0a\\u6cd0\\u0001\\u2802~\\u0a00\\uea6f\\u0000\\u130a\\u0204\\u767b\\u0000\\u7204\\u1218\\u7000\\u0411\\u3072\\u0012\\u0670\\u9d28\\u0000\\u6f0a\\u00eb\\u0a00\\u7b02v\\u0400\\u5672\\u0012\\u1170\\u7204\\u1260\\u7000\\u2806\\u009d\\u0a00\\ueb6f\\u0000\\u020a\\u767b\\u0000\\u7204\\u1288\\u7000\\u0411\\ub672\\u0012\\u0670\\u9d28\\u0000\\u6f0a\\u00eb\\u0a00\\ueed0\\u0000\\u2802~\\u0a00\\uea6f\\u0000\\u130a\\u0205\\u787b\\u0000\\u7204\\u1304\\u7000\\u0511\\u1a72\\u0013\\u0670\\u9d28\\u0000\\u6f0a\\u00ec\\u0a00\\u7b02x\\u0400\\u4e72\\u0013\\u1170\\u7205\\u1374\\u7000\\u2806\\u009d\\u0a00\\uec6f\\u0000\\u020a\\u787b\\u0000\\u7204\\u13c0\\u7000\\u0511\\ufffd\\u0013\\u0670\\u9d28\\u0000\\u6f0a\\u00ec\\u0a00\\u7b02x\\u0400\\u2272\\u0014\\u1170\\u7205\\u1444\\u7000\\u2806\\u009d\\u0a00\\uec6f\\u0000\\u020a\\u787b\\u0000\\u7204\\u1482\\u7000\\u0511\\ua072\\u0014\\u0670\\u9d28\\u0000\\u6f0a\\u00ec\\u0a00\\u7b02x\\u0400\\ue472\\u0014\\u1170\\u7205\\u150e\\u7000\\u2806\\u009d\\u0a00\\uec6f\\u0000\\u020a\\u787b\\u0000\\u7204\\u1552\\u7000\\u0511\\u7c72\\u0015\\u0670\\u9d28\\u0000\\u6f0a\\u00ec\\u0a00\\u1e2a\\u8014t\\u0400\\u1e2a\\u2802$\\u0a00\\u7a2a\\u2802\\u00ed\\u0a00\\uee73\\u0000\\u7d0a\\u00ef\\u0a00\\u2802'\\u0a00\\u0302\\uf07d\\u0000\\u2a0a\\u0000\\u301b\\u0005K\\u00005\\u1100\\u0c03\\u0d16\\u3e2b\\u0908\\u0a9a\\u0602\\u2804\\u00f1\\u0a00\\u2cde\\u070b\\uc072\\u0015\\u1770\\u048d\\u0000\\u1301\\u1104\\u1604\\u6f06\\u00d5\\u0a00\\u11a2\\u2804\\u00bb\\u0600\\u2807\\u043e\\u0600\\u022c\\u1afe\\u00de\\u1709\\u0d58\\u0809\\u698e\\ubc32*\\u1001\\u0000\\u0000\\n\\u140a\\u2c00\\u0006\\u0100\\u3013\\u0003M\\u00006\\u1100\\ud003G\\u1b00\\u7e28\\u0000\\u160a\\uf26f\\u0000\\u740aH\\u1b00\\u060a\\u322c\\u0c06\\u0d16\\u262b\\u0908\\u47a3\\u0000\\u0b1b\\u0402\\u0112\\u16feG\\u1b00\\uf36f\\u0000\\u2806\\u0099\\u0a00\\u2803\\u00f3\\u0a00\\u1709\\u0d58\\u0809\\u698e\\ud432\\u1e2a\\u2802'\\u0a00\\u362a\\u7b02\\u00f4\\u0a00\\u2816\\u00f5\\u0a00*\\u3013\\u0004&\\u00007\\u1100\\uf673\\u0000\\u0a0a\\u0406\\uf47d\\u0000\\u020a\\uef7b\\u0000\\u030a\\ufe06\\uf706\\u0000\\u730a\\u00f8\\u0a00\\uf96f\\u0000\\u2a0a\\u0232\\uef7b\\u0000\\u6f0a\\u00fa\\u0a00\\u1e2a\\u2802'\\u0a00\\u1e2a\\u7b02\\u00fb\\u0a00*\\u3013\\u0004&\\u00008\\u1100\\ufc73\\u0000\\u0a0a\\u0406\\ufb7d\\u0000\\u020a\\uef7b\\u0000\\u030a\\ufe06\\ufd06\\u0000\\u730a\\u00f8\\u0a00\\uf96f\\u0000\\u2a0a\\u0000\\u301b\\u0003<\\u00009\\u1100\\u7b02\\u00ef\\u0a00\\u1203\\u6f00\\u00fe\\u0a00\\u052d\\u1404\\u1651\\u042a\\u6f06\\u00ff\\u0a00\\u0451\\u1450\\ud428\\u0000\\u0c0a\\u12de\\u070b\\u3e28\\u0004\\u2c06\\ufe02\\u041a\\u5114\\u0c16\\u00de\\u2a08\\u1001\\u0000\\u0000\\u0015\\u2813\\u1200\\u0006\\u0100\\u3013\\u00032\\u0000:\\u1100\\u0302\\u0012(\\u0001\\u2d0a\\u0409\\u15feL\\u1b00\\u2a16\\u0204\\uf07b\\u0000\\u6f0a\\u0162\\u0600\\u6f06\\u015a\\u0600\\u4ca5\\u0000\\u811bL\\u1b00\\u2a17\\u0000\\u3013\\u0004_\\u0000;\\u1100\\u0302\\u0012\\u016f\\u0001\\u2c0a\\u0602\\ud02aL\\u1b00\\u7e28\\u0000\\u6f0a\\u00a6\\u0a00\\uf472\\u0015\\u0370\\u4c72\\b\\u2870\\u0102\\u0a00\\u030b\\u282c\\u7203\\u161c\\u7000\\u6f1b\\u0096\\u0a00\\u0e2d\\u7203\\u162a\\u7000\\u6f1b\\u0096\\u0a00\\u0c2c\\u7207\\u1632\\u7000\\u9928\\u0000\\u0b0a\\u7307\\u0103\\u0a00\\u227a\\u0302\\u0428\\u0001\\u2a0a\\u0222\\u7d14\\u008e\\u0400\\ua22a\\u0202\\u8e7b\\u0000\\u2504\\u0b2d\\u2826\\u00ed\\u0a00\\u0573\\u0001\\u7d0a\\u008e\\u0400\\u7b02\\u008e\\u0400\\u0403\\u066f\\u0001\\u2a0a\\u0000\\u3013\\u0003*\\u0000<\\u1100\\u7b02\\u008e\\u0400\\u172c\\u7b02\\u008e\\u0400\\u1203\\u6f00\\u0107\\u0a00\\u070b\\u052c\\u0604\\u1751\\u022a\\u0403\\u0828\\u0001\\u0c0a\\u2a08\\u0232\\u097e\\u0001\\u280a\\u0198\\u0600\\u922a\\u2802'\\u0a00\\u0302\\ua028\\u0001\\u0206\\u0a73\\u0001\\u280a\\u019e\\u0600\\u7e02\\u02f7\\u0400\\u9a28\\u0001\\u2a06\\u021e\\u907b\\u0000\\u2a04\\u0222\\u7d03\\u0090\\u0400\\u1e2a\\u7b02\\u0091\\u0400\\u222a\\u0302\\u917d\\u0000\\u2a04\\u021e\\u927b\\u0000\\u2a04\\u0222\\u7d03\\u0092\\u0400\\u1e2a\\u7b02\\u0093\\u0400\\u222a\\u0302\\u937d\\u0000\\u2a04\\u023a\\uf57e\\u0002\\u0304\\u2804\\u01a8\\u0600\\u3a2a\\u7e02\\u02f6\\u0400\\u0403\\ua828\\u0001\\u2a06\\u023a\\uf77e\\u0002\\u0304\\u2804\\u01a8\\u0600\\u3a2a\\u7e02\\u02f8\\u0400\\u0403\\ua828\\u0001\\u2a06\\u023a\\uf97e\\u0002\\u0304\\u2804\\u01a8\\u0600\\u6e2a\\u2802\\u019f\\u0600\\u122c\\u2802\\u019f\\u0600\\u0b6f\\u0001\\u020a\\u2814\\u01a0\\u0600*\\u301b\\u0003J\\u0000=\\u1100\\uf328\\b\\u0a06\\u2802\\u019d\\u0600\\u0c6f\\u0001\\u0c0a\\u202b\\u6f08\\u010d\\u0a00\\u060b\\uf16f\\b\\u1206\\u2801\\u010e\\u0a00\\u0112\\u0f28\\u0001\\u6f0a\\u0110\\u0a00\\u6f08*\\u0a00\\ufffd\\u2c08\\u0806\\u036f\\u0000\\ufffd\\u2a06\\u0000\\u1001\\u0000\\u0002\\u0012\\u3e2c\\u0a00\\u0000\\u0000\\u301b\\u0003Q\\u0000>\\u1100\\u0203\\u9928\\u0001\\u2806\\u0b26\\u0600\\u422c\\u2c05\\u0514\\u698e\\u3116\\u280ek\\u0a00\\u0504\\u6c28\\u0000\\u100a\\u2802\\u0111\\u0a00\\u7e0a\\u008f\\u0400\\u6f03\\u0112\\u0a00\\u1328\\u0001\\u020a\\u9f28\\u0001\\u0406\\u726f\\u0000\\ufffd\\u0607\\u1328\\u0001\\ufffd*\\u0000\\u1001\\u0000\\u0002;\\u490e\\u0700\\u0000\\u0000\\u3013\\u0003X\\u0000?\\u1100\\u1473\\u0001\\u0a0a\\u7e06\\u02f5\\u0400\\u6f1e\\u0115\\u0a00\\u7e06\\u02f6\\u0400\\u6f1d\\u0115\\u0a00\\u7e06\\u02f7\\u0400\\u0f1f\\u156f\\u0001\\u060a\\uf87e\\u0002\\u1f04\\u6f0e\\u0115\\u0a00\\u7e06\\u02f9\\u0400\\u0c1f\\u156f\\u0001\\u060a\\ufa7e\\u0002\\u1a04\\u156f\\u0001\\u060a\\u8f80\\u0000\\u2a04\\u02f6\\ued28\\u0000\\u730a\\u0116\\u0a00\\u947d\\u0000\\u0204\\uca73\\u0000\\u7d0a\\u0095\\u0400\\u2802\\u00ed\\u0a00\\u1773\\u0001\\u7d0a\\u0096\\u0400\\u2802'\\u0a00\\u7302\\u0118\\u0a00\\ub128\\u0001\\u2a06\\u021e\\u987b\\u0000\\u2a04\\u0222\\u7d03\\u0098\\u0400\\u1e2a\\u7b02\\u0096\\u0400\\u5a2a\\u7b02\\u0094\\u0400\\u196f\\u0001\\u730a\\u011a\\u0a00\\u1b28\\u0001\\u2a0a\\u281a\\u0010\\u2b00\\u1e2a\\u7b02\\u0099\\u0400\\u222a\\u0302\\u997d\\u0000\\u2a04\\u021e\\u9a7b\\u0000\\u2a04\\u0222\\u7d03\\u009a\\u0400*\\u3013\\u00022\\u0000@\\u1100\\u7b02\\u0095\\u0400\\u1128\\u0000\\u0a2b\\u0206\\u947b\\u0000\\u6f04\\u0119\\u0a00\\u1228\\u0000\\u7e2b\\u0097\\u0400\\u1328\\u0000\\u282b\\u0014\\u2b00\\u1b6f\\u0001\\u2a0a\\u0372\\u0b2d\\u6a72\\u0016\\u7370\\u0120\\u0a00\\u027a\\u6f03\\u0c80\\u0600\\u2803\\u01b6\\u0600*\\u3003\\u0003E\\u0000\\u0000\\u0000\\u2d03\\u7210\\u1678\\u7000\\uae72\\u0016\\u7370\\u0121\\u0a00\\u047a\\u0b2d\\u6a72\\u0016\\u7370\\u0120\\u0a00\\u727a\\u16b8\\u7000\\u0403\\ua56f\\u0000\\u6f0a\\u00d5\\u0a00\\u1528\\u0000\\u022b\\u947b\\u0000\\u0304\\u6f04\\u0122\\u0a00*\\u0000\\u3013\\u0003\\u0014\\u0000A\\u1100\\u7b02\\u0094\\u0400\\u1203\\u6f00\\u0123\\u0a00\\u022d\\u2a14\\u2a06\\u024a\\u2803\\u01b7\\u0600\\u2d75\\u0000\\ua51b-\\u1b00*\\u3013\\u0005.\\u0000B\\u1100\\u0502\\ub728\\u0001\\u0a06\\u2d06\\u7217\\u16f0\\u7000\\u8d17\\u0004\\u0100\\u070b\\u0516\\u07a2\\u5c73\\f\\u7a06\\u0302\\u0604\\u040e\\uba28\\u0001\\u2a06\\u025a\\ub028\\u0001\\u0e06\\u0304\\u0504\\ufffd\\u0001\\u6f06\\u0124\\u0a00*\\u0000\\u3013\\u0004,\\u0000B\\u1100\\u0402\\ub728\\u0001\\u0a06\\u2d06\\u7217\\u16f0\\u7000\\u8d17\\u0004\\u0100\\u070b\\u0416\\u07a2\\u5673\\f\\u7a06\\u0302\\u0506\\ubc28\\u0001\\u2a06\\u3013\\u0002\\u001c\\u0000C\\u1100\\u0405\\ufffd\\u0001\\u0a06\\u0306\\ueb6f\\u0001\\u0206\\ub028\\u0001\\u0606\\u246f\\u0001\\u2a0a\\u3013\\u0004+\\u0000B\\u1100\\u0302\\ub728\\u0001\\u0a06\\u2d06\\u7217\\u16f0\\u7000\\u8d17\\u0004\\u0100\\u070b\\u0316\\u07a2\\u5c73\\f\\u7a06\\u0602\\u2804\\u01be\\u0600*\\u3013\\u0003%\\u0000C\\u1100\\u0304\\ufffd\\u0001\\u0a06\\u2806\\u0b21\\u0600\\u2028\\u000b\\u6f06\\u01ec\\u0600\\u2802\\u01b0\\u0600\\u6f06\\u0124\\u0a00\\u0a2a\\u2a02\\u023a\\u947b\\u0000\\u0304\\u256f\\u0001\\u260a*\\u301b\\u0005\\u00cf\\u0000D\\u1100\\u2d03\\u720b\\u171e\\u7000\\u2073\\u0001\\u7a0a\\u2802\\u01c7\\u0600\\u2802\\u01c9\\u0600\\u060a\\u266f\\u0001\\u0d0a\\u8b38\\u0000\\u1200\\u2803\\u0127\\u0a00\\u030b\\u4672\\u0017\\u1770\\u048d\\u0000\\u1301\\u1104\\u1604\\ua207\\u0411\\ua36f\\u0001\\u0706\\u6f03\\u0194\\u0600\\u7203\\u1768\\u7000\\u8d17\\u0004\\u0100\\u0513\\u0511\\u0716\\u11a2\\u6f05\\u01a3\\u0600\\u46de\\u080c\\u9e72\\u0017\\u1770\\u048d\\u0000\\u1301\\u1106\\u1606\\ua207\\u0611\\ubb28\\u0000\\u0806\\u3f28\\u0004\\u2c06\\ufe02\\u031a\\ud072\\u0017\\u1870\\u048d\\u0000\\u1301\\u1107\\u1607\\ua207\\u0711\\u0817\\u11a2\\u6f07\\u01a5\\u0600\\u00de\\u0312\\u2828\\u0001\\u3a0a\\uff69\\uffff\\u0ede\\u0312\\u16fe[\\u1b00\\u036f\\u0000\\ufffd*\\u1c01\\u0000\\u0000I\\u6c23\\u4600\\u0006\\u0100\\u0002\\\"\\uc09e\\u0e00\\u0000\\u0000\\u301b\\u0005\\u00cf\\u0000D\\u1100\\u2d03\\u720b\\u171e\\u7000\\u2073\\u0001\\u7a0a\\u2802\\u01c7\\u0600\\u2802\\u01c9\\u0600\\u060a\\u266f\\u0001\\u0d0a\\u8b38\\u0000\\u1200\\u2803\\u0127\\u0a00\\u030b\\u0c72\\u0018\\u1770\\u048d\\u0000\\u1301\\u1104\\u1604\\ua207\\u0411\\ua36f\\u0001\\u0706\\u6f03\\u0195\\u0600\\u7203\\u1832\\u7000\\u8d17\\u0004\\u0100\\u0513\\u0511\\u0716\\u11a2\\u6f05\\u01a3\\u0600\\u46de\\u080c\\u6c72\\u0018\\u1770\\u048d\\u0000\\u1301\\u1106\\u1606\\ua207\\u0611\\ubb28\\u0000\\u0806\\u3f28\\u0004\\u2c06\\ufe02\\u031a\\ua272\\u0018\\u1870\\u048d\\u0000\\u1301\\u1107\\u1607\\ua207\\u0711\\u0817\\u11a2\\u6f07\\u01a5\\u0600\\u00de\\u0312\\u2828\\u0001\\u3a0a\\uff69\\uffff\\u0ede\\u0312\\u16fe[\\u1b00\\u036f\\u0000\\ufffd*\\u1c01\\u0000\\u0000I\\u6c23\\u4600\\u0006\\u0100\\u0002\\\"\\uc09e\\u0e00\\u0000\\u0000\\u301b\\u0002r\\u0000E\\u1100\\ue272\\u0018\\u2870\\u009e\\u0600\\u1602\\uca28\\u0001\\u0a06\\u6f06\\u0129\\u0a00\\u2b0d\\u1233\\u2803\\u012a\\u0a00\\u720b\\u1924\\u7000\\u2807\\u0016\\u2b00\\u6f07\\u0520\\u0600\\u18de\\u080c\\u3c72\\u0019\\u2870\\u00b6\\u0600\\u2808\\u043e\\u0600\\u022c\\u1afe\\u00de\\u0312\\u2b28\\u0001\\u2d0a\\ufffd\\u120e\\ufe03\\u5d16\\u0000\\u6f1b\\u0003\\u0a00\\u72dc\\u196e\\u7000\\u9e28\\u0000\\u2a06\\u0000\\u1c01\\u0000\\u0000.\\u3608\\u1800\\u0006\\u0100\\u0002\\u0019\\u5940\\u0e00\\u0000\\u0000\\u301b\\u0002\\u00ba\\u0000F\\u1100\\u8f28\\u0000\\u2d06\\u2a01\\ube72\\u0019\\u2870\\u009e\\u0600\\ufe72\\u0019\\u2870\\u009e\\u0600\\u7b02\\u0094\\u0400\\u196f\\u0001\\u280a\\u0014\\u2b00\\u060a\\u2c6f\\u0001\\u130a\\u2b04\\u1213\\u2804\\u012d\\u0a00\\u720b\\u1a10\\u7000\\u2807\\u0017\\u2b00\\u0412\\u2e28\\u0001\\u2d0a\\ufffd\\u120e\\ufe04\\u5e16\\u0000\\u6f1b\\u0003\\u0a00\\u72dc\\u1a18\\u7000\\u9e28\\u0000\\u0206\\ub028\\u0001\\u2806\\u0018\\u2b00\\u080c\\u2f6f\\u0001\\u130a\\u2b05\\u1213\\u2805\\u0130\\u0a00\\u720d\\u1a10\\u7000\\u2809\\u0019\\u2b00\\u0512\\u3128\\u0001\\u2d0a\\ufffd\\u120e\\ufe05\\u5f16\\u0000\\u6f1b\\u0003\\u0a00\\u72dc\\u1a26\\u7000\\u9e28\\u0000\\u2a06\\u0000\\u1c01\\u0000\\u00025\\u5520\\u0e00\\u0000\\u0000\\u0002\\u0081\\ua120\\u0e00\\u0000\\u0000\\u0222\\u6f03\\u0c8b\\u0600*\\u0000\\u301b\\u0004\\u00b6\\u0000G\\u1100\\u7472\\u001a\\u2870\\u0095\\u0600\\u3273\\u0001\\u0a0a\\u2802\\u01b0\\u0600\\u1828\\u0000\\u0b2b\\u6f07\\u012f\\u0a00\\u0513\\u522b\\u0512\\u3028\\u0001\\u0c0a\\u6f08\\u01e0\\u0600\\u1428\\u0000\\u0d2b\\u6f09\\u012c\\u0a00\\u0613\\u1b2b\\u0612\\u2d28\\u0001\\u130a\\u0604\\u0411\\u336f\\u0001\\u2d0a\\u0608\\u0411\\u346f\\u0001\\u120a\\u2806\\u012e\\u0a00\\ufffd\\u0ede\\u0612\\u16fe^\\u1b00\\u036f\\u0000\\ufffd\\u0512\\u3128\\u0001\\u2d0a\\ufffd\\u120e\\ufe05\\u5f16\\u0000\\u6f1b\\u0003\\u0a00\\u06dc\\u7e03\\u009b\\u0400\\u112d\\ufe14\\ucc06\\u0001\\u7306\\u0135\\u0a00\\u9b80\\u0000\\u7e04\\u009b\\u0400\\u1a28\\u0000\\u2a2b\\u0000\\u1c01\\u0000\\u0002B\\u6a28\\u0e00\\u0000\\u0000\\u0002$\\u835f\\u0e00\\u0000\\u0000\\u301b\\u0002\\u00e8\\u0000H\\u1100\\uca73\\u0000\\u0a0a\\u2802\\u01b0\\u0600\\u1828\\u0000\\u0b2b\\u6f07\\u012f\\u0a00\\u0613\\u0f2b\\u0612\\u3028\\u0001\\u0c0a\\u0806\\ucb6f\\u0000\\u120a\\u2806\\u0131\\u0a00\\ue82d\\u0ede\\u0612\\u16fe_\\u1b00\\u036f\\u0000\\ufffd\\u7b02\\u0094\\u0400\\u196f\\u0001\\u280a\\u0014\\u2b00\\u090d\\u2c6f\\u0001\\u130a\\u2b07\\u1211\\u2807\\u012d\\u0a00\\u0413\\u1106\\u6f04\\u00cb\\u0a00\\u0712\\u2e28\\u0001\\u2d0a\\ufffd\\u120e\\ufe07\\u5e16\\u0000\\u6f1b\\u0003\\u0a00\\u02dc\\u6f06\\u0136\\u0a00\\u1b28\\u0000\\u7d2b\\u0095\\u0400\\ua472\\u001a\\u0270\\u957b\\u0000\\u6f04\\u0137\\u0a00\\u1c28\\u0000\\u022b\\u957b\\u0000\\u6f04\\u0138\\u0a00\\u0813\\u102b\\u0812\\u3928\\u0001\\u130a\\u1105\\u2805\\u05ae\\u0600\\u0812\\u3a28\\u0001\\u2d0a\\ufffd\\u120e\\ufe08\\u6116\\u0000\\u6f1b\\u0003\\u0a00\\u2adc\\u2801\\u0000\\u0002\\u001a\\u361c\\u0e00\\u0000\\u0000\\u0002]\\u7b1e\\u0e00\\u0000\\u0000\\u0002\\u00bc\\ufffd\\u0000\\u0000\\u301b\\u0002s\\u0000E\\u1100\\u2802\\u01c6\\u0600\\u1702\\uca28\\u0001\\u0a06\\u6f06\\u0129\\u0a00\\u2b0d\\u1242\\u2803\\u012a\\u0a00\\u720b\\u1ae0\\u7000\\u2807\\u0016\\u2b00\\u0207\\u1f6f\\u0005\\ufffd\\u0c26\\u2808\\u043e\\u0600\\u022c\\u1afe\\u3728\\u000b\\u2c06\\u7212\\u1b02\\u7000\\u2807`\\u0a00\\u7308\\u0c58\\u0600\\ufffd\\u1200\\u2803\\u012b\\u0a00\\ub52d\\u0ede\\u0312\\u16fe]\\u1b00\\u036f\\u0000\\ufffd*\\u1c01\\u0000\\u0000*\\u3309\\u2600\\u0006\\u0100\\u0002\\u0015\\u644f\\u0e00\\u0000\\u0000\\u021e\\uc728\\u0001\\u2a06\\u0246\\u957b\\u0000\\u2804\\u001d\\u2b00\\u1e28\\u0000\\u2a2b\\u0000\\u3013\\u0001\\u001d\\u0000I\\u1100\\u7b02\\u0095\\u0400\\u1f28\\u0000\\u0a2b\\u2c03\\u0607\\u2028\\u0000\\u0a2b\\u2806!\\u2b00*\\u0000\\u301b\\u0003>\\u0000J\\u1100\\u6f03\\u013c\\u0a00\\u2b0b\\u0720\\u3d6f\\u0001\\u0a0a\\u2802\\u01ad\\u0600\\u0012\\u3e28\\u0001\\u120a\\u2800\\u013f\\u0a00\\u406f\\u0001\\u070a\\u2a6f\\u0000\\u2d0a\\ufffd\\u070a\\u062c\\u6f07\\u0003\\u0a00\\u2adc\\u0000\\u1001\\u0000\\u0002\\u0007\\u332c\\u0a00\\u0000\\u0000\\u732e\\u01d0\\u0600\\u9780\\u0000\\u2a04\\u034a\\u806f\\f\\u0406\\u806f\\f\\u2806\\u0142\\u0a00\\u5a2a\\u6f03\\u0c80\\u0600\\u022d\\u2a16\\u6f03\\u0c80\\u0600\\u686f\\u0000\\u2a0a\\u021e\\u2728\\u0000\\u2a0a\\u0256\\u4328\\u0001\\u020a\\u2803\\u01d3\\u0600\\u0402\\ud528\\u0001\\u2a06\\u021e\\u9c7b\\u0000\\u2a04\\u0222\\u7d03\\u009c\\u0400\\u1e2a\\u7b02\\u009d\\u0400\\u222a\\u0302\\u9d7d\\u0000\\u2a04\\u023a\\u4328\\u0001\\u020a\\u2803\\u01d9\\u0600\\u562a\\u2802\\u0143\\u0a00\\u0302\\ufffd\\u0206\\u2804\\u01db\\u0600\\u1e2a\\u7b02\\u009e\\u0400\\u222a\\u0302\\u9e7d\\u0000\\u2a04\\u021e\\u9f7b\\u0000\\u2a04\\u0222\\u7d03\\u009f\\u0400\\ufe2a\\u2802\\u0b20\\u0600\\u226f\\u000b\\u1706\\u8d58\\u00cc\\u0100\\ua07d\\u0000\\u0204\\u2728\\u0000\\u020a\\u4473\\u0001\\u280a\\u01e5\\u0600\\u7302\\u0118\\u0a00\\ue328\\u0001\\u0206\\u3273\\u0001\\u280a\\u01e1\\u0600\\u8e2a\\u2802\\u01dc\\u0600\\u0302\\ue928\\u0001\\u0206\\ue028\\u0001\\u0e06\\u6f04\\u0145\\u0a00\\u0402\\u2805\\u01ec\\u0600\\u9a2a\\u2802\\u01dc\\u0600\\u0302\\ue928\\u0001\\u0206\\ue028\\u0001\\u0506\\u456f\\u0001\\u020a\\u2804\\u0b20\\u0600\\uec28\\u0001\\u2a06\\u026a\\ufffd\\u0001\\u0206\\u2803\\u01e9\\u0600\\u2802\\u01e0\\u0600\\u6f04\\u0145\\u0a00\\u1e2a\\u7b02\\u00a4\\u0400\\u222a\\u0302\\ua47d\\u0000\\u2a04\\u021e\\ua57b\\u0000\\u2a04\\u0222\\u7d03\\u00a5\\u0400\\u1e2a\\u7b02\\u00a6\\u0400\\u222a\\u0302\\ua67d\\u0000\\u2a04\\u021e\\ua77b\\u0000\\u2a04\\u0222\\u7d03\\u00a7\\u0400\\u1e2a\\u7b02\\u00a1\\u0400*\\u3013\\u0004\\u00d8\\u0000K\\u1100\\u0302\\ua17d\\u0000\\u0204\\ua17b\\u0000\\u1f04\\u6f2a\\u009e\\u0a00\\u020a\\ua17b\\u0000\\u1f04\\u6f2a\\u0146\\u0a00\\u060b\\u2f16\\u020f\\u7d18\\u00a2\\u0400\\u0302\\ua37d\\u0000\\u2a04\\u0706\\u4d33\\u2802\\u01e8\\u0600\\u0616\\ub66f\\u0000\\u0c0a\\u2802\\u01e8\\u0600\\u1706\\u6f58\\u00e9\\u0a00\\u080d\\u6d6f\\u0000\\u160a\\u0f31\\u1902\\ua27d\\u0000\\u0204\\u7d08\\u00a3\\u0400\\u092a\\u6d6f\\u0000\\u160a\\u0e31\\u1a02\\ua27d\\u0000\\u0204\\u7d09\\u00a3\\u0400\\u062a\\u3b2d\\u0207\\ue828\\u0001\\u6f06m\\u0a00\\u5917\\u2b33\\u2802\\u01e8\\u0600\\u0217\\ue828\\u0001\\u6f06m\\u0a00\\u5918\\ub66f\\u0000\\u130a\\u0204\\u7d1b\\u00a2\\u0400\\u1102\\u7d04\\u00a3\\u0400\\u022a\\u7d17\\u00a2\\u0400\\u7e02[\\u0a00\\ua37d\\u0000\\u2a04\\u3013\\u0002A\\u0000L\\u1100\\u4773\\u0001\\u0a0a\\u2128\\u000b\\u6f06\\u0b22\\u0600\\u2b0b\\u021a\\ua07b\\u0000\\u0704\\u2c90\\u060c\\u2807\\u0b29\\u0600\\u486f\\u0001\\u070a\\u5817\\u070b\\u2028\\u000b\\u6f06\\u0b22\\u0600\\ufffd\\u0149\\u0a00\\u762a\\u7e03\\u02fb\\u0400\\u2328\\u000b\\u2c06\\u2a01\\u7b02\\u00a0\\u0400\\u6f03\\u0b22\\u0600\\u9c17*\\u3013\\u0002#\\u0000\\u0002\\u1100\\u6f03\\u0b22\\u0600\\u2b0a\\u0210\\u2806\\u0b29\\u0600\\ueb28\\u0001\\u0606\\u5817\\u060a\\u6f04\\u0b22\\u0600\\ue731\\u762a\\u7e03\\u02fb\\u0400\\u2328\\u000b\\u2c06\\u2a01\\u7b02\\u00a0\\u0400\\u6f03\\u0b22\\u0600\\u9c16*\\u0000\\u301b\\u0006\\u00fb\\u0000M\\u1100\\u5a73\\u0000\\u0a0a\\u2806k\\u0a00\\u4272\\u001b\\u1870\\u048d\\u0000\\u0d01\\u1609\\u7b02\\u00a3\\u0400\\u09a2\\u0217\\ua27b\\u0000\\u8c04T\\u0200\\u09a2\\u4a6f\\u0001\\u260a\\u7206\\u1b76\\u7000\\u5e6f\\u0000\\u260a\\u0b16\\u382b\\u7b02\\u00a0\\u0400\\u9007\\u2a2c\\u2806k\\u0a00\\u8e72\\u001b\\u1770\\u048d\\u0000\\u1301\\u1104\\u1604\\u2807\\u0b29\\u0600\\u5f6f\\u0000\\ua20a\\u0411\\u4a6f\\u0001\\u260a\\u1707\\u0b58\\u0207\\ua07b\\u0000\\u8e04\\u3269\\u06bd\\u9872\\u001b\\u6f70^\\u0a00\\u0226\\ue028\\u0001\\u6f06\\u014b\\u0a00\\u0513\\u2d2b\\u0511\\u4c6f\\u0001\\u0c0a\\u2806k\\u0a00\\u8e72\\u001b\\u1770\\u048d\\u0000\\u1301\\u1106\\u1606\\u6f08\\u0c80\\u0600\\u11a2\\u6f06\\u014a\\u0a00\\u1126\\u6f05*\\u0a00\\uca2d\\u0cde\\u0511\\u072c\\u0511\\u036f\\u0000\\ufffd\\u7206\\u1bb6\\u7000\\u5e6f\\u0000\\u260a\\u6f06_\\u0a00*\\u1001\\u0000\\u0002\\u00a2\\ufffd\\u0c00\\u0000\\u0000\\u0376\\ufb7e\\u0002\\u2804\\u0b23\\u0600\\u022c\\u2a16\\u7b02\\u00a0\\u0400\\u6f03\\u0b22\\u0600\\u2a90\\u0000\\u3013\\u0003i\\u0000N\\u1100\\u7b02\\u00a2\\u0400\\u060a\\u0645\\u0000\\u0200\\u0000\\u0400\\u0000\\u0600\\u0000\\u1400\\u0000\\u2200\\u0000\\u3000\\u0000\\u2b00\\u1702\\u162a\\u032a\\u7b02\\u00a3\\u0400\\u6f1a\\u0094\\u0a00\\u032a\\u7b02\\u00a3\\u0400\\u6f1a\\u0096\\u0a00\\u032a\\u7b02\\u00a3\\u0400\\u6f1a\\u0097\\u0a00\\u032a\\u7b02\\u00a3\\u0400\\u6f1a\\u0095\\u0a00\\ufe16\\u1604\\u01fe\\u1e2a\\u7b02\\u014d\\u0a00*\\u0000\\u301b\\u0005K\\u00005\\u1100\\u0c03\\u0d16\\u3e2b\\u0908\\u0a9a\\u0602\\u2804\\u014e\\u0a00\\u2cde\\u070b\\uc072\\u0015\\u1770\\u048d\\u0000\\u1301\\u1104\\u1604\\u6f06\\u00d5\\u0a00\\u11a2\\u2804\\u00bb\\u0600\\u2807\\u043e\\u0600\\u022c\\u1afe\\u00de\\u1709\\u0d58\\u0809\\u698e\\ubc32*\\u1001\\u0000\\u0000\\n\\u140a\\u2c00\\u0006\\u0100\\u3013\\u0003\\u0083\\u0000O\\u1100\\ud003L\\u1b00\\u7e28\\u0000\\u160a\\u4f6f\\u0001\\u2c0a\\u036f\\u506f\\u0001\\u0d0a\\u1316\\u2b04\\u095c\\u0411\\u0a9a\\ud006G\\u1b00\\u7e28\\u0000\\u160a\\uf26f\\u0000\\u740aH\\u1b00\\u070b\\u0513\\u1316\\u2b06\\u112a\\u1105\\ua306G\\u1b00\\u020c\\u1204\\ufe02\\u4716\\u0000\\u6f1b\\u00f3\\u0600\\u9928\\u0000\\u060a\\u5128\\u0001\\u110a\\u1706\\u1358\\u1106\\u1106\\u8e05\\u3269\\u11ce\\u1704\\u1358\\u1104\\u0904\\u698e\\u9d32\\u322a\\u7b02\\u014d\\u0a00\\u526f\\u0001\\u2a0a\\u023a\\u4d7b\\u0001\\u030a\\u6f04\\u0153\\u0a00\\u3a2a\\u7b02\\u014d\\u0a00\\u0403\\u546f\\u0001\\u2a0a\\u0000\\u3013\\u0003#\\u0000P\\u1100\\u0302\\u0012\\u5528\\u0001\\u2c0a\\u0602\\u722a\\u1bba\\u7000\\u7203\\u084c\\u7000\\u9d28\\u0000\\u730a\\u0c55\\u0600\\u3a7a\\u7b02\\u014d\\u0a00\\u0403\\u546f\\u0001\\u2a0a\\u024a\\u5673\\u0001\\u7d0a\\u014d\\u0a00\\u2802'\\u0a00\\u1e2a\\u2802$\\u0a00\\u1e2a\\u2802$\\u0a00*\\u0000\\u301b\\u0002(\\u0000Q\\u1100\\u2802\\u01fe\\u0600\\u2803\\u0157\\u0a00\\u060a\\u586f\\u0001\\u260a\\u0602\\u0e28\\u0002\\ufffd\\u060a\\u062c\\u6f06\\u0003\\u0a00\\u2adc\\u1001\\u0000\\u0002\\r\\u1d10\\u0a00\\u0000\\u0000\\u023a\\ufe28\\u0001\\u0206\\u2803\\u020e\\u0600\\ub62a\\u2802'\\u0a00\\u2802\\u00ed\\u0a00\\u5973\\u0001\\u280a\\u0202\\u0600\\u7302\\u015a\\u0a00\\u0428\\u0002\\u0206\\u5b73\\u0001\\u7d0a\\u00b0\\u0400\\u1e2a\\u7b02\\u00b1\\u0400\\u222a\\u0302\\ub17d\\u0000\\u2a04\\u021e\\ub27b\\u0000\\u2a04\\u0222\\u7d03\\u00b2\\u0400\\u1e2a\\u7b02\\u00b3\\u0400\\u222a\\u0302\\ub37d\\u0000\\u2a04\\u021e\\ub47b\\u0000\\u2a04\\u0222\\u7d03\\u00b4\\u0400*\\u0000\\u301b\\u0003G\\u0000R\\u1100\\u5a73\\u0001\\u0a0a\\u2802\\u0203\\u0600\\u5c6f\\u0001\\u0c0a\\u1d2b\\u6f08\\u015d\\u0a00\\u070b\\uff6f\\u0001\\u0306\\u6f1b\\u0094\\u0a00\\u072c\\u0706\\u5e6f\\u0001\\u080a\\u2a6f\\u0000\\u2d0a\\ufffd\\u080a\\u062c\\u6f08\\u0003\\u0a00\\u06dc*\\u1001\\u0000\\u0002\\u0012\\u3b29\\u0a00\\u0000\\u0000\\u3013\\u0003F\\u0000S\\u1100\\u0302\\u2814\\u020b\\u0600\\u060a\\u382d\\u8d1b\\u00bf\\u0100\\u070b\\u7216\\u1be2\\u7000\\u07a2\\u0317\\u07a2\\u7218\\u1bf6\\u7000\\u07a2\\u0219\\uff28\\u0001\\ua206\\u1a07\\u0272\\u001c\\ua270\\u2807\\u00a7\\u0a00\\u5573\\f\\u7a06\\u2a06\\u0000\\u3013\\u0003\\u001e\\u0000&\\u1100\\u2802\\u0201\\u0600\\u1203\\u6f00\\u015f\\u0a00\\u022d\\u2a04\\u2806k\\u0a00\\u6028\\u0001\\u2a0a\\u0000\\u3013\\u00035\\u0000T\\u1100\\u2802\\u0201\\u0600\\u1203\\u6f00\\u015f\\u0a00\\u022d\\u2a04\\u2806\\u0604\\u0600\\u0a2c\\u0112\\u15feq\\u1b00\\u2a07\\u2806k\\u0a00\\u6028\\u0001\\u730a\\u0161\\u0a00*\\u0000\\u3013\\u0003\\u0014\\u0000&\\u1100\\u2802\\u0201\\u0600\\u1203\\u6f00\\u015f\\u0a00\\u022d\\u0a04\\u2a06\\u3013\\u0004h\\u0000U\\u1100\\u0b03\\u0c16\\u192b\\u0807\\u0a9a\\u2802\\u01ff\\u0600\\u1b06\\u946f\\u0000\\u2c0a\\ufffd\\u084c\\u5817\\u080c\\u8e07\\u3269\\u1be1\\ubf8d\\u0000\\u0d01\\u1609\\u0a72\\u001c\\ua270\\u1709\\u5e72\\u001c\\u0370\\u6228\\u0001\\ua20a\\u1809\\u6272\\u001c\\ua270\\u1909\\u2802\\u01ff\\u0600\\u09a2\\u721a\\u0956\\u7000\\u09a2\\ua728\\u0000\\u730a\\u0163\\u0a00\\u2a7a\\u3013\\u00027\\u0000V\\u1100\\u6628\\u0001\\u020a\\uee7b\\u0004\\u3304\\u0215\\ued7b\\u0004\\u1f04\\u33fe\\u020b\\u7d16\\u04ed\\u0400\\u0a02\\u132b\\u7316\\u1066\\u0600\\u060a\\u7b02\\u04ef\\u0400\\uef7d\\u0004\\u0604\\u1e2a\\u2802\\u105f\\u0600*\\u301b\\u0002\\u0141\\u0000W\\u1100\\u7b02\\u04ed\\u0400\\u070b\\u0345\\u0000\\u0c00\\u0000\\u1b00\\u0001\\u5d00\\u0000\\u0700\\u3b1b\\u00e7\\u0000\\u0f38\\u0001\\u0200\\u7d15\\u04ed\\u0400\\u0202\\uef7b\\u0004\\u7b04\\u00b0\\u0400\\u676f\\u0001\\u7d0a\\u04f3\\u0400\\u1702\\ued7d\\u0004\\u2b04\\u0232\\u7c02\\u04f3\\u0400\\u6828\\u0001\\u7d0a\\u04f0\\u0400\\u0202\\uf07b\\u0004\\u7d04\\u04ec\\u0400\\u1802\\ued7d\\u0004\\u1704\\ufffd\\u00c9\\u0000\\u1702\\ued7d\\u0004\\u0204\\uf37c\\u0004\\u2804\\u0169\\u0a00\\uc12d\\u2802\\u1067\\u0600\\u0202\\uef7b\\u0004\\u6f04\\u0203\\u0600\\u5c6f\\u0001\\u7d0a\\u04f4\\u0400\\u1902\\ued7d\\u0004\\u2b04\\u0272\\u7b02\\u04f4\\u0400\\u5d6f\\u0001\\u7d0a\\u04f1\\u0400\\u0202\\uf17b\\u0004\\u6f04\\u020d\\u0600\\ue56f\\u0000\\u7d0a\\u04f5\\u0400\\u1a02\\ued7d\\u0004\\u2b04\\u022f\\u7b02\\u04f5\\u0400\\ue66f\\u0000\\u7d0a\\u04f2\\u0400\\u0202\\uf27b\\u0004\\u7d04\\u04ec\\u0400\\u1b02\\ued7d\\u0004\\u1704\\ufffd\\u0238\\u7d1a\\u04ed\\u0400\\u7b02\\u04f5\\u0400\\u2a6f\\u0000\\u2d0a\\u02c4\\u6928\\u0010\\u0206\\uf47b\\u0004\\u6f04*\\u0a00\\u812d\\u2802\\u1068\\u0600\\u0a16\\u07de\\u2802\\u1064\\u0600\\u06dc*\\u0000\\u1c41\\u0000\\u0004\\u0000\\u0000\\u0000\\u0138\\u0000\\u0138\\u0000\\u0007\\u0000\\u0000\\u0000\\u021e\\uec7b\\u0004\\u2a04\\u731a\\u016a\\u0a00z\\u301b\\u0002j\\u0000X\\u1100\\u7b02\\u04ed\\u0400\\u060a\\u5917\\u0245\\u0000\\u0200\\u0000\\u0200\\u0000\\u2b00\\ufffd\\u0207\\u6728\\u0010\\ufffd\\u7b02\\u04ed\\u0400\\u070b\\u5919\\u0345\\u0000\\u0100\\u0000\\u0100\\u0000\\u0100\\u0000\\u2a00\\u7b02\\u04ed\\u0400\\u080c\\u591a\\u0245\\u0000\\u0200\\u0000\\u0200\\u0000\\u2b00\\ufffd\\u0207\\u6928\\u0010\\ufffd\\u07de\\u2802\\u1068\\u0600\\u2adc\\u0000\\u2801\\u0000\\u0002\\u0019\\u1b02\\u0700\\u0000\\u0000\\u0002W\\u5902\\u0700\\u0000\\u0000\\u0002>\\u6224\\u0700\\u0000\\u0000\\u021e\\uec7b\\u0004\\u2a04\\u0266\\u2728\\u0000\\u020a\\u7d03\\u04ed\\u0400\\u2802\\u0166\\u0a00\\uee7d\\u0004\\u2a04\\u0266\\u7d15\\u04ed\\u0400\\u7c02\\u04f3\\u0400\\u16fer\\u1b00\\u036f\\u0000\\u2a0a\\u026e\\u7d15\\u04ed\\u0400\\u7b02\\u04f4\\u0400\\u0b2c\\u7b02\\u04f4\\u0400\\u036f\\u0000\\u2a0a\\u026e\\u7d19\\u04ed\\u0400\\u7b02\\u04f5\\u0400\\u0b2c\\u7b02\\u04f5\\u0400\\u036f\\u0000\\u2a0a\\u3013\\u0002\\u0011\\u0000V\\u1100\\ufe1f\\u6673\\u0010\\u0a06\\u0206\\uef7d\\u0004\\u0604*\\u0000\\u3013\\u0005\\u00e6\\u0000&\\u1100\\u6f03\\u016b\\u0a00\\u6f2c\\u2802\\u0201\\u0600\\u6f03\\u016c\\u0a00\\u6d6f\\u0001\\u2d0a\\u0219\\u0128\\u0002\\u0306\\u6c6f\\u0001\\u030a\\u6e6f\\u0001\\u6f0a\\u016f\\u0a00\\u342b\\u7c72\\u001c\\u0370\\u6c6f\\u0001\\u030a\\u6e6f\\u0001\\u020a\\u0128\\u0002\\u0306\\u6c6f\\u0001\\u6f0a\\u0170\\u0a00\\u7128\\u0001\\u0a0a\\u7b02\\u00b0\\u0400\\u6f06\\u0172\\u0a00\\u6f03\\u0173\\u0a00\\u982d\\u6f03\\u0174\\u0a00\\u0226\\u6f03\\u016c\\u0a00(\\u0002\\u0306\\u756f\\u0001\\u2d0a\\u2b5a\\u0350\\u766f\\u0001\\u1f0a\\u330f\\u2a01\\u6f03\\u0176\\u0a00\\u2e1a\\u0309\\u766f\\u0001\\u190a\\u1933\\u2502\\u0528\\u0002\\u0306\\u6e6f\\u0001\\u280a\\u0099\\u0a00\\u0628\\u0002\\u2b06\\u031a\\u766f\\u0001\\u170a\\u1133\\u2802\\u0203\\u0600\\u7303\\u01fd\\u0600\\u776f\\u0001\\u030a\\u786f\\u0001\\u2d0a\\u2aa8\\u021e\\u2428\\u0000\\u2a0a\\u7e2e\\u02f7\\u0400\\u1128\\u0002\\u2a06\\u0000\\u3013\\u0003,\\u0000Y\\u1100\\u2a73\\r\\u0a06\\uaa73\\u0001\\u0b06\\u3d72\\u001d\\u0270\\u7306\\u01de\\u0600\\u070c\\ub06f\\u0001\\u0806\\u246f\\u0001\\u070a\\u3e28\\u000b\\u2a06\\u0232\\uf77e\\u0002\\u2804\\u0213\\u0600*\\u0000\\u3013\\u0003&\\u0000Z\\u1100\\uaa73\\u0001\\u0a06\\u3d72\\u001d\\u0370\\u7302\\u01de\\u0600\\u060b\\ub06f\\u0001\\u0706\\u246f\\u0001\\u060a\\u3e28\\u000b\\u2a06\\u0232\\uf77e\\u0002\\u2804\\u0215\\u0600*\\u3013\\u0002\\u001a\\u0000[\\u1100\\ud373\\r\\u0a06\\u0206\\u4428\\b\\u6f06\\u0dd7\\u0600\\u0306\\u1328\\u0002\\u2a06\\u021e\\u2428\\u0000\\u2a0a\\u281a\\u0160\\u0600\\u362a\\u0302\\u3228\\u000b\\u2806\\u0219\\u0600\\u2a2a\\u0302\\u0416\\u1b28\\u0002\\u2a06\\u023a\\u0403\\u3228\\u000b\\u2806\\u021b\\u0600*\\u0000\\u301b\\u0004:\\u0000Q\\u1100\\u2802\\u00ed\\u0a00\\u7973\\u0001\\u7d0a\\u00ba\\u0400\\u2802\\u01aa\\u0600\\u0502\\ubc7d\\u0000\\u0304\\u1c28\\u0002\\u0a06\\u0602\\u0403\\u3228\\u0002\\ufffd\\u060a\\u062c\\u6f06\\u0003\\u0a00\\u2adc\\u0000\\u1001\\u0000\\u0002$\\u2f0b\\u0a00\\u0000\\u0000\\u0266\\u6928\\u0000\\u2d0a\\u020f\\u7a6f\\u0001\\u100a\\u0200\\u5728\\u0001\\u2a0a\\u2a14\\u023a\\u0403\\u3228\\u000b\\u2806\\u021e\\u0600\\u2e2a\\u0302\\u1604\\u2805\\u0220\\u0600\\u3e2a\\u0302\\u0504\\u3228\\u000b\\u2806\\u0220\\u0600\\ua22a\\u2802\\u00ed\\u0a00\\u7973\\u0001\\u7d0a\\u00ba\\u0400\\u2802\\u01aa\\u0600\\u0e02\\u7d04\\u00bc\\u0400\\u0302\\u0504\\u3228\\u0002\\u2a06\\u0000\\u301b\\u0004J\\u0000\\\\\\u1100\\u2802\\u00ed\\u0a00\\u7973\\u0001\\u7d0a\\u00ba\\u0400\\u2802\\u01aa\\u0600\\u2802\\u0b32\\u0600\\ubc7d\\u0000\\u0304\\u7b6f\\u0001\\u730a\\u017c\\u0a00\\u060a\\u7d28\\u0001\\u0b0a\\u0702\\u1604\\u3228\\u0002\\ufffd\\u060a\\u062c\\u6f06\\u0003\\u0a00\\u2adc\\u0000\\u1001\\u0000\\u0002-\\u3f12\\u0a00\\u0000\\u0000\\u301b\\u0004J\\u0000\\\\\\u1100\\u2802\\u00ed\\u0a00\\u7973\\u0001\\u7d0a\\u00ba\\u0400\\u2802\\u01aa\\u0600\\u2802\\u0b32\\u0600\\ubc7d\\u0000\\u0304\\u7b6f\\u0001\\u730a\\u017c\\u0a00\\u060a\\u7d28\\u0001\\u0b0a\\u0702\\u0504\\u3228\\u0002\\ufffd\\u060a\\u062c\\u6f06\\u0003\\u0a00\\u2adc\\u0000\\u1001\\u0000\\u0002-\\u3f12\\u0a00\\u0000\\u0000\\u3013\\u0001\\u0012\\u0000]\\u1100\\u4172\\u001d\\u2870\\u017e\\u0a00\\u060a\\u4f75\\u0000\\u2a02\\u021e\\ubd7b\\u0000\\u2a04\\u0222\\u7d03\\u00bd\\u0400\\u0a2a\\u2a02\\u02ba\\uba7b\\u0000\\u6f04\\u017f\\u0a00\\ube7e\\u0000\\u2d04\\u1411\\u06fe\\u024d\\u0600\\u8073\\u0001\\u800a\\u00be\\u0400\\ube7e\\u0000\\u2804\\\"\\u2b00*\\u0000\\u301b\\u0003I\\u0000^\\u1100\\u7b02\\u00ba\\u0400\\u826f\\u0001\\u280a#\\u2b00\\u060a\\u676f\\u0001\\u0c0a\\u152b\\u0212\\u6828\\u0001\\u0b0a\\u7b02\\u00ba\\u0400\\u0307\\u836f\\u0001\\u120a\\u2802\\u0169\\u0a00\\ue22d\\u0ede\\u0212\\u16fer\\u1b00\\u036f\\u0000\\ufffd*\\u0000\\u1001\\u0000\\u0002\\u0018\\u3a22\\u0e00\\u0000\\u0000\\u0f22\\u2800\\u0184\\u0a00\\u222a\\u000f\\u8528\\u0001\\u2a0a\\u0000\\u3003\\u0003K\\u0000\\u0000\\u0000\\u7b02\\u00ba\\u0400\\ubf7e\\u0000\\u2d04\\u1411\\u06fe\\u024e\\u0600\\u8673\\u0001\\u800a\\u00bf\\u0400\\ubf7e\\u0000\\u2804$\\u2b00\\uc07e\\u0000\\u2d04\\u1411\\u06fe\\u024f\\u0600\\u8773\\u0001\\u800a\\u00c0\\u0400\\uc07e\\u0000\\u2804%\\u2b00\\u322a\\u7b02\\u00bb\\u0400\\u1873\\u0002\\u2a06\\u282e\\u0b32\\u0600\\u376f\\t\\u2a06\\u2832\\u0b32\\u0600\\u6f02\\u0938\\u0600\\u2e2a\\u3228\\u000b\\u6f06\\u0939\\u0600\\ue62a\\u7202\\u166a\\u7000\\u6f1b\\u0094\\u0a00\\u292d\\u7202\\u1d4b\\u7000\\u6f1b\\u0094\\u0a00\\u1b2d\\u7202\\u1d5b\\u7000\\u6f1b\\u0094\\u0a00\\u0d2d\\u7202\\u1d79\\u7000\\u6f1b\\u0094\\u0a00\\u172a\\uae2a\\u7202\\u1d99\\u7000\\u6f1b\\u0094\\u0a00\\u1b2d\\u7202\\u1daf\\u7000\\u6f1b\\u0094\\u0a00\\u0d2d\\u7202\\u1dd5\\u7000\\u6f1b\\u0094\\u0a00\\u172a\\u522a\\u7202\\u04af\\u7000\\u5b7e\\u0000\\u6f0a\\u00b7\\u0a00\\u0010\\u2a02\\u3013\\u0003\\u001e\\u0000\\u0002\\u1100\\u2d02\\u1402\\u022a\\u3a1f\\u9e6f\\u0000\\u0a0a\\u1606\\u022f\\u2a02\\u0602\\u5817\\ue96f\\u0000\\u2a0a\\u0000\\u3013\\u0003J\\u0000_\\u1100\\u8b73\\u000f\\u0a06\\u0206\\u866f\\u000f\\u0606\\u6f02\\u0c80\\u0600\\u816f\\f\\u0206\\u6f02\\u0c80\\u0600\\ufd72\\u001d\\u2870\\u0099\\u0a00\\u816f\\f\\u7206\\u1e0f\\u7000\\u6f06\\u0c80\\u0600\\u6f02\\u0c80\\u0600\\u1528\\u0000\\u062b\\u0010\\u2a02\\u0000\\u301b\\u0005\\u00bd\\u0000`\\u1100\\u1202\\ufe03\\u7115\\u0000\\u091b\\u2528\\u0002\\u0306\\u586f\\u0001\\u260a\\u7303\\u01fd\\u0600\\u040a\\u1d2c\\u0402\\ubb7d\\u0000\\u0204\\u0406\\u2816\\u0236\\u0600\\u9672\\u001e\\u0470\\u0a28\\u0000\\u2b2b\\u0209\\u1406\\u2816\\u0236\\u0600\\u1702\\u6173\\u0001\\u280a\\u0225\\u0600\\u0602\\u3328\\u0002\\u0206\\u3428\\u0002\\ufffd\\u0b5b\\u1602\\u6173\\u0001\\u280a\\u0225\\u0600\\u2807\\u043f\\u0600\\u022c\\u1afe\\u7207\\u1ee8\\u7000\\u8d17\\u0004\\u0100\\u0413\\u0411\\u0416\\u11a2\\u7304\\u0c57\\u0600\\u080c\\u2272\\u001f\\u1770\\u048d\\u0000\\u1301\\u1105\\u1605\\ua204\\u0511\\ubb28\\u0000\\u0506\\u0a2d\\u2808\\u043e\\u0600\\u022c\\u7a08\\u00de*\\u0000\\u1001\\u0000\\u0000\\u0000\\u6161\\u5b00\\u0006\\u0100\\u3013\\u0002n\\u0000a\\u1100\\u6f03\\u020d\\u0600\\u2628\\u0000\\u0a2b\\u2806'\\u2b00\\u592c\\u3928\\u000b\\u0d06\\u0312\\u8a28\\u0001\\u2d0a\\u2807\\u0b37\\u0600\\u072b\\u0312\\u8b28\\u0001\\u2c0a\\u2813\\u018c\\u0a00\\u2806\\u0162\\u0a00\\u070b\\u5573\\f\\u7a06\\u1306\\u1604\\u0513\\u172b\\u0411\\u0511\\u0c9a\\uf87e\\u0002\\u0804\\u8028\\u0000\\u1106\\u1705\\u1358\\u1105\\u1105\\u8e04\\u3269\\u2ae1\\u021e\\u2728\\u0000\\u2a0a\\u021e\\ue06f\\u0001\\u2a06\\u021e\\u806f\\f\\u2a06\\u02ca\\uf67b\\u0004\\u0304\\u806f\\f\\u6f06\\u018d\\u0a00\\u1e2d\\u7072\\u001f\\u0370\\u806f\\f\\u2806\\r\\u2b00\\u2502\\uf77b\\u0004\\u1704\\u7d58\\u04f7\\u0400*\\u0000\\u3013\\u0004\\u00f3\\u0000b\\u1100\\u6a73\\u0010\\u0b06\\u2802\\u0224\\u0600\\u120c\\u2802\\u018a\\u0a00\\u0b2d\\u2372 \\u2870\\u00b0\\u0600\\u022a\\u2428\\u0002\\u0d06\\u0312\\u8e28\\u0001\\u2d0a\\u720b\\u20a8\\u7000\\ub028\\u0000\\u2a06\\u2802\\u01ae\\u0600\\u720a\\u2128\\u7000\\u2802\\u01b0\\u0600\\u8f6f\\u0001\\u060a\\u906f\\u0001\\u280a(\\u2b00\\u0207\\ub028\\u0001\\u7e06\\u00c1\\u0400\\u112d\\ufe14\\u5006\\u0002\\u7306\\u0191\\u0a00\\uc180\\u0000\\u7e04\\u00c1\\u0400\\u2928\\u0000\\u7e2b\\u00c2\\u0400\\u112d\\ufe14\\u5106\\u0002\\u7306\\u0193\\u0a00\\uc280\\u0000\\u7e04\\u00c2\\u0400\\u2a28\\u0000\\u732b\\u0194\\u0a00\\uf67d\\u0004\\u0704\\u7d16\\u04f7\\u0400\\u2806\\u0014\\u2b00\\ufe07\\u6b06\\u0010\\u7306\\u0195\\u0a00\\u966f\\u0001\\u720a\\u21b9\\u7000\\u2802\\u01b0\\u0600\\u8f6f\\u0001\\u060a\\u906f\\u0001\\u070a\\uf77b\\u0004\\u2804+\\u2b00\\u8a2a\\u7b02\\u00ba\\u0400\\u2803\\u0243\\u0600\\u976f\\u0001\\u2d0a\\u020e\\u7303\\u01fc\\u0600\\u0403\\u3628\\u0002\\u2a06\\u0000\\u3013\\u0004a\\u0000c\\u1100\\u1803\\ubf8d\\u0000\\u0a01\\u1606\\u4172\\u001d\\ua270\\u1706\\u9672\\\"\\ua270\\u6f06\\u020c\\u0600\\u6f03\\u01ff\\u0600\\u6b28\\u0000\\u6f0a\\u0198\\u0a00\\u0b25\\u2e2c\\u7207\\u22b2\\u7000\\u9928\\u0001\\u2d0a\\u070e\\uce72\\\"\\u2870\\u0199\\u0a00\\u0b2d\\u022a\\u0403\\u2805\\u0237\\u0600\\u022a\\u0403\\u2805\\u0238\\u0600*\\u0000\\u301b\\u0004e\\u0000d\\u1100\\ufffd\\u2870\\u0095\\u0600\\u1703\\ubf8d\\u0000\\u0c01\\u1608\\u9672\\\"\\ua270\\u6f08\\u020c\\u0600\\u7203\\u1d41\\u7000\\u076f\\u0002\\u2806,\\u2b00\\u060a\\u9a6f\\u0001\\u0d0a\\u112b\\u0312\\u9b28\\u0001\\u0b0a\\u0702\\u0504\\u3828\\u0002\\u1206\\u2803\\u019c\\u0a00\\ue62d\\u0ede\\u0312\\u16fe~\\u1b00\\u036f\\u0000\\ufffd*\\u0000\\u1001\\u0000\\u00028\\u561e\\u0e00\\u0000\\u0000\\u024a\\uff6f\\u0001\\u7206\\u230c\\u7000\\u6f19\\u0094\\u0a00*\\u301b\\u0004\\u036d\\u0000e\\u1100\\u2272#\\u2870\\u0095\\u0600\\u1703\\ubf8d\\u0000\\u1301\\u1107\\u1607\\u4172\\u001d\\ua270\\u0711\\u0c6f\\u0002\\u0306\\u4472#\\u1670\\u096f\\u0002\\u2c06\\u020b\\u6b28\\u0000\\u280a\\u01b3\\u0600\\u7203\\u236c\\u7000\\u7128\\u0000\\u6f06\\u0b1f\\u0600\\u0b6f\\u0002\\u2806\\u0b2a\\u0600\\u7228\\u0000\\u0206\\u7203\\u238e\\u7000\\u6f16\\u0209\\u0600\\uac28\\u0001\\u0306\\uc072#\\u0570\\u096f\\u0002\\u0a06\\u2c04\\u0212\\uba7b\\u0000\\u0404\\u4328\\u0002\\u0606\\u836f\\u0001\\u020a\\ubc7b\\u0000\\u0304\\ud672#\\u0270\\ubc7b\\u0000\\u6f04\\u090f\\u0600\\u096f\\u0002\\u6f06\\u0910\\u0600\\u7b02\\u00bc\\u0400\\u7203\\u23f6\\u7000\\u7b02\\u00bc\\u0400\\u116f\\t\\u6f06\\u020a\\u0600\\u126f\\t\\u0206\\ubc7b\\u0000\\u0304\\u2272$\\u0270\\ubc7b\\u0000\\u6f04\\u0913\\u0600\\u096f\\u0002\\u6f06\\u0914\\u0600\\u7203\\u244e\\u7000\\u7328\\u0000\\u6f06\\u0209\\u0600\\u7428\\u0000\\u0306\\u7872$\\u2870u\\u0600\\u096f\\u0002\\u2806v\\u0600\\u7203\\u24ac\\u7000\\u7928\\u0000\\u6f06\\u020b\\u0600\\u7a28\\u0000\\u0306\\ucc72$\\u2870w\\u0600\\u096f\\u0002\\u2806x\\u0600\\u7203\\u24f2\\u7000\\u7d28\\u0000\\u6f06\\u0209\\u0600\\u7e28\\u0000\\u0206\\ubc7b\\u0000\\u0304\\u2a72%\\u0270\\ubc7b\\u0000\\u6f04\\u0917\\u0600\\u1f6f\\u000b\\u6f06\\u020b\\u0600\\u2a28\\u000b\\u6f06\\u0918\\u0600\\u6f03\\u0203\\u0600\\u2c28\\u0000\\u0b2b\\u7e07\\u00c3\\u0400\\u112d\\ufe14\\u5206\\u0002\\u7306\\u019d\\u0a00\\uc380\\u0000\\u7e04\\u00c3\\u0400\\u2d28\\u0000\\u282b,\\u2b00\\u080c\\u9a6f\\u0001\\u130a\\u2b08\\u1215\\u2808\\u019b\\u0a00\\u020d\\u0409\\u8028\\u0000\\u280a\\u023f\\u0600\\u0812\\u9c28\\u0001\\u2d0a\\ufffd\\u120e\\ufe08\\u7e16\\u0000\\u6f1b\\u0003\\u0a00\\u73dc\\u015a\\u0a00\\u0413\\u6f07\\u019a\\u0a00\\u0913\\u0e38\\u0001\\u1200\\u2809\\u019b\\u0a00\\u0513\\u0511\\uff6f\\u0001\\u2806k\\u0a00\\u986f\\u0001\\u250a\\u0a13\\ufffd\\ufe00\\u7e13\\u04f8\\u0400\\u612d\\u731d\\u019e\\u0a00\\u7225\\u230c\\u7000\\u2816\\u019f\\u0a00\\u7225\\u254a\\u7000\\u2817\\u019f\\u0a00\\u7225\\u255a\\u7000\\u2818\\u019f\\u0a00\\u7225\\u256e\\u7000\\u2819\\u019f\\u0a00\\u7225\\u257e\\u7000\\u281a\\u019f\\u0a00\\u7225\\u2590\\u7000\\u281b\\u019f\\u0a00\\u7225\\u259c\\u7000\\u281c\\u019f\\u0a00\\u13fe\\uf880\\u0004\\ufe04\\u7e13\\u04f8\\u0400\\u0a11\\u0b12\\ua028\\u0001\\u2c0a\\u115f\\u450b\\u0007\\u0000M\\u0000\\u0002\\u0000\\u0013\\u0000\\u0013\\u0000\\u001d\\u0000'\\u00002\\u0000\\u3a2b\\u1102\\u0405\\u8028\\u0000\\u060a\\u4028\\u0002\\u2b06\\u023a\\u0511\\u3d28\\u0002\\u2b06\\u0230\\u0511\\u3c28\\u0002\\u2b06\\u1126\\u1104\\u6f05\\u015e\\u0a00\\u1b2b\\u1102\\u2805\\u0242\\u0600\\u112b\\ua672%\\u1170\\u6f05\\u01ff\\u0600\\u0d28\\u0000\\u122b\\u2809\\u019c\\u0a00\\ue63a\\ufffd\\ufffd\\u120e\\ufe09\\u7e16\\u0000\\u6f1b\\u0003\\u0a00\\u11dc\\u6f04\\u019a\\u0a00\\u0c13\\u172b\\u0c12\\u9b28\\u0001\\u130a\\u0206\\u0611\\u2802\\u01b0\\u0600\\u3928\\u0002\\u1206\\u280c\\u019c\\u0a00\\ue02d\\u0ede\\u0c12\\u16fe~\\u1b00\\u036f\\u0000\\ufffd*\\u0000\\u4c41\\u0000\\u0002\\u0000\\u01c3\\u0000\\\"\\u0000\\u01e5\\u0000\\u000e\\u0000\\u0000\\u0000\\u0002\\u0000\\u0202\\u0000\\u0121\\u0000\\u0323\\u0000\\u000e\\u0000\\u0000\\u0000\\u0002\\u0000\\u033a\\u0000$\\u0000\\u035e\\u0000\\u000e\\u0000\\u0000\\u0000\\u301b\\u0004d\\u0000d\\u1100\\ufffd%\\u2870\\u0095\\u0600\\u1703\\ubf8d\\u0000\\u0c01\\u1608r&\\ua270\\u6f08\\u020c\\u0600\\u7203\\u065b\\u7000\\u076f\\u0002\\u2806,\\u2b00\\u060a\\u9a6f\\u0001\\u0d0a\\u102b\\u0312\\u9b28\\u0001\\u0b0a\\u0702\\u2804\\u023a\\u0600\\u0312\\u9c28\\u0001\\u2d0a\\ufffd\\u120e\\ufe03\\u7e16\\u0000\\u6f1b\\u0003\\u0a00\\u2adc\\u1001\\u0000\\u00028\\u551d\\u0e00\\u0000\\u0000\\u301b\\u0004\\u028e\\u0000f\\u1100\\u1703\\ubf8d\\u0000\\u1301\\u1113\\u1613\\u5b72\\u0006\\ua270\\u1311\\u0c6f\\u0002\\u0306\\uae72\\u0016\\u7270\\u1d3d\\u7000\\u0b6f\\u0002\\u0a06\\u7203\\u260c\\u7000\\u6f17\\u0209\\u0600\\u070b\\u0b2d\\u1c72&\\u2870\\u009e\\u0600\\u732a\\u01dc\\u0600\\u030c\\u6472&\\u1470\\u0b6f\\u0002\\u0d06\\u2d09\\u030d\\u7672&\\u1470\\u0b6f\\u0002\\u0d06\\u0608\\ue96f\\u0001\\u0906\\u6f2c\\u1709\\ufffd\\u1301\\u1114\\u1614\\u2c1f\\u119d\\u6f14\\u01a1\\u0a00\\u1513\\u1316\\u2b16\\u114a\\u1115\\u9a16\\u0413\\u0411\\u7a6f\\u0001\\u130a\\u0205\\u0511\\ub728\\u0001\\u1306\\u1106\\u2c06\\u080f\\ue06f\\u0001\\u1106\\u6f06\\u0145\\u0a00\\u172b\\u8672&\\u1170\\u7205\\u2696\\u7000\\u9d28\\u0000\\u730a\\u0c55\\u0600\\u117a\\u1716\\u1358\\u1116\\u1116\\u8e15\\u3269\\u08ae\\u7203\\u26ae\\u7000\\u6f16\\u0209\\u0600\\ue76f\\u0001\\u0306\\u016f\\u0002\\u7206\\u0645\\u7000\\u0712\\u5f6f\\u0001\\u2c0a\\u1116\\u2807\\u0b2a\\u0600\\u0813\\u1108\\u6f08\\u01eb\\u0600\\ue238\\u0000\\u0300\\u016f\\u0002\\u7206\\u26ba\\u7000\\u0712\\u5f6f\\u0001\\u2c0a\\u115c\\u2807\\u022f\\u0600\\u0713\\u0711\\u8d17\\u00d8\\u0100\\u1713\\u1711\\u1f16\\u9d2c\\u1711\\ua16f\\u0001\\u130a\\u1109\\u1309\\u1618\\u1913\\u272b\\u1811\\u1911\\u139a\\u110a\\u280ai\\u0a00\\u112d\\u0a11\\u2a28\\u000b\\u1306\\u080b\\u0b11\\ueb6f\\u0001\\u1106\\u1719\\u1358\\u1119\\u1119\\u8e18\\u3269\\u2bd1\\u1672\\u0c13\\u2028\\u000b\\u6f06\\u0b22\\u0600\\u0d13\\u6f03\\u0201\\u0600\\uc872&\\u1270\\u6f0e\\u015f\\u0a00\\u0e2c\\u0e11\\u2a28\\u000b\\u6f06\\u0b22\\u0600\\u0c13\\u6f03\\u0201\\u0600\\ufffd\\u1270\\u6f0f\\u015f\\u0a00\\u0e2c\\u0f11\\u2a28\\u000b\\u6f06\\u0b22\\u0600\\u0d13\\u0c11\\u1013\\u132b\\u1108\\u2810\\u0b29\\u0600\\ueb6f\\u0001\\u1106\\u1710\\u1358\\u1110\\u1110\\u310d\\u03e7\\u036f\\u0002\\u2806,\\u2b00\\u1113\\u1111\\u9a6f\\u0001\\u130a\\u2b1a\\u1256\\u281a\\u019b\\u0a00\\u1213\\u1211\\uff6f\\u0001\\u2806k\\u0a00\\u986f\\u0001\\u250a\\u1b13\\u372c\\u1b11\\uec72&\\u2870\\u0199\\u0a00\\u102d\\u1b11\\ufc72&\\u2870\\u0199\\u0a00\\u0d2d\\u192b\\u0802\\u1211\\u3b28\\u0002\\u2b06\\u020e\\u1211\\u6f08\\u01e2\\u0600\\u3a28\\u0002\\u1206\\u281a\\u019c\\u0a00\\ua12d\\u0ede\\u1a12\\u16fe~\\u1b00\\u036f\\u0000\\ufffd\\u0804\\u246f\\u0001\\u2a0a\\u0000\\u1001\\u0000\\u0002\\u0215\\u7863\\u0e02\\u0000\\u0000\\u301b\\u0004\\u007f\\u0000g\\u1100\\u1704\\ubf8d\\u0000\\u1301\\u1104\\u1604\\u0a72'\\ua270\\u0411\\u0c6f\\u0002\\u0406\\u036f\\u0002\\u2806,\\u2b00\\u060a\\u9a6f\\u0001\\u130a\\u2b05\\u1236\\u2805\\u019b\\u0a00\\u070b\\uff6f\\u0001\\u0c06\\u2802\\u0217\\u0600\\u656f\\u0001\\u0806\\ua26f\\u0001\\u0d0a\\u0902\\u1607\\u4628\\u0002\\u0306\\ue46f\\u0001\\u0906\\ua36f\\u0001\\u120a\\u2805\\u019c\\u0a00\\uc12d\\u0ede\\u0512\\u16fe~\\u1b00\\u036f\\u0000\\ufffd*\\u1001\\u0000\\u0002-\\u7043\\u0e00\\u0000\\u0000\\u3013\\u0004G\\u0000h\\u1100\\u1703\\ubf8d\\u0000\\u0c01\\u1608\\u1a72'\\ua270\\u6f08\\u020c\\u0600\\u7203\\u16ae\\u7000\\u086f\\u0002\\u0a06\\u0302\\u2c72'\\u6f70\\u0208\\u0600\\u4c28\\u0002\\u0b06\\u2802\\u01ad\\u0600\\u0706\\uca28\\b\\u6f06\\u0140\\u0a00*\\u301b\\u0004\\u01ec\\u0000i\\u1100\\u1803\\ubf8d\\u0000\\u1301\\u1108\\u1608\\u3872'\\ua270\\u0811\\u7217\\u2748\\u7000\\u11a2\\u6f08\\u020c\\u0600\\u7203\\u275c\\u7000\\u6f16\\u0209\\u0600\\u140a\\u730b\\u01a4\\u0a00\\u030c\\u036f\\u0002\\u2806,\\u2b00\\u090d\\u9a6f\\u0001\\u130a\\u3809\\u017f\\u0000\\u0912\\u9b28\\u0001\\u130a\\u1104\\u6f04\\u01ff\\u0600\\u0513\\u0411\\u6872'\\u1470\\u0b6f\\u0002\\u2806\\u0230\\u0600\\u0613\\u0511\\u6b28\\u0000\\u6f0a\\u0198\\u0a00\\u1325\\u390a\\u0145\\u0000\\u13fe\\uf97e\\u0004\\u2d04\\u1d61\\u9e73\\u0001\\u250a\\u7272'\\u1670\\u9f28\\u0001\\u250a\\u9272'\\u1770\\u9f28\\u0001\\u250a\\uc672'\\u1870\\u9f28\\u0001\\u250a\\ud472'\\u1970\\u9f28\\u0001\\u250a\\ue672'\\u1a70\\u9f28\\u0001\\u250a\\uf672'\\u1b70\\u9f28\\u0001\\u250a\\u1472(\\u1c70\\u9f28\\u0001\\ufe0a\\u8013\\u04f9\\u0400\\u13fe\\uf97e\\u0004\\u1104\\u120a\\u280b\\u01a0\\u0a00\\uc639\\u0000\\u1100\\u450b\\u0007\\u0000\\u0005\\u0000\\r\\u00004\\u00004\\u00004\\u00004\\u00004\\u0000\\u9e38\\u0000\\u1100\\u0b04\\u9638\\u0000\\u1100\\u2d06\\u7217\\u2834\\u7000\\u0511\\u7072(\\u2870\\u009d\\u0a00\\u5573\\f\\u7a06\\u1108\\u1106\\u6f04\\u01a5\\u0a00\\u6f2b\\u0611\\u172d\\u3472(\\u1170\\u7205\\u2870\\u7000\\u9d28\\u0000\\u730a\\u0c55\\u0600\\u027a\\u1728\\u0002\\u6f06\\u0164\\u0600\\u0611\\ua66f\\u0001\\u130a\\u0207\\u0711\\u0411\\u2808\\u023e\\u0600\\u2c06\\u1109\\u2807\\u0231\\u0600\\u0713\\u2c07\\u020b\\u0711\\u2807\\u024a\\u0600\\u0713\\u7872(\\u1170\\u2807.\\u2b00\\u1102\\u6f07\\u0c80\\u0600\\u0711\\ub628\\u0001\\u1206\\u2809\\u019c\\u0a00\\u753a\\ufffd\\ufffd\\u120e\\ufe09\\u7e16\\u0000\\u6f1b\\u0003\\u0a00\\u2adc\\u1c41\\u0000\\u0002\\u0000K\\u0000\\u0192\\u0000\\u01dd\\u0000\\u000e\\u0000\\u0000\\u0000\\u301b\\u0004\\u0212\\u0000j\\u1100\\u7204\\u2768\\u7000\\u086f\\u0002\\u2806\\u0230\\u0600\\u050a\\u142c\\u0605\\u0112\\ua76f\\u0001\\u2c0a\\u0209\\u0703\\u2814\\u023e\\u0600\\u7503\\u019a\\u0200\\u030c\\u9575\\u0001\\u0d02\\u0302\\u1704\\u4628\\u0002\\u0406\\u036f\\u0002\\u2806,\\u2b00\\u0413\\u0411\\u9a6f\\u0001\\u130a\\u380f\\u019b\\u0000\\u0f12\\u9b28\\u0001\\u130a\\u1105\\u6f05\\u01ff\\u0600\\u0613\\u3908\\u00ba\\u0000\\u0611\\u2e28\\u0002\\u2c06\\u1145\\u7205\\u16ae\\u7000\\u086f\\u0002\\u1306\\u0207\\u0711\\ub728\\u0001\\u1306\\u1108\\u2d08\\u7217\\u289c\\u7000\\u0711\\uc472(\\u2870\\u009d\\u0a00\\u5573\\f\\u7a06\\u6f08\\u0fc4\\u0600\\u0811\\u456f\\u0001\\u380a\\u0135\\u0000\\u0611\\u2d28\\u0002\\u2c06\\u1163\\u7205\\u2768\\u7000\\u086f\\u0002\\u2806\\u0230\\u0600\\u0913\\u2802\\u0217\\u0600\\u646f\\u0001\\u1106\\u6f09\\u01a6\\u0a00\\u0a13\\u0a11\\ufe39\\u0000\\u0200\\u0a11\\u0511\\u2805\\u023e\\u0600\\u0a11\\u806f\\f\\u2c06\\u020f\\u0a11\\u806f\\f\\u1106\\u280a\\u01b6\\u0600\\u6f08\\u0fc4\\u0600\\u0a11\\u456f\\u0001\\u380a\\u00c9\\u0000\\u3909\\u00ba\\u0000\\u0611\\u2e28\\u0002\\u2c06\\u113d\\u7205\\u16ae\\u7000\\u086f\\u0002\\u1306\\u020b\\u0b11\\ub728\\u0001\\u1306\\u110c\\u2d0c\\u7217\\u289c\\u7000\\u0b11\\uc472(\\u2870\\u009d\\u0a00\\u5573\\f\\u7a06\\u1109\\u6f0c\\u0f86\\u0600\\u7d2b\\u0611\\u2d28\\u0002\\u2c06\\u116b\\u7205\\u2768\\u7000\\u086f\\u0002\\u2806\\u0230\\u0600\\u0d13\\u2802\\u0217\\u0600\\u646f\\u0001\\u1106\\u6f0d\\u01a6\\u0a00\\u0e13\\u0e11\\u492c\\u1102\\u110e\\u0505\\u3e28\\u0002\\u1106\\u6f0e\\u0c80\\u0600\\u0f2c\\u1102\\u6f0e\\u0c80\\u0600\\u0e11\\ub628\\u0001\\u0906\\u856f\\u000f\\u2c06\\u720b\\u28de\\u7000\\u5573\\f\\u7a06\\u1109\\u6f0e\\u0f86\\u0600\\u092b\\u0302\\u0511\\u4428\\u0002\\u1206\\u280f\\u019c\\u0a00\\u593a\\ufffd\\ufffd\\u120e\\ufe0f\\u7e16\\u0000\\u6f1b\\u0003\\u0a00\\u2adc\\u0000\\u1c41\\u0000\\u0002\\u0000U\\u0000\\u01ae\\u0000\\u0203\\u0000\\u000e\\u0000\\u0000\\u0000\\u301b\\u0004\\u01d0\\u0000k\\u1100\\u1703\\ubf8d\\u0000\\u1301\\u110f\\u160f\\u1e72)\\ua270\\u0f11\\u0c6f\\u0002\\u0306\\u3472)\\u6f70\\u0207\\u0600\\u2c28\\u0000\\u0a2b\\u6f06\\u019a\\u0a00\\u1013\\u7c38\\u0001\\u1200\\u2810\\u019b\\u0a00\\u070b\\u3c72)\\u1470\\u0b6f\\u0002\\u0c06\\u2c08\\u080c\\u4a72)\\u2870\\u0099\\u0a00\\u070c\\u6872'\\u1470\\u0b6f\\u0002\\u2806\\u0230\\u0600\\u090d\\u502c\\u2802\\u0217\\u0600\\u1709\\uf528\\u0000\\u080a\\u736f\\u0001\\ufffd\\u133b\\u1104\\u2804\\u043f\\u0600\\u022c\\u1afe\\u0411\\u4e72)\\u2870\\u00bf\\u0600\\u8272)\\u0970\\u9928\\u0000\\u110a\\u7304\\u0c58\\u0600\\u0513\\u0511\\u3e28\\u0004\\u2c06\\u1103\\u7a05\\u00de\\u7207\\u29b8\\u7000\\u6f14\\u020b\\u0600\\u0613\\u0611\\u6e2c\\u1104\\u2806\\u00da\\u0a00\\u0713\\ud272)\\u1170\\u2807\\n\\u2b00\\u0711\\ue728\\u0000\\u130a\\u0208\\u1728\\u0002\\u1106\\u0808\\u6f6f\\u0001\\ufffd\\u00af\\u0000\\u0913\\u0911\\u3f28\\u0004\\u2c06\\ufe02\\u111a\\u7209\\u294e\\u7000\\ubf28\\u0000\\u7206\\u2982\\u7000\\u0611\\u9928\\u0000\\u110a\\u7309\\u0c58\\u0600\\u0a13\\u0a11\\u3e28\\u0004\\u2c06\\u1103\\u7a0a\\u73de\\u7207\\u2a08\\u7000\\u6f14\\u020b\\u0600\\u0b13\\u0b11\\u612c\\u1a72*\\u1170\\u280b\\n\\u2b00\\u0b11\\ua828\\u0001\\u130a\\u020c\\u1728\\u0002\\u1106\\u080c\\u6f6f\\u0001\\ufffd\\u133c\\u110d\\u280d\\u043f\\u0600\\u022c\\u1afe\\u0d11\\u4e72)\\u2870\\u00bf\\u0600\\u8272)\\u1170\\u280b\\u0099\\u0a00\\u0d11\\u5873\\f\\u1306\\u110e\\u280e\\u043e\\u0600\\u032c\\u0e11\\ufffd\\u1200\\u2810\\u019c\\u0a00\\u783a\\ufffd\\ufffd\\u120e\\ufe10\\u7e16\\u0000\\u6f1b\\u0003\\u0a00\\u2adc\\u6441\\u0000\\u0000\\u0000p\\u0000\\u0015\\u0000\\u0085\\u0000;\\u0000\\u0006\\u0100\\u0000\\u0000\\u00d2\\u00002\\u0000\\u0104\\u0000<\\u0000\\u0006\\u0100\\u0000\\u0000\\u0152\\u0000%\\u0000\\u0177\\u0000<\\u0000\\u0006\\u0100\\u0002\\u00002\\u0000\\u018f\\u0000\\u01c1\\u0000\\u000e\\u0000\\u0000\\u0000\\u301b\\u0005\\u00e3\\u0000l\\u1100\\u1703\\ubf8d\\u0000\\u1301\\u1104\\u1604\\u5072*\\ua270\\u0411\\u0c6f\\u0002\\u0306\\u6072*\\u6f70\\u0208\\u0600\\u030a\\u6a72*\\u1670\\u096f\\u0002\\u0b06\\u0602\\u4c28\\u0002\\u0a06\\u2806\\u08cd\\u0600\\u060a\\u040c\\u082c\\u0604\\ufffd\\u0c0a\\u2808\\u01a9\\u0a00\\u152c\\u8472*\\u0870\\u0b28\\u0000\\u022b\\u0508\\u3528\\u0002\\u2b06\\u0639\\u3d72\\u001d\\u6f70\\u01aa\\u0a00\\u0b2c\\u0402\\u0506\\u4128\\u0002\\u2b06\\u0721\\u0d2c\\uae72*\\u0870\\u0b28\\u0000\\ufffd\\u724f\\u2b12\\u7000\\u2808\\u0099\\u0a00\\uab73\\u0001\\u7a0a\\u3cde\\u090d\\u4672+\\u1770\\u048d\\u0000\\u1301\\u1105\\u1605\\ua206\\u0511\\ubb28\\u0000\\u0706\\u022c\\u1cde\\u2809\\u043e\\u0600\\u022c\\u1afe\\u7e72+\\u0670\\u9928\\u0000\\u090a\\u5873\\f\\u7a06*\\u1001\\u0000\\u00002\\ua674\\u3c00\\u0006\\u0100\\u3013\\u0003f\\u0000m\\u1100\\u0a03\\u2804\\u01ac\\u0a00\\u2f2c\\u2804\\u0080\\u0a00\\u060a\\u0c2d\\uac72+\\u0470\\u0d28\\u0000\\u2a2b\\u2804\\u00e1\\u0a00\\u070b\\u0c2d\\ufc72+\\u0470\\u0d28\\u0000\\u2a2b\\u1007\\u0602\\u2804\\u00e0\\u0a00\\u080c\\u0413\\u1316\\u2b05\\u1114\\u1104\\u9a05\\u020d\\u0509\\u3528\\u0002\\u1106\\u1705\\u1358\\u1105\\u1105\\u8e04\\u3269\\u2ae4\\u0000\\u3013\\u0004O\\u0000n\\u1100\\u1703\\ubf8d\\u0000\\u0c01\\u1608\\u4a72,\\ua270\\u6f08\\u020c\\u0600\\u7203\\u2768\\u7000\\u086f\\u0002\\u0a06\\u2802\\u0217\\u0600\\u6c6f\\u0001\\u0606\\uad6f\\u0001\\u0b0a\\u0702\\u1703\\u4628\\u0002\\u7206\\u2c54\\u7000\\u2807/\\u2b00\\u2807\\u1034\\u0600\\u1e2a\\u2802\\u01ae\\u0a00*\\u301b\\u0004X\\u0000&\\u1100\\u0302\\u2804\\u0245\\u0600\\u012c\\u022a\\u0403\\u4728\\u0002\\u2c06\\u2a01\\u0302\\u2804\\u0248\\u0600\\u012c\\u022a\\u6f04\\u0205\\u0600\\u4c28\\u0002\\u0a06\\u0403\\uff6f\\u0001\\u0606\\u2802\\u0217\\u0600\\ua928\\u0005\\ufffd\\u2614\\u8872,\\u0470\\uff6f\\u0001\\u0606\\u3028\\u0000\\ufe2b\\u2a1a\\u1001\\u0000\\u0000.\\u4315\\u1400\\u0154\\u0200\\u3013\\u0004h\\u0000o\\u1100\\u6f04\\u01ff\\u0600\\u030a\\u1206\\u2801\\u05ab\\u0600\\u022d\\u2a16\\u2807\\u05ac\\u0600\\u080c\\u2814\\u00d4\\u0a00\\u422c\\u0307\\u6f14\\u01af\\u0a00\\ue974\\u0000\\u0d01\\u0402\\u2808\\u024b\\u0600\\u0413\\u0411\\u082d\\u2808\\u0441\\u0600\\u0413\\u1102\\u0404\\u2817\\u0246\\u0600\\u1102\\u0404\\u4928\\u0002\\u0906\\u0411\\ub06f\\u0001\\u260a\\u2a17\\u2a16\\u301b\\u0004~\\u0000p\\u1100\\u6f04\\u0201\\u0600\\u3128\\u0000\\u0a2b\\u6f06\\u01b1\\u0a00\\u0413\\u4e2b\\u0412\\ub228\\u0001\\u0b0a\\u0112\\u0e28\\u0001\\u0c0a\\u0112\\u0f28\\u0001\\u0d0a\\u2c05\\u080e\\u6872'\\u1b70\\u946f\\u0000\\u2d0a\\u0325\\u0208\\u2809\\u024c\\u0600\\u2802\\u0217\\u0600\\ua928\\u0005\\ufffd\\u260f\\ud472,\\u0970\\u28080\\u2b00\\u1afe\\u0412\\ub328\\u0001\\u2d0a\\ufffd\\u120e\\ufe04\\u8716\\u0000\\u6f1b\\u0003\\u0a00\\u2adc\\u0000\\u1c01\\u0000\\u0000?\\u5516\\u0f00\\u0154\\u0200\\u0002\\u0014\\u6f5b\\u0e00\\u0000\\u0000\\u3013\\u0004A\\u0000q\\u1100\\u6f04\\u01ff\\u0600\\u030b\\u1207\\u2800\\u05ab\\u0600\\u2d2c\\u0402\\u6f06\\u01b4\\u0a00\\u4b28\\u0002\\u0c06\\u2c08\\u021c\\u0408\\u2817\\u0246\\u0600\\u0802\\u2804\\u0249\\u0600\\u0306\\u1408\\ub56f\\u0001\\u170a\\u162a*\\u0000\\u3013\\u0004:\\u0000r\\u1100\\u6f04\\u0205\\u0600\\u022c\\u2a16\\u6f04\\u01ff\\u0600\\u030a\\u1206\\u2801\\u05ab\\u0600\\u022d\\u2a16\\u0307\\u6f14\\u01af\\u0a00\\u020c\\u0408\\u2817\\u0246\\u0600\\u0802\\u2804\\u0249\\u0600\\u2a17\\u0000\\u301b\\u0003?\\u0000s\\u1100\\u6f04\\u0203\\u0600\\u2c28\\u0000\\u0a2b\\u6f06\\u019a\\u0a00\\u2b0c\\u1210\\u2802\\u019b\\u0a00\\u020b\\u0703\\u4428\\u0002\\u1206\\u2802\\u019c\\u0a00\\ue72d\\u0ede\\u0212\\u16fe~\\u1b00\\u036f\\u0000\\ufffd*\\u1001\\u0000\\u0002\\u0013\\u301d\\u0e00\\u0000\\u0000\\u3013\\u0004\\u00b1\\u0000t\\u1100\\u7204\\u2768\\u7000\\u086f\\u0002\\u2806\\u0230\\u0600\\u020a\\u1728\\u0002\\u6f06\\u0164\\u0600\\u6f06\\u01a6\\u0a00\\u070b\\u9575\\u0001\\u0c02\\u2d08\\u720b\\u2d2a\\u7000\\u5573\\f\\u7a06\\u0702\\u1404\\u3e28\\u0002\\u2b06\\u081a\\u856f\\u000f\\u7506\\u0195\\u0200\\u080c\\u0b2d\\ua872-\\u7370\\u0c55\\u0600\\u087a\\u856f\\u000f\\u2d06\\u08de\\u6f03\\u0f86\\u0600\\u0307\\u806f\\f\\u6f06\\u0c81\\u0600\\u0303\\u806f\\f\\u7206\\u1dfd\\u7000\\u9928\\u0000\\u6f0a\\u0c81\\u0600\\u3372.\\u0770\\u806f\\f\\u0706\\ua56f\\u0000\\u6f0a\\u00a6\\u0a00\\u6f03\\u0c80\\u0600\\u3228\\u0000\\u072b*\\u0000\\u3013\\u0003C\\u0000&\\u1100\\u1ed0\\u0001\\u2802~\\u0a00\\u6f04\\u01b6\\u0a00\\u022d\\u2a14\\u7203\\u2768\\u7000\\u6f14\\u020b\\u0600\\u3028\\u0002\\u0a06\\u2d06\\u1402\\u022a\\u1728\\u0002\\u6f06\\u0168\\u0600\\u0602\\u4c28\\u0002\\u6f06\\u01b7\\u0a00*\\u301b\\u0004i\\u0000u\\u1100\\u0a03\\u2802\\u01ad\\u0600\\u3328\\u0000\\u0b2b\\u6f07\\u01b8\\u0a00\\u0413\\u362b\\u0412\\ub928\\u0001\\u0c0a\\u0212\\u3f28\\u0001\\u0d0a\\u2c09\\u0623\\u9f72.\\u1270\\u2802\\u013e\\u0a00\\ua572.\\u2870\\u009d\\u0a00\\u6f09\\u08c1\\u0600\\ub76f\\u0000\\u0a0a\\u0412\\uba28\\u0001\\u2d0a\\ufffd\\u120e\\ufe04\\u8a16\\u0000\\u6f1b\\u0003\\u0a00\\u06dc*\\u0000\\u1001\\u0000\\u0002\\u0016\\u5943\\u0e00\\u0000\\u0000\\u023a\\u2728\\u0000\\u020a\\u2816\\u0255\\u0600\\u1e2a\\u7b02\\u00c4\\u0400\\u222a\\u0302\\uc47d\\u0000\\u2a04\\u0222\\u6f03\\u0257\\u0600\\u1e2a\\u7b02\\u00c6\\u0400\\u222a\\u0302\\uc67d\\u0000\\u2a04\\u0000\\u3013\\u0002#\\u0000]\\u1100\\u2802\\u0258\\u0600\\u6f03\\u00cf\\u0600\\u7e0a\\u00c5\\u0400\\u6f06\\u0093\\u0a00\\u072c\\u2802\\u0254\\u0600\\u162a\\u322a\\u8c17\\u00cc\\u0100\\uc580\\u0000\\u2a04\\u021e\\u5328\\u0002\\u2a06\\u0222\\u2803\\u00f2\\u0600\\u1e2a\\u2802\\u0253\\u0600\\u1e2a\\u7b02\\u00cd\\u0400\\u222a\\u0302\\ucd7d\\u0000\\u2a04\\u021e\\uce7b\\u0000\\u2a04\\u0222\\u7d03\\u00ce\\u0400\\u1e2a\\u7b02\\u00cf\\u0400\\u222a\\u0302\\ucf7d\\u0000\\u2a04\\u3013\\u00031\\u0000v\\u1100\\u2802\\u0261\\u0600\\u032d\\u2b1a\\u1b01\\u020a\\u5f28\\u0002\\u0306\\u486f\\b\\u0206\\u6328\\u0002\\u0606\\u956f\\u0000\\u160a\\u0732\\u2802\\u0254\\u0600\\u162a\\u1e2a\\u2802\\u025e\\u0600\\u1e2a\\u7b02\\u00d0\\u0400\\u222a\\u0302\\ud07d\\u0000\\u2a04\\u021e\\ud17b\\u0000\\u2a04\\u0222\\u7d03\\u00d1\\u0400*\\u3013\\u00030\\u0000v\\u1100\\u2802\\u0267\\u0600\\u032d\\u2b1a\\u1b01\\u020a\\u5f28\\u0002\\u0306\\u486f\\b\\u0206\\u6928\\u0002\\u0606\\u946f\\u0000\\u2c0a\\u0207\\u5428\\u0002\\u2a06\\u2a16\\u021e\\u5e28\\u0002\\u2a06\\u021e\\ud27b\\u0000\\u2a04\\u0222\\u7d03\\u00d2\\u0400\\u1e2a\\u7b02\\u00d3\\u0400\\u222a\\u0302\\ud37d\\u0000\\u2a04\\u0000\\u3013\\u00033\\u0000w\\u1100\\u2802\\u026f\\u0600\\u032d\\u2b1a\\u1b01\\u020a\\u5f28\\u0002\\u0306\\u486f\\b\\u0b06\\u0207\\u6d28\\u0002\\u0606\\u956f\\u0000\\u160a\\u072f\\u2802\\u0254\\u0600\\u162a\\u1e2a\\u2802\\u025e\\u0600\\u1e2a\\u2802\\u025e\\u0600\\u1e2a\\u7b02\\u00d4\\u0400\\u222a\\u0302\\ud47d\\u0000\\u2a04\\u021e\\ud57b\\u0000\\u2a04\\u0222\\u7d03\\u00d5\\u0400*\\u0000\\u3013\\u00030\\u0000v\\u1100\\u2802\\u0276\\u0600\\u032d\\u2b1a\\u1b01\\u020a\\u5f28\\u0002\\u0306\\u486f\\b\\u0206\\u7428\\u0002\\u0606\\u946f\\u0000\\u2d0a\\u0207\\u5428\\u0002\\u2a06\\u2a16\\u0222\\u2803\\u0280\\u0600\\u322a\\uf57e\\u0002\\u0204\\u8028\\u0002\\u2a06\\u7e32\\u02f6\\u0400\\u2802\\u0280\\u0600\\u322a\\uf77e\\u0002\\u0204\\u8028\\u0002\\u2a06\\u7e32\\u02f8\\u0400\\u2802\\u0280\\u0600\\u322a\\uf97e\\u0002\\u0204\\u8028\\u0002\\u2a06\\u7e32\\u02fa\\u0400\\u2802\\u0280\\u0600*\\u3013\\u0003@\\u0000x\\u1100\\u2503\\u062d\\u7e26[\\u0a00\\ubc28\\u0001\\u0a0a\\u2806\\u01bd\\u0a00\\u082d\\u2806\\u0b48\\u0600\\u052b\\ud67e\\u0000\\u0b04\\u0207\\u8373\\u0002\\u0c06\\u2c03\\u080d\\ua972.\\u0370\\u8f6f\\u0002\\u2606\\u2a08\\u282e\\u0b43\\u0600\\ud680\\u0000\\u2a04\\u0236\\u7e03\\u02f6\\u0400\\u8328\\u0002\\u2a06\\u0000\\u3013\\u0003`\\u0000y\\u1100\\u2802'\\u0a00\\u2d03\\u720b\\u065b\\u7000\\u2073\\u0001\\u7a0a\\u1404\\u2328\\u000b\\u2c06\\u720b\\u2ec7\\u7000\\u2073\\u0001\\u7a0a\\u0302\\ufffd\\u0204\\ud473\\b\\u0a06\\u0406\\ufffd\\b\\u0606\\u6f03\\u02b0\\u0600\\ue76f\\b\\u0606\\u3328\\u0010\\u6f06\\u1032\\u0600\\ufffd\\u0606\\ud77d\\u0000\\u2a04\\u021e\\ud77b\\u0000\\u2a04\\u023a\\ud77b\\u0000\\u0304\\ue56f\\b\\u0206\\u8a2a\\u1403\\u2328\\u000b\\u2c06\\u720b\\u2ec7\\u7000\\u2073\\u0001\\u7a0a\\u7b02\\u00d7\\u0400\\u6f03\\u08dd\\u0600\\u2a02\\u023a\\ud77b\\u0000\\u0304\\ue76f\\b\\u0206\\u3a2a\\u7b02\\u00d7\\u0400\\u6f03\\u08ea\\u0600\\u2a02\\u3013\\u0004%\\u0000\\u0013\\u1100\\u7b02\\u00d7\\u0400\\u6f03\\u08ea\\u0600\\u7b02\\u00d7\\u0400\\u8d17\\u0004\\u0100\\u060a\\u0416\\u06a2\\uec6f\\b\\u0206*\\u0000\\u3013\\u0004)\\u0000\\u0013\\u1100\\u7b02\\u00d7\\u0400\\u6f03\\u08ea\\u0600\\u7b02\\u00d7\\u0400\\u8d18\\u0004\\u0100\\u060a\\u0416\\u06a2\\u0517\\u06a2\\uec6f\\b\\u0206*\\u0000\\u3013\\u0004.\\u0000\\u0013\\u1100\\u7b02\\u00d7\\u0400\\u6f03\\u08ea\\u0600\\u7b02\\u00d7\\u0400\\u8d19\\u0004\\u0100\\u060a\\u0416\\u06a2\\u0517\\u06a2\\u0e18\\ua204\\u6f06\\u08ec\\u0600\\u2a02\\u0000\\u3013\\u00043\\u0000\\u0013\\u1100\\u7b02\\u00d7\\u0400\\u6f03\\u08ea\\u0600\\u7b02\\u00d7\\u0400\\u8d1a\\u0004\\u0100\\u060a\\u0416\\u06a2\\u0517\\u06a2\\u0e18\\ua204\\u1906\\u050e\\u06a2\\uec6f\\b\\u0206\\u6a2a\\u7b02\\u00d7\\u0400\\u6f03\\u08ea\\u0600\\u7b02\\u00d7\\u0400\\u6f04\\u08ec\\u0600\\u2a02\\u029a\\ud77b\\u0000\\u0304\\uee6f\\b\\u0206\\ud77b\\u0000\\u0404\\uea6f\\b\\u0206\\ud77b\\u0000\\u0504\\uec6f\\b\\u0206\\u8a2a\\u2d03\\u720b\\u16ae\\u7000\\u2073\\u0001\\u7a0a\\u7b02\\u00d7\\u0400\\uf16f\\b\\u0306\\u6f04\\u01be\\u0a00\\u2a02\\u301b\\u0004X\\u0000z\\u1100\\u2d03\\u720b\\u2ed9\\u7000\\u2073\\u0001\\u7a0a\\u6f03\\u01bf\\u0a00\\u026f\\u0000\\u0b0a\\u1f2b\\u6f07\\u0005\\u0a00\\u020a\\ud77b\\u0000\\u6f04\\u08f1\\u0600\\u0306\\u6f06\\u01c0\\u0a00\\ube6f\\u0001\\u070a\\u2a6f\\u0000\\u2d0a\\ufffd\\u0711\\u0a75\\u0000\\u0c01\\u2c08\\u0806\\u036f\\u0000\\ufffd\\u2a02\\u1001\\u0000\\u0002\\u001a\\u452b\\u1100\\u0000\\u0000\\u023a\\ud77b\\u0000\\u0304\\ufffd\\u0206\\u3e2a\\u7b02\\u00d7\\u0400\\u0403\\ufc6f\\b\\u0206*\\u3003\\u0003G\\u0000\\u0000\\u0000\\u2c03\\u020d\\uef72.\\u0370\\u8f28\\u0002\\u2606\\u2c04\\u020d\\ua972.\\u0470\\u8f28\\u0002\\u2606\\u2c05\\u0212\\u1172/\\u0570\\ud08c\\u0000\\u2801\\u028f\\u0600\\u0226\\ufffd\\u0204\\ud77b\\u0000\\u6f04\\u02b3\\u0600*\\u3003\\u0003U\\u0000\\u0000\\u0000\\u2c03\\u0308\\uc16f\\u0001\\u2d0a\\u2a01\\u2c04\\u020d\\uef72.\\u0470\\u8f28\\u0002\\u2606\\u2c05\\u020d\\ua972.\\u0570\\u8f28\\u0002\\u2606\\u040e\\u132c\\u7202\\u2f11\\u7000\\u040e\\ud08c\\u0000\\u2801\\u028f\\u0600\\u0226\\ufffd\\u0204\\ud77b\\u0000\\u6f04\\u02b3\\u0600*\\u0000\\u3003\\u0003M\\u0000\\u0000\\u0000\\u2d03\\u2a01\\u2c04\\u020d\\uef72.\\u0470\\u8f28\\u0002\\u2606\\u2c05\\u020d\\ua972.\\u0570\\u8f28\\u0002\\u2606\\u040e\\u132c\\u7202\\u2f11\\u7000\\u040e\\ud08c\\u0000\\u2801\\u028f\\u0600\\u0226\\ufffd\\u0204\\ud77b\\u0000\\u6f04\\u02b3\\u0600*\\u0000\\u3013\\u0002\\n\\u0000{\\u1100\\u0302\\u8373\\u0002\\u0a06\\u2a06\\u0000\\u3013\\u0002\\u000e\\u0000{\\u1100\\u7e02\\u02f5\\u0400\\u8373\\u0002\\u0a06\\u2a06\\u0000\\u3013\\u0002\\u000e\\u0000{\\u1100\\u7e02\\u02f6\\u0400\\u8373\\u0002\\u0a06\\u2a06\\u0000\\u3013\\u0002\\u000e\\u0000{\\u1100\\u7e02\\u02f7\\u0400\\u8373\\u0002\\u0a06\\u2a06\\u0000\\u3013\\u0002\\u000e\\u0000{\\u1100\\u7e02\\u02f8\\u0400\\u8373\\u0002\\u0a06\\u2a06\\u0000\\u3013\\u0002\\u000e\\u0000{\\u1100\\u7e02\\u02f9\\u0400\\u8373\\u0002\\u0a06\\u2a06\\u0000\\u3013\\u0002\\u000e\\u0000{\\u1100\\u7e02\\u02fa\\u0400\\u8373\\u0002\\u0a06\\u2a06\\u0222\\u2803\\u02a4\"}",
        "process": {
            "command_line": "\"C:\\ProgramData\\PCDr\\CSAW\\CSAW_Child.exe\" /child",
            "executable": "C:\\ProgramData\\PCDr\\CSAW\\CSAW_Child.exe",
            "hash": {
                "md5": "423050654da76dab9c2866ba3c13ce38",
                "sha1": "bb900fd4da5c72e3bb2c977dbbe2e3c02e1c387d",
                "sha256": "e5626a87403b5efbc0c1873059eeacd9ead8b046dcc7da32fbb4e87e9a5e8dfa"
            },
            "name": " ",
            "parent": {
                "command_line": "\"C:\\Users\\d.semren.SNS\\AppData\\Roaming\\PCDr\\Update\\Binaries\\CSAW.exe\" /NA /noui",
                "hash": {
                    "md5": "423050654da76dab9c2866ba3c13ce38",
                    "sha1": "bb900fd4da5c72e3bb2c977dbbe2e3c02e1c387d",
                    "sha256": "e5626a87403b5efbc0c1873059eeacd9ead8b046dcc7da32fbb4e87e9a5e8dfa"
                },
                "name": " ",
                "pid": 1780,
                "working_directory": "Local"
            },
            "pid": 14832,
            "start": "2021-09-16T14:22:42.671+00:00",
            "working_directory": "Local"
        },
        "related": {
            "hash": [
                "e5626a87403b5efbc0c1873059eeacd9ead8b046dcc7da32fbb4e87e9a5e8dfa",
                "423050654da76dab9c2866ba3c13ce38",
                "bb900fd4da5c72e3bb2c977dbbe2e3c02e1c387d"
            ],
            "user": [
                "SNS\\d.semren"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "id": "S-1-5-21-3542462677-1213864171-2030164332-6187",
            "name": "SNS\\d.semren"
        }
    }
    	
	```


=== "file_creation2.json"

    ```json
	
    {
        "event": {
            "start": "2206-11-13T06:23:32.121+00:00",
            "action": "fileCreation"
        },
        "deepvisibility": {
            "event": {
                "type": "fileCreation"
            },
            "true_context": {
                "key": "CCC43343435EABDF"
            },
            "agent": {
                "seq_id": 35,
                "uuid": "4d311e18709146cba871111111111111",
                "trace_id": "BABABABABEEE43452345234523423423",
                "managment_url": "https://euce1-110-nfr.sentinelone.net"
            },
            "process": {
                "family": "SYS_WIN32",
                "executable": {
                    "name": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "node": {
                        "key": "C8E88AA83F5B15B6"
                    },
                    "start": "2021-08-05T07:45:42.654+00:00",
                    "is_dir": "E_FALSE",
                    "size_bytes": "2442584",
                    "signature": {
                        "signed": {
                            "identity": "GOOGLE LLC"
                        }
                    }
                },
                "parent": {
                    "node": {
                        "key": "03267F6915111A61"
                    }
                },
                "counters": {
                    "model_child_process": 25,
                    "os_child_process": 25,
                    "cross_process": 1610,
                    "module_load": 245,
                    "file_creation": 148,
                    "file_deletion": 58,
                    "file_modification": 416,
                    "registry_modification": 32,
                    "cross_process_dup_thread_handle": 20,
                    "cross_process_dup_process_handle": 1590
                },
                "node": {
                    "key": "BAE25D38782A6941"
                },
                "user": {
                    "sid": "S-1-5-21-6562365326-8585787878-2021012021-6543"
                },
                "interactive": "E_FALSE",
                "excluded": "E_FALSE",
                "root": "E_TRUE",
                "session_id": 11,
                "integrity_level": "MEDIUM",
                "is_wow64": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "true_context": {
                    "key": "CCC43343435EABDF"
                }
            },
            "host": {
                "os": {
                    "revision": "88888"
                }
            },
            "file": {
                "node": {
                    "key": "737373ABCDEF7373"
                },
                "location": "Local"
            }
        },
        "agent": {
            "version": "S1-WIN/2.2.11.333"
        },
        "process": {
            "name": "Google Chrome",
            "working_directory": "Local",
            "command_line": "\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\"",
            "pid": 14896,
            "start": "2021-08-09T13:28:53.932+00:00",
            "executable": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        },
        "file": {
            "created": "2206-11-13T06:23:32.121+00:00",
            "path": "C:\\Users\\a.hifumii\\AppData\\Local\\Google\\Chrome\\User Data\\98798798-bbb2-9898-aaaa-1212121212f.tmp",
            "type": "file",
            "extension": "tmp",
            "name": "98798798-bbb2-9898-aaaa-1212121212f.tmp"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "user": [
                "SNS\\a.hifumii"
            ]
        },
        "user": {
            "name": "SNS\\a.hifumii",
            "id": "S-1-5-21-6562365326-8585787878-2021012021-6543"
        },
        "host": {
            "type": "laptop",
            "name": "LAPTOP-COM13",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            }
        }
    }
    	
	```


=== "process_exit.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.5.7.370"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "seq_id": 102,
                "trace_id": "AEA057B816964BDF82E0E2EC171B0C10",
                "uuid": "e4fb82d7034d4d8983f8f9e103aa394b"
            },
            "event": {
                "type": "processExit"
            },
            "host": {
                "os": {
                    "revision": "19043"
                }
            },
            "process": {
                "counters": {
                    "module_load": 212
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\WINDOWS\\System32\\wermgr.exe",
                    "node": {
                        "key": "31E86945F742D096"
                    },
                    "signature": {
                        "signed": {
                            "identity": "MICROSOFT WINDOWS"
                        }
                    },
                    "size_bytes": "228680",
                    "start": "18446732429235951616"
                },
                "family": "SYS_WIN32",
                "integrity_level": "SYSTEM",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "03B4B5C3910B72FF"
                },
                "parent": {
                    "counters": {
                        "cross_process": 39,
                        "model_child_process": 1095,
                        "module_load": 80,
                        "os_child_process": 1095
                    },
                    "excluded": "E_FALSE",
                    "executable": {
                        "is_dir": "E_FALSE",
                        "name": "C:\\WINDOWS\\System32\\svchost.exe",
                        "node": {
                            "key": "B10478282C996149"
                        },
                        "signature": {
                            "signed": {
                                "identity": "MICROSOFT WINDOWS PUBLISHER"
                            }
                        },
                        "size_bytes": "57360",
                        "start": "18446732429235951616"
                    },
                    "family": "SYS_WIN32",
                    "integrity_level": "SYSTEM",
                    "interactive": "E_FALSE",
                    "is_redirected_command_processor": "E_FALSE",
                    "is_wow64": "E_FALSE",
                    "node": {
                        "key": "6308FCA4876DA87C"
                    },
                    "parent": {
                        "node": {
                            "key": "6B6B39C296E3FD3D"
                        }
                    },
                    "root": "E_TRUE",
                    "true_context": {
                        "key": "D4ADBE51EE6EC2D0"
                    },
                    "user": {
                        "sid": "S-1-5-18"
                    }
                },
                "root": "E_TRUE",
                "true_context": {
                    "key": "3B49B9603DFF38C9"
                },
                "user": {
                    "sid": "S-1-5-18"
                }
            },
            "true_context": {
                "key": "3B49B9603DFF38C9"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "start": "2021-09-14T15:51:44.684+00:00",
            "action": "processExit"
        },
        "host": {
            "name": "LAPTOP-COM08",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"seqId\": 102, \"uuid\": \"e4fb82d7034d4d8983f8f9e103aa394b\", \"traceId\": \"AEA057B816964BDF82E0E2EC171B0C10\", \"agentVersion\": \"S1-WIN/21.5.7.370\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19043\", \"computerName\": \"LAPTOP-COM08\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631634704684\"}, \"event_type\": \"processExit\", \"trueContext\": {\"key\": {\"value\": \"3B49B9603DFF38C9\"}}, \"source\": {\"node\": {\"key\": {\"value\": \"03B4B5C3910B72FF\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"31E86945F742D096\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\WINDOWS\\\\System32\\\\wermgr.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"228680\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"573ad9af63a6a0ab9b209ece518fd582b54cfef5\", \"sha256\": \"1c09759dcd31fdc81bcd6685438d7efb34e0229f1096bfd57d41ecfe614d07dc\", \"md5\": \"f7991343cf02ed92cb59f394e8b89f1f\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"C:\\\\WINDOWS\\\\system32\\\\wermgr.exe -upload\", \"fullPid\": {\"pid\": 9876, \"startTime\": {\"millisecondsSinceEpoch\": \"1631634703718\"}}, \"user\": {\"name\": \"AUTORITE NT\\\\Syst\\u00e8me\", \"sid\": \"S-1-5-18\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"6308FCA4876DA87C\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Windows Problem Reporting\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"integrityLevel\": \"SYSTEM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"3B49B9603DFF38C9\"}}, \"counters\": {\"moduleLoad\": 212}}, \"parent\": {\"node\": {\"key\": {\"value\": \"6308FCA4876DA87C\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"B10478282C996149\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\WINDOWS\\\\System32\\\\svchost.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"57360\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS PUBLISHER\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"010db07461e45b41c886192df6fd425ba8d42d82\", \"sha256\": \"643ec58e82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7\", \"md5\": \"f586835082f632dc8d9404d83bc16316\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"C:\\\\WINDOWS\\\\system32\\\\svchost.exe -k netsvcs -p -s Schedule\", \"fullPid\": {\"pid\": 1744, \"startTime\": {\"millisecondsSinceEpoch\": \"1631022021170\"}}, \"user\": {\"name\": \"AUTORITE NT\\\\Syst\\u00e8me\", \"sid\": \"S-1-5-18\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"6B6B39C296E3FD3D\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Host Process for Windows Services\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"integrityLevel\": \"SYSTEM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"D4ADBE51EE6EC2D0\"}}, \"counters\": {\"modelChildProcess\": 1095, \"osChildProcess\": 1095, \"crossProcess\": 39, \"moduleLoad\": 80, \"crossProcessOutOfGroup\": 39, \"crossProcessOpenProcess\": 39}}}",
        "process": {
            "command_line": "C:\\WINDOWS\\system32\\wermgr.exe -upload",
            "hash": {
                "md5": "f7991343cf02ed92cb59f394e8b89f1f",
                "sha1": "573ad9af63a6a0ab9b209ece518fd582b54cfef5",
                "sha256": "1c09759dcd31fdc81bcd6685438d7efb34e0229f1096bfd57d41ecfe614d07dc"
            },
            "name": "Windows Problem Reporting",
            "parent": {
                "command_line": "C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Schedule",
                "hash": {
                    "md5": "f586835082f632dc8d9404d83bc16316",
                    "sha1": "010db07461e45b41c886192df6fd425ba8d42d82",
                    "sha256": "643ec58e82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7"
                },
                "name": "Host Process for Windows Services",
                "pid": 1744,
                "start": "2021-09-07T13:40:21.170+00:00",
                "working_directory": "Local"
            },
            "pid": 9876,
            "start": "2021-09-14T15:51:43.718+00:00",
            "working_directory": "Local",
            "executable": "C:\\WINDOWS\\System32\\wermgr.exe"
        },
        "related": {
            "hash": [
                "573ad9af63a6a0ab9b209ece518fd582b54cfef5",
                "643ec58e82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7",
                "1c09759dcd31fdc81bcd6685438d7efb34e0229f1096bfd57d41ecfe614d07dc",
                "f586835082f632dc8d9404d83bc16316",
                "f7991343cf02ed92cb59f394e8b89f1f",
                "010db07461e45b41c886192df6fd425ba8d42d82"
            ],
            "user": [
                "AUTORITE NT\\Syst\u00e8me"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "id": "S-1-5-18",
            "name": "AUTORITE NT\\Syst\u00e8me"
        }
    }
    	
	```


=== "reg_value_delete.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.5.7.370"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "seq_id": 43,
                "trace_id": "63014A4A2D8B42148CBD53DA4C5937A8",
                "uuid": "19f22913365942f2afeed1463c96104b"
            },
            "event": {
                "type": "regValueDelete"
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "process": {
                "counters": {
                    "file_modification": 1,
                    "model_child_process": 2,
                    "net_conn_out": 26,
                    "os_child_process": 2
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\Windows\\System32\\ntoskrnl.exe",
                    "node": {
                        "key": "AC786EF3445E33CE"
                    },
                    "signature": {
                        "signed": {
                            "identity": "MICROSOFT WINDOWS"
                        }
                    },
                    "size_bytes": "10848576",
                    "start": "18446732429235951616"
                },
                "family": "SYS_WIN32",
                "integrity_level": "SYSTEM",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "1BA4624EB033A7CC"
                },
                "parent": {
                    "node": {
                        "key": "1BA4624EB033A7CC"
                    }
                },
                "root": "E_TRUE",
                "true_context": {
                    "key": "6508114A467ECCA8"
                }
            },
            "true_context": {
                "key": "6508114A467ECCA8"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "regValueDelete",
            "start": "2021-09-16T09:38:25.794+00:00"
        },
        "host": {
            "name": "LAPTOP-COM11",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"seqId\": 43, \"uuid\": \"19f22913365942f2afeed1463c96104b\", \"traceId\": \"63014A4A2D8B42148CBD53DA4C5937A8\", \"agentVersion\": \"S1-WIN/21.5.7.370\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-COM11\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631785105794\"}, \"event_type\": \"regValueDelete\", \"trueContext\": {\"key\": {\"value\": \"6508114A467ECCA8\"}}, \"regValue\": {\"key\": {}, \"path\": \"MACHINE\\\\SYSTEM\\\\ControlSet001\\\\Services\\\\SentinelDeviceControl\\\\Enum\\\\53\"}, \"source\": {\"node\": {\"key\": {\"value\": \"1BA4624EB033A7CC\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"AC786EF3445E33CE\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\Windows\\\\System32\\\\ntoskrnl.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"10848576\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"560b6a3b55112d9834e28def41d5ac3de0e03928\"}}, \"fullPid\": {\"pid\": 4, \"startTime\": {\"millisecondsSinceEpoch\": \"1631781067519\"}}, \"user\": {\"name\": \"SYSTEM\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"1BA4624EB033A7CC\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"NT Kernel & System\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"integrityLevel\": \"SYSTEM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"6508114A467ECCA8\"}}, \"counters\": {\"modelChildProcess\": 2, \"osChildProcess\": 2, \"fileModification\": 1, \"netConnIn\": 16, \"netConnOut\": 26}}}",
        "process": {
            "executable": "C:\\Windows\\System32\\ntoskrnl.exe",
            "hash": {
                "sha1": "560b6a3b55112d9834e28def41d5ac3de0e03928"
            },
            "name": "NT Kernel & System",
            "pid": 4,
            "start": "2021-09-16T08:31:07.519+00:00"
        },
        "registry": {
            "path": "MACHINE\\SYSTEM\\ControlSet001\\Services\\SentinelDeviceControl\\Enum\\53",
            "value": "53"
        },
        "related": {
            "hash": [
                "560b6a3b55112d9834e28def41d5ac3de0e03928"
            ],
            "user": [
                "SYSTEM"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "name": "SYSTEM"
        }
    }
    	
	```


=== "file_deletion.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.7.1.240"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "trace_id": "01FFJG3VW54HS5577EY3CY83M8",
                "uuid": "f63008e522ce40c9afd4348634b5ab3b"
            },
            "event": {
                "type": "fileDeletion"
            },
            "file": {
                "location": "Local",
                "node": {
                    "key": "780E03EC9E64BBE3"
                }
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "process": {
                "counters": {
                    "cross_process": 332191,
                    "cross_process_dup_process_handle": 329760,
                    "cross_process_dup_thread_handle": 2431,
                    "dns_lookups": 5,
                    "file_creation": 295369,
                    "file_deletion": 282078,
                    "file_modification": 849997,
                    "model_child_process": 761,
                    "module_load": 1177,
                    "net_conn_out": 5,
                    "os_child_process": 761,
                    "registry_modification": 788
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "node": {
                        "key": "05893E5943D0005C"
                    },
                    "signature": {
                        "signed": {
                            "identity": "GOOGLE LLC"
                        }
                    },
                    "size_bytes": "2465624",
                    "start": "2021-09-02T08:59:58.477+00:00"
                },
                "family": "SYS_WIN32",
                "integrity_level": "MEDIUM",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "0D7A69B0C2C26E73"
                },
                "parent": {
                    "node": {
                        "key": "41CA3A862279A7BC"
                    }
                },
                "root": "E_TRUE",
                "session_id": 1,
                "true_context": {
                    "key": "6B188EE5E8C5F24F"
                },
                "user": {
                    "sid": "S-1-5-21-3542462677-1213864171-2030164332-6187"
                }
            },
            "true_context": {
                "key": "6B188EE5E8C5F24F"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "fileDeletion",
            "start": "2021-09-14T15:51:46.079+00:00"
        },
        "file": {
            "created": "2021-09-14T15:51:45.524+00:00",
            "extension": "exe",
            "name": "todelete_429a860c9774094b_0_1.exe",
            "path": "C:\\Users\\d.semren.SNS\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Service Worker\\CacheStorage\\1ab01c3b969bd7dcc799e2be1a4ce60699f20543\\650d1e12-cd20-438f-8c15-b58c713de9c7\\todelete_429a860c9774094b_0_1.exe",
            "type": "file"
        },
        "host": {
            "name": "LAPTOP-TECH20",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"uuid\": \"f63008e522ce40c9afd4348634b5ab3b\", \"traceId\": \"01FFJG3VW54HS5577EY3CY83M8\", \"agentVersion\": \"S1-WIN/21.7.1.240\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-TECH20\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631634706079\"}, \"event_type\": \"fileDeletion\", \"trueContext\": {\"key\": {\"value\": \"6B188EE5E8C5F24F\"}}, \"source\": {\"node\": {\"key\": {\"value\": \"0D7A69B0C2C26E73\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"05893E5943D0005C\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"1630573198477\"}, \"path\": \"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"2465624\", \"signature\": {\"signed\": {\"identity\": \"GOOGLE LLC\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"a82705f4f5d1408f7c14d16a9cbe26c509422b29\", \"sha256\": \"07832d5f6344bd4d68376a6ca3c5baabb9cef7166a3752268e73fadffb07ddff\", \"md5\": \"a766188d75e570ea3f9b09fb9d82cb54\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"\\\"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\\\"\", \"fullPid\": {\"pid\": 26188, \"startTime\": {\"millisecondsSinceEpoch\": \"1631516876708\"}}, \"user\": {\"name\": \"SNS\\\\d.semren\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6187\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"41CA3A862279A7BC\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Google Chrome\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 1, \"integrityLevel\": \"MEDIUM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"6B188EE5E8C5F24F\"}}, \"counters\": {\"modelChildProcess\": 761, \"osChildProcess\": 761, \"crossProcess\": 332191, \"moduleLoad\": 1177, \"fileCreation\": 295369, \"fileDeletion\": 282078, \"fileModification\": 849997, \"netConnOut\": 5, \"registryModification\": 788, \"crossProcessDupThreadHandle\": 2431, \"crossProcessDupProcessHandle\": 329760, \"dnsLookups\": 5}}, \"targetFile\": {\"node\": {\"key\": {\"value\": \"780E03EC9E64BBE3\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"1631634705524\"}, \"path\": \"C:\\\\Users\\\\d.semren.SNS\\\\AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Service Worker\\\\CacheStorage\\\\1ab01c3b969bd7dcc799e2be1a4ce60699f20543\\\\650d1e12-cd20-438f-8c15-b58c713de9c7\\\\todelete_429a860c9774094b_0_1.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"hashes\": {}, \"fileLocation\": \"Local\"}}",
        "process": {
            "command_line": "\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\"",
            "hash": {
                "md5": "a766188d75e570ea3f9b09fb9d82cb54",
                "sha1": "a82705f4f5d1408f7c14d16a9cbe26c509422b29",
                "sha256": "07832d5f6344bd4d68376a6ca3c5baabb9cef7166a3752268e73fadffb07ddff"
            },
            "name": "Google Chrome",
            "pid": 26188,
            "start": "2021-09-13T07:07:56.708+00:00",
            "working_directory": "Local",
            "executable": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        },
        "related": {
            "hash": [
                "a766188d75e570ea3f9b09fb9d82cb54",
                "a82705f4f5d1408f7c14d16a9cbe26c509422b29",
                "07832d5f6344bd4d68376a6ca3c5baabb9cef7166a3752268e73fadffb07ddff"
            ],
            "user": [
                "SNS\\d.semren"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "id": "S-1-5-21-3542462677-1213864171-2030164332-6187",
            "name": "SNS\\d.semren"
        }
    }
    	
	```


=== "file_creation_missing_fields.json"

    ```json
	
    {
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "message": "{\"timestamp\":{\"millisecondsSinceEpoch\":\"1629899209700\"},\"fileCreation\":{\"trueContext\":{\"key\":{\"value\":\"0506A768B8828E35\"}},\"source\":{\"node\":{\"key\":{\"value\":\"2FFCA561EE506063\"}},\"executable\":{\"node\":{\"key\":{\"value\":\"E4CD922E494CA3C5\"}},\"creationTime\":{},\"path\":\"C:\\\\Program Files\\\\Fortinet\\\\FortiClient\\\\FortiESNAC.exe\",\"owner\":{},\"isDir\":\"E_FALSE\",\"sizeBytes\":\"4253328\",\"hashes\":{},\"fileLocation\":\"Local\"},\"commandLine\":\"FortiESNAC.exe -s FC_{73EFB30F-1CAD-4a7a-AE2E-150282B6CE25}_000018\",\"fullPid\":{\"pid\":6104,\"startTime\":{\"millisecondsSinceEpoch\":\"1629878298032\"}},\"user\":{\"name\":\"AUTORITE NT\\\\Syst\u00e8me\",\"sid\":\"S-1-5-18\"},\"interactive\":\"E_FALSE\",\"parent\":{\"node\":{\"key\":{\"value\":\"D3250A9CB211CC1E\"}},\"fullPid\":{\"startTime\":{}}},\"excluded\":\"E_FALSE\",\"name\":\"FortiClient Network Access Control\",\"root\":\"E_FALSE\",\"subsystem\":\"SYS_WIN32\",\"integrityLevel\":\"SYSTEM\",\"isWow64\":\"E_FALSE\",\"isRedirectedCommandProcessor\":\"E_FALSE\",\"trueContext\":{\"key\":{\"value\":\"0506A768B8828E35\"}},\"counters\":{\"moduleLoad\":1948,\"fileCreation\":647,\"fileDeletion\":647,\"fileModification\":2141,\"exeModification\":40,\"netConnOut\":203,\"registryModification\":654,\"dnsLookups\":30}},\"targetFile\":{\"node\":{\"key\":{\"value\":\"4685AD1C6BC7D31D\"}},\"creationTime\":{},\"path\":\"C:\\\\Program Files\\\\Fortinet\\\\FortiClient\\\\large_data_upload\\\\0.bin\",\"owner\":{},\"isDir\":\"E_FALSE\",\"hashes\":{},\"fileLocation\":\"Local\"}},\"meta\":{\"seqId\":45,\"uuid\":\"6ce43ff9d060310b37fb4eba7ad3c1f0f2d9a5ab\",\"traceId\":\"E1A04C7727EB41E5A3D0FF068D4BE544\",\"agentVersion\":\"S1-WIN/4.4.3.149\",\"osFamily\":\"windows\",\"osName\":\"Windows 10 Pro\",\"osRevision\":\"19043\",\"computerName\":\"LAPTOP-COM4\",\"machineType\":\"laptop\",\"mgmtUrl\":\"https://euce1-110-nfr.sentinelone.net\"}}",
        "event": {
            "start": "2021-08-25T13:46:49.700+00:00",
            "action": "fileCreation"
        },
        "deepvisibility": {
            "true_context": {
                "key": "0506A768B8828E35"
            },
            "event": {
                "type": "fileCreation"
            },
            "agent": {
                "seq_id": 45,
                "uuid": "6ce43ff9d060310b37fb4eba7ad3c1f0f2d9a5ab",
                "trace_id": "E1A04C7727EB41E5A3D0FF068D4BE544",
                "managment_url": "https://euce1-110-nfr.sentinelone.net"
            },
            "host": {
                "os": {
                    "revision": "19043"
                }
            },
            "process": {
                "node": {
                    "key": "2FFCA561EE506063"
                },
                "executable": {
                    "node": {
                        "key": "E4CD922E494CA3C5"
                    },
                    "name": "C:\\Program Files\\Fortinet\\FortiClient\\FortiESNAC.exe",
                    "is_dir": "E_FALSE",
                    "size_bytes": "4253328"
                },
                "user": {
                    "sid": "S-1-5-18"
                },
                "interactive": "E_FALSE",
                "parent": {
                    "node": {
                        "key": "D3250A9CB211CC1E"
                    }
                },
                "excluded": "E_FALSE",
                "root": "E_FALSE",
                "family": "SYS_WIN32",
                "integrity_level": "SYSTEM",
                "is_wow64": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "true_context": {
                    "key": "0506A768B8828E35"
                },
                "counters": {
                    "module_load": 1948,
                    "file_creation": 647,
                    "file_deletion": 647,
                    "file_modification": 2141,
                    "registry_modification": 654,
                    "dns_lookups": 30,
                    "net_conn_out": 203
                }
            },
            "file": {
                "node": {
                    "key": "4685AD1C6BC7D31D"
                },
                "location": "Local"
            }
        },
        "agent": {
            "version": "S1-WIN/4.4.3.149"
        },
        "host": {
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "name": "LAPTOP-COM4",
            "type": "laptop"
        },
        "process": {
            "working_directory": "Local",
            "command_line": "FortiESNAC.exe -s FC_{73EFB30F-1CAD-4a7a-AE2E-150282B6CE25}_000018",
            "pid": 6104,
            "start": "2021-08-25T07:58:18.032+00:00",
            "name": "FortiClient Network Access Control",
            "executable": "C:\\Program Files\\Fortinet\\FortiClient\\FortiESNAC.exe"
        },
        "user": {
            "name": "AUTORITE NT\\Syst\u00e8me",
            "id": "S-1-5-18"
        },
        "file": {
            "path": "C:\\Program Files\\Fortinet\\FortiClient\\large_data_upload\\0.bin",
            "type": "file",
            "extension": "bin",
            "name": "0.bin"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "user": [
                "AUTORITE NT\\Syst\u00e8me"
            ]
        }
    }
    	
	```


=== "open_process.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.5.7.370"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "seq_id": 63,
                "trace_id": "CEBBC94D38B041B1B2DE01C315EB28F5",
                "uuid": "bcc4bf7a284441599707050e1d58a8dd"
            },
            "event": {
                "type": "openProcess"
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "process": {
                "counters": {
                    "cross_process": 5262,
                    "dns_lookups": 51,
                    "module_load": 222,
                    "net_conn_out": 1813
                },
                "desired_access": 5240,
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\WINDOWS\\system32\\lsass.exe",
                    "node": {
                        "key": "1F70F08D24687577"
                    },
                    "signature": {
                        "signed": {
                            "identity": "MICROSOFT WINDOWS PUBLISHER"
                        }
                    },
                    "size_bytes": "59448",
                    "start": "18446732429235951616"
                },
                "family": "SYS_WIN32",
                "integrity_level": "SYSTEM",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "2A2CC1C3468CB3D8"
                },
                "parent": {
                    "excluded": "E_FALSE",
                    "executable": {
                        "is_dir": "E_FALSE",
                        "name": "C:\\WINDOWS\\system32\\wininit.exe",
                        "node": {
                            "key": "E2ABEBDC5F08F279"
                        },
                        "signature": {
                            "signed": {
                                "identity": "MICROSOFT WINDOWS PUBLISHER"
                            }
                        },
                        "size_bytes": "419432",
                        "start": "18446732429235951616"
                    },
                    "family": "SYS_WIN32",
                    "integrity_level": "SYSTEM",
                    "interactive": "E_FALSE",
                    "is_redirected_command_processor": "E_FALSE",
                    "is_wow64": "E_FALSE",
                    "node": {
                        "key": "611EAD3E998CF40A"
                    },
                    "parent": {
                        "node": {
                            "key": "0D332A871A7DB912"
                        }
                    },
                    "root": "E_TRUE",
                    "true_context": {
                        "key": "5318E7F038459CED"
                    },
                    "user": {
                        "sid": "S-1-5-18"
                    }
                },
                "relations": "PR_OTHER",
                "root": "E_TRUE",
                "target": {
                    "command_line": "taskhostw.exe Install $(Arg0)",
                    "counters": {
                        "module_load": 44
                    },
                    "excluded": "E_FALSE",
                    "executable": {
                        "is_dir": "E_FALSE",
                        "name": "C:\\WINDOWS\\system32\\taskhostw.exe",
                        "node": {
                            "key": "23FF6C2F651EEA11"
                        },
                        "signature": {
                            "signed": {
                                "identity": "MICROSOFT WINDOWS"
                            }
                        },
                        "size_bytes": "97096",
                        "start": "18446732429235951616"
                    },
                    "family": "SYS_WIN32",
                    "hash": {
                        "md5": "564e4806ab18f93b93d551cd10c1598e",
                        "sha1": "fed4b4a753a9541389aa670c69e624be07569ccd",
                        "sha256": "0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad"
                    },
                    "integrity_level": "MEDIUM",
                    "interactive": "E_FALSE",
                    "is_redirected_command_processor": "E_FALSE",
                    "is_wow64": "E_FALSE",
                    "name": "Host Process for Windows Tasks",
                    "node": {
                        "key": "E94742BA9CF1A186"
                    },
                    "parent": {
                        "node": {
                            "key": "399C73C0494DC82C"
                        }
                    },
                    "pid": 15728,
                    "root": "E_TRUE",
                    "session_id": 7,
                    "start": "2021-09-14T15:51:51.621+00:00",
                    "true_context": {
                        "key": "AB55C980E679578F"
                    },
                    "user": {
                        "sid": "S-1-5-21-3542462677-1213864171-2030164332-6152"
                    },
                    "working_directory": "Local"
                },
                "true_context": {
                    "key": "A2DC49811AF8CC72"
                },
                "user": {
                    "sid": "S-1-5-18"
                }
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "start": "2021-09-14T15:51:52.102+00:00",
            "action": "openProcess"
        },
        "host": {
            "name": "LAPTOP-TECH15",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"seqId\": 63, \"uuid\": \"bcc4bf7a284441599707050e1d58a8dd\", \"traceId\": \"CEBBC94D38B041B1B2DE01C315EB28F5\", \"agentVersion\": \"S1-WIN/21.5.7.370\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-TECH15\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631634712102\"}, \"event_type\": \"openProcess\", \"source\": {\"node\": {\"key\": {\"value\": \"2A2CC1C3468CB3D8\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"1F70F08D24687577\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\WINDOWS\\\\system32\\\\lsass.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"59448\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS PUBLISHER\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"28f7fb54c7bcd9d6e71669ea5bddf72ea65311ce\", \"sha256\": \"362ab9743ff5d0f95831306a780fc3e418990f535013c80212dd85cb88ef7427\", \"md5\": \"15a556def233f112d127025ab51ac2d3\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"C:\\\\WINDOWS\\\\system32\\\\lsass.exe\", \"fullPid\": {\"pid\": 992, \"startTime\": {\"millisecondsSinceEpoch\": \"1630919462523\"}}, \"user\": {\"name\": \"AUTORITE NT\\\\Syst\\u00e8me\", \"sid\": \"S-1-5-18\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"611EAD3E998CF40A\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"E2ABEBDC5F08F279\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\WINDOWS\\\\system32\\\\wininit.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"419432\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS PUBLISHER\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"915ea28bdaa9a2230ce52080693d7f7e27620ed5\", \"sha256\": \"268ca325c8f12e68b6728ff24d6536030aab6e05603d0179033b1e51d8476d86\", \"md5\": \"9ef51c8ad595c5e2a123c06ad39fccd7\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"wininit.exe\", \"fullPid\": {\"pid\": 900, \"startTime\": {\"millisecondsSinceEpoch\": \"1630919462470\"}}, \"user\": {\"name\": \"AUTORITE NT\\\\Syst\\u00e8me\", \"sid\": \"S-1-5-18\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"0D332A871A7DB912\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Windows Start-Up Application\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"integrityLevel\": \"SYSTEM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"5318E7F038459CED\"}}}, \"excluded\": \"E_FALSE\", \"name\": \"Local Security Authority Process\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"integrityLevel\": \"SYSTEM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"A2DC49811AF8CC72\"}}, \"counters\": {\"crossProcess\": 5262, \"moduleLoad\": 222, \"netConnOut\": 1813, \"crossProcessOutOfGroup\": 5262, \"crossProcessOpenProcess\": 5262, \"dnsLookups\": 51}}, \"target\": {\"node\": {\"key\": {\"value\": \"E94742BA9CF1A186\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"23FF6C2F651EEA11\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\WINDOWS\\\\system32\\\\taskhostw.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"97096\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"fed4b4a753a9541389aa670c69e624be07569ccd\", \"sha256\": \"0322728dbce3a577c4a13b907ad7375d27e74880b63f7371384f67d19197a0ad\", \"md5\": \"564e4806ab18f93b93d551cd10c1598e\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"taskhostw.exe Install $(Arg0)\", \"fullPid\": {\"pid\": 15728, \"startTime\": {\"millisecondsSinceEpoch\": \"1631634711621\"}}, \"user\": {\"name\": \"SNS\\\\j.varinot\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6152\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"399C73C0494DC82C\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"92BFF1D465C6BF8D\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\WINDOWS\\\\system32\\\\svchost.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"57360\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS PUBLISHER\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"010db07461e45b41c886192df6fd425ba8d42d82\", \"sha256\": \"643ec58e82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7\", \"md5\": \"f586835082f632dc8d9404d83bc16316\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"C:\\\\WINDOWS\\\\system32\\\\svchost.exe -k netsvcs -p -s Schedule\", \"fullPid\": {\"pid\": 1928, \"startTime\": {\"millisecondsSinceEpoch\": \"1630919463114\"}}, \"user\": {\"name\": \"AUTORITE NT\\\\Syst\\u00e8me\", \"sid\": \"S-1-5-18\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"D382137395ABA2C4\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Host Process for Windows Services\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"integrityLevel\": \"SYSTEM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"4F9F0BD86D6CFE40\"}}, \"counters\": {\"modelChildProcess\": 1596, \"osChildProcess\": 1596, \"crossProcess\": 63, \"moduleLoad\": 81, \"crossProcessOutOfGroup\": 63, \"crossProcessOpenProcess\": 63}}, \"excluded\": \"E_FALSE\", \"name\": \"Host Process for Windows Tasks\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 7, \"integrityLevel\": \"MEDIUM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"AB55C980E679578F\"}}, \"counters\": {\"moduleLoad\": 44}}, \"desiredAccess\": 5240, \"relations\": \"PR_OTHER\"}",
        "process": {
            "command_line": "C:\\WINDOWS\\system32\\lsass.exe",
            "hash": {
                "md5": "15a556def233f112d127025ab51ac2d3",
                "sha1": "28f7fb54c7bcd9d6e71669ea5bddf72ea65311ce",
                "sha256": "362ab9743ff5d0f95831306a780fc3e418990f535013c80212dd85cb88ef7427"
            },
            "name": "Local Security Authority Process",
            "parent": {
                "command_line": "wininit.exe",
                "hash": {
                    "md5": "9ef51c8ad595c5e2a123c06ad39fccd7",
                    "sha1": "915ea28bdaa9a2230ce52080693d7f7e27620ed5",
                    "sha256": "268ca325c8f12e68b6728ff24d6536030aab6e05603d0179033b1e51d8476d86"
                },
                "name": "Windows Start-Up Application",
                "pid": 900,
                "working_directory": "Local"
            },
            "pid": 992,
            "start": "2021-09-06T09:11:02.523+00:00",
            "working_directory": "Local",
            "executable": "C:\\WINDOWS\\system32\\lsass.exe"
        },
        "related": {
            "hash": [
                "15a556def233f112d127025ab51ac2d3",
                "28f7fb54c7bcd9d6e71669ea5bddf72ea65311ce",
                "362ab9743ff5d0f95831306a780fc3e418990f535013c80212dd85cb88ef7427",
                "915ea28bdaa9a2230ce52080693d7f7e27620ed5",
                "268ca325c8f12e68b6728ff24d6536030aab6e05603d0179033b1e51d8476d86",
                "9ef51c8ad595c5e2a123c06ad39fccd7"
            ],
            "user": [
                "AUTORITE NT\\Syst\u00e8me"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "id": "S-1-5-18",
            "name": "AUTORITE NT\\Syst\u00e8me"
        }
    }
    	
	```


=== "event_dns.json"

    ```json
	
    {
        "event": {
            "start": "2021-08-09T13:33:30.404+00:00",
            "action": "dns"
        },
        "deepvisibility": {
            "event": {
                "type": "dns"
            },
            "true_context": {
                "key": "C20F3967ACBB2FE7"
            },
            "agent": {
                "seq_id": 35,
                "uuid": "4d311e18709146cba8797a22e3c20762",
                "trace_id": "BA1BE2835D6E4FF7B023C72DCE8B3829",
                "managment_url": "https://euce1-110-nfr.sentinelone.net"
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "dns": {
                "answers": {
                    "results": "type:  5 googlehosted.l.googleusercontent.com;142.250.179.65;"
                }
            },
            "process": {
                "family": "SYS_WIN32",
                "executable": {
                    "name": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "node": {
                        "key": "C8E88AA83F5B15B6"
                    },
                    "start": "2021-08-05T07:45:42.879+00:00",
                    "is_dir": "E_FALSE",
                    "size_bytes": "2442584",
                    "signature": {
                        "signed": {
                            "identity": "GOOGLE LLC"
                        }
                    }
                },
                "parent": {
                    "node": {
                        "key": "BAE25D38782A6941"
                    }
                },
                "counters": {
                    "module_load": 90,
                    "file_creation": 45,
                    "file_deletion": 19,
                    "file_modification": 101,
                    "net_conn_out": 31,
                    "dns_lookups": 35
                },
                "user": {
                    "sid": "S-1-5-21-1525252525-7987987987-1111111111-6174"
                },
                "interactive": "E_FALSE",
                "excluded": "E_FALSE",
                "root": "E_FALSE",
                "session_id": 11,
                "integrity_level": "MEDIUM",
                "is_wow64": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "true_context": {
                    "key": "C20F3967ACBB2FE7"
                },
                "node": {
                    "key": "87E0B0E05D9D6CC8"
                }
            }
        },
        "agent": {
            "version": "S1-WIN/4.6.14.304"
        },
        "host": {
            "name": "LAPTOP-COM13",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "process": {
            "name": "Google Chrome",
            "working_directory": "Local",
            "command_line": "\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\" --type=utility --utility-sub-type=network.mojom.NetworkService --field-trial-handle=1692,16822032697640791725,9639588106693567222,131072 --lang=fr --service-sandbox-type=none --mojo-platform-channel-handle=2056 /prefetch:8",
            "pid": 13796,
            "start": "2021-08-09T13:28:54.223+00:00",
            "executable": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        },
        "dns": {
            "question": {
                "name": "lh5.googleusercontent.com"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "user": [
                "CLIENT\\t.Naohisa"
            ]
        },
        "user": {
            "name": "CLIENT\\t.Naohisa",
            "id": "S-1-5-21-1525252525-7987987987-1111111111-6174"
        }
    }
    	
	```


=== "file_modification.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.7.1.240"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "trace_id": "01FFJC477DKY75XNH1KZPNVR44",
                "uuid": "f63008e522ce40c9afd4348634b5ab3b"
            },
            "event": {
                "type": "fileModification"
            },
            "file": {
                "location": "Local",
                "is_kernel_module": false
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "process": {
                "counters": {
                    "dns_lookups": 5131,
                    "file_creation": 15609,
                    "file_deletion": 10968,
                    "file_modification": 25519,
                    "module_load": 237,
                    "net_conn_out": 7312
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "node": {
                        "key": "05893E5943D0005C"
                    },
                    "signature": {
                        "signed": {
                            "identity": "GOOGLE LLC"
                        }
                    },
                    "size_bytes": "2465624",
                    "start": "2021-09-02T08:59:58.477+00:00"
                },
                "family": "SYS_WIN32",
                "integrity_level": "MEDIUM",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "B3B1945F1C32FBE0"
                },
                "parent": {
                    "node": {
                        "key": "0D7A69B0C2C26E73"
                    }
                },
                "root": "E_FALSE",
                "session_id": 1,
                "true_context": {
                    "key": "6B188EE5E8C5F24F"
                },
                "user": {
                    "sid": "S-1-5-21-3542462677-1213864171-2030164332-6187"
                }
            },
            "true_context": {
                "key": "6B188EE5E8C5F24F"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "start": "2021-09-14T14:41:46.789+00:00",
            "action": "fileModification"
        },
        "file": {
            "created": "2021-09-14T14:41:46.782+00:00",
            "path": "C:\\Users\\d.semren.SNS\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\TransportSecurity",
            "name": "TransportSecurity"
        },
        "host": {
            "name": "LAPTOP-TECH20",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"uuid\": \"f63008e522ce40c9afd4348634b5ab3b\", \"traceId\": \"01FFJC477DKY75XNH1KZPNVR44\", \"agentVersion\": \"S1-WIN/21.7.1.240\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-TECH20\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631630506789\"}, \"event_type\": \"fileModification\", \"trueContext\": {\"key\": {\"value\": \"6B188EE5E8C5F24F\"}}, \"source\": {\"node\": {\"key\": {\"value\": \"B3B1945F1C32FBE0\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"05893E5943D0005C\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"1630573198477\"}, \"path\": \"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"2465624\", \"signature\": {\"signed\": {\"identity\": \"GOOGLE LLC\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"a82705f4f5d1408f7c14d16a9cbe26c509422b29\", \"sha256\": \"07832d5f6344bd4d68376a6ca3c5baabb9cef7166a3752268e73fadffb07ddff\", \"md5\": \"a766188d75e570ea3f9b09fb9d82cb54\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"\\\"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\\\" --type=utility --utility-sub-type=network.mojom.NetworkService --field-trial-handle=1744,7600736140352570522,3112921143749416041,131072 --lang=fr --service-sandbox-type=none --mojo-platform-channel-handle=2092 /prefetch:8\", \"fullPid\": {\"pid\": 17924, \"startTime\": {\"millisecondsSinceEpoch\": \"1631516877934\"}}, \"user\": {\"name\": \"SNS\\\\d.semren\", \"sid\": \"S-1-5-21-3542462677-1213864171-2030164332-6187\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"0D7A69B0C2C26E73\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Google Chrome\", \"root\": \"E_FALSE\", \"subsystem\": \"SYS_WIN32\", \"sessionId\": 1, \"integrityLevel\": \"MEDIUM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"6B188EE5E8C5F24F\"}}, \"counters\": {\"moduleLoad\": 237, \"fileCreation\": 15609, \"fileDeletion\": 10968, \"fileModification\": 25519, \"netConnOut\": 7312, \"dnsLookups\": 5131}}, \"file\": {\"node\": {\"key\": {\"value\": \"11B30D7B6C017731\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"1631630506782\"}, \"path\": \"C:\\\\Users\\\\d.semren.SNS\\\\AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\TransportSecurity\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"hashes\": {}, \"fileLocation\": \"Local\"}, \"isKernelModule\": \"E_FALSE\", \"hashes\": {}, \"oldHashes\": {}}",
        "process": {
            "command_line": "\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\" --type=utility --utility-sub-type=network.mojom.NetworkService --field-trial-handle=1744,7600736140352570522,3112921143749416041,131072 --lang=fr --service-sandbox-type=none --mojo-platform-channel-handle=2092 /prefetch:8",
            "hash": {
                "md5": "a766188d75e570ea3f9b09fb9d82cb54",
                "sha1": "a82705f4f5d1408f7c14d16a9cbe26c509422b29",
                "sha256": "07832d5f6344bd4d68376a6ca3c5baabb9cef7166a3752268e73fadffb07ddff"
            },
            "name": "Google Chrome",
            "pid": 17924,
            "start": "2021-09-13T07:07:57.934+00:00",
            "working_directory": "Local",
            "executable": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        },
        "related": {
            "hash": [
                "a82705f4f5d1408f7c14d16a9cbe26c509422b29",
                "07832d5f6344bd4d68376a6ca3c5baabb9cef7166a3752268e73fadffb07ddff",
                "a766188d75e570ea3f9b09fb9d82cb54"
            ],
            "user": [
                "SNS\\d.semren"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "id": "S-1-5-21-3542462677-1213864171-2030164332-6187",
            "name": "SNS\\d.semren"
        }
    }
    	
	```


=== "reg_value_modified.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.5.7.370"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "seq_id": 133,
                "trace_id": "8D9114CB762D473FAA5189BD13762FB2",
                "uuid": "4d311e18709146cba8797a22e3c20762"
            },
            "event": {
                "type": "regValueModified"
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "process": {
                "counters": {
                    "model_child_process": 25,
                    "module_load": 87,
                    "os_child_process": 25
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\Windows\\System32\\svchost.exe",
                    "node": {
                        "key": "294CA423F5D3A1E5"
                    },
                    "signature": {
                        "signed": {
                            "identity": "MICROSOFT WINDOWS PUBLISHER"
                        }
                    },
                    "size_bytes": "57360",
                    "start": "18446732429235951616"
                },
                "family": "SYS_WIN32",
                "integrity_level": "SYSTEM",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "645A938883C36D21"
                },
                "parent": {
                    "node": {
                        "key": "DEF87C2AB48B84DC"
                    }
                },
                "root": "E_TRUE",
                "true_context": {
                    "key": "B3E0EF7ECFD0D296"
                },
                "user": {
                    "sid": "S-1-5-19"
                }
            },
            "registry": {
                "new": {
                    "value_type": "3"
                },
                "old": {
                    "data": {
                        "type": "REG_SZ",
                        "strings": [
                            "00C0F0FF"
                        ]
                    },
                    "value_type": "1"
                }
            },
            "true_context": {
                "key": "B3E0EF7ECFD0D296"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "regValueModified",
            "start": "2021-09-16T09:39:16.204+00:00"
        },
        "host": {
            "name": "LAPTOP-COM13",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"seqId\": 133, \"uuid\": \"4d311e18709146cba8797a22e3c20762\", \"traceId\": \"8D9114CB762D473FAA5189BD13762FB2\", \"agentVersion\": \"S1-WIN/21.5.7.370\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-COM13\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631785156204\"}, \"event_type\": \"regValueModified\", \"trueContext\": {\"key\": {\"value\": \"B3E0EF7ECFD0D296\"}}, \"regValue\": {\"key\": {}, \"path\": \"MACHINE\\\\SYSTEM\\\\ControlSet001\\\\Control\\\\Class\\\\{4d36e96c-e325-11ce-bfc1-08002be10318}\\\\0003\\\\GlobalSettings\\\\AnalogDigitalCapture\\\\Node000\\\\Chan001\"}, \"oldValueType\": 3, \"newValueType\": 3, \"source\": {\"node\": {\"key\": {\"value\": \"645A938883C36D21\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"294CA423F5D3A1E5\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"57360\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS PUBLISHER\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"010db07461e45b41c886192df6fd425ba8d42d82\", \"sha256\": \"643ec58e82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7\", \"md5\": \"f586835082f632dc8d9404d83bc16316\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"C:\\\\Windows\\\\System32\\\\svchost.exe -k LocalServiceNetworkRestricted -p\", \"fullPid\": {\"pid\": 3504, \"startTime\": {\"millisecondsSinceEpoch\": \"1631625850355\"}}, \"user\": {\"name\": \"AUTORITE NT\\\\SERVICE LOCAL\", \"sid\": \"S-1-5-19\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"DEF87C2AB48B84DC\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"Host Process for Windows Services\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"integrityLevel\": \"SYSTEM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"B3E0EF7ECFD0D296\"}}, \"counters\": {\"modelChildProcess\": 25, \"osChildProcess\": 25, \"moduleLoad\": 87}}, \"oldValueData\": \"00C0F0FF\", \"newValueData\": \"0040EEFF\"}",
        "process": {
            "command_line": "C:\\Windows\\System32\\svchost.exe -k LocalServiceNetworkRestricted -p",
            "executable": "C:\\Windows\\System32\\svchost.exe",
            "hash": {
                "md5": "f586835082f632dc8d9404d83bc16316",
                "sha1": "010db07461e45b41c886192df6fd425ba8d42d82",
                "sha256": "643ec58e82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7"
            },
            "name": "Host Process for Windows Services",
            "pid": 3504,
            "start": "2021-09-14T13:24:10.355+00:00",
            "working_directory": "Local"
        },
        "registry": {
            "data": {
                "bytes": "0040EEFF",
                "type": "REG_BINARY"
            },
            "path": "MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e96c-e325-11ce-bfc1-08002be10318}\\0003\\GlobalSettings\\AnalogDigitalCapture\\Node000\\Chan001",
            "value": "Chan001"
        },
        "related": {
            "hash": [
                "010db07461e45b41c886192df6fd425ba8d42d82",
                "f586835082f632dc8d9404d83bc16316",
                "643ec58e82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7"
            ],
            "user": [
                "AUTORITE NT\\SERVICE LOCAL"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "id": "S-1-5-19",
            "name": "AUTORITE NT\\SERVICE LOCAL"
        }
    }
    	
	```


=== "sched_task_update.json"

    ```json
	
    {
        "agent": {
            "version": "S1-WIN/21.5.7.370"
        },
        "deepvisibility": {
            "agent": {
                "managment_url": "https://euce1-110-nfr.sentinelone.net",
                "seq_id": 63,
                "trace_id": "CEBBC94D38B041B1B2DE01C315EB28F5",
                "uuid": "bcc4bf7a284441599707050e1d58a8dd"
            },
            "event": {
                "type": "schedTaskUpdate"
            },
            "host": {
                "os": {
                    "revision": "19042"
                }
            },
            "process": {
                "counters": {
                    "dns_lookups": 1,
                    "model_child_process": 1,
                    "module_load": 1158,
                    "net_conn_out": 7,
                    "os_child_process": 1
                },
                "excluded": "E_FALSE",
                "executable": {
                    "is_dir": "E_FALSE",
                    "name": "C:\\WINDOWS\\system32\\MoUsoCoreWorker.exe",
                    "node": {
                        "key": "99892497510C239E"
                    },
                    "signature": {
                        "signed": {
                            "identity": "MICROSOFT WINDOWS"
                        }
                    },
                    "size_bytes": "1614848",
                    "start": "18446732429235951616"
                },
                "family": "SYS_WIN32",
                "integrity_level": "SYSTEM",
                "interactive": "E_FALSE",
                "is_redirected_command_processor": "E_FALSE",
                "is_wow64": "E_FALSE",
                "node": {
                    "key": "38F2355042BA2367"
                },
                "parent": {
                    "node": {
                        "key": "B485A24CFF4A8D31"
                    }
                },
                "root": "E_TRUE",
                "true_context": {
                    "key": "4FE2F2ADB5655DDF"
                },
                "user": {
                    "sid": "S-1-5-18"
                }
            },
            "scheduled_task": {
                "name": "\\Microsoft\\Windows\\UpdateOrchestrator\\Schedule Maintenance Work"
            },
            "true_context": {
                "key": "4FE2F2ADB5655DDF"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "schedTaskUpdate",
            "start": "2021-09-14T15:51:48.620+00:00"
        },
        "host": {
            "name": "LAPTOP-TECH15",
            "os": {
                "family": "windows",
                "name": "Windows 10 Pro"
            },
            "type": "laptop"
        },
        "message": "{\"meta\": {\"seqId\": 63, \"uuid\": \"bcc4bf7a284441599707050e1d58a8dd\", \"traceId\": \"CEBBC94D38B041B1B2DE01C315EB28F5\", \"agentVersion\": \"S1-WIN/21.5.7.370\", \"osFamily\": \"windows\", \"osName\": \"Windows 10 Pro\", \"osRevision\": \"19042\", \"computerName\": \"LAPTOP-TECH15\", \"machineType\": \"laptop\", \"mgmtUrl\": \"https://euce1-110-nfr.sentinelone.net\"}, \"timestamp\": {\"millisecondsSinceEpoch\": \"1631634708620\"}, \"event_type\": \"schedTaskUpdate\", \"trueContext\": {\"key\": {\"value\": \"4FE2F2ADB5655DDF\"}}, \"taskName\": \"\\\\Microsoft\\\\Windows\\\\UpdateOrchestrator\\\\Schedule Maintenance Work\", \"source\": {\"node\": {\"key\": {\"value\": \"38F2355042BA2367\"}}, \"executable\": {\"node\": {\"key\": {\"value\": \"99892497510C239E\"}}, \"creationTime\": {\"millisecondsSinceEpoch\": \"18446732429235951616\"}, \"path\": \"C:\\\\WINDOWS\\\\system32\\\\MoUsoCoreWorker.exe\", \"owner\": {}, \"isDir\": \"E_FALSE\", \"sizeBytes\": \"1614848\", \"signature\": {\"signed\": {\"identity\": \"MICROSOFT WINDOWS\", \"valid\": {}}}, \"hashes\": {\"sha1\": \"a5a6716e38b06d44f4803b5167db2a0862b1d6bf\", \"sha256\": \"a250e2af9b662d6a81552178ac7514e81032c5a4b7031666f8e777f597ea5a9d\", \"md5\": \"475c5e07f8375dab6e5888301b1705e6\"}, \"fileLocation\": \"Local\"}, \"commandLine\": \"C:\\\\Windows\\\\System32\\\\mousocoreworker.exe -Embedding\", \"fullPid\": {\"pid\": 8588, \"startTime\": {\"millisecondsSinceEpoch\": \"1631289768083\"}}, \"user\": {\"name\": \"AUTORITE NT\\\\Syst\\u00e8me\", \"sid\": \"S-1-5-18\"}, \"interactive\": \"E_FALSE\", \"parent\": {\"node\": {\"key\": {\"value\": \"B485A24CFF4A8D31\"}}, \"fullPid\": {\"startTime\": {}}}, \"excluded\": \"E_FALSE\", \"name\": \"MoUSO Core Worker Process\", \"root\": \"E_TRUE\", \"subsystem\": \"SYS_WIN32\", \"integrityLevel\": \"SYSTEM\", \"isWow64\": \"E_FALSE\", \"isRedirectedCommandProcessor\": \"E_FALSE\", \"trueContext\": {\"key\": {\"value\": \"4FE2F2ADB5655DDF\"}}, \"counters\": {\"modelChildProcess\": 1, \"osChildProcess\": 1, \"moduleLoad\": 1158, \"netConnOut\": 7, \"dnsLookups\": 1}}}",
        "process": {
            "command_line": "C:\\Windows\\System32\\mousocoreworker.exe -Embedding",
            "hash": {
                "md5": "475c5e07f8375dab6e5888301b1705e6",
                "sha1": "a5a6716e38b06d44f4803b5167db2a0862b1d6bf",
                "sha256": "a250e2af9b662d6a81552178ac7514e81032c5a4b7031666f8e777f597ea5a9d"
            },
            "name": "MoUSO Core Worker Process",
            "pid": 8588,
            "start": "2021-09-10T16:02:48.083+00:00",
            "working_directory": "Local",
            "executable": "C:\\WINDOWS\\system32\\MoUsoCoreWorker.exe"
        },
        "related": {
            "hash": [
                "a5a6716e38b06d44f4803b5167db2a0862b1d6bf",
                "a250e2af9b662d6a81552178ac7514e81032c5a4b7031666f8e777f597ea5a9d",
                "475c5e07f8375dab6e5888301b1705e6"
            ],
            "user": [
                "AUTORITE NT\\Syst\u00e8me"
            ]
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d"
            }
        },
        "user": {
            "id": "S-1-5-18",
            "name": "AUTORITE NT\\Syst\u00e8me"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`agent.version` | `keyword` | Version of the agent. |
|`deepvisibility.agent.managment_url` | `keyword` | None |
|`deepvisibility.agent.seq_id` | `long` | None |
|`deepvisibility.agent.trace_id` | `keyword` | None |
|`deepvisibility.agent.uuid` | `keyword` | None |
|`deepvisibility.dns.answers.results` | `keyword` | None |
|`deepvisibility.event.type` | `keyword` | None |
|`deepvisibility.file.is_kernel_module` | `boolean` | None |
|`deepvisibility.file.location` | `keyword` | None |
|`deepvisibility.file.node.key` | `keyword` | None |
|`deepvisibility.host.os.revision` | `keyword` | None |
|`deepvisibility.indicator.category` | `keyword` | None |
|`deepvisibility.indicator.classification` | `keyword` | None |
|`deepvisibility.indicator.description` | `keyword` | None |
|`deepvisibility.indicator.id` | `keyword` | None |
|`deepvisibility.indicator.long_description` | `keyword` | None |
|`deepvisibility.indicator.metadata` | `keyword` | None |
|`deepvisibility.indicator.name` | `keyword` | None |
|`deepvisibility.indicator.tactics` | `object` | None |
|`deepvisibility.process.counters.cross_process` | `long` | None |
|`deepvisibility.process.counters.cross_process_dup_process_handle` | `long` | None |
|`deepvisibility.process.counters.cross_process_dup_thread_handle` | `long` | None |
|`deepvisibility.process.counters.dns_lookups` | `long` | None |
|`deepvisibility.process.counters.file_creation` | `long` | None |
|`deepvisibility.process.counters.file_deletion` | `long` | None |
|`deepvisibility.process.counters.file_modification` | `long` | None |
|`deepvisibility.process.counters.model_child_process` | `long` | None |
|`deepvisibility.process.counters.module_load` | `long` | None |
|`deepvisibility.process.counters.net_conn_out` | `long` | None |
|`deepvisibility.process.counters.os_child_process` | `long` | None |
|`deepvisibility.process.counters.registry_modification` | `long` | None |
|`deepvisibility.process.desired_access` | `long` | None |
|`deepvisibility.process.excluded` | `keyword` | None |
|`deepvisibility.process.executable.is_dir` | `keyword` | None |
|`deepvisibility.process.executable.name` | `keyword` | None |
|`deepvisibility.process.executable.node.key` | `keyword` | None |
|`deepvisibility.process.executable.signature.signed.identity` | `keyword` | None |
|`deepvisibility.process.executable.size_bytes` | `keyword` | None |
|`deepvisibility.process.executable.start` | `keyword` | None |
|`deepvisibility.process.family` | `keyword` | None |
|`deepvisibility.process.integrity_level` | `keyword` | None |
|`deepvisibility.process.interactive` | `keyword` | None |
|`deepvisibility.process.is_redirected_command_processor` | `keyword` | None |
|`deepvisibility.process.is_wow64` | `keyword` | None |
|`deepvisibility.process.node.key` | `keyword` | None |
|`deepvisibility.process.parent.counters.cross_process` | `long` | None |
|`deepvisibility.process.parent.counters.cross_process_dup_process_handle` | `long` | None |
|`deepvisibility.process.parent.counters.cross_process_dup_thread_handle` | `long` | None |
|`deepvisibility.process.parent.counters.dns_lookups` | `long` | None |
|`deepvisibility.process.parent.counters.file_creation` | `long` | None |
|`deepvisibility.process.parent.counters.file_deletion` | `long` | None |
|`deepvisibility.process.parent.counters.file_modification` | `long` | None |
|`deepvisibility.process.parent.counters.model_child_process` | `long` | None |
|`deepvisibility.process.parent.counters.module_load` | `long` | None |
|`deepvisibility.process.parent.counters.net_conn_out` | `long` | None |
|`deepvisibility.process.parent.counters.os_child_process` | `long` | None |
|`deepvisibility.process.parent.counters.registry_modification` | `long` | None |
|`deepvisibility.process.parent.excluded` | `keyword` | None |
|`deepvisibility.process.parent.executable.is_dir` | `keyword` | None |
|`deepvisibility.process.parent.executable.name` | `keyword` | None |
|`deepvisibility.process.parent.executable.node.key` | `keyword` | None |
|`deepvisibility.process.parent.executable.signature.signed.identity` | `keyword` | None |
|`deepvisibility.process.parent.executable.size_bytes` | `keyword` | None |
|`deepvisibility.process.parent.executable.start` | `keyword` | None |
|`deepvisibility.process.parent.family` | `keyword` | None |
|`deepvisibility.process.parent.integrity_level` | `keyword` | None |
|`deepvisibility.process.parent.interactive` | `keyword` | None |
|`deepvisibility.process.parent.is_redirected_command_processor` | `keyword` | None |
|`deepvisibility.process.parent.is_wow64` | `keyword` | None |
|`deepvisibility.process.parent.node.key` | `keyword` | None |
|`deepvisibility.process.parent.parent.node.key` | `keyword` | None |
|`deepvisibility.process.parent.root` | `keyword` | None |
|`deepvisibility.process.parent.session_id` | `long` | None |
|`deepvisibility.process.parent.true_context.key` | `keyword` | None |
|`deepvisibility.process.parent.user.sid` | `keyword` | None |
|`deepvisibility.process.relations` | `keyword` | None |
|`deepvisibility.process.root` | `keyword` | None |
|`deepvisibility.process.session_id` | `long` | None |
|`deepvisibility.process.target.command_line` | `keyword` | None |
|`deepvisibility.process.target.counters.cross_process` | `long` | None |
|`deepvisibility.process.target.counters.cross_process_dup_process_handle` | `long` | None |
|`deepvisibility.process.target.counters.cross_process_dup_thread_handle` | `long` | None |
|`deepvisibility.process.target.counters.dns_lookups` | `long` | None |
|`deepvisibility.process.target.counters.file_creation` | `long` | None |
|`deepvisibility.process.target.counters.file_deletion` | `long` | None |
|`deepvisibility.process.target.counters.file_modification` | `long` | None |
|`deepvisibility.process.target.counters.model_child_process` | `long` | None |
|`deepvisibility.process.target.counters.module_load` | `long` | None |
|`deepvisibility.process.target.counters.net_conn_out` | `long` | None |
|`deepvisibility.process.target.counters.os_child_process` | `long` | None |
|`deepvisibility.process.target.counters.registry_modification` | `long` | None |
|`deepvisibility.process.target.excluded` | `keyword` | None |
|`deepvisibility.process.target.executable` | `keyword` | None |
|`deepvisibility.process.target.executable.is_dir` | `keyword` | None |
|`deepvisibility.process.target.executable.name` | `keyword` | None |
|`deepvisibility.process.target.executable.node.key` | `keyword` | None |
|`deepvisibility.process.target.executable.signature.signed.identity` | `keyword` | None |
|`deepvisibility.process.target.executable.size_bytes` | `keyword` | None |
|`deepvisibility.process.target.executable.start` | `keyword` | None |
|`deepvisibility.process.target.family` | `keyword` | None |
|`deepvisibility.process.target.hash.md5` | `keyword` | None |
|`deepvisibility.process.target.hash.sha1` | `keyword` | None |
|`deepvisibility.process.target.hash.sha256` | `keyword` | None |
|`deepvisibility.process.target.integrity_level` | `keyword` | None |
|`deepvisibility.process.target.interactive` | `keyword` | None |
|`deepvisibility.process.target.is_redirected_command_processor` | `keyword` | None |
|`deepvisibility.process.target.is_wow64` | `keyword` | None |
|`deepvisibility.process.target.name` | `keyword` | None |
|`deepvisibility.process.target.node.key` | `keyword` | None |
|`deepvisibility.process.target.parent.node.key` | `keyword` | None |
|`deepvisibility.process.target.pid` | `long` | None |
|`deepvisibility.process.target.root` | `keyword` | None |
|`deepvisibility.process.target.session_id` | `long` | None |
|`deepvisibility.process.target.start` | `date` | None |
|`deepvisibility.process.target.true_context.key` | `keyword` | None |
|`deepvisibility.process.target.user.sid` | `keyword` | None |
|`deepvisibility.process.target.working_directory` | `keyword` | None |
|`deepvisibility.process.true_context.key` | `keyword` | None |
|`deepvisibility.process.user.sid` | `keyword` | None |
|`deepvisibility.registry.export_path` | `keyword` | None |
|`deepvisibility.registry.import_path` | `keyword` | None |
|`deepvisibility.registry.new.value_type` | `keyword` | None |
|`deepvisibility.registry.old.data.bytes` | `keyword` | None |
|`deepvisibility.registry.old.data.strings` | `keyword` | None |
|`deepvisibility.registry.old.key_name` | `keyword` | None |
|`deepvisibility.registry.old.value_type` | `keyword` | None |
|`deepvisibility.registry.security_information` | `long` | None |
|`deepvisibility.registry.value_type` | `keyword` | None |
|`deepvisibility.scheduled_task.name` | `keyword` | None |
|`deepvisibility.scheduled_task.trigger_type` | `long` | None |
|`deepvisibility.script.app_name` | `keyword` | None |
|`deepvisibility.true_context.key` | `keyword` | None |
|`destination.address` | `keyword` | Destination network address. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.port` | `long` | Port of the destination. |
|`dll.name` | `keyword` | Name of the library. |
|`dll.path` | `keyword` | Full file path of the library. |
|`dns.question.name` | `keyword` | The name being queried. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`file.code_signature.exists` | `boolean` | Boolean to capture if a signature is present. |
|`file.code_signature.subject_name` | `keyword` | Subject name of the code signer |
|`file.code_signature.valid` | `boolean` | Boolean to capture if the digital signature is verified against the binary content. |
|`file.created` | `date` | File creation time. |
|`file.extension` | `keyword` | File extension, excluding the leading dot. |
|`file.hash.md5` | `keyword` | MD5 hash. |
|`file.hash.sha1` | `keyword` | SHA1 hash. |
|`file.hash.sha256` | `keyword` | SHA256 hash. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.owner` | `keyword` | File owner's username. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`file.size` | `long` | File size in bytes. |
|`file.type` | `keyword` | File type (file, dir, or symlink). |
|`file.uid` | `keyword` | The user ID (UID) or security identifier (SID) of the file owner. |
|`host.name` | `keyword` | Name of the host. |
|`host.os.family` | `keyword` | OS family (such as redhat, debian, freebsd, windows). |
|`host.os.name` | `keyword` | Operating system name, without the version. |
|`host.type` | `keyword` | Type of host. |
|`http.request.method` | `keyword` | HTTP request method. |
|`network.direction` | `keyword` | Direction of the network traffic. |
|`process.code_signature.exists` | `boolean` | Boolean to capture if a signature is present. |
|`process.code_signature.subject_name` | `keyword` | Subject name of the code signer |
|`process.code_signature.valid` | `boolean` | Boolean to capture if the digital signature is verified against the binary content. |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.exit_code` | `long` | The exit code of the process. |
|`process.hash.md5` | `keyword` | MD5 hash. |
|`process.hash.sha1` | `keyword` | SHA1 hash. |
|`process.hash.sha256` | `keyword` | SHA256 hash. |
|`process.name` | `keyword` | Process name. |
|`process.parent.command_line` | `wildcard` | Full command line that started the process. |
|`process.parent.executable` | `keyword` | Absolute path to the process executable. |
|`process.parent.hash.md5` | `keyword` | MD5 hash. |
|`process.parent.hash.sha1` | `keyword` | SHA1 hash. |
|`process.parent.hash.sha256` | `keyword` | SHA256 hash. |
|`process.parent.name` | `keyword` | Process name. |
|`process.parent.pid` | `long` | Process id. |
|`process.parent.start` | `date` | The time the process started. |
|`process.parent.working_directory` | `keyword` | The working directory of the process. |
|`process.pid` | `long` | Process id. |
|`process.start` | `date` | The time the process started. |
|`process.working_directory` | `keyword` | The working directory of the process. |
|`registry.data.bytes` | `keyword` | Original bytes written with base64 encoding. |
|`registry.data.strings` | `wildcard` | List of strings representing what was written to the registry. |
|`registry.path` | `keyword` | Full path, including hive, key and value |
|`registry.value` | `keyword` | Name of the value written. |
|`source.address` | `keyword` | Source network address. |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.id` | `keyword` | Unique identifier of the user. |
|`user.name` | `keyword` | Short name or login of the user. |

