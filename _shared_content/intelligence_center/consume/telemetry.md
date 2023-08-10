# Telemetry

## Telemetry of an Observable

The Observable Telemetry feature within Sekoia.io provides a visual representation of observable instances and their frequency of appearance across monitored perimeters.

The feature showcases the occurrence count of an observable, offering a valuable perspective on its presence within Sekoia.io's monitored environment. This data is presented in a daily breakdown over the past year, where each day is represented by a compact square box. The color intensity of the square box corresponds to the proportional number of observable sightings.

The Observable Telemetry feature ensures flexibility for users to tailor their view based on their profile and permissions. This adaptability is particularly designed to accommodate Managed Security Service Providers (MSSPs) and various user scenarios. A granular filtering options is available:

- **All Sekoia.io Communities**: Users can assess the telemetry of an observable across all Sekoia.io communities, offering a global comprehensive perspective of occurrences.
- **User Community and Sub-Communities (MSSPs)**: For MSSPs, the system enables filtering of observable telemetry within the user's community and all its sub-communities. This feature facilitates robust monitoring across multiple interconnected entities.
- **User Community**: customers can focus on their own user community's observable telemetry, providing insights into their specific technical landscape.

It is important to note that the Observable Telemetry feature focuses on specific observable types, including:

- Publicly Addressable IPv4 Addresses
- Publicly Addressable IPv6 Addresses
- Domain Names with Public Top-Level Domains (TLDs) like .com, .gov.uk, .fr, etc.
- File Hashes

### Usecases

#### Anteriority Check for Indicator of Compromise (IoC)

Organizations often use observables as Indicators of Compromise (IoCs) to identify potential security threats. The telemetry visualization can serve as a crucial step in assessing the viability of an observable before using it as an IoC.

The telemetry data provides a valuable resource to scrutinize the observable's historical occurrences over time. By examining its consistent patterns of appearance, security experts can discern its reliability as an IoC. Contrary to what might be assumed, if the observable is continuously observed without significant deviations, it's less likely to be a reliable IoC. The visualization tool serves as a dynamic timeline, allowing security analysts to efficiently assess the observable's credibility.

#### Alert Contextualization

When a security alert is triggered, context is crucial to understand the urgency and potential impact of the threat. Telemetry visualization of the related observables can provide this context by showing the historical patterns and associations of the observable involved in the alert.

The telemetry visualization can display the past occurrences and fluctuations in the observable's sightings. By comparing the current sighting with historical data, security analysts can determine if the current alert is part of a larger pattern or an isolated incident, aiding in appropriate response decisions.


## Telemetry of a Threat

Sekoia.io employs telemetry visualization to track the occurrence patterns of various threat instances over time. Threats, in this context, encompass distinct categories of intelligence objects such as attack-patterns, campaigns, infrastructures, intrusion-sets, malware, threat-actors, tools, and vulnerabilities.

Telemetry is presented graphically, illustrating the frequency of threat sightings on monitored perimeters. This visualization utilizes small square boxes that are color-coded based on the proportional count of sightings. These squares are organized along a timeline, representing days over the past year.

A threat's occurrence is recorded whenever an alert is generated due to the detection materials associated with the threat. These detection materials can be Indicator of Compromises (IoCs), correlation rules, or AI models directly linked to the threat object.

Sekoia.io grants users the flexibility to filter threat telemetry according to their profile and permissions. This functionality is particularly designed with Managed Security Service Providers (MSSPs) in mind, catering to diverse client scenarios. A granular filtering options is available:

- **All Sekoia.io Communities**: Users can assess threat telemetry across all Sekoia.io communities, offering a comprehensive perspective of threat occurrences.
- **User Community and Sub-Communities (MSSPs)**: For MSSPs, the system enables filtering of threat telemetry within the user's community and all its sub-communities. This feature facilitates robust threat monitoring across multiple interconnected entities.
- **User Community**: customers can focus on their own user community's threat telemetry, providing insights into their specific threat landscape.


### Usecases

#### Assessing Threat Scope: Distinguishing Global vs. Targeted Threats

The Threat Telemetry feature in Sekoia.io serves as a pivotal tool for discerning the scope of a threat under investigation. One crucial use case involves the ability to determine whether a threat is widespread across various communities or if it's specifically targeted, only appearing within your community.

- **Global Threats**: If a threat is detected across multiple communities within Sekoia.io, the Threat Telemetry visualization will reveal a consistent and widespread pattern of occurrences. The color-coded squares, representing threat sightings, will be noticeable beyond your community's data points. This indicates that the threat has a broader impact and could potentially necessitate collaborative responses in the context of an MSSP.

- **Targeted Threats**: Conversely, if the threat's occurrences are confined solely to your community's data points in the Threat Telemetry visualization, it suggests a more targeted threat. This insight can guide investigations and response efforts more effectively. It may surely also impact the severity of the incident.

By providing a clear distinction between global and targeted threat occurrences, the Threat Telemetry feature empowers security professionals to make well-informed decisions and adopt appropriate strategies for threat mitigation and incident response.

#### Adaptive Cyber Stack Configuration: Prioritize the Strengthening of you Security Posture

An important use case of the Threat Telemetry feature lies in the ability to leverage threat telemetry insights to fine-tune your cyber stack configuration, aligning defenses with evolving threat landscapes. Threat Telemetry acts as a proactive informant for optimizing your cybersecurity arsenal, catering to the ever-changing threat landscape:

- **Identifying Emerging Threat Trends**: By analyzing the Threat Telemetry data, security professionals can detect notable surges in specific threats, malware strains, or Tactics, Techniques, and Procedures (TTPs). Unusual spikes in sightings become indicators of evolving threat patterns that require attention.

- **Adaptive Configuration**: Armed with this information, security teams can consider adapting their cyber stack configurations to counter the identified threats. This may involve fine-tuning existing detection mechanisms, enhancing monitoring for specific indicators, or even investing in new security technologies.

- **Precise Resource Allocation**: Threat Telemetry helps organizations allocate resources judiciously. Instead of a blanket approach, security investments can be targeted towards addressing the most pertinent threats based on their recent escalation in sightings.

Incorporating insights from Threat Telemetry to adapt the configuration of your cyber stack support a real proactive cybersecurity strategy. It transforms the feature from a data source to a decision-enabling tool, empowering security professionals to fortify their defenses with precision, intelligence, and real-time relevance.
