# Authentications

In order to simplify the recognition and semantic interpretation of authentications, it is necessary to respect some standardization.

An authentication is fully recognized as valid when all of these three fields are completed:

- event.category : with the value `authentication`
- event.type : with the value `start`
- action.outcome : with the value `success` if the authentication successed or `failure` else

Other fields are necessary in order to be able to fully describe the authentication. These fields are described in the table below. This list is not exhaustive, do not hesitate to fill in as many fields as possible.

| Field                       | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| event.action                | Logon action type                                                    |
| event.reason                | Reason type                                                          |
| sekoiaio.client.name        | Hostname from which authentication is requested                      |
| sekoiaio.client.os.type     | OS type of the host from which authentication is requested           |
| client.domain               | Domain of the host from which authentication is requested            |
| client.ip                   | IP of the host from which authentication is requested                |
| client.geo.country_iso_code | ISO COUNTRY CODE of the host from which authentication is requested  |
| sekoiaio.server.name        | Host name  targeted by the authentication                            |
| sekoiaio.server.os.type     | OS type of the host targeted by the authentication                   |
| server.domain               | Host domain targeted by the authentication                           |
| server.ip                   | Host IP targeted by the authentication                               |
| server.geo.country_iso_code | Host geoloc targeted by the authentication                           |
| sekoiaio.authentication.process.name | process name has perfomed authentication (i.e., sshd, kerberos, ...) |
| user.name                   | user name has requested authentication                               |
| user.domain                 | user domain has requested authentication                             |
| user.id                     | user id has requested authentication                                 |
| user.email                  | user email has requested authentication                              |
| user.target.name            | user name targeted by the authentication                             |
| user.target.domain          | user domain targeted by the authentication                           |
| user.target.id              | user id targeted by the authentication                               |
| user.target.email           | user email targeted by the authentication                            |


You can also extract some additional information like urls, user agent, ...

## Application authentications

### How to parse authentication events

These following examples describe a set of successfully authentications.

#### AWS Cloudtrail

```JSON
{
  "additionalEventData": {
    "LoginTo": "https://console.aws.amazon.com/billing/home?region=eu-west-3&state=hashArgs%23%2F&isauthcode=true",
    "MFAUsed": "No",
    "MobileVersion": "No"
  },
  "awsRegion": "us-east-1",
  "eventID": "9d4ca355-a7d3-4422-96ae-dbe2c3431609",
  "eventName": "ConsoleLogin", # (1)
  "eventSource": "signin.amazonaws.com",
  "eventTime": "2020-08-19T15:33:43Z",
  "eventType": "AwsConsoleSignIn",
  "eventVersion": "1.05",
  "recipientAccountId": "1111111111",
  "requestParameters": null,
  "responseElements": {
    "ConsoleLogin": "Success" # (2)
  },
  "sourceIPAddress": "1.2.3.4",
  "userAgent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
  "userIdentity": {
    "accessKeyId": "",
    "accountId": "1111111111",
    "arn": "arn:aws:iam::1111111111:root",
    "principalId": "1111111111", # (3)
    "type": "Root"
  }
}
```

1. The eventName allows to determine the `event.category` and `event.type`
2. The outcome of the event
3. The identifier of the mandatary user

Will result into this ECS document:

```json
{
  "event": {
    "category": ["authentication"],
    "type": ["start"]
  },
  "user": {
    "id": "1111111111"
  },
  "action": {
    "outcome": "success"
  },
  "client": {
    "ip": "1.2.3.4"
  }
}
```

#### Salesforce

```JSON
{
  "EVENT_TYPE": "Login", # (1)
  "USER": "john.doe@example.com", # (3)
  "LOGIN_STATUS": "Success", # (2)
  "IP_ADDRESS": "192.168.0.1",
  "LOGIN_TIME": "2023-07-03T10:15:00Z",
  "DEVICE_TYPE": "Desktop",
  "BROWSER": "Chrome",
  "PLATFORM": "Windows 10",
  "LOGIN_GEO_LOCATION": "San Francisco, CA",
  "SESSION_ID": "ABC123XYZ",
  "LOGIN_URL": "https://login.salesforce.com"
}
```

1. The field EVENT_TYPE is used to determine the `event.category` and `event.type`
2. The outcome of the event
3. The email of the user

Will result into this ECS document

```json
{
  "event": {
    "category": ["authentication"],
    "type": ["start"]
  },
  "user": {
    "email": "john.doe@example.org"
  },
  "action": {
    "outcome": "success"
  },
  "client": {
    "ip": "192.168.0.1"
  },
  "url": {
    "original": "https://login.salesforce.com"
  }
}
```

#### RSA SecurID

```
11:23:02,069, example.intranet, audit.runtime.com.rsa.ims.authn.impl.AuthenticationBrokerImpl, INFO, da0011b4f66e4b7e86f90f9dd6e937e7,0e34d92f7c6549b19ed28471c02a049b,5.6.7.8,1.2.3.4,AUTHN_LOGIN_EVENT,13002,SUCCESS,AUTHN_METHOD_SUCCESS,e7ec7ff59d604a2ba3fa09067bbd65a4-L0+/miv3k62B,39b1319237f946428aecf267190b537d,09f1f5fc30e947ce9e564d5a91745091,000000000000000000001000e0011000,HDTCO04,HDTCO04,,559eb5ec2d43408cbce2a43b65eafe8c,000000000000000000001000e0011000,1.2.3.4,source.hostname,000000000000000000002000f1022000,SecurID_Native,,,AUTHN_LOGIN_EVENT,6,4,,,,,da624c0ecf554764953fcc346b999682,000523656192,,
```

1. The value `AUTHN_LOGIN_EVENT` is used to determine the `event.category` and `event.type`
2. The value `SUCCESS` is used to define the outcome
3. The column 15 as the user identifier
4. The column 18 as the user name
5. The column 23 as the client ip
6. The column 24 as the client name
7. The column 3 as the server name

Will result into this ECS document

```json
{
  "event": {
    "category": ["authentication"],
    "type": ["start"]
  },
  "user": {
    "id": "39b1319237f946428aecf267190b537d",
    "name": "HDTCO04"
  },
  "action": {
    "outcome": "success"
  },
  "client": {
    "ip": "1.2.3.4"
  },
  "sekoiaio": {
    "client": {
      "name": "source.hostname"
    },
    "server": {
      "name": "example.intranet"
    }
  }
}
```

### How to write a good smart-description for authentication events

From the previous samples, we can build the following smart-description:

```json
{
  "value": "{user.name} signed in from {sekoiaio.client.name} ({client.ip})",
  "conditions": [
     {"field": "event.category", "value": "authentication"},
     {"field": "event.type", "value": "start"},
     {"field": "user.name"},
     {"field": "sekoiaio.client.name"},
     {"field": "client.ip"}
  ]
}
```

For the AWS cloudtrail event, this smart-description will result into:

`1111111111 signed in from source.hostname (1.2.3.4)`

However, If you extract more information from the event, you can improve the smart-description:

```json
{
  "value": "{user.name} signed in from {sekoiaio.client.name} ({client.ip}) on {url.original}",
  "conditions": [
     {"field": "event.category", "value": "authentication"},
     {"field": "event.type", "value": "start"},
     {"field": "user.name"},
     {"field": "sekoiaio.client.name"},
     {"field": "client.ip"},
     {"field": "url.original"}
  ]
}
```

For the Salesforce event, this smart-description will result into:

`john.doe@example.org signed in from source.hostname (192.168.0.1) on https://login.salesforce.com`

## Windows OS authentications

Sources:

- [microsoft.com: 4624(S): An account was successfully logged on.](https://learn.microsoft.com/fr-fr/windows/security/threat-protection/auditing/event-4624)
- [microsoft.com: 4625(F): An account failed to log on.](https://learn.microsoft.com/fr-fr/windows/security/threat-protection/auditing/event-4625)

### action.outcome

For Windows events, we can map `action.id` with `action.outcome` as follow:

| action.id | action.outcome |
| --------- | -------------- |
| 4624      | `success`      |
| 4625      | `failure`      |

### event.action

For Windows events, we can map `action.properties.LogonType` with `event.action` as follow:

| action.properties.LogonType | event.action                             |
| --------------------------- | ---------------------------------------- |
| 2	                          | authentication_interactive               |
| 3	                          | authentication_network                   |
| 4	                          | authentication_batch                     |
| 5	                          | authentication_service                   |
| 7	                          | authentication_unlock                    |
| 8	                          | authentication_network_cleartext         |
| 9	                          | authentication_alternative_credentials   |
| 10                          | authentication_remote_interactive        |
| 11                          | authentication_cached_interactive        |
| 12                          | authentication_cached_remote_interactive |
| 13                          | authentication_cached_unlock             |

### event.reason

For Windows events, we can map `action.properties.SubStatus` with `event.reason` as follow:

| action.properties.SubStatus | event.reason                             |
| --------------------------- | ---------------------------------------- |
| 0xC0000064                  | user_not_exist                           |
| 0xC000006A                  |	bad_password                             |
| 0xC0000234                  |	user_locked_out                          |
| 0xC0000072                  |	user_disabled                            |
| 0xC000006F                  |	time_restriction                         |
| 0xC0000070                  |	policy_restriction                       |
| 0xC0000193                  |	account_expired                          |
| 0xC0000071                  |	password_expired                         |
| 0xC0000133                  |	clock_not_sync                           |
| 0xC0000224                  |	need_to_update_password                  |
| 0xC0000225                  |	os_problem                               |
| 0xc000015b                  |	user_not_granted                         |


### Parsing example for a Windows authentication

#### Success authentication example
This event represents a successful authentication on a Windows host collected through a nxlog collector.

```
{
  "EventTime": "2010-06-18 15:28:23",
  "Hostname": "V-FOO",
  "Keywords": -9214364837600034816,
  "EventType": "AUDIT_SUCCESS",
  "SeverityValue": 2,
  "Severity": "INFO",
  "EventID": 4624,
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "ProviderGuid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
  "Version": 1,
  "Task": 12544,
  "OpcodeValue": 0,
  "RecordNumber": 10457874880,
  "ProcessID": 744,
  "ThreadID": 2352,
  "Channel": "Security",
  "Category": "Logon",
  "Opcode": "Info",
  "SubjectUserSid": "S-1-0-0",
  "SubjectUserName": "-",
  "SubjectDomainName": "-",
  "SubjectLogonId": "0x0",
  "TargetUserSid": "S-1-5-21-1574594750-1263408776-2012955550-69701",
  "TargetUserName": "SVC_DD_SP-SEARCH",
  "TargetDomainName": "KEY",
  "TargetLogonId": "0xfbee0744",
  "LogonType": "3",
  "LogonProcessName": "NtLmSsp ",
  "AuthenticationPackageName": "NTLM",
  "WorkstationName": "V-FOO",
  "LogonGuid": "{00000000-0000-0000-0000-000000000000}",
  "TransmittedServices": "-",
  "LmPackageName": "NTLM V2",
  "KeyLength": "128",
  "ProcessName": "-",
  "IpAddress": "-",
  "IpPort": "-",
  "ImpersonationLevel": "%%1833",
  "EventReceivedTime": "2010-06-18 15:28:24",
  "SourceModuleName": "in",
  "SourceModuleType": "im_msvistalog"
}
```

The previous event will result into this ECS document:

```json
{
  "event": {
    "code": "4624",
    "provider": "Microsoft-Windows-Security-Auditing",
    "category": [
      "authentication"
    ],
    "type": [
      "start"
    ],
    "action": "authentication_network"
  },
  "sekoiaio": {
    "client": {
      "os": {
        "type": "windows"
      },
      "name": "V-FOO"
    },
    "server": {
      "name": "V-FOO",
      "os": {
        "type": "windows"
      }
    },
    "authentication": {
      "process": {
        "name": "NtLmSsp "
      }
    }
  },
  "action": {
    "outcome": "success"
  },
  "host": {
    "name": "V-FOO"
  },
  "process": {
    "thread": {
      "id": 2352
    },
    "pid": 744,
    "id": 744
  },
  "user": {
    "id": "S-1-0-0",
    "target": {
      "name": "SVC_DD_SP-SEARCH",
      "domain": "KEY",
      "id": "S-1-5-21-1574594750-1263408776-2012955550-69701"
    },
    "name": "-",
    "domain": "-"
  }
}
```

With the following smart-description:

```json
{
  "value": "{user.target.domain}\\{user.target.name} logged on to {sekoiaio.server.name} ({event.action})",
  "relationships": [
    {
      "source": "user.target.name",
      "target": "sekoiaio.server.name",
      "type": "event.action"
    }
  ],
  "conditions": [
    {"field": "event.category", "value": "authentication"},
    {"field": "event.type", "value": "start"},
    {"field": "action.outcome", "value": "success"},
    {"field": "event.action"},
    {"field": "user.target.name"},
    {"field": "user.target.domain"},
    {"field": "sekoiaio.server.name"},
    {"field": "event.provider", "value": "Microsoft-Windows-Security-Auditing"}
  ]
}
```

Will result into the description:

`KEY\\SVC_DD_SP-SEARCH logged on to V-FOO (authentication_network)`


#### Failure authentication example
This event represents a failing authentication on a Windows host collected through a nxlog collector.

```
{
  "ProcessName": "-",
  "Channel": "Security",
  "Hostname": "vm-foo",
  "LogonType": "3",
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "IpPort": "-",
  "Severity": "Info",
  "SubjectLogonId": "0x3e7",
  "SubjectUserName": "VM-FOO$",
  "EventID": "4625",
  "IpAddress": "-",
  "SubjectDomainName": "CORPDOMAIN",
  "ProcessId": "0x354",
  "LogonProcessName": "Schannel",
  "SubjectUserSid": "S-1-5-18",
  "TargetUserSid": "S-1-0-0"
}
```

The previous event will result into this ECS document:

```json
{
  "event": {
    "code": "4625",
    "provider": "Microsoft-Windows-Security-Auditing",
    "category": [
      "authentication"
    ],
    "type": [
      "start"
    ],
    "action": "authentication_network"
  },
  "sekoiaio": {
    "client": {
      "os": {
        "type": "windows"
      },
      "name": "vm-foo"
    },
    "server": {
      "name": "vm-foo",
      "os": {
        "type": "windows"
      }
    },
    "authentication": {
      "process": {
        "name": "Schannel"
      }
    }
  },
  "action": {
    "outcome": "failure"
  },
  "host": {
    "name": "vm-foo"
  },
  "user": {
    "id": "S-1-5-18",
    "target": {
      "id": "S-1-0-0"
    },
    "name": "VM-FOO$",
    "domain": "CORPDOMAIN"
  }
}
```

With the following smart-description:

```json
{
  "value": "{user.target.domain}\\{user.target.name} failed to log on to {sekoiaio.server.name} ({event.action})",
  "relationships": [
    {
      "source": "user.target.name",
      "target": "sekoiaio.server.name",
      "type": "event.action"
    }
  ],
  "conditions": [
    {"field": "event.category", "value": "authentication"},
    {"field": "event.type", "value": "start"},
    {"field": "action.outcome", "value": "failure"},
    {"field": "event.action"},
    {"field": "user.target.name"},
    {"field": "user.target.domain"},
    {"field": "sekoiaio.server.name"},
    {"field": "event.provider", "value": "Microsoft-Windows-Security-Auditing"}
  ]
}
```

Will result into the description:

`KEY\\SVC_DD_SP-SEARCH logged on to V-FOO (authentication_network)`

