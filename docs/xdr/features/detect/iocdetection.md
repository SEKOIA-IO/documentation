# IOC detection

IOC detection is a critical mechanism in detecting attacks that are trying to harm your system or have already breached it. The Sekoia SOC platform is powered by our Threat Detection & Research (TDR) team, which constantly enriches our IOC database with its state-of-the-art investigations and extensive expertise in Intelligence.

With IOC detection, all future and past events are verified automatically to ensure you anticipate, detect, and neutralize threats.

## How does IOC detection at Sekoia work?

Sekoia Threat Detection & Research (TDR) team maintains the CTI database with millions of IOCs through their investigation and dedicated expertise. All this incredible work directly benefits Sekoia XDR clients.

You can consult the number of IOCs that are automatically verified in the Rules catalog page. The number of IOCs is calculated according to the CTI detection rules enabled.

![verified iocs](/assets/operation_center/rules_catalog/verified_iocs.gif){: style="max-width:100%"}

Each new event ingested by Sekoia XDR is scanned against our CTI database. If an Indicator is detected, our Sekoia Intelligence Feed rule will immediately alert you.

### Sekoia Retrohunt engine

Moreover, each time a new indicator is added to our CTI database, Sekoia XDR will perform retrohunting on all available events that were ingested in the past. It means that Sekoia XDR doesn't miss any past or ongoing attacks within your system.

#### How do you recognize a retrohunt alert?

On the Alerts page, look for the Detection type of the alert. `CTI Retrohunt` alerts are triggered retroactively when a new indicator appears in our CTI database.

![detection type](/assets/operation_center/alerts/detection_type.png){: style="max-width:100%"}

#### Would your SOC team like to scan a specific list of IOCs to perform retrohunt?

That’s possible via the IOC collections. You can import a specific list of IOCs to perform retrohunting.
Please see the dedicated documentation on [IOC Collections](../ioccollections).

## Technical dive into IOC detection

We will explain how to enable and detail some technical concepts around IOC detection.

### Enable IOC detection

Our recommendation is to enable the Sekoia Intelligence Feed rule. You will automatically benefit from the protection of our CTI database and its IOCs.
Another option is to create your own custom CTI rule and choose a feed source. The feed source can be an IOC Collections provided by your SOC team.

If no CTI rule is enabled, a warning message will be displayed on the Rules catalog page.

![retrohunt disabled](/assets/operation_center/rules_catalog/retrohunt_disabled.gif){: style="max-width:100%"}

### How far in the past is retrohunting performed?

Our IOC detection will perform a retrohunt based on the valid period of the indicator (`valid from` and `valid until`).

By default, we always add 5 additional days of retrohunt to the `valid from` value. If the `valid from` of an indicator is empty, it means that retrohunt will start 5 days before the current date.

### Is retrohunt performed immediately after I import an indicator?

Sekoia XDR will perform retrohunting as soon as possible, depending on resource availability. We select the appropriate moment to perform this operation without altering user experience.
Rest assured, our retrohunt engine is quite performant, but we can't provide the exact delay.

### Which event fields are verified when performing IOC detection?

The tables below list the ECS event fields that are verified by IOC detection and if they are supported by Sekoia Intelligence Feed rule and/or by IOC Collections.

#### User fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| user.id | yes | no |
| user.name | yes | yes |
| user.domain | yes | yes |
| user.email | yes | yes |
| user.changes.email | yes | yes |
| user.effective.email | yes | yes |
| user.target.email | yes | yes |
| related.user | yes | yes |

#### Domain fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| dns.question.name | yes | yes |
| dns.question.type | yes | no |
| dns.question.registered_domain | yes | yes |
| dns.size_in_char | yes | no |
| client.domain | yes | yes |
| client.registered_domain | yes | yes |
| destination.domain | yes | yes |
| destination.registered_domain | yes | yes |
| source.domain | yes | yes |
| source.registered_domain | yes | yes |
| server.domain | yes | yes |
| server.registered_domain | yes | yes |
| related.hosts | yes | yes |

#### Email fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| client.user.email | yes | yes |
| destination.user.email | yes | yes |
| file.x509.alternative_names | yes | yes |
| host.user.email | yes | yes |
| server.user.email | yes | yes |
| source.user.email | yes | yes |
| email.from.address | yes | yes |
| email.sender.address | yes | yes |
| email.to.address | yes | yes |
| email.cc.address | yes | yes |
| email.bcc.address | yes | yes |

#### File fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| file.size | yes | no |
| file.name | yes | no |
| file.mime_type | yes | no |
| file.created | yes | no |
| file.ctime | yes | no |
| file.mtime | yes | no |
| file.path | yes | no |

#### Hash fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| dll.hash.md5 | yes | yes |
| dll.hash.sha1 | yes | yes |
| dll.hash.sha256 | yes | yes |
| dll.hash.sha512 | yes | yes |
| file.hash.md5 | yes | yes |
| file.hash.sha1 | yes | yes |
| file.hash.sha256 | yes | yes |
| file.hash.sha512 | yes | yes |
| file.hash.ssdeep | yes | yes |
| email.attachments.file.hash.md5 | yes | yes |
| email.attachments.file.hash.sha1 | yes | yes |
| email.attachments.file.hash.sha256 | yes | yes |
| email.attachments.file.hash.sha512 | yes | yes |
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
| related.hash.md5 | yes | yes |
| related.hash.sha1 | yes | yes |
| related.hash.sha256 | yes | yes |
| related.hash.sha512 | yes | yes |

#### IP fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| client.ip | yes | yes |
| destination.ip | yes | yes |
| host.ip | yes | yes |
| server.ip | yes | yes |
| source.ip | yes | yes |

#### Network fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| source.port | yes | no |
| destination.port | yes | no |
| source.bytes | yes | no |
| destination.bytes | yes | no |
| source.packets | yes | no |
| destination.packets | yes | no |
| network.transport | yes | no |
| http.request.method | yes | no |
| http.version | yes | no |
| http.request.body.bytes | yes | no |
| user_agent.original | yes | no |
| http.request.referrer | yes | no |
| http.response.status_code | yes | no |
| http.response.bytes | yes | no |
| network.protocol | yes | no |
| as.number | yes | no |
| as.organization.name | yes | no |

#### Process fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| process.pid | yes | no |
| process.start | yes | no |
| process.command_line | yes | no |
| process.working_directory | yes | no |
| process.executable | yes | no |
| process.name | yes | no |
| process.parent.pid | yes | no |
| process.parent.start | yes | no |
| process.parent.command_line | yes | no |
| process.parent.working_directory | yes | no |
| process.parent.executable | yes | no |
| process.parent.name | yes | no |

#### Registry fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| registry.key | yes | no |
| registry.value | yes | no |

#### URL fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| url.domain | yes | yes |
| url.full | yes | yes |
| url.original | yes | yes |
| url.path | yes | yes |
| url.registered_domain | yes | yes |

#### x509 Certificate fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| x509.serial_number | yes | no |
| x509.signature_algorithm | yes | no |
| x509.issuer.common_name | yes | no |
| x509.issuer.distinguished_name | yes | no |
| x509.not_before | yes | no |
| x509.not_after | yes | no |
| x509.subject.distinguished_name | yes | no |
| x509.subject.common_name | yes | no |
| x509.public_key_algorithm | yes | no |
| x509.public_key_exponent | yes | no |
| tls.client.x509 | yes | no |
| tls.server.x509 | yes | no |

#### Custom fields

| Event field | Verified by Sekoia Intelligence | Verified by IOC Collections |
| --- | --- | --- |
| action.name | yes | no |
| action.type | yes | no |
| action.outcome | yes | no |
| action.outcome_reason | yes | no |
| action.properties.targetedUser | yes | no |
| log.hostname | yes | no |
| application.category | yes | no |
| x509.subject.common_name | yes | no |
| x509.public_key_algorithm | yes | no |
| x509.public_key_exponent | yes | no |
| tls.client.x509 | yes | no |
| tls.server.x509 | yes | no |