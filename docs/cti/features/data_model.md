# Data model

The Sekoia Intelligence platform models all Cyber Threat Intelligence (CTI) using STIX 2.1 (Structured Threat Information eXpression), the OASIS standard for describing and exchanging threat intelligence. Sekoia is an active member of the OASIS CTI Technical Committee.

## Objects

Objects represent the structural building blocks of Sekoia's intelligence knowledge. Each Object type answers a specific question an analyst needs to ask when investigating a threat: who is behind an attack, how did they operate, what did they use, where did it happen, etc.

### Object types

| Type | Definition |
| :---: | :--- |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=attack-pattern.png" alt="Attack Pattern"><br><strong>Attack Pattern</strong></span> | A description of a specific technique or behavior an adversary uses to achieve a tactical goal during an attack (for example, exploiting a public-facing application). Attack Patterns in Sekoia are aligned with recognized frameworks such as MITRE ATT&CK and the Cyber Kill Chain, so they can be used directly to drive behavior-based detection. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=campaign.png" alt="Campaign"><br><strong>Campaign</strong></span> | A set of malicious activities or coordinated attacks conducted over a defined period, usually impacting specific industries, regions, or assets. A Campaign ties together the malware, infrastructure, and TTPs used in that particular wave of attacks, distinguishing it from the intrusion set's activity as a whole. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=courses-of-actions.png" alt="Course of Action"><br><strong>Course of Action</strong></span> | A recommended measure that could be taken in regard to a threat: a remediation, mitigation, or defensive action (for example, patching a vulnerability). |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=identity.png" alt="Identity"><br><strong>Identity</strong></span> | An organization, group, or class of actors, including sectors of activity (for example, the finance sector), victims of an attack, internal or external sources that produce intelligence (Sekoia itself is represented as an Identity). |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=indicator.png" alt="Indicator"><br><strong>Indicator</strong></span> | A pattern that indicates suspicious or malicious activity, built on top of one or more Observables. Unlike a raw Observable, an Indicator is always contextualized: it carries a validity period, a confidence score, and a link to the threat it relates to (malware, campaign, intrusion set, *etc.*). Indicators are the objects exported through Sekoia's CTI feeds to trigger detection. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=infrastructure.png" alt="Infrastructure"><br><strong>Infrastructure</strong></span> | The systems, software services, and virtual or physical resources used to support an operation, for example, Command-and-Control (C2) servers, proxies, or hosting used by an adversary. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=intrusion set.png" alt="Intrusion Set"><br><strong>Intrusion Set</strong></span> | A structured set of adversarial behaviors, tools, and resources believed to be orchestrated by a single organization, pursuing one or multiple goals over time. An Intrusion Set is broader than a single Campaign, representing the persistent activity of an attacker group. Intrusion Set entries within Sekoia intelligence are attributed in a vendor-agnostic way and list known aliases used across the industry. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=report.png" alt="Report"><br><strong>Report</strong></span> | A collection of threat intelligence covering a specific topic, for example, the profile of a threat actor, an intrusion, a malware family, or an attack technique. Beyond its narrative text, a Report contains structured references to all the STIX Objects it discusses. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=location.png" alt="Location"><br><strong>Location</strong></span> | A geographic area (a country, region, or part of the world) associated with a threat's origin or with the victims it targets. Locations are used to contextualize Threat Actors, Campaigns, and other objects based on geographic targeting or provenance. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=threat actor.png" alt="Threat Actor"><br><strong>Threat Actor</strong></span> | A specific individual, group, or organization, including nation-state sponsors, believed to be acting with malicious intent, capability, and the specific intent to execute cyberattacks. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=vulnerability.png" alt="Vulnerability"><br><strong>Vulnerability</strong></span> | A flaw, bug, or misconfiguration in software or hardware that can be directly exploited by an adversary to compromise a system or network, for example, a CVE. Vulnerabilities connect to the threats that exploit them. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=malware.png" alt="Malware"><br><strong>Malware</strong></span> | A malicious code designed to compromise the confidentiality, integrity, or availability of a system: ransomware, spyware, backdoors, rootkits, *etc.* A malware is contextualized with its Kill Chain and MITRE ATT&CK mapping, related intrusion Sets, Campaigns, and exportable Indicators. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=tool.png" alt="Tool"><br><strong>Tool</strong></span> | A legitimate software (utility or dual-use program not inherently malicious) that adversaries repurpose to carry out attacks, such as remote administration tools used for lateral movement. A tool's presence isn't malicious by itself, but its use in a given context can be. |

## Observables

Observables are the raw technical artifacts collected from investigations, sandboxes, honeypots, and open sources. An observable is not inherently malicious and only becomes threat-relevant once it's converted in an Indicator or enriched with tags in the platform.

### Observable types

| Type | Definition |
| :---: | :--- |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=address.png" alt="Address"><br><strong>Address</strong></span> | A generic technical identifier or physical/geographic location descriptor, used broadly before being classified into a more specific type such as an IPv4, IPv6, or MAC address. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=email-address.png" alt="Email Address"><br><strong>Email Address</strong></span> | A single email address, used to track sender addresses in phishing campaigns or target addresses in spear-phishing. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=ipv4.png" alt="Ipv4 address"><br><strong>Ipv4 address</strong></span> | One or more IPv4 addresses, expressed using CIDR notation. Tracked to detect scanners, command-and-control servers, or exfiltration nodes. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=ipv6.png" alt="Ipv6 address"><br><strong>Ipv6 address</strong></span> | One or more IPv6 addresses, expressed using CIDR notation. Used to track modern internet infrastructure involved in command-and-control or scanning activity. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=phone-number.png" alt="Phone number"><br><strong>Phone number</strong></span> | A single phone number, often tracked in vishing or smishing campaigns, or as part of threat actor registration details. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=autonomous system.png" alt="AS (Autonomous System)"><br><strong>AS (Autonomous System)</strong></span> | A large routing block on the internet, managed by a single administrative entity. AS observables are used to analyze the networks that host malicious infrastructure. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=file.png" alt="File"><br><strong>File</strong></span> | The properties of a file, containing at least a hash or a name. Tracked using attributes like file paths, sizes, and cryptographic hashes (MD5, SHA-256) to identify known malicious payloads. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=mac-address.png" alt="Mac address"><br><strong>Mac address</strong></span> | A single Media Access Control (MAC) address (a unique 48-bit hardware identifier) assigned to a network interface, useful for internal host tracking during an investigation. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=text.png" alt="Text"><br><strong>Text</strong></span> | A fragment of text, such as a comment or note, used to capture raw message content, configuration strings, or unstructured information collected from a source. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=windows-registry-key.png" alt="Windows registry key"><br><strong>Windows registry key</strong></span> | A database entry used by the Windows operating system. Tracked to detect malware persistence mechanisms, privilege escalation, or unauthorized configuration changes. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=directory.png" alt="Directory"><br><strong>Directory</strong></span> | A file-system path container. Tracked to identify where malware is dropped, staged, or executed on a compromised host. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=name file.png" alt="Filename"><br><strong>Filename</strong></span> | The name string assigned to a file, used on its own to spot known malicious payloads or suspicious naming that mimics legitimate system files. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=mutex.png" alt="Mutex"><br><strong>Mutex</strong></span> | A mutual exclusion object used by software to prevent multiple instances of a program from running at once. Malware often uses a unique, identifiable mutex name for this purpose. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=url.png" alt="URL (uniform resource locator)"><br><strong>URL (uniform resource locator)</strong></span> | A complete web address, used to identify hosted malware payloads, phishing forms, or command-and-control endpoints. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=x509.png" alt="x509 Certificate"><br><strong>x509 Certificate</strong></span> | A public-key digital certificate, as defined by the ITU X.509 standard. Analyzed to uncover malicious TLS infrastructure or signed malware code. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=domain-name.png" alt="Domain name"><br><strong>Domain name</strong></span> | A human-readable network location string, mapped to one or more IP addresses. Frequently monitored to track malicious infrastructure or phishing sites. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=organizations.png" alt="Organization"><br><strong>Organization</strong></span> | The name of a company, association, or other entity, tracked as an observable identity. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=user account.png" alt="User account"><br><strong>User account</strong></span> | An instance of a user account on any system. Monitored to detect credential stuffing, lateral movement, or unauthorized administrative access. |
| <span style="display: block; text-align: center;"><img src="/assets/intelligence/icons/Size=24px, Name=crypto wallet.png" alt="Crypto wallet"><br><strong>Crypto wallet</strong></span> | TO DO (currently adding the “Crypto wallet” observable type in the platform) |

<!-- TODO: Confirm whether this article should include the complete list of observable tags and the link to the observable tag documentation. -->

## Indicator versus Observable

|  | Observable | Indicator |
| --- | --- | --- |
| **What it is** | A raw technical artifact | A pattern built on Observable(s), wrapped with context |
| **Inherently malicious?** | No, for example, [google.com](http://google.com) is a valid, benign observable | Yes, always tied to a specific threat |
| **Comes with** | Optional tags for context | Confidence score, validity period, and a Kill Chain phase |
| **Exported in CTI feeds?** | No | Yes |
| **Triggers real-time alerts in Sekoia?** | Not directly, only via tag-based detection rules | Yes, including retro-hunting across historical logs, bounded by its validity period and log retention |

## External sources

One of the founding principles of the Intelligence Center is the consolidation of information coming from several sources.

Sources are represented in STIX by `Identity` objects.

Our consolidation strategy means that the `created_by_ref` field of the STIX objects is always set to the Sekoia Identity. The sources that contributed to one of our STIX Objects are available as references in the `x_inthreat_sources_refs` custom field.

As an example, here are parts of a `Spearphishing Link` object:

````json
{
  "type": "attack-pattern",
  "name": "Spearphishing Link",
  "id": "attack-pattern--6cd1a813-ccdf-4ba0-9b54-cb808f1059cc",
  "created_by_ref": "identity--357447d7-9229-4ce1-b7fa-f1b83587048e",
  "x_inthreat_sources_refs": [
    "identity--357447d7-9229-4ce1-b7fa-f1b83587048e",
    "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5"
  ]
}
````

## Confidence

STIX 2.1 adds an optional `confidence` field for an object creator to express how confident they are about the information.

When specified, this confidence level on objects should be read with the [Admiralty Credibility](https://docs.google.com/document/d/1Cqi89CU6FwEdLjGFqMnxpl3T4iSWE_gbImBq2WXEXYk/edit#heading=h.1v6elyto0uqg) scale.

| Number | Meaning | Details |
| --- | --- | --- |
| 1 | Confirmed by other sources | Confirmed by other independent sources; logical in itself; consistent with other information on the subject |
| 2 | Probably true | Not confirmed; logical in itself; consistent with other information on the subject |
| 3 | Possibly true | Not confirmed; reasonably logical in itself; agrees with some other information on the subject |
| 4 | Doubtful | Not confirmed; possible but not logical; no other information on the subject |
| 5 | Improbable | Not confirmed; not logical in itself; contradicted by other information on the subject |
| 6 | Truth cannot be judged | No basis exists for evaluating the validity of the information |

## Reliability

Next to the source, represented by the `Identity` object type, the `confidence` score may be specified to express the source's reliability. When specified, this reliability level should be read with the [Admiralty Reliability](https://docs.google.com/document/d/1Cqi89CU6FwEdLjGFqMnxpl3T4iSWE_gbImBq2WXEXYk/edit#heading=h.1v6elyto0uqg) scale.

| Letter | Meaning | Details |
| --- | --- | --- |
| A | Completely reliable | No doubt of authenticity, trustworthiness, or competency; has a history of complete reliability |
| B | Usually reliable | Minor doubt about authenticity, trustworthiness, or competency; has a history of valid information most of the time |
| C | Fairly reliable | Doubt of authenticity, trustworthiness, or competency but has provided valid information in the past |
| D | Not usually reliable | Significant doubt about authenticity, trustworthiness, or competency but has provided valid information in the past |
| E | Unreliable | Lacking in authenticity, trustworthiness, and competency; history of invalid information |
| F | Reliability cannot be judged | No basis exists for evaluating the reliability of the source |

## Related articles

- [Observables](/cti/features/consume/observables.md): Overview of observable data in Sekoia.
- [Create feeds](/cti/features/consume/create_feed.md): How to create CTI feeds.