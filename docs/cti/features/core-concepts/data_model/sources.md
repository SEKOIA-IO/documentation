# Sources

The Intelligence module consolidates data from a curated set of trusted sources, continuously monitored and updated by Sekoia. Rather than exposing raw, unfiltered feeds, the platform merges contributions from multiple origins into a single, deduplicated knowledge base, to ensure consistency and reliability across all objects.

Sources are represented in STIX as **Identity objects** and fall into four categories:

* **Sekoia analyst production** — finished intelligence produced by Sekoia's internal analyst team
* **Open-source intelligence (OSINT)** — curated public feeds and threat repositories
* **Partner and subscription feeds** — third-party intelligence providers integrated into the platform
* **Automated collection** — infrastructure tracking, malware sandboxes, and threat monitoring systems operated by Sekoia

### Source examples <a href="#source-examples" id="source-examples"></a>

| Source                     | Category             | Description                                                      |
| -------------------------- | -------------------- | ---------------------------------------------------------------- |
| **Sekoia**                 | Analyst production   | Internal threat intelligence produced by Sekoia analysts         |
| **Sekoia C2 Tracker**      | Automated collection | Continuous tracking of active command and control infrastructure |
| **Sekoia Malware Watcher** | Automated collection | Automated monitoring of malware samples and behavior             |
| **URLHaus**                | OSINT                | Community-driven feed of malicious URLs                          |
| **PhishTank**              | OSINT                | Community-driven feed of phishing URLs                           |
| **MalwareBazaar**          | OSINT                | Open repository of malware samples                               |
| **Tria.ge**                | Partner              | Malware sandbox and dynamic analysis platform                    |
| **The MITRE Corporation**  | Partner              | ATT\&CK framework and attack pattern reference                   |

### How sources are tracked on objects <a href="#how-sources-are-tracked-on-objects" id="how-sources-are-tracked-on-objects"></a>

Every object in the Intelligence module carries two source-related fields:

* `created_by_ref` — always set to the Sekoia Identity, as the consolidating entity responsible for the object
* `x_inthreat_sources_refs` — lists all Identity objects that contributed to the information

This model means you always know where the data comes from, even when multiple sources reported on the same threat.

**Example:**

```json
json{
  "type": "attack-pattern",
  "name": "Spearphishing Link",
  "created_by_ref": "identity--357447d7-9229-4ce1-b7fa-f1b83587048e",
  "x_inthreat_sources_refs": [
    "identity--357447d7-9229-4ce1-b7fa-f1b83587048e",
    "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5"
  ]
}
```

Here, the object was consolidated by Sekoia but also references a contribution from The MITRE Corporation.

### Source reliability <a href="#source-reliability" id="source-reliability"></a>

Each source can be assigned a **reliability score** using the Admiralty Reliability scale. This score reflects how trustworthy and consistent a source has proven to be over time.

| Score | Meaning                      |
| ----- | ---------------------------- |
| A     | Completely reliable          |
| B     | Usually reliable             |
| C     | Fairly reliable              |
| D     | Not usually reliable         |
| E     | Unreliable                   |
| F     | Reliability cannot be judged |

The reliability score applies to the **source itself**, not to individual objects. For object-level confidence scoring, see [Objects →](objects.md).
