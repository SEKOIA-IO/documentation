---
title: "Navigate the platform"
description: "Learn how to use the Sekoia interface: the main navigation menu, workspace and community switching, filters, and menu personalization."
keywords: [navigation, interface, menu, filters, workspace, community, personalize, favorites, keyboard shortcut]
audience: all
module: all
type: task
---

# Navigate the platform

Sekoia's interface is built around a persistent left-hand navigation menu that gives you access to all features within your current workspace and community. This article explains how to move around the platform, switch between environments, and apply filters.

## The navigation menu

The left-hand menu is organized into three collapsible sections, plus fixed items at the top and bottom. The items available to you depend on your subscription and assigned role.

**Top area**

| Item | What it does |
|---|---|
| **Community name** | Shows your active community. Click to switch communities (multi-tenant only). |
| **Search for IOCs** | Search the Intelligence database for observables and indicators. |
| **Ask Roy** | Open the Roy AI assistant panel. |
| **Notifications** | Access your personal notification history. |
| **Homepage** | The platform home page with summary widgets. |
| **Tasks** | Your assigned investigation tasks. |
| **Dashboards** | Preconfigured and custom security dashboards. |
| **Threat Landscape** | Overview of the threat landscape relevant to your organization. |

**Investigate section**

| Item | What you find there |
|---|---|
| **Cases** | Security cases grouping related alerts and investigations |
| **Events** | Full event history from all connected data sources |
| **Notebooks** | Collaborative investigation notebooks |
| **Alerts** | Active security alerts raised by detection rules |
| **Queries** | Saved and ad-hoc event queries |

**Observe section**

| Item | What you find there |
|---|---|
| **Intelligence** | Threat intelligence database (threat actors, malware, campaigns, indicators) |
| **Feeds** | Custom CTI feeds filtered by sector, geography, or threat type |
| **Reports** | FLINT threat reports and analytical content |
| **IoC Collections** | Curated indicator collections for detection |
| **Graph Explorations** | Visual relationship maps between threat objects |

**Configure section**

| Item | What you find there |
|---|---|
| **Rules Catalog** | Detection rules mapped to the MITRE ATT&CK framework |
| **Intakes** | Data source connectors for log ingestion |
| **Entities** | Logical groupings of assets for scoping detection |
| **Assets** | Inventory of discovered assets in your environment |
| **Playbooks** | Automation workflows for alert enrichment and response |
| **Integrations** | Installed integration connectors and their status |

**Bottom area**

| Item | What it does |
|---|---|
| **Your name** | Access your profile, security settings, and display preferences. |
| **Settings** | Workspace and community configuration (admin). |
| **Early features** | Preview features not yet in general availability. |
| **Help & support** | Documentation, Academy, and support portal. |

> 📸 [SCREENSHOT SUGGESTION: The full left-hand navigation menu in an active Sekoia session, showing the Investigate, Observe, and Configure collapsible sections. | ALT TEXT: Sekoia left-hand navigation menu with collapsible sections Investigate, Observe, and Configure, plus fixed items at the top and bottom.]

## Switch between workspaces and communities

### Switch workspace

To move to a different workspace:

1. Click your current workspace name at the top of the navigation menu.
2. Select the workspace you want to access from the dropdown list.

### Switch community

To filter on a specific community in a multi-tenant workspace:

1. Click the **Communities** button in the breadcrumb at the top of the page.
2. Select one or more communities from the list to display their data.

!!! note "Single-tenant workspaces"
    The **Communities** button only appears in multi-tenant workspaces. In single-tenant mode, your workspace contains one community and no switcher is displayed.

## Use filters

Most data pages, including **Alerts**, **Rules Catalog**, **Intakes**, **Playbooks**, and **Intelligence**, include a filter panel. Use it to narrow down results based on multiple criteria.

To open the filter panel:

- Click the **Filters** button on the page, or
- Press **F** on your keyboard from any of these pages.

Once the filter panel is open:

- Select a filter category and choose one or more values.
- Apply multiple filters at the same time. The default operator between filters is AND.
- Change the operator (is / is not / is any of) by clicking on it in the active filter tag.
- Remove a single filter by clicking the cross next to its tag.
- Remove all filters by clicking **Clear filters**.

!!! tip "Keyboard navigation in filters"
    Use the **Up** and **Down** arrow keys to navigate filter options, **Enter** to select a value, and **Esc** to close the panel.

## Personalize your menu

You can pin pages to favorites and reorder navigation sections to match your daily workflow.

See [Customize your interface](/getting_started/customize_your_interface.md) for the step-by-step procedures.

## Related links

- [Workspace and communities](/getting_started/workspace_and_communities.md): Explanation of the workspace and community structure and what each level controls.
- [Customize your interface](/getting_started/customize_your_interface.md): Add pages to favorites, reorder menu sections, and configure table columns.
