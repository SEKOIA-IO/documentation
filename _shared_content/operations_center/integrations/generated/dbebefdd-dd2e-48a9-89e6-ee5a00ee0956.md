
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Application logs` | Application activities from the VM are collected and saved |
| `File monitoring` | Monitor files and devices activities |
| `Network device logs` | Network activities from the VM are collected and saved |
| `Services` | VM services activities are collected and saved |








### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "event_01.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=31000 param1=\"0\" param2=\"0\" param3=\"0\" param4=\"0\" ChangesXML=\"<changes><object><property internal=\"SyslogReportingEnabled\" type=\"Boolean\"><old>False</old><new>True</new></property><property internal=\"SyslogReportingHost\" type=\"String\"><old /><new>logconcentrator.example.org</new></property><property internal=\"SyslogReportingPort\" type=\"Integer\"><old /><new>20517</new></property><property internal=\"SyslogReportingProtocol\" type=\"SyslogProtocol\"><old /><new>Tcp</new></property><property internal=\"SyslogReportingCertificateThumbprint\" type=\"String\"><old /><new></new></property></object></changes>\" UserName=\"example.com\\jdoe\" Version=\"1\" Description=\"Backup server general options have been changed\"]",
        "event": {
            "category": [
                "configuration"
            ],
            "reason": "Backup server general options have been changed",
            "type": [
                "change"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "related": {
            "user": [
                "jdoe"
            ]
        },
        "user": {
            "domain": "example.com",
            "name": "jdoe"
        },
        "veeam": {
            "instance": {
                "id": 31000
            },
            "job": {
                "object": "\"<changes><object><property"
            }
        }
    }
    	
	```


=== "event_02.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=31000 param1=\"0\" param2=\"0\" param3=\"0\" param4=\"0\" ChangesXML=\"<changes><object /></changes>\" UserName=\"example.com\\jdoe\" Version=\"1\" Description=\"Backup server general options have been changed\"]",
        "event": {
            "category": [
                "configuration"
            ],
            "reason": "Backup server general options have been changed",
            "type": [
                "change"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "related": {
            "user": [
                "jdoe"
            ]
        },
        "user": {
            "domain": "example.com",
            "name": "jdoe"
        },
        "veeam": {
            "instance": {
                "id": 31000
            },
            "job": {
                "object": "<changes><object /></changes>"
            }
        }
    }
    	
	```


=== "event_03.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=25300 CredentialsId=\"11111111-2222-4333-4444-555555555555\" AccountName=\"example.com\\jdoe\" param3=\"0\" param4=\"0\" param5=\"0\" UserName=\"example.com\\jdoe\" UserFullInfo=\"<ModifiedUserInfo fullName=\"example.com\\jdoe\" loginType=\"0\" />\" Version=\"1\" Description=\"Credentials example.com\\jdoe have been added\"]",
        "event": {
            "category": [
                "configuration"
            ],
            "reason": "Credentials example.com\\jdoe have been added",
            "type": [
                "creation"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "related": {
            "user": [
                "jdoe"
            ]
        },
        "user": {
            "domain": "example.com",
            "name": "jdoe"
        },
        "veeam": {
            "credentials": {
                "id": "11111111-2222-4333-4444-555555555555"
            },
            "instance": {
                "id": 25300
            }
        }
    }
    	
	```


=== "event_04.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=23010 JobID=\"11111111-2222-4333-4444-555555555555\" JobType=\"12003\" Platform=\"6\" JobName=\"Agent Backup Job 1\" ChangesXML=\"<changes><object id=\"11111111-2222-4333-4444-555555555555\" /></changes>\" param6=\"MyMachine\\jdoe\" Version=\"1\" Description=\"Agent Backup job 'Agent Backup Job 1' has been created.\"]",
        "event": {
            "category": [
                "configuration"
            ],
            "reason": "Agent Backup job 'Agent Backup Job 1' has been created.",
            "type": [
                "creation"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 23010
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "name": "Agent Backup Job 1",
                "object": "\"<changes><object",
                "type": "12003"
            }
        }
    }
    	
	```


=== "event_05.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=23110 JobID=\"11111111-2222-4333-4444-555555555555\" JobType=\"12003\" Platform=\"N\\A\" JobName=\"Agent Backup Job 1\" ChangesXML=\"<changes><object id=\"11111111-2222-4333-4444-555555555555\" /></changes>\" UserName=\"example.com\\jdoe\" Version=\"1\" Description=\"'1' objects has been created for 'Agent Backup Job 1'.\"]",
        "event": {
            "category": [
                "configuration"
            ],
            "reason": "'1' objects has been created for 'Agent Backup Job 1'.",
            "type": [
                "creation"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "related": {
            "user": [
                "jdoe"
            ]
        },
        "user": {
            "domain": "example.com",
            "name": "jdoe"
        },
        "veeam": {
            "instance": {
                "id": 23110
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "name": "Agent Backup Job 1",
                "object": "\"<changes><object",
                "type": "12003"
            }
        }
    }
    	
	```


=== "event_06.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=710 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" JobType=\"12003\" Platform=\"6\" Flags=\"1\" Version=\"1\" Description=\"Agent Backup job 'Agent Backup Job 1' has been started by user .\\SYSTEM.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "Agent Backup job 'Agent Backup Job 1' has been started by user .\\SYSTEM.",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 710
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12003"
            }
        }
    }
    	
	```


=== "event_07.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=810 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" JobType=\"12005\" Flags=\"0\" Version=\"1\" Description=\"Rescan job 'Rescan of Agent Backup Job 1' has been started.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "Rescan job 'Rescan of Agent Backup Job 1' has been started.",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 810
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12005"
            }
        }
    }
    	
	```


=== "event_08.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=32900 param1=\"0\" HostName=\"127.0.0.1\" ComponentDisplayName=\"Veeam Agent for Windows\" Result=\"True\" IsInstallOrUpgrade=\"True\" Version=\"1\" Description=\"Component [Veeam Agent for Windows] on the host [127.0.0.1] has been updated\"]",
        "event": {
            "category": [
                "configuration"
            ],
            "reason": "Component [Veeam Agent for Windows] on the host [127.0.0.1] has been updated",
            "type": [
                "change"
            ]
        },
        "agent": {
            "name": "Veeam Agent for Windows"
        },
        "host": {
            "ip": [
                "127.0.0.1"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "related": {
            "ip": [
                "127.0.0.1"
            ]
        },
        "veeam": {
            "instance": {
                "id": 32900
            }
        }
    }
    	
	```


=== "event_09.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=23010 JobID=\"11111111-2222-4333-4444-555555555555\" JobType=\"12000\" Platform=\"6\" JobName=\"Agent Backup Job 1 - 127.0.0.1\" ChangesXML=\"<changes><object id=\"11111111-2222-4333-4444-555555555555\" /></changes>\" param6=\"SYSTEM\" Version=\"1\" Description=\"Agent Backup job 'Agent Backup Job 1 - 127.0.0.1' has been created.\"]",
        "event": {
            "category": [
                "configuration"
            ],
            "reason": "Agent Backup job 'Agent Backup Job 1 - 127.0.0.1' has been created.",
            "type": [
                "creation"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 23010
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "name": "Agent Backup Job 1 - 127.0.0.1",
                "object": "\"<changes><object",
                "type": "12000"
            }
        }
    }
    	
	```


=== "event_10.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=110 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" JobType=\"12000\" Platform=\"6\" Flags=\"1\" Version=\"1\" Description=\"Agent Backup job 'Agent Backup Job 1 - 127.0.0.1' has been started by user NT AUTHORITY\\SYSTEM.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "Agent Backup job 'Agent Backup Job 1 - 127.0.0.1' has been started by user NT AUTHORITY\\SYSTEM.",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 110
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12000"
            }
        }
    }
    	
	```


=== "event_11.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=890 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" Result=\"0\" JobType=\"12005\" WillBeRetried=\"False\" Version=\"1\" Description=\"The Rescan job 'Rescan of Agent Backup Job 1' has finished with Success state.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "The Rescan job 'Rescan of Agent Backup Job 1' has finished with Success state.",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 890
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12005"
            }
        }
    }
    	
	```


=== "event_12.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=42290 param1=\"0\" param2=\"0\" param3=\"0\" param4=\"0\" ChangesXML=\"<changes><object><property internal=\"IsEnabledInlineScanning\" type=\"Boolean\"><old>False</old><new>True</new></property><property internal=\"InlineScanningSensitivity\" type=\"ERansomwareScanningSensitivity\"><old /><new>Normal</new></property></object></changes>\" UserName=\"example.com\\jdoe\" Version=\"1\" Description=\"Malware detection settings have been changed.\"]",
        "event": {
            "category": [
                "malware"
            ],
            "reason": "Malware detection settings have been changed.",
            "type": [
                "info"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "related": {
            "user": [
                "jdoe"
            ]
        },
        "user": {
            "domain": "example.com",
            "name": "jdoe"
        },
        "veeam": {
            "instance": {
                "id": 42290
            },
            "job": {
                "object": "\"<changes><object><property"
            }
        }
    }
    	
	```


=== "event_13.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=10010 OibID=\"11111111-2222-4333-4444-555555555555\" OriginalOibID=\"11111111-2222-4333-4444-555555555555\" VmRef=\"11111111-2222-4333-4444-555555555555\" VmName=\"127.0.0.1\" ServerName=\"This server\" DateTime=\"12/19/2023 10:35:56\" IsCorrupted=\"False\" Platform=\"6\" StorageSize=\"35864576\" RepositoryID=\"11111111-2222-4333-4444-555555555555\" IsFull=\"True\" Version=\"1\" Description=\"VM '127.0.0.1' restore point has been created.\"]",
        "event": {
            "category": [
                "file"
            ],
            "reason": "VM '127.0.0.1' restore point has been created.",
            "type": [
                "creation"
            ]
        },
        "@timestamp": "2023-12-19T10:35:56Z",
        "host": {
            "ip": [
                "127.0.0.1"
            ]
        },
        "observer": {
            "name": "This server",
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "related": {
            "ip": [
                "127.0.0.1"
            ]
        },
        "veeam": {
            "instance": {
                "id": 10010
            },
            "vm": {
                "ref": "11111111-2222-4333-4444-555555555555"
            }
        }
    }
    	
	```


=== "event_14.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=150 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" JobType=\"12000\" TaskSessionID=\"11111111-2222-4333-4444-555555555555\" OibID=\"11111111-2222-4333-4444-555555555555\" OriginalOibID=\"11111111-2222-4333-4444-555555555555\" CreationTime=\"12/19/2023 10:35:56\" Status=\"5\" SourceHostName=\"MyMachine\" VmRef=\"11111111-2222-4333-4444-555555555555\" VmName=\"127.0.0.1\" TransferredGb=\"0.031\" Platform=\"6\" IsEntry=\"False\" Version=\"1\" Description=\"VM 127.0.0.1 task has finished with 'InProgress' state.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "VM 127.0.0.1 task has finished with 'InProgress' state.",
            "type": [
                "end"
            ]
        },
        "host": {
            "ip": [
                "127.0.0.1"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "related": {
            "ip": [
                "127.0.0.1"
            ]
        },
        "veeam": {
            "instance": {
                "id": 150
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12000"
            },
            "vm": {
                "ref": "11111111-2222-4333-4444-555555555555"
            }
        }
    }
    	
	```


=== "event_15.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=790 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" param3=\"0\" JobType=\"12003\" Platform=\"6\" WillBeRetried=\"False\" Version=\"1\" Description=\"Agent Backup job 'Agent Backup Job 1' finished with Success. All objects have been backed up successfully.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "Agent Backup job 'Agent Backup Job 1' finished with Success. All objects have been backed up successfully.",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 790
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12003"
            }
        }
    }
    	
	```


=== "event_16.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=810 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" JobType=\"12005\" Flags=\"0\" Version=\"1\" Description=\"Rescan job 'Rescan of 127.0.0.1' has been started.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "Rescan job 'Rescan of 127.0.0.1' has been started.",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 810
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12005"
            }
        }
    }
    	
	```


=== "event_17.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=890 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" Result=\"0\" JobType=\"12005\" WillBeRetried=\"False\" Version=\"1\" Description=\"The Rescan job 'Rescan of 127.0.0.1' has finished with Success state.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "The Rescan job 'Rescan of 127.0.0.1' has finished with Success state.",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 890
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12005"
            }
        }
    }
    	
	```


=== "event_18.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=29100 ProtectionGroupID=\"11111111-2222-4333-4444-555555555555\" ProtectionGroupName=\"Protection Group 1\" UserName=\"example.com\\jdoe\" Version=\"1\" Description=\"Protection Group Protection Group 1 has been added.\"]",
        "event": {
            "category": [
                "configuration"
            ],
            "reason": "Protection Group Protection Group 1 has been added.",
            "type": [
                "creation"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "related": {
            "user": [
                "jdoe"
            ]
        },
        "user": {
            "domain": "example.com",
            "name": "jdoe"
        },
        "veeam": {
            "instance": {
                "id": 29100
            },
            "protection": {
                "group": {
                    "id": "11111111-2222-4333-4444-555555555555",
                    "name": "Protection Group 1"
                }
            }
        }
    }
    	
	```


=== "event_19.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=810 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" JobType=\"12005\" Flags=\"1\" Version=\"1\" Description=\"Rescan job 'Rescan of Protection Group 1' has been started by user MyMachine\\jdoe.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "Rescan job 'Rescan of Protection Group 1' has been started by user MyMachine\\jdoe.",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 810
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12005"
            }
        }
    }
    	
	```


=== "event_20.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=890 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" Result=\"0\" JobType=\"12005\" WillBeRetried=\"False\" Version=\"1\" Description=\"The Rescan job 'Rescan of Protection Group 1' has finished with Success state.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "The Rescan job 'Rescan of Protection Group 1' has finished with Success state.",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 890
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12005"
            }
        }
    }
    	
	```


=== "event_21.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=710 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" JobType=\"12003\" Platform=\"6\" Flags=\"0\" Version=\"1\" Description=\"Agent Backup job 'Agent Backup Job 1' has been started.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "Agent Backup job 'Agent Backup Job 1' has been started.",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 710
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12003"
            }
        }
    }
    	
	```


=== "event_22.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=110 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" JobType=\"12000\" Platform=\"6\" Flags=\"0\" Version=\"1\" Description=\"Agent Backup job 'Agent Backup Job 1 - 127.0.0.1' has been started.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "Agent Backup job 'Agent Backup Job 1 - 127.0.0.1' has been started.",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 110
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12000"
            }
        }
    }
    	
	```


=== "event_23.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=790 JobSessionID=\"11111111-2222-4333-4444-555555555555\" JobID=\"11111111-2222-4333-4444-555555555555\" param3=\"0\" JobType=\"12003\" Platform=\"6\" WillBeRetried=\"True\" Version=\"1\" Description=\"Agent Backup job 'Agent Backup Job 1' finished with Success. All objects have been backed up successfully.\"]",
        "event": {
            "category": [
                "process"
            ],
            "reason": "Agent Backup job 'Agent Backup Job 1' finished with Success. All objects have been backed up successfully.",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "veeam": {
            "instance": {
                "id": 790
            },
            "job": {
                "id": "11111111-2222-4333-4444-555555555555",
                "type": "12003"
            }
        }
    }
    	
	```


=== "event_24.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=10050 OibID=\"11111111-2222-4333-4444-555555555555\" OriginalOibID=\"11111111-2222-4333-4444-555555555555\" VmRef=\"11111111-2222-4333-4444-555555555555\" VmName=\"127.0.0.1\" ServerName=\"This server\" DateTime=\"12/22/2023 15:27:59\" IsCorrupted=\"False\" Platform=\"6\" StorageSize=\"53710848\" RepositoryID=\"11111111-2222-4333-4444-555555555555\" IsFull=\"False\" Version=\"1\" Description=\"Restore point for VM '127.0.0.1' has been removed by user example.com\\jdoe.\"]",
        "event": {
            "category": [
                "file"
            ],
            "reason": "Restore point for VM '127.0.0.1' has been removed by user example.com\\jdoe.",
            "type": [
                "deletion"
            ]
        },
        "@timestamp": "2023-12-22T15:27:59Z",
        "host": {
            "ip": [
                "127.0.0.1"
            ]
        },
        "observer": {
            "name": "This server",
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "related": {
            "ip": [
                "127.0.0.1"
            ],
            "user": [
                "jdoe"
            ]
        },
        "user": {
            "domain": "example.com",
            "name": "jdoe"
        },
        "veeam": {
            "instance": {
                "id": 10050
            },
            "vm": {
                "ref": "11111111-2222-4333-4444-555555555555"
            }
        }
    }
    	
	```


=== "event_25.json"

    ```json
	
    {
        "message": "[categoryId=0 instanceId=111111 JobID=\"000000000-0000000000-000000000-000000000\" JobType=\"0\" Platform=\"N\\A\" JobName=\"TEST_BACKUP\" ChangesXML=\"11111232323(BDD_TEST_01)\" UserName=\"example.com\\Administrator\" VbrHostName=\"example.com\" VbrVersion=\"1.2.3.4\" Version=\"1\" Description=\"'1' objects has been deleted for 'TEST_BACKUP'.\"]",
        "event": {
            "category": [
                "configuration"
            ],
            "reason": "'1' objects has been deleted for 'TEST_BACKUP'.",
            "type": [
                "deletion"
            ]
        },
        "observer": {
            "product": "Veeam Backup & Replication",
            "vendor": "Veeam"
        },
        "related": {
            "user": [
                "Administrator"
            ]
        },
        "user": {
            "domain": "example.com",
            "name": "Administrator"
        },
        "veeam": {
            "instance": {
                "id": 111111
            },
            "job": {
                "id": "000000000-0000000000-000000000-000000000",
                "name": "TEST_BACKUP",
                "object": "11111232323(BDD_TEST_01)",
                "type": "0"
            }
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`agent.name` | `keyword` | Custom name of the agent. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`host.ip` | `ip` | Host ip addresses. |
|`host.name` | `keyword` | Name of the host. |
|`observer.name` | `keyword` | Custom name of the observer. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`user.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.name` | `keyword` | Short name or login of the user. |
|`veeam.credentials.id` | `keyword` | Credentials ID |
|`veeam.instance.id` | `long` | Instance ID |
|`veeam.job.id` | `keyword` | Job identifier |
|`veeam.job.name` | `keyword` | Job name |
|`veeam.job.object` | `keyword` | Job object |
|`veeam.job.type` | `keyword` | Job type |
|`veeam.protection.group.id` | `keyword` | ID of the protection group |
|`veeam.protection.group.name` | `keyword` | Name of the protection group |
|`veeam.vm.ref` | `keyword` | Reference of the used virtual machine |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Veeam/veeam_backup).