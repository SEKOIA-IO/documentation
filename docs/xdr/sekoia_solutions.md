# Welcome to Sekoia's documentation


## The Sekoia AI SOC Platform

The Sekoia SOC platform brings threat detection, investigation, and response into one open, cloud-native platform. It connects high-fidelity **Cyber Threat Intelligence (CTI)**, security telemetry, and **Asset Intelligence** to give analysts a clearer view of what's happening across their environment.

With its Agentic SOC approach, Sekoia uses AI to handle repetitive investigation tasks, enrich alerts, and support threat hunting. Analysts spend less time sorting through noise and more time responding to threats that need expert judgment.

The result is faster detection, more efficient investigations, and lower operational overhead. Sekoia helps security teams reduce Mean Time to Detect (MTTD) and Mean Time to Respond (MTTR) while keeping their existing tools and data sources connected.

![SEKOIA AI SOC Platform Overview](/assets/sekoia_system.png){: style="max-width:100%"}

## Security operations platform architecture and modules

Sekoia's modular security operations platform lets teams start with the capabilities they need and expand over time. Each module uses a shared data schema and workflow, helping security teams connect detection, Cyber Threat Intelligence (CTI), asset context, and AI assistance in one environment.

### Core platform modules

#### [Sekoia Defend](/xdr/index.md)

Sekoia Defend is the platform's detection and response engine and a practical alternative to a traditional Security Information and Event Management (SIEM) system. It collects, normalizes, and analyzes security logs from across the environment.

Defend also includes native Security Orchestration, Automation and Response (SOAR) capabilities. Teams can use playbooks to automate remediation steps, coordinate response actions, and reduce manual work during an investigation.

#### [Sekoia Intelligence](/cti/index.md)

Sekoia Intelligence is a Cyber Threat Intelligence platform that provides context on attacker infrastructure, malware, campaigns, and emerging threat activity. Teams can use it as a standalone CTI source or connect it to Sekoia Defend.

When integrated, Sekoia Intelligence helps correlate threat intelligence with security events and gives analysts additional context during detection and investigation.

### Expansion modules

#### [Reveal for Asset Intelligence](/xdr/features/modules/reveal_index.md)

Reveal adds Asset Intelligence to Sekoia Defend through continuous asset discovery and inventory. It maps alerts and suspicious activity to the systems, users, and cloud resources involved, giving analysts better context during an investigation.

Reveal also helps teams identify shadow IT and short-lived cloud assets that may not appear in standard inventories.

#### [Sekoia Elevate for an Agentic SOC](/xdr/features/modules/elevate_overview.md)

Sekoia Elevate adds AI assistance to the SOC. Its intelligent agents connect related incidents across data sources, enrich alerts with relevant CTI, and help prioritize threats for investigation.

Analysts receive more context earlier in the investigation and can focus their time on decisions that require human judgment.

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js" data-verify-origin=""></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(51.95% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://app.storylane.io/demo/nyxpygn2vyiw?embed=inline" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>

## Open, cloud-native security operations architecture

Sekoia builds its security operations platform around open integrations, portable detection logic, and cloud-native scalability. Security teams can connect the data sources they already use, apply detection rules across environments, and scale ingestion without maintaining traditional security infrastructure.

### Integration-first architecture

Sekoia provides hundreds of pre-built connectors and an API-first architecture for collecting security data from cloud services, SaaS applications, and on-premises systems. This gives teams a practical way to bring more telemetry into one security operations platform while keeping integration work manageable.

### OCSF and Sigma support

Sekoia supports the Open Cybersecurity Schema Framework (OCSF) for normalizing security data and Sigma for writing portable detection rules. Open standards help teams move data between tools, reduce dependence on proprietary formats, and adapt detection logic as their environment changes.

### Cloud-native scalability

Sekoia runs on a multi-tenant, cloud-native architecture designed to process high volumes of security telemetry. Teams can expand data ingestion without deploying and maintaining the infrastructure typically associated with on-premises security platforms.

!!! info "Licensing architecture"

    While **Defend** and **Intelligence** function as independent products, **Reveal** and **Elevate** are integrated modules that require an active Sekoia Defend license to operate.

## Read more

Explore the technical specifications and configuration guides for each component of the Sekoia ecosystem.

- [Sekoia Defend Overview](/xdr/index.md)
- [Sekoia Intelligence Overview](/cti/index.md)
- [Reveal: Asset Intelligence Overview](/xdr/features/modules/reveal_index.md)
- [Integration Library: A comprehensive catalog of supported log sources, intake formats, and transport protocols (Syslog, HTTPS, Cloud-to-Cloud)](/integration/index.md)
- [Sekoia API Reference](/developer/quickstart.md)
