
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Authentication logs` | From system module, login dataset retrieve User logins, logouts, and system boots |
| `File monitoring` | From audit module, the file metric-set sends events when a file is changed (created, updated, or deleted) on disk. The events contain file metadata and hashes |
| `Process monitoring` | From system module, process dataset retrieve Started and stopped processes |
| `Process use of network` | From system module, socket dataset retrieve Opened and Closed sockets |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "example1.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"event\":{\"module\":\"system\",\"dataset\":\"process\",\"kind\":\"event\",\"category\":[\"process\"],\"type\":[\"end\"],\"action\":\"process_stopped\"},\"process\":{\"working_directory\":\"/my/directory\",\"start\":\"2021-01-01T00:01:01.000Z\",\"name\":\"smtp\",\"entity_id\":\"AZERTY123456789\",\"ppid\":1457,\"executable\":\"/usr/lib/postfix/sbin/smtp\",\"pid\":123123,\"args\":[\"smtp\",\"-t\",\"unix\",\"-u\",\"-c\"],\"hash\":{\"sha1\":\"53fe0c00019fb177e43c7ac214f466f01158384e\"}},\"message\":\"Process smtp (PID: 123123) by user postfix STOPPED\",\"user\":{\"effective\":{\"id\":\"999\",\"group\":{\"id\":\"222\"}},\"saved\":{\"id\":\"999\",\"group\":{\"id\":\"222\"}},\"name\":\"postfix\",\"id\":\"999\",\"group\":{\"id\":\"222\",\"name\":\"postfix\"}},\"service\":{\"type\":\"system\"},\"ecs\":{\"version\":\"1.9.0\"},\"host\":{\"name\":\"fame\"},\"agent\":{\"hostname\":\"fame\",\"ephemeral_id\":\"qsdfghjklm-1111-2222-3333-azertyuiop\",\"id\":\"wxcvbn-010101-121212-4444-azertyuiop\",\"name\":\"fame\",\"type\":\"auditbeat\",\"version\":\"7.13.0\"}}",
        "event": {
            "kind": "event",
            "module": "system",
            "category": [
                "process"
            ],
            "type": [
                "end"
            ],
            "action": "process_stopped"
        },
        "agent": {
            "hostname": "fame",
            "ephemeral_id": "qsdfghjklm-1111-2222-3333-azertyuiop",
            "id": "wxcvbn-010101-121212-4444-azertyuiop",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0"
        },
        "auditbeat": {
            "@metadata": {},
            "event": {},
            "process": {
                "hash": {}
            },
            "message": "Process smtp (PID: 123123) by user postfix STOPPED",
            "user": {
                "effective": {
                    "group": {}
                },
                "saved": {
                    "group": {}
                },
                "group": {}
            },
            "service": {},
            "ecs": {},
            "host": {},
            "agent": {}
        },
        "auditd": {
            "user": {
                "effective": {
                    "group": {}
                },
                "saved": {
                    "id": "999",
                    "group": {
                        "id": "222"
                    }
                },
                "group": {
                    "id": "222"
                }
            }
        },
        "host": {
            "name": "fame"
        },
        "log": {
            "hostname": "fame"
        },
        "process": {
            "working_directory": "/my/directory",
            "start": "2021-01-01T00:01:01.000Z",
            "name": "smtp",
            "entity_id": "AZERTY123456789",
            "executable": "/usr/lib/postfix/sbin/smtp",
            "pid": 123123,
            "args": [
                "smtp",
                "-t",
                "unix",
                "-u",
                "-c"
            ],
            "hash": {
                "sha1": "53fe0c00019fb177e43c7ac214f466f01158384e"
            },
            "parent": {
                "pid": 1457
            },
            "command_line": "smtp -t unix -u -c"
        },
        "service": {
            "type": "system"
        },
        "@timestamp": "2021-01-01T00:01:01.000Z",
        "user": {
            "effective": {
                "id": "999",
                "group": {
                    "id": "222"
                }
            },
            "saved": {
                "group": {
                    "id": "222"
                }
            },
            "name": "postfix",
            "id": "999",
            "group": {
                "id": "222",
                "name": "postfix"
            }
        },
        "related": {
            "hash": [
                "53fe0c00019fb177e43c7ac214f466f01158384e"
            ],
            "user": [
                "postfix"
            ]
        }
    }
    	
	```


=== "example10.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-11-09T17:39:26.389Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.15.1\"},\"process\":{\"ppid\":18470,\"title\":\"/opt/google/chrome/chrome --type=zygote --enable-crashpad --crashpad-handler-pid=18479 --enable-crash-reporter=, --change-stack-\",\"name\":\"chrome\",\"executable\":\"/opt/google/chrome/chrome\",\"working_directory\":\"/home/housetodd\",\"pid\":18488},\"auditd\":{\"session\":\"3\",\"summary\":{\"actor\":{\"primary\":\"housetodd\",\"secondary\":\"housetodd\"},\"object\":{\"primary\":\"/proc/1/oom_score_adj\",\"type\":\"file\"},\"how\":\"/opt/google/chrome/chrome\"},\"paths\":[{\"cap_fe\":\"0\",\"cap_fver\":\"0\",\"inode\":\"16064\",\"name\":\"/proc/1/\",\"ogid\":\"0\",\"ouid\":\"0\",\"rdev\":\"00:00\",\"cap_fi\":\"0000000000000000\",\"cap_fp\":\"0000000000000000\",\"dev\":\"00:04\",\"item\":\"0\",\"mode\":\"040555\",\"nametype\":\"PARENT\"},{\"nametype\":\"NORMAL\",\"ogid\":\"0\",\"ouid\":\"0\",\"cap_fe\":\"0\",\"dev\":\"00:04\",\"item\":\"1\",\"mode\":\"0100644\",\"name\":\"/proc/1/oom_score_adj\",\"rdev\":\"00:00\",\"cap_fi\":\"0000000000000000\",\"cap_fp\":\"0000000000000000\",\"cap_fver\":\"0\",\"inode\":\"25973\"}],\"message_type\":\"syscall\",\"sequence\":9052,\"result\":\"fail\",\"data\":{\"tty\":\"(none)\",\"exit\":\"EACCES\",\"a0\":\"7ffc1bfcdfa0\",\"a3\":\"7ffc1bfcde00\",\"a2\":\"55881de610b8\",\"a1\":\"1b6\",\"arch\":\"x86_64\",\"syscall\":\"creat\"}},\"event\":{\"module\":\"auditd\",\"category\":[\"file\"],\"action\":\"opened-file\",\"outcome\":\"failure\",\"kind\":\"event\",\"type\":[\"creation\"]},\"user\":{\"filesystem\":{\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"group\":{\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"name\":\"housetodd\"},\"name\":\"housetodd\"},\"name\":\"housetodd\",\"audit\":{\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"name\":\"housetodd\"},\"saved\":{\"group\":{\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"name\":\"housetodd\"},\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"name\":\"housetodd\"},\"group\":{\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"name\":\"housetodd\"},\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\"},\"host\":{\"name\":\"xps-housetodd\",\"ip\":[\"144.1.237.149\"],\"mac\":[\"22:69:ae:27:fe:66\"],\"hostname\":\"xps-housetodd\",\"architecture\":\"x86_64\",\"os\":{\"family\":\"debian\",\"name\":\"Ubuntu\",\"kernel\":\"4.15.0-161-generic\",\"codename\":\"bionic\",\"type\":\"linux\",\"platform\":\"ubuntu\",\"version\":\"18.04.6 LTS (Bionic Beaver)\"},\"id\":\"7dd912136af040e4a6ea4f683010b824\",\"containerized\":false},\"file\":{\"gid\":\"0\",\"owner\":\"housetodd\",\"group\":\"housetodd\",\"path\":\"/proc/1/oom_score_adj\",\"device\":\"00:00\",\"inode\":\"25973\",\"mode\":\"0644\",\"uid\":\"0\"},\"tags\":[\"access\"],\"service\":{\"type\":\"auditd\"},\"ecs\":{\"version\":\"1.11.0\"},\"agent\":{\"version\":\"7.15.1\",\"hostname\":\"xps-housetodd\",\"ephemeral_id\":\"f1ac5b09-4f0c-42cf-b9f7-f854eeae073a\",\"id\":\"e9872892-b999-4ad5-83da-d6ec9dbc1f81\",\"name\":\"xps-housetodd\",\"type\":\"auditbeat\"}}",
        "event": {
            "kind": "event",
            "module": "auditd",
            "category": [
                "file"
            ],
            "type": [
                "creation"
            ],
            "action": "opened-file"
        },
        "agent": {
            "version": "7.15.1",
            "hostname": "xps-housetodd",
            "ephemeral_id": "f1ac5b09-4f0c-42cf-b9f7-f854eeae073a",
            "id": "e9872892-b999-4ad5-83da-d6ec9dbc1f81",
            "name": "xps-housetodd",
            "type": "auditbeat"
        },
        "auditbeat": {
            "@metadata": {},
            "process": {},
            "auditd": {
                "summary": {
                    "actor": {},
                    "object": {}
                },
                "paths": [
                    {},
                    {}
                ],
                "data": {}
            },
            "event": {},
            "user": {
                "filesystem": {
                    "group": {}
                },
                "audit": {},
                "saved": {
                    "group": {}
                },
                "group": {}
            },
            "host": {
                "os": {}
            },
            "file": {},
            "tags": [
                "access"
            ],
            "service": {},
            "ecs": {},
            "agent": {}
        },
        "auditd": {
            "session": "3",
            "summary": {
                "actor": {
                    "primary": "housetodd",
                    "secondary": "housetodd"
                },
                "object": {
                    "primary": "/proc/1/oom_score_adj",
                    "type": "file"
                },
                "how": "/opt/google/chrome/chrome"
            },
            "paths": [
                {
                    "cap_fe": "0",
                    "cap_fver": "0",
                    "inode": "16064",
                    "name": "/proc/1/",
                    "ogid": "0",
                    "ouid": "0",
                    "rdev": "00:00",
                    "cap_fi": "0000000000000000",
                    "cap_fp": "0000000000000000",
                    "dev": "00:04",
                    "item": "0",
                    "mode": "040555",
                    "nametype": "PARENT"
                },
                {
                    "nametype": "NORMAL",
                    "ogid": "0",
                    "ouid": "0",
                    "cap_fe": "0",
                    "dev": "00:04",
                    "item": "1",
                    "mode": "0100644",
                    "name": "/proc/1/oom_score_adj",
                    "rdev": "00:00",
                    "cap_fi": "0000000000000000",
                    "cap_fp": "0000000000000000",
                    "cap_fver": "0",
                    "inode": "25973"
                }
            ],
            "message_type": "syscall",
            "sequence": 9052,
            "result": "fail",
            "data": {
                "tty": "(none)",
                "exit": "EACCES",
                "a0": "7ffc1bfcdfa0",
                "a3": "7ffc1bfcde00",
                "a2": "55881de610b8",
                "a1": "1b6",
                "arch": "x86_64",
                "syscall": "creat"
            },
            "user": {
                "filesystem": {
                    "group": {}
                },
                "audit": {},
                "saved": {
                    "group": {
                        "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430",
                        "name": "housetodd"
                    },
                    "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430",
                    "name": "housetodd"
                },
                "group": {
                    "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430"
                }
            }
        },
        "file": {
            "gid": "0",
            "owner": "housetodd",
            "group": "housetodd",
            "path": "/proc/1/oom_score_adj",
            "device": "00:00",
            "inode": "25973",
            "mode": "0644",
            "uid": "0"
        },
        "host": {
            "name": "xps-housetodd",
            "ip": [
                "144.1.237.149"
            ],
            "mac": [
                "22:69:ae:27:fe:66"
            ],
            "hostname": "xps-housetodd",
            "architecture": "x86_64",
            "os": {
                "family": "debian",
                "name": "Ubuntu",
                "kernel": "4.15.0-161-generic",
                "codename": "bionic",
                "type": "linux",
                "platform": "ubuntu",
                "version": "18.04.6 LTS (Bionic Beaver)"
            },
            "id": "7dd912136af040e4a6ea4f683010b824",
            "containerized": false
        },
        "log": {
            "hostname": "xps-housetodd"
        },
        "process": {
            "title": "/opt/google/chrome/chrome --type=zygote --enable-crashpad --crashpad-handler-pid=18479 --enable-crash-reporter=, --change-stack-",
            "name": "chrome",
            "executable": "/opt/google/chrome/chrome",
            "working_directory": "/home/housetodd",
            "pid": 18488,
            "parent": {
                "pid": 18470
            }
        },
        "service": {
            "type": "auditd"
        },
        "@timestamp": "2021-11-09T17:39:26.389Z",
        "user": {
            "filesystem": {
                "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430",
                "group": {
                    "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430",
                    "name": "housetodd"
                },
                "name": "housetodd"
            },
            "name": "housetodd",
            "audit": {
                "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430",
                "name": "housetodd"
            },
            "saved": {
                "group": {
                    "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430"
                }
            },
            "group": {
                "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430",
                "name": "housetodd"
            },
            "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430"
        },
        "related": {
            "user": [
                "housetodd"
            ],
            "ip": [
                "144.1.237.149"
            ],
            "hosts": [
                "xps-housetodd"
            ]
        }
    }
    	
	```


=== "example11.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-11-09T19:07:37.325Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.15.1\"},\"event\":{\"outcome\":\"unknown\",\"kind\":\"event\",\"type\":[\"info\"],\"module\":\"auditd\",\"category\":[\"file\"],\"action\":\"violated-seccomp-policy\"},\"user\":{\"id\":\"56d2c11c-9371-4617-bac3-2c18e86042c6\",\"audit\":{\"id\":\"56d2c11c-9371-4617-bac3-2c18e86042c6\",\"name\":\"UWWL21LVdEVmqrbT\"},\"group\":{\"id\":\"56d2c11c-9371-4617-bac3-2c18e86042c6\",\"name\":\"UWWL21LVdEVmqrbT\"},\"name\":\"UWWL21LVdEVmqrbT\"},\"process\":{\"name\":\"ThreadPoolSingl\",\"executable\":\"/opt/google/chrome/chrome\",\"pid\":2720},\"host\":{\"mac\":[\"0c:5d:c0:dc:1f:3f\"],\"hostname\":\"xps-UWWL21LVdEVmqrbT\",\"architecture\":\"x86_64\",\"os\":{\"family\":\"debian\",\"name\":\"Ubuntu\",\"kernel\":\"4.15.0-161-generic\",\"codename\":\"bionic\",\"type\":\"linux\",\"platform\":\"ubuntu\",\"version\":\"18.04.6 LTS (Bionic Beaver)\"},\"id\":\"7dd912136af040e4a6ea4f683010b824\",\"containerized\":false,\"ip\":[\"43.161.42.208\"],\"name\":\"xps-UWWL21LVdEVmqrbT\"},\"agent\":{\"id\":\"e9872892-b999-4ad5-83da-d6ec9dbc1f81\",\"name\":\"xps-UWWL21LVdEVmqrbT\",\"type\":\"auditbeat\",\"version\":\"7.15.1\",\"hostname\":\"xps-UWWL21LVdEVmqrbT\",\"ephemeral_id\":\"f1ac5b09-4f0c-42cf-b9f7-f854eeae073a\"},\"ecs\":{\"version\":\"1.11.0\"},\"auditd\":{\"session\":\"2\",\"summary\":{\"how\":\"/opt/google/chrome/chrome\",\"actor\":{\"primary\":\"UWWL21LVdEVmqrbT\",\"secondary\":\"UWWL21LVdEVmqrbT\"},\"object\":{\"primary\":\"stat\",\"type\":\"process\"}},\"message_type\":\"seccomp\",\"sequence\":12522,\"result\":\"unknown\",\"data\":{\"code\":\"0x50000\",\"syscall\":\"stat\",\"compat\":\"0\",\"ip\":\"0x7fe0a0df1845\",\"arch\":\"x86_64\",\"sig\":\"0\"}},\"service\":{\"type\":\"auditd\"}}",
        "event": {
            "kind": "event",
            "module": "auditd",
            "category": [
                "file"
            ],
            "type": [
                "info"
            ],
            "action": "violated-seccomp-policy"
        },
        "agent": {
            "id": "e9872892-b999-4ad5-83da-d6ec9dbc1f81",
            "name": "xps-UWWL21LVdEVmqrbT",
            "type": "auditbeat",
            "version": "7.15.1",
            "hostname": "xps-UWWL21LVdEVmqrbT",
            "ephemeral_id": "f1ac5b09-4f0c-42cf-b9f7-f854eeae073a"
        },
        "auditbeat": {
            "@metadata": {},
            "event": {},
            "user": {
                "audit": {},
                "group": {}
            },
            "process": {},
            "host": {
                "os": {}
            },
            "agent": {},
            "ecs": {},
            "auditd": {
                "summary": {
                    "actor": {},
                    "object": {}
                },
                "data": {}
            },
            "service": {}
        },
        "auditd": {
            "session": "2",
            "summary": {
                "how": "/opt/google/chrome/chrome",
                "actor": {
                    "primary": "UWWL21LVdEVmqrbT",
                    "secondary": "UWWL21LVdEVmqrbT"
                },
                "object": {
                    "primary": "stat",
                    "type": "process"
                }
            },
            "message_type": "seccomp",
            "sequence": 12522,
            "result": "unknown",
            "data": {
                "code": "0x50000",
                "syscall": "stat",
                "compat": "0",
                "ip": "0x7fe0a0df1845",
                "arch": "x86_64",
                "sig": "0"
            },
            "user": {
                "audit": {},
                "group": {
                    "id": "56d2c11c-9371-4617-bac3-2c18e86042c6"
                }
            }
        },
        "host": {
            "mac": [
                "0c:5d:c0:dc:1f:3f"
            ],
            "hostname": "xps-UWWL21LVdEVmqrbT",
            "architecture": "x86_64",
            "os": {
                "family": "debian",
                "name": "Ubuntu",
                "kernel": "4.15.0-161-generic",
                "codename": "bionic",
                "type": "linux",
                "platform": "ubuntu",
                "version": "18.04.6 LTS (Bionic Beaver)"
            },
            "id": "7dd912136af040e4a6ea4f683010b824",
            "containerized": false,
            "ip": [
                "43.161.42.208"
            ],
            "name": "xps-UWWL21LVdEVmqrbT"
        },
        "log": {
            "hostname": "xps-UWWL21LVdEVmqrbT"
        },
        "process": {
            "name": "ThreadPoolSingl",
            "executable": "/opt/google/chrome/chrome",
            "pid": 2720
        },
        "service": {
            "type": "auditd"
        },
        "@timestamp": "2021-11-09T19:07:37.325Z",
        "user": {
            "id": "56d2c11c-9371-4617-bac3-2c18e86042c6",
            "audit": {
                "id": "56d2c11c-9371-4617-bac3-2c18e86042c6",
                "name": "UWWL21LVdEVmqrbT"
            },
            "group": {
                "id": "56d2c11c-9371-4617-bac3-2c18e86042c6",
                "name": "UWWL21LVdEVmqrbT"
            },
            "name": "UWWL21LVdEVmqrbT"
        },
        "related": {
            "ip": [
                "43.161.42.208"
            ],
            "hosts": [
                "xps-UWWL21LVdEVmqrbT"
            ],
            "user": [
                "UWWL21LVdEVmqrbT"
            ]
        }
    }
    	
	```


=== "example12.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-11-09T18:35:01.754Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.15.1\"},\"related\":{\"user\":[\"root\"]},\"service\":{\"type\":\"auditd\"},\"event\":{\"module\":\"auditd\",\"category\":[\"authentication\"],\"action\":\"changed-login-id-to\",\"outcome\":\"success\",\"kind\":\"event\",\"type\":[\"start\"]},\"user\":{\"audit\":{\"id\":\"0\",\"name\":\"root\"},\"effective\":{\"id\":\"0\",\"name\":\"root\"}},\"ecs\":{\"version\":\"1.11.0\"},\"host\":{\"containerized\":false,\"ip\":[\"66.253.230.251\"],\"mac\":[\"5e:55:38:73:40:a4\"],\"hostname\":\"web-65\",\"architecture\":\"x86_64\",\"os\":{\"codename\":\"bionic\",\"type\":\"linux\",\"platform\":\"ubuntu\",\"version\":\"18.04.6 LTS (Bionic Beaver)\",\"family\":\"debian\",\"name\":\"Ubuntu\",\"kernel\":\"4.15.0-161-generic\"},\"name\":\"web-65\",\"id\":\"7dd912136af040e4a6ea4f683010b824\"},\"agent\":{\"ephemeral_id\":\"f1ac5b09-4f0c-42cf-b9f7-f854eeae073a\",\"id\":\"e9872892-b999-4ad5-83da-d6ec9dbc1f81\",\"name\":\"web-65\",\"type\":\"auditbeat\",\"version\":\"7.15.1\",\"hostname\":\"web-65\"},\"process\":{\"pid\":20899},\"auditd\":{\"data\":{\"tty\":\"(none)\",\"old-ses\":\"4294967295\"},\"session\":\"436\",\"summary\":{\"actor\":{\"primary\":\"unset\",\"secondary\":\"root\"},\"object\":{\"primary\":\"0\",\"type\":\"user-session\"}},\"message_type\":\"login\",\"sequence\":11578,\"result\":\"success\"}}",
        "event": {
            "kind": "event",
            "module": "auditd",
            "category": [
                "authentication"
            ],
            "type": [
                "start"
            ],
            "action": "changed-login-id-to"
        },
        "agent": {
            "ephemeral_id": "f1ac5b09-4f0c-42cf-b9f7-f854eeae073a",
            "id": "e9872892-b999-4ad5-83da-d6ec9dbc1f81",
            "name": "web-65",
            "type": "auditbeat",
            "version": "7.15.1",
            "hostname": "web-65"
        },
        "auditbeat": {
            "@metadata": {},
            "related": {},
            "service": {},
            "event": {},
            "user": {
                "audit": {},
                "effective": {}
            },
            "ecs": {},
            "host": {
                "os": {}
            },
            "agent": {},
            "process": {},
            "auditd": {
                "data": {},
                "summary": {
                    "actor": {},
                    "object": {}
                }
            }
        },
        "auditd": {
            "data": {
                "tty": "(none)",
                "old-ses": "4294967295"
            },
            "session": "436",
            "summary": {
                "actor": {
                    "primary": "unset",
                    "secondary": "root"
                },
                "object": {
                    "primary": "0",
                    "type": "user-session"
                }
            },
            "message_type": "login",
            "sequence": 11578,
            "result": "success",
            "user": {
                "audit": {},
                "effective": {}
            }
        },
        "host": {
            "containerized": false,
            "ip": [
                "66.253.230.251"
            ],
            "mac": [
                "5e:55:38:73:40:a4"
            ],
            "hostname": "web-65",
            "architecture": "x86_64",
            "os": {
                "codename": "bionic",
                "type": "linux",
                "platform": "ubuntu",
                "version": "18.04.6 LTS (Bionic Beaver)",
                "family": "debian",
                "name": "Ubuntu",
                "kernel": "4.15.0-161-generic"
            },
            "name": "web-65",
            "id": "7dd912136af040e4a6ea4f683010b824"
        },
        "log": {
            "hostname": "web-65"
        },
        "process": {
            "pid": 20899
        },
        "related": {
            "ip": [
                "66.253.230.251"
            ],
            "hosts": [
                "web-65"
            ]
        },
        "service": {
            "type": "auditd"
        },
        "@timestamp": "2021-11-09T18:35:01.754Z",
        "user": {
            "audit": {
                "id": "0",
                "name": "root"
            },
            "effective": {
                "id": "0",
                "name": "root"
            }
        }
    }
    	
	```


=== "example13.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-11-09T19:02:33.866Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.15.1\"},\"event\":{\"kind\":\"event\",\"type\":[\"start\"],\"module\":\"auditd\",\"category\":[\"process\"],\"action\":\"started-service\",\"outcome\":\"success\"},\"user\":{\"id\":\"16bb03ba-2e90-4c98-a5c8-c3d8b8b52c1e\",\"name\":\"X9PzJKityWAFaA5i\"},\"process\":{\"pid\":1,\"name\":\"systemd\",\"executable\":\"/lib/systemd/systemd\"},\"auditd\":{\"result\":\"success\",\"data\":{\"unit\":\"anacron\"},\"summary\":{\"how\":\"/lib/systemd/systemd\",\"actor\":{\"primary\":\"unset\",\"secondary\":\"X9PzJKityWAFaA5i\"},\"object\":{\"primary\":\"anacron\",\"type\":\"service\"}},\"message_type\":\"service_start\",\"sequence\":12295},\"service\":{\"type\":\"auditd\"},\"ecs\":{\"version\":\"1.11.16bb03ba-2e90-4c98-a5c8-c3d8b8b52c1e\"},\"host\":{\"hostname\":\"LCPmbaxBgGyJj8VH\",\"architecture\":\"x86_64\",\"os\":{\"name\":\"Ubuntu\",\"kernel\":\"4.15.0-161-generic\",\"codename\":\"bionic\",\"type\":\"linux\",\"platform\":\"ubuntu\",\"version\":\"18.04.6 LTS (Bionic Beaver)\",\"family\":\"debian\"},\"name\":\"LCPmbaxBgGyJj8VH\",\"id\":\"7dd912136af040e4a6ea4f683010b824\",\"containerized\":false,\"ip\":[\"87.138.107.154\"],\"mac\":[\"09:d0:5f:99:43:f6\"]},\"agent\":{\"hostname\":\"LCPmbaxBgGyJj8VH\",\"ephemeral_id\":\"f1ac5b09-4f0c-42cf-b9f7-f854eeae073a\",\"id\":\"e9872892-b999-4ad5-83da-d6ec9dbc1f81\",\"name\":\"LCPmbaxBgGyJj8VH\",\"type\":\"auditbeat\",\"version\":\"7.15.1\"}}",
        "event": {
            "kind": "event",
            "module": "auditd",
            "category": [
                "process"
            ],
            "type": [
                "start"
            ],
            "action": "started-service"
        },
        "agent": {
            "hostname": "LCPmbaxBgGyJj8VH",
            "ephemeral_id": "f1ac5b09-4f0c-42cf-b9f7-f854eeae073a",
            "id": "e9872892-b999-4ad5-83da-d6ec9dbc1f81",
            "name": "LCPmbaxBgGyJj8VH",
            "type": "auditbeat",
            "version": "7.15.1"
        },
        "auditbeat": {
            "@metadata": {},
            "event": {},
            "user": {},
            "process": {},
            "auditd": {
                "data": {},
                "summary": {
                    "actor": {},
                    "object": {}
                }
            },
            "service": {},
            "ecs": {},
            "host": {
                "os": {}
            },
            "agent": {}
        },
        "auditd": {
            "result": "success",
            "data": {
                "unit": "anacron"
            },
            "summary": {
                "how": "/lib/systemd/systemd",
                "actor": {
                    "primary": "unset",
                    "secondary": "X9PzJKityWAFaA5i"
                },
                "object": {
                    "primary": "anacron",
                    "type": "service"
                }
            },
            "message_type": "service_start",
            "sequence": 12295,
            "user": {}
        },
        "host": {
            "hostname": "LCPmbaxBgGyJj8VH",
            "architecture": "x86_64",
            "os": {
                "name": "Ubuntu",
                "kernel": "4.15.0-161-generic",
                "codename": "bionic",
                "type": "linux",
                "platform": "ubuntu",
                "version": "18.04.6 LTS (Bionic Beaver)",
                "family": "debian"
            },
            "name": "LCPmbaxBgGyJj8VH",
            "id": "7dd912136af040e4a6ea4f683010b824",
            "containerized": false,
            "ip": [
                "87.138.107.154"
            ],
            "mac": [
                "09:d0:5f:99:43:f6"
            ]
        },
        "log": {
            "hostname": "LCPmbaxBgGyJj8VH"
        },
        "process": {
            "pid": 1,
            "name": "systemd",
            "executable": "/lib/systemd/systemd"
        },
        "service": {
            "type": "auditd"
        },
        "@timestamp": "2021-11-09T19:02:33.866Z",
        "user": {
            "id": "16bb03ba-2e90-4c98-a5c8-c3d8b8b52c1e",
            "name": "X9PzJKityWAFaA5i"
        },
        "related": {
            "ip": [
                "87.138.107.154"
            ],
            "hosts": [
                "LCPmbaxBgGyJj8VH"
            ],
            "user": [
                "X9PzJKityWAFaA5i"
            ]
        }
    }
    	
	```


=== "example2.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"message\":\"Process containerd (PID: 1197) by user root is RUNNING\",\"user\":{\"group\":{\"name\":\"root\",\"id\":\"0\"},\"effective\":{\"id\":\"0\",\"group\":{\"id\":\"0\"}},\"saved\":{\"id\":\"0\",\"group\":{\"id\":\"0\"}},\"name\":\"root\",\"id\":\"0\"},\"ecs\":{\"version\":\"1.9.0\"},\"host\":{\"name\":\"fame\"},\"agent\":{\"hostname\":\"fame\",\"ephemeral_id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"name\":\"fame\",\"type\":\"auditbeat\",\"version\":\"7.13.0\"},\"service\":{\"type\":\"system\"},\"event\":{\"action\":\"existing_process\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"module\":\"system\",\"dataset\":\"process\",\"kind\":\"state\",\"category\":[\"process\"],\"type\":[\"info\"]},\"process\":{\"args\":[\"containerd\"],\"pid\":1197,\"ppid\":1,\"working_directory\":\"/\",\"entity_id\":\"AZERTYqsdfghjklm\",\"name\":\"containerd\",\"executable\":\"/usr/bin/containerd\",\"start\":\"2021-01-01T00:01:01.000Z\",\"hash\":{\"sha1\":\"azertyuiop1234567890\"}, \"command_line\": \"/usr/bin/containerd\"}}",
        "event": {
            "kind": "state",
            "module": "system",
            "category": [
                "process"
            ],
            "type": [
                "info"
            ],
            "action": "existing_process"
        },
        "agent": {
            "hostname": "fame",
            "ephemeral_id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0"
        },
        "auditbeat": {
            "@metadata": {},
            "message": "Process containerd (PID: 1197) by user root is RUNNING",
            "user": {
                "group": {},
                "effective": {
                    "group": {}
                },
                "saved": {
                    "group": {}
                }
            },
            "ecs": {},
            "host": {},
            "agent": {},
            "service": {},
            "event": {},
            "process": {
                "hash": {}
            }
        },
        "auditd": {
            "user": {
                "group": {
                    "id": "0"
                },
                "effective": {
                    "group": {}
                },
                "saved": {
                    "id": "0",
                    "group": {
                        "id": "0"
                    }
                }
            }
        },
        "host": {
            "name": "fame"
        },
        "log": {
            "hostname": "fame"
        },
        "process": {
            "args": [
                "containerd"
            ],
            "pid": 1197,
            "working_directory": "/",
            "entity_id": "AZERTYqsdfghjklm",
            "name": "containerd",
            "executable": "/usr/bin/containerd",
            "start": "2021-01-01T00:01:01.000Z",
            "hash": {
                "sha1": "azertyuiop1234567890"
            },
            "command_line": "/usr/bin/containerd",
            "parent": {
                "pid": 1
            }
        },
        "service": {
            "type": "system"
        },
        "@timestamp": "2021-01-01T00:01:01.000Z",
        "user": {
            "group": {
                "name": "root",
                "id": "0"
            },
            "effective": {
                "id": "0",
                "group": {
                    "id": "0"
                }
            },
            "saved": {
                "group": {
                    "id": "0"
                }
            },
            "name": "root",
            "id": "0"
        },
        "related": {
            "hash": [
                "azertyuiop1234567890"
            ],
            "user": [
                "root"
            ]
        }
    }
    	
	```


=== "example3.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"message\":\"Process unattended-upgr (PID: 1195) by user root is RUNNING\",\"user\":{\"name\":\"root\",\"id\":\"0\",\"group\":{\"id\":\"0\",\"name\":\"root\"},\"effective\":{\"group\":{\"id\":\"0\"},\"id\":\"0\"},\"saved\":{\"id\":\"0\",\"group\":{\"id\":\"0\"}}},\"service\":{\"type\":\"system\"},\"event\":{\"type\":[\"info\"],\"action\":\"existing_process\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"module\":\"system\",\"dataset\":\"process\",\"kind\":\"state\",\"category\":[\"process\"]},\"process\":{\"args\":[\"/usr/bin/python3\",\"/usr/share/unattended-upgrades/unattended-upgrade-shutdown\",\"--wait-for-signal\"],\"start\":\"2021-01-01T00:01:01.000Z\",\"hash\":{\"sha1\":\"azertyuiop1234567890\"},\"name\":\"unattended-upgr\",\"entity_id\":\"rvSkGilnHCy6yuIZ\",\"pid\":1195,\"ppid\":1,\"executable\":\"/usr/bin/python3.8\",\"working_directory\":\"/\"},\"ecs\":{\"version\":\"1.9.0\"},\"host\":{\"name\":\"fame\"},\"agent\":{\"version\":\"7.13.0\",\"hostname\":\"fame\",\"ephemeral_id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"name\":\"fame\",\"type\":\"auditbeat\"}}",
        "event": {
            "kind": "state",
            "module": "system",
            "category": [
                "process"
            ],
            "type": [
                "info"
            ],
            "action": "existing_process"
        },
        "agent": {
            "version": "7.13.0",
            "hostname": "fame",
            "ephemeral_id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "name": "fame",
            "type": "auditbeat"
        },
        "auditbeat": {
            "@metadata": {},
            "message": "Process unattended-upgr (PID: 1195) by user root is RUNNING",
            "user": {
                "group": {},
                "effective": {
                    "group": {}
                },
                "saved": {
                    "group": {}
                }
            },
            "service": {},
            "event": {},
            "process": {
                "hash": {}
            },
            "ecs": {},
            "host": {},
            "agent": {}
        },
        "auditd": {
            "user": {
                "group": {
                    "id": "0"
                },
                "effective": {
                    "group": {}
                },
                "saved": {
                    "id": "0",
                    "group": {
                        "id": "0"
                    }
                }
            }
        },
        "host": {
            "name": "fame"
        },
        "log": {
            "hostname": "fame"
        },
        "process": {
            "args": [
                "/usr/bin/python3",
                "/usr/share/unattended-upgrades/unattended-upgrade-shutdown",
                "--wait-for-signal"
            ],
            "start": "2021-01-01T00:01:01.000Z",
            "hash": {
                "sha1": "azertyuiop1234567890"
            },
            "name": "unattended-upgr",
            "entity_id": "rvSkGilnHCy6yuIZ",
            "pid": 1195,
            "executable": "/usr/bin/python3.8",
            "working_directory": "/",
            "parent": {
                "pid": 1
            },
            "command_line": "/usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal"
        },
        "service": {
            "type": "system"
        },
        "@timestamp": "2021-01-01T00:01:01.000Z",
        "user": {
            "name": "root",
            "id": "0",
            "group": {
                "id": "0",
                "name": "root"
            },
            "effective": {
                "group": {
                    "id": "0"
                },
                "id": "0"
            },
            "saved": {
                "group": {
                    "id": "0"
                }
            }
        },
        "related": {
            "hash": [
                "azertyuiop1234567890"
            ],
            "user": [
                "root"
            ]
        }
    }
    	
	```


=== "example4.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"ecs\":{\"version\":\"1.9.0\"},\"host\":{\"name\":\"fame\"},\"agent\":{\"version\":\"7.13.0\",\"hostname\":\"fame\",\"ephemeral_id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"name\":\"fame\",\"type\":\"auditbeat\"},\"user\":{\"effective\":{\"id\":\"114\",\"group\":{\"id\":\"121\"}},\"saved\":{\"id\":\"114\",\"group\":{\"id\":\"121\"}},\"name\":\"postgres\",\"id\":\"114\",\"group\":{\"name\":\"postgres\",\"id\":\"121\"}},\"service\":{\"type\":\"system\"},\"event\":{\"category\":[\"process\"],\"type\":[\"info\"],\"action\":\"existing_process\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"module\":\"system\",\"dataset\":\"process\",\"kind\":\"state\"},\"process\":{\"executable\":\"/usr/lib/postgresql/9.5/bin/postgres\",\"ppid\":1231,\"start\":\"2021-01-01T00:01:01.000Z\",\"hash\":{\"sha1\":\"azertyuiop1234567890\"},\"name\":\"postgres\",\"args\":[\"postgres: cuckoo cuckoo 127.0.0.1(45786) idle\"],\"entity_id\":\"azertyuiop\",\"working_directory\":\"/var/lib/postgresql/9.5/main\",\"pid\":207706},\"message\":\"Process postgres (PID: 207706) by user postgres is RUNNING\"}",
        "event": {
            "kind": "state",
            "module": "system",
            "category": [
                "process"
            ],
            "type": [
                "info"
            ],
            "action": "existing_process"
        },
        "agent": {
            "version": "7.13.0",
            "hostname": "fame",
            "ephemeral_id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "name": "fame",
            "type": "auditbeat"
        },
        "auditbeat": {
            "@metadata": {},
            "ecs": {},
            "host": {},
            "agent": {},
            "user": {
                "effective": {
                    "group": {}
                },
                "saved": {
                    "group": {}
                },
                "group": {}
            },
            "service": {},
            "event": {},
            "process": {
                "hash": {}
            },
            "message": "Process postgres (PID: 207706) by user postgres is RUNNING"
        },
        "auditd": {
            "user": {
                "effective": {
                    "group": {}
                },
                "saved": {
                    "id": "114",
                    "group": {
                        "id": "121"
                    }
                },
                "group": {
                    "id": "121"
                }
            }
        },
        "host": {
            "name": "fame"
        },
        "log": {
            "hostname": "fame"
        },
        "process": {
            "executable": "/usr/lib/postgresql/9.5/bin/postgres",
            "start": "2021-01-01T00:01:01.000Z",
            "hash": {
                "sha1": "azertyuiop1234567890"
            },
            "name": "postgres",
            "args": [
                "postgres: cuckoo cuckoo 127.0.0.1(45786) idle"
            ],
            "entity_id": "azertyuiop",
            "working_directory": "/var/lib/postgresql/9.5/main",
            "pid": 207706,
            "parent": {
                "pid": 1231
            }
        },
        "service": {
            "type": "system"
        },
        "@timestamp": "2021-01-01T00:01:01.000Z",
        "user": {
            "effective": {
                "id": "114",
                "group": {
                    "id": "121"
                }
            },
            "saved": {
                "group": {
                    "id": "121"
                }
            },
            "name": "postgres",
            "id": "114",
            "group": {
                "name": "postgres",
                "id": "121"
            }
        },
        "related": {
            "hash": [
                "azertyuiop1234567890"
            ],
            "user": [
                "postgres"
            ]
        }
    }
    	
	```


=== "example5.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"related\":{\"ip\":[\"127.0.0.1\",\"127.0.0.1\"]},\"service\":{\"type\":\"system\"},\"ecs\":{\"version\":\"1.9.0\"},\"host\":{\"name\":\"fame\"},\"client\":{\"port\":88888,\"packets\":1,\"bytes\":52,\"ip\":\"127.0.0.1\"},\"system\":{\"audit\":{\"socket\":{\"kernel_sock_address\":\"0xffff8e9955b02300\"}}},\"network\":{\"direction\":\"unknown\",\"type\":\"ipv4\",\"transport\":\"tcp\",\"packets\":2,\"bytes\":84,\"community_id\":\"12345678901234567891234567890\"},\"event\":{\"duration\":116168,\"module\":\"system\",\"kind\":\"event\",\"action\":\"network_flow\",\"type\":[\"info\",\"connection\"],\"dataset\":\"socket\",\"end\":\"2021-01-01T00:01:01.000Z\",\"category\":[\"network\",\"network_traffic\"],\"start\":\"2021-01-01T00:01:01.000Z\"},\"flow\":{\"complete\":false,\"final\":true},\"agent\":{\"version\":\"7.13.0\",\"hostname\":\"fame\",\"ephemeral_id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"name\":\"fame\",\"type\":\"auditbeat\"},\"source\":{\"packets\":1,\"bytes\":52,\"ip\":\"127.0.0.1\",\"port\":88888},\"destination\":{\"port\":11111,\"packets\":1,\"bytes\":32,\"ip\":\"127.0.0.1\"},\"server\":{\"ip\":\"127.0.0.1\",\"port\":11111,\"packets\":1,\"bytes\":32}}",
        "event": {
            "kind": "event",
            "module": "system",
            "category": [
                "network",
                "network_traffic"
            ],
            "type": [
                "info",
                "connection"
            ],
            "action": "network_flow"
        },
        "agent": {
            "version": "7.13.0",
            "hostname": "fame",
            "ephemeral_id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "name": "fame",
            "type": "auditbeat"
        },
        "auditbeat": {
            "@metadata": {},
            "related": {},
            "service": {},
            "ecs": {},
            "host": {},
            "client": {},
            "system": {
                "audit": {
                    "socket": {}
                }
            },
            "network": {},
            "event": {},
            "flow": {},
            "agent": {},
            "source": {},
            "destination": {},
            "server": {}
        },
        "client": {
            "port": 88888,
            "packets": 1,
            "bytes": 52,
            "ip": "127.0.0.1",
            "address": "127.0.0.1"
        },
        "destination": {
            "port": 11111,
            "packets": 1,
            "bytes": 32,
            "ip": "127.0.0.1",
            "address": "127.0.0.1"
        },
        "host": {
            "name": "fame"
        },
        "log": {
            "hostname": "fame"
        },
        "network": {
            "direction": "unknown",
            "type": "ipv4",
            "transport": "tcp",
            "packets": 2,
            "bytes": 84,
            "community_id": "12345678901234567891234567890"
        },
        "related": {
            "ip": [
                "127.0.0.1"
            ]
        },
        "server": {
            "ip": "127.0.0.1",
            "port": 11111,
            "packets": 1,
            "bytes": 32
        },
        "service": {
            "type": "system"
        },
        "source": {
            "packets": 1,
            "bytes": 52,
            "ip": "127.0.0.1",
            "port": 88888,
            "address": "127.0.0.1"
        },
        "system": {
            "audit": {
                "socket": {}
            }
        },
        "@timestamp": "2021-01-01T00:01:01.000Z"
    }
    	
	```


=== "example6.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"user\":{\"group\":{\"name\":\"messagebus\",\"id\":\"110\"},\"effective\":{\"id\":\"106\",\"group\":{\"id\":\"110\"}},\"saved\":{\"group\":{\"id\":\"110\"},\"id\":\"106\"},\"name\":\"messagebus\",\"id\":\"106\"},\"ecs\":{\"version\":\"1.9.0\"},\"host\":{\"name\":\"fame\"},\"agent\":{\"hostname\":\"fame\",\"ephemeral_id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"name\":\"fame\",\"type\":\"auditbeat\",\"version\":\"7.13.0\"},\"service\":{\"type\":\"system\"},\"event\":{\"category\":[\"process\"],\"type\":[\"info\"],\"action\":\"existing_process\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"module\":\"system\",\"dataset\":\"process\",\"kind\":\"state\"},\"process\":{\"args\":[\"/usr/bin/dbus-daemon\",\"--system\",\"--address=systemd:\",\"--nofork\",\"--nopidfile\",\"--systemd-activation\",\"--syslog-only\"],\"hash\":{\"sha1\":\"azertyuiop1234567890\"},\"entity_id\":\"azertyuiop\",\"working_directory\":\"/\",\"ppid\":1,\"pid\":645,\"start\":\"2021-01-01T00:01:01.000Z\",\"executable\":\"/usr/bin/dbus-daemon\",\"name\":\"dbus-daemon\"},\"message\":\"Process dbus-daemon (PID: 645) by user messagebus is RUNNING\"}",
        "event": {
            "kind": "state",
            "module": "system",
            "category": [
                "process"
            ],
            "type": [
                "info"
            ],
            "action": "existing_process"
        },
        "agent": {
            "hostname": "fame",
            "ephemeral_id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0"
        },
        "auditbeat": {
            "@metadata": {},
            "user": {
                "group": {},
                "effective": {
                    "group": {}
                },
                "saved": {
                    "group": {}
                }
            },
            "ecs": {},
            "host": {},
            "agent": {},
            "service": {},
            "event": {},
            "process": {
                "hash": {}
            },
            "message": "Process dbus-daemon (PID: 645) by user messagebus is RUNNING"
        },
        "auditd": {
            "user": {
                "group": {
                    "id": "110"
                },
                "effective": {
                    "group": {}
                },
                "saved": {
                    "group": {
                        "id": "110"
                    },
                    "id": "106"
                }
            }
        },
        "host": {
            "name": "fame"
        },
        "log": {
            "hostname": "fame"
        },
        "process": {
            "args": [
                "/usr/bin/dbus-daemon",
                "--system",
                "--address=systemd:",
                "--nofork",
                "--nopidfile",
                "--systemd-activation",
                "--syslog-only"
            ],
            "hash": {
                "sha1": "azertyuiop1234567890"
            },
            "entity_id": "azertyuiop",
            "working_directory": "/",
            "pid": 645,
            "start": "2021-01-01T00:01:01.000Z",
            "executable": "/usr/bin/dbus-daemon",
            "name": "dbus-daemon",
            "parent": {
                "pid": 1
            },
            "command_line": "/usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only"
        },
        "service": {
            "type": "system"
        },
        "@timestamp": "2021-01-01T00:01:01.000Z",
        "user": {
            "group": {
                "name": "messagebus",
                "id": "110"
            },
            "effective": {
                "id": "106",
                "group": {
                    "id": "110"
                }
            },
            "saved": {
                "group": {
                    "id": "110"
                }
            },
            "name": "messagebus",
            "id": "106"
        },
        "related": {
            "hash": [
                "azertyuiop1234567890"
            ],
            "user": [
                "messagebus"
            ]
        }
    }
    	
	```


=== "example7.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"service\":{\"type\":\"system\"},\"event\":{\"action\":\"existing_process\",\"id\":\"e9c16612-2053-4bc6-86aa-7e04c6114ecc\",\"module\":\"system\",\"dataset\":\"process\",\"kind\":\"state\",\"category\":[\"process\"],\"type\":[\"info\"]},\"process\":{\"executable\":\"/usr/lib/postgresql/9.5/bin/postgres\",\"entity_id\":\"1234zertyui\",\"ppid\":1231,\"start\":\"2021-01-01T00:01:01.000Z\",\"name\":\"postgres\",\"pid\":1234,\"working_directory\":\"/var/lib/postgresql/9.5/main\",\"hash\":{\"sha1\":\"12345678901234567891234567890\"},\"args\":[\"postgres: wal writer process   \"]},\"host\":{\"name\":\"fame\"},\"agent\":{\"ephemeral_id\":\"0101010-abcd-1234-a1b2c3d4e5f6g7h8\",\"id\":\"0101010-abcd-1234-a1b2c3d4e5f6g7h8\",\"name\":\"fame\",\"type\":\"auditbeat\",\"version\":\"7.13.0\",\"hostname\":\"fame\"},\"ecs\":{\"version\":\"1.9.0\"},\"message\":\"Process postgres (PID: 1234) by user postgres is RUNNING\",\"user\":{\"effective\":{\"group\":{\"id\":\"121\"},\"id\":\"114\"},\"saved\":{\"id\":\"114\",\"group\":{\"id\":\"121\"}},\"name\":\"postgres\",\"id\":\"114\",\"group\":{\"id\":\"121\",\"name\":\"postgres\"}}}",
        "event": {
            "kind": "state",
            "module": "system",
            "category": [
                "process"
            ],
            "type": [
                "info"
            ],
            "action": "existing_process"
        },
        "agent": {
            "ephemeral_id": "0101010-abcd-1234-a1b2c3d4e5f6g7h8",
            "id": "0101010-abcd-1234-a1b2c3d4e5f6g7h8",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0",
            "hostname": "fame"
        },
        "auditbeat": {
            "@metadata": {},
            "service": {},
            "event": {},
            "process": {
                "hash": {}
            },
            "host": {},
            "agent": {},
            "ecs": {},
            "message": "Process postgres (PID: 1234) by user postgres is RUNNING",
            "user": {
                "effective": {
                    "group": {}
                },
                "saved": {
                    "group": {}
                },
                "group": {}
            }
        },
        "auditd": {
            "user": {
                "effective": {
                    "group": {}
                },
                "saved": {
                    "id": "114",
                    "group": {
                        "id": "121"
                    }
                },
                "group": {
                    "id": "121"
                }
            }
        },
        "host": {
            "name": "fame"
        },
        "log": {
            "hostname": "fame"
        },
        "process": {
            "executable": "/usr/lib/postgresql/9.5/bin/postgres",
            "entity_id": "1234zertyui",
            "start": "2021-01-01T00:01:01.000Z",
            "name": "postgres",
            "pid": 1234,
            "working_directory": "/var/lib/postgresql/9.5/main",
            "hash": {
                "sha1": "12345678901234567891234567890"
            },
            "args": [
                "postgres: wal writer process   "
            ],
            "parent": {
                "pid": 1231
            }
        },
        "service": {
            "type": "system"
        },
        "@timestamp": "2021-01-01T00:01:01.000Z",
        "user": {
            "effective": {
                "group": {
                    "id": "121"
                },
                "id": "114"
            },
            "saved": {
                "group": {
                    "id": "121"
                }
            },
            "name": "postgres",
            "id": "114",
            "group": {
                "id": "121",
                "name": "postgres"
            }
        },
        "related": {
            "hash": [
                "12345678901234567891234567890"
            ],
            "user": [
                "postgres"
            ]
        }
    }
    	
	```


=== "example8.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"destination\":{\"bytes\":123,\"ip\":\"8.8.8.8\",\"port\":53,\"packets\":1},\"event\":{\"end\":\"2021-01-01T00:01:01.000Z\",\"type\":[\"info\",\"connection\"],\"action\":\"network_flow\",\"dataset\":\"socket\",\"kind\":\"event\",\"category\":[\"network\",\"network_traffic\"],\"start\":\"2021-01-01T00:01:01.000Z\",\"duration\":12345,\"module\":\"system\"},\"process\":{\"pid\":9876543,\"name\":\"smtp\",\"args\":[\"smtp\",\"-t\",\"unix\",\"-u\",\"-c\"],\"executable\":\"/usr/lib/postfix/sbin/smtp\",\"created\":\"2021-01-01T00:01:01.000Z\"},\"client\":{\"bytes\":70,\"domain\":\"malware1.viralstudio.org\",\"ip\":\"255.255.255.1\",\"port\":58855,\"packets\":1},\"ecs\":{\"version\":\"1.9.0\"},\"server\":{\"bytes\":123,\"ip\":\"8.8.8.8\",\"port\":53,\"packets\":1},\"source\":{\"domain\":\"malware1.viralstudio.org\",\"ip\":\"255.255.255.1\",\"port\":58855,\"packets\":1,\"bytes\":70},\"network\":{\"transport\":\"udp\",\"packets\":2,\"bytes\":210,\"community_id\":\"azertyuiopsdfghjklm\",\"direction\":\"egress\",\"type\":\"ipv4\"},\"group\":{\"id\":\"0\",\"name\":\"root\"},\"service\":{\"type\":\"system\"},\"host\":{\"name\":\"fame\"},\"agent\":{\"ephemeral_id\":\"0101010-abcd-1234-a1b2c3d4e5f6g7h8\",\"id\":\"123poi-99zz-4qzds099-qsd-azerty\",\"name\":\"fame\",\"type\":\"auditbeat\",\"version\":\"7.13.0\",\"hostname\":\"fame\"},\"flow\":{\"final\":true,\"complete\":false},\"related\":{\"ip\":[\"255.255.255.1\",\"8.8.8.8\"],\"user\":[\"root\"]},\"user\":{\"id\":\"0\",\"name\":\"root\"},\"system\":{\"audit\":{\"socket\":{\"gid\":0,\"euid\":0,\"egid\":0,\"kernel_sock_address\":\"0xffffffffffffff\",\"uid\":0}}}}",
        "event": {
            "kind": "event",
            "module": "system",
            "category": [
                "network",
                "network_traffic"
            ],
            "type": [
                "info",
                "connection"
            ],
            "action": "network_flow"
        },
        "agent": {
            "ephemeral_id": "0101010-abcd-1234-a1b2c3d4e5f6g7h8",
            "id": "123poi-99zz-4qzds099-qsd-azerty",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0",
            "hostname": "fame"
        },
        "auditbeat": {
            "@metadata": {},
            "destination": {},
            "event": {},
            "process": {},
            "client": {},
            "ecs": {},
            "server": {},
            "source": {},
            "network": {},
            "group": {},
            "service": {},
            "host": {},
            "agent": {},
            "flow": {},
            "related": {},
            "user": {},
            "system": {
                "audit": {
                    "socket": {}
                }
            }
        },
        "auditd": {
            "user": {}
        },
        "client": {
            "bytes": 70,
            "domain": "malware1.viralstudio.org",
            "ip": "255.255.255.1",
            "port": 58855,
            "packets": 1,
            "address": "malware1.viralstudio.org",
            "top_level_domain": "org",
            "subdomain": "malware1",
            "registered_domain": "viralstudio.org"
        },
        "destination": {
            "bytes": 123,
            "ip": "8.8.8.8",
            "port": 53,
            "packets": 1,
            "address": "8.8.8.8"
        },
        "group": {
            "id": "0",
            "name": "root"
        },
        "host": {
            "name": "fame"
        },
        "log": {
            "hostname": "fame"
        },
        "network": {
            "transport": "udp",
            "packets": 2,
            "bytes": 210,
            "community_id": "azertyuiopsdfghjklm",
            "direction": "egress",
            "type": "ipv4"
        },
        "process": {
            "pid": 9876543,
            "name": "smtp",
            "args": [
                "smtp",
                "-t",
                "unix",
                "-u",
                "-c"
            ],
            "executable": "/usr/lib/postfix/sbin/smtp",
            "command_line": "smtp -t unix -u -c"
        },
        "related": {
            "hosts": [
                "malware1.viralstudio.org"
            ],
            "ip": [
                "255.255.255.1",
                "8.8.8.8"
            ],
            "user": [
                "root"
            ]
        },
        "server": {
            "bytes": 123,
            "ip": "8.8.8.8",
            "port": 53,
            "packets": 1
        },
        "service": {
            "type": "system"
        },
        "source": {
            "domain": "malware1.viralstudio.org",
            "ip": "255.255.255.1",
            "port": 58855,
            "packets": 1,
            "bytes": 70,
            "address": "malware1.viralstudio.org",
            "top_level_domain": "org",
            "subdomain": "malware1",
            "registered_domain": "viralstudio.org"
        },
        "system": {
            "audit": {
                "socket": {}
            }
        },
        "@timestamp": "2021-01-01T00:01:01.000Z",
        "user": {
            "id": "0",
            "name": "root"
        }
    }
    	
	```


=== "example9.json"

    ```json
	
    {
        "message": "{\"@timestamp\":\"2021-11-09T16:17:55.149Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.15.1\"},\"event\":{\"kind\":\"event\",\"type\":[\"start\"],\"module\":\"auditd\",\"category\":[\"process\"],\"action\":\"ran-command\",\"outcome\":\"success\"},\"user\":{\"id\":\"4e8ff660-f139-4248-8b64-ad29495fca9e\",\"name\":\"NElD74Hc4MX8PjLF\",\"audit\":{\"id\":\"4e8ff660-f139-4248-8b64-ad29495fca9e\",\"name\":\"NElD74Hc4MX8PjLF\"}},\"host\":{\"hostname\":\"web-66\",\"architecture\":\"x86_64\",\"os\":{\"type\":\"linux\",\"platform\":\"ubuntu\",\"version\":\"18.04.6 LTS (Bionic Beaver)\",\"family\":\"debian\",\"name\":\"Ubuntu\",\"kernel\":\"4.15.0-161-generic\",\"codename\":\"bionic\"},\"id\":\"7dd912136af040e4a6ea4f683010b824\",\"containerized\":false,\"ip\":[\"173.8.126.146\"],\"name\":\"web-66\",\"mac\":[\"57:4c:ff:5d:1e:41\"]},\"agent\":{\"id\":\"e9872892-b999-4ad5-83da-d6ec9dbc1f81\",\"name\":\"web-66\",\"type\":\"auditbeat\",\"version\":\"7.15.1\",\"hostname\":\"web-66\",\"ephemeral_id\":\"f1ac5b09-4f0c-42cf-b9f7-f854eeae073a\"},\"ecs\":{\"version\":\"1.11.0\"},\"process\":{\"pid\":12416,\"working_directory\":\"/home/NElD74Hc4MX8PjLF/Documents/Projets/Qh1HoDnBg4mYfHhi\"},\"auditd\":{\"data\":{\"terminal\":\"pts/3\",\"cmd\":\"systemctl status auditbeat\"},\"session\":\"2\",\"summary\":{\"actor\":{\"primary\":\"NElD74Hc4MX8PjLF\",\"secondary\":\"NElD74Hc4MX8PjLF\"},\"object\":{\"primary\":\"systemctl status auditbeat\",\"type\":\"process\"}},\"message_type\":\"user_cmd\",\"sequence\":465,\"result\":\"success\"},\"service\":{\"type\":\"auditd\"}}",
        "event": {
            "kind": "event",
            "module": "auditd",
            "category": [
                "process"
            ],
            "type": [
                "start"
            ],
            "action": "ran-command"
        },
        "agent": {
            "id": "e9872892-b999-4ad5-83da-d6ec9dbc1f81",
            "name": "web-66",
            "type": "auditbeat",
            "version": "7.15.1",
            "hostname": "web-66",
            "ephemeral_id": "f1ac5b09-4f0c-42cf-b9f7-f854eeae073a"
        },
        "auditbeat": {
            "@metadata": {},
            "event": {},
            "user": {
                "audit": {}
            },
            "host": {
                "os": {}
            },
            "agent": {},
            "ecs": {},
            "process": {},
            "auditd": {
                "data": {},
                "summary": {
                    "actor": {},
                    "object": {}
                }
            },
            "service": {}
        },
        "auditd": {
            "data": {
                "terminal": "pts/3",
                "cmd": "systemctl status auditbeat"
            },
            "session": "2",
            "summary": {
                "actor": {
                    "primary": "NElD74Hc4MX8PjLF",
                    "secondary": "NElD74Hc4MX8PjLF"
                },
                "object": {
                    "primary": "systemctl status auditbeat",
                    "type": "process"
                }
            },
            "message_type": "user_cmd",
            "sequence": 465,
            "result": "success",
            "user": {
                "audit": {}
            }
        },
        "host": {
            "hostname": "web-66",
            "architecture": "x86_64",
            "os": {
                "type": "linux",
                "platform": "ubuntu",
                "version": "18.04.6 LTS (Bionic Beaver)",
                "family": "debian",
                "name": "Ubuntu",
                "kernel": "4.15.0-161-generic",
                "codename": "bionic"
            },
            "id": "7dd912136af040e4a6ea4f683010b824",
            "containerized": false,
            "ip": [
                "173.8.126.146"
            ],
            "name": "web-66",
            "mac": [
                "57:4c:ff:5d:1e:41"
            ]
        },
        "log": {
            "hostname": "web-66"
        },
        "process": {
            "pid": 12416,
            "working_directory": "/home/NElD74Hc4MX8PjLF/Documents/Projets/Qh1HoDnBg4mYfHhi"
        },
        "service": {
            "type": "auditd"
        },
        "@timestamp": "2021-11-09T16:17:55.149Z",
        "user": {
            "id": "4e8ff660-f139-4248-8b64-ad29495fca9e",
            "name": "NElD74Hc4MX8PjLF",
            "audit": {
                "id": "4e8ff660-f139-4248-8b64-ad29495fca9e",
                "name": "NElD74Hc4MX8PjLF"
            }
        },
        "related": {
            "ip": [
                "173.8.126.146"
            ],
            "hosts": [
                "web-66"
            ],
            "user": [
                "NElD74Hc4MX8PjLF"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`agent.hostname` | `keyword` | Deprecated - use agent.name or agent.id to identify an agent. Hostname of the agent. |
|`cloud.image.id` | `keyword` | Image ID for the cloud instance. |
|`container.image.name` | `keyword` | Name of the image the container was built on. |
|`error.message` | `match_only_text` | Error message. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.module` | `keyword` | Name of the module this data is coming from. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`fields` | `object` | Contains user configurable fields. |
|`host.name` | `keyword` | Name of the host. |
|`log.hostname` | `keyword` | Hostname of the computer (temporary fix for detection rules and smart description). |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.parent.pid` | `long` | Process id. |

