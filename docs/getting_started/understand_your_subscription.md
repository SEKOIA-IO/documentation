---
title: "Understand your subscription"
description: "Learn what each Sekoia plan includes, how add-on modules work, and how to read your subscription page."
keywords: [subscription, plan, defend core, defend prime, intelligence, reveal, elevate, trial, license, modules]
audience: admin
module: all
type: concept
---

# Understand your subscription

Sekoia is available in several plans that determine which products and features your team can access. This article explains the plan structure, the add-on modules, and how to interpret the information on your Subscriptions page.

## Who can access this page

Navigate to **Settings > Workspace > Subscriptions**.

| Role | View subscriptions | Allocate or manage subscriptions |
|---|---|---|
| **Admin** | Yes | Yes |
| **Analyst** | Yes | No |
| **Guest** | Yes | No |

To allocate a subscription or trial to a community, your account must also have the **Manage community licenses** permission enabled on your role.

## Products and plans

Sekoia offers two core products, which are sold and licensed separately.

### Sekoia Defend

Sekoia Defend is the XDR product for detection and response operations. It is available in two plans:

| Plan | What it includes |
|---|---|
| **Defend Core** | Collect, Detect, Investigate, and Automate capabilities. Standard retention and asset limits. |
| **Defend Prime** | All Defend Core capabilities, plus extended retention, higher asset limits, and priority access to new features. |

The key parameters that vary between plans and contracts include:

- **Number of defended assets** — the volume of assets covered under the license
- **Hot storage** — the number of days events are kept in fast-access storage for search and investigation
- **Archiving duration** — the total retention period for archived event data

### Sekoia Intelligence

Sekoia Intelligence is the CTI product for threat knowledge and analysis. It is licensed separately from Defend and can be purchased independently or combined with a Defend plan.

## Add-on modules

Add-on modules extend Defend with specialized capabilities. They require an active Defend subscription.

| Module | What it adds |
|---|---|
| **Reveal** | Asset intelligence: unified inventory, vulnerability context, behavioral signals, attack path visualization |
| **Elevate** | AI-powered agentic triage: autonomous alert analysis and verdict generation |

## Trial subscription

When a new community is created, a trial subscription is automatically made available. The trial allows you to explore the platform without a financial commitment.

| Property | Value |
|---|---|
| Duration | 45 days |
| Plan | Defend Prime |
| Number of assets | Up to 1,000 |
| Hot storage | 7 days |
| Archiving duration | 0 days |

!!! note "Allocating a trial to a community"
    In a multi-tenant workspace, administrators can allocate trial subscriptions to managed communities. See the related link at the end of this article for the procedure.

## Read the Subscriptions page

The Subscriptions page gives you a centralized view of all active and expired licenses for your communities.

To access the Subscriptions page, navigate to **Settings > Workspace > Subscriptions**.

For each subscription, you can see:

- The plan type (Defend Core, Defend Prime, or Intelligence)
- The subscription period and expiration date
- The region, number of defended assets, and storage retention values
- The remaining days on the subscription

!!! warning "Expired subscriptions"
    Communities with no active subscription are flagged with a red indicator in the multi-tenant community list. An expired subscription does not delete your data, but it may limit your access to platform features.

In a multi-tenant workspace, the Subscriptions page shows all managed communities. You can filter the list by trial status, near-expiration, or inactive communities.

## Compare plans

To view a comparison of available plans directly in the platform, click **Compare plans** on the Subscriptions page. To discuss an upgrade or renewal, click **Contact us**.

## Related links

- [Workspace setup overview](/getting_started/workspace_setup_overview) — Full checklist for configuring your workspace before your team starts.
- [Invite users](/getting_started/invite_users) — How to add team members once your subscription is confirmed.
