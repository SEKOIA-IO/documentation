# Telemetry

Telemetry measures how often an observable or a threat has been sighted across the Sekoia.io ecosystem. It answers a simple but critical question: is what you are looking at a widespread, recurring signal — or something rare and targeted?

The Intelligence module provides two types of telemetry, each with a distinct purpose:

* **Observable telemetry** — tracks how many times a specific technical artifact (an IP, a domain, a file hash) has appeared in parsed events across communities
* **Threat telemetry** — tracks how often a threat object (a malware, a campaign, an intrusion set) has triggered detection alerts across communities

Both types are visualized as a **heatmap**: a daily breakdown over the past year, where each square represents a day and its color intensity reflects the volume of sightings.

## Observable telemetry <a href="#observable-telemetry" id="observable-telemetry"></a>

Observable telemetry is available for four types of observables:

* Publicly addressable IPv4 addresses
* Publicly addressable IPv6 addresses
* Domain names linked to public TLDs (.com, .fr, .gov.uk, and others)
* File hashes

### How it is computed <a href="#how-it-is-computed" id="how-it-is-computed"></a>

A sighting is recorded each time the value of an observable is parsed in an event. The telemetry aggregates these sightings over time and presents them as a daily heatmap covering the past year.

### Filters <a href="#filters" id="filters"></a>

Telemetry can be scoped to match your monitoring context:

| Filter                     | Available to           | Description                                                   |
| -------------------------- | ---------------------- | ------------------------------------------------------------- |
| **All Sekoia.io**          | All users              | Global view across all communities in the Sekoia.io ecosystem |
| **My managed communities** | MSSPs and multi-tenant | Sightings within your community and all its sub-communities   |
| **Single community**       | MSSPs and multi-tenant | Sightings scoped to one selected community                    |

### How to access it <a href="#how-to-access-it" id="how-to-access-it"></a>

**From the Intelligence module:**

1. Open the Intelligence Database page
2. Search for an observable and open the Observables tab
3. Click on the observable to open its detail page
4. If the observable is a public IPv4, IPv6, domain name, or file hash, the telemetry heatmap will be available on the page

**From an alert investigation:**

1. Open an Alert details page
2. Go to the Graph Investigation tab
3. Click on a supported observable in the graph
4. In the left panel, a button showing the number of sightings will appear
5. Click it to open the full telemetry heatmap

***

## Threat telemetry <a href="#threat-telemetry" id="threat-telemetry"></a>

Threat telemetry is available for all STIX object types: attack patterns, campaigns, infrastructures, intrusion sets, malware, threat actors, tools, and vulnerabilities.

### How it is computed <a href="#how-it-is-computed" id="how-it-is-computed"></a>

A threat sighting is recorded each time an alert is triggered by detection materials linked to that threat object. Detection materials include IoCs, correlation rules, and AI models directly associated with the threat.

### Filters <a href="#filters" id="filters"></a>

The same three filters apply as for observable telemetry: **all Sekoia.io, managed communities, or a single selected community.**

### How to access it <a href="#how-to-access-it" id="how-to-access-it"></a>

1. Open the Intelligence Database page
2. Search for a threat object and click on it to open its detail page
3. The telemetry heatmap appears in the page header. Each square represents a month in this condensed view.
4. Click on any square to expand the full daily heatmap



## Use cases <a href="#use-cases" id="use-cases"></a>

### Validating an IoC before using it <a href="#validating-an-ioc-before-using-it" id="validating-an-ioc-before-using-it"></a>

Before promoting an observable to an IoC or importing external IoCs into the platform, telemetry helps assess whether the observable is a credible signal. An artifact that appears consistently across all communities without deviation is likely benign infrastructure — not a reliable indicator of compromise.

> Note: the telemetry report generated for IoC collections reflects observable telemetry (occurrence of a value), not threat telemetry (occurrence of a threat ID).

### Distinguishing global threats from targeted attacks <a href="#distinguishing-global-threats-from-targeted-attack" id="distinguishing-global-threats-from-targeted-attack"></a>

Threat telemetry reveals whether a threat is widespread or confined to your environment. If sightings appear across many communities, the threat is likely part of a broad campaign. If they appear only within your community, it points to a targeted attack — which typically warrants a different response and may increase incident severity.

### Prioritizing your security posture <a href="#prioritizing-your-security-posture" id="prioritizing-your-security-posture"></a>

Spikes in threat sightings signal emerging activity that deserves attention. By monitoring telemetry trends over time, security teams can identify which threats are escalating, adjust detection mechanisms accordingly, and allocate resources toward the most active and relevant threats rather than applying a blanket approach.

