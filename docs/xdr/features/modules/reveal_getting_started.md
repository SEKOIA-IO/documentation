# Getting started with Reveal

Reveal is a Sekoia add-on module that adds asset intelligence to your investigation workflows. This guide walks you through the setup process and helps you validate that each capability works as expected.

## Learning goal

After completing this guide, you will have a functional Reveal setup that provides asset context, activity history, vulnerability data, endpoint hygiene, and relationship analysis directly in your investigation workflows.

## Before you begin

Confirm that the following conditions are met before you start:

- The Reveal add-on module is enabled for your community. Without it, Reveal-specific capabilities are not available.
- You have access to at least one supported telemetry source.

You do not need all data sources to start. Each source unlocks additional capabilities. Refer to the [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md) to understand what each source provides.

## Step 1: Onboard telemetry

Onboard the telemetry required to start Passive Asset Discovery.

!!! note "Passive Asset Discovery starts automatically"
    You do not need to enable Passive Asset Discovery manually. It starts as soon as Sekoia receives supported telemetry containing asset identifiers.

Passive Asset Discovery creates, merges, and lightly enriches asset records from identifiers observed in your telemetry. It gives you a starting point for asset-centric investigation before you configure any connectors.

## Step 2: Validate event data coverage

Check that Sekoia receives event data from the sources required for activity-based features.

Useful event sources include:

- Authentication logs
- Identity provider logs
- Endpoint activity
- Network activity

Event data is required for asset timelines, Points of Interest, Attack Path Visualization, and alert and case context.

## Step 3: Configure Asset Connectors

Configure Asset Connectors to enrich assets with structured context from your external systems.

To get the most value, prioritize connectors that provide:

- Identity and account information
- Endpoint information and posture
- Vulnerability data

Asset Connectors provide deeper and more authoritative context than Passive Asset Discovery alone.

## Step 4: Deploy the Sekoia Endpoint Agent

Deploy the Sekoia Endpoint Agent on endpoints where you need direct endpoint visibility and hygiene signals.

The agent provides:

- Endpoint identity and presence
- Local posture information
- Hygiene signals such as firewall and disk encryption status (where supported)

Deploy the agent when endpoint posture must be visible in Reveal, or when endpoint-level context should complement your connector data.

## Step 5: Validate the analyst experience

Open the asset context panel from an alert, case, or asset view and confirm the following:

- Asset identity and key attributes are populated.
- Recent activity is visible in the asset timeline.
- Related alerts and cases appear when available.
- Vulnerabilities are listed when a vulnerability connector is configured.
- Endpoint hygiene signals are present when the agent or a supported connector is deployed.
- Points of Interest appear when behavioral event data is available.
- Attack Path Visualization shows relationships when authentication event data is available.

> 📸 [SCREENSHOT SUGGESTION: Asset context panel showing populated overview tab with identity, timeline, vulnerabilities, and hygiene cards visible. | ALT TEXT: Asset context panel with asset data populated across multiple tabs.]

## Outcome

When all steps are complete, analysts can open any asset from an alert or case and immediately see its identity, activity history, posture, exposure, and relationships without pivoting to external tools.

To get the most out of Reveal, combine all four data sources: telemetry for passive discovery, event data for activity context, Asset Connectors for deep enrichment, and the Sekoia Endpoint Agent for endpoint posture.

## Related links

- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md)
- [Troubleshoot Reveal](/xdr/features/modules/reveal_troubleshoot.md)
- [Asset context panel](/xdr/features/investigate/asset_context_panel.md)
- [Attack Path Visualization](/xdr/features/investigate/attack_path_visualization.md)
- [Points of Interest](/xdr/features/detect/points_of_interest.md)
