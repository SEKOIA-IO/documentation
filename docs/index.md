---
title: Sekoia documentation
---

# Welcome to Sekoia's documentation


## The Sekoia Autonomous Defensive Intelligence Platform

Sekoia brings threat detection, investigation and response into one open, cloud-native platform. It connects Sekoia's own cyber threat intelligence (CTI), your security telemetry and asset intelligence, so every alert arrives with the context needed to act on it.

AI agents take on repetitive investigation work: they gather evidence, reach a verdict and show their reasoning, and analysts review and approve before any response. Teams spend less time sorting noise and more time on threats that need expert judgment, cutting mean time to detect (MTTD) and mean time to respond (MTTR).

![Sekoia Autonomous Defensive Intelligence Platform](/assets/sekoia_system.png){: style="max-width:100%"}

## Platform modules

The platform is modular: start with the capabilities you need and add more over time. Every module shares one data schema and one workflow, so detection, intelligence and investigation stay connected.

### Core platform modules

#### [Sekoia Defend](/xdr/index.md)

Sekoia Defend is the platform's detection and response engine and a practical alternative to a traditional Security Information and Event Management (SIEM) system. It collects, normalizes, and analyzes security logs from across the environment.

Defend also includes native Security Orchestration, Automation and Response (SOAR) capabilities. Teams can use playbooks to automate remediation steps, coordinate response actions, and reduce manual work during an investigation.

#### [Sekoia Intelligence](/cti/index.md)

Sekoia Intelligence is a cyber threat intelligence platform that gives context on attacker infrastructure, tools and behavior, researched by Sekoia's own threat analysts.

Use it as a standalone CTI source, or connect it to Sekoia Defend to correlate threat intelligence with your security events automatically.

### Expansion modules

#### [Sekoia Reveal: Asset Intelligence](/xdr/features/modules/reveal_index.md)

Sekoia Reveal adds asset intelligence to Sekoia Defend through continuous asset discovery and inventory. It maps alerts and suspicious activity to the systems, users and cloud resources involved, so analysts see what is at stake straight away.

Reveal also finds shadow IT and short-lived cloud assets that standard inventories miss, and adds exposure context, such as vulnerabilities and hygiene, so teams fix what matters first.

#### [Sekoia Elevate:AI Agents](/xdr/features/modules/elevate_overview.md)

Sekoia Elevate adds AI agents that investigate alerts end to end. They connect related incidents across data sources, enrich alerts with Sekoia CTI, and return a verdict with a confidence score and the reasoning behind it.

Analysts can review every step, adjust how the agents investigate, and approve any response. They get the full context earlier, and spend their time on decisions rather than data gathering.

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js" data-verify-origin=""></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(51.95% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://app.storylane.io/demo/nyxpygn2vyiw?embed=inline" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>

## Open, cloud-native security operations architecture

Sekoia builds its security operations platform around open integrations, portable detection logic, and cloud-native scalability. Security teams can connect the data sources they already use, apply detection rules across environments, and scale ingestion without maintaining traditional security infrastructure.

### Integration-first architecture

Sekoia provides 350+ pre-built connectors and an API-first architecture for collecting security data from endpoint, network, cloud, email and identity sources. Bring your existing telemetry into one platform without replacing the tools you already use.

### OCSF and Sigma support

Sekoia supports the Open Cybersecurity Schema Framework (OCSF) to normalize security data, and Sigma for portable detection rules. Open standards make it easier to move data between tools, reuse detection content and avoid proprietary lock-in.

### Cloud-native scalability

Sekoia runs on a multi-tenant, cloud-native architecture built to process high volumes of security telemetry. Teams can grow data ingestion without deploying or maintaining the infrastructure a traditional SIEM needs.

Prefer to run it yourself? Sekoia is also available as SaaS in your region, in a private cloud, or Self-Hosted.

!!! info "Licensing architecture"

Defend and Intelligence are independent products: use either on its own, or both together. Reveal and Elevate extend Defend and need an active Sekoia Defend licence.

## Read more

Explore the technical specifications and configuration guides for each component of the Sekoia ecosystem.

- [Sekoia Defend Overview](/xdr/index.md)
- [Sekoia Intelligence Overview](/cti/index.md)
- [Reveal: Asset Intelligence Overview](/xdr/features/modules/reveal_index.md)
- [Integration Library: A comprehensive catalog of supported log sources, intake formats, and transport protocols (Syslog, HTTPS, Cloud-to-Cloud)](/integration/index.md)
- [Sekoia API Reference](/developer/quickstart.md)
