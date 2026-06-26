---
title: "Workspace and communities"
description: "A workspace is your organization's top-level Sekoia environment. Communities are subdivisions within a workspace that allow separate configurations for different teams or clients."
keywords: [workspace, community, multi-tenant, single-tenant, mssp, organization, hierarchy, environment]
audience: all
module: all
type: concept
---

# Workspace and communities

A workspace is the top-level environment in Sekoia that contains all your organization's data, users, and configurations. Communities are subdivisions within a workspace that allow different teams or client organizations to operate with their own settings and data.

Understanding the relationship between workspaces and communities helps you know where to configure things and how to navigate between environments.

## Workspace

A workspace is your organization's dedicated Sekoia environment. It is the root container for all communities, users, and global settings.

At the workspace level, you manage:

- User access and authentication (SSO, security policies)
- Subscription and licensing
- Workspace-wide roles and permissions
- Community creation and structure

You access your workspace by logging into Sekoia. If your account belongs to multiple workspaces (for example, if you work with several organizations), you can switch between them from the navigation menu.

## Community

A community is an operational subdivision within a workspace. Communities let you separate detection data, intakes, alerts, playbooks, and configurations between different organizational units, clients, or environments.

A community can:

- Run independently with its own intakes, rules, and alerts
- Inherit configuration from the parent workspace
- Have its own users with community-specific role assignments

Most day-to-day security operations in Sekoia happen at the community level. When you create an alert filter, activate a detection rule, or configure an intake, you do it within a community.

## Single-tenant vs multi-tenant mode

The way you use communities depends on your organization's structure.

| Mode | Structure | Typical use case |
|---|---|---|
| **Single-tenant** | One workspace with one community | Direct customers running their own security operations |
| **Multi-tenant** | One workspace with multiple communities | MSSPs managing several client environments from a single pane of glass |

In single-tenant mode, the workspace and the community effectively represent the same environment. The distinction is administrative.

In multi-tenant mode, each community represents a separate client or business unit. Workspace administrators can view and manage all communities from a centralized panel, including subscriptions, user access, and alert volumes.

!!! note "Community switcher"
    In multi-tenant workspaces, a **Communities** button appears in the breadcrumb at the top of the page. Use it to switch between communities or select multiple communities to display aggregated data across all of them.

## What you configure at each level

| Level | Examples of what you configure |
|---|---|
| **Workspace** | SSO provider, workspace security policies, inactive account rules, subscription management |
| **Community** | Intakes, detection rules, alerts, playbooks, notifications, API keys, entities |

If you are not sure whether a setting belongs to the workspace or the community, check the **Settings** menu. Workspace-level settings appear under a **Workspace** section, and community-level settings appear under the community name.

> 📸 [SCREENSHOT SUGGESTION: The Settings page showing the Workspace and Community sections side by side in the left navigation. | ALT TEXT: Settings navigation showing workspace and community configuration sections.]

## Switching between workspaces and communities

To switch to a different workspace, click your current workspace name at the top of the navigation menu and select another workspace from the dropdown.

To switch to a different community in a multi-tenant workspace, click the **Communities** button in the breadcrumb and select the community you want to access.

## Related links

- [Navigate the platform](/getting_started/navigate_the_platform) — How to use the Sekoia interface, including the workspace and community switcher.
- [Workspace setup overview](/getting_started/workspace_setup_overview) — Step-by-step guide for administrators to configure a new workspace.
- [Roles and permissions](/getting_started/roles_and_permissions) — How access is controlled at the workspace and community level.
- [Invite users](/getting_started/invite_users) — How to add users to a workspace or community.
