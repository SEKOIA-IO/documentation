---
title: "Step 1: Explore the threat intelligence database"
description: "Search the Sekoia Intelligence knowledge base to find threat actors, malware, indicators, and other CTI objects."
keywords: [intelligence, cti, search, threat actor, malware, indicator, observable, stix, tlp, database]
audience: analyst
module: intelligence
type: task
---

# Step 1: Explore the threat intelligence database

The Sekoia Intelligence database contains hundreds of thousands of threat objects: threat actors, malware families, attack campaigns, reports, indicators of compromise, and observables. This step shows you how to search and navigate this knowledge base effectively.

## Before you begin

- You have an active Sekoia Intelligence subscription.
- Familiarize yourself with the key terms: see [Glossary](/getting_started/glossary) for definitions of indicator, observable, IOC, STIX, and TLP.

## Open the intelligence database

In the navigation menu, select **Intelligence**.

The Intelligence page contains a main search bar and a results table. You can search from this page or from the search bar embedded in the navigation menu, which is accessible from any page in the platform.

## Search for a threat object

To search the database:

1. Enter a search term in the main search bar (for example, a threat actor name, a malware family, a domain, or an IP address).
2. Press **Enter**.

The results page shows three tabs:

| Tab | What it contains |
|---|---|
| **Objects** | STIX objects: threat actors, malware, campaigns, reports, indicators, attack patterns |
| **Observables** | Technical artifacts: IP addresses, domains, URLs, file hashes, email addresses |
| **Unknown observables** | Values you searched for that are not in the database |

!!! tip "Always check all tabs"
    A search for a domain name might return both an indicator object (under Objects) and the raw observable value (under Observables). Check both tabs to get the full picture.

??? example "Example: Search for a threat actor"
    Search for `APT28`.

    Under the **Objects** tab, you will find the Intrusion Set object for APT28 (also known as Fancy Bear). Click the object name to open its detail page, which shows:

    - A description of the group's known activities and targets
    - Associated malware families and tools
    - Related campaigns and attack patterns
    - Known indicators linked to this group
    - The MITRE ATT&CK techniques this group uses

## Read an object detail page

Click any object in the results table to open its detail page.

The detail page shows:

- The object name, type, and description
- The TLP classification (who can view and share this information)
- The confidence level assigned by Sekoia analysts
- Relationships to other objects (for example, a malware linked to a threat actor, or an indicator linked to a campaign)
- The source and last update date

> 📸 [SCREENSHOT SUGGESTION: An Intelligence object detail page for a threat actor, showing description, TLP badge, confidence level, related objects, and the relationship graph. | ALT TEXT: Threat actor detail page with description, TLP level, confidence score, and related CTI objects.]

## Understand TLP levels

TLP (Traffic Light Protocol) classifies how intelligence can be shared.

| TLP | Color in the interface | Sharing restriction |
|---|---|---|
| **White** | White badge | No restriction |
| **Green** | Green badge | Share within the security community |
| **Amber** | Amber badge | Restrict to your organization |
| **Red** | Red badge | Do not share outside direct recipients |

Most Sekoia Intelligence objects are TLP Amber or TLP White.

## Search for observables

To check whether a specific value, such as an IP address, domain, or file hash, is known in the Sekoia Intelligence database:

1. Enter the value directly in the search bar (for example, `185.213.83.102` or `a5f3c2d1...`).
2. Check the **Observables** tab in the results.

If the observable is known and currently valid (within its validity period), it displays a blue tag. If the validity period has passed, it displays an orange tag.

!!! note "Observables vs indicators"
    An observable is a raw technical artifact. An indicator is an observable that has been contextualized, linked to a threat, and given a validity period. A valid indicator in Sekoia Intelligence can trigger alerts in Sekoia Defend when it appears in your event stream.

## Filter results

To refine your search, open the filter panel on the right side of the results table. You can filter by:

- Object type (report, intrusion set, malware, indicator, etc.)
- TLP level
- Source
- Confidence level
- Last update date

## Related links

- [Step 2: Read and act on threat reports](/getting_started/intelligence_step2_read_threat_reports) — Find and interpret FLINT reports and set up feeds.
- [Glossary](/getting_started/glossary) — Definitions of key CTI terms.
