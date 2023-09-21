# Best Pratices

Raw events may represent information in different ways. For each datasource, the parser will extract important information and generate a normalized JSON document.

This document describes some principles can help define how to generate the JSON document.


## Authentications

In order to simplify the recognition and semantic interpretation of authentications, it is necessary to respect some standardization.

An authentication is fully recognized as valid when all of these three fields are completed:
- event.category : with the value `authentication`
- event.type : with the value `start`
- action.outcome : with the value `success` if the authentication successed or `failure` else

Other fields are necessary in order to be able to fully describe the authentication. These fields are described in the table below

| Field                       | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| event.action                | Logon action type                                                    |
| event.reason                | Reason type                                                          |
| sekoiaio.client.name        | Hostname from which authentication is requested                      |
| sekoiaio.client.domain      | Domain of the host from which authentication is requested            |
| client.ip                   | IP of the host from which authentication is requested                |
| client.os.type              | OS type of the host from which authentication is requested           |
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


### A user authenticate on a Windows Host
Sources:
- [https://learn.microsoft.com/fr-fr/windows/security/threat-protection/auditing/event-4624)](https://learn.microsoft.com/fr-fr/windows/security/threat-protection/auditing/event-4624)
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



This event, from a Windows host, describes a successfully authentication:

```

```

For this event, the parser will follow these principles:

- Set **event**.category to the category `authentication`
- Set **event**.category to `start`
- Set **action**.outcome to `success`
- Set **user*.name with the name of the principal
