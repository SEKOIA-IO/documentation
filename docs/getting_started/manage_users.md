---
title: "Manage users"
description: "View, edit, deactivate, and remove user accounts in your Sekoia workspace."
keywords: [users, manage, deactivate, delete, roles, admin, workspace, account management]
audience: admin
module: all
type: task
---

# Manage users

After your team has been invited to Sekoia, you may need to update user roles, deactivate accounts for departing employees, or remove users from your workspace. All user management actions are available from the workspace settings.

## Before you begin

- You must have the **Admin** role to manage users.

## View the user list

1. Navigate to **Settings > Workspace > Users**.
2. Use the search bar to find a specific user by name or email.
3. Use the **Filter by Status** dropdown to filter by active or deactivated accounts.

The user list shows each user's name, email address, role, registration date, and authentication method.

## Edit a user's roles

To change the roles assigned to a user:

1. Navigate to **Settings > Workspace > Users**.
2. Click the user's name to open their detail page.
3. In the **Roles** section, click **Manage roles** to assign a new role.
4. Save your changes.

A user can hold multiple custom or one built-in roles simultaneously. Their effective permissions are the union of all assigned roles.

## Deactivate a user account

Deactivating an account suspends access without deleting the user's data. Use this when an employee leaves the organization or when you need to temporarily suspend access.

To deactivate an account, you have two options:

**From the user list:**

1. Locate the user in the **Settings > Workspace > Users** list.
2. Click **...** to the right of the user's name.
3. Select **Deactivate**.

**From the user detail page:**

1. Click the user's name to open their detail page.
2. Click **Deactivate account**.

Deactivated users appear in the user list with a **Deactivated** status. Filter by **Status > Deactivated** to list only inactive accounts.

## Reactivate a user account

!!! warning "Time-sensitive reactivation"
    After reactivation, the user must log in at least once before midnight on the same day. If they do not log in in time, their account is automatically deactivated again.

To reactivate a deactivated account:

1. Navigate to **Settings > Workspace > Users**.
2. Filter by **Status > Deactivated** to locate the account.
3. Click **...** to the right of the user's name.
4. Select **Reactivate** and confirm.

Notify the user immediately after reactivation so they can log in within the required window.

## Delete a user

Deleting a user permanently removes them from the community. This action cannot be undone.

!!! warning "Permanent action"
    Deleting a user removes all their community memberships and assigned roles. Consider deactivating instead if you may need to restore access later.

To delete a user:

1. Click the user's name to open their detail page.
2. Click **Delete from community**.
3. Confirm the deletion.

## Automatic deactivation for inactive accounts

To comply with PCI/DSS requirements, Sekoia can automatically deactivate accounts that have been inactive for 90 days.

To enable this setting:

1. Navigate to **Settings > Workspace > Security**.
2. Find the **Inactive accounts deactivation** section.
3. Enable the toggle and confirm.

## Related links

- [Invite users](/getting_started/invite_users.md) — How to add new users to a workspace or community.
- [Roles and permissions](/getting_started/roles_and_permissions.md) — Overview of role types and permission levels.
- [Secure your account](/getting_started/secure_your_account.md) — How to reset a user's two-factor authentication.
