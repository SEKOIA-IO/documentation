# Observables

STIX Cyber Observables (SCOs) are technical artifacts that have been observed across the Sekoia.io ecosystem. They are the raw material of threat intelligence: factual, source-agnostic, and not inherently malicious.

Observables are automatically collected from multiple sources: open-source intelligence, partner feeds, subscriptions, and Sekoia internal analysis (including C2 trackers and malware sandboxes).

> For a detailed explanation of the difference between an observable and an indicator, [see Indicators vs. Observables →.](indicators-vs.-observables.md)

### Supported types <a href="#supported-types" id="supported-types"></a>

| Type                     | Description                                                                   |
| ------------------------ | ----------------------------------------------------------------------------- |
| **IPv4 / IPv6 Address**  | Public or private IP address observed in threat activity or infrastructure    |
| **Domain Name**          | A registered domain collected from threat feeds or Sekoia analysis            |
| **URL**                  | A full web address pointing to a potentially malicious resource               |
| **File**                 | A file artifact identified by name, path, hash (MD5, SHA-1, SHA-256), or size |
| **Email Address**        | An address observed in phishing campaigns or malicious communication          |
| **Autonomous System**    | A network block identified by ASN, linked to hosting infrastructure           |
| **Network Traffic**      | A communication flow between two hosts or services                            |
| **User Account**         | A system or web account observed in an intrusion or credential leak           |
| **Windows Registry Key** | A registry entry created or modified by malware                               |
| **Process**              | A running process observed during malicious execution                         |
| **x509 Certificate**     | A TLS certificate used by malicious infrastructure                            |
| **MAC Address**          | A hardware address observed in network traffic                                |
| **Mutex**                | A named mutex created by malware at runtime                                   |

***

### Tags <a href="#tags" id="tags"></a>

Tags are the primary mechanism for enriching observables with context. They do not assert maliciousness — they describe what is known about an artifact at a given point in time.

Each tag has a validity period (`valid_from` / `valid_until`). Tags are updated continuously: an IP address might be tagged `scanner:*` for a period, then have that tag expire once scanning activity is no longer observed.

Tags serve two purposes across the Sekoia.io platform:

* **Context enrichment** in the XDR: analysts get immediate context on logs and events involving a tagged observable
* **Detection rules**: tag-based rules can be created to flag suspicious activity or reduce false positives

**Tag examples:**

| Tag                | Meaning                                                 |
| ------------------ | ------------------------------------------------------- |
| `tor`              | Tor exit node                                           |
| `scanner:*`        | Host involved in mass scanning or exploitation attempts |
| `sinkhole`         | Known sinkhole address                                  |
| `nod:1month`       | Newly observed domain (past month)                      |
| `nod:4months`      | Newly observed domain (past 4 months)                   |
| `nod:12months`     | Newly observed domain (past year)                       |
| `dynamic-dns`      | Top dynamic malicious domains                           |
| `cryptomining`     | Domain related to cryptomining activity                 |
| `country:*`        | Geolocation tag                                         |
| `rfc1918`          | Private address range (RFC 1918)                        |
| `tor`              | Tor exit node                                           |
| `disposable_email` | Domain providing disposable email services              |
| `url_shortener`    | URL shortener service                                   |
| `cloudflare`       | Cloudflare IPv4 range                                   |
| `office365`        | Microsoft Office 365 IP ranges and domains              |

***

### Sources <a href="#sources" id="sources"></a>

Observables are collected and consolidated from a wide range of sources. Each observable references its origin through the `x_inthreat_sources_refs` field.

**Source examples:**

| Source                 | Type                                   |
| ---------------------- | -------------------------------------- |
| Sekoia                 | Internal analyst production            |
| Sekoia C2 Tracker      | Automated command and control tracking |
| Sekoia Malware Watcher | Automated malware monitoring           |
| URLHaus                | Open-source malicious URL feed         |
| PhishTank              | Open-source phishing feed              |
| MalwareBazaar          | Open-source malware sample feed        |
| Tria.ge                | Malware sandbox                        |

***

### Relationships between observables <a href="#relationships-between-observables" id="relationships-between-observables"></a>

Observables are not isolated data points. They can be linked to other observables through typed relationships, forming a technical graph of infrastructure and activity.

Examples:

* An IP address `belongs-to` a subnet
* A URL is `hosted-on` a domain
* A domain `resolves-to` an IP address

These relationships can be explored directly from any observable detail page, or visualized in [Graph Explorations →](../../graph_explorations.md).

***

### Use case <a href="#use-case" id="use-case"></a>

You are investigating a security incident and have collected a list of suspicious domain names from your logs. You want to know if they are already known in the Intelligence module and whether there is any threat context attached to them.

Paste the domain names into the search interface and hit enter. For each domain, the platform will tell you:

* Whether it is a **known observable**, with associated tags (e.g. `dynamic-dns`, `nod:1month`) and any linked threats
* Whether it has already been **promoted to an IoC** and is tied to a specific malware, campaign, or intrusion set
* Whether it is **unknown**, meaning it has never been observed in the Sekoia.io ecosystem

This workflow is useful both for **triage** (quickly filtering relevant observables from noise) and for **investigation** (building context around a suspicious artifact before escalating).

***

### Searching observables <a href="#searching-observables" id="searching-observables"></a>

The Intelligence module provides a search interface for querying observables at scale, including bulk search across multiple values. Results are split between known observables (with associated context and tags) and unknown ones.

For full details on search capabilities, filters, and bulk lookup, see [Find Observables →](../../intelligence/find-observables.md).

