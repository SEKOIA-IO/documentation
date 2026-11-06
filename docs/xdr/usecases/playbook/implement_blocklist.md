# Implement a blocklist in Sekoia

Use an IOC Collection as a blocklist to share IP addresses, domains, URLs, or other observable values with a firewall or proxy. You can populate the collection through the interface, import a file, or automate updates with a playbook.

## How blocklists work

1. Add the indicators you want to block to an IOC Collection.
2. Configure your firewall or proxy to retrieve the collection regularly through the API.
3. The equipment uses the retrieved values according to its blocking policy.

Sekoia provides the list; the receiving equipment enforces the blocking policy.

## Create your blocklist

You need a Sekoia Defend or Sekoia Intelligence subscription with access to IOC Collections, and permissions to **View IOC collections** and **Manage IOC collections** in the community where you create the blocklist.

1. [Create an IOC Collection](/cti/features/consume/ioccollections.md#create-an-ioc-collection).
2. Return to the **IOC Collections** page.
3. Click the three dots next to the collection and select **Copy Feed ID**. You will use this ID in the equipment's retrieval URL.

Use a dedicated collection per observable type, such as IP addresses, domains, or URLs, when the equipment expects separate lists for each type.

## Add indicators to your blocklist

Add indicators through the interface using one of these methods:

- **Text import**: enter a list of observable values through the interface.
- **File import**: upload a CSV, XLS, or XLSX file and map its columns to indicator properties.

For each indicator, set a **Description** to explain the blocking reason and review its **Valid From** and **Valid Until** dates. With text import, the properties you enter apply to all imported values. File import can provide a different description for each indicator.

Follow [Import IOCs inside a collection](/cti/features/consume/ioccollections.md#import-iocs-inside-a-collection) for detailed instructions.

## Connect your firewall or proxy

### Prerequisites

- The equipment must be able to reach the Sekoia API over HTTPS, authenticate, and periodically refresh an external list.
- [Create an API key](/getting_started/manage_api_keys.md) for the equipment with the **View IOC collections** permission in the collection's community. The **Guest** role or a custom role containing that permission can be used.
- Check which observable types and text formats the equipment supports.

Basic authentication is supported: use `username` as the username and the **API key as the password**. Configure these credentials in the equipment's authentication settings.

### Choose your regional API URL

Use the API base URL for the region where your community is hosted. See [Find your base URL](/developer/quickstart.md#step-1-find-your-base-url) for the full regional table and how to identify your region.

In the examples below, replace `BASE_URL` with that regional API base URL, without a trailing slash. For example:

- **FRA1**: replace `BASE_URL` with `https://api.sekoia.io`.
- **FRA2**: replace `BASE_URL` with `https://app.fra2.sekoia.io/api`.

Keep the `/v2/inthreat/...` path and query parameters after the base URL. For other regions, use the corresponding value from the same table.

### Export observable values only

Replace `YOUR-IOC-COLLECTION-FEED-ID` with the copied Feed ID:

```text
BASE_URL/v2/inthreat/collections/YOUR-IOC-COLLECTION-FEED-ID/objects?format=text&limit=10000&skip_expired=true&include_revoked=false
```

This format returns observable values on separate lines.

### Include the blocking reason

If the equipment supports inline comments in the `observable # comment` format, use the custom template `$observables # $description`:

```text
BASE_URL/v2/inthreat/collections/YOUR-IOC-COLLECTION-FEED-ID/objects?format=custom&template=%24observables%20%23%20%24description&limit=10000&skip_expired=true&include_revoked=false
```

Example response:

```text
192.0.2.10 # Indicator added after investigating a phishing alert
192.0.2.11 #
```

The comment comes from the **indicator's description**. Missing descriptions produce an empty comment, and description line breaks are replaced with spaces. This template does not populate descriptions automatically.

Check your equipment's support for inline comments and how it displays them before choosing this format. Custom exports group multiple observable values from the same indicator on one line, separated by commas; the receiving equipment must accept that structure. See [Custom export templates](/cti/features/consume/ioccollections.md#export-an-ioc-collection-with-a-custom-format) for details.

### Filters, limits, and refresh

Both examples use `skip_expired=true` and `include_revoked=false` to exclude expired and revoked indicators. Keep these filters when customizing the URL.

The examples request up to **10,000 indicators per call**. Collections can contain more, but an equipment integration using a single request must not assume it receives the full collection beyond that limit. For larger collections, use a client that supports API pagination or split the blocklist into collections that the equipment can consume completely.

Configure the refresh interval and blocking policy according to your equipment's capabilities.

### Vendor configuration guides

Use your vendor's instructions to configure retrieval, authentication, and policy enforcement:

- [Palo Alto — External Dynamic List](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/policy/use-an-external-dynamic-list-in-policy/external-dynamic-list)
- [Check Point — Custom Intelligence Feed](https://support.checkpoint.com/results/sk/sk132193)
- [Fortinet — External Block List](https://docs.fortinet.com/document/fortigate/6.2.0/new-features/625349/external-block-list-threat-feed-policy)

## Verify the integration

1. Add a test indicator and a description to the collection. Use an observable you control, or a documentation-only value such as `192.0.2.10`.
2. Retrieve the configured URL with the equipment's API key. Check that the expected value is present and, for custom exports, that its description appears.
3. Trigger or wait for a refresh on the equipment. Verify that retrieval succeeds and the list is available to the intended policy.
4. Revoke the test indicator and refresh again. Verify that it disappears from the API response and the equipment's list.

## Maintain your blocklist

Add indicators through the interface or file import as needed. You can [edit an indicator](/cti/features/consume/ioccollections.md#edit-an-indicator) to update its description or validity dates, or [revoke it](/cti/features/consume/ioccollections.md#revoke-an-indicator) when it should no longer be blocked.

With the filters above, expired and revoked indicators are excluded from subsequent responses. Changes take effect on the equipment after a successful refresh, according to its policy and caching behavior.

## Automate blocklist updates with a playbook (optional)

Once the blocklist works with manual updates, you can use a playbook to add artifacts found in alerts automatically.

### Playbook prerequisites

- A **Sekoia Defend** subscription is required for playbook automation.
- The user configuring the playbook needs the **SYMPHONY** permissions.
- The playbook needs an API key with the **Analyst** role or a custom role containing the permissions required by the selected template: **View alerts**, **View intakes**, **View IOC collections**, **Manage IOC collections**, **View observables**, and **View intelligence**.

These permissions are for the playbook's account. The equipment only needs the consultation permission described in [Connect your firewall or proxy](#connect-your-firewall-or-proxy).

### Create your playbook

1. Go to the **Playbooks** page in your regional Sekoia application and click **+ New Playbook**.
2. If multi-tenant is available, select the community where the playbook should run.
3. Choose **Use a template** and search for `blocklist` or `IOC Collection`.
4. Select a template and click **Create**.

![Examples of blocklist playbook templates](/assets/operation_center/playbooks/blocklist-templates.png)

### Configure your playbook

1. Open each **Sekoia** action and select the account used to call the APIs. Create an account with the playbook's API key if needed.
2. In **Add IOC to IOC Collection**, set the collection ID to the **Feed ID** copied earlier.
3. Optionally, set `valid_for` to the validity period in days. Otherwise, the action uses its defaults: 30 days for IP addresses and 6 months for domains and URLs.
4. Save the changes and enable the playbook.
5. Verify that a playbook execution adds the expected indicator to the collection and that the equipment retrieves it on refresh.

The custom export reads descriptions already stored on indicators. Do not assume that the selected action or template fills the description with alert context; check its available inputs and the resulting indicator. You can add or edit the description through the interface.
