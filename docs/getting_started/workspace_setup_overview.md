---
title: "Workspace setup overview"
description: "A step-by-step checklist for administrators to configure a Sekoia workspace before their team starts using the platform."
keywords: [workspace setup, admin, configuration, checklist, onboarding, users, roles, api keys, subscription]
audience: admin
module: all
type: task
---

# Workspace setup overview

Before your team can start detecting and responding to threats in Sekoia, an administrator must complete a set of configuration steps. This article gives you a checklist of everything to set up, in the recommended order, with links to each detailed procedure.

This section is intended for workspace administrators. Analysts who have been invited to an already-configured workspace can skip directly to [Set up your account](/getting_started/log_in_for_the_first_time.md).

## Prerequisites

- You have received a Sekoia workspace with administrator access.
- You have logged in and secured your own account (see [Secure your account](/getting_started/secure_your_account.md)).

## Configuration checklist

### Step 1: Verify your subscription and license level

Before inviting users or configuring intakes, confirm that your subscription includes the products and modules your team needs. Record the license type, retention settings, asset or data limits, and expiration date so your team can configure data collection within the contract.

Navigate to **Settings > Workspace > Subscriptions** and verify:

- Which products are active (Defend, Intelligence).
- Which add-on modules are enabled (Reveal, Elevate).
- The expiration date and limits of your current plan.
- The hot storage and archiving duration available for investigations.

See: [Understand your subscription](/getting_started/understand_your_subscription.md)

### Step 2: Start monitoring usage

Review consumption before configuring your first data source, then continue monitoring it as you add intakes, detection rules, and playbooks.

Navigate to **Settings > Usage** and review the current and projected consumption for each relevant community.

See: [Monitor your usage](/getting_started/monitor_your_usage.md)

If consumption approaches a limit, review [Investigate overusage](/xdr/usecases/playbook/investigate_overusage.md), the [Optimization rules overview](/xdr/features/collect/optimization_rules_overview.md), and [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md) before changing your data collection configuration.

### Step 3: Confirm your region

Ensure that all team members know the correct URL for your workspace region. The URL depends on where your workspace is hosted.

!!! warning "Region-specific URLs"
    All platform URLs (app, API, intake) are region-specific. Share the correct app URL with your team before inviting them. Analysts who use the wrong URL will not be able to access the workspace.

See: [Log in for the first time](/getting_started/log_in_for_the_first_time.md) for the full region URL reference.

### Step 4: Create communities (multi-tenant only)

If you manage multiple clients or business units, create a community for each one before inviting users.

Navigate to **Settings > Workspace > Communities** and create the communities you need. Each community operates independently with its own intakes, detection rules, and alerts.

See: [Workspace and communities](/getting_started/workspace_and_communities.md)

### Step 5: Define roles

Review the available roles before inviting users so you can assign the correct permissions from the start.

Sekoia provides three built-in roles: **Guest** (read-only), **Analyst** (read and write), and **Admin** (full access including management). You can also create custom roles with specific permission sets.

See: [Roles and permissions](/getting_started/roles_and_permissions.md)

### Step 6: Invite users

Invite your team members by email. Each user receives a welcome email with a link to set their password.

Navigate to **Settings > Workspace > Users** and click **Add new users**.

See: [Invite users](/getting_started/invite_users.md)

### Step 7: Create API keys

If your team uses integrations, playbooks that interact with external tools, or third-party CTI connections, create the necessary API keys before the team starts configuring intakes.

Navigate to **Settings > Workspace > API Keys** and create a key for each integration use case with the minimum permissions required.

See: [Manage API keys](/getting_started/manage_api_keys.md)

### Step 8: Configure notifications

Set up notification rules so your team receives alerts when critical events occur, such as a new high-urgency alert, an intake stopping data collection, or a playbook error.

Navigate to **Settings > Notifications** and create your first notification rules.

See: [Notification system overview](/getting_started/notification_system_overview.md)

## What comes next

Once your workspace is configured, guide your analysts through the quick start for their product:

- [Quick start: Defend](/getting_started/quick_start_defend.md): Connect data sources, activate detection rules, and triage alerts.
- [Quick start: Intelligence](/getting_started/quick_start_intelligence.md): Explore the threat database and read reports.
- [Quick start: Reveal](/getting_started/quick_start_reveal.md): Set up asset intelligence.
- [Quick start: Elevate](/getting_started/quick_start_elevate.md): Activate AI-powered alert triage.

## Related links

- [Understand your subscription](/getting_started/understand_your_subscription.md): What each plan includes and how to read your subscription page.
- [Monitor your usage](/getting_started/monitor_your_usage.md): How to review consumption from the beginning of your subscription.
- [Investigate overusage](/xdr/usecases/playbook/investigate_overusage.md): Identify the causes of usage above your expected volume.
- [Optimization rules overview](/xdr/features/collect/optimization_rules_overview.md): How optimization rules reduce unnecessary event processing.
- [Invite users](/getting_started/invite_users.md): How to add team members to your workspace or community.
- [Roles and permissions](/getting_started/roles_and_permissions.md): Built-in and custom roles explained.
- [Manage API keys](/getting_started/manage_api_keys.md): Create and manage programmatic access tokens.
- [Notification system overview](/getting_started/notification_system_overview.md): How to configure automated alerts for your team.
