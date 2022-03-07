
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Authentication logs` | From system module, login dataset retreive User logins, logouts, and system boots |
| `File monitoring` | From audit module, the file metricset sends events when a file is changed (created, updated, or deleted) on disk. The events contain file metadata and hashes |
| `Process monitoring` | From system module, process dataset retreive Started and stopped processes |
| `Process use of network` | From system module, socket dataset retreive Opened and Closed sockets |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "example8.json"

    ```json
	
    {
        "agent": {
            "ephemeral_id": "0101010-abcd-1234-a1b2c3d4e5f6g7h8",
            "hostname": "fame",
            "id": "123poi-99zz-4qzds099-qsd-azerty",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0"
        },
        "client": {
            "bytes": 70,
            "domain": "malware1.viralstudio.org",
            "ip": "255.255.255.1",
            "packets": 1,
            "port": 58855
        },
        "destination": {
            "bytes": 123,
            "ip": "8.8.8.8",
            "packets": 1,
            "port": 53
        },
        "ecs": {
            "version": "1.9.0"
        },
        "event": {
            "action": "network_flow",
            "category": [
                "network",
                "network_traffic"
            ],
            "dataset": "socket",
            "duration": 12345,
            "end": "2021-01-01T00:01:01.000Z",
            "kind": "event",
            "module": "system",
            "start": "2021-01-01T00:01:01.000Z",
            "type": [
                "info",
                "connection"
            ]
        },
        "group": {
            "id": "0",
            "name": "root"
        },
        "host": {
            "name": "fame"
        },
        "network": {
            "bytes": 210,
            "community_id": "azertyuiopsdfghjklm",
            "direction": "egress",
            "packets": 2,
            "transport": "udp",
            "type": "ipv4"
        },
        "process": {
            "args": [
                "smtp",
                "-t",
                "unix",
                "-u",
                "-c"
            ],
            "executable": "/usr/lib/postfix/sbin/smtp",
            "name": "smtp",
            "pid": 9876543,
            "command_line": "smtp -t unix -u -c"
        },
        "related": {
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
            "packets": 1,
            "port": 53
        },
        "service": {
            "type": "system"
        },
        "source": {
            "bytes": 70,
            "domain": "malware1.viralstudio.org",
            "ip": "255.255.255.1",
            "packets": 1,
            "port": 58855
        },
        "user": {
            "id": "0",
            "name": "root"
        }
    }
    	
	```


=== "example12.json"

    ```json
	
    {
        "ecs": {
            "version": "1.10.0"
        },
        "user": {
            "audit": {
                "id": "0",
                "name": "root"
            },
            "effective": {
                "id": "0",
                "name": "root"
            }
        },
        "host": {
            "mac": [
                "5e:55:38:73:40:a4"
            ],
            "id": "7dd912136af040e4a6ea4f683010b824",
            "name": "web-65",
            "containerized": false,
            "hostname": "web-65",
            "os": {
                "type": "linux",
                "platform": "ubuntu",
                "name": "Ubuntu",
                "kernel": "4.15.0-161-generic",
                "family": "debian",
                "version": "18.04.6 LTS (Bionic Beaver)",
                "codename": "bionic"
            },
            "ip": [
                "66.253.230.251"
            ],
            "architecture": "x86_64"
        },
        "agent": {
            "id": "e9872892-b999-4ad5-83da-d6ec9dbc1f81",
            "type": "auditbeat",
            "name": "web-65",
            "hostname": "web-65",
            "version": "7.15.1",
            "ephemeral_id": "f1ac5b09-4f0c-42cf-b9f7-f854eeae073a"
        },
        "sekoiaio": {
            "intake": {
                "dialect_uuid": "021e9def-5a55-4369-941e-af269b45bef1",
                "parsing_status": "success",
                "dialect": "auditbeat"
            },
            "customer": {
                "id": "986e50d4-5db1-4dfd-a079-ca8f462647e1",
                "community_uuid": "437c6901-db28-473e-b2bc-0c79c57585c8",
                "community_name": "8qVekia1L80BrZOJ"
            },
            "entity": {
                "uuid": "0d4efad3-ac86-48d3-b2ac-5591d6ad2a09",
                "id": "d6DQmV77mYqMlxTh",
                "name": "nr1AfxwR5deBbmEO"
            }
        },
        "service": {
            "type": "auditd"
        },
        "@timestamp": "2021-11-09T18:35:02.761Z",
        "message": "{\"@timestamp\":\"2021-11-09T18:35:01.754Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.15.1\"},\"related\":{\"user\":[\"root\"]},\"service\":{\"type\":\"auditd\"},\"event\":{\"module\":\"auditd\",\"category\":[\"authentication\"],\"action\":\"changed-login-id-to\",\"outcome\":\"success\",\"kind\":\"event\",\"type\":[\"start\"]},\"user\":{\"audit\":{\"id\":\"0\",\"name\":\"root\"},\"effective\":{\"id\":\"0\",\"name\":\"root\"}},\"ecs\":{\"version\":\"1.11.0\"},\"host\":{\"containerized\":false,\"ip\":[\"66.253.230.251\"],\"mac\":[\"5e:55:38:73:40:a4\"],\"hostname\":\"web-65\",\"architecture\":\"x86_64\",\"os\":{\"codename\":\"bionic\",\"type\":\"linux\",\"platform\":\"ubuntu\",\"version\":\"18.04.6 LTS (Bionic Beaver)\",\"family\":\"debian\",\"name\":\"Ubuntu\",\"kernel\":\"4.15.0-161-generic\"},\"name\":\"web-65\",\"id\":\"7dd912136af040e4a6ea4f683010b824\"},\"agent\":{\"ephemeral_id\":\"f1ac5b09-4f0c-42cf-b9f7-f854eeae073a\",\"id\":\"e9872892-b999-4ad5-83da-d6ec9dbc1f81\",\"name\":\"web-65\",\"type\":\"auditbeat\",\"version\":\"7.15.1\",\"hostname\":\"web-65\"},\"process\":{\"pid\":20899},\"auditd\":{\"data\":{\"tty\":\"(none)\",\"old-ses\":\"4294967295\"},\"session\":\"436\",\"summary\":{\"actor\":{\"primary\":\"unset\",\"secondary\":\"root\"},\"object\":{\"primary\":\"0\",\"type\":\"user-session\"}},\"message_type\":\"login\",\"sequence\":11578,\"result\":\"success\"}}",
        "event": {
            "dialect_uuid": "4922a107-c91d-46e8-ab0b-d21236d92b90",
            "id": "8a23c8c9-59c5-4226-9507-5432f1a33898",
            "type": [
                "start"
            ],
            "category": [
                "authentication"
            ],
            "hash": "260c64ee23e7fed757cd65e01aebc80dc9333089",
            "kind": "event",
            "created": "2021-05-26",
            "module": "auditd",
            "dialect": "auditbeat",
            "outcome": "success",
            "action": "changed-login-id-to"
        },
        "related": {
            "hash": [
                "260c64ee23e7fed757cd65e01aebc80dc9333089"
            ],
            "ip": [
                "66.253.230.251"
            ],
            "hosts": [
                "web-65"
            ]
        },
        "process": {
            "pid": 20899
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
            "result": "success"
        }
    }
    	
	```


=== "example3.json"

    ```json
	
    {
        "agent": {
            "ephemeral_id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "hostname": "fame",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0"
        },
        "auditbeat": {
            "message": "Process unattended-upgr (PID: 1195) by user root is RUNNING"
        },
        "auditd": {
            "user": {
                "saved": {
                    "group": {
                        "id": "0"
                    },
                    "id": "0"
                }
            }
        },
        "event": {
            "action": "existing_process",
            "category": [
                "process"
            ],
            "dataset": "process",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "kind": "state",
            "module": "system",
            "type": [
                "info"
            ]
        },
        "host": {
            "name": "fame"
        },
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"message\":\"Process unattended-upgr (PID: 1195) by user root is RUNNING\",\"user\":{\"name\":\"root\",\"id\":\"0\",\"group\":{\"id\":\"0\",\"name\":\"root\"},\"effective\":{\"group\":{\"id\":\"0\"},\"id\":\"0\"},\"saved\":{\"id\":\"0\",\"group\":{\"id\":\"0\"}}},\"service\":{\"type\":\"system\"},\"event\":{\"type\":[\"info\"],\"action\":\"existing_process\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"module\":\"system\",\"dataset\":\"process\",\"kind\":\"state\",\"category\":[\"process\"]},\"process\":{\"args\":[\"/usr/bin/python3\",\"/usr/share/unattended-upgrades/unattended-upgrade-shutdown\",\"--wait-for-signal\"],\"start\":\"2021-01-01T00:01:01.000Z\",\"hash\":{\"sha1\":\"azertyuiop1234567890\"},\"name\":\"unattended-upgr\",\"entity_id\":\"rvSkGilnHCy6yuIZ\",\"pid\":1195,\"ppid\":1,\"executable\":\"/usr/bin/python3.8\",\"working_directory\":\"/\"},\"ecs\":{\"version\":\"1.9.0\"},\"host\":{\"name\":\"fame\"},\"agent\":{\"version\":\"7.13.0\",\"hostname\":\"fame\",\"ephemeral_id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"name\":\"fame\",\"type\":\"auditbeat\"}}",
        "process": {
            "args": [
                "/usr/bin/python3",
                "/usr/share/unattended-upgrades/unattended-upgrade-shutdown",
                "--wait-for-signal"
            ],
            "entity_id": "rvSkGilnHCy6yuIZ",
            "executable": "/usr/bin/python3.8",
            "hash": {
                "sha1": "azertyuiop1234567890"
            },
            "name": "unattended-upgr",
            "pid": 1195,
            "ppid": 1,
            "start": "2021-01-01T00:01:01.000Z",
            "working_directory": "/",
            "command_line": "/usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "auditbeat",
                "dialect_uuid": "12345678-azer-1234-a1z2-12qsdfghjklm"
            }
        },
        "service": {
            "type": "system"
        },
        "user": {
            "effective": {
                "group": {
                    "id": "0"
                },
                "id": "0"
            },
            "group": {
                "id": "0",
                "name": "root"
            },
            "id": "0",
            "name": "root"
        }
    }
    	
	```


=== "example10.json"

    ```json
	
    {
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
            "group": {
                "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430",
                "name": "housetodd"
            },
            "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430"
        },
        "auditbeat": {
            "tags": [
                "access"
            ]
        },
        "@timestamp": "2021-11-09T17:39:27.218Z",
        "event": {
            "category": [
                "file"
            ],
            "id": "3a4fc4b3-f7b8-4b41-b696-bf7d452a0bec",
            "dialect_uuid": "18f1e8ee-7e55-484d-b210-a7ebeeb62924",
            "kind": "event",
            "created": "2021-06-10",
            "hash": "89e3ad1078a4ee2210d04736528e10476dda685d",
            "module": "auditd",
            "type": [
                "creation"
            ],
            "outcome": "failure",
            "action": "opened-file",
            "dialect": "auditbeat"
        },
        "message": "{\"@timestamp\":\"2021-11-09T17:39:26.389Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.15.1\"},\"process\":{\"ppid\":18470,\"title\":\"/opt/google/chrome/chrome --type=zygote --enable-crashpad --crashpad-handler-pid=18479 --enable-crash-reporter=, --change-stack-\",\"name\":\"chrome\",\"executable\":\"/opt/google/chrome/chrome\",\"working_directory\":\"/home/housetodd\",\"pid\":18488},\"auditd\":{\"session\":\"3\",\"summary\":{\"actor\":{\"primary\":\"housetodd\",\"secondary\":\"housetodd\"},\"object\":{\"primary\":\"/proc/1/oom_score_adj\",\"type\":\"file\"},\"how\":\"/opt/google/chrome/chrome\"},\"paths\":[{\"cap_fe\":\"0\",\"cap_fver\":\"0\",\"inode\":\"16064\",\"name\":\"/proc/1/\",\"ogid\":\"0\",\"ouid\":\"0\",\"rdev\":\"00:00\",\"cap_fi\":\"0000000000000000\",\"cap_fp\":\"0000000000000000\",\"dev\":\"00:04\",\"item\":\"0\",\"mode\":\"040555\",\"nametype\":\"PARENT\"},{\"nametype\":\"NORMAL\",\"ogid\":\"0\",\"ouid\":\"0\",\"cap_fe\":\"0\",\"dev\":\"00:04\",\"item\":\"1\",\"mode\":\"0100644\",\"name\":\"/proc/1/oom_score_adj\",\"rdev\":\"00:00\",\"cap_fi\":\"0000000000000000\",\"cap_fp\":\"0000000000000000\",\"cap_fver\":\"0\",\"inode\":\"25973\"}],\"message_type\":\"syscall\",\"sequence\":9052,\"result\":\"fail\",\"data\":{\"tty\":\"(none)\",\"exit\":\"EACCES\",\"a0\":\"7ffc1bfcdfa0\",\"a3\":\"7ffc1bfcde00\",\"a2\":\"55881de610b8\",\"a1\":\"1b6\",\"arch\":\"x86_64\",\"syscall\":\"creat\"}},\"event\":{\"module\":\"auditd\",\"category\":[\"file\"],\"action\":\"opened-file\",\"outcome\":\"failure\",\"kind\":\"event\",\"type\":[\"creation\"]},\"user\":{\"filesystem\":{\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"group\":{\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"name\":\"housetodd\"},\"name\":\"housetodd\"},\"name\":\"housetodd\",\"audit\":{\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"name\":\"housetodd\"},\"saved\":{\"group\":{\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"name\":\"housetodd\"},\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"name\":\"housetodd\"},\"group\":{\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\",\"name\":\"housetodd\"},\"id\":\"5511617b-5ca7-4dd5-bb80-d8590dff4430\"},\"host\":{\"name\":\"xps-housetodd\",\"ip\":[\"144.1.237.149\"],\"mac\":[\"22:69:ae:27:fe:66\"],\"hostname\":\"xps-housetodd\",\"architecture\":\"x86_64\",\"os\":{\"family\":\"debian\",\"name\":\"Ubuntu\",\"kernel\":\"4.15.0-161-generic\",\"codename\":\"bionic\",\"type\":\"linux\",\"platform\":\"ubuntu\",\"version\":\"18.04.6 LTS (Bionic Beaver)\"},\"id\":\"7dd912136af040e4a6ea4f683010b824\",\"containerized\":false},\"file\":{\"gid\":\"0\",\"owner\":\"housetodd\",\"group\":\"housetodd\",\"path\":\"/proc/1/oom_score_adj\",\"device\":\"00:00\",\"inode\":\"25973\",\"mode\":\"0644\",\"uid\":\"0\"},\"tags\":[\"access\"],\"service\":{\"type\":\"auditd\"},\"ecs\":{\"version\":\"1.11.0\"},\"agent\":{\"version\":\"7.15.1\",\"hostname\":\"xps-housetodd\",\"ephemeral_id\":\"f1ac5b09-4f0c-42cf-b9f7-f854eeae073a\",\"id\":\"e9872892-b999-4ad5-83da-d6ec9dbc1f81\",\"name\":\"xps-housetodd\",\"type\":\"auditbeat\"}}",
        "ecs": {
            "version": "1.10.0"
        },
        "process": {
            "pid": 18488,
            "name": "chrome",
            "working_directory": "/home/housetodd",
            "ppid": 18470,
            "title": "/opt/google/chrome/chrome --type=zygote --enable-crashpad --crashpad-handler-pid=18479 --enable-crash-reporter=, --change-stack-",
            "executable": "/opt/google/chrome/chrome"
        },
        "host": {
            "id": "7dd912136af040e4a6ea4f683010b824",
            "os": {
                "type": "linux",
                "kernel": "4.15.0-161-generic",
                "codename": "bionic",
                "name": "Ubuntu",
                "family": "debian",
                "platform": "ubuntu",
                "version": "18.04.6 LTS (Bionic Beaver)"
            },
            "mac": [
                "22:69:ae:27:fe:66"
            ],
            "name": "xps-housetodd",
            "ip": [
                "144.1.237.149"
            ],
            "hostname": "xps-housetodd",
            "architecture": "x86_64",
            "containerized": false
        },
        "sekoiaio": {
            "entity": {
                "id": "jw2ASKHGnsWFqGDQ",
                "uuid": "322dcda2-5cd1-438d-a49e-d76ef40d2fed",
                "name": "I8WiW2OHB9jqnxZW"
            },
            "intake": {
                "dialect_uuid": "021e9def-5a55-4369-941e-af269b45bef1",
                "dialect": "auditbeat",
                "parsing_status": "success"
            },
            "customer": {
                "id": "fe4f8db6-3ec4-4111-b5e9-0802cfed3d62",
                "community_uuid": "0da1e49f-203a-4585-973a-fbb54331bccb",
                "community_name": "jP0oXIBnhYiuJ0lI"
            }
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
                "saved": {
                    "group": {
                        "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430",
                        "name": "housetodd"
                    },
                    "id": "5511617b-5ca7-4dd5-bb80-d8590dff4430",
                    "name": "housetodd"
                }
            }
        },
        "agent": {
            "type": "auditbeat",
            "id": "e9872892-b999-4ad5-83da-d6ec9dbc1f81",
            "name": "xps-housetodd",
            "version": "7.15.1",
            "hostname": "xps-housetodd",
            "ephemeral_id": "f1ac5b09-4f0c-42cf-b9f7-f854eeae073a"
        },
        "file": {
            "inode": "25973",
            "path": "/proc/1/oom_score_adj",
            "gid": "0",
            "uid": "0",
            "group": "housetodd",
            "device": "00:00",
            "owner": "housetodd",
            "mode": "0644"
        },
        "service": {
            "type": "auditd"
        },
        "related": {
            "hash": [
                "89e3ad1078a4ee2210d04736528e10476dda685d"
            ],
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


=== "example13.json"

    ```json
	
    {
        "event": {
            "dialect_uuid": "423c9f61-0282-464d-a2f3-f2d745b59a3b",
            "id": "c7679ece-e22f-4144-a7f5-619034aa036d",
            "category": [
                "process"
            ],
            "hash": "249e78b65ea6378a41037766bd8b1f01abd1a371",
            "outcome": "success",
            "module": "auditd",
            "type": [
                "start"
            ],
            "dialect": "auditbeat",
            "created": "2021-03-12",
            "kind": "event",
            "action": "started-service"
        },
        "host": {
            "id": "7dd912136af040e4a6ea4f683010b824",
            "name": "LCPmbaxBgGyJj8VH",
            "mac": [
                "09:d0:5f:99:43:f6"
            ],
            "os": {
                "family": "debian",
                "name": "Ubuntu",
                "codename": "bionic",
                "type": "linux",
                "version": "18.04.6 LTS (Bionic Beaver)",
                "kernel": "4.15.0-161-generic",
                "platform": "ubuntu"
            },
            "architecture": "x86_64",
            "ip": [
                "87.138.107.154"
            ],
            "containerized": false,
            "hostname": "LCPmbaxBgGyJj8VH"
        },
        "user": {
            "id": "16bb03ba-2e90-4c98-a5c8-c3d8b8b52c1e",
            "name": "X9PzJKityWAFaA5i"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "message": "{\"@timestamp\":\"2021-11-09T19:02:33.866Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.15.1\"},\"event\":{\"kind\":\"event\",\"type\":[\"start\"],\"module\":\"auditd\",\"category\":[\"process\"],\"action\":\"started-service\",\"outcome\":\"success\"},\"user\":{\"id\":\"16bb03ba-2e90-4c98-a5c8-c3d8b8b52c1e\",\"name\":\"X9PzJKityWAFaA5i\"},\"process\":{\"pid\":1,\"name\":\"systemd\",\"executable\":\"/lib/systemd/systemd\"},\"auditd\":{\"result\":\"success\",\"data\":{\"unit\":\"anacron\"},\"summary\":{\"how\":\"/lib/systemd/systemd\",\"actor\":{\"primary\":\"unset\",\"secondary\":\"X9PzJKityWAFaA5i\"},\"object\":{\"primary\":\"anacron\",\"type\":\"service\"}},\"message_type\":\"service_start\",\"sequence\":12295},\"service\":{\"type\":\"auditd\"},\"ecs\":{\"version\":\"1.11.16bb03ba-2e90-4c98-a5c8-c3d8b8b52c1e\"},\"host\":{\"hostname\":\"LCPmbaxBgGyJj8VH\",\"architecture\":\"x86_64\",\"os\":{\"name\":\"Ubuntu\",\"kernel\":\"4.15.0-161-generic\",\"codename\":\"bionic\",\"type\":\"linux\",\"platform\":\"ubuntu\",\"version\":\"18.04.6 LTS (Bionic Beaver)\",\"family\":\"debian\"},\"name\":\"LCPmbaxBgGyJj8VH\",\"id\":\"7dd912136af040e4a6ea4f683010b824\",\"containerized\":false,\"ip\":[\"87.138.107.154\"],\"mac\":[\"09:d0:5f:99:43:f6\"]},\"agent\":{\"hostname\":\"LCPmbaxBgGyJj8VH\",\"ephemeral_id\":\"f1ac5b09-4f0c-42cf-b9f7-f854eeae073a\",\"id\":\"e9872892-b999-4ad5-83da-d6ec9dbc1f81\",\"name\":\"LCPmbaxBgGyJj8VH\",\"type\":\"auditbeat\",\"version\":\"7.15.1\"}}",
        "sekoiaio": {
            "customer": {
                "id": "c4f66c2f-d5b8-422b-99bb-58861ecf29b2",
                "community_name": "nPBqXTDSBeAay0G4",
                "community_uuid": "9074f2a1-49f9-4b01-9fc7-6c826a330a5a"
            },
            "entity": {
                "id": "6jg8OBtPENQkrAFy",
                "uuid": "3fca9011-7dd8-4a75-a311-9cee8a9daf8a",
                "name": "pW9vnD1tYtahvz1u"
            },
            "intake": {
                "dialect_uuid": "021e9def-5a55-4369-941e-af269b45bef1",
                "parsing_status": "success",
                "dialect": "auditbeat"
            }
        },
        "agent": {
            "id": "e9872892-b999-4ad5-83da-d6ec9dbc1f81",
            "name": "LCPmbaxBgGyJj8VH",
            "type": "auditbeat",
            "ephemeral_id": "f1ac5b09-4f0c-42cf-b9f7-f854eeae073a",
            "version": "7.15.1",
            "hostname": "LCPmbaxBgGyJj8VH"
        },
        "service": {
            "type": "auditd"
        },
        "@timestamp": "2021-11-09T19:02:33.866Z",
        "related": {
            "user": [
                "X9PzJKityWAFaA5i"
            ],
            "hash": [
                "249e78b65ea6378a41037766bd8b1f01abd1a371"
            ],
            "hosts": [
                "LCPmbaxBgGyJj8VH"
            ],
            "ip": [
                "87.138.107.154"
            ]
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
            "sequence": 12295
        },
        "process": {
            "pid": 1,
            "name": "systemd",
            "executable": "/lib/systemd/systemd"
        }
    }
    	
	```


=== "example9.json"

    ```json
	
    {
        "@timestamp": "2021-11-09T16:19:27.788Z",
        "process": {
            "pid": 12416,
            "working_directory": "/home/NElD74Hc4MX8PjLF/Documents/Projets/Qh1HoDnBg4mYfHhi"
        },
        "event": {
            "category": [
                "process"
            ],
            "id": "5a4533a0-1493-4c8c-a77c-c11bcb6dad7c",
            "dialect_uuid": "1b730d40-efc3-4d5d-b2e1-88bec50279b4",
            "kind": "event",
            "module": "auditd",
            "action": "ran-command",
            "type": [
                "start"
            ],
            "outcome": "success",
            "hash": "d0bbb264b6b96f6d62736c1af94d8b83b3b6ad3f",
            "created": "2021-08-20",
            "dialect": "auditbeat"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success",
                "dialect_uuid": "021e9def-5a55-4369-941e-af269b45bef1",
                "dialect": "auditbeat"
            },
            "entity": {
                "id": "Qh1HoDnBg4mYfHhi",
                "uuid": "0b326c92-cdae-4149-818d-7d2e24864eff",
                "name": "3utjzQNc3uN2iAL7"
            },
            "customer": {
                "id": "d5afec27-90be-43b0-8b6a-902b1ae1ee42",
                "community_name": "kBugMo5Or8YMCmmi",
                "community_uuid": "de723233-a1db-4c72-a0a8-3a14df6e9154"
            }
        },
        "message": "{\"@timestamp\":\"2021-11-09T16:17:55.149Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.15.1\"},\"event\":{\"kind\":\"event\",\"type\":[\"start\"],\"module\":\"auditd\",\"category\":[\"process\"],\"action\":\"ran-command\",\"outcome\":\"success\"},\"user\":{\"id\":\"4e8ff660-f139-4248-8b64-ad29495fca9e\",\"name\":\"NElD74Hc4MX8PjLF\",\"audit\":{\"id\":\"4e8ff660-f139-4248-8b64-ad29495fca9e\",\"name\":\"NElD74Hc4MX8PjLF\"}},\"host\":{\"hostname\":\"web-66\",\"architecture\":\"x86_64\",\"os\":{\"type\":\"linux\",\"platform\":\"ubuntu\",\"version\":\"18.04.6 LTS (Bionic Beaver)\",\"family\":\"debian\",\"name\":\"Ubuntu\",\"kernel\":\"4.15.0-161-generic\",\"codename\":\"bionic\"},\"id\":\"7dd912136af040e4a6ea4f683010b824\",\"containerized\":false,\"ip\":[\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\",\"173.8.126.146\"],\"name\":\"web-66\",\"mac\":[\"57:4c:ff:5d:1e:41\",\"57:4c:ff:5d:1e:41\",\"57:4c:ff:5d:1e:41\",\"57:4c:ff:5d:1e:41\",\"57:4c:ff:5d:1e:41\",\"57:4c:ff:5d:1e:41\",\"57:4c:ff:5d:1e:41\",\"57:4c:ff:5d:1e:41\",\"57:4c:ff:5d:1e:41\",\"57:4c:ff:5d:1e:41\",\"57:4c:ff:5d:1e:41\",\"57:4c:ff:5d:1e:41\"]},\"agent\":{\"id\":\"e9872892-b999-4ad5-83da-d6ec9dbc1f81\",\"name\":\"web-66\",\"type\":\"auditbeat\",\"version\":\"7.15.1\",\"hostname\":\"web-66\",\"ephemeral_id\":\"f1ac5b09-4f0c-42cf-b9f7-f854eeae073a\"},\"ecs\":{\"version\":\"1.11.0\"},\"process\":{\"pid\":12416,\"working_directory\":\"/home/NElD74Hc4MX8PjLF/Documents/Projets/Qh1HoDnBg4mYfHhi\"},\"auditd\":{\"data\":{\"terminal\":\"pts/3\",\"cmd\":\"systemctl status auditbeat\"},\"session\":\"2\",\"summary\":{\"actor\":{\"primary\":\"NElD74Hc4MX8PjLF\",\"secondary\":\"NElD74Hc4MX8PjLF\"},\"object\":{\"primary\":\"systemctl status auditbeat\",\"type\":\"process\"}},\"message_type\":\"user_cmd\",\"sequence\":465,\"result\":\"success\"},\"service\":{\"type\":\"auditd\"}}",
        "related": {
            "ip": [
                "173.8.126.146"
            ],
            "hash": [
                "d0bbb264b6b96f6d62736c1af94d8b83b3b6ad3f"
            ],
            "user": [
                "NElD74Hc4MX8PjLF"
            ],
            "hosts": [
                "web-66"
            ]
        },
        "agent": {
            "type": "auditbeat",
            "id": "e9872892-b999-4ad5-83da-d6ec9dbc1f81",
            "name": "web-66",
            "ephemeral_id": "f1ac5b09-4f0c-42cf-b9f7-f854eeae073a",
            "version": "7.15.1",
            "hostname": "web-66"
        },
        "user": {
            "id": "4e8ff660-f139-4248-8b64-ad29495fca9e",
            "name": "NElD74Hc4MX8PjLF",
            "audit": {
                "id": "4e8ff660-f139-4248-8b64-ad29495fca9e",
                "name": "NElD74Hc4MX8PjLF"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "service": {
            "type": "auditd"
        },
        "host": {
            "hostname": "web-66",
            "id": "7dd912136af040e4a6ea4f683010b824",
            "mac": [
                "57:4c:ff:5d:1e:41"
            ],
            "name": "web-66",
            "containerized": false,
            "architecture": "x86_64",
            "ip": [
                "173.8.126.146"
            ],
            "os": {
                "type": "linux",
                "name": "Ubuntu",
                "family": "debian",
                "version": "18.04.6 LTS (Bionic Beaver)",
                "kernel": "4.15.0-161-generic",
                "platform": "ubuntu",
                "codename": "bionic"
            }
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
            "result": "success"
        }
    }
    	
	```


=== "example2.json"

    ```json
	
    {
        "agent": {
            "ephemeral_id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "hostname": "fame",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0"
        },
        "auditbeat": {
            "message": "Process containerd (PID: 1197) by user root is RUNNING"
        },
        "auditd": {
            "user": {
                "saved": {
                    "group": {
                        "id": "0"
                    },
                    "id": "0"
                }
            }
        },
        "event": {
            "action": "existing_process",
            "category": [
                "process"
            ],
            "dataset": "process",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "kind": "state",
            "module": "system",
            "type": [
                "info"
            ]
        },
        "host": {
            "name": "fame"
        },
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"message\":\"Process containerd (PID: 1197) by user root is RUNNING\",\"user\":{\"group\":{\"name\":\"root\",\"id\":\"0\"},\"effective\":{\"id\":\"0\",\"group\":{\"id\":\"0\"}},\"saved\":{\"id\":\"0\",\"group\":{\"id\":\"0\"}},\"name\":\"root\",\"id\":\"0\"},\"ecs\":{\"version\":\"1.9.0\"},\"host\":{\"name\":\"fame\"},\"agent\":{\"hostname\":\"fame\",\"ephemeral_id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"name\":\"fame\",\"type\":\"auditbeat\",\"version\":\"7.13.0\"},\"service\":{\"type\":\"system\"},\"event\":{\"action\":\"existing_process\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"module\":\"system\",\"dataset\":\"process\",\"kind\":\"state\",\"category\":[\"process\"],\"type\":[\"info\"]},\"process\":{\"args\":[\"containerd\"],\"pid\":1197,\"ppid\":1,\"working_directory\":\"/\",\"entity_id\":\"AZERTYqsdfghjklm\",\"name\":\"containerd\",\"executable\":\"/usr/bin/containerd\",\"start\":\"2021-01-01T00:01:01.000Z\",\"hash\":{\"sha1\":\"azertyuiop1234567890\"}, \"command_line\": \"/usr/bin/containerd\"}}",
        "process": {
            "args": [
                "containerd"
            ],
            "entity_id": "AZERTYqsdfghjklm",
            "executable": "/usr/bin/containerd",
            "hash": {
                "sha1": "azertyuiop1234567890"
            },
            "name": "containerd",
            "pid": 1197,
            "ppid": 1,
            "start": "2021-01-01T00:01:01.000Z",
            "working_directory": "/",
            "command_line": "/usr/bin/containerd"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "auditbeat",
                "dialect_uuid": "12345678-azer-1234-a1z2-12qsdfghjklm"
            }
        },
        "service": {
            "type": "system"
        },
        "user": {
            "effective": {
                "group": {
                    "id": "0"
                },
                "id": "0"
            },
            "group": {
                "id": "0",
                "name": "root"
            },
            "id": "0",
            "name": "root"
        }
    }
    	
	```


=== "example1.json"

    ```json
	
    {
        "event": {
            "module": "system",
            "dataset": "process",
            "kind": "event",
            "category": [
                "process"
            ],
            "type": [
                "end"
            ],
            "action": "process_stopped"
        },
        "process": {
            "working_directory": "/my/directory",
            "start": "2021-01-01T00:01:01.000Z",
            "name": "smtp",
            "entity_id": "AZERTY123456789",
            "ppid": 1457,
            "executable": "/usr/lib/postfix/sbin/smtp",
            "pid": 123123,
            "args": [
                "smtp",
                "-t",
                "unix",
                "-u",
                "-c"
            ],
            "command_line": "smtp -t unix -u -c",
            "hash": {
                "sha1": "53fe0c00019fb177e43c7ac214f466f01158384e"
            }
        },
        "auditbeat": {
            "message": "Process smtp (PID: 123123) by user postfix STOPPED"
        },
        "auditd": {
            "user": {
                "saved": {
                    "id": "999",
                    "group": {
                        "id": "222"
                    }
                }
            }
        },
        "user": {
            "effective": {
                "id": "999",
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
        "service": {
            "type": "system"
        },
        "ecs": {
            "version": "1.9.0"
        },
        "host": {
            "name": "fame"
        },
        "agent": {
            "hostname": "fame",
            "ephemeral_id": "qsdfghjklm-1111-2222-3333-azertyuiop",
            "id": "wxcvbn-010101-121212-4444-azertyuiop",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0"
        }
    }
    	
	```


=== "example11.json"

    ```json
	
    {
        "event": {
            "category": [
                "file"
            ],
            "id": "52b3da13-728a-4c7f-8857-ab01774ad49b",
            "outcome": "success",
            "module": "auditd",
            "type": [
                "info"
            ],
            "dialect": "auditbeat",
            "action": "violated-seccomp-policy",
            "hash": "2ca4c1dee00078e88b47ffdc1a0584a43e0fbbb1",
            "kind": "event",
            "created": "2021-04-06",
            "dialect_uuid": "138080ec-6961-43fd-97c2-99ef95a9a1ed"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "host": {
            "mac": [
                "0c:5d:c0:dc:1f:3f"
            ],
            "id": "7dd912136af040e4a6ea4f683010b824",
            "name": "xps-UWWL21LVdEVmqrbT",
            "architecture": "x86_64",
            "containerized": false,
            "os": {
                "type": "linux",
                "family": "debian",
                "name": "Ubuntu",
                "version": "18.04.6 LTS (Bionic Beaver)",
                "kernel": "4.15.0-161-generic",
                "codename": "bionic",
                "platform": "ubuntu"
            },
            "ip": [
                "43.161.42.208"
            ],
            "hostname": "xps-UWWL21LVdEVmqrbT"
        },
        "message": "{\"@timestamp\":\"2021-11-09T19:07:37.325Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.15.1\"},\"event\":{\"outcome\":\"unknown\",\"kind\":\"event\",\"type\":[\"info\"],\"module\":\"auditd\",\"category\":[\"file\"],\"action\":\"violated-seccomp-policy\"},\"user\":{\"id\":\"56d2c11c-9371-4617-bac3-2c18e86042c6\",\"audit\":{\"id\":\"56d2c11c-9371-4617-bac3-2c18e86042c6\",\"name\":\"UWWL21LVdEVmqrbT\"},\"group\":{\"id\":\"56d2c11c-9371-4617-bac3-2c18e86042c6\",\"name\":\"UWWL21LVdEVmqrbT\"},\"name\":\"UWWL21LVdEVmqrbT\"},\"process\":{\"name\":\"ThreadPoolSingl\",\"executable\":\"/opt/google/chrome/chrome\",\"pid\":2720},\"host\":{\"mac\":[\"0c:5d:c0:dc:1f:3f\"],\"hostname\":\"xps-UWWL21LVdEVmqrbT\",\"architecture\":\"x86_64\",\"os\":{\"family\":\"debian\",\"name\":\"Ubuntu\",\"kernel\":\"4.15.0-161-generic\",\"codename\":\"bionic\",\"type\":\"linux\",\"platform\":\"ubuntu\",\"version\":\"18.04.6 LTS (Bionic Beaver)\"},\"id\":\"7dd912136af040e4a6ea4f683010b824\",\"containerized\":false,\"ip\":[\"43.161.42.208\"],\"name\":\"xps-UWWL21LVdEVmqrbT\"},\"agent\":{\"id\":\"e9872892-b999-4ad5-83da-d6ec9dbc1f81\",\"name\":\"xps-UWWL21LVdEVmqrbT\",\"type\":\"auditbeat\",\"version\":\"7.15.1\",\"hostname\":\"xps-UWWL21LVdEVmqrbT\",\"ephemeral_id\":\"f1ac5b09-4f0c-42cf-b9f7-f854eeae073a\"},\"ecs\":{\"version\":\"1.11.0\"},\"auditd\":{\"session\":\"2\",\"summary\":{\"how\":\"/opt/google/chrome/chrome\",\"actor\":{\"primary\":\"UWWL21LVdEVmqrbT\",\"secondary\":\"UWWL21LVdEVmqrbT\"},\"object\":{\"primary\":\"stat\",\"type\":\"process\"}},\"message_type\":\"seccomp\",\"sequence\":12522,\"result\":\"unknown\",\"data\":{\"code\":\"0x50000\",\"syscall\":\"stat\",\"compat\":\"0\",\"ip\":\"0x7fe0a0df1845\",\"arch\":\"x86_64\",\"sig\":\"0\"}},\"service\":{\"type\":\"auditd\"}}",
        "sekoiaio": {
            "entity": {
                "id": "XvCY1OAD5kpZ4aMT",
                "name": "ijcI4rUMLB7FQJUl",
                "uuid": "bee1bd11-f55d-4d9c-a6b2-cd083ef6eb30"
            },
            "customer": {
                "community_name": "IaK78sRooYQr06mu",
                "id": "e8cf9595-d9fd-49d6-814d-a36976e997a9",
                "community_uuid": "4d2ae6d8-87a6-41a9-a9cf-6f6cdb667edc"
            },
            "intake": {
                "dialect": "auditbeat",
                "parsing_status": "success",
                "dialect_uuid": "021e9def-5a55-4369-941e-af269b45bef1"
            }
        },
        "agent": {
            "type": "auditbeat",
            "id": "e9872892-b999-4ad5-83da-d6ec9dbc1f81",
            "name": "xps-UWWL21LVdEVmqrbT",
            "ephemeral_id": "f1ac5b09-4f0c-42cf-b9f7-f854eeae073a",
            "version": "7.15.1",
            "hostname": "xps-UWWL21LVdEVmqrbT"
        },
        "related": {
            "hosts": [
                "xps-UWWL21LVdEVmqrbT"
            ],
            "ip": [
                "43.161.42.208"
            ],
            "user": [
                "UWWL21LVdEVmqrbT"
            ],
            "hash": [
                "2ca4c1dee00078e88b47ffdc1a0584a43e0fbbb1"
            ]
        },
        "user": {
            "id": "56d2c11c-9371-4617-bac3-2c18e86042c6",
            "name": "UWWL21LVdEVmqrbT",
            "audit": {
                "id": "56d2c11c-9371-4617-bac3-2c18e86042c6",
                "name": "UWWL21LVdEVmqrbT"
            },
            "group": {
                "id": "56d2c11c-9371-4617-bac3-2c18e86042c6",
                "name": "UWWL21LVdEVmqrbT"
            }
        },
        "process": {
            "pid": 2720,
            "executable": "/opt/google/chrome/chrome",
            "name": "ThreadPoolSingl"
        },
        "@timestamp": "2021-11-09T19:07:40.601Z",
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
            }
        },
        "service": {
            "type": "auditd"
        }
    }
    	
	```


=== "example6.json"

    ```json
	
    {
        "agent": {
            "ephemeral_id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "hostname": "fame",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0"
        },
        "auditbeat": {
            "message": "Process dbus-daemon (PID: 645) by user messagebus is RUNNING"
        },
        "auditd": {
            "user": {
                "saved": {
                    "group": {
                        "id": "110"
                    },
                    "id": "106"
                }
            }
        },
        "event": {
            "action": "existing_process",
            "category": [
                "process"
            ],
            "dataset": "process",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "kind": "state",
            "module": "system",
            "type": [
                "info"
            ]
        },
        "host": {
            "name": "fame"
        },
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"user\":{\"group\":{\"name\":\"messagebus\",\"id\":\"110\"},\"effective\":{\"id\":\"106\",\"group\":{\"id\":\"110\"}},\"saved\":{\"group\":{\"id\":\"110\"},\"id\":\"106\"},\"name\":\"messagebus\",\"id\":\"106\"},\"ecs\":{\"version\":\"1.9.0\"},\"host\":{\"name\":\"fame\"},\"agent\":{\"hostname\":\"fame\",\"ephemeral_id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"name\":\"fame\",\"type\":\"auditbeat\",\"version\":\"7.13.0\"},\"service\":{\"type\":\"system\"},\"event\":{\"category\":[\"process\"],\"type\":[\"info\"],\"action\":\"existing_process\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"module\":\"system\",\"dataset\":\"process\",\"kind\":\"state\"},\"process\":{\"args\":[\"/usr/bin/dbus-daemon\",\"--system\",\"--address=systemd:\",\"--nofork\",\"--nopidfile\",\"--systemd-activation\",\"--syslog-only\"],\"hash\":{\"sha1\":\"azertyuiop1234567890\"},\"entity_id\":\"azertyuiop\",\"working_directory\":\"/\",\"ppid\":1,\"pid\":645,\"start\":\"2021-01-01T00:01:01.000Z\",\"executable\":\"/usr/bin/dbus-daemon\",\"name\":\"dbus-daemon\"},\"message\":\"Process dbus-daemon (PID: 645) by user messagebus is RUNNING\"}",
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
            "entity_id": "azertyuiop",
            "executable": "/usr/bin/dbus-daemon",
            "hash": {
                "sha1": "azertyuiop1234567890"
            },
            "name": "dbus-daemon",
            "pid": 645,
            "ppid": 1,
            "start": "2021-01-01T00:01:01.000Z",
            "working_directory": "/",
            "command_line": "/usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only"
        },
        "service": {
            "type": "system"
        },
        "user": {
            "effective": {
                "group": {
                    "id": "110"
                },
                "id": "106"
            },
            "group": {
                "id": "110",
                "name": "messagebus"
            },
            "id": "106",
            "name": "messagebus"
        }
    }
    	
	```


=== "example4.json"

    ```json
	
    {
        "agent": {
            "ephemeral_id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "hostname": "fame",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0"
        },
        "auditbeat": {
            "message": "Process postgres (PID: 207706) by user postgres is RUNNING"
        },
        "auditd": {
            "user": {
                "saved": {
                    "group": {
                        "id": "121"
                    },
                    "id": "114"
                }
            }
        },
        "event": {
            "action": "existing_process",
            "category": [
                "process"
            ],
            "dataset": "process",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "kind": "state",
            "module": "system",
            "type": [
                "info"
            ]
        },
        "host": {
            "name": "fame"
        },
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"ecs\":{\"version\":\"1.9.0\"},\"host\":{\"name\":\"fame\"},\"agent\":{\"version\":\"7.13.0\",\"hostname\":\"fame\",\"ephemeral_id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"name\":\"fame\",\"type\":\"auditbeat\"},\"user\":{\"effective\":{\"id\":\"114\",\"group\":{\"id\":\"121\"}},\"saved\":{\"id\":\"114\",\"group\":{\"id\":\"121\"}},\"name\":\"postgres\",\"id\":\"114\",\"group\":{\"name\":\"postgres\",\"id\":\"121\"}},\"service\":{\"type\":\"system\"},\"event\":{\"category\":[\"process\"],\"type\":[\"info\"],\"action\":\"existing_process\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"module\":\"system\",\"dataset\":\"process\",\"kind\":\"state\"},\"process\":{\"executable\":\"/usr/lib/postgresql/9.5/bin/postgres\",\"ppid\":1231,\"start\":\"2021-01-01T00:01:01.000Z\",\"hash\":{\"sha1\":\"azertyuiop1234567890\"},\"name\":\"postgres\",\"args\":[\"postgres: cuckoo cuckoo 127.0.0.1(45786) idle\"],\"entity_id\":\"azertyuiop\",\"working_directory\":\"/var/lib/postgresql/9.5/main\",\"pid\":207706},\"message\":\"Process postgres (PID: 207706) by user postgres is RUNNING\"}",
        "process": {
            "args": [
                "postgres: cuckoo cuckoo 127.0.0.1(45786) idle"
            ],
            "entity_id": "azertyuiop",
            "executable": "/usr/lib/postgresql/9.5/bin/postgres",
            "hash": {
                "sha1": "azertyuiop1234567890"
            },
            "name": "postgres",
            "pid": 207706,
            "ppid": 1231,
            "start": "2021-01-01T00:01:01.000Z",
            "working_directory": "/var/lib/postgresql/9.5/main"
        },
        "service": {
            "type": "system"
        },
        "user": {
            "effective": {
                "group": {
                    "id": "121"
                },
                "id": "114"
            },
            "group": {
                "id": "121",
                "name": "postgres"
            },
            "id": "114",
            "name": "postgres"
        }
    }
    	
	```


=== "example5.json"

    ```json
	
    {
        "agent": {
            "ephemeral_id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "hostname": "fame",
            "id": "12345678-azer-1234-a1z2-12qsdfghjklm",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0"
        },
        "client": {
            "address": "127.0.0.1",
            "bytes": 52,
            "ip": "127.0.0.1",
            "packets": 1,
            "port": 88888
        },
        "destination": {
            "address": "127.0.0.1",
            "bytes": 32,
            "ip": "127.0.0.1",
            "packets": 1,
            "port": 11111
        },
        "event": {
            "action": "network_flow",
            "category": [
                "network",
                "network_traffic"
            ],
            "dataset": "socket",
            "duration": 116168,
            "end": "2021-01-01T00:01:01.000Z",
            "kind": "event",
            "module": "system",
            "start": "2021-01-01T00:01:01.000Z",
            "type": [
                "info",
                "connection"
            ]
        },
        "host": {
            "name": "fame"
        },
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"related\":{\"ip\":[\"127.0.0.1\",\"127.0.0.1\"]},\"service\":{\"type\":\"system\"},\"ecs\":{\"version\":\"1.9.0\"},\"host\":{\"name\":\"fame\"},\"client\":{\"port\":88888,\"packets\":1,\"bytes\":52,\"ip\":\"127.0.0.1\"},\"system\":{\"audit\":{\"socket\":{\"kernel_sock_address\":\"0xffff8e9955b02300\"}}},\"network\":{\"direction\":\"unknown\",\"type\":\"ipv4\",\"transport\":\"tcp\",\"packets\":2,\"bytes\":84,\"community_id\":\"12345678901234567891234567890\"},\"event\":{\"duration\":116168,\"module\":\"system\",\"kind\":\"event\",\"action\":\"network_flow\",\"type\":[\"info\",\"connection\"],\"dataset\":\"socket\",\"end\":\"2021-01-01T00:01:01.000Z\",\"category\":[\"network\",\"network_traffic\"],\"start\":\"2021-01-01T00:01:01.000Z\"},\"flow\":{\"complete\":false,\"final\":true},\"agent\":{\"version\":\"7.13.0\",\"hostname\":\"fame\",\"ephemeral_id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"id\":\"12345678-azer-1234-a1z2-12qsdfghjklm\",\"name\":\"fame\",\"type\":\"auditbeat\"},\"source\":{\"packets\":1,\"bytes\":52,\"ip\":\"127.0.0.1\",\"port\":88888},\"destination\":{\"port\":11111,\"packets\":1,\"bytes\":32,\"ip\":\"127.0.0.1\"},\"server\":{\"ip\":\"127.0.0.1\",\"port\":11111,\"packets\":1,\"bytes\":32}}",
        "network": {
            "bytes": 84,
            "community_id": "12345678901234567891234567890",
            "direction": "unknown",
            "packets": 2,
            "transport": "tcp",
            "type": "ipv4"
        },
        "server": {
            "bytes": 32,
            "ip": "127.0.0.1",
            "packets": 1,
            "port": 11111
        },
        "service": {
            "type": "system"
        },
        "source": {
            "address": "127.0.0.1",
            "bytes": 52,
            "ip": "127.0.0.1",
            "packets": 1,
            "port": 88888
        }
    }
    	
	```


=== "example7.json"

    ```json
	
    {
        "agent": {
            "ephemeral_id": "0101010-abcd-1234-a1b2c3d4e5f6g7h8",
            "hostname": "fame",
            "id": "0101010-abcd-1234-a1b2c3d4e5f6g7h8",
            "name": "fame",
            "type": "auditbeat",
            "version": "7.13.0"
        },
        "auditbeat": {
            "message": "Process postgres (PID: 1234) by user postgres is RUNNING"
        },
        "auditd": {
            "user": {
                "saved": {
                    "group": {
                        "id": "121"
                    },
                    "id": "114"
                }
            }
        },
        "event": {
            "action": "existing_process",
            "category": [
                "process"
            ],
            "dataset": "process",
            "id": "e9c16612-2053-4bc6-86aa-7e04c6114ecc",
            "kind": "state",
            "module": "system",
            "type": [
                "info"
            ]
        },
        "host": {
            "name": "fame"
        },
        "message": "{\"@timestamp\":\"2021-01-01T00:01:01.000Z\",\"@metadata\":{\"beat\":\"auditbeat\",\"type\":\"_doc\",\"version\":\"7.13.0\"},\"service\":{\"type\":\"system\"},\"event\":{\"action\":\"existing_process\",\"id\":\"e9c16612-2053-4bc6-86aa-7e04c6114ecc\",\"module\":\"system\",\"dataset\":\"process\",\"kind\":\"state\",\"category\":[\"process\"],\"type\":[\"info\"]},\"process\":{\"executable\":\"/usr/lib/postgresql/9.5/bin/postgres\",\"entity_id\":\"1234zertyui\",\"ppid\":1231,\"start\":\"2021-01-01T00:01:01.000Z\",\"name\":\"postgres\",\"pid\":1234,\"working_directory\":\"/var/lib/postgresql/9.5/main\",\"hash\":{\"sha1\":\"12345678901234567891234567890\"},\"args\":[\"postgres: wal writer process   \"]},\"host\":{\"name\":\"fame\"},\"agent\":{\"ephemeral_id\":\"0101010-abcd-1234-a1b2c3d4e5f6g7h8\",\"id\":\"0101010-abcd-1234-a1b2c3d4e5f6g7h8\",\"name\":\"fame\",\"type\":\"auditbeat\",\"version\":\"7.13.0\",\"hostname\":\"fame\"},\"ecs\":{\"version\":\"1.9.0\"},\"message\":\"Process postgres (PID: 1234) by user postgres is RUNNING\",\"user\":{\"effective\":{\"group\":{\"id\":\"121\"},\"id\":\"114\"},\"saved\":{\"id\":\"114\",\"group\":{\"id\":\"121\"}},\"name\":\"postgres\",\"id\":\"114\",\"group\":{\"id\":\"121\",\"name\":\"postgres\"}}}",
        "process": {
            "args": [
                "postgres: wal writer process   "
            ],
            "entity_id": "1234zertyui",
            "executable": "/usr/lib/postgresql/9.5/bin/postgres",
            "hash": {
                "sha1": "12345678901234567891234567890"
            },
            "name": "postgres",
            "pid": 1234,
            "ppid": 1231,
            "start": "2021-01-01T00:01:01.000Z",
            "working_directory": "/var/lib/postgresql/9.5/main"
        },
        "service": {
            "type": "system"
        },
        "user": {
            "effective": {
                "group": {
                    "id": "121"
                },
                "id": "114"
            },
            "group": {
                "id": "121",
                "name": "postgres"
            },
            "id": "114",
            "name": "postgres"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`agent.build.original` | `keyword` | Extended build information for the agent. |
|`agent.ephemeral_id` | `keyword` | Ephemeral identifier of this agent. |
|`agent.hostname` | `keyword` | None |
|`agent.id` | `keyword` | Unique identifier of this agent. |
|`agent.name` | `keyword` | Custom name of the agent. |
|`agent.type` | `keyword` | Type of the agent. |
|`agent.version` | `keyword` | Version of the agent. |
|`as.number` | `long` | None |
|`as.organization.name` | `keyword` | None |
|`as.organization.name.text` | `text` | None |
|`auditbeat.event.original` | `keyword` | None |
|`auditbeat.labels` | `text` | None |
|`auditbeat.message` | `text` | None |
|`auditbeat.tags` | `text` | None |
|`auditbeat.timezone` | `keyword` | None |
|`auditd.data.a0` | `keyword` | None |
|`auditd.data.a1` | `keyword` | None |
|`auditd.data.a2` | `keyword` | None |
|`auditd.data.a3` | `keyword` | None |
|`auditd.data.a[0-3]` | `keyword` | None |
|`auditd.data.acct` | `keyword` | None |
|`auditd.data.acl` | `keyword` | None |
|`auditd.data.action` | `keyword` | None |
|`auditd.data.added` | `keyword` | None |
|`auditd.data.addr` | `keyword` | None |
|`auditd.data.apparmor` | `keyword` | None |
|`auditd.data.arch` | `keyword` | None |
|`auditd.data.argc` | `keyword` | None |
|`auditd.data.audit_backlog_limit` | `keyword` | None |
|`auditd.data.audit_backlog_wait_time` | `keyword` | None |
|`auditd.data.audit_enabled` | `keyword` | None |
|`auditd.data.audit_failure` | `keyword` | None |
|`auditd.data.banners` | `keyword` | None |
|`auditd.data.bool` | `keyword` | None |
|`auditd.data.bus` | `keyword` | None |
|`auditd.data.cap_fe` | `keyword` | None |
|`auditd.data.cap_fi` | `keyword` | None |
|`auditd.data.cap_fp` | `keyword` | None |
|`auditd.data.cap_fver` | `keyword` | None |
|`auditd.data.cap_pe` | `keyword` | None |
|`auditd.data.cap_pi` | `keyword` | None |
|`auditd.data.cap_pp` | `keyword` | None |
|`auditd.data.capability` | `keyword` | None |
|`auditd.data.cgroup` | `keyword` | None |
|`auditd.data.changed` | `keyword` | None |
|`auditd.data.cipher` | `keyword` | None |
|`auditd.data.class` | `keyword` | None |
|`auditd.data.cmd` | `keyword` | None |
|`auditd.data.code` | `keyword` | None |
|`auditd.data.compat` | `keyword` | None |
|`auditd.data.daddr` | `keyword` | None |
|`auditd.data.data` | `keyword` | None |
|`auditd.data.default-context` | `keyword` | None |
|`auditd.data.device` | `keyword` | None |
|`auditd.data.dir` | `keyword` | None |
|`auditd.data.direction` | `keyword` | None |
|`auditd.data.dmac` | `keyword` | None |
|`auditd.data.dport` | `keyword` | None |
|`auditd.data.enforcing` | `keyword` | None |
|`auditd.data.entries` | `keyword` | None |
|`auditd.data.exit` | `keyword` | None |
|`auditd.data.fam` | `keyword` | None |
|`auditd.data.family` | `keyword` | None |
|`auditd.data.fd` | `keyword` | None |
|`auditd.data.fe` | `keyword` | None |
|`auditd.data.feature` | `keyword` | None |
|`auditd.data.fi` | `keyword` | None |
|`auditd.data.file` | `keyword` | None |
|`auditd.data.flags` | `keyword` | None |
|`auditd.data.format` | `keyword` | None |
|`auditd.data.fp` | `keyword` | None |
|`auditd.data.fver` | `keyword` | None |
|`auditd.data.grantors` | `keyword` | None |
|`auditd.data.grp` | `keyword` | None |
|`auditd.data.hook` | `keyword` | None |
|`auditd.data.hostname` | `keyword` | None |
|`auditd.data.icmp_type` | `keyword` | None |
|`auditd.data.id` | `keyword` | None |
|`auditd.data.igid` | `keyword` | None |
|`auditd.data.img-ctx` | `keyword` | None |
|`auditd.data.inif` | `keyword` | None |
|`auditd.data.ino` | `keyword` | None |
|`auditd.data.inode_gid` | `keyword` | None |
|`auditd.data.inode_uid` | `keyword` | None |
|`auditd.data.invalid_context` | `keyword` | None |
|`auditd.data.ioctlcmd` | `keyword` | None |
|`auditd.data.ip` | `keyword` | None |
|`auditd.data.ipid` | `keyword` | None |
|`auditd.data.ipx-net` | `keyword` | None |
|`auditd.data.items` | `keyword` | None |
|`auditd.data.iuid` | `keyword` | None |
|`auditd.data.kernel` | `keyword` | None |
|`auditd.data.kind` | `keyword` | None |
|`auditd.data.ksize` | `keyword` | None |
|`auditd.data.laddr` | `keyword` | None |
|`auditd.data.len` | `keyword` | None |
|`auditd.data.list` | `keyword` | None |
|`auditd.data.lport` | `keyword` | None |
|`auditd.data.mac` | `keyword` | None |
|`auditd.data.macproto` | `keyword` | None |
|`auditd.data.maj` | `keyword` | None |
|`auditd.data.major` | `keyword` | None |
|`auditd.data.minor` | `keyword` | None |
|`auditd.data.model` | `keyword` | None |
|`auditd.data.msg` | `keyword` | None |
|`auditd.data.nargs` | `keyword` | None |
|`auditd.data.net` | `keyword` | None |
|`auditd.data.new` | `keyword` | None |
|`auditd.data.new-chardev` | `keyword` | None |
|`auditd.data.new-disk` | `keyword` | None |
|`auditd.data.new-enabled` | `keyword` | None |
|`auditd.data.new-fs` | `keyword` | None |
|`auditd.data.new-level` | `keyword` | None |
|`auditd.data.new-log_passwd` | `keyword` | None |
|`auditd.data.new-mem` | `keyword` | None |
|`auditd.data.new-net` | `keyword` | None |
|`auditd.data.new-range` | `keyword` | None |
|`auditd.data.new-rng` | `keyword` | None |
|`auditd.data.new-role` | `keyword` | None |
|`auditd.data.new-seuser` | `keyword` | None |
|`auditd.data.new-vcpu` | `keyword` | None |
|`auditd.data.new_gid` | `keyword` | None |
|`auditd.data.new_lock` | `keyword` | None |
|`auditd.data.new_pe` | `keyword` | None |
|`auditd.data.new_pi` | `keyword` | None |
|`auditd.data.new_pp` | `keyword` | None |
|`auditd.data.nlnk-fam` | `keyword` | None |
|`auditd.data.nlnk-grp` | `keyword` | None |
|`auditd.data.nlnk-pid` | `keyword` | None |
|`auditd.data.oauid` | `keyword` | None |
|`auditd.data.obj` | `keyword` | None |
|`auditd.data.obj_gid` | `keyword` | None |
|`auditd.data.obj_uid` | `keyword` | None |
|`auditd.data.ocomm` | `keyword` | None |
|`auditd.data.oflag` | `keyword` | None |
|`auditd.data.old` | `keyword` | None |
|`auditd.data.old-auid` | `keyword` | None |
|`auditd.data.old-chardev` | `keyword` | None |
|`auditd.data.old-disk` | `keyword` | None |
|`auditd.data.old-enabled` | `keyword` | None |
|`auditd.data.old-fs` | `keyword` | None |
|`auditd.data.old-level` | `keyword` | None |
|`auditd.data.old-log_passwd` | `keyword` | None |
|`auditd.data.old-mem` | `keyword` | None |
|`auditd.data.old-net` | `keyword` | None |
|`auditd.data.old-range` | `keyword` | None |
|`auditd.data.old-rng` | `keyword` | None |
|`auditd.data.old-role` | `keyword` | None |
|`auditd.data.old-ses` | `keyword` | None |
|`auditd.data.old-seuser` | `keyword` | None |
|`auditd.data.old-vcpu` | `keyword` | None |
|`auditd.data.old_enforcing` | `keyword` | None |
|`auditd.data.old_lock` | `keyword` | None |
|`auditd.data.old_pe` | `keyword` | None |
|`auditd.data.old_pi` | `keyword` | None |
|`auditd.data.old_pp` | `keyword` | None |
|`auditd.data.old_prom` | `keyword` | None |
|`auditd.data.old_val` | `keyword` | None |
|`auditd.data.op` | `keyword` | None |
|`auditd.data.opid` | `keyword` | None |
|`auditd.data.oses` | `keyword` | None |
|`auditd.data.outif` | `keyword` | None |
|`auditd.data.parent` | `keyword` | None |
|`auditd.data.per` | `keyword` | None |
|`auditd.data.perm` | `keyword` | None |
|`auditd.data.perm_mask` | `keyword` | None |
|`auditd.data.permissive` | `keyword` | None |
|`auditd.data.pfs` | `keyword` | None |
|`auditd.data.printer` | `keyword` | None |
|`auditd.data.prom` | `keyword` | None |
|`auditd.data.proto` | `keyword` | None |
|`auditd.data.qbytes` | `keyword` | None |
|`auditd.data.range` | `keyword` | None |
|`auditd.data.reason` | `keyword` | None |
|`auditd.data.removed` | `keyword` | None |
|`auditd.data.res` | `keyword` | None |
|`auditd.data.resrc` | `keyword` | None |
|`auditd.data.rport` | `keyword` | None |
|`auditd.data.sauid` | `keyword` | None |
|`auditd.data.scontext` | `keyword` | None |
|`auditd.data.selected-context` | `keyword` | None |
|`auditd.data.seperm` | `keyword` | None |
|`auditd.data.seperms` | `keyword` | None |
|`auditd.data.seqno` | `keyword` | None |
|`auditd.data.seresult` | `keyword` | None |
|`auditd.data.ses` | `keyword` | None |
|`auditd.data.seuser` | `keyword` | None |
|`auditd.data.sig` | `keyword` | None |
|`auditd.data.sigev_signo` | `keyword` | None |
|`auditd.data.smac` | `keyword` | None |
|`auditd.data.socket.addr` | `keyword` | None |
|`auditd.data.socket.family` | `keyword` | None |
|`auditd.data.socket.path` | `keyword` | None |
|`auditd.data.socket.port` | `keyword` | None |
|`auditd.data.socket.saddr` | `keyword` | None |
|`auditd.data.spid` | `keyword` | None |
|`auditd.data.sport` | `keyword` | None |
|`auditd.data.state` | `keyword` | None |
|`auditd.data.subj` | `keyword` | None |
|`auditd.data.success` | `keyword` | None |
|`auditd.data.syscall` | `keyword` | None |
|`auditd.data.table` | `keyword` | None |
|`auditd.data.tclass` | `keyword` | None |
|`auditd.data.tcontext` | `keyword` | None |
|`auditd.data.terminal` | `keyword` | None |
|`auditd.data.tty` | `keyword` | None |
|`auditd.data.unit` | `keyword` | None |
|`auditd.data.uri` | `keyword` | None |
|`auditd.data.uuid` | `keyword` | None |
|`auditd.data.val` | `keyword` | None |
|`auditd.data.ver` | `keyword` | None |
|`auditd.data.virt` | `keyword` | None |
|`auditd.data.vm` | `keyword` | None |
|`auditd.data.vm-ctx` | `keyword` | None |
|`auditd.data.vm-pid` | `keyword` | None |
|`auditd.data.watch` | `keyword` | None |
|`auditd.message_type` | `keyword` | None |
|`auditd.paths` | `nested` | None |
|`auditd.result` | `keyword` | None |
|`auditd.sequence` | `long` | None |
|`auditd.session` | `keyword` | None |
|`auditd.summary.actor.primary` | `keyword` | None |
|`auditd.summary.actor.secondary` | `keyword` | None |
|`auditd.summary.how` | `keyword` | None |
|`auditd.summary.object.primary` | `keyword` | None |
|`auditd.summary.object.secondary` | `keyword` | None |
|`auditd.summary.object.type` | `keyword` | None |
|`auditd.user.saved.group.id` | `keyword` | None |
|`auditd.user.saved.group.name` | `keyword` | None |
|`auditd.user.saved.id` | `keyword` | None |
|`auditd.user.saved.name` | `keyword` | None |
|`client.address` | `keyword` | Client network address. |
|`client.as.number` | `long` | Unique number allocated to the autonomous system. |
|`client.as.organization.name` | `keyword` | Organization name. |
|`client.as.organization.name.text` | `text` | None |
|`client.bytes` | `long` | Bytes sent from the client to the server. |
|`client.domain` | `keyword` | The domain name of the client. |
|`client.geo.city_name` | `keyword` | City name. |
|`client.geo.continent_code` | `keyword` | Continent code. |
|`client.geo.continent_name` | `keyword` | Name of the continent. |
|`client.geo.country_iso_code` | `keyword` | Country ISO code. |
|`client.geo.country_name` | `keyword` | Country name. |
|`client.geo.location` | `geo_point` | Longitude and latitude. |
|`client.geo.name` | `keyword` | User-defined description of a location. |
|`client.geo.postal_code` | `keyword` | Postal code. |
|`client.geo.region_iso_code` | `keyword` | Region ISO code. |
|`client.geo.region_name` | `keyword` | Region name. |
|`client.geo.timezone` | `keyword` | Time zone. |
|`client.ip` | `ip` | IP address of the client. |
|`client.mac` | `keyword` | MAC address of the client. |
|`client.nat.ip` | `ip` | Client NAT ip address |
|`client.nat.port` | `long` | Client NAT port |
|`client.packets` | `long` | Packets sent from the client to the server. |
|`client.port` | `long` | Port of the client. |
|`client.registered_domain` | `keyword` | The highest registered client domain, stripped of the subdomain. |
|`client.subdomain` | `keyword` | The subdomain of the domain. |
|`client.top_level_domain` | `keyword` | The effective top level domain (com, org, net, co.uk). |
|`client.user.domain` | `keyword` | Name of the directory the user is a member of. |
|`client.user.email` | `keyword` | User email address. |
|`client.user.full_name` | `keyword` | User's full name, if available. |
|`client.user.full_name.text` | `text` | None |
|`client.user.group.domain` | `keyword` | Name of the directory the group is a member of. |
|`client.user.group.id` | `keyword` | Unique identifier for the group on the system/platform. |
|`client.user.group.name` | `keyword` | Name of the group. |
|`client.user.hash` | `keyword` | Unique user hash to correlate information for a user in anonymized form. |
|`client.user.id` | `keyword` | Unique identifier of the user. |
|`client.user.name` | `keyword` | Short name or login of the user. |
|`client.user.name.text` | `text` | None |
|`client.user.roles` | `keyword` | Array of user roles at the time of the event. |
|`cloud.account.id` | `keyword` | The cloud account or organization id. |
|`cloud.account.name` | `keyword` | The cloud account name. |
|`cloud.availability_zone` | `keyword` | Availability zone in which this host, resource, or service is located. |
|`cloud.image.id` | `keyword` | None |
|`cloud.instance.id` | `keyword` | Instance ID of the host machine. |
|`cloud.instance.name` | `keyword` | Instance name of the host machine. |
|`cloud.machine.type` | `keyword` | Machine type of the host machine. |
|`cloud.project.id` | `keyword` | The cloud project id. |
|`cloud.project.name` | `keyword` | The cloud project name. |
|`cloud.provider` | `keyword` | Name of the cloud provider. |
|`cloud.region` | `keyword` | Region in which this host, resource, or service is located. |
|`cloud.service.name` | `keyword` | The cloud service name. |
|`code_signature.exists` | `boolean` | None |
|`code_signature.signing_id` | `keyword` | None |
|`code_signature.status` | `keyword` | None |
|`code_signature.subject_name` | `keyword` | None |
|`code_signature.team_id` | `keyword` | None |
|`code_signature.trusted` | `boolean` | None |
|`code_signature.valid` | `boolean` | None |
|`container.id` | `keyword` | Unique container id. |
|`container.image.name` | `keyword` | Name of the image the container was built on. |
|`container.image.tag` | `keyword` | Container image tags. |
|`container.labels` | `object` | Image labels. |
|`container.name` | `keyword` | Container name. |
|`container.runtime` | `keyword` | Runtime managing this container. |
|`data_stream.dataset` | `constant_keyword` | The field can contain anything that makes sense to signify the source of the data. |
|`data_stream.namespace` | `constant_keyword` | A user defined namespace. Namespaces are useful to allow grouping of data. |
|`data_stream.type` | `constant_keyword` | An overarching type for the data stream. |
|`destination.address` | `keyword` | Destination network address. |
|`destination.as.number` | `long` | Unique number allocated to the autonomous system. |
|`destination.as.organization.name` | `keyword` | Organization name. |
|`destination.as.organization.name.text` | `text` | None |
|`destination.bytes` | `long` | Bytes sent from the destination to the source. |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.geo.city_name` | `keyword` | City name. |
|`destination.geo.continent_code` | `keyword` | Continent code. |
|`destination.geo.continent_name` | `keyword` | Name of the continent. |
|`destination.geo.country_iso_code` | `keyword` | Country ISO code. |
|`destination.geo.country_name` | `keyword` | Country name. |
|`destination.geo.location` | `geo_point` | Longitude and latitude. |
|`destination.geo.name` | `keyword` | User-defined description of a location. |
|`destination.geo.postal_code` | `keyword` | Postal code. |
|`destination.geo.region_iso_code` | `keyword` | Region ISO code. |
|`destination.geo.region_name` | `keyword` | Region name. |
|`destination.geo.timezone` | `keyword` | Time zone. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.mac` | `keyword` | MAC address of the destination. |
|`destination.nat.ip` | `ip` | Destination NAT ip |
|`destination.nat.port` | `long` | Destination NAT Port |
|`destination.packets` | `long` | Packets sent from the destination to the source. |
|`destination.path` | `keyword` | None |
|`destination.port` | `long` | Port of the destination. |
|`destination.registered_domain` | `keyword` | The highest registered destination domain, stripped of the subdomain. |
|`destination.subdomain` | `keyword` | The subdomain of the domain. |
|`destination.top_level_domain` | `keyword` | The effective top level domain (com, org, net, co.uk). |
|`destination.user.domain` | `keyword` | Name of the directory the user is a member of. |
|`destination.user.email` | `keyword` | User email address. |
|`destination.user.full_name` | `keyword` | User's full name, if available. |
|`destination.user.full_name.text` | `text` | None |
|`destination.user.group.domain` | `keyword` | Name of the directory the group is a member of. |
|`destination.user.group.id` | `keyword` | Unique identifier for the group on the system/platform. |
|`destination.user.group.name` | `keyword` | Name of the group. |
|`destination.user.hash` | `keyword` | Unique user hash to correlate information for a user in anonymized form. |
|`destination.user.id` | `keyword` | Unique identifier of the user. |
|`destination.user.name` | `keyword` | Short name or login of the user. |
|`destination.user.name.text` | `text` | None |
|`destination.user.roles` | `keyword` | Array of user roles at the time of the event. |
|`dll.code_signature.exists` | `boolean` | Boolean to capture if a signature is present. |
|`dll.code_signature.signing_id` | `keyword` | The identifier used to sign the process. |
|`dll.code_signature.status` | `keyword` | Additional information about the certificate status. |
|`dll.code_signature.subject_name` | `keyword` | Subject name of the code signer |
|`dll.code_signature.team_id` | `keyword` | The team identifier used to sign the process. |
|`dll.code_signature.trusted` | `boolean` | Stores the trust status of the certificate chain. |
|`dll.code_signature.valid` | `boolean` | Boolean to capture if the digital signature is verified against the binary content. |
|`dll.hash.md5` | `keyword` | MD5 hash. |
|`dll.hash.sha1` | `keyword` | SHA1 hash. |
|`dll.hash.sha256` | `keyword` | SHA256 hash. |
|`dll.hash.sha512` | `keyword` | SHA512 hash. |
|`dll.hash.ssdeep` | `keyword` | SSDEEP hash. |
|`dll.name` | `keyword` | Name of the library. |
|`dll.path` | `keyword` | Full file path of the library. |
|`dll.pe.architecture` | `keyword` | CPU architecture target for the file. |
|`dll.pe.company` | `keyword` | Internal company name of the file, provided at compile-time. |
|`dll.pe.description` | `keyword` | Internal description of the file, provided at compile-time. |
|`dll.pe.file_version` | `keyword` | Process name. |
|`dll.pe.imphash` | `keyword` | A hash of the imports in a PE file. |
|`dll.pe.original_file_name` | `keyword` | Internal name of the file, provided at compile-time. |
|`dll.pe.product` | `keyword` | Internal product name of the file, provided at compile-time. |
|`dns.answers` | `object` | Array of DNS answers. |
|`dns.answers.class` | `keyword` | The class of DNS data contained in this resource record. |
|`dns.answers.data` | `keyword` | The data describing the resource. |
|`dns.answers.name` | `keyword` | The domain name to which this resource record pertains. |
|`dns.answers.ttl` | `long` | The time interval in seconds that this resource record may be cached before it should be discarded. |
|`dns.answers.type` | `keyword` | The type of data contained in this resource record. |
|`dns.header_flags` | `keyword` | Array of DNS header flags. |
|`dns.id` | `keyword` | The DNS packet identifier assigned by the program that generated the query. The identifier is copied to the response. |
|`dns.op_code` | `keyword` | The DNS operation code that specifies the kind of query in the message. |
|`dns.question.class` | `keyword` | The class of records being queried. |
|`dns.question.name` | `keyword` | The name being queried. |
|`dns.question.registered_domain` | `keyword` | The highest registered domain, stripped of the subdomain. |
|`dns.question.subdomain` | `keyword` | The subdomain of the domain. |
|`dns.question.top_level_domain` | `keyword` | The effective top level domain (com, org, net, co.uk). |
|`dns.question.type` | `keyword` | The type of record being queried. |
|`dns.resolved_ip` | `ip` | Array containing all IPs seen in answers.data |
|`dns.response_code` | `keyword` | The DNS response code. |
|`dns.type` | `keyword` | The type of DNS event captured, query or answer. |
|`docker.container.labels` | `object` | None |
|`ecs.version` | `keyword` | ECS version this event conforms to. |
|`error.code` | `keyword` | Error code describing the error. |
|`error.id` | `keyword` | Unique identifier for the error. |
|`error.message` | `match_only_text` | Error message. |
|`error.stack_trace` | `wildcard` | The stack trace of this error in plain text. |
|`error.stack_trace.text` | `text` | None |
|`error.type` | `keyword` | The type of the error, for example the class name of the exception. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.created` | `date` | Time when the event was first read by an agent or by your pipeline. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.duration` | `long` | Duration of the event in nanoseconds. |
|`event.end` | `date` | event.end contains the date when the event ended or when the activity was last observed. |
|`event.hash` | `keyword` | Hash (perhaps logstash fingerprint) of raw field to be able to demonstrate log integrity. |
|`event.id` | `keyword` | Unique ID to describe the event. |
|`event.ingested` | `date` | Timestamp when an event arrived in the central data store. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.module` | `keyword` | Name of the module this data is coming from. |
|`event.origin` | `keyword` | None |
|`event.original` | `keyword` | Raw text message of entire event. |
|`event.outcome` | `keyword` | The outcome of the event. The lowest level categorization field in the hierarchy. |
|`event.provider` | `keyword` | Source of the event. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.reference` | `keyword` | Event reference URL |
|`event.risk_score` | `float` | Risk score or priority of the event (e.g. security solutions). Use your system's original value here. |
|`event.risk_score_norm` | `float` | Normalized risk score or priority of the event (0-100). |
|`event.sequence` | `long` | Sequence number of the event. |
|`event.severity` | `long` | Numeric severity of the event. |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`event.timezone` | `keyword` | Event time zone. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`event.url` | `keyword` | Event investigation URL |
|`fields` | `object` | None |
|`file.accessed` | `date` | Last time the file was accessed. |
|`file.attributes` | `keyword` | Array of file attributes. |
|`file.code_signature.exists` | `boolean` | Boolean to capture if a signature is present. |
|`file.code_signature.signing_id` | `keyword` | The identifier used to sign the process. |
|`file.code_signature.status` | `keyword` | Additional information about the certificate status. |
|`file.code_signature.subject_name` | `keyword` | Subject name of the code signer |
|`file.code_signature.team_id` | `keyword` | The team identifier used to sign the process. |
|`file.code_signature.trusted` | `boolean` | Stores the trust status of the certificate chain. |
|`file.code_signature.valid` | `boolean` | Boolean to capture if the digital signature is verified against the binary content. |
|`file.created` | `date` | File creation time. |
|`file.ctime` | `date` | Last time the file attributes or metadata changed. |
|`file.device` | `keyword` | Device that is the source of the file. |
|`file.directory` | `keyword` | Directory where the file is located. |
|`file.drive_letter` | `keyword` | Drive letter where the file is located. |
|`file.extension` | `keyword` | File extension, excluding the leading dot. |
|`file.gid` | `keyword` | Primary group ID (GID) of the file. |
|`file.group` | `keyword` | Primary group name of the file. |
|`file.hash.md5` | `keyword` | MD5 hash. |
|`file.hash.sha1` | `keyword` | SHA1 hash. |
|`file.hash.sha256` | `keyword` | SHA256 hash. |
|`file.hash.sha512` | `keyword` | SHA512 hash. |
|`file.hash.ssdeep` | `keyword` | SSDEEP hash. |
|`file.inode` | `keyword` | Inode representing the file in the filesystem. |
|`file.mime_type` | `keyword` | Media type of file, document, or arrangement of bytes. |
|`file.mode` | `keyword` | Mode of the file in octal representation. |
|`file.mtime` | `date` | Last time the file content was modified. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.origin` | `keyword` | None |
|`file.origin.text` | `text` | None |
|`file.owner` | `keyword` | File owner's username. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`file.path.text` | `text` | None |
|`file.pe.architecture` | `keyword` | CPU architecture target for the file. |
|`file.pe.company` | `keyword` | Internal company name of the file, provided at compile-time. |
|`file.pe.description` | `keyword` | Internal description of the file, provided at compile-time. |
|`file.pe.file_version` | `keyword` | Process name. |
|`file.pe.imphash` | `keyword` | A hash of the imports in a PE file. |
|`file.pe.original_file_name` | `keyword` | Internal name of the file, provided at compile-time. |
|`file.pe.product` | `keyword` | Internal product name of the file, provided at compile-time. |
|`file.selinux.domain` | `keyword` | None |
|`file.selinux.level` | `keyword` | None |
|`file.selinux.role` | `keyword` | None |
|`file.selinux.user` | `keyword` | None |
|`file.setgid` | `boolean` | None |
|`file.setuid` | `boolean` | None |
|`file.size` | `long` | File size in bytes. |
|`file.target_path` | `keyword` | Target path for symlinks. |
|`file.target_path.text` | `text` | None |
|`file.type` | `keyword` | File type (file, dir, or symlink). |
|`file.uid` | `keyword` | The user ID (UID) or security identifier (SID) of the file owner. |
|`file.x509.alternative_names` | `keyword` | List of subject alternative names (SAN). |
|`file.x509.issuer.common_name` | `keyword` | List of common name (CN) of issuing certificate authority. |
|`file.x509.issuer.country` | `keyword` | List of country (C) codes |
|`file.x509.issuer.distinguished_name` | `keyword` | Distinguished name (DN) of issuing certificate authority. |
|`file.x509.issuer.locality` | `keyword` | List of locality names (L) |
|`file.x509.issuer.organization` | `keyword` | List of organizations (O) of issuing certificate authority. |
|`file.x509.issuer.organizational_unit` | `keyword` | List of organizational units (OU) of issuing certificate authority. |
|`file.x509.issuer.state_or_province` | `keyword` | List of state or province names (ST, S, or P) |
|`file.x509.not_after` | `date` | Time at which the certificate is no longer considered valid. |
|`file.x509.not_before` | `date` | Time at which the certificate is first considered valid. |
|`file.x509.public_key_algorithm` | `keyword` | Algorithm used to generate the public key. |
|`file.x509.public_key_curve` | `keyword` | The curve used by the elliptic curve public key algorithm. This is algorithm specific. |
|`file.x509.public_key_exponent` | `long` | Exponent used to derive the public key. This is algorithm specific. |
|`file.x509.public_key_size` | `long` | The size of the public key space in bits. |
|`file.x509.serial_number` | `keyword` | Unique serial number issued by the certificate authority. |
|`file.x509.signature_algorithm` | `keyword` | Identifier for certificate signature algorithm. |
|`file.x509.subject.common_name` | `keyword` | List of common names (CN) of subject. |
|`file.x509.subject.country` | `keyword` | List of country (C) code |
|`file.x509.subject.distinguished_name` | `keyword` | Distinguished name (DN) of the certificate subject entity. |
|`file.x509.subject.locality` | `keyword` | List of locality names (L) |
|`file.x509.subject.organization` | `keyword` | List of organizations (O) of subject. |
|`file.x509.subject.organizational_unit` | `keyword` | List of organizational units (OU) of subject. |
|`file.x509.subject.state_or_province` | `keyword` | List of state or province names (ST, S, or P) |
|`file.x509.version_number` | `keyword` | Version of x509 format. |
|`geo.city_name` | `keyword` | None |
|`geo.continent_code` | `keyword` | None |
|`geo.continent_name` | `keyword` | None |
|`geo.country_iso_code` | `keyword` | None |
|`geo.country_name` | `keyword` | None |
|`geo.location` | `geo_point` | None |
|`geo.name` | `keyword` | None |
|`geo.postal_code` | `keyword` | None |
|`geo.region_iso_code` | `keyword` | None |
|`geo.region_name` | `keyword` | None |
|`geo.timezone` | `keyword` | None |
|`geoip.city_name` | `keyword` | None |
|`geoip.continent_name` | `keyword` | None |
|`geoip.country_iso_code` | `keyword` | None |
|`geoip.location` | `geo_point` | None |
|`geoip.region_name` | `keyword` | None |
|`group.domain` | `keyword` | Name of the directory the group is a member of. |
|`group.id` | `keyword` | Unique identifier for the group on the system/platform. |
|`group.name` | `keyword` | Name of the group. |
|`hash.blake2b_256` | `keyword` | None |
|`hash.blake2b_384` | `keyword` | None |
|`hash.blake2b_512` | `keyword` | None |
|`hash.md5` | `keyword` | None |
|`hash.sha1` | `keyword` | None |
|`hash.sha224` | `keyword` | None |
|`hash.sha256` | `keyword` | None |
|`hash.sha384` | `keyword` | None |
|`hash.sha3_224` | `keyword` | None |
|`hash.sha3_256` | `keyword` | None |
|`hash.sha3_384` | `keyword` | None |
|`hash.sha3_512` | `keyword` | None |
|`hash.sha512` | `keyword` | None |
|`hash.sha512_224` | `keyword` | None |
|`hash.sha512_256` | `keyword` | None |
|`hash.ssdeep` | `keyword` | None |
|`hash.xxh64` | `keyword` | None |
|`host.architecture` | `keyword` | Operating system architecture. |
|`host.containerized` | `boolean` | None |
|`host.cpu.usage` | `scaled_float` | Percent CPU used, between 0 and 1. |
|`host.disk.read.bytes` | `long` | The number of bytes read by all disks. |
|`host.disk.write.bytes` | `long` | The number of bytes written on all disks. |
|`host.domain` | `keyword` | Name of the directory the group is a member of. |
|`host.geo.city_name` | `keyword` | City name. |
|`host.geo.continent_code` | `keyword` | Continent code. |
|`host.geo.continent_name` | `keyword` | Name of the continent. |
|`host.geo.country_iso_code` | `keyword` | Country ISO code. |
|`host.geo.country_name` | `keyword` | Country name. |
|`host.geo.location` | `geo_point` | Longitude and latitude. |
|`host.geo.name` | `keyword` | User-defined description of a location. |
|`host.geo.postal_code` | `keyword` | Postal code. |
|`host.geo.region_iso_code` | `keyword` | Region ISO code. |
|`host.geo.region_name` | `keyword` | Region name. |
|`host.geo.timezone` | `keyword` | Time zone. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.id` | `keyword` | Unique host id. |
|`host.ip` | `ip` | Host ip addresses. |
|`host.mac` | `keyword` | Host MAC addresses. |
|`host.name` | `keyword` | Name of the host. |
|`host.network.egress.bytes` | `long` | The number of bytes sent on all network interfaces. |
|`host.network.egress.packets` | `long` | The number of packets sent on all network interfaces. |
|`host.network.ingress.bytes` | `long` | The number of bytes received on all network interfaces. |
|`host.network.ingress.packets` | `long` | The number of packets received on all network interfaces. |
|`host.os.build` | `keyword` | None |
|`host.os.codename` | `keyword` | None |
|`host.os.family` | `keyword` | OS family (such as redhat, debian, freebsd, windows). |
|`host.os.full` | `keyword` | Operating system name, including the version or code name. |
|`host.os.full.text` | `text` | None |
|`host.os.kernel` | `keyword` | Operating system kernel version as a raw string. |
|`host.os.name` | `keyword` | Operating system name, without the version. |
|`host.os.name.text` | `text` | None |
|`host.os.platform` | `keyword` | Operating system platform (such centos, ubuntu, windows). |
|`host.os.type` | `keyword` | Which commercial OS family (one of: linux, macos, unix or windows). |
|`host.os.version` | `keyword` | Operating system version as a raw string. |
|`host.type` | `keyword` | Type of host. |
|`host.uptime` | `long` | Seconds the host has been up. |
|`host.user.full_name.text` | `text` | None |
|`host.user.name.text` | `text` | None |
|`http.request.body.bytes` | `long` | Size in bytes of the request body. |
|`http.request.body.content` | `wildcard` | The full HTTP request body. |
|`http.request.body.content.text` | `text` | None |
|`http.request.bytes` | `long` | Total size in bytes of the request (body and headers). |
|`http.request.id` | `keyword` | HTTP request ID. |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.mime_type` | `keyword` | Mime type of the body of the request. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`http.response.body.bytes` | `long` | Size in bytes of the response body. |
|`http.response.body.content` | `wildcard` | The full HTTP response body. |
|`http.response.body.content.text` | `text` | None |
|`http.response.bytes` | `long` | Total size in bytes of the response (body and headers). |
|`http.response.mime_type` | `keyword` | Mime type of the body of the response. |
|`http.response.status_code` | `long` | HTTP response status code. |
|`http.version` | `keyword` | HTTP version. |
|`interface.alias` | `keyword` | None |
|`interface.id` | `keyword` | None |
|`interface.name` | `keyword` | None |
|`jolokia.agent.id` | `keyword` | None |
|`jolokia.agent.version` | `keyword` | None |
|`jolokia.secured` | `boolean` | None |
|`jolokia.server.product` | `keyword` | None |
|`jolokia.server.vendor` | `keyword` | None |
|`jolokia.server.version` | `keyword` | None |
|`jolokia.url` | `keyword` | None |
|`kubernetes.annotations` | `text` | None |
|`kubernetes.container.name` | `keyword` | None |
|`kubernetes.deployment.name` | `keyword` | None |
|`kubernetes.labels` | `text` | None |
|`kubernetes.namespace` | `keyword` | None |
|`kubernetes.node.hostname` | `keyword` | None |
|`kubernetes.node.name` | `keyword` | None |
|`kubernetes.pod.ip` | `ip` | None |
|`kubernetes.pod.name` | `keyword` | None |
|`kubernetes.pod.uid` | `keyword` | None |
|`kubernetes.replicaset.name` | `keyword` | None |
|`kubernetes.selectors` | `text` | None |
|`kubernetes.statefulset.name` | `keyword` | None |
|`log.file.path` | `keyword` | Full path to the log file this event came from. |
|`log.level` | `keyword` | Log level of the log event. |
|`log.logger` | `keyword` | Name of the logger. |
|`log.origin.file.line` | `long` | The line number of the file which originated the log event. |
|`log.origin.file.name` | `keyword` | The code file which originated the log event. |
|`log.origin.function` | `keyword` | The function which originated the log event. |
|`log.syslog` | `object` | Syslog metadata |
|`log.syslog.facility.code` | `long` | Syslog numeric facility of the event. |
|`log.syslog.facility.name` | `keyword` | Syslog text-based facility of the event. |
|`log.syslog.priority` | `long` | Syslog priority of the event. |
|`log.syslog.severity.code` | `long` | Syslog numeric severity of the event. |
|`log.syslog.severity.name` | `keyword` | Syslog text-based severity of the event. |
|`network.application` | `keyword` | Application level protocol name. |
|`network.bytes` | `long` | Total bytes transferred in both directions. |
|`network.community_id` | `keyword` | A hash of source and destination IPs and ports. |
|`network.direction` | `keyword` | Direction of the network traffic. |
|`network.forwarded_ip` | `ip` | Host IP address when the source IP address is the proxy. |
|`network.iana_number` | `keyword` | IANA Protocol Number. |
|`network.inner` | `object` | Inner VLAN tag information |
|`network.inner.vlan.id` | `keyword` | VLAN ID as reported by the observer. |
|`network.inner.vlan.name` | `keyword` | Optional VLAN name as reported by the observer. |
|`network.name` | `keyword` | Name given by operators to sections of their network. |
|`network.packets` | `long` | Total packets transferred in both directions. |
|`network.protocol` | `keyword` | Application protocol name. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`network.type` | `keyword` | In the OSI Model this would be the Network Layer. ipv4, ipv6, ipsec, pim, etc |
|`network.vlan.id` | `keyword` | VLAN ID as reported by the observer. |
|`network.vlan.name` | `keyword` | Optional VLAN name as reported by the observer. |
|`observer.egress` | `object` | Object field for egress information |
|`observer.egress.interface.alias` | `keyword` | Interface alias |
|`observer.egress.interface.id` | `keyword` | Interface ID |
|`observer.egress.interface.name` | `keyword` | Interface name |
|`observer.egress.vlan.id` | `keyword` | VLAN ID as reported by the observer. |
|`observer.egress.vlan.name` | `keyword` | Optional VLAN name as reported by the observer. |
|`observer.egress.zone` | `keyword` | Observer Egress zone |
|`observer.geo.city_name` | `keyword` | City name. |
|`observer.geo.continent_code` | `keyword` | Continent code. |
|`observer.geo.continent_name` | `keyword` | Name of the continent. |
|`observer.geo.country_iso_code` | `keyword` | Country ISO code. |
|`observer.geo.country_name` | `keyword` | Country name. |
|`observer.geo.location` | `geo_point` | Longitude and latitude. |
|`observer.geo.name` | `keyword` | User-defined description of a location. |
|`observer.geo.postal_code` | `keyword` | Postal code. |
|`observer.geo.region_iso_code` | `keyword` | Region ISO code. |
|`observer.geo.region_name` | `keyword` | Region name. |
|`observer.geo.timezone` | `keyword` | Time zone. |
|`observer.hostname` | `keyword` | Hostname of the observer. |
|`observer.ingress` | `object` | Object field for ingress information |
|`observer.ingress.interface.alias` | `keyword` | Interface alias |
|`observer.ingress.interface.id` | `keyword` | Interface ID |
|`observer.ingress.interface.name` | `keyword` | Interface name |
|`observer.ingress.vlan.id` | `keyword` | VLAN ID as reported by the observer. |
|`observer.ingress.vlan.name` | `keyword` | Optional VLAN name as reported by the observer. |
|`observer.ingress.zone` | `keyword` | Observer ingress zone |
|`observer.ip` | `ip` | IP addresses of the observer. |
|`observer.mac` | `keyword` | MAC addresses of the observer. |
|`observer.name` | `keyword` | Custom name of the observer. |
|`observer.os.family` | `keyword` | OS family (such as redhat, debian, freebsd, windows). |
|`observer.os.full` | `keyword` | Operating system name, including the version or code name. |
|`observer.os.full.text` | `text` | None |
|`observer.os.kernel` | `keyword` | Operating system kernel version as a raw string. |
|`observer.os.name` | `keyword` | Operating system name, without the version. |
|`observer.os.name.text` | `text` | None |
|`observer.os.platform` | `keyword` | Operating system platform (such centos, ubuntu, windows). |
|`observer.os.type` | `keyword` | Which commercial OS family (one of: linux, macos, unix or windows). |
|`observer.os.version` | `keyword` | Operating system version as a raw string. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.serial_number` | `keyword` | Observer serial number. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`observer.version` | `keyword` | Observer version. |
|`orchestrator.api_version` | `keyword` | API version being used to carry out the action |
|`orchestrator.cluster.name` | `keyword` | Name of the cluster. |
|`orchestrator.cluster.url` | `keyword` | URL of the API used to manage the cluster. |
|`orchestrator.cluster.version` | `keyword` | The version of the cluster. |
|`orchestrator.namespace` | `keyword` | Namespace in which the action is taking place. |
|`orchestrator.organization` | `keyword` | Organization affected by the event (for multi-tenant orchestrator setups). |
|`orchestrator.resource.name` | `keyword` | Name of the resource being acted upon. |
|`orchestrator.resource.type` | `keyword` | Type of resource being acted upon. |
|`orchestrator.type` | `keyword` | Orchestrator cluster type (e.g. kubernetes, nomad or cloudfoundry). |
|`organization.id` | `keyword` | Unique identifier for the organization. |
|`organization.name` | `keyword` | Organization name. |
|`organization.name.text` | `text` | None |
|`os.family` | `keyword` | None |
|`os.full` | `keyword` | None |
|`os.full.text` | `text` | None |
|`os.kernel` | `keyword` | None |
|`os.name` | `keyword` | None |
|`os.name.text` | `text` | None |
|`os.platform` | `keyword` | None |
|`os.type` | `keyword` | None |
|`os.version` | `keyword` | None |
|`package.architecture` | `keyword` | Package architecture. |
|`package.build_version` | `keyword` | Build version information |
|`package.checksum` | `keyword` | Checksum of the installed package for verification. |
|`package.description` | `keyword` | Description of the package. |
|`package.install_scope` | `keyword` | Indicating how the package was installed, e.g. user-local, global. |
|`package.installed` | `date` | Time when package was installed. |
|`package.license` | `keyword` | Package license |
|`package.name` | `keyword` | Package name |
|`package.path` | `keyword` | Path where the package is installed. |
|`package.reference` | `keyword` | Package home page or reference URL |
|`package.size` | `long` | Package size in bytes. |
|`package.type` | `keyword` | Package type |
|`package.version` | `keyword` | Package version |
|`pe.architecture` | `keyword` | None |
|`pe.company` | `keyword` | None |
|`pe.description` | `keyword` | None |
|`pe.file_version` | `keyword` | None |
|`pe.imphash` | `keyword` | None |
|`pe.original_file_name` | `keyword` | None |
|`pe.product` | `keyword` | None |
|`process.args` | `keyword` | Array of process arguments. |
|`process.args_count` | `long` | Length of the process.args array. |
|`process.code_signature.exists` | `boolean` | Boolean to capture if a signature is present. |
|`process.code_signature.signing_id` | `keyword` | The identifier used to sign the process. |
|`process.code_signature.status` | `keyword` | Additional information about the certificate status. |
|`process.code_signature.subject_name` | `keyword` | Subject name of the code signer |
|`process.code_signature.team_id` | `keyword` | The team identifier used to sign the process. |
|`process.code_signature.trusted` | `boolean` | Stores the trust status of the certificate chain. |
|`process.code_signature.valid` | `boolean` | Boolean to capture if the digital signature is verified against the binary content. |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.command_line.text` | `text` | None |
|`process.entity_id` | `keyword` | Unique identifier for the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.executable.text` | `text` | None |
|`process.exit_code` | `long` | The exit code of the process. |
|`process.hash.blake2b_256` | `keyword` | None |
|`process.hash.blake2b_384` | `keyword` | None |
|`process.hash.blake2b_512` | `keyword` | None |
|`process.hash.md5` | `keyword` | MD5 hash. |
|`process.hash.sha1` | `keyword` | SHA1 hash. |
|`process.hash.sha224` | `keyword` | None |
|`process.hash.sha256` | `keyword` | SHA256 hash. |
|`process.hash.sha384` | `keyword` | None |
|`process.hash.sha3_224` | `keyword` | None |
|`process.hash.sha3_256` | `keyword` | None |
|`process.hash.sha3_384` | `keyword` | None |
|`process.hash.sha3_512` | `keyword` | None |
|`process.hash.sha512` | `keyword` | SHA512 hash. |
|`process.hash.sha512_224` | `keyword` | None |
|`process.hash.sha512_256` | `keyword` | None |
|`process.hash.ssdeep` | `keyword` | SSDEEP hash. |
|`process.hash.xxh64` | `keyword` | None |
|`process.name` | `keyword` | Process name. |
|`process.name.text` | `text` | None |
|`process.parent.args` | `keyword` | Array of process arguments. |
|`process.parent.args_count` | `long` | Length of the process.args array. |
|`process.parent.code_signature.exists` | `boolean` | Boolean to capture if a signature is present. |
|`process.parent.code_signature.signing_id` | `keyword` | The identifier used to sign the process. |
|`process.parent.code_signature.status` | `keyword` | Additional information about the certificate status. |
|`process.parent.code_signature.subject_name` | `keyword` | Subject name of the code signer |
|`process.parent.code_signature.team_id` | `keyword` | The team identifier used to sign the process. |
|`process.parent.code_signature.trusted` | `boolean` | Stores the trust status of the certificate chain. |
|`process.parent.code_signature.valid` | `boolean` | Boolean to capture if the digital signature is verified against the binary content. |
|`process.parent.command_line` | `wildcard` | Full command line that started the process. |
|`process.parent.command_line.text` | `text` | None |
|`process.parent.entity_id` | `keyword` | Unique identifier for the process. |
|`process.parent.executable` | `keyword` | Absolute path to the process executable. |
|`process.parent.executable.text` | `text` | None |
|`process.parent.exit_code` | `long` | The exit code of the process. |
|`process.parent.hash.md5` | `keyword` | MD5 hash. |
|`process.parent.hash.sha1` | `keyword` | SHA1 hash. |
|`process.parent.hash.sha256` | `keyword` | SHA256 hash. |
|`process.parent.hash.sha512` | `keyword` | SHA512 hash. |
|`process.parent.hash.ssdeep` | `keyword` | SSDEEP hash. |
|`process.parent.name` | `keyword` | Process name. |
|`process.parent.name.text` | `text` | None |
|`process.parent.pe.architecture` | `keyword` | CPU architecture target for the file. |
|`process.parent.pe.company` | `keyword` | Internal company name of the file, provided at compile-time. |
|`process.parent.pe.description` | `keyword` | Internal description of the file, provided at compile-time. |
|`process.parent.pe.file_version` | `keyword` | Process name. |
|`process.parent.pe.imphash` | `keyword` | A hash of the imports in a PE file. |
|`process.parent.pe.original_file_name` | `keyword` | Internal name of the file, provided at compile-time. |
|`process.parent.pe.product` | `keyword` | Internal product name of the file, provided at compile-time. |
|`process.parent.pgid` | `long` | Identifier of the group of processes the process belongs to. |
|`process.parent.pid` | `long` | Process id. |
|`process.parent.start` | `date` | The time the process started. |
|`process.parent.thread.id` | `long` | Thread ID. |
|`process.parent.thread.name` | `keyword` | Thread name. |
|`process.parent.title` | `keyword` | Process title. |
|`process.parent.title.text` | `text` | None |
|`process.parent.uptime` | `long` | Seconds the process has been up. |
|`process.parent.working_directory` | `keyword` | The working directory of the process. |
|`process.parent.working_directory.text` | `text` | None |
|`process.pe.architecture` | `keyword` | CPU architecture target for the file. |
|`process.pe.company` | `keyword` | Internal company name of the file, provided at compile-time. |
|`process.pe.description` | `keyword` | Internal description of the file, provided at compile-time. |
|`process.pe.file_version` | `keyword` | Process name. |
|`process.pe.imphash` | `keyword` | A hash of the imports in a PE file. |
|`process.pe.original_file_name` | `keyword` | Internal name of the file, provided at compile-time. |
|`process.pe.product` | `keyword` | Internal product name of the file, provided at compile-time. |
|`process.pgid` | `long` | Identifier of the group of processes the process belongs to. |
|`process.pid` | `long` | Process id. |
|`process.start` | `date` | The time the process started. |
|`process.thread.id` | `long` | Thread ID. |
|`process.thread.name` | `keyword` | Thread name. |
|`process.title` | `keyword` | Process title. |
|`process.title.text` | `text` | None |
|`process.uptime` | `long` | Seconds the process has been up. |
|`process.working_directory` | `keyword` | The working directory of the process. |
|`process.working_directory.text` | `text` | None |
|`registry.data.bytes` | `keyword` | Original bytes written with base64 encoding. |
|`registry.data.strings` | `wildcard` | List of strings representing what was written to the registry. |
|`registry.data.type` | `keyword` | Standard registry type for encoding contents |
|`registry.hive` | `keyword` | Abbreviated name for the hive. |
|`registry.key` | `keyword` | Hive-relative path of keys. |
|`registry.path` | `keyword` | Full path, including hive, key and value |
|`registry.value` | `keyword` | Name of the value written. |
|`related.hash` | `keyword` | All the hashes seen on your event. |
|`related.hosts` | `keyword` | All the host identifiers seen on your event. |
|`related.ip` | `ip` | All of the IPs seen on your event. |
|`related.user` | `keyword` | All the user names or other user identifiers seen on the event. |
|`rule.author` | `keyword` | Rule author |
|`rule.category` | `keyword` | Rule category |
|`rule.description` | `keyword` | Rule description |
|`rule.id` | `keyword` | Rule ID |
|`rule.license` | `keyword` | Rule license |
|`rule.name` | `keyword` | Rule name |
|`rule.reference` | `keyword` | Rule reference URL |
|`rule.ruleset` | `keyword` | Rule ruleset |
|`rule.uuid` | `keyword` | Rule UUID |
|`rule.version` | `keyword` | Rule version |
|`server.address` | `keyword` | Server network address. |
|`server.as.number` | `long` | Unique number allocated to the autonomous system. |
|`server.as.organization.name` | `keyword` | Organization name. |
|`server.as.organization.name.text` | `text` | None |
|`server.bytes` | `long` | Bytes sent from the server to the client. |
|`server.domain` | `keyword` | The domain name of the server. |
|`server.geo.city_name` | `keyword` | City name. |
|`server.geo.continent_code` | `keyword` | Continent code. |
|`server.geo.continent_name` | `keyword` | Name of the continent. |
|`server.geo.country_iso_code` | `keyword` | Country ISO code. |
|`server.geo.country_name` | `keyword` | Country name. |
|`server.geo.location` | `geo_point` | Longitude and latitude. |
|`server.geo.name` | `keyword` | User-defined description of a location. |
|`server.geo.postal_code` | `keyword` | Postal code. |
|`server.geo.region_iso_code` | `keyword` | Region ISO code. |
|`server.geo.region_name` | `keyword` | Region name. |
|`server.geo.timezone` | `keyword` | Time zone. |
|`server.ip` | `ip` | IP address of the server. |
|`server.mac` | `keyword` | MAC address of the server. |
|`server.nat.ip` | `ip` | Server NAT ip |
|`server.nat.port` | `long` | Server NAT port |
|`server.packets` | `long` | Packets sent from the server to the client. |
|`server.port` | `long` | Port of the server. |
|`server.registered_domain` | `keyword` | The highest registered server domain, stripped of the subdomain. |
|`server.subdomain` | `keyword` | The subdomain of the domain. |
|`server.top_level_domain` | `keyword` | The effective top level domain (com, org, net, co.uk). |
|`server.user.domain` | `keyword` | Name of the directory the user is a member of. |
|`server.user.email` | `keyword` | User email address. |
|`server.user.full_name` | `keyword` | User's full name, if available. |
|`server.user.full_name.text` | `text` | None |
|`server.user.group.domain` | `keyword` | Name of the directory the group is a member of. |
|`server.user.group.id` | `keyword` | Unique identifier for the group on the system/platform. |
|`server.user.group.name` | `keyword` | Name of the group. |
|`server.user.hash` | `keyword` | Unique user hash to correlate information for a user in anonymized form. |
|`server.user.id` | `keyword` | Unique identifier of the user. |
|`server.user.name` | `keyword` | Short name or login of the user. |
|`server.user.name.text` | `text` | None |
|`server.user.roles` | `keyword` | Array of user roles at the time of the event. |
|`service.ephemeral_id` | `keyword` | Ephemeral identifier of this service. |
|`service.id` | `keyword` | Unique identifier of the running service. |
|`service.name` | `keyword` | Name of the service. |
|`service.node.name` | `keyword` | Name of the service node. |
|`service.state` | `keyword` | Current state of the service. |
|`service.type` | `keyword` | The type of the service. |
|`service.version` | `keyword` | Version of the service. |
|`socket.entity_id` | `keyword` | None |
|`source.address` | `keyword` | Source network address. |
|`source.as.number` | `long` | Unique number allocated to the autonomous system. |
|`source.as.organization.name` | `keyword` | Organization name. |
|`source.as.organization.name.text` | `text` | None |
|`source.bytes` | `long` | Bytes sent from the source to the destination. |
|`source.domain` | `keyword` | The domain name of the source. |
|`source.geo.city_name` | `keyword` | City name. |
|`source.geo.continent_code` | `keyword` | Continent code. |
|`source.geo.continent_name` | `keyword` | Name of the continent. |
|`source.geo.country_iso_code` | `keyword` | Country ISO code. |
|`source.geo.country_name` | `keyword` | Country name. |
|`source.geo.location` | `geo_point` | Longitude and latitude. |
|`source.geo.name` | `keyword` | User-defined description of a location. |
|`source.geo.postal_code` | `keyword` | Postal code. |
|`source.geo.region_iso_code` | `keyword` | Region ISO code. |
|`source.geo.region_name` | `keyword` | Region name. |
|`source.geo.timezone` | `keyword` | Time zone. |
|`source.ip` | `ip` | IP address of the source. |
|`source.mac` | `keyword` | MAC address of the source. |
|`source.nat.ip` | `ip` | Source NAT ip |
|`source.nat.port` | `long` | Source NAT port |
|`source.packets` | `long` | Packets sent from the source to the destination. |
|`source.path` | `keyword` | None |
|`source.port` | `long` | Port of the source. |
|`source.registered_domain` | `keyword` | The highest registered source domain, stripped of the subdomain. |
|`source.subdomain` | `keyword` | The subdomain of the domain. |
|`source.top_level_domain` | `keyword` | The effective top level domain (com, org, net, co.uk). |
|`source.user.domain` | `keyword` | Name of the directory the user is a member of. |
|`source.user.email` | `keyword` | User email address. |
|`source.user.full_name` | `keyword` | User's full name, if available. |
|`source.user.full_name.text` | `text` | None |
|`source.user.group.domain` | `keyword` | Name of the directory the group is a member of. |
|`source.user.group.id` | `keyword` | Unique identifier for the group on the system/platform. |
|`source.user.group.name` | `keyword` | Name of the group. |
|`source.user.hash` | `keyword` | Unique user hash to correlate information for a user in anonymized form. |
|`source.user.id` | `keyword` | Unique identifier of the user. |
|`source.user.name` | `keyword` | Short name or login of the user. |
|`source.user.name.text` | `text` | None |
|`source.user.roles` | `keyword` | Array of user roles at the time of the event. |
|`span.id` | `keyword` | Unique identifier of the span within the scope of its trace. |
|`system.audit.host.architecture` | `keyword` | None |
|`system.audit.host.boottime` | `date` | None |
|`system.audit.host.containerized` | `boolean` | None |
|`system.audit.host.hostname` | `keyword` | None |
|`system.audit.host.id` | `keyword` | None |
|`system.audit.host.ip` | `ip` | None |
|`system.audit.host.mac` | `keyword` | None |
|`system.audit.host.os.codename` | `keyword` | None |
|`system.audit.host.os.family` | `keyword` | None |
|`system.audit.host.os.kernel` | `keyword` | None |
|`system.audit.host.os.name` | `keyword` | None |
|`system.audit.host.os.platform` | `keyword` | None |
|`system.audit.host.os.type` | `keyword` | None |
|`system.audit.host.os.version` | `keyword` | None |
|`system.audit.host.timezone.name` | `keyword` | None |
|`system.audit.host.timezone.offset.sec` | `long` | None |
|`system.audit.host.uptime` | `long` | None |
|`system.audit.package.arch` | `keyword` | None |
|`system.audit.package.entity_id` | `keyword` | None |
|`system.audit.package.installtime` | `date` | None |
|`system.audit.package.license` | `keyword` | None |
|`system.audit.package.name` | `keyword` | None |
|`system.audit.package.release` | `keyword` | None |
|`system.audit.package.size` | `long` | None |
|`system.audit.package.summary` | `keyword` | None |
|`system.audit.package.url` | `keyword` | None |
|`system.audit.package.version` | `keyword` | None |
|`system.audit.user.dir` | `keyword` | None |
|`system.audit.user.gid` | `keyword` | None |
|`system.audit.user.group` | `keyword` | None |
|`system.audit.user.name` | `keyword` | None |
|`system.audit.user.shell` | `keyword` | None |
|`system.audit.user.user_information` | `keyword` | None |
|`threat.framework` | `keyword` | Threat classification framework. |
|`threat.tactic.id` | `keyword` | Threat tactic id. |
|`threat.tactic.name` | `keyword` | Threat tactic. |
|`threat.tactic.reference` | `keyword` | Threat tactic URL reference. |
|`threat.technique.id` | `keyword` | Threat technique id. |
|`threat.technique.name` | `keyword` | Threat technique name. |
|`threat.technique.name.text` | `text` | None |
|`threat.technique.reference` | `keyword` | Threat technique URL reference. |
|`threat.technique.subtechnique.id` | `keyword` | Threat subtechnique id. |
|`threat.technique.subtechnique.name` | `keyword` | Threat subtechnique name. |
|`threat.technique.subtechnique.name.text` | `text` | None |
|`threat.technique.subtechnique.reference` | `keyword` | Threat subtechnique URL reference. |
|`timeseries.instance` | `keyword` | None |
|`tls.cipher` | `keyword` | String indicating the cipher used during the current connection. |
|`tls.client.certificate` | `keyword` | PEM-encoded stand-alone certificate offered by the client. |
|`tls.client.certificate_chain` | `keyword` | Array of PEM-encoded certificates that make up the certificate chain offered by the client. |
|`tls.client.hash.md5` | `keyword` | Certificate fingerprint using the MD5 digest of DER-encoded version of certificate offered by the client. |
|`tls.client.hash.sha1` | `keyword` | Certificate fingerprint using the SHA1 digest of DER-encoded version of certificate offered by the client. |
|`tls.client.hash.sha256` | `keyword` | Certificate fingerprint using the SHA256 digest of DER-encoded version of certificate offered by the client. |
|`tls.client.issuer` | `keyword` | Distinguished name of subject of the issuer of the x.509 certificate presented by the client. |
|`tls.client.ja3` | `keyword` | A hash that identifies clients based on how they perform an SSL/TLS handshake. |
|`tls.client.not_after` | `date` | Date/Time indicating when client certificate is no longer considered valid. |
|`tls.client.not_before` | `date` | Date/Time indicating when client certificate is first considered valid. |
|`tls.client.server_name` | `keyword` | Hostname the client is trying to connect to. Also called the SNI. |
|`tls.client.subject` | `keyword` | Distinguished name of subject of the x.509 certificate presented by the client. |
|`tls.client.supported_ciphers` | `keyword` | Array of ciphers offered by the client during the client hello. |
|`tls.client.x509.alternative_names` | `keyword` | List of subject alternative names (SAN). |
|`tls.client.x509.issuer.common_name` | `keyword` | List of common name (CN) of issuing certificate authority. |
|`tls.client.x509.issuer.country` | `keyword` | List of country (C) codes |
|`tls.client.x509.issuer.distinguished_name` | `keyword` | Distinguished name (DN) of issuing certificate authority. |
|`tls.client.x509.issuer.locality` | `keyword` | List of locality names (L) |
|`tls.client.x509.issuer.organization` | `keyword` | List of organizations (O) of issuing certificate authority. |
|`tls.client.x509.issuer.organizational_unit` | `keyword` | List of organizational units (OU) of issuing certificate authority. |
|`tls.client.x509.issuer.state_or_province` | `keyword` | List of state or province names (ST, S, or P) |
|`tls.client.x509.not_after` | `date` | Time at which the certificate is no longer considered valid. |
|`tls.client.x509.not_before` | `date` | Time at which the certificate is first considered valid. |
|`tls.client.x509.public_key_algorithm` | `keyword` | Algorithm used to generate the public key. |
|`tls.client.x509.public_key_curve` | `keyword` | The curve used by the elliptic curve public key algorithm. This is algorithm specific. |
|`tls.client.x509.public_key_exponent` | `long` | Exponent used to derive the public key. This is algorithm specific. |
|`tls.client.x509.public_key_size` | `long` | The size of the public key space in bits. |
|`tls.client.x509.serial_number` | `keyword` | Unique serial number issued by the certificate authority. |
|`tls.client.x509.signature_algorithm` | `keyword` | Identifier for certificate signature algorithm. |
|`tls.client.x509.subject.common_name` | `keyword` | List of common names (CN) of subject. |
|`tls.client.x509.subject.country` | `keyword` | List of country (C) code |
|`tls.client.x509.subject.distinguished_name` | `keyword` | Distinguished name (DN) of the certificate subject entity. |
|`tls.client.x509.subject.locality` | `keyword` | List of locality names (L) |
|`tls.client.x509.subject.organization` | `keyword` | List of organizations (O) of subject. |
|`tls.client.x509.subject.organizational_unit` | `keyword` | List of organizational units (OU) of subject. |
|`tls.client.x509.subject.state_or_province` | `keyword` | List of state or province names (ST, S, or P) |
|`tls.client.x509.version_number` | `keyword` | Version of x509 format. |
|`tls.curve` | `keyword` | String indicating the curve used for the given cipher, when applicable. |
|`tls.established` | `boolean` | Boolean flag indicating if the TLS negotiation was successful and transitioned to an encrypted tunnel. |
|`tls.next_protocol` | `keyword` | String indicating the protocol being tunneled. |
|`tls.resumed` | `boolean` | Boolean flag indicating if this TLS connection was resumed from an existing TLS negotiation. |
|`tls.server.certificate` | `keyword` | PEM-encoded stand-alone certificate offered by the server. |
|`tls.server.certificate_chain` | `keyword` | Array of PEM-encoded certificates that make up the certificate chain offered by the server. |
|`tls.server.hash.md5` | `keyword` | Certificate fingerprint using the MD5 digest of DER-encoded version of certificate offered by the server. |
|`tls.server.hash.sha1` | `keyword` | Certificate fingerprint using the SHA1 digest of DER-encoded version of certificate offered by the server. |
|`tls.server.hash.sha256` | `keyword` | Certificate fingerprint using the SHA256 digest of DER-encoded version of certificate offered by the server. |
|`tls.server.issuer` | `keyword` | Subject of the issuer of the x.509 certificate presented by the server. |
|`tls.server.ja3s` | `keyword` | A hash that identifies servers based on how they perform an SSL/TLS handshake. |
|`tls.server.not_after` | `date` | Timestamp indicating when server certificate is no longer considered valid. |
|`tls.server.not_before` | `date` | Timestamp indicating when server certificate is first considered valid. |
|`tls.server.subject` | `keyword` | Subject of the x.509 certificate presented by the server. |
|`tls.server.x509.alternative_names` | `keyword` | List of subject alternative names (SAN). |
|`tls.server.x509.issuer.common_name` | `keyword` | List of common name (CN) of issuing certificate authority. |
|`tls.server.x509.issuer.country` | `keyword` | List of country (C) codes |
|`tls.server.x509.issuer.distinguished_name` | `keyword` | Distinguished name (DN) of issuing certificate authority. |
|`tls.server.x509.issuer.locality` | `keyword` | List of locality names (L) |
|`tls.server.x509.issuer.organization` | `keyword` | List of organizations (O) of issuing certificate authority. |
|`tls.server.x509.issuer.organizational_unit` | `keyword` | List of organizational units (OU) of issuing certificate authority. |
|`tls.server.x509.issuer.state_or_province` | `keyword` | List of state or province names (ST, S, or P) |
|`tls.server.x509.not_after` | `date` | Time at which the certificate is no longer considered valid. |
|`tls.server.x509.not_before` | `date` | Time at which the certificate is first considered valid. |
|`tls.server.x509.public_key_algorithm` | `keyword` | Algorithm used to generate the public key. |
|`tls.server.x509.public_key_curve` | `keyword` | The curve used by the elliptic curve public key algorithm. This is algorithm specific. |
|`tls.server.x509.public_key_exponent` | `long` | Exponent used to derive the public key. This is algorithm specific. |
|`tls.server.x509.public_key_size` | `long` | The size of the public key space in bits. |
|`tls.server.x509.serial_number` | `keyword` | Unique serial number issued by the certificate authority. |
|`tls.server.x509.signature_algorithm` | `keyword` | Identifier for certificate signature algorithm. |
|`tls.server.x509.subject.common_name` | `keyword` | List of common names (CN) of subject. |
|`tls.server.x509.subject.country` | `keyword` | List of country (C) code |
|`tls.server.x509.subject.distinguished_name` | `keyword` | Distinguished name (DN) of the certificate subject entity. |
|`tls.server.x509.subject.locality` | `keyword` | List of locality names (L) |
|`tls.server.x509.subject.organization` | `keyword` | List of organizations (O) of subject. |
|`tls.server.x509.subject.organizational_unit` | `keyword` | List of organizational units (OU) of subject. |
|`tls.server.x509.subject.state_or_province` | `keyword` | List of state or province names (ST, S, or P) |
|`tls.server.x509.version_number` | `keyword` | Version of x509 format. |
|`tls.version` | `keyword` | Numeric part of the version parsed from the original string. |
|`tls.version_protocol` | `keyword` | Normalized lowercase protocol name parsed from original string. |
|`trace.id` | `keyword` | Unique identifier of the trace. |
|`transaction.id` | `keyword` | Unique identifier of the transaction within the scope of its trace. |
|`url.domain` | `keyword` | Domain of the url. |
|`url.extension` | `keyword` | File extension from the request url, excluding the leading dot. |
|`url.fragment` | `keyword` | Portion of the url after the `#`. |
|`url.full` | `wildcard` | Full unparsed URL. |
|`url.full.text` | `text` | None |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`url.original.text` | `text` | None |
|`url.password` | `keyword` | Password of the request. |
|`url.path` | `wildcard` | Path of the request, such as "/search". |
|`url.port` | `long` | Port of the request, such as 443. |
|`url.query` | `keyword` | Query string of the request. |
|`url.registered_domain` | `keyword` | The highest registered url domain, stripped of the subdomain. |
|`url.scheme` | `keyword` | Scheme of the url. |
|`url.subdomain` | `keyword` | The subdomain of the domain. |
|`url.top_level_domain` | `keyword` | The effective top level domain (com, org, net, co.uk). |
|`url.username` | `keyword` | Username of the request. |
|`user.audit.id` | `keyword` | None |
|`user.audit.name` | `keyword` | None |
|`user.changes.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.changes.email` | `keyword` | User email address. |
|`user.changes.full_name` | `keyword` | User's full name, if available. |
|`user.changes.full_name.text` | `text` | None |
|`user.changes.group.domain` | `keyword` | Name of the directory the group is a member of. |
|`user.changes.group.id` | `keyword` | Unique identifier for the group on the system/platform. |
|`user.changes.group.name` | `keyword` | Name of the group. |
|`user.changes.hash` | `keyword` | Unique user hash to correlate information for a user in anonymized form. |
|`user.changes.id` | `keyword` | Unique identifier of the user. |
|`user.changes.name` | `keyword` | Short name or login of the user. |
|`user.changes.name.text` | `text` | None |
|`user.changes.roles` | `keyword` | Array of user roles at the time of the event. |
|`user.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.effective.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.effective.email` | `keyword` | User email address. |
|`user.effective.full_name` | `keyword` | User's full name, if available. |
|`user.effective.full_name.text` | `text` | None |
|`user.effective.group.domain` | `keyword` | Name of the directory the group is a member of. |
|`user.effective.group.id` | `keyword` | Unique identifier for the group on the system/platform. |
|`user.effective.group.name` | `keyword` | Name of the group. |
|`user.effective.hash` | `keyword` | Unique user hash to correlate information for a user in anonymized form. |
|`user.effective.id` | `keyword` | Unique identifier of the user. |
|`user.effective.name` | `keyword` | Short name or login of the user. |
|`user.effective.name.text` | `text` | None |
|`user.effective.roles` | `keyword` | Array of user roles at the time of the event. |
|`user.email` | `keyword` | User email address. |
|`user.entity_id` | `keyword` | None |
|`user.filesystem.group.id` | `keyword` | None |
|`user.filesystem.group.name` | `keyword` | None |
|`user.filesystem.id` | `keyword` | None |
|`user.filesystem.name` | `keyword` | None |
|`user.full_name` | `keyword` | User's full name, if available. |
|`user.full_name.text` | `text` | None |
|`user.group.domain` | `keyword` | Name of the directory the group is a member of. |
|`user.group.id` | `keyword` | Unique identifier for the group on the system/platform. |
|`user.group.name` | `keyword` | Name of the group. |
|`user.hash` | `keyword` | Unique user hash to correlate information for a user in anonymized form. |
|`user.id` | `keyword` | Unique identifier of the user. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user.name.text` | `text` | None |
|`user.roles` | `keyword` | Array of user roles at the time of the event. |
|`user.selinux.category` | `keyword` | None |
|`user.selinux.domain` | `keyword` | None |
|`user.selinux.level` | `keyword` | None |
|`user.selinux.role` | `keyword` | None |
|`user.selinux.user` | `keyword` | None |
|`user.target.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.target.email` | `keyword` | User email address. |
|`user.target.full_name` | `keyword` | User's full name, if available. |
|`user.target.full_name.text` | `text` | None |
|`user.target.group.domain` | `keyword` | Name of the directory the group is a member of. |
|`user.target.group.id` | `keyword` | Unique identifier for the group on the system/platform. |
|`user.target.group.name` | `keyword` | Name of the group. |
|`user.target.hash` | `keyword` | Unique user hash to correlate information for a user in anonymized form. |
|`user.target.id` | `keyword` | Unique identifier of the user. |
|`user.target.name` | `keyword` | Short name or login of the user. |
|`user.target.name.text` | `text` | None |
|`user.target.roles` | `keyword` | Array of user roles at the time of the event. |
|`user.terminal` | `keyword` | None |
|`user_agent.device.name` | `keyword` | Name of the device. |
|`user_agent.name` | `keyword` | Name of the user agent. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |
|`user_agent.original.text` | `text` | None |
|`user_agent.os.family` | `keyword` | OS family (such as redhat, debian, freebsd, windows). |
|`user_agent.os.full` | `keyword` | Operating system name, including the version or code name. |
|`user_agent.os.full.text` | `text` | None |
|`user_agent.os.kernel` | `keyword` | Operating system kernel version as a raw string. |
|`user_agent.os.name` | `keyword` | Operating system name, without the version. |
|`user_agent.os.name.text` | `text` | None |
|`user_agent.os.platform` | `keyword` | Operating system platform (such centos, ubuntu, windows). |
|`user_agent.os.type` | `keyword` | Which commercial OS family (one of: linux, macos, unix or windows). |
|`user_agent.os.version` | `keyword` | Operating system version as a raw string. |
|`user_agent.version` | `keyword` | Version of the user agent. |
|`vlan.id` | `keyword` | None |
|`vlan.name` | `keyword` | None |
|`vulnerability.category` | `keyword` | Category of a vulnerability. |
|`vulnerability.classification` | `keyword` | Classification of the vulnerability. |
|`vulnerability.description` | `keyword` | Description of the vulnerability. |
|`vulnerability.description.text` | `text` | None |
|`vulnerability.enumeration` | `keyword` | Identifier of the vulnerability. |
|`vulnerability.id` | `keyword` | ID of the vulnerability. |
|`vulnerability.reference` | `keyword` | Reference of the vulnerability. |
|`vulnerability.report_id` | `keyword` | Scan identification number. |
|`vulnerability.scanner.vendor` | `keyword` | Name of the scanner vendor. |
|`vulnerability.score.base` | `float` | Vulnerability Base score. |
|`vulnerability.score.environmental` | `float` | Vulnerability Environmental score. |
|`vulnerability.score.temporal` | `float` | Vulnerability Temporal score. |
|`vulnerability.score.version` | `keyword` | CVSS version. |
|`vulnerability.severity` | `keyword` | Severity of the vulnerability. |
|`x509.alternative_names` | `keyword` | None |
|`x509.issuer.common_name` | `keyword` | None |
|`x509.issuer.country` | `keyword` | None |
|`x509.issuer.distinguished_name` | `keyword` | None |
|`x509.issuer.locality` | `keyword` | None |
|`x509.issuer.organization` | `keyword` | None |
|`x509.issuer.organizational_unit` | `keyword` | None |
|`x509.issuer.state_or_province` | `keyword` | None |
|`x509.not_after` | `date` | None |
|`x509.not_before` | `date` | None |
|`x509.public_key_algorithm` | `keyword` | None |
|`x509.public_key_curve` | `keyword` | None |
|`x509.public_key_exponent` | `long` | None |
|`x509.public_key_size` | `long` | None |
|`x509.serial_number` | `keyword` | None |
|`x509.signature_algorithm` | `keyword` | None |
|`x509.subject.common_name` | `keyword` | None |
|`x509.subject.country` | `keyword` | None |
|`x509.subject.distinguished_name` | `keyword` | None |
|`x509.subject.locality` | `keyword` | None |
|`x509.subject.organization` | `keyword` | None |
|`x509.subject.organizational_unit` | `keyword` | None |
|`x509.subject.state_or_province` | `keyword` | None |
|`x509.version_number` | `keyword` | None |

