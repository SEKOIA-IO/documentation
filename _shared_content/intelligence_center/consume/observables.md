# Observables

An observable is a piece of technical information that can help identify or investigate a potential threat. When an observable clearly represents malicious activity and has threat context, Sekoia can treat it as an indicator of compromise (IoC).

Use observables to investigate technical values such as IP addresses, domains, URLs, file hashes, and email addresses.

## Find an observable

Use the [Intelligence search workflow](/cti/features/consume/intelligence.md) to search for one or more observable values.

When you paste multiple values, review the **Known** and **Unknown** result views. The **Known** view contains values available in the Intelligence database. The **Unknown** view contains values that Sekoia has not identified.

Select an observable to open its details page.

## Observable types

Sekoia can store observables such as:

| Type | Examples |
|---|---|
| Network | IPv4 address, IPv6 address, autonomous system, MAC address |
| Web | Domain name, URL, email address |
| File | File, filename, file hash |
| Certificate | X.509 certificate |
| System | Directory, mutex, Windows registry key |
| Organization | Organization name |
| Text | Text value |

## Sources and enrichment

Observables can come from public sources, subscriptions, partners, and Sekoia internal analysis.

Sources and enrichment can provide context such as:

- geolocation;
- Internet service provider;
- reputation;
- scanning activity;
- cloud provider or hosting information;
- security reports.

## Tags and validity

Tags add context to an observable. Examples include tags for cloud providers, country ranges, scanning activity, URL shorteners, sinkholes, and newly observed domains.

Tags can include validity dates:

- **Valid from** indicates when the information became valid;
- **Valid until** indicates when the information expires.

Review the validity dates before using a tag as current evidence. A tag with an expired validity period remains part of the observable history but no longer represents current enrichment.

## Observable relationships

An observable can relate to other observables and intelligence objects. For example:

- an IP address can belong to a subnet;
- a URL can be hosted on a domain;
- an observable can be associated with a malware, campaign, or intrusion set;
- an observable can become an IoC when its threat context confirms malicious activity.

Use these relationships to move from a technical value to the wider threat context. For relationship workflows, see [Investigate an object](/cti/features/consume/investigate_an_object.md).

## Review observable details

An observable details page can include:

- the observable value;
- its type;
- TLP and confidence;
- sources;
- tags and validity dates;
- related objects;
- external references;
- the raw object when available.

Use the details page to validate the value, review its enrichment, and decide whether its related threat context is relevant to your investigation.

## Example workflow

You find several domains during an investigation and want to check whether Sekoia has already seen them.

1. Search for the domains in **Intelligence**.

2. Review the **Known** results.

3. Check the sources, tags, and validity dates for each known observable.

4. Open an observable to review its related malware, campaigns, or other objects.

5. Review the **Unknown** results separately. An unknown observable is not evidence that the value is benign. It means that Sekoia has not identified it in the searched data.

## Related articles

[Intelligence](/cti/features/consume/intelligence.md): How to search and filter objects and observables.

[Investigate an object](/cti/features/consume/investigate_an_object.md): How to review an object’s context, relationships, graph, and reports.

[Data model](/cti/features/data_model.md): Reference for objects, observables, relationships, sources, and confidence.

[Graph Explorations](/cti/features/consume/graph_explorations.md): How to explore relationships in a visual graph.
