# Authentications

In order to simplify the recognition and semantic interpretation of authentications, it is necessary to respect some standardization.

An authentication is fully recognized as valid when all of these four fields are completed:

- event.category : with the value `authentication`
- event.type : with the value `start`
- action.outcome : with the value `success` if the authentication successed or `failure` else
- user.name, user.id or user.email: with the name, the identifier or the email of the principal

You can also extract some additional information like ip addresses, hostname or urls.

## Application authentications

### How to parse authentication events

These following examples describe a set of successfully authentications provided by an application or a Cloud application

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

1. The eventName allows to determine the event.category and event.type
2. The outcome of the event
3. The identifier of the principal

will result into this ECS document

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
  "source": {
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

1. The EVENT_TYPE allows to determine the event.category and event.type
2. The outcome of the event
3. The email of the principal

will result into this ECS document

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
  "source": {
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

1. The value AUTHN_LOGIN_EVENT allows to determine the event.category and event.type
2. The value SUCCESS allows to define the outcome
3. The 

will result into this ECS document

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
  "source": {
    "ip": "1.2.3.4"
  },
  "destination": {
    "address": "example.intranet"
  }
}
```

### How to write a good smart-description for authentication events

From the previous samples, we can build the following smart-description:

```json
{
  "value": "{user.name} sign in from {source.ip}",
  "conditions": [
     {"field": "event.category", "value": "authentication"},
     {"field": "event.type", "value": "start"},
     {"field": "user.name"},
     {"field": "source.ip"}
  ]
}
```

For the AWS cloudtrail event, this smart-description will result into:

`1111111111 sign in from 1.2.3.4`

However, If you extract more information from the event, you can improve the smart-description:

```json
{
  "value": "{user.name} sign in from {source.ip} on {url.original}",
  "conditions": [
     {"field": "event.category", "value": "authentication"},
     {"field": "event.type", "value": "start"},
     {"field": "user.name"},
     {"field": "source.ip"}
     {"field": "url.original"}
  ]
}
```

For the Salesforce event, this smart-description will result into:

`john.doe@example.org sign in from 192.168.0.1 on https://login.salesforce.com`

## OS authentications

Operating systems may provide further information about authentications.

Other fields are necessary in order to be able to fully describe the authentication. These fields are described in the table below

| Field                       | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| event.action                | Logon action type                                                    |
| event.reason                | Reason type                                                          |
| sekoiaio.client.name        | Hostname from which authentication is requested                      |
| sekoiaio.client.domain      | Domain of the host from which authentication is requested            |
| client.ip                   | IP of the host from which authentication is requested                |
| sekoia.client.os.type       | OS type of the host from which authentication is requested           |
| client.geo.country_iso_code | ISO COUNTRY CODE of the host from which authentication is requested  |
| process.name                | process name has perfomed authentication (i.e., sshd, kerberos, ...) |
| sekoiaio.server.name        | Host name  targeted by the authentication                            |
| sekoiaio.server.domain      | Host domain targeted by the authentication                           |
| server.ip                   | Host ip targeted by the authentication                               |
| server.os.type              | Host os targeted by the authentication                               |
| server.geo.country_iso_code | Host geoloc targeted by the authentication                           |
| client.user.name            | user name has requested authentication                               |
| client.user.domain          | user domain has requested authentication                             |
| client.user.id              | user id has requested authentication                                 |
| client.user.email           | user email has requested authentication                              |
| user.target.name            | user name targeted by the authentication                             |
| user.target.domain          | user domain targeted by the authentication                           |
| user.target.id              | user id targeted by the authentication                               |
| user.target.email           | user email targeted by the authentication                            |

In the following, we give concrete examples on different dialects, to help fill in these fields.


### An user authentication on a Windows Host

Sources:

- [https://learn.microsoft.com/fr-fr/windows/security/threat-protection/auditing/event-4624](https://learn.microsoft.com/fr-fr/windows/security/threat-protection/auditing/event-4624)
- [https://learn.microsoft.com/fr-fr/windows/security/threat-protection/auditing/event-4625](https://learn.microsoft.com/fr-fr/windows/security/threat-protection/auditing/event-4625)

#### action.outcome

For windows events, we can map action.id with action.outcome as follow:

| action.id | action.outcome |
| --------- | -------------- |
| 4624      | `success`      |
| 4625      | `failure`      |

#### event.action

For windows events, we can map `action.properties.LogonType` with `event.action` as follow:

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

#### event.reason

For windows events, we can map `action.properties.SubStatus` with `event.reason` as follow:

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


#### How to parse and describe a Windows authentication

This event represents a successful authentication on a Windows host collected through a nxlog collector.

```json
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
  "Message": "An account was successfully logged on.\r\n\r\nSubject:\r\n\tSecurity ID:\t\tS-1-0-0\r\n\tAccount Name:\t\t-\r\n\tAccount Domain:\t\t-\r\n\tLogon ID:\t\t0x0\r\n\r\nLogon Type:\t\t\t3\r\n\r\nImpersonation Level:\t\tImpersonation\r\n\r\nNew Logon:\r\n\tSecurity ID:\t\tS-1-5-21-1574594750-1263408776-2012955550-69701\r\n\tAccount Name:\t\tSVC_DD_SP-SEARCH\r\n\tAccount Domain:\t\tKEY\r\n\tLogon ID:\t\t0xFBEE0744\r\n\tLogon GUID:\t\t{00000000-0000-0000-0000-000000000000}\r\n\r\nProcess Information:\r\n\tProcess ID:\t\t0x0\r\n\tProcess Name:\t\t-\r\n\r\nNetwork Information:\r\n\tWorkstation Name:\tV-FOO\r\n\tSource Network Address:\t-\r\n\tSource Port:\t\t-\r\n\r\nDetailed Authentication Information:\r\n\tLogon Process:\t\tNtLmSsp \r\n\tAuthentication Package:\tNTLM\r\n\tTransited Services:\t-\r\n\tPackage Name (NTLM only):\tNTLM V2\r\n\tKey Length:\t\t128\r\n\r\nThis event is generated when a logon session is created. It is generated on the computer that was accessed.\r\n\r\nThe subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.\r\n\r\nThe logon type field indicates the kind of logon that occurred. The most common types are 2 (interactive) and 3 (network).\r\n\r\nThe New Logon fields indicate the account for whom the new logon was created, i.e. the account that was logged on.\r\n\r\nThe network fields indicate where a remote logon request originated. Workstation name is not always available and may be left blank in some cases.\r\n\r\nThe impersonation level field indicates the extent to which a process in the logon session can impersonate.\r\n\r\nThe authentication information fields provide detailed information about this specific logon request.\r\n\t- Logon GUID is a unique identifier that can be used to correlate this event with a KDC event.\r\n\t- Transited services indicate which intermediate services have participated in this logon request.\r\n\t- Package name indicates which sub-protocol was used among the NTLM protocols.\r\n\t- Key length indicates the length of the generated session key. This will be 0 if no session key was requested.",
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
    ]
  },
  "action": {
    "record_id": 10457874880,
    "type": "Security",
    "id": 4624,
    "name": "An account was successfully logged on",
    "outcome": "success",
    "properties": [{
          "LogonType": "3",
    }]
  },
  "host": {
    "hostname": "V-FOO",
    "name": "V-FOO"
  },
  "user": {
    "id": "S-1-0-0",
    "target": {
      "name": "SVC_DD_SP-SEARCH",
      "domain": "KEY",
      "id": "S-1-5-21-1574594750-1263408776-2012955550-69701"
    }
  }
}
```

With the following smart-description:

```json
  {
    "value": "{user.target.domain}\\{user.target.name} logged on to {host.name} (LogonType {action.properties.LogonType})",
    "relationships": [
      {
        "source": "user.target.name",
        "target": "host.name",
        "type": "logged on to"
      }
    ],
    "conditions": [
      {"field": "action.id", "value": 4624},
      {"field": "user.target.name"},
      {"field": "user.target.domain"},
      {"field": "host.name"},
      {"field": "action.properties.LogonType"},
      { "field": "event.provider", "value": "Microsoft-Windows-Security-Auditing"}
    ]
  }
```

will result into the description:

`KEY\\SVC_DD_SP-SEARCH logged on to V-FOO (LogonType 3)`
