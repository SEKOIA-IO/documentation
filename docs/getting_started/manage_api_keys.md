---
title: "Manage API keys"
description: "Create, configure, and revoke API keys to enable programmatic access and integrations in Sekoia."
keywords: [api key, authentication, integration, permissions, revoke, expire, automation, playbook, cti]
audience: admin
module: all
type: task
---

# Manage API keys

API keys provide programmatic access to Sekoia without requiring a user session. They are used to connect external tools, run automated integrations, and execute playbook actions that interact with the platform or third-party services. This article explains when to use API keys and how to create, configure, and revoke them.

## When you need an API key

API keys are required for:

- Connecting external tools to the Sekoia API (SIEM, ticketing systems, SOAR platforms)
- Playbooks that call Sekoia's API as part of their action chain
- CTI interconnection with third-party threat intelligence platforms
- Automated scripts or pipelines that query the platform

!!! note "Permissions-based, not role-based"
    Sekoia API keys are permissions-based. When you create a key, you select exactly which permissions it carries, independent of any user role. Always apply the principle of least privilege: grant only the permissions the integration actually needs.

## Create an API key

Only users with the Admin role can create API keys.

1. Navigate to **Settings > Workspace > API Keys**.
2. Click **+ API key**.
3. Enter a descriptive name for the key (for example, `VirusTotal enrichment - Playbooks`).
4. Enter a description of at least 10 characters explaining what the key is used for.
5. Set an expiration date: 30 days, 180 days, 365 days, a custom duration up to one year, or no expiration.
6. Select the permissions the key requires.
7. Click **Save**.

!!! warning "Copy the key immediately"
    The API key is displayed only once, immediately after creation. Copy it and store it in a secure vault before closing the window. Sekoia cannot display the key value again after you navigate away.

The maximum length of an API key is 100 characters.

## View and filter your API keys

To view the list of API keys for your community, navigate to **Settings > Workspace > API Keys**.

You can filter keys by status:

| Status | Meaning |
|---|---|
| **Active** | The key is valid and can be used |
| **Revoked** | The key has been manually revoked and can no longer be used |
| **Expired** | The key reached its expiration date and can no longer be used |

Keys are listed by creation date, most recent first.

## Revoke an API key

Revoking a key permanently disables it. This action cannot be undone.

!!! warning "Irreversible action"
    Revoking an API key immediately breaks any integration or automation that relies on it. Before revoking, confirm that the key is no longer in use or that a replacement key has been deployed.

To revoke an API key:

1. Navigate to **Settings > Workspace > API Keys**.
2. Click **Edit** next to the key you want to revoke.
3. Click **Revoke**.
4. Confirm the action.

## Best practices

- Give each key a clear, descriptive name that identifies its purpose and the system it connects.
- Set expiration dates on all keys used for integrations. Rotate keys regularly.
- Store all API keys in a secrets management vault, never in plain text files or source code.
- Revoke keys immediately when an integration is decommissioned or a team member with key access leaves.

## Related links

- [Workspace setup overview](/getting_started/workspace_setup_overview) — Full admin checklist for configuring your workspace.
- [Roles and permissions](/getting_started/roles_and_permissions) — How user roles differ from API key permissions.
