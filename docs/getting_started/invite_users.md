---
title: "Invite users"
description: "Add users to a Sekoia workspace or community by sending them an email invitation."
keywords: [invite, users, workspace, community, email, onboarding, admin, sso, okta]
audience: admin
module: all
type: task
---

# Invite users

To give a team member access to Sekoia, you send them an invitation from the workspace settings. They receive an email with a link to set their password and join the workspace or community. This article explains how to invite new users and how automatic user creation works with SSO.

## Before you begin

- You must have the **Admin** role to invite users.
- Decide which community the user should join and which role they should receive. See [Roles and permissions](/getting_started/roles_and_permissions) if you need help choosing.

## Invite a user by email

1. Navigate to **Settings > Workspace > Users**.
2. Click **Add new users**.
3. Enter the email addresses of the users you want to invite. Separate multiple addresses with a comma.
4. Select the communities you want to add the users to.
5. Assign a role for each community.
6. Click **Send invitation**.

Invited users receive a welcome email with a link to set their password. The link is valid for 24 hours.

!!! note "Existing Sekoia users"
    If an invited user already has a Sekoia account in another workspace, they do not receive a password setup email. They can access the new community immediately using their existing credentials.

!!! note "Multi-tenant workspaces"
    In a multi-tenant workspace, an invited user only has access to the specific communities you selected during invitation. They do not have access to the workspace as a whole or to other communities.

## Set up automatic user creation with SSO Okta

If your workspace uses SSO with Okta, you can configure Sekoia to automatically create a user account the first time someone from your organization logs in.

When automatic creation is enabled:

- A new user account is created on first login without requiring a manual invitation.
- You can set the default role assigned to automatically created users.

To configure this option, navigate to **Settings > Workspace > Security > SSO** and enable **Automatic user creation**.

See the SSO configuration guide for the full setup procedure.

## Related links

- [Manage users](/getting_started/manage_users) — How to edit roles, deactivate accounts, and remove users after they have been invited.
- [Roles and permissions](/getting_started/roles_and_permissions) — Overview of built-in and custom roles to help you choose the right access level.
- [Workspace setup overview](/getting_started/workspace_setup_overview) — Full admin checklist for configuring a workspace.
