# Case custom views

Case custom views are named, saved configurations of the cases listing page that store your filters, displayed columns and sort order. You open a view in one click instead of rebuilding the same filters at every session, and you can keep it private or share it with everyone in your community.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia.io plans to roll out this functionality to all environments soon.

## Why use custom views

Filters applied with the **Filters** button on the cases listing page are temporary. They are not kept from one session to the next and you cannot share them with your team, so every analyst rebuilds the same queues every day.

A custom view turns a filter combination into a permanent, named queue. Analysts start their shift on the right list of cases, and a SOC team triages from the same shared map during standups and handoffs.

## What a view contains

A view stores three settings of the cases listing page:

| Setting | Description |
|---|---|
| Filters | Any combination of the case filters, for example **Custom fields** is *Business Impact* and **Priority** is *Medium*. |
| Columns | The columns displayed in the table and their order, configured in **Show/hide table columns**. |
| Sort order | The order of the listing: **Last edition**, **Creation date** or **By highest priority**. |

## The views bar

Views appear as tabs in a bar above the cases list. The **All cases** tab shows every case without saved filters. Your private views and the views shared with your community follow it, in the order you set. The **+ New view** button at the end of the bar creates a new view.

Selecting a view applies its filters, columns and sort order immediately. When you change any of these settings on an open view, **Reset** and a save button appear so you can discard or keep your changes. The save button reads **Save** on a private view and **Save for everyone** on a shared view.

![Cases listing page with the views bar showing All cases, the private view My cases, the shared views Open and New Today, and the New view button](/assets/operation_center/cases/case-custom-views-bar.png){: style="max-width:100%"}

## Visibility

Each view has one of two visibility settings, chosen when you create it and editable later.

| Visibility | Icon | Who sees the view |
|---|---|---|
| Private | Lock | Only you. |
| Share to the community | People | Every user of the community with the permission to view case custom views. |

!!! warning "Shared views update for everyone"
    Saving changes to a shared view updates it immediately for every user of the community who has access to it.

## Limits

| View type | Limit |
|---|---|
| Shared views | 20 per community |
| Private views | 10 per user |

## Views in multi-tenant mode

In multi-tenant mode, views are scoped to the level where you create them. A view created at the workspace level is not shared with sub-communities, and each community keeps its own set of views. To give analysts of several communities the same queue, create the view in each community.

## Permissions

Two permissions of the **Cases** group control access to custom views. Grant them through a custom role.

| Permission | Description |
|---|---|
| View case custom views | List and view case custom views. |
| Manage case custom views | Create, update and delete case custom views. |

## Use cases

* **Personal queue**: a private **My cases** view filtered on your assignments, sorted by highest priority.
* **Team triage queue**: a shared **L1 queue** or **High priority** view so every analyst of the squad works from the same list.
* **SLA follow-up**: a shared **SLA breached** view reviewed during the daily standup.
* **Business context**: a shared view filtered on a custom field such as **Business impact**, with the custom fields column displayed.

## Related articles

* [Manage case custom views](/xdr/features/investigate/manage_case_custom_views.md): How to create, save, edit, duplicate, delete and reorder views.
* [Manage cases](/xdr/features/investigate/manage_cases.md): How to filter, sort and perform bulk actions on cases from the listing page.
* [Cases](/xdr/features/investigate/cases.md): Overview of what cases are and how they are structured.
* [Custom fields](/xdr/features/investigate/custom_fields.md): How to extend alerts and cases with structured, typed metadata fields.
* [Roles and permissions](/getting_started/roles_and_permissions.md): How built-in and custom roles grant access to platform features.
* [Workspace and communities](/getting_started/workspace_and_communities.md): How workspaces and communities are organized in multi-tenant mode.
