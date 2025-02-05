uuid: 5fdf8838-1529-4243-8fbc-e6bfa7b52e30
name: STIX
type: playbook

# STIX

![STIX](/assets/playbooks/library/stix.png){ align=right width=150 }

[STIX](https://oasis-open.github.io/cti-documentation/) is a cybersecurity serialization format used to represent cyber threat intelligence, directed by the [OASIS Cyber Threat Intelligence Technical Committee](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti). It peered with TAXII, a protocol used to exchange cyber threat intelligence (CTI) over HTTPS

## Configuration

This module accepts no configuration.

## Triggers

### fetch_taxii2_collection

Fetch objects from a TAXII 2 Server

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sleep_time` | `integer` | Time in seconds the worker sleeps between the checks of new events |
| `collection_url` | `string` | URL of the TAXII Collection |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | Bundle of STIX objects fetched from the collection |

## Actions

### Add Source

Add a Source to a STIX Bundle

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | STIX Bundle |
| `bundle_path` | `string` | STIX Bundle (from file) |
| `source` | `object` | STIX Identity Source |
| `source_path` | `string` | STIX Identity Source (from file) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | Resulting STIX Bundle |
| `bundle_path` | `string` | Resulting STIX Bundle (in a file) |

### Add Tags

Add Tags to Observables

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | STIX Bundle |
| `bundle_path` | `string` | STIX Bundle (from file) |
| `tags` | `array` | Tags to add to all observables |
| `valid_for` | `integer` | Period of validity for created tags (in days) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | Resulting STIX Bundle |
| `bundle_path` | `string` | Resulting STIX Bundle (in a file) |

### Create Relationships

Create STIX Relationships

**Configuration**

{'type': 'string', 'description': 'Description of generated STIX relationships'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | STIX Bundle |
| `bundle_path` | `string` | STIX Bundle (from file) |
| `relationship_type` | `string` | STIX Relationship Type |
| `source` | `string` | STIX ID or JSON Path expression for the relationships' sources |
| `target` | `string` | STIX ID or JSON Path expression for the relationships' targets |
| `tlp` | `string` | TLP to use for relationships (as english or STIX ID) |
| `confidence` | `integer` | Admiralty Credibility score for created relationship (from 1 - Confirmed by other sources, to 6 - Truth cannot be judged) |
| `description` | `string` | Description of generated STIX relationships |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | Resulting STIX Bundle |
| `bundle_path` | `string` | Resulting STIX Bundle (in a file) |

### Cryptolaemus To STIX

Parse Cryptolaemus content

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `content` | `string` | Content to parse |
| `content_path` | `string` | Path to the content file |
| `malware_id` | `string` | Id of the Emotet Malware |
| `campaign_ids` | `object` | Ids of the campaigns. The key must be the campaign name and the value its id. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle_path` | `string` | Path of the bundle file containing the parsed content. |

### CVE to STIX

Convert CVE JSON to STIX 2.1

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `cve_list` | `array` | CVE Objects to convert to STIX |
| `cve_list_paths` | `array` | CVE Objects to convert to STIX, from file paths |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle_path` | `object` | Path of converted STIX Bundle |

### Filter bundle

Filter objects inside a bundle

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | STIX Bundle |
| `bundle_path` | `string` | STIX Bundle (from file) |
| `condition` | `object` | Condition to match |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | Bundle with matching objects |
| `bundle_path` | `string` | Bundle with matching objects (in a file) |
| `excluded_bundle` | `object` | Bundle with excluded objects |
| `excluded_bundle_path` | `string` | Bundle with excluded objects (in a file) |

### Json objects to Observables

Convert a list of json objects into a list of observables

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `items` | `array` | Items to convert to observables |
| `items_path` | `string` | Path of the file holding the list of items to convert |
| `type` | `string` | type of observables |
| `value_path` | `string` | Name or JSON path of the attribute holding the value |
| `tags` | `array` | List of tags to add to the observables |
| `source` | `object` | STIX Identity Source |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `observables` | `object` | Bundle with the list of observables |
| `observables_path` | `string` | Path of the file holding the bundle with the observables |

### VirusTotal LiveHunt to Observables

Convert a livehunt notification into a list of observables

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `notification` | `object` | LiveHunt notification to convert to observables |
| `notification_path` | `string` | Path of the file holding the LiveHunt notification to convert |
| `notification_to_history` | `boolean` | Whether or not the notification should be added to the observable's history. Default to false |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `observables` | `object` | Bundle with the list of observables |
| `observables_path` | `string` | Path of the file holding the bundle with the observables |

### MISP to STIX

Convert MISP event to STIX 2.1

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `event` | `object` | MISP event to convert to STIX |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | Converted STIX Bundle |

### Observables to Contextualized Indicators

Generate Contextualized Indicators from Observables

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | STIX Bundle |
| `bundle_path` | `string` | STIX Bundle (from file) |
| `rules` | `array` | Rules to use on observables to contextualize data |
| `indicator_types` | `array` | STIX Indicator Types |
| `exclude` | `array` | Fields to exclude from pattern |
| `kill_chain_phases` | `array` | Indicator Kill Chain Phases |
| `tlp` | `string` | TLP to use for indicators (as english or STIX ID) |
| `valid_for` | `integer` | Period of validity for created indicator (in days) |
| `confidence` | `integer` | Admiralty Credibility score for created indicator (from 1 - Confirmed by other sources, to 6 - Truth cannot be judged) |
| `port_path` | `string` | JSON Path to extract the port in the observable. |
| `network_traffic_direction` | `string` | Direction of the network traffic. Either 'src' or 'dst' |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | Resulting STIX Bundle |
| `bundle_path` | `string` | Resulting STIX Bundle (in a file) |

### Observables to Indicators

Generate Indicators from Observables

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | STIX Bundle |
| `bundle_path` | `string` | STIX Bundle (from file) |
| `indicator_types` | `array` | STIX Indicator Types |
| `exclude` | `array` | Fields to exclude from pattern |
| `kill_chain_phases` | `array` | Indicator Kill Chain Phases |
| `tlp` | `string` | TLP to use for indicators (as english or STIX ID) |
| `valid_for` | `integer` | Period of validity for created indicator (in days) |
| `confidence` | `integer` | Admiralty Credibility score for created indicator (from 1 - Confirmed by other sources, to 6 - Truth cannot be judged) |
| `port_path` | `string` | JSON Path to extract the port in the observable. |
| `network_traffic_direction` | `string` | Direction of the network traffic. Either 'src' or 'dst' |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | Resulting STIX Bundle |
| `bundle_path` | `string` | Resulting STIX Bundle (in a file) |

### Remove Orphan Objects

Remove objects without any relationship from a STIX bundle.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | STIX Bundle |
| `bundle_path` | `string` | STIX Bundle (from file) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | Resulting STIX Bundle |
| `bundle_path` | `string` | Resulting STIX Bundle (in a file) |

### Split bundle

Split a STIX Bundle in smaller ones

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | STIX Bundle |
| `bundle_path` | `string` | STIX Bundle (from file) |
| `number_of_items` | `number` | Approximate number of items to include in each bundle |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle_paths` | `array` | Resulting STIX Bundles |

### STIX to MISP

Convert STIX bundle to MISP event

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | STIX Bundle |
| `bundle_path` | `string` | STIX Bundle (from file) |
| `organization` | `object` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `event` | `object` | Resulting MISP event |
| `event_path` | `string` | Resulting MISP event (to file) |

### Strings to Observables

Convert a list of strings into a list of observables

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `items` | `array` | Items to convert to observables |
| `items_path` | `string` | Path of the file holding the list of items to convert |
| `type` | `string` | type of observables |
| `tags` | `array` | List of tags to add to the observables |
| `source` | `object` | STIX Identity Source |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `observables` | `object` | Bundle with the list of observables |
| `observables_path` | `string` | Path of the file holding the bundle with the observables |


## Extra

Module **`STIX` v1.72.1**