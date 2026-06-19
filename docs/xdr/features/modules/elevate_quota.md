# Manage your Elevate runs

Elevate operates on a monthly run pack. Each investigation the agent runs, whether automatic or manually triggered, consumes one run. This article explains how to monitor your runs and how to optimize consumption so you do not exhaust your run pack before the end of the month.

## Prerequisites

[PLACEHOLDER: Confirm the required role to view and manage runs, for example administrator.]

## Monitor your runs

Track your run consumption from the Usage page. Navigate to **Settings > Usage** to view consumed runs against your monthly run pack, your daily burn, and, for MSSPs, the consumption of each community.

[PLACEHOLDER: Confirm the exact location and name of the Elevate runs view on the Usage page, then add a screenshot placeholder.]

When the run pack is exhausted, the agent stops analyzing new alerts and displays the **AI monthly quota limit reached** state on any alert it cannot process.

!!! note "Runs reset monthly"
    Runs reset at the start of each month and do not roll over. Unused runs from one month are not added to the next.

## Optimize run consumption

You can reduce consumption without disabling Elevate entirely by restricting which alerts the agent analyzes.

**Filter by detection rule** to focus the agent on alert types where AI investigation adds the most value and skip categories already handled by playbooks. See [Limit auto-analysis to specific rules](/xdr/features/modules/elevate_rule_filter.md).

**Disable auto-analysis for specific communities** when certain sub-tenants generate high alert volumes that do not require AI investigation. See [Override Elevate settings for a community](/xdr/features/modules/elevate_community_override.md).

**Use manual analysis selectively** to trigger investigations only on alerts that warrant deeper review. See [Trigger a manual Elevate analysis](/xdr/features/modules/elevate_manual_analysis.md).

## Run management for MSSPs

If you manage multiple communities, your sub-tenants draw from a shared workspace run pack. From the Usage page you can review each community's consumption against the pack. To keep a single noisy sub-tenant from consuming a disproportionate share, disable or limit auto-analysis for that community. See [Override Elevate settings for a community](/xdr/features/modules/elevate_community_override.md) and [Limit auto-analysis to specific rules](/xdr/features/modules/elevate_rule_filter.md).

## What happens when the run pack is exhausted

When your monthly run pack is reached:

- The agent stops analyzing new alerts automatically.
- Alerts that cannot be analyzed display the **AI monthly quota limit reached** state in the **Verdict** column.
- Manual analysis via Roy is also blocked until your runs reset.

Runs reset automatically at the start of next month.

[PLACEHOLDER: Confirm whether a self-serve run top-up or a larger run pack is available before the monthly reset, and add the relevant steps if so.]

## Related articles

- [Elevate](/xdr/features/modules/elevate_overview.md): Concept overview of how Elevate works and its key concepts.
- [Elevate analysis states](/xdr/features/modules/elevate_analysis_states.md): Reference table of all possible AI analysis states including AI limit reached.
- [Limit auto-analysis to specific rules](/xdr/features/modules/elevate_rule_filter.md): How to restrict which alerts Elevate analyzes to control consumption.
- [Override Elevate settings for a community](/xdr/features/modules/elevate_community_override.md): How to disable Elevate for specific communities to reduce consumption.
