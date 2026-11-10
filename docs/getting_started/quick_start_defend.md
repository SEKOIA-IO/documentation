---
title: "Quick start: Defend"
description: "A five-step tutorial to start protecting your organization with Sekoia Defend: from connecting your first data source to automating alert responses."
keywords: [quick start, defend, xdr, getting started, tutorial, intakes, detection rules, alerts, playbooks]
audience: analyst
module: defend
type: tutorial
---

# Quick start: Defend

Sekoia Defend is your extended detection and response platform. In five steps, you will connect your first data source, verify that events are flowing into the platform, activate detection rules, triage your first alert, and set up a basic automated response. By the end of this guide, your SOC environment will be operational.

## Learning goal

After completing this guide, you will be able to:

- Connect at least one data source and verify event reception
- Activate detection rules and understand coverage across the MITRE ATT&CK framework
- Navigate and triage alerts
- Activate a playbook to automate a response action

## Prerequisites

- You have logged in to Sekoia and your account is active.
- Your workspace administrator has confirmed your subscription is active. Review [Understand your subscription](understand_your_subscription.md) and [Monitor your usage](monitor_your_usage.md) before connecting a data source.
- You have the **Analyst** or **Admin** role in your community.

{% hint style="info" %}
**Admin access required for Step 1**

Connecting a data source (creating an intake) requires Admin access or a custom role with intake management permissions. If you do not have this access, ask your administrator to complete Step 1 and then continue from Step 2.
{% endhint %}

## The five steps

| Step | What you do | Time estimate |
|---|---|---|
| [Step 1](defend_step1_connect_data_source.md) | Connect a data source | 10-20 min |
| [Step 2](defend_step2_verify_event_reception.md) | Verify event reception | 5-10 min |
| [Step 3](defend_step3_activate_detection_rules.md) | Activate detection rules | 10-15 min |
| [Step 4](defend_step4_triage_first_alert.md) | Triage your first alert | 15-30 min |
| [Step 5](defend_step5_automate_with_playbooks.md) | Automate with playbooks | 15-20 min |

## Outcome

When you complete all five steps, you will have a functioning Sekoia Defend environment that collects your logs, detects threats as they arrive, and surfaces alerts for investigation. You will also have your first automated response workflow active.

If your subscription includes Elevate, the next step is to activate AI-powered alert triage. See [Quick start: Elevate](quick_start_elevate.md).

## Prefer to learn with video?

Each step in this guide is also covered in the Sekoia Academy. Visit the [Academy](https://academy.sekoia.io) to follow along with video tutorials.

## Related links

- [Step 1: Connect a data source](defend_step1_connect_data_source.md): Create your first intake and connect a log source.
- [Step 2: Verify event reception](defend_step2_verify_event_reception.md): Confirm that events are flowing into the platform.
- [Step 3: Activate detection rules](defend_step3_activate_detection_rules.md): Enable rules from the catalog and review your MITRE ATT&CK coverage.
- [Step 4: Triage your first alert](defend_step4_triage_first_alert.md): Investigate and close your first security alert.
- [Step 5: Automate with playbooks](defend_step5_automate_with_playbooks.md): Set up an automated response workflow.
- [Workspace setup overview](workspace_setup_overview.md): Admin checklist to prepare the workspace before this guide.
- [Quick start: Elevate](quick_start_elevate.md): Activate AI-powered alert triage once your Defend environment is running.
