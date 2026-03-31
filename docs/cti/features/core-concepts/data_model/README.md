# Data Model

The Intelligence module structures all Cyber Threat Intelligence data around [**STIX 2.1**](https://oasis-open.github.io/cti-documentation/stix/intro.html), the industry standard for representing, sharing, and consuming threat intelligence.

STIX 2.1 defines three types of data the platform builds on:

* [**STIX Domain Objects (SDOs)**](objects.md) — structured, contextualized representations of threats: threat actors, malware, campaigns, vulnerabilities, and more
* [**STIX Cyber Observables (SCOs)** ](observables.md)— raw technical artifacts collected from various sources: IPs, domains, file hashes, URLs, and more
* [**STIX Relationship Objects (SROs)**](relationships.md) — typed links between SDOs, forming the knowledge graph

This structure ensures that all data is **machine-readable**, **consistently formatted**, and **directly interoperable with your existing tools** — SIEM, SOAR, TIP, or any STIX-compatible platform.

Together with [**telemetry**](telemetry.md), SDOs, SCOs, and SROs form the three building blocks of the Intelligence module.

### Building Blocks

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h4><strong>Objects</strong></h4></td><td>Structured CTI entities — threat actors, malware, campaigns, vulnerabilities, and more — and the relationships that connect them. Always contextualized, always exportable.</td><td><a href="objects.md">objects.md</a></td></tr><tr><td><h4>Observables</h4></td><td>Technical artifacts collected from open sources, partner feeds, and Sekoia internal analysis — IPs, domains, file hashes, URLs, and more. Context determines whether they become Indicators of Compromise.</td><td><a href="observables.md">observables.md</a></td></tr><tr><td><h4>Relationships</h4></td><td>Typed links between threat objects — <em>uses</em>, <em>targets</em>, <em>attributed-to</em>, <em>indicates</em>, and more. Relationships are what turns isolated objects into a connected knowledge graph.</td><td></td></tr><tr><td><h4>Telemetry</h4></td><td>Occurrence signals for observables and threats across the Sekoia.io ecosystem — track sightings over time to validate IOCs, assess threat scope, and prioritize response.</td><td><a href="telemetry.md">telemetry.md</a></td></tr><tr><td><h4 id="sources">Sources</h4></td><td>Every object in the Intelligence module traces back to its origin — Sekoia analysts, open-source intelligence, partners, and subscriptions — consolidated into a single, deduplicated knowledge graph.</td><td></td></tr></tbody></table>





