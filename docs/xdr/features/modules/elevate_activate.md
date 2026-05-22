# Activate Elevate on a workspace

This article explains how to enable the Elevate investigation agent on your workspace so it automatically analyzes all incoming alerts.

## Prerequisites

- Your Sekoia plan includes the Elevate add-on. To verify, navigate to **Settings > Subscriptions** and confirm that an Elevate entry appears alongside your current plan.
- You have administrator-level access to the workspace.

## Activate the agent

The Elevate investigation agent is available as soon as the Elevate add-on is enabled on your workspace. The agent is disabled by default so you control when quota consumption begins.

!!! warning "Quota consumption starts immediately"
    Enabling the agent triggers analysis of all new incoming alerts across all communities in the workspace. Each analysis consumes one unit of your monthly investigation quota. Review your quota allocation before activating.

To activate the agent:

1. Navigate to **Settings > AI agent**.
2. Select **Investigation agent** under the **Workspace** section.
3. Toggle **Auto-analyze alerts** to enabled.

> 📸 [SCREENSHOT SUGGESTION: Settings > AI agent panel showing the Investigation agent section with the Auto-analyze alerts toggle switched to the enabled position. | ALT TEXT: AI agent settings panel with the Auto-analyze alerts toggle enabled.]

Once enabled, the agent analyzes every new alert that arrives across all communities in the workspace.

## Add agent instructions

The **Instructions** field lets you provide contextual guidance the agent takes into account when analyzing alerts. Use it to describe environment-specific context, known legitimate behaviors, or investigation priorities specific to your organization.

[PLACEHOLDER: Confirm field format, character limit, and add 1-2 examples of effective instructions.]

## Result

New incoming alerts are automatically analyzed by the Elevate agent. The **Verdict** column in the alert list updates as each investigation completes.

## Related links

- [Limit auto-analysis to specific rules](/xdr/features/modules/elevate_rule_filter.md): How to restrict which alerts Elevate analyzes to control quota usage.
- [Override Elevate settings for a community](/xdr/features/modules/elevate_community_override.md): How to enable or disable Elevate independently for a specific community.
- [Manage your Elevate investigation quota](/xdr/features/modules/elevate_quota.md): How to monitor and optimize your monthly investigation quota.
