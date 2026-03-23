# Feeds

A feed allows you to filter Cyber Threat Intelligence (CTI) objects from the Sekoia.io database to distribute them to external security tools or use them as dynamic filters within the platform. Feeds are shared across all users within the community that created them to ensure consistent intelligence scoping.

Feeds serve as versatile components for both internal analysis and external integration:

- **Filter reports and intelligence views:** You can use a feed as a filter on the **Reports** page to view only content matching specific criteria, such as industry sectors or geographic regions.

- **Scope intelligence database views**: To visualize the exact contents of a feed, navigate to the Intelligence Database, click Filters, select Feeds, and choose your specific feed.

- **Create detection rules**: Users with a Defend subscription can link a feed to a CTI detection rule to automatically match indicators of compromise (IOCs) against telemetry.

- **External dissemination:** You can share filtered data with firewalls, SIEMs, or TIPs using dedicated API or TAXII endpoints.

## Feeds listing

The **Feeds** page is accessible from the main menu. Each feed appears as a row with the following columns:

- **Name** – The title of the feed
- **Format** – The export format (JSON/STIX, Text, CSV, or Custom)
- **Created by** – The community that created the feed
- **Filters** – Active filters: object types, sources, TLPs, observables
- **Actions (⋯)** – **Disseminate**, **Edit**, **Duplicate**, or **Delete** *(unavailable on the Default Feed)*

## Default Feed

Every community with the Intelligence subscription has a **Default Feed** available out of the box — no setup required. It covers the **entire Sekoia CTI database** with no filters applied. It is always accessible and **cannot be deleted**.

Use the following Feed ID to access it programmatically: `textd6092c37-d8d7-45c3-8aff-c4dc26030608`

!!! tip
    Create additional feeds whenever you need a filtered, scoped view — for a specific TLP, source, or object type.

## Consume a feed

To integrate a feed with an external tool, you must retrieve its dissemination details.

1. Navigate to the **Feeds** page.
2. Locate the desired feed and click the **Actions (⋯)** icon.
3. Select **Disseminate**.

| Link | Use |
| --- | --- |
| **Public Feed ID** | Fetch or update the collection programmatically |
| **Public API URL** | Direct API calls and integrations (`https://app.sekoia.io/api/v2/inthreat/collections/...`) |
| **Public TAXII URL** | TAXII-compatible systems and platforms (`https://app.sekoia.io/api/v2/inthreat/taxii-server/...`) |

A single feed can be consumed simultaneously through all three links.

## Duplicate a feed

Duplicating a feed allows you to create a new version with similar filters without starting from scratch.
1. Navigate to the **Feeds **page.
2. Click the **Actions (⋯)** icon on the feed row.
3. Select **Duplicate**.

Sekoia.io creates an exact copy of the filters and settings. Each duplicate receives its own unique Feed ID and dissemination URLs.

---

## Create a feed

Create a feed to generate a filtered and scoped view of threat intelligence based on specific criteria like TLP, sources, or object types.

**Prerequisites**
    You must have the necessary permissions within your community to manage CTI configurations.

**Procedure**

1. Navigate to the **Feeds** page from the main menu.
2. Click **+ Feed** at the top right of the page.
3. In the **Define Your Feed** section, select the **Object Type **filters to include specific STIX objects.

    !!! note "Relationship handling"
        The feed only includes the selected object types; relationships between objects are excluded. If you leave this empty, all types are included.

4. Select the **Intelligence Sources** to scope the data.
5. Filter the output by selecting the allowed **TLP levels** (White, Green, Amber, Red).
6. Select whether to **Exclude indicators** that are expired or revoked.
7. Click Next.
8. In the Configure Dissemination Settings section, select the Sorting order.
   - **Newest to oldest:** Best for single-batch retrieval.
   - **Oldest to newest**: Required for paginated retrieval.
9. Select the output Format and configure its specific parameters.

??? example "Feed Format Specifications"
* JSON / STIX: Standard for CTI platforms. Max 10,000 objects per call.
* Text: One object per line, ideal for Firewall EDLs. Max 2,000 objects per call.
* CSV: Customizable spreadsheet format. Max 2,000 objects per call.
* Custom: User-defined template using variables like $tlp, $id, $name, and $observables. Max 2,000 objects per call.

10. Click Save.

The feed is now active and appears in the feed listing, ready for internal use or external dissemination.

## Edit a feed

Modify existing feed filters or dissemination formats to update the data flow to your connected tools.

1. Navigate to the **Feeds** page.
2. Locate the feed and click the **Actions (⋯)** icon.
3. Select **Edit**.
4. Update the filters or settings as required.
5. Click Save.

## Delete a feed

Remove a feed that is no longer required for your operations.

!!! warning "Permanent Action"
    Deleting a feed is irreversible. Any external tools relying on this Feed ID or URL will lose access to the data stream.

1. Navigate to the **Feeds** page.
2. Locate the feed and click the **Actions (⋯)** icon.
3. Select **Delete**.
4. **Confirm** the action in the modal.

# Create detection rules from a feed

Link a feed to a CTI detection rule to automatically monitor your environment for specific threats. This feature requires a Defend subscription.

1. Navigate to **Rules Catalog.**
2. Click to create a new CTI Rule.
3. In the source selection, choose **IOC Collections**.
4. Select your custom feed from the list.
5. Configure the rule logic and status.
6. Click **Save.**

The rule is now active and will check both incoming telemetry and historical events for matches against the feed indicators.


