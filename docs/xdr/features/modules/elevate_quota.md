# Manage your Elevate investigation quota

Elevate operates on a monthly investigation quota. Each alert analyzed by the agent, whether automatically or manually triggered, consumes one unit. This article explains how to monitor your quota and how to optimize usage to avoid reaching the limit before the end of your billing cycle.

## Prerequisites

[PLACEHOLDER: Confirm required role to view and manage quota, e.g. administrator.]

## Monitor your quota

[PLACEHOLDER: Confirm the exact location of the quota view, e.g. Settings > Usage or a dedicated Elevate dashboard. Add screenshot placeholder once confirmed.]

Your quota usage is displayed as a progress bar showing consumed units against your monthly allocation (for example, 1000/1000). When the limit is reached, the agent stops analyzing new alerts and displays the **AI limit reached** state on any alert it cannot process.

## Optimize quota usage

You can reduce quota consumption without disabling Elevate entirely by restricting which alerts the agent analyzes.

**Filter by detection rule** to focus the agent on alert types where AI investigation adds the most value and skip categories already handled by playbooks. See [Limit auto-analysis to specific rules](/xdr/features/modules/elevate_rule_filter.md).

**Disable auto-analysis for specific communities** when certain sub-tenants generate high alert volumes that do not require AI investigation. See [Override Elevate settings for a community](/xdr/features/modules/elevate_community_override.md).

**Use manual analysis selectively** to trigger investigations only on alerts that warrant deeper review. See [Trigger a manual Elevate analysis](/xdr/features/modules/elevate_manual_analysis.md).

## Quota management for MSSPs

[PLACEHOLDER: Describe how MSSPs manage and distribute investigation quotas across sub-tenants. Include whether quotas are set per community or at the workspace level, and how overages are handled.]

## What happens when the quota is exhausted

When your monthly quota is reached:

- The agent stops analyzing new alerts automatically.
- Alerts that cannot be analyzed display the **AI limit reached** state in the **Verdict** column.
- Manual analysis via Roy is also blocked until the quota resets.

To resume analysis before the next billing cycle, contact your administrator to upgrade your plan.

[PLACEHOLDER: Confirm whether self-serve quota top-up is available and add the relevant steps if so.]

## Related links

- [Elevate](/xdr/features/modules/elevate_overview.md): Concept overview of how Elevate works and its key concepts.
- [Elevate analysis states](/xdr/features/modules/elevate_analysis_states.md): Reference table of all possible AI analysis states including AI limit reached.
- [Limit auto-analysis to specific rules](/xdr/features/modules/elevate_rule_filter.md): How to restrict which alerts Elevate analyzes to control quota usage.
- [Override Elevate settings for a community](/xdr/features/modules/elevate_community_override.md): How to disable Elevate for specific communities to reduce consumption.
