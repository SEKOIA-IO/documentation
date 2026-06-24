# Sekoia Defend 

!!! note "Licensing & Ecosystem"
    Sekoia Defend is the foundational module of the Sekoia AI SOC Platform. It operates as a **standalone product** for detection and response. Its capabilities can be seamlessly extended by integrating **Sekoia Intelligence** (also available standalone), or by activating the **Reveal** and **Elevate** modules.

    
Sekoia Defend makes it possible to easily integrate and analyze the events produced by your applications, endpoints, cloud and SaaS perimeters in real time, and we designed it with the sole purpose of protecting your assets from potential cyber threats.


  <script async src="https://js.storylane.io/js/v2/storylane.js"></script>
  <div class="sl-embed" style="position:relative;padding-bottom:56.25%;width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://sekoia.storylane.io/demo/8zdjfok9atpn?embed=popup" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>

## Product Features

### Collect

To defend your business, you need to know what's going on. Monitoring your assets is a prerequisite for their security.
Sekoia.io is able to collect logs via various mechanisms, setting it up on your end is easy!

1. Find out the supported [ingestion methods](/integration/ingestion_methods/index.md).
2. Take a look at our pre-defined [Integrations](/integration/categories/index.md)' list that keeps growing to suit all of your needs.
3. Configure your [Intakes](features/collect/intakes.md) to collect your logs.
4. Organize your intakes in [Entities](features/collect/entities.md).
5. Enrich your events with your [Assets](features/collect/assets.md).

### Detect

Sekoia.io combines Cyber Threat Intelligence, anomaly detection and advanced Threat detection scenarios to effectively detect attacks, intrusions and compromises. By design, Sekoia.io is built to protect your organization against the most aggressive and advanced threats.

1. Discover the [Rules Catalog](features/detect/rules_catalog.md).
2. Create your [own detection rules](features/detect/sigma.md).

### Investigate

Sekoia Defend (XDR) allows you to conduct investigations on malicious activities directly from an alert or by means of the event history.
Case management makes it possible to reconcile alerts with each other and to document the associated analyzes and results.

1. Review [Security Alerts](features/investigate/alerts.md) raised by Sekoia.io and investigate on their malicious activities.
2. Hunt down the intruders with the [Event History](features/investigate/events.md) and its drill down capabilities.
3. Use [Case Management](features/investigate/cases.md) to centralize your observations on an incident and collaborate with other stake holders.

### Automate

Automating your security improves your cybersecurity operations by consolidating your procedures. SOC Automation combines security tools, processes and people to accelerate the execution of your security responses while ensuring their repeatability and auditability.

- Manage your [Playbooks](features/automate/index.md) to automate your SOC.

### Report

- Review your Security with dedicated [Dashboards](features/report/dashboards.md) or build your own control center.

### Reveal (Asset Visibility & Inventory)

Reveal is an add-on module that continuously discovers, unifies, and contextualizes your assets (hosts, accounts, networks). It merges data from third-party asset inventories, vulnerability management tools, the sekoia endpoint agent and passive asset identification into a single, unified Asset Inventory.  

Each asset is enriched with a context such as, Timeline, Hygiene posture, Vulnerabilities, and Points of Interest. Open the Asset Context Panel from Alerts, Cases, Events, or Assets to see identity, activity, and risk in place — speeding up triage and decisions.  

#### Get started
1. Connect sources: Deploy the [Sekoia Endpoint Agent](https://docs.sekoia.io/integration/categories/endpoint/sekoiaio/#enabling-host-hygiene-collection) and integrate your [asset inventory](https://docs.sekoia.io/xdr/features/collect/integrations_hub/) and [vulnerability management](https://docs.sekoia.io/xdr/features/collect/integrations_hub/) tools.  
2. Curate inventory: Assign criticality, tags; resolve duplicates and address coverage gaps through your [asset inventory](https://docs.sekoia.io/xdr/features/collect/assets/#your-asset-inventory).  
3. Investigate: Use the Asset Context Panel (coming soon) anywhere to view your assets with context.
