# Objects

STIX Domain Objects (SDOs) are the core entities of the Intelligence module. They represent structured, contextualized knowledge about cyber threats — who is behind them, what tools they use, how they operate, and what they target.

Every SDO is:

* **Contextualized** — always associated with a confidence score, a source reference, and a validity scope
* **Exportable** — available through the CTI feed via API, TAXII, or MISP
* **Interconnected** — linked to other objects through typed relationships (SROs)

### Supported Object Types <a href="#supported-object-types" id="supported-object-types"></a>

| Object type          | Description                                                           |
| -------------------- | --------------------------------------------------------------------- |
| **Threat Actor**     | A person, group, or organization conducting malicious activity        |
| **Intrusion Set**    | A clustered set of TTPs and resources tied to a specific threat actor |
| **Campaign**         | A time-bounded series of attacks sharing a common objective           |
| **Malware**          | Malicious code designed to compromise, disrupt, or exfiltrate data    |
| **Tool**             | Legitimate or dual-use software leveraged during an attack            |
| **Attack Pattern**   | A technique used by threat actors, mapped to MITRE ATT\&CK            |
| **Vulnerability**    | A weakness in a system that can be exploited                          |
| **Course of Action** | A recommended measure to prevent or respond to a threat               |
| **Identity**         | A source, organization, or entity referenced in the knowledge graph   |
| **Indicator**        | An IoC tied to a threat, with a confidence score and validity period  |
| **Report**           | A finished intelligence document grouping related STIX objects        |
| **Infrastructure**   | Systems or resources used by threat actors to conduct operations      |

### Confidence <a href="#confidence" id="confidence"></a>

Each object carries an optional confidence score expressing how certain Sekoia is about the information. Confidence is rated on the **Admiralty Credibility scale** (1–6):

| Score | Meaning                    |
| ----- | -------------------------- |
| 1     | Confirmed by other sources |
| 2     | Probably true              |
| 3     | Possibly true              |
| 4     | Doubtful                   |
| 5     | Improbable                 |
| 6     | Truth cannot be judged     |

### TLP <a href="#tlp" id="tlp"></a>

Objects are classified using the **Traffic Light Protocol (TLP)** to indicate how they can be shared:

| Label         | Meaning                                           |
| ------------- | ------------------------------------------------- |
| **TLP:CLEAR** | No restriction — publicly shareable               |
| **TLP:GREEN** | Community sharing — no public disclosure          |
| **TLP:AMBER** | Limited sharing — within organization and clients |
| **TLP:RED**   | Strict — named recipients only                    |

###
