# Override Elevate settings for a community

When Elevate is activated at the workspace level, all communities inherit that configuration by default. This article explains how to override the agent settings for a specific community to enable or disable Elevate independently.

## Prerequisites

- Elevate is activated on your workspace. See [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md).
- You have administrator-level access to the workspace.

## Override the configuration for a community

1. Navigate to **Settings > AI agent**.
2. Select the community you want to configure from the community list.
3. Select **Override**.
4. Toggle **Auto-analyze alerts** to the desired state for this community.

> 📸 [SCREENSHOT SUGGESTION: AI agent settings panel for a specific community, showing the Override button and the Auto-analyze alerts toggle in a custom state with an indicator confirming that the community uses its own settings. | ALT TEXT: Community-level AI agent settings with the Override option active and a custom auto-analyze toggle state.]

An indicator confirms that this community now uses its own settings and no longer inherits the workspace-level configuration.

!!! note "Understanding the inherited state"
    Before you select **Override**, the toggle reflects the workspace-level setting. It does not represent a choice made at the community level. Select **Override** to manage this community independently.

## Result

The community uses its own Elevate configuration independently of the workspace setting. Other communities are not affected.

To revert to the workspace configuration, return to the community's AI agent settings and remove the override.

## Related links

- [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md): How to enable the Elevate agent at the workspace level.
- [Limit auto-analysis to specific rules](/xdr/features/modules/elevate_rule_filter.md): How to restrict which alerts Elevate analyzes within a workspace or community.
- [Manage your Elevate investigation quota](/xdr/features/modules/elevate_quota.md): How to monitor and optimize your monthly investigation quota.
