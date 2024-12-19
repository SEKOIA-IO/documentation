# Shodan and VirusTotal configuration

This use case describes how to activate Shodan playbook if an alert is coming from VirusTotal

There are 2 steps:
1- How to create a Shodan playbook
2- Combine Shodan playbook into VirusTotal

## Prerequisites

- A Sekoia.io XDR licence
- The user that configures the Playbook should have a Role that contains:
	* The SYMPHONY permissions
- An API Key with a Role that contains at least the following permission:
	* View alerts
	* View anomaly stats
	* View anomaly dataset
	* View event stats in asset listing

> To create your API Key, follow this [documentation](../../../getting_started/manage_api_keys.md).

## Playbook configuration

### Create a comment on Sekoia.io alert from Shodan

1. Configure the `Alert Created` block

  - On the right panel, under the Module Configuration section, click on `+ Create new configuration`
  - Complete the form with the following information:
    * **Name**: ReadAlertContent
    * **Api_key**: TO BE REPLACED BY YOUR Sekoia.io API KEY
    * **Base_url**: `https://api.sekoia.io`
  - Click on the `Save` button

2. Configure the `Get Events` block

  - On the left panel, **search for** the `Get Events` block
  - **Drag and drop** it underneath the `Alert Created` block

  Copy data from previous block
  - On the right panel, select the **ReadAlertContent** configuration previously created
  - Select the `Alert Created` block and copy values in the following fields with **copy** icon on the right
    - **earliest_time** = copy and pasting value of `first_seen_at`
    - **latest_time** = copy and pasting value of `last_seen_at`
    - **query** = copy value and pasting of `short_id` and pre-filling `alert_short_ids:"`<replace by short_id>`"`
  - Link the blocks `Get Alert` to `Get Events`

3. Configure the `Get host` Shodan block

  - On the left panel, **search for** the `Get host` block
  - **Drag and drop** it underneath the `Get Events` block
  - On the right panel, **complete the form** with the following information:
    - **ip** = `{{node.x.['events'][0]['destination.ip']}}`   replace x by the node of `Get Events` (in code tab, search `Get Events` and you will find the node number to be used)
  - Link the blocks `Foreach` to `Get host`  

4. Configure the `Comment alert` block

  - On the left panel, **search for** the `Comment alert` block
  - **Drag and drop** it underneath the `Get host` Shodan block
  - On the right panel, **complete the form** with the following information:
    - **content** = `{{node.x['data'][0]['location']['city']}}`   replace x by the node of `Get host` (in code tab, search `Get host` and you will find the node number to be used)
    - **uuid** = copy value and pasting of `short_id` (found in `Alert Created` block)
  - Link the blocks `Get host` to `Comment alert`  

Your playbook should look like the following:

![Playbook Shodan-SIO Use Case](/assets/playbooks/library/UseCases/Shodan_VT_1.png)

### Enrich Shodan with VirusTotal template

  1. Use **Enhance network alerts with VirusTotal** template
  2. Change part of the playbook and add the Shodan part (to enrich Lookup IPs)
  - **Lookup** (Shodan) = add form and fill hostname (copy `Url` of `Scan Url` block)
  - **Comment Alert** :
    - content = copy `type` of `Lookup` block
    - uuid = copy `uuid` of `Comment : Domain enrich by VT` block  	

Your playbook should look like the following:

![Playbook Shodan-VT Use Case](/assets/playbooks/library/UseCases/Shodan_VT_2.png)
