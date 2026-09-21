# Data model

The Sekoia Intelligence platform models all Cyber Threat Intelligence (CTI) using STIX 2.1 (Structured Threat Information eXpression), the OASIS standard for describing and exchanging threat intelligence. Sekoia is an active member of the OASIS CTI Technical Committee.

## Objects

Objects represent the structural building blocks of Sekoia's intelligence knowledge. Each Object type answers a specific question an analyst needs to ask when investigating a threat: who is behind an attack, how did they operate, what did they use, where did it happen, etc.

The following diagrams show the icons for the supported Object types.

![Object types](/assets/intelligence_center/data-model-objects.png){: style="max-width:100%"}

### Object types

| Type | Definition |
| --- | --- |
| **Attack Pattern** | A description of a specific technique or behavior an adversary uses to achieve a tactical goal during an attack (for example, exploiting a public-facing application). Attack Patterns in Sekoia are aligned with recognized frameworks such as MITRE ATT&CK and the Cyber Kill Chain, so they can be used directly to drive behavior-based detection. |
| **Campaign** | A set of malicious activities or coordinated attacks conducted over a defined period, usually impacting specific industries, regions, or assets. A Campaign ties together the malware, infrastructure, and TTPs used in that particular wave of attacks, distinguishing it from the intrusion set's activity as a whole. |
| **Course of Action** | A recommended measure that could be taken in regard to a threat: a remediation, mitigation, or defensive action (for example, patching a vulnerability). |
| **Identity** | An organization, group, or class of actors, including sectors of activity (for example, the finance sector), victims of an attack, internal or external sources that produce intelligence (Sekoia itself is represented as an Identity). |
| **Indicator** | A pattern that indicates suspicious or malicious activity, built on top of one or more Observables. Unlike a raw Observable, an Indicator is always contextualized: it carries a validity period, a confidence score, and a link to the threat it relates to (malware, campaign, intrusion set, *etc.*). Indicators are the objects exported through Sekoia's CTI feeds to trigger detection. |
| **Infrastructure** | The systems, software services, and virtual or physical resources used to support an operation, for example, Command-and-Control (C2) servers, proxies, or hosting used by an adversary. |
| **Intrusion Set** | A structured set of adversarial behaviors, tools, and resources believed to be orchestrated by a single organization, pursuing one or multiple goals over time. An Intrusion Set is broader than a single Campaign, representing the persistent activity of an attacker group. Intrusion Set entries within Sekoia intelligence are attributed in a vendor-agnostic way and list known aliases used across the industry. |
| **Report** | A collection of threat intelligence covering a specific topic, for example, the profile of a threat actor, an intrusion, a malware family, or an attack technique. Beyond its narrative text, a Report contains structured references to all the STIX Objects it discusses. |
| **Location** | A geographic area (a country, region, or part of the world) associated with a threat's origin or with the victims it targets. Locations are used to contextualize Threat Actors, Campaigns, and other objects based on geographic targeting or provenance. |
| **Threat Actor** | A specific individual, group, or organization, including nation-state sponsors, believed to be acting with malicious intent, capability, and the specific intent to execute cyberattacks. |
| **Vulnerability** | A flaw, bug, or misconfiguration in software or hardware that can be directly exploited by an adversary to compromise a system or network, for example, a CVE. Vulnerabilities connect to the threats that exploit them. |
| **Malware** | A malicious code designed to compromise the confidentiality, integrity, or availability of a system: ransomware, spyware, backdoors, rootkits, *etc.* A malware is contextualized with its Kill Chain and MITRE ATT&CK mapping, related intrusion Sets, Campaigns, and exportable Indicators. |
| **Tool** | A legitimate software (utility or dual-use program not inherently malicious) that adversaries repurpose to carry out attacks, such as remote administration tools used for lateral movement. A tool's presence isn't malicious by itself, but its use in a given context can be. |

## Observables

Observables are the raw technical artifacts collected from investigations, sandboxes, honeypots, and open sources. An observable is not inherently malicious and only becomes threat-relevant once it's converted in an Indicator or enriched with tags in the platform.

The following diagram shows the icons for the supported Observable types.

![Observable types](/assets/intelligence_center/data-model-observables.png){: style="max-width:100%"}

### Observable types

| Type | Definition |
| --- | --- |
| **Address** | A generic technical identifier or physical/geographic location descriptor, used broadly before being classified into a more specific type such as an IPv4, IPv6, or MAC address. |
| **Email Address** | A single email address, used to track sender addresses in phishing campaigns or target addresses in spear-phishing. |
| **Ipv4 address** | One or more IPv4 addresses, expressed using CIDR notation. Tracked to detect scanners, command-and-control servers, or exfiltration nodes. |
| **Ipv6 address** | One or more IPv6 addresses, expressed using CIDR notation. Used to track modern internet infrastructure involved in command-and-control or scanning activity. |
| **Phone number** | A single phone number, often tracked in vishing or smishing campaigns, or as part of threat actor registration details. |
| **AS (Autonomous System)** | A large routing block on the internet, managed by a single administrative entity. AS observables are used to analyze the networks that host malicious infrastructure. |
| **File** | The properties of a file, containing at least a hash or a name. Tracked using attributes like file paths, sizes, and cryptographic hashes (MD5, SHA-256) to identify known malicious payloads. |
| **Mac address** | A single Media Access Control (MAC) address (a unique 48-bit hardware identifier) assigned to a network interface, useful for internal host tracking during an investigation. |
| **Text** | A fragment of text, such as a comment or note, used to capture raw message content, configuration strings, or unstructured information collected from a source. |
| **Windows registry key** | A database entry used by the Windows operating system. Tracked to detect malware persistence mechanisms, privilege escalation, or unauthorized configuration changes. |
| **Directory** | A file-system path container. Tracked to identify where malware is dropped, staged, or executed on a compromised host. |
| **Filename** | The name string assigned to a file, used on its own to spot known malicious payloads or suspicious naming that mimics legitimate system files. |
| **Mutex** | A mutual exclusion object used by software to prevent multiple instances of a program from running at once. Malware often uses a unique, identifiable mutex name for this purpose. |
| **URL (uniform resource locator)** | A complete web address, used to identify hosted malware payloads, phishing forms, or command-and-control endpoints. |
| **x509 Certificate** | A public-key digital certificate, as defined by the ITU X.509 standard. Analyzed to uncover malicious TLS infrastructure or signed malware code. |
| **Domain name** | A human-readable network location string, mapped to one or more IP addresses. Frequently monitored to track malicious infrastructure or phishing sites. |
| **Organization** | The name of a company, association, or other entity, tracked as an observable identity. |
| **User account** | An instance of a user account on any system. Monitored to detect credential stuffing, lateral movement, or unauthorized administrative access. |
| **Crypto wallet** | TO DO (currently adding the “Crypto wallet” observable type in the platform) |

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
