---
title: "Roles and permissions"
description: "Roles in Sekoia control what each user can see and do within a workspace or community. This article explains the built-in roles, custom roles, and restricted roles available to administrators."
keywords: [roles, permissions, analyst, admin, guest, custom role, restricted role, access control, user management]
audience: admin
module: all
type: concept
---

# Roles and permissions

Roles in Sekoia control what each user can see and do within a workspace or community. Every user is assigned at least one role, which determines their access to pages, features, and data. This article explains the available role types and when to use each one.

## Built-in roles

Every Sekoia community includes three built-in roles that cover the most common access patterns. Built-in roles cannot be modified.

| Role | Access level | Typical users |
|---|---|---|
| **Guest** | Read-only access to platform data | External stakeholders, auditors, clients who need visibility but not interaction |
| **Analyst** | Read and write access for security operations | SOC analysts, threat intelligence analysts, security engineers |
| **Admin** | Full access including community management, user administration, and configuration | Security managers, platform administrators, MSSP operators |

### What the Admin role can do

The Admin role includes all Analyst permissions plus:

- Invite and remove users
- Assign and modify roles
- Create and revoke API keys
- Manage subscriptions and community settings
- Reset user 2FA
- Configure SSO and workspace security policies

!!! tip "Least privilege principle"
    Assign users the lowest role that allows them to do their job. Grant Admin access only to users who actively need to manage the workspace or community.

## Custom roles

If the built-in roles do not match your team's access requirements, administrators can create custom roles with a specific set of permissions.

Custom roles are useful when you need:

- A role with analyst-level access but without the ability to modify detection rules
- A role restricted to viewing alerts and cases but not playbooks
- A role for an external API integration with narrowly scoped permissions

To create a custom role, navigate to **Settings > Workspace > Roles** and click the **+ Role** button.

You can discover all available permissions from the same page. Permissions are grouped by feature area (Alerts, Rules, Playbooks, Users, etc.).

## Restricted roles

Restricted roles limit a user's access to events from specific intakes. They are useful for organizations that need to keep certain data streams visible only to authorized users.

For example, you can create a restricted role that allows an analyst to see events and alerts only from a specific endpoint intake, preventing them from accessing logs from other sources.

To create a restricted role, navigate to **Settings > Workspace > Roles** and select the **Restricted** option when creating a new role.

## Intake-restricted roles

Intake-restricted roles are a variant of restricted roles with a more limited permission set. They are designed for scenarios where a user or external system needs read-only access scoped to one or more specific data sources.

## Assigning roles to users

Roles are assigned when you invite a user or from the user detail page.

To change a user's role after they have been invited:

1. Navigate to **Settings > Workspace > Users**.
2. Click the user's name.
3. In the **Roles** section, add or remove roles as needed.
4. Save your changes.

A user can hold multiple roles simultaneously. Their effective permissions are the union of all assigned roles.

??? note "Legacy role names (pre-2024 API reference)"
    If you use the Sekoia API directly or maintain older scripts, you may encounter these internal role identifiers. They correspond to the current role system as follows.

    | Legacy name | Description |
    |---|---|
    | `admin` | Community administrator |
    | `symphony_operator` | Playbook usage |
    | `ic_viewer` | Intelligence read-only |
    | `oc_viewer` | View operation center data (read-only) |
    | `oc_contributor` | View and comment on alerts |
    | `oc_operator` | Manage alerts and incidents |
    | `oc_administrator` | Manage rules, templates, entities, countermeasures |
    | `manage_api_keys` | Manage API keys of the community |
    | `manage_community` | Any action on community settings |
    | `manage_roles` | Create, update, delete, and assign roles |
    | `manage_members` | Add and remove users from the community |

    You can view all current permissions directly in the platform under **Settings > Workspace Roles**.


## Related links

- [Invite users](/getting_started/invite_users.md) — How to add users and assign roles during the invitation process.
- [Manage users](/getting_started/manage_users.md) — How to view and modify user access after onboarding.
- [Workspace setup overview](/getting_started/workspace_setup_overview.md) — Full checklist for configuring your workspace.
