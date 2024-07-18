# 🌟 Event Standardization for EDR Systems

To ensure consistent recognition and semantic interpretation of EDR (Endpoint Detection and Response) events, we follow the standardization guidelines bellow. We recommend users to adopt the same guidelines for their EDR custom format. The already supported EDR systems include SentinelOne, HarfangLab, CrowdStrike, Cybereason, Sophos, Stormshield, Symantec, Tehtris, TrendMicro, and WithSecure.

## 📋 Recommended Fields

| **Field**        | **Description**                                | **Examples of values**                          |
|------------------|------------------------------------------------|-------------------------------------------------|
| `action.type`    | Specifies the action taken by the EDR system.  | `block`, `allow`, `alert`                       |
| `event.category` | The high-level category of the event.          | `malware`, `intrusion`, `policy`                |
| `event.code`     | A unique identifier or code representing the event. | `12345`, `67890`, `ABCDE`                     |
| `event.kind`     | Describes the kind of event.                    | `event`, `alert`, `metric`                      |
| `event.dataset`  | Specifies the dataset used by the EDR system.  | `sentinelone`, `harfanglab`, `crowdstrike`, `cybereason`, `sophos`, `stormshield`, `symantec`, `tehtris`, `trendmicro`, `withsecure` |
| `event.severity` | The severity level of the event.               | `low`, `medium`, `high`, `critical`             |

## 🛠️ Optional Fields

To provide more context and enhance the description of the events, including additional fields is encouraged. The following optional fields can be used:

| **Field**               | **Description**                                 | **Examples**                                     |
|-------------------------|-------------------------------------------------|--------------------------------------------------|
| `host.name`             | Name of the host where the event occurred.       | `host-123`                                       |
| `user.id`               | The unique identifier of the user involved in the event. | `user-456`                                |
| `process.name`          | The process name that triggered the event/alert.    | `malware.exe`                                    |
| `process.pid`           | The process ID that triggered the event/alert.      | `2345`                                           |
| `process.commandline`   | The command that launched the process.          | `sudo deluser toto`                              |
| `file.hash`             | The hash of the file related to the event.      | `abcdef1234567890`                               |
| `agent.id`              | The unique ID of the agent that detected the event. | `12313-21341623`                             |
| `agent.name`            | The name of the agent that detected the event.  | `harfanglab`                                     |
| `host.hostname`         | The hostname that generated the event.           | `user admin`                                     |
| `host.os.full`          | The OS of the host that generated the event.     | `Windows 11 Enterprise`, `Ubuntu 22.04`          |
| `host.domain`           | The domain of the host that generated the event. | `Workgroup`                                      |

## Examples of event parsing
In this section, raw events extracted from real use cases are used to show the expected parsing outcome. For each example, the input will be a raw event in json format and the output will be in ECS.

    
### HarfangLab EDR
This is a HarfangLab EDR alert that was triggered by Harfang agent in a Windows machine. The related event is the creation of a new local user by a Powershell.

**Raw Event Before Parsing**    
```json
    {
      "maturity": "stable",
      "@version": "1",
      "alert_unique_id": "abff9ea2-6e76-49f6-906b-c3cf32cb04e6",
      "status": "new",
      "quarantine": 4,
      "type": "rtlogs",
      "aggregation_key": "ccccd34ff9422ae4d80654c35137b25aa5424116a73723c87590d825d71c05cf",
      "level_int": 20,
      "rule_id": "742a1f89-039d-459e-b772-50a881353a76",
      "detection_date": "2024-07-12T08:13:14.258+00:00",
      "rule_content": "title: Local User Created via PowerShell",
      "groups": [],
      "level": "low",
      "threat_key": 38,
      "tags": [
        "attack.persistence",
        "attack.t1136.001"
      ],
      "tenant": "448da7e0536dffb4",
      "details_powershell": {
        "PowershellCommand": "New-LocalUser -Name User9549 -Password (ConvertTo-SecureString -AsPlainText \"Password123\" -Force)",
        "PowershellScriptPath": ""
      },
      "threat_values": [
        "1553619e-8271-4941-8e10-9153e99cc5dc",
        "Local User Created via PowerShell"
      ],
      "threat_type": "agent_rule",
      "@event_create_date": "2024-07-12T08:13:14.258Z",
      "@timestamp": "2024-07-12T08:13:14.430Z",
      "msg": "Detects the usage of PowerShell to create a new local user.\n Attackers can create new users to achieve persistence.",
      "execution": 0,
      "mitre_cells": [
        "persistence__t1136.001"
      ],
      "image_name": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
      "ingestion_date": "2024-07-12T08:13:14.430+00:00",
      "alert_time": "2024-07-12T08:13:14.430+00:00",
      "alert_subtype": "process",
      "process": {
        "current_directory": "C:\\Users\\administrateur\\",
        "parent_integrity_level": "High",
        "status": 0,
        "logonid": 1348216,
        "grandparent_image": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
        "pid": 10880,
        "fake_parent_image": "",
        "signature_info": {
          "signer_info": {
            "thumbprint": "71f53a26bb1625e466727183409a30d03d7923df",
            "thumbprint_sha256": "ce08760345bd5a18aa9091e6f083522ad593bd42f587699e025afd55be589334",
            "serial_number": "330000045ff3c96c1a7ff7da1d00000000045f",
            "issuer_name": "Microsoft Windows Production PCA 2011",
            "display_name": "Microsoft Windows"
          },
          "root_info": {
            "thumbprint": "3b1efd3a66ea28b16697394703a72ca340a05bd5",
            "thumbprint_sha256": "df545bf219a2439c36983b54cdfc903dfa4f37d3996d8d84b4c31eec6f3c163e",
            "serial_number": "28cc3a25bfba44ac449a9b586b4339aa",
            "issuer_name": "Microsoft Root Certificate Authority 2010",
            "display_name": "Microsoft Root Certificate Authority 2010"
          },
          "signed_authenticode": false,
          "signed_catalog": true
        },
        "pe_imphash": "AFACF6DC9041114B198160AAB4D0AE77",
        "grandparent_integrity_level": "High",
        "parent_unique_id": "93086cd1-8271-4941-0c11-000cb3115df3",
        "ancestors": "C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.12_3.12.1264.0_x64__qbz5n2kfra8p0\\python3.12.exe|C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe|C:\\Users\\administrateur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe|C:\\Users\\administrateur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe|C:\\Windows\\explorer.exe|C:\\Windows\\System32\\userinit.exe|C:\\Windows\\System32\\winlogon.exe|C:\\Windows\\System32\\smss.exe|C:\\Windows\\System32\\smss.exe",
        "integrity_level": "High",
        "sigma_rule_content": "title: Local User Created via PowerShellw",
        "ppid": 4364,
        "process_unique_id": "93086cd1-8271-4941-802a-0039d517a425",
        "hashes": {
          "md5": "9d8e30eff21108092d5980c931876b7e",
     
        "session": 2,
        "log_platform_flag": 0,
        "grandparent_unique_id": "93086cd1-8271-4941-0429-0029050971a0",
        "dont_create_process": true,
        "parent_commandline": "C:\\Users\\administrateur\\AppData\\Local\\Microsoft\\WindowsApps\\python3.exe .\\normal-traffic.py --activities perform_user_management",
        "process_name": "powershell.exe",
        "username": "vm-windows\\administrateur",
        "fake_parent_commandline": "",
        "system_event_type": "powershell_event",
        "pe_timestamp_int": 144346722,
        "size": 450560,
        "grandparent_commandline": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -noexit -command try { . \"c:\\Users\\administrateur\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\out\\vs\\workbench\\contrib\\terminal\\browser\\media\\shellIntegration.ps1\" } catch {}",
        "usersid": "S-1-5-21-3860028710-1894839758-596913598-500",
        "image_name": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
        "commandline": "powershell.exe -Command New-LocalUser -Name User9549 -Password (ConvertTo-SecureString -AsPlainText \"Password123\" -Force)",
        "parent_image": "C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.12_3.12.1264.0_x64__qbz5n2kfra8p0\\python3.12.exe",
        "fake_ppid": 0,
        "pe_timestamp": "1974-07-29T16:18:42.000Z",
        "create_time": "2024-07-12T08:13:13.221Z",
        "signed": true,
        "ioc_matches": [],
        "log_type": "process"
      },
      "agent": {
        "version": "3.10.2",
        "hostname": "vm-windows",
        "ostype": "windows",
        "osversion": "10.0.22631",
        "distroid": null,
        "domain": null,
        "agentid": "1553619e-8271-4941-8e10-9153e99cc5dc",
        "dnsdomainname": null,
        "osproducttype": "Windows 11 Enterprise",
        "domainname": "WORKGROUP",
        "additional_info": {}
      },
      "detection_origin": "agent",
      "rule_name": "Local User Created via PowerShell",
      "alert_type": "sigma",
      "log_type": "alert"
    }
    {
  "event": {
    "id": "00000000-0000-0000-0000-000000000000",
    "dataset": "alert",
    "kind": "alert",
    "type": "start",
    "category": "process"
  },
  "agent": {
    "id": "1553619e-8271-4941-8e10-9153e99cc5dc",
    "name": "harfanglab"
  },
  "@timestamp": "2024-07-12T08:13:14.258000Z",
  "host": {
    "domain": "WORKGROUP",
    "os": {
      "full": "Windows 11 Enterprise",
      "version": "10.0.22631"
    },
    "hostname": "vm-windows",
    "name": "vm-windows"
  },
  "log": {
    "hostname": "vm-windows"
  },
  "organization": {
    "id": "448da7f0536dffb4"
  },
  "harfanglab": {
    "groups": [],
    "process": {
      "powershell": {
        "command": "New-LocalUser -Name User9549 -Password (ConvertTo-SecureString -AsPlainText \"Password123\" -Force)"
      }
    },
    "level": "low",
    "status": "new",
    "execution": 0,
    "alert_time": "2024-07-12T08:13:14.430+00:00",
    "alert_subtype": "process"
  },
  "rule": {
    "id": "742a1f89-039d-459e-b772-50a881353a76",
    "name": "Local User Created via PowerShell",
    "category": "sigma",
    "description": "Detects the usage of PowerShell to create a new local user. Attackers can create new users to achieve persistence."
  },
  "user": {
    "name": "vm-windows\\administrateur"
  },
  "process": {
    "pid": 10880,
    "name": "powershell.exe",
    "executable": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
    "command_line": "powershell.exe -Command New-LocalUser -Name User9549 -Password (ConvertTo-SecureString -AsPlainText \"Password123\" -Force)",
    "working_directory": "C:\\Users\\administrateur\\"
  },
  "file": {
    "hash": {
      "md5": "9d8e30daf21108092d5980c931876b7e"
    }
  },
  "hosts": [
    "vm-windows"
  ],
  "user": [
    "vm-windows\\ad"
  ]
}
```
  
### Crowdstrike Falcon
Let’s take a look to another EDR example and see how the different ECS fields extracted from the raw event.
    
**Raw Event Before Parsing**
    
```json
    {
        "metadata": {
            "customerIDString": "d1f2145b3a034de8ab4183caf2f04fc1",
            "offset": 29314494,
            "eventType": "DetectionSummaryEvent",
            "eventCreationTime": 1719928251000,
            "version": "1.0"
        },
        "event": {
            "ProcessStartTime": 1719928251,
            "ProcessEndTime": 1719928286,
            "ProcessId": 1719928251086056200,
            "ParentProcessId": 1719928251069954800,
            "ComputerName": "linux-vm",
            "UserName": "root",
            "DetectName": "Known Malware",
            "DetectDescription": "A suspicious process related to a likely malicious file was launched. Review any binaries 
    involved as they may be related to malware.",
            "Severity": 4,
            "SeverityName": "High",
            "FileName": "git",
            "FilePath": "/usr/bin/",
            "CommandLine": "git clone https://github.com/redcanaryco/atomic-red-team.git",
            "SHA256String": "29aa689f38158d2e8941fa54e436f0260890af31cecad1e8799e5c2df7bc1ecc",
            "MD5String": "675853ca01ec441df7a015b91a7e1272",
            "SHA1String": "0000000000000000000000000000000000000000",
            "MachineDomain": "",
            
            "FalconHostLink": 
    "https://falcon.eu-1.crowdstrike.com/activity/detections/detail/59ad3c811b3c42aeb70af4f6b547830f/266290477136?_cid=g050007dwaanfoynhxtktq44fxufrgse",
            "SensorId": "59ad3c811b3c42aeb70af4f6b547830f",
            "DetectId": "ldt:59ad3c811b3c42aeb70af4f6b547830f:266290477136",
            "LocalIP": "172.17.0.1",
            "MACAddress": "02-42-a1-71-d8-a9",
            "Tactic": "Malware",
            "Technique": "Malicious File",
            "Objective": "Falcon Detection Method",
            "PatternDispositionDescription": "Detection, process would have been killed if related prevention policy setting
     was enabled.",
            "PatternDispositionValue": 272,
            "PatternDispositionFlags": {
                "Indicator": false,
                "Detect": false,
                "InddetMask": false,
                "SensorOnly": false,
                "Rooting": false,
                "KillProcess": true,
                "KillSubProcess": false,
                "QuarantineMachine": false,
                "QuarantineFile": false,
                "PolicyDisabled": true,
                "KillParent": false,
                "OperationBlocked": false,
                "ProcessBlocked": false,
                "RegistryOperationBlocked": false,
                "CriticalProcessDisabled": false,
                "BootupSafeguardEnabled": false,
                "FsOperationBlocked": false,
                "HandleOperationDowngraded": false,
                "KillActionFailed": false,
                "BlockingUnsupportedOrDisabled": false,
                "SuspendProcess": false,
                "SuspendParent": false
            },
            "ParentImageFileName": "/usr/bin/sudo",
            "ParentCommandLine": "sudo git clone https://github.com/redcanaryco/atomic-red-team.git",
            "GrandparentImageFileName": "/usr/bin/bash",
            "GrandparentCommandLine": "-bash",
            "HostGroups": "47286f6e248a444c9a5445adf3d2cbd4",
            "PatternId": 30115
        }
    }
```
    
In this example the fields `event.kind` , `event.type` and `event.category`  are correctly parsed respectively to 'alert', 'info' and 'category' because `metadata.eventType`is 'DetectionSummaryEvent'
    
The result after parsing is as follows :
    
**ECS Fields After parsing**
    
```json
    {
      "event": {
        "id": "00000000-0000-0000-0000-000000000000",
        "kind": "alert",
        "type": "info",
        "category": "intrusion_detection",
        "severity": 4
      },
      "sekoiaio": {
        "intake": {
          "dialect": "test",
          "dialect_uuid": "00000000-0000-0000-0000-000000000000",
          "parsing_status": "success"
        }
      },
      "@timestamp": "2024-07-02T13:50:51Z",
      "crowdstrike": {
        "event_type": "DetectionSummaryEvent",
        "detect_id": "ldt:59ad3c811b3c42aeb70af4f6b547830f:266290477136",
        "host_groups": "47286f6e248a444c9a5445adf3d2cbd4",
        "severity_name": "High",
        "detect_description": "A suspicious process related to a likely malicious file was launched. Review any binaries involved as they may be related to malware."
      },
      "host": {
        "ip": "172.17.0.1",
        "mac": "02-42-a1-71-d8-a9",
        "name": "linux-vm"
      },
      "user": {
        "name": "root"
      },
      "process": {
        "pid": 1719928251086056200,
        "name": "git",
        "parent": {
          "pid": 1719928251069954800,
          "name": "sudo",
          "executable": "/usr/bin/sudo",
          "command_line": "sudo git clone https://github.com/redcanaryco/atomic-red-team.git",
          "working_directory": "/usr/bin"
        },
        "command_line": "git clone https://github.com/redcanaryco/atomic-red-team.git",
        "working_directory": "/usr/bin/",
        "start": "2024-07-02T13:50:51Z",
        "end": "2024-07-02T13:51:26Z"
      },
      "log": {
        "hostname": "linux-vm"
      },
      "file": {
        "hash": {
          "md5": "675853ca01ec441df7a015b91a7e1272",
          "sha256": "29aa689f38158d2e8941fa54e436f0260890af31cecad1e8799e5c2df7bc1ecc"
        }
      },
      "threat": {
        "tactic": {
          "name": "Malware"
        },
        "technique": {
          "name": "Malicious File"
        },
        "indicator": {
          "description": "Detection, process would have been killed if related prevention policy setting was enabled."
        }
      },
      "related": {
        "hash": [
          "29aa689f38158d2e8941fa54e436f0260890af31cecad1e8799e5c2df7bc1ecc",
          "675853ca01ec441df7a015b91a7e1272"
        ],
        "ip": [
          "172.17.0.1"
        ],
        "user": [
          "root"
        ]
      }
    
```
    
!!! note
     Following these standards ensures that the EDR event data is consistent and can be easily interpreted and analyzed across different systems. This standardization helps in providing a unified view of security events and enhances the capability to respond to incidents efficiently.
