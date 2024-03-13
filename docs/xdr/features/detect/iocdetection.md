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

![detection type](/assets/operation_center/alerts/detection_type.gif){: style="max-width:100%"}

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

The tables below list the ECS event fields that are verified by IOC detection.

#### Observable type: Domain Name

| STIX path | ECS event field | 
| --- | --- |
| domain-name:value | client.domain<br>client.registered_domain<br>destination.domain<br>destination.registered_domain<br>dns.question.name<br>source.domain<br>source.registered_domain<br>server.domain<br>server.registered_domain<br>tls.client.x509.alternative_names<br>url.domain<br>x509.alternative_names<br>x509.subject.common_name |

#### Observable type: Email Address

| STIX path | ECS event field |
| --- | --- |
| email-addr:value| client.user.email<br>destination.user.email<brdestination.user.full_name<br>email.from.address<br>email.sender.address<br>email.to.address<br>email.cc.address<br>email.bcc.address<br>file.x509.alternative_names<brhost.user.email><br>server.user.email<br>source.user.email<br>source.user.full_name<br>tls.client.x509.alternative_names<br>user.email<br>user.effective.email<br>user.target.email |
| email-addr:display_name | destination.user.full_name<br>source.user.full_name |

#### Observable type: File

| STIX path | ECS event field |
| --- | --- |
| file:ctime | file.created |
| file:hashes.MD5 | dll.hash.md5<br>email.attachments.file.hash.md5<br>file.hash.md5<br>process.hash.md5 |
| file.hash.SHA-1 | file.hash.sha1<br>dll.hash.sha1<br>email.attachments.file.hash.sha1<br>process.hash.sha1 |
| file.hash.SHA-256 | file.hash.sha256<br>dll.hash.sha256<br>email.attachments.file.hash.sha256<br>process.hash.sha256 |
| file.hash.SHA-512 | file.hash.sha512<br>dll.hash.sha512<br>email.attachments.file.hash.sha512<br>process.hash.sha512 |
| file:hashes.SSDEEP | file.hash.ssdeep | 
| file:mime_type | file.mime_type | 
| file:mtime | file.ctime |
| file:name | file.name |
| file:size | file.size |

#### Observable type: IPv4 Address & IPv6 Address

| STIX path | ECS event field |
| --- | --- |
| ipv4-addr:value | client.ip<br>destination.ip<br>host.ip<br>server.ip<br>source.ip |

#### Observable type: Network Traffic

| STIX path | ECS event field |
| --- | --- |
| network-traffic:action_ref.name | action.name |
| network-traffic:action_ref.verb | action.type |
| network-traffic:action_ref.outcome | action.outcome |
| network-traffic:dst_byte_count | destination.bytes |
| network-traffic:dst_ref.value | destination.ip |
| network-traffic:dst_packets | destination.packets |
| network-traffic:dst_port | destination.port |
| network-traffic:extensions.http-request-ext.message_body_length | http.request.body.bytes |
| network-traffic:extensions.http-request-ext.request_method | http.request.method |
| network-traffic:extensions.http-request-ext.x_request_referrer | http.request.referrer |
| network-traffic:extensions.x-http-response.x_response_bytes | http.response.bytes |
| network-traffic:extensions.x-http-response.x_response_status_code | http.response.status_code |
| network-traffic:extensions.http-request-ext.request_version | http.version |
| network-traffic:x_dpi_protocols[*] | network.protocol |
| network-traffic:protocols[*] | network.transport |
| network-traffic:src_byte_count | source.bytes |
| network-traffic:src_ref.value | source.ip |
| network-traffic:src_packets | source.packets |
| network-traffic:src_port | source.port |
| network-traffic:extensions.http-request-ext.request_value | url.path |
| network-traffic:extensions.http-request-ext.request_header.User-Agent | user_agent.original | 

#### Observable type: URL

| STIX path | ECS event field |
| --- | --- |
| url:value | url.full<br>url.original |

#### Observable type: Windows Registry Key

| STIX path | ECS event field |
| --- | --- |
| windows-registry-key:key | registry.key | 
| windows-registry-key:values | registry.value |

#### Observable type: X.509 Certificate

| STIX path | ECS event field |
| --- | --- |
| x509-certificate:issuer | x509.issuer.common_name<br>x509.issuer.distinguished_name | 
| x509-certificate:serial_number | x509.serial_number | 
| x509-certificate:signature_algorithm | x509.signature_algorithm |
| x509-certificate:subject | x509.subject.common_name<br>x509.subject.distinguished_name |
| x509-certificate:subject_public_key_algorithm | x509.public_key_algorithm | 
| x509-certificate:subject_public_key_exponent | x509.public_key_exponent |
| x509-certificate:validity_not_before | x509.not_before | 
| x509-certificate:validity_not_after | x509.not_after | 