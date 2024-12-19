# Implement a blocklist in Sekoia.io

While investigating an alert, an analyst can discover malicious IP addresses, domains, URLs or other kind of artifacts.
To contain the threat, the analyst might want to block the communications with these artifacts on the different network security solutions (firewalls, proxys, …) that are deployed in the information system. 

This article will show how a blocklist can be implemented in Sekoia.io to automate this task.

## How does it work?

The implementation of a blocklist in Sekoia.io is based on the [IOC Collections](../../../cti/features/consume/ioccollections.md) and consists of two parts:

- The first is to set up one or more playbooks to add the artifacts found in an alert to an IOC Collection.
- The second is to set up your networks security solutions to retrieve automatically and regularly the content of an IOC collection and block communications based on the retrieved content.

## Prerequisites

- A Sekoia.io XDR licence
- The user that configures the playbooks should have a Role that contains:
	* The SYMPHONY permissions
- An API Key with the **Analyst** role or a custom role that contains at least the following permission for the playbook:
	* View alerts
    * View intakes
    * View IOC collections
    * Manage IOC collections
- An API Key with the **Guest** role or a custom role that contains the following permission to authenticate the network security solutions:
    * View IOC collections

> To create your API Key, follow this [documentation](../../../getting_started/manage_api_keys.md).

## Create your IOC Collection

Our recommandation is to create a dedicated IOC Collection per artifact type (IP address, domain, URL...) to serve as a blocklist as it will be easier to maintain in time. You can follow this [documentation](../../../cti/features/consume/ioccollections.md) to create a new IOC Collection - no need to import data into it at this point.

Once the IOC Collection is created:
- Go back to the `IOC Collections` page
- Click on the three dots next to the newly created IOC Collection
- Select `Copy Feed ID` (Keep this value safe for later use)

## Create your playbook

Playbook templates were created to ease the process of setting up the playbooks to send the notifications to Slack or Teams. 

To create the playbook for your blocklist, follow these steps: 

- **Go to** the [Playbook page](https://app.sekoia.io/operations/playbooks)
- **Click** on `+ New Playbook`
- If multi-tenant is available, **select** the Community where the Playbook should be executed
- Choose the `Use a template` option 
- Search for `blocklist` or `IOC Collection` to filter the results
- Select one of the available templates and click on `Create`

![Examples of blocklist playbook templates](../../../assets/operation_center/playbooks/blocklist-templates.png)


## Configure your playbook

Once your playbook is created, the following configuration steps are required:

- Open each `Sekoia.io` action and select the account that needs to be used to communicate with Sekoia.io APIs. You may have to create an account with the API key you created previously if no account exists.
- Open the `Add IOC to IOC Collection` action and replace the ID of the IOC Collection with the `Feed ID` from the previous step. Optionnally, you can also specify the `valid_for` parameter with the number of days for which the indicator will be valid (only valid indicators will be retrieved by the network security solutions). Default validity values will be used otherwise (30 days for IP addresses, 6 months for domains and URLs). 
- Save the modifications and enable your playbook.

## Configure your network security solution

!!! warning
    The network security solution that will retrieve the IOC Collection content must be able to authenticate itself against Sekoia.io. 

The URL to use to retrieve the content of the IOC Collection is `https://app.sekoia.io/api/v2/inthreat/collections/YOUR-IOC-COLLECTION-FEED-ID/objects?format=text&limit=10000&skip_expired=true&include_revoked=false`. As specified in this URL, the maximum number of indicators that can be retrieved is limited to 10,000. Basic authentication mechanism is supported with `username` as user name and the **API Key as password**.

Please refer to your vendor documentation (see below for some references) for a more detailed step by step approach on configuring the network security solution.

## External vendor documentation

- [Palo Alto - External Dynamic List](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/policy/use-an-external-dynamic-list-in-policy/external-dynamic-list)
- [Checkpoint - Custom Intelligence Feed](https://support.checkpoint.com/results/sk/sk132193)
- [Fortinet - External Block List](https://docs.fortinet.com/document/fortigate/6.2.0/new-features/625349/external-block-list-threat-feed-policy)
