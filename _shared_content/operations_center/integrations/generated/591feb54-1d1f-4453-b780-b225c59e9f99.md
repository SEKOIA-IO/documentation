
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Host network interface` | every packets are logged and information on the outcome, the source/destination are extracted |
| `Network device logs` | ACL logs are examined in detail |
| `Network protocol analysis` | packets are fully analyzed |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `host` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "test_arp_src_ip.json"

    ```json
	
    {
        "message": "2023 Jan 11 19:27:57 CET: %ARP-2-DUP_SRC_IP: arp [20856] Source address of packet received from 0050.5683.69cd on Vlan756(port-channel100) is duplicate of local, 10.30.38.5 (message repeated 1 time)",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 2,
            "code": "DUP_SRC_IP",
            "reason": "arp [20856] Source address of packet received from 0050.5683.69cd on Vlan756(port-channel100) is duplicate of local, 10.30.38.5 (message repeated 1 time)"
        },
        "@timestamp": "2023-01-11T18:27:57.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "source": {
            "ip": "10.30.38.5",
            "address": "10.30.38.5"
        },
        "host": {
            "mac": "00:50:56:83:69:CD"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "ARP"
                },
                "observer": {
                    "interface": {
                        "name": "port-channel100"
                    },
                    "vlan": "Vlan756"
                }
            }
        },
        "related": {
            "ip": [
                "10.30.38.5"
            ]
        }
    }
    	
	```


=== "test_authpriv.json"

    ```json
	
    {
        "message": "2023 Jan 15 00:31:52 CET: %AUTHPRIV-3-SYSTEM_MSG: pam_aaa:Authentication failed from 1.2.3.4 - dcos_sshd[6531]",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 3,
            "code": "SYSTEM_MSG",
            "reason": "pam_aaa:Authentication failed from 1.2.3.4 - dcos_sshd[6531]",
            "module": "pam"
        },
        "@timestamp": "2023-01-14T23:31:52.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "process": {
            "pid": 6531,
            "name": "dcos_sshd"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "AUTHPRIV",
                    "outcome": "failure"
                }
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        }
    }
    	
	```


=== "test_daemon.json"

    ```json
	
    {
        "message": "2023 Jan 15 00:31:52 CET: %DAEMON-3-SYSTEM_MSG: error: PAM: Authentication failure for illegal user USERID from 4.3.6.5 - dcos_sshd[6526]",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 3,
            "code": "SYSTEM_MSG",
            "reason": "error: PAM: Authentication failure for illegal user USERID from 4.3.6.5 - dcos_sshd[6526]",
            "module": "pam"
        },
        "@timestamp": "2023-01-14T23:31:52.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "source": {
            "ip": "4.3.6.5",
            "address": "4.3.6.5"
        },
        "user": {
            "name": "USERID"
        },
        "process": {
            "pid": 6526,
            "name": "dcos_sshd"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "DAEMON",
                    "outcome": "failure"
                }
            }
        },
        "related": {
            "ip": [
                "4.3.6.5"
            ],
            "user": [
                "USERID"
            ]
        }
    }
    	
	```


=== "test_if_down_admin_down.json"

    ```json
	
    {
        "message": "2023 Jan 17 12:23:16 CET: %ETHPORT-5-IF_DOWN_ADMIN_DOWN: Interface Ethernet1/38 (description:SRV-01) is down (Administratively down)",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 5,
            "code": "IF_DOWN_ADMIN_DOWN",
            "reason": "Administratively down",
            "action": "down"
        },
        "@timestamp": "2023-01-17T11:23:16.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "ETHPORT"
                },
                "observer": {
                    "interface": {
                        "name": "Ethernet1/38"
                    }
                }
            }
        }
    }
    	
	```


=== "test_if_down_cfg_change.json"

    ```json
	
    {
        "message": "2023 Jan 17 12:23:15 CET: %ETHPORT-5-IF_DOWN_CFG_CHANGE: Interface Ethernet1/38 (description:SRV-01) is down(Config change)",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 5,
            "code": "IF_DOWN_CFG_CHANGE",
            "reason": "Config change",
            "action": "down"
        },
        "@timestamp": "2023-01-17T11:23:15.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "ETHPORT"
                },
                "observer": {
                    "interface": {
                        "name": "Ethernet1/38"
                    }
                }
            }
        }
    }
    	
	```


=== "test_if_duplex.json"

    ```json
	
    {
        "message": "2023 Jan 11 18:43:54 CET: %ETHPORT-5-IF_DUPLEX: Interface Ethernet1/38, operational duplex mode changed to Full",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 5,
            "code": "IF_DUPLEX",
            "reason": "operational duplex mode changed to Full"
        },
        "@timestamp": "2023-01-11T17:43:54.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "ETHPORT"
                },
                "observer": {
                    "interface": {
                        "name": "Ethernet1/38"
                    }
                }
            }
        }
    }
    	
	```


=== "test_if_rx_flow_control.json"

    ```json
	
    {
        "message": "2023 Jan 11 18:43:54 CET: %ETHPORT-5-IF_RX_FLOW_CONTROL: Interface Ethernet1/38, operational Receive Flow Control state changed to off",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 5,
            "code": "IF_RX_FLOW_CONTROL",
            "reason": "operational Receive Flow Control state changed to off"
        },
        "@timestamp": "2023-01-11T17:43:54.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "ETHPORT"
                },
                "observer": {
                    "interface": {
                        "name": "Ethernet1/38"
                    }
                }
            }
        }
    }
    	
	```


=== "test_if_speed.json"

    ```json
	
    {
        "message": "2023 Jan 11 18:43:54 CET: %ETHPORT-5-SPEED: Interface Ethernet1/38, operational speed changed to 1 Gbps",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 5,
            "code": "SPEED",
            "reason": "operational speed changed to 1 Gbps"
        },
        "@timestamp": "2023-01-11T17:43:54.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "ETHPORT"
                },
                "observer": {
                    "interface": {
                        "name": "Ethernet1/38"
                    }
                }
            }
        }
    }
    	
	```


=== "test_if_up.json"

    ```json
	
    {
        "message": "2023 Jan 17 12:23:02 CET: %ETHPORT-5-IF_UP: Interface Ethernet1/38 (description:SRV-01) is up in mode access",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 5,
            "code": "IF_UP",
            "reason": "Interface Ethernet1/38 (description:SRV-01) is up in mode access",
            "action": "up"
        },
        "@timestamp": "2023-01-17T11:23:02.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "ETHPORT"
                },
                "observer": {
                    "interface": {
                        "name": "Ethernet1/38"
                    }
                }
            }
        }
    }
    	
	```


=== "test_port_channel_members_down.json"

    ```json
	
    {
        "message": "2023 Jan 11 16:46:31 CET: %ETHPORT-5-IF_DOWN_PORT_CHANNEL_MEMBERS_DOWN: Interface port-channel110 is down (No operational members)",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 5,
            "code": "IF_DOWN_PORT_CHANNEL_MEMBERS_DOWN",
            "reason": "No operational members",
            "action": "down"
        },
        "@timestamp": "2023-01-11T15:46:31.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "ETHPORT"
                },
                "observer": {
                    "interface": {
                        "name": "port-channel110"
                    }
                }
            }
        }
    }
    	
	```


=== "test_port_channel_suspended.json"

    ```json
	
    {
        "message": "2023 Jan 11 16:46:45 CET: %ETH_PORT_CHANNEL-5-PORT_SUSPENDED: Ethernet1/38: Ethernet1/38 is suspended",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 5,
            "code": "PORT_SUSPENDED",
            "reason": "Ethernet1/38 is suspended"
        },
        "@timestamp": "2023-01-11T15:46:45.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "ETH_PORT_CHANNEL"
                },
                "observer": {
                    "interface": {
                        "name": "Ethernet1/38"
                    }
                }
            }
        }
    }
    	
	```


=== "test_user.json"

    ```json
	
    {
        "message": "2023 Jan 13 02:11:53 CET: %USER-3-SYSTEM_MSG: Failed to open file: No such file or directory - securityd",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 3,
            "code": "SYSTEM_MSG",
            "reason": "No such file or directory"
        },
        "@timestamp": "2023-01-13T01:11:53.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "file": {
            "name": "securityd"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "USER",
                    "outcome": "failure"
                }
            }
        }
    }
    	
	```


=== "test_vshd_syslog_cmd_exec.json"

    ```json
	
    {
        "message": "2023 Jan 11 19:06:23 CET: %VSHD-5-VSHD_SYSLOG_CMD_EXEC: User:jdoe executed the command:securityd",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 5,
            "code": "VSHD_SYSLOG_CMD_EXEC",
            "reason": "User:jdoe executed the command:securityd"
        },
        "@timestamp": "2023-01-11T18:06:23.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "user": {
            "name": "jdoe"
        },
        "process": {
            "command_line": "securityd",
            "args": [
                "securityd"
            ],
            "executable": "securityd",
            "name": "securityd"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "VSHD"
                }
            }
        },
        "related": {
            "user": [
                "jdoe"
            ]
        }
    }
    	
	```


=== "test_vshd_syslog_config.json"

    ```json
	
    {
        "message": "2023 Jan 11 19:00:56 CET: %VSHD-5-VSHD_SYSLOG_CONFIG_I: Configured from vty by jdoe on 1.2.3.4@pts/0",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 5,
            "code": "VSHD_SYSLOG_CONFIG_I",
            "reason": "Configured from vty by jdoe on 1.2.3.4@pts/0"
        },
        "@timestamp": "2023-01-11T18:00:56.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "destination": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "user": {
            "name": "jdoe"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "VSHD"
                },
                "observer": {
                    "terminal": "pts/0"
                }
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "jdoe"
            ]
        }
    }
    	
	```


=== "test_vshd_syslog_config2.json"

    ```json
	
    {
        "message": "2023 Jan 11 19:00:56 CET: %VSHD-5-VSHD_SYSLOG_CONFIG_I: Configured from vty by jdoe on console",
        "event": {
            "kind": "event",
            "category": [
                "host"
            ],
            "type": [
                "info"
            ],
            "severity": 5,
            "code": "VSHD_SYSLOG_CONFIG_I",
            "reason": "Configured from vty by jdoe on console"
        },
        "@timestamp": "2023-01-11T18:00:56.000000Z",
        "observer": {
            "vendor": "Cisco",
            "product": "NX-OS"
        },
        "user": {
            "name": "jdoe"
        },
        "cisco": {
            "nxos": {
                "event": {
                    "facility": "VSHD"
                },
                "observer": {
                    "terminal": "console"
                }
            }
        },
        "related": {
            "user": [
                "jdoe"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`cisco.nxos.event.facility` | `keyword` | The facility of the event |
|`cisco.nxos.observer.interface.name` | `keyword` | The name of the interface |
|`cisco.nxos.observer.terminal` | `keyword` | The identifier of the terminal used for the action |
|`cisco.nxos.observer.vlan` | `keyword` | The virtual lan of the observed packet |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.ip` | `ip` | IP address of the destination. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.module` | `keyword` | Name of the module this data is coming from. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.severity` | `long` | Numeric severity of the event. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`host.mac` | `keyword` | Host MAC addresses. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`process.args` | `keyword` | Array of process arguments. |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.name` | `keyword` | Process name. |
|`process.pid` | `long` | Process id. |
|`source.ip` | `ip` | IP address of the source. |
|`user.name` | `keyword` | Short name or login of the user. |

