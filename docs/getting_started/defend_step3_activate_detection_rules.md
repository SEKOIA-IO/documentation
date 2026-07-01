---
title: "Step 3: Activate detection rules"
description: "Browse the Sekoia Defend rules catalog, understand effort levels, and activate detection rules to start generating security alerts."
keywords: [detection rules, rules catalog, effort level, mitre attack, sigma, activate rules, automatic rules, coverage]
audience: analyst
module: defend
type: task
---

# Step 3: Activate detection rules

Detection rules are the logic that transforms raw events into security alerts. Sekoia provides a catalog of over 1,000 verified rules, each mapped to a specific MITRE ATT&CK technique. This step guides you through understanding the catalog, choosing which rules to activate, and reviewing your detection coverage.

## Before you begin

- You have completed [Step 2: Verify event reception](/getting_started/defend_step2_verify_event_reception.md) and your intake is receiving valid events.

## Open the rules catalog

In the navigation menu, select **Configure > Rules Catalog**.

The catalog lists all rules available to your community. Each rule shows its name, effort level, type, associated threats, and compatible intake formats.

> 📸 [SCREENSHOT SUGGESTION: The rules catalog page showing a list of rules with effort level badges, type indicators, and the MITRE ATT&CK matrix preview. | ALT TEXT: Rules catalog showing detection rules with effort levels and MITRE ATT&CK coverage matrix.]

## Understand effort levels

Every rule has an effort level that indicates how much configuration it requires and how likely it is to generate false positives.

| Level | Description | Recommended action |
|---|---|---|
| **Elementary** | Requires no effort to enable, generates few false positives | Enable all at initial setup |
| **Intermediate** | Similar to Elementary but may produce more alerts | Enable all at initial setup |
| **Advanced** | May need tuning depending on your environment | Enable selectively after the initial run period |
| **Master** | High detection specificity, requires environment-specific tuning | Enable progressively with alert filters |

## Activate rules for your first setup

For a new Sekoia deployment, follow this recommended sequence:

### Activate all Elementary and Intermediate rules

1. In the rules catalog, click on **Filters**.
2. Set **Effort level** to **Elementary**.
3. Click on the **Enable/Disable rules** button.
4. Click **Select all**
5. Click **Enable**.
6. Repeat with **Effort level** set to **Intermediate**.

This gives you broad detection coverage immediately with minimal false positive risk.

### Filter by your intake format

To see only the rules that apply to your connected data sources:

1. In the left panel, in **Filters rules by intake format** section, select your intake format (for example, **Windows**, **Office 365**, or **Palo Alto**).
2. The catalog filters to show only rules compatible with that intake.
3. Enable the rules relevant to your environment.

!!! tip "Configured badge"
    Rules that are compatible with an intake you have already configured show a **Configured** badge. Use this to quickly identify which rules can start generating alerts immediately.

## Set up automatic rule enablement

New verified rules are added to the catalog regularly. To ensure your detection coverage stays current without manual review:

1. Click the **Settings** icon in the top right of the rules catalog page.
2. Under **New verified rules**, select the maximum effort level you want enabled automatically (for example, **Intermediate**).
3. Toggle on the **Enable new verified rules** option. 
4. Save your configuration.

From this point, all new Sekoia-verified rules up to that effort level are activated automatically when they are added to the catalog.

## Review your MITRE ATT&CK coverage

The rules catalog includes a MITRE ATT&CK matrix view that shows your detection coverage across tactics and techniques.

To open the full matrix:

1. Scroll to the matrix preview on the rules catalog page.
2. Click the preview to open the full-screen view.

Darker cells indicate more rules covering that technique. White cells indicate gaps in your coverage. Use this view to identify which areas of the attack chain you are not yet monitoring.

![MITRE ATT&CK matrix showing detection rule coverage with color-coded cells.](docs/assets/getting_started/mitre_matrix.png){: style="width: 100%; max-width: 100%"}


## Related links

- [Step 4: Triage your first alert](/getting_started/defend_step4_triage_first_alert.md) — What to do when detection rules start generating alerts.
- [Notification system overview](/getting_started/notification_system_overview.md) — Set up a notification to be informed when new rules are added to the catalog.
