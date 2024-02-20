# IOC detection

IOC detection is a critical mechanism in detecting attacks that are trying to harm your system or have already breached inside your system. The Sekoia SOC platform is powered by our Threat Detection & Research (TDR) team that is constantly enriching our IOC database with their state-of-the-art investigations and long expertise in Intelligence.

With IOC detection, all future and past events are verified automatically to ensure that you anticipe, detect and neutralize threats.

## How does IOC detection works in Sekoia?

Sekoia Threat Detection & Research (TDR) team maintains the CTI database with millions of IOCs through their investigation and dedicated expertise.
Sekoia XDR clients benefits of all this incredible work within the platform automatically. You can consult the number of IOCs available in the Rules catalog page.

Each new event ingested by Sekoia XDR is scanned against our CTI database. If an Indicator is detected, our Sekoia Intelligence Feed rule will immediately alert you.

### What is event more incredible? Sekoia Retrohunt engine

Each time a new indicator is added in our CTI database, Sekoia XDR performs retrohunting on all available events that were ingested in the past. It means that Sekoia XDR will not miss past or ongoing attacks in your system.

#### How do you recognize a retrohunt alert?

In Alerts page, look for the Detection type of the alert. `CTI Retrohunt` alerts are a type of alert that were triggered retroactively when a new indicator was added in our CTI database.

#### Your SOC team would like to scan a specific list of IOCs to perform retrohunt?
That’s possible via the IOC collections. You can import a specific list of IOCs to perform retrohunting. IOC collection feature is available in our Prime plan.
See the dedicated documentation for IOC collection.

## Technical dive into IOC detection

We will detail some technical concepts around IOC detection and how to enable and correctly use IOC detection.

### Enable IOC detection

Our recommandation is to enable the Sekoia Intelligence Feed rule. You will automatically benefit of the protection of our CTI database and its IOCs.
Another option is to create your own custom CTI rule and choose a feed source. The feed source can be an IOC collection provided by your SOC team.

If no CTI rule is enabled, a warning message will be displayed in the Rules catalog page.

### Indicator types supported in IOC collections

The supported indicator types are:

- IP address
- Domain name
- URL
- File hash
- Email address.

### Which event fields are verified when performing IOC detection?

The following ECS event fields will be verified during IOC detection. 
Since IOC collection supports a limited list of indicator types, some event fields are only verified with CTI rule which supports more indicator types.

The tables below indicate in which case event field will be verified.

#### Username

| Event field | Verified with IOC collection | Verified with CTI rule |
| --- | --- | --- |
| user.name | yes | yes |
| user.domain | yes | yes |
| related.user | yes | yes |

#### IP

| Event field | Verified with IOC collection | Verified with CTI rule |
| --- | --- | --- |
| client.ip | yes | yes |
| destination.ip | yes | yes |
| host.ip | yes | yes |
| server.ip | yes | yes |
| source.ip | yes | yes |
| related.ip | yes | yes |

#### Domain

| Event field | Verified with IOC collection | Verified with CTI rule |
| --- | --- | --- |
| dns.question.name | yes | yes |
| dns.question.type | no | yes |
| dns.question.registered_domain | yes | yes |
| dns.size_in_char | no | yes |
| client.domain | yes | yes |
| client.registered_domain | yes | yes |
| destination.domain | yes | yes |
| destination.registered_domain | yes | yes |
| source.domain | yes | yes |
| source.registered_domain | yes | yes |
| server.domain | yes | yes |
| server.registered_domain | yes | yes |
| url.domain | yes | yes |
| url.registered_domain | yes | yes |
| related.hosts | yes | yes |

#### Email

| Event field | Verified with IOC collection | Verified with CTI rule |
| --- | --- | --- |
| client.user.email | yes | yes |
| destiantion.user.email | yes | yes |
| file.x509.alternative_names | yes | yes |
| host.user.email | yes | yes |
| server.user.email | yes | yes |
| source.user.email | yes | yes |
| user.email | yes | yes |
| user.changes.email | yes | yes |
| user.effective.email | yes | yes |
| user.target.email | yes | yes |
| email.from | yes | yes |
| email.to | yes | yes |
| email.from.address | yes | yes |
| email.to.address | yes | yes |
| email.cc.address | yes | yes |
| email.bcc.address | yes | yes |
| retarus.sender | yes | yes |
| retarus.recipient | yes | yes |

#### File

| Event field | Verified with IOC collection | Verified with CTI rule |
| --- | --- | --- |
| file.size | no | yes |
| file.name | no | yes |
| file.mime_type | no | yes |
| file.created | no | yes |
| file.mtime | no | yes |
| file.ctime | no | yes |
| file.path | no | yes |
| process.hash.md5 | yes | yes |
| process.hash.sha1 | yes | yes |
| process.hash.sha256 | yes | yes |
| process.hash.sha512 | yes | yes |
| process.hash.ssdeep | yes | yes |
| process.parent.hash.md5 | yes | yes |
| process.parent.hash.sha1 | yes | yes |
| process.parent.hash.sha256 | yes | yes |
| process.parent.hash.sha512 | yes | yes |
| process.parent.hash.ssdeep | yes | yes |
| process.pid | no | yes |
| process.start | no | yes |
| process.working_directory | no | yes |
| process.command_line | no | yes |
| process.executable | no | yes |
| process.name | no | yes |
| process.parent.pid | no | yes |
| process.parent.start | no | yes |
| process.parent.command_line | no | yes |
| process.parent.working_directory | no | yes |
| process.parent.executable | no | yes |
| process.parent.name | no | yes |

#### Network

| Event field | Verified with IOC collection | Verified with CTI rule |
| --- | --- | --- |
| source.port | no | yes |
| destination.port | no | yes |
| source.bytes | no | yes |
| destination.bytes | no | yes |
| source.packets | no | yes |
| destination.packets | no | yes |
| network.transport | no | yes |
| http.request.method | no | yes |
| url.path | no | yes |
| http.version | no | yes |
| http.request.body.bytes | no | yes |
| user_agent.original | no | yes |
| http.request.referrer | no | yes |
| http.response.status_code | no | yes |
| http.response.bytes | no | yes |
| network.protocol | no | yes |
| as.number | no | yes |
| as.organization.name | no | yes |

!!! warning
	Note that when importing indicators in an IOC collection, if you select the kill chain ‘Command a Control’ then our retrohunt engine will look only into destination.ip.
    This in order to reduce false-positives as C2 servers tends to scan networks a lot. By doing this, we look for slave servers that responds to a C2 server.

### How far in the past is retrohunting performed?

Our IOC detection will perform retrohunt based on the valid period of the indicator (valid from and valid until).
By default, 5 additional days are always added to handle cases where the indicator has specified valid period.

### Is retrohunt performed immediately after I import an indicator?

Sekoia XDR will perform retrohunting as soon as possible depending on ressources availability. We select the appropriate moment to perform this operation without altering user experience.
Rest assured, our retrohunt engine is quite performant :) but we cannot provide the exact delay.