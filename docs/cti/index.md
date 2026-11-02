# Sekoia Intelligence (CTI) for security operations

Sekoia Intelligence provides contextualized Cyber Threat Intelligence (CTI) for detection, investigation, and threat hunting. Digital Risk Protection (DRP) complements CTI by monitoring organization-specific identifiers for external exposures across clear, deep, and dark web sources.

## Availability

Sekoia Intelligence is available in the Sekoia SOC platform with a [Sekoia Defend](/xdr/index.md) license, or as a standalone [Cyber Threat Intelligence (CTI)](/cti/index.md) product delivered through API integration.

Sekoia Intelligence gives security teams current, contextualized threat intelligence for detection, investigation, and threat hunting. Each intelligence record includes explicit validity timestamps and is updated as new evidence emerges. Analysts can distinguish active threat activity from expired indicators and focus on intelligence that applies to their environment.

The Intelligence Center combines analyst research, threat publications, and a searchable CTI knowledge base. Teams can monitor developing threats, investigate attacker infrastructure, and follow campaigns across sectors and geographies.

Sekoia Intelligence draws on more than 500 sources to track over 200 threat actor groups and their infrastructure worldwide. Sekoia analysts process and assess this material, adding context for strategic planning, detection engineering, and incident response.

## Digital Risk Protection

Digital Risk Protection helps organizations monitor external exposures that match identifiers configured in Flare. These identifiers can represent domains, names, keywords, IP addresses, and other values related to the organization.

The workflow connects Flare and Sekoia as follows:

1. Configure identifiers and policies in Flare.
2. Collect matching Flare events through the [Flare Events intake](/integration/categories/threat_intelligence/flare_events.md).
3. Normalize the events in Sekoia for search, detection, and investigation.
4. Activate detection rules that match your monitoring requirements.
5. Investigate the resulting Sekoia alerts and pivot to Flare with the `event.url` field.

DRP focuses on organization-specific exposure monitoring. CTI provides broader context about threat actors, malware, campaigns, infrastructure, and indicators. You can use both capabilities together during detection and investigation.

To configure the workflow, see [Get started with Flare in Sekoia Digital Risk](/getting_started/quick_start_flare.md). For the normalized fields and event coverage, see [Flare events in Sekoia Digital Risk](/cti/features/flare_events_overview.md).

## Intelligence Center features

### Access and investigate threat intelligence

Use the Intelligence Center to research threat actors, malware, infrastructure, campaigns, and related activity. The database combines external sources with research produced by Sekoia analysts, giving strategic and operational teams a shared intelligence resource.

Search the intelligence database:

Find current intelligence enriched with analyst research and contextual analysis. See [Intelligence database](/cti/features/consume/intelligence.md).

Set up custom feeds:

Follow topics relevant to your organization and receive updates when reports change. See [Feeds](/cti/features/consume/feeds.md).

Explore relationships:

Use [Graph Explorations](/cti/features/consume/graph_explorations.md) to investigate connections between threat actors, infrastructure, malware, and cases.

### Tailor intelligence to your priorities

Filter intelligence by sector, activity, source, or geography. Create custom feeds around the threats and regions most relevant to your organization.

Filter the content you see in the database by setting up [feeds](/cti/features/consume/feeds.md).

### Monitor and report on threat activity

Use dashboards and widgets to track threat activity, research output, and changes in your intelligence database. Teams can create views around the key performance indicators (KPIs) that matter to their security operations.

Create and edit your [dashboards](/cti/features/monitor/dashboard.md) to monitor sectors, research output, or the evolution of your threat database.

## Related articles

[Quick start: Intelligence](/getting_started/quick_start_intelligence.md): Explore the CTI knowledge base, investigate reports, disseminate intelligence, and configure Digital Risk Protection monitoring.

[Flare Events](/integration/categories/threat_intelligence/flare_events.md): Reference for the Flare integration, supported events, collection model, normalized fields, and detection coverage.

[Flare events in Sekoia Digital Risk](/cti/features/flare_events_overview.md): Overview of how Flare events move through collection, normalization, detection, and investigation.