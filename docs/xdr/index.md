# Sekoia Defend

!!! note "Licensing and ecosystem"

    Sekoia Defend is the core detection and response module of the [Sekoia SOC platform](sekoia_solutions.md). It can operate as a **standalone product** and expand with [Sekoia Intelligence](/cti/index.md), [Reveal for Asset Intelligence](features/modules/reveal_index.md), and [Sekoia Elevate](features/modules/elevate_overview.md) for AI-assisted SOC workflows.

Defend collects and analyzes security events from applications, endpoints, cloud services, and SaaS environments. It gives security teams the tools to detect suspicious activity, investigate incidents, automate response actions, and report on their security operations.

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js"></script>
  <div class="sl-embed" style="position:relative;padding-bottom:56.25%;width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://sekoia.storylane.io/demo/8zdjfok9atpn?embed=popup" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
</div>

## Product features

### Collect security data

Sekoia Defend supports multiple ingestion methods for bringing security data into the platform. Teams can connect applications, endpoints, cloud services, and SaaS environments, then organize and enrich the events they collect.

The collection workflow includes:

1. **Choose an ingestion method:** Select the method that fits the data source and deployment model. See the supported [ingestion methods](/integration/ingestion_methods/index.md).
2. **Connect an integration:** Use the supported [Integrations](/integration/categories/index.md) catalog to collect data from security and business applications.
3. **Configure Intakes:** Set up the [Intakes](features/collect/intakes.md) that receive and process incoming logs.
4. **Organize Intakes into Entities:** Structure data sources around the systems, environments, or business units they represent with [Entities](features/collect/entities.md).
5. **Enrich events with Assets:** Add [asset](features/collect/assets.md) context to help analysts understand which systems and resources are involved.

### Detect threats

Sekoia Defend combines Cyber Threat Intelligence (CTI), anomaly detection, and detection scenarios to identify suspicious activity, intrusions, and compromises.

Security teams can:

- Review detection logic in the [Rules Catalog](features/detect/rules_catalog.md).
- Create and manage [custom detection rules](features/detect/sigma.md).
- Use [Sigma rules](features/detect/sigma.md) to make detection logic more portable across tools.

### Investigate alerts and incidents

Analysts can investigate activity directly from a security alert or through the event history. Case management helps teams connect related alerts, document findings, and collaborate throughout an investigation.

Defend supports:

- **Security alert investigation:** Review [alerts](features/investigate/alerts.md) and examine the activity behind them.
- **Event history and threat hunting:** Search historical [events](features/investigate/events.md) and drill down into relevant activity.
- **Case management:** Centralize observations, evidence, and investigation results around an incident with [Case Management](features/investigate/cases.md).

### Automate response

Sekoia Defend includes Security Orchestration, Automation and Response (SOAR) capabilities for repeatable response actions. Teams can use [Playbooks](features/automate/index.md) to automate parts of their SOC workflows, coordinate actions across security tools, and maintain an auditable record of what happened.

### Report on security operations

Use dedicated [Dashboards](features/report/dashboards.md) or create custom views to monitor security activity and operational metrics. Teams can build dashboards around the measures that matter to their SOC, including alert activity, investigation status, and response performance.
