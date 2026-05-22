# Limit auto-analysis to specific rules

By default, when auto-analysis is enabled, the Elevate agent analyzes every incoming alert regardless of the detection rule that triggered it. This article explains how to restrict analysis to a specific set of rules to focus your quota where it adds the most value.

## Prerequisites

- Elevate is activated on your workspace. See [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md).
- You have administrator-level access to the workspace.

## When to use rule filtering

Rule filtering is useful when you already have playbooks reliably handling certain alert types and want to reserve your Elevate quota for detections where AI investigation adds the most value, such as high-volume, complex, or time-consuming alert categories.

!!! note "Default behavior"
    When no rules are selected in the filter, the agent analyzes all incoming alerts. Selecting one or more rules restricts analysis exclusively to alerts triggered by those rules.

## Configure the rule filter

1. Navigate to **Settings > AI agent**.
2. Select **Investigation agent** under the **Workspace** section.
3. Enable **Limit auto-analyze to specific rules**.
4. Use the search bar to find the rules you want to include.
5. Select each rule you want the agent to analyze.

> 📸 [SCREENSHOT SUGGESTION: AI agent settings panel with the "Limit auto-analyze to specific rules" option expanded, showing a search bar and a selectable list of detection rules. | ALT TEXT: Rule filter configuration panel showing a list of detection rules that can be selected for Elevate auto-analysis.]

## Result

The agent analyzes only alerts triggered by the rules you selected. Alerts from all other rules are not processed automatically. You can still trigger a manual analysis on any alert at any time.

## Related links

- [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md): How to enable the Elevate agent on your workspace.
- [Trigger a manual Elevate analysis](/xdr/features/modules/elevate_manual_analysis.md): How to analyze an alert that was excluded by the rule filter.
- [Manage your Elevate investigation quota](/xdr/features/modules/elevate_quota.md): How to monitor and optimize your monthly investigation quota.
