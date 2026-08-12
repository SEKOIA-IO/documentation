---
title: "Monitor your usage"
description: "Review your Sekoia consumption from the start of your subscription and identify changes before they affect your data coverage or operations."
keywords: [usage, consumption, analyzed bytes, playbook actions, license, retention, limits, optimization]
audience: all
module: all
type: task
---

# Monitor your usage

The Usage page shows how your communities consume the resources covered by your Sekoia license. Review it from the start of your subscription to compare current consumption with your license limits and identify changes early.

## Before you begin

- You must have access to **Settings > Usage**.
- You must know the license type and limits assigned to your community. See [Understand your subscription](/getting_started/understand_your_subscription.md).

!!! note "Usage and permissions"
    If the **Usage** page is not available in your **Settings** menu, ask your workspace administrator to confirm your consumption and license limits.

## Review your consumption

1. Open **Settings**.
2. Select **Usage**.
3. Select the month you want to review.
4. Review the consumption metrics available for your community.

The page can include the following information:

| Metric | What it shows |
|---|---|
| **Analyzed bytes** | The volume of data analyzed for the selected community and month. |
| **Current consumption** | The volume already consumed during the selected period. |
| **Projected consumption** | An estimate of the volume expected by the end of the period, based on consumption trends. |
| **Executed playbook actions** | The number of actions executed by playbooks for the selected community and month. |
| **Subscribed assets** | The number of assets covered by the subscription, when the metric is available for your plan. |

The metrics shown depend on your product and license. Some Intelligence-only communities may have fewer consumption widgets.

## Review multi-tenant consumption

In a multi-tenant workspace, use the community summary to compare consumption across managed communities. Review the following information for each community when available:

- Community name.
- Subscription type.
- Number of subscribed assets.
- Analyzed bytes for the selected month.

Use this view to identify a community whose consumption differs from the others or approaches its contracted limit.

## Establish a monitoring routine

Review the Usage page:

- At the beginning of the subscription period, to record the starting point.
- After adding a new intake or increasing an existing data source volume.
- After enabling detection rules or playbooks that can increase processing or action volume.
- Before the end of each month, to compare current and projected consumption.

If consumption approaches a limit, review [Investigate overusage](/xdr/usecases/playbook/investigate_overusage.md), the [Optimization rules overview](/xdr/features/collect/optimization_rules_overview.md), and [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md). Ask your workspace administrator or Customer Success Manager (CSM) about contract-specific limits and options when relevant.

## Related links

- [Understand your subscription](/getting_started/understand_your_subscription.md): Identify your license type, retention settings, and limits.
- [Investigate overusage](/xdr/usecases/playbook/investigate_overusage.md): Identify the causes of usage above your expected volume.
- [Optimization rules overview](/xdr/features/collect/optimization_rules_overview.md): Configure rules that reduce unnecessary event processing.
- [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md): Review practical ways to control data volume.
- [Workspace setup overview](/getting_started/workspace_setup_overview.md): Complete the administrator setup checklist.
