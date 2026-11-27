# Choose the right endpoint telemetry strategy for your SOC

Your SOC needs endpoint visibility, but your infrastructure does not use one endpoint security product everywhere. Some workstations run Microsoft Defender, critical servers use another EDR, legacy systems cannot support kernel-level agents, and exporting all raw telemetry may require additional licensing.

Sekoia lets you combine full telemetry ingestion, alert-based investigation, Endpoint Agent collection, and existing log forwarders in one detection and response workflow. This approach gives your analysts consistent visibility while allowing you to adapt collection to your infrastructure and control ingestion volume.

## Scenario

Your organization operates a mixed infrastructure:

- Microsoft Defender protects most workstations.
- A separate EDR protects critical servers.
- Several legacy systems cannot run your standard EDR agent.
- Active Directory Domain Controllers are subject to a strict no-agent policy.
- Your EDR vendors charge extra to export raw telemetry at scale.

During an investigation, the SOC receives an alert on a workstation but cannot immediately determine whether the same activity affected a critical server or a Domain Controller. The team needs a collection strategy that provides broad coverage without exporting every event from every EDR.

The expected result is a unified workflow where Sekoia can:

- Ingest full endpoint telemetry where export is practical.
- Query the EDR data lake only when an alert requires more context.
- Cover systems without an EDR through the Sekoia Endpoint Agent or existing forwarders.
- Apply the same investigation and response process across endpoint products.
- Reduce low-value events before they increase ingestion volume.

## Do it in Sekoia

Use the following steps to select the right endpoint telemetry method for each part of your infrastructure, configure the corresponding collection path, and connect it to Sekoia detection and response workflows.

## Prerequisites

Before you start, make sure that you have:

- Access to a Sekoia Defend workspace with permission to create intakes and playbooks.
- Administrative access to the EDR platforms that you want to connect.
- API credentials for any EDR that Sekoia must query or control through playbooks.
- Azure permissions if you plan to forward Microsoft Defender XDR events through Azure Event Hub.
- Network access and installation permissions for hosts that will run the Sekoia Endpoint Agent or a log forwarder.
- An active **Elevate** licence if you want Sekoia to investigate alerts automatically.
- An active **Reveal** licence if you want to collect endpoint hygiene or application inventory data.

## Step 1: Choose the collection method for each part of your infrastructure

Your infrastructure may require several collection methods. Use the following table to select the most appropriate option for each asset group.

| Your environment | Recommended method | Main benefit |
| --- | --- | --- |
| EDR with free or low-cost telemetry export, such as HarfangLab or Microsoft Defender through Azure Event Hub | **Full telemetry ingestion** | Maximum real-time detection and CTI matching with complete endpoint context |
| EDR with costly telemetry export add-ons, such as CrowdStrike Falcon Telemetry, SentinelOne Cloud Funnel 2.0, or Palo Alto | **On-demand querying** | Avoid exporting all raw telemetry while preserving investigation context when an alert requires it |
| Servers without an EDR, legacy operating systems, or Active Directory Domain Controllers | **Sekoia Endpoint Agent or log forwarders** | Extend endpoint visibility to systems that cannot use the standard EDR collection path |

You can combine these methods in the same environment. For example, you can ingest full telemetry from Microsoft Defender, query SentinelOne only when an alert requires more context, and use WEF/WEC with NXLog to collect Domain Controller events without installing an agent.

## Step 2: Integrate endpoint telemetry 

### Option A: Configure full telemetry ingestion when raw export is available

Use full telemetry ingestion when your EDR can export raw endpoint events without prohibitive licensing or infrastructure costs.

This method provides the most complete detection and investigation context in Sekoia. It is particularly useful when you want Sekoia to apply its own detection rules and threat intelligence matching to process, file, network, DNS, and registry activity.

#### A.1 Create the EDR intake

In Sekoia, open **Intakes** and create the integration that matches your endpoint source. Then configure the EDR to forward both alerts and raw endpoint telemetry to the intake.

Examples include:

- [HarfangLab](/integration/categories/endpoint/harfanglab.md), which supports alert and telemetry collection.
- [Microsoft Defender XDR](/integration/categories/endpoint/microsoft_365_defender.md), which can forward supported event types through Azure Event Hub.
- [CrowdStrike Falcon Telemetry](/integration/categories/endpoint/crowdstrike_falcon_telemetry.md).
- [SentinelOne Cloud Funnel 2.0](/integration/categories/endpoint/sentinelone_cloudfunnel2.0.md).

Forward the event types required for detection and investigation, such as:

- Process execution.
- File changes.
- Network connections.
- DNS activity.
- Registry changes.
- PowerShell or command execution.
- Authentication and logon activity.

#### A.2 Use normalized endpoint events

Sekoia parses and normalizes the events received from the different endpoint sources. Your detection rules, event queries, and dashboards can therefore use the same normalized fields across EDR vendors.

This means that changing the EDR protecting a group of endpoints does not require you to rebuild all your Sekoia detection and investigation logic.

See [Intake formats overview](/integration/develop_integration/formats/overview.md), [Parsing and ECS normalization](/integration/develop_integration/formats/parser.md), and [Querying events](/xdr/features/investigate/querying_events.md).

#### A.3 Investigate with Sekoia detection, CTI, and Elevate

Once the telemetry is available in Sekoia:

1. Apply Sekoia detection rules in addition to the EDR's native detections.
2. Match hashes, IP addresses, and domains with Sekoia CTI.
3. Use [Sekoia Elevate](/xdr/features/modules/elevate_overview.md) to investigate the alert across endpoint, network, identity, and cloud data.

See [The Elevate investigation method](/xdr/features/modules/elevate_investigation_method.md) for more information about how Elevate collects evidence and reaches a verdict.

### Option B: Configure on-demand querying when full export is not practical

Use on-demand querying when your EDR stores detailed telemetry in its own data lake, but exporting all of that telemetry to Sekoia would require an expensive add-on or create unnecessary ingestion volume.

In this setup, Sekoia receives the alerts continuously and retrieves raw telemetry only when an investigation requires it.

#### B.1 Ingest alerts only

Create an alert intake for your EDR and forward only the alerts that require investigation in Sekoia.

Examples include:

- [CrowdStrike Falcon](/integration/categories/endpoint/crowdstrike_falcon.md).
- [SentinelOne](/integration/categories/endpoint/sentinelone.md).
- [Microsoft Defender XDR Graph API](/integration/categories/endpoint/microsoft_365_defender_graphapi.md).

Sekoia can then correlate these alerts with network, identity, cloud, and other security data already available in the platform.

#### B.2 Connect the EDR API

Configure the EDR account in **Playbooks** so that Sekoia can communicate with the EDR through its API.

This bidirectional connection allows Sekoia to retrieve additional telemetry or trigger response actions without requiring the EDR to export its entire data lake.

#### B.3 Query the EDR during the investigation

When an alert requires more context, use Elevate and Playbooks to query the external EDR.

For example:

- Use **Query events in Deep Visibility** with SentinelOne to retrieve events for a specific query and time range.
- Use **Get agent telemetry** with HarfangLab to retrieve process, network, DNS, or authentication telemetry around an alert.
- Use **List processes** with HarfangLab to inspect the processes running on the affected endpoint.

See the [SentinelOne automation library](/xdr/features/automate/library/sentinelone.md) and the [HarfangLab automation library](/xdr/features/automate/library/harfanglab.md) for the available actions.

### Option C: Cover systems outside the EDR perimeter

Use the Sekoia Endpoint Agent or existing log forwarders to cover systems that do not have an EDR, cannot run your standard EDR agent, or must remain agentless.

This method is particularly useful for:

- Critical servers without EDR coverage.
- Legacy operating systems.
- Linux and macOS systems outside the EDR perimeter.
- Active Directory Domain Controllers.
- Environments where EDR telemetry export costs are too high.

#### C.1 Deploy the Sekoia Endpoint Agent

The [Sekoia Endpoint Agent](/integration/categories/endpoint/sekoiaio.md) supports Windows, Linux, and macOS. It can collect endpoint telemetry as a standalone collector or alongside an existing EDR.

Create a Sekoia Endpoint Agent intake and follow the [installation guide](/integration/categories/endpoint/install_sekoia_endpoint_agent.md).

During installation, enable the collector roles that match your requirements:

- **Telemetry and Active Directory:** Use the `event-collector` role to collect process, file, DNS, network, PowerShell, and Sysmon events. You can also use it to collect Active Directory security logs on Domain Controllers.
- **Security posture checks:** Use the `compliance-collector` role to collect endpoint hygiene information, such as disk encryption and host firewall status. This feature requires Sekoia Reveal.
- **Software and vulnerability inventory:** Use the `software-collector` role to collect installed applications, versions, and associated vulnerability information. This feature also requires Sekoia Reveal.

See [Configure the Sekoia Endpoint Agent](/integration/categories/endpoint/configure_sekoia_endpoint_agent.md) for the available configuration options and [Events and fields reference](/integration/categories/endpoint/sekoia_endpoint_agent_events_reference.md) for the collected data.

> **Active Directory Domain Controllers**
>
> Deploying the Sekoia Endpoint Agent on a Domain Controller may be appropriate when your organization allows endpoint agents on these systems. However, some Microsoft troubleshooting procedures require administrators to completely uninstall third-party agents during deep operating system or Active Directory investigations.
>
> If your IT policy does not allow agents on Domain Controllers, use the WEF/WEC and NXLog method described below.

#### C.2 Reuse existing log forwarders

If you already have a log collection infrastructure, reuse it instead of deploying another agent.

For Active Directory, use Windows Event Forwarding with a Windows Event Collector and NXLog to forward authentication and security logs to Sekoia without installing an agent directly on the Domain Controllers.

See the [Windows integration guide](/integration/categories/endpoint/windows.md).

For Elastic environments, forward existing collector streams to Sekoia:

- Use [Winlogbeat](/integration/categories/endpoint/winlogbeat.md) for Windows Event Logs.
- Use [Linux Auditbeat](/integration/categories/endpoint/auditbeat_linux.md) for Linux audit and system activity.

## Step 3: Control telemetry volume and ingestion costs

Once your collection methods are in place, apply filtering at the earliest possible point in the pipeline.

Sekoia recommends the following hierarchy:

1. **Source-level filtering:** Configure the EDR export policy to send only security-relevant event types.
2. **Agent-level filtering:** When using the Sekoia Endpoint Agent, apply optimization rules on the host to remove high-volume, low-value events before transmission.
3. **Platform-level filtering:** Use Sekoia optimization rules to filter parsed events at the intake when filtering at the source or forwarder is not possible.

See [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md) and [Reduce event volume with the Sekoia Endpoint Agent](/integration/categories/endpoint/reduce_event_volume_endpoint_agent.md).

Filtering at the source or on the agent reduces network traffic and ingestion volume. Platform-level filtering takes place after the event has reached Sekoia, so it mainly reduces processing and storage.

## Step 4: Automate response across your EDR tools

The collection method does not determine how you respond to an incident. Once your EDR accounts are connected to Sekoia, Playbooks can trigger investigation, enrichment, and containment actions across different endpoint products.

Examples include:

- **Host isolation**
  - **Isolate hosts** with CrowdStrike Falcon.
  - **Isolate an endpoint** with SentinelOne.
  - **Isolate a machine** with Microsoft Defender.
  - **Isolate an agent** with HarfangLab.
- **Hash and IOC blocking**
  - **Block IOC** or **Push IOCs for prevention** with CrowdStrike Falcon.
  - **Block SHA-1 and/or SHA-256** with SentinelOne.
  - **Push IOCs** with Microsoft Defender.
  - **Create IOCs** with HarfangLab and enable `block_on_agent`.
- **Forensic collection**
  - **Download File from Endpoint** with HarfangLab.
  - **Get malwares from threat** with SentinelOne.

See the relevant automation libraries for [CrowdStrike Falcon](/xdr/features/automate/library/crowdstrike-falcon.md), [SentinelOne](/xdr/features/automate/library/sentinelone.md), [Microsoft Defender](/xdr/features/automate/library/microsoftdefender.md), and [HarfangLab](/xdr/features/automate/library/harfanglab.md).

If your endpoint product is not available in the library, use the [Automation SDK](/integration/develop_integration/automation/create_a_module.md) to build a custom connector or action.

## Outcome

You now have a collection strategy adapted to each part of your infrastructure:

- Full telemetry ingestion provides the deepest detection and investigation context where raw export is affordable.
- On-demand querying preserves investigation context without exporting all EDR telemetry.
- The Sekoia Endpoint Agent and existing log forwarders cover servers, legacy systems, Linux and macOS hosts, and agentless Domain Controller deployments.
- Source, agent, and platform filtering help control telemetry volume.
- Playbooks and Elevate connect investigation and response across your EDR tools.

This gives your SOC one endpoint detection and response workflow, even when the underlying collection methods and EDR products differ.

## Related articles

- [Sekoia Endpoint Agent](/integration/categories/endpoint/sekoiaio.md): Review supported operating systems, collected events, and resource usage.
- [Install the Sekoia Endpoint Agent](/integration/categories/endpoint/install_sekoia_endpoint_agent.md): Create an intake and deploy the agent on Windows, Linux, or macOS.
- [Configure the Sekoia Endpoint Agent](/integration/categories/endpoint/configure_sekoia_endpoint_agent.md): Configure optional collectors and agent settings.
- [Microsoft Defender XDR](/integration/categories/endpoint/microsoft_365_defender.md): Forward Defender telemetry through Azure Event Hub.
- [HarfangLab](/integration/categories/endpoint/harfanglab.md): Forward HarfangLab alerts and endpoint telemetry.
- [Sekoia Elevate](/xdr/features/modules/elevate_overview.md): Understand autonomous alert investigation and analyst validation.
- [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md): Review an Elevate investigation and its findings.
- [Playbooks](/xdr/features/automate/index.md): Build workflows that query external systems and trigger response actions.
- [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md): Apply filtering at the source, forwarder, and platform levels.
