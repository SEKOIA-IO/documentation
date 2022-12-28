# Shodan and VirusTotal configuration

This use case describes how to activate Shodan playbook if an alert is coming from VirusTotal
There are 2 steps:
1- How to create a Shodan playbook
2- Combine Shodan playbook into VirusTotal

## Prerequisites

- A SEKOIA.IO XDR licence
- The user that configures the Playbook should have a Role that contains:
	* The SYMPHONY permissions
- An API Key with a Role that contains at least the following permission:
	* SIC_READ_ALERTS
	* EVENTS_READ_STATS
	* EVENTS_READ_DATASETS
	* SIC_READ_EVENT_STATS

> To create your API Key, follow this [documentation](../../../getting_started/generate_api_keys.md).

