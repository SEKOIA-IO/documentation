# The Sekoia AI SOC Platform

The Sekoia AI SOC Platform is an open, cloud-native security operations ecosystem designed to unify detection, investigation, and response. Built for performance and analyst efficiency, the platform moves beyond traditional silos by correlating high-fidelity **Cyber Threat Intelligence (CTI)** with real-time telemetry and **Asset Intelligence**.

By leveraging an "Agentic SOC" approach, Sekoia enables security teams to automate repetitive tasks and focus on complex threat hunting, significantly reducing both Mean Time to Detect (MTTR) and operational overhead.


## Platform Architecture & Modules

The platform is modular, allowing organizations to deploy specific capabilities as needed while maintaining a unified data schema and workflow.

### Core Components (Standalone)
* **Sekoia Defend:** The central detection and response engine. It provides a robust SIEM-alternative environment to collect, normalize, and analyze logs. It includes native SOAR capabilities to orchestrate remediation through automated playbooks.
* **Sekoia Intelligence:** An industry-leading CTI platform that provides actionable insights into attacker infrastructure, malware patterns, and strategic trends. It can be used as a standalone intelligence source or integrated natively into Defend for automated correlation.

### Expansion Modules (Add-ons)
* **Reveal (Asset Intelligence):** An exclusive module for Defend that provides continuous asset discovery and inventory. It contextualizes alerts by mapping them to specific organizational assets, ensuring visibility across shadow IT and ephemeral cloud resources.
* **Elevate (Agentic SOC):** A specialized AI module that deploys intelligent agents to assist analysts. Elevate autonomously connects disparate incidents, enriches alerts with active CTI, and prioritizes critical threats to streamline the decision-making process.

![SEKOIA Licence system Overview](/assets/sekoia_system.png){: style="max-width:100%"}


## Engineering Principles

* **Integration-First:** Hundreds of pre-built connectors and a powerful API-first architecture ensure seamless ingestion from any cloud, SaaS, or on-premise source.
* **OCSF & Sigma Support:** We leverage open standards for data normalization and detection logic, preventing vendor lock-in and allowing for easy rule portability.
* **Scalability:** A multi-tenant, cloud-native backend designed to handle massive ingestion volumes without the management burden of legacy infrastructure.

!!! info "Licensing Architecture"
    While **Defend** and **Intelligence** function as independent products, **Reveal** and **Elevate** are integrated modules that require an active Sekoia Defend license to operate.

## Read more
Explore the technical specifications and configuration guides for each component of the Sekoia ecosystem.

(Sekoia Defend Overview)[/xdr/index.md]
(Sekoia Intelligence Overview)[/cti/index.md]
(Reveal: Asset Intelligence Overview)[/xdr/features/modules/reveal_index.md]
(Integration Library: A comprehensive catalog of supported log sources, intake formats, and transport protocols (Syslog, HTTPS, Cloud-to-Cloud))[/integration/index.md]
(Sekoia API Reference)[/developer/quickstart.md]
