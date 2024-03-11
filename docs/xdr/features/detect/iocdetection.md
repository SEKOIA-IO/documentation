# IOC Detection

IOC detection is a critical mechanism in detecting attacks that are trying to harm your system or have already breached it. The Sekoia SOC platform is powered by our Threat Detection & Research (TDR) team, which constantly enriches our IOC database with its state-of-the-art investigations and extensive expertise in Intelligence.

With IOC detection, all future and past events are verified automatically to ensure you anticipate, detect, and neutralize threats.

## How does IOC detection at Sekoia work?

Sekoia Threat Detection & Research (TDR) team maintains the CTI database with millions of IOCs through their investigation and dedicated expertise. 
All this incredible work benefits Sekoia XDR clients, who can consult the number of IOCs available on the Rules catalog page.

![verified iocs](/assets/operation_center/rules_catalog/verified_iocs.gif){: style="max-width:100%"}

Each new event ingested by Sekoia XDR is scanned against our CTI database. If an Indicator is detected, our Sekoia Intelligence Feed rule will immediately alert you.

### Sekoia Retrohunt engine

Each time a new indicator is added to our CTI database, Sekoia XDR will also perform retrohunting on all available events that were ingested in the past. It means that Sekoia XDR doesn't miss any past or ongoing attacks within your system.

#### How do you recognize a retrohunt alert?

On the Alerts page, look for the Detection type of the alert. `CTI Retrohunt` alerts are triggered retroactively when a new indicator appears in our CTI database.

![detection type](/assets/operation_center/alerts/detection_type.png){: style="max-width:100%"}

#### Would your SOC team like to scan a specific list of IOCs to perform retrohunt?
That’s possible via the IOC collections. You can import a specific list of IOCs to perform retrohunting.
Please see the dedicated documentation on [IOC Collections](../ioccollections).

## Technical dive into IOC detection

We will detail some technical concepts around IOC detection and explain how to enable and correctly use IOC detection.

### Enable IOC detection

Our recommendation is to enable the Sekoia Intelligence Feed rule. You will automatically benefit from the protection of our CTI database and its IOCs.
Another option is to create your own custom CTI rule and choose a feed source. The feed source can be an IOC Collections provided by your SOC team.

If no CTI rule is enabled, a warning message will be displayed on the Rules catalog page.

![retrohunt disabled](/assets/operation_center/rules_catalog/retrohunt_disabled.gif){: style="max-width:100%"}

### How far in the past is retrohunting performed?

Our IOC detection will perform a retrohunt based on the valid period of the indicator (valid from and valid until).
By default, 5 additional days are always added to handle cases where the indicator has a specified valid period.

### Is retrohunt performed immediately after I import an indicator?

Sekoia XDR will perform retrohunting as soon as possible, depending on resource availability. We select the appropriate moment to perform this operation without altering user experience.

### Which event fields are verified when performing IOC detection?

The tables below list the ECS event fields that are verified by IOC detection. ECS event fields are grouped by STIX observable types.

#### Observable type: Domain Name

| ECS event field | 
| --- |
| client.domain |
| client.registered_domain |
| destination.domain |
| destination.registered_domain |
| dns.question.name |
| dns.size_in_char |
| source.domain |
| source.registered_domain |
| server.domain |
| server.registered_domain |
| tls.client.x509.alternative_names |
| url.domain |
| url.registered_domain |
| x509.alternative_names |
| x509.subject.common_name |

#### Observable type: Email Address

| ECS event field |
| --- |
| client.user.email |
| destination.user.email |
| destination.user.full_name |
| email.from.address |
| email.sender.address |
| email.to.address |
| email.cc.address |
| email.bcc.address |
| file.x509.alternative_names |
| host.user.email |
| server.user.email |
| source.user.email |
| source.user.full_name |
| tls.client.x509.alternative_names |
| user.email |
| user.effective.email |
| user.target.email |

#### Observable type: File

| ECS event field |
| --- |
| dll.hash.md5 |
| dll.hash.sha1 |
| dll.hash.sha256 |
| dll.hash.sha512 |
| email.attachments.file.hash.md5 |
| email.attachments.file.hash.sha1 |
| email.attachments.file.hash.sha256 |
| email.attachments.file.hash.sha512 |
| file.size | 
| file.name | 
| file.mime_type | 
| file.created | 
| file.ctime | 
| file.hash.md5 |
| file.hash.sha1 |
| file.hash.sha256 |
| file.hash.sha512 |
| file.hash.ssdeep |
| file.mtime | 
| file.path | 
| process.hash.md5 |
| process.hash.sha1 |
| process.hash.sha256 |
| process.hash.sha512 |
| process.hash.ssdeep |
| process.working_directory |

#### Observable type: IPv4 Address & IPv6 Address

| ECS event field |
| --- |
| client.ip |
| destination.ip |
| host.ip |
| server.ip |
| source.ip |

#### Observable type: Network Traffic

| ECS event field |
| --- |
| action.name |
| action.type |
| action.outcome |
| destination.bytes |
| destination.ip |
| destination.packets |
| destination.port |
| dns.size_in_char |
| http.request.body.bytes |
| http.request.method |
| http.request.referrer |
| http.response.bytes |
| http.response.status_code |
| http.version |
| network.protocol |
| network.transport |
| source.bytes |
| source.ip |
| source.packets |
| source.port |
| url.path |
| user_agent.original |

#### Observable type: Process

| ECS event field |
| --- |
| process.command_line |
| process.executable |
| process.pid |
| process.ppid |
| process.start |  
| process.hash.md5 |
| process.hash.sha1 |
| process.hash.sha256 |
| process.hash.sha512 |
| process.hash.ssdeep |
| process.working_directory |  
| process.name | 
| process.parent.command_line |
| process.parent.executable | 
| process.parent.hash.md5 |
| process.parent.hash.sha1 |
| process.parent.hash.sha256 |
| process.parent.hash.sha512 |
| process.parent.hash.ssdeep |
| process.parent.name |
| process.parent.pid |
| process.parent.start |
| process.parent.working_directory | 

#### Observable type: URL

| ECS event field |
| --- |
| url.full |
| url.original |

#### Observable type: User Account

| ECS event field |
| --- |
| action.name |
| action.outcome |
| action.outcome_reason |
| action.properties.targetedUser
| action.type |
| log.hostname |
| user.domain |
| user.email |
| user.full_name |
| user.id |
| user.name |

#### Observable type: Windows Registry Key

| ECS event field |
| --- |
| registry.key | 
| registry.value |

#### Observable type: X.509 Certificate

| ECS event field |
| --- |
| x509.issuer.common_name | 
| x509.issuer.distinguished_name | 
| x509.not_before | 
| x509.not_after | 
| x509.public_key_algorithm | 
| x509.public_key_exponent |
| x509.serial_number | 
| x509.signature_algorithm |
| x509.subject.distinguished_name | 
| x509.subject.common_name |