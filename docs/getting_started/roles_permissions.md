## Roles

Content is on its way. 

## Permissions

In SEKOIA.IO, permissions do not necessarily have common names across the platform. 

Use the search bar on top of the permissions list to filter permissions depending on the needed service.
  
### Operations Center

#### Alerts

Need to access the [alerts](https://docs.sekoia.io/xdr/features/investigate/alerts/) page? Search `alert` and you’ll get all the permissions linked to this page. 

| Name | Description |
| --- | --- |
| SIC_WRITE_ALERTS_COMMENT | Post a comment on an alert |
| SIC_WRITE_ALERTS_WORKFLOW | Triggers an action on the alert workflow |
| SIC_WRITE_ALERTS | Create, Update and delete SIC alerts |
| SIC_READ_ALERTS | List and consult SIC alerts |
| SIC_READ_ALERT_STATS | Get statistics about SIC alerts |
| SIC_WRITE_GENERATION_MODES | Create or edit alert generation mode |
| SIC_READ_GENERATION_MODES | Get generation modes |

!!! note
    SIC is the term we use internally for the Operations Center. 


#### Assets

Need to access the [Assets](https://docs.sekoia.io/xdr/features/collect/assets/) page? Search `Assets` and you’ll get all the permissions linked to this page. 

| Name | Description |
| --- | --- |
| ASSETMANAGEMENT_VIEW_CUSTOM_ASSET | Allow to read a custom asset |
| ASSETMANAGEMENT_WRITE_CUSTOM_ASSET_KEY | Allow to create a custom key |
| ASSETMANAGEMENT_CREATE_ASSET_KEY | Allow to add a key to an asset |
| ASSETMANAGEMENT_DELETE_ASSET_KEY | Allow to delete a key of an asset |
| ASSETMANAGEMENT_DELETE_ASSET_ATTRIBUTE | Allow to delete an attribute of an asset |
| ASSETMANAGEMENT_UPDATE_ASSET_ATTRIBUTE | Allow to update a key of an asset |
| ASSETMANAGEMENT_CREATE_ASSET_ATTRIBUTE | Allow to add an attribute to an asset |
| ASSETMANAGEMENT_VIEW_ASSET_ATTRIBUTE | Allow to retrieve or list attributes of an asset |
| ASSETMANAGEMENT_DELETE_ASSET_OWNER | Allow to delete an owner of an asset |
| ASSETMANAGEMENT_CREATE_ASSET_OWNER | Allow to add an owner to an asset |
| ASSETMANAGEMENT_VIEW_ASSET_ONwER | Allow to retrieve or list owners of an asset |
| ASSETMANAGEMENT_DELETE_ASSET | Allow to delete an asset |
| ASSETMANAGEMENT_UPDATE_ASSET | Allow to update an asset |
| ASSETMANAGEMENT_CREATE_ASSET | Allow to create a new asset |
| ASSETMANAGEMENT_VIEW_ASSET | Allow to retrieve or list assets |
| ASSETMANAGEMENT_VIEW_ATTRIBUTE_NAME | Allow to list attribute names |
| ASSETMANAGEMENT_VIEW_ASSET_TYPE | Allow to list types of assets |
| ASSETMANAGEMENT_VIEW_ASSET_CATEGORY | Allow to list categories of assets |

#### Cases

Need to access the [Cases](https://docs.sekoia.io/xdr/features/investigate/cases/) page? Search `incident` and you’ll get all the permissions linked to this page. 

| Name | Description |
| --- | --- |
| SIC_READ_INCIDENTS | Get incidents |
| SIC_WRITE_INCIDENTS | Edit incidents |

!!! note
    Incident is the term we use internally for Cases.


#### Countermeasures

Need to access the Countermeasures page? Search `countermeasure` and you’ll get all the permissions linked to this page. 

| Name | Description |
| --- | --- |
| SIC_READ_COUNTERMEASURES | Get information about a set of countermeasures |
| SIC_DELETE_COUNTERMEASURES | Delete a set of countermeasures |
| SIC_WRITE_COUNTERMEASURES | Create or edit a set of countermeasures |

#### Entities

Need to access the [Entities](https://docs.sekoia.io/xdr/features/collect/entities/) page? Search `entity` and you’ll get all the permissions linked to this page. 

| Name | Description |
| --- | --- |
| SIC_DELETE_ENTITIES | Delete entities |
| SIC_READ_ENTITIES | Get information about entities |
| SIC_WRITE_ENTITIES | Create or edit entities |

#### Events

Need to access the [events](https://docs.sekoia.io/xdr/features/investigate/events/) page? Search `events` and you’ll get all the permissions linked to this page. 

| Name | Description |
| --- | --- |
| EVENTS_READ_STATS | Read statistics |
| EVENTS_READ_DATASETS | Read anomaly dataset |
| SIC_READ_EVENT_STATS | Get statistics about SIC events |

#### Intakes

Need to access the [intakes](https://docs.sekoia.io/xdr/features/collect/intakes/) page and create or edit some intakes? Search `intake` and you’ll get all the permissions linked to this page. 

| Name | Description |
| --- | --- |
| SIC_READ_INTAKES | Get information about a set of intakes |
| SIC_WRITE_INTAKES | Create or edit intakes |

#### Rules

Need to set up a role for the [Rules Catalog](https://docs.sekoia.io/xdr/features/detect/rules_catalog/)? Search `rule` and you’ll get all the permissions linked to this page. 

| Name | Description |
| --- | --- |
| SIC_CONFIGURE_RULES | Configure setting for rules |
| SIC_ENABLE_DISABLE_RULES | Enable or disable rules |
| SIC_DELETE_RULES | Delete rules |
| SIC_READ_RULES | Get information related to rules |
| SIC_WRITE_RULES | Create or edit detection rules |

### Intelligence Center

Need to access the Intelligence Center ? Here are all the permissions linked to the product.

| Name | Description |
| --- | --- |
| INTHREAT_WRITE_GRAPHS | Write graphs to InThreat |
| INTHREAT_READ_GRAPHS | Read graphs from InThreat |
| INTHREAT_WRITE_FEEDS | Write feeds to InThreat |
| INTHREAT_READ_FEEDS | Read feeds from InThreat |
| INTHREAT_READ_OBSERVABLES | Read observables from InThreat |
| INTHREAT_READ_OBJECTS | Read objects from InThreat |
| READ_TELEMETRY | Read the telemetry measures |

!!! note
    InThreat is the term we use internally for the Intelligence Center 


## Common

### Playbooks

Need to access [playbooks](https://docs.sekoia.io/tip/features/automate/)? Search `symphony` and you’ll get all the permissions linked to this page. 

| Name | Description |
| --- | --- |
| SYMPHONY_READ_PLAYBOOK_RUNS_STATS | List and get statistics about Symphony Playbook Runs |
| SYMPHONY_READ_MODULES | List and get Symphony Modules |
| SYMPHONY_WRITE_PLAYBOOK_RUNS | Modify Symphony Playbook Runs |
| SYMPHONY_READ_PLAYBOOK_RUNS | List and get Symphony Playbook Runs |
| SYMPHONY_WRITE_PLAYBOOKS | Write Symphony Playbooks |
| SYMPHONY_READ_PLAYBOOKS | List and get Symphony Playbooks |

!!! note
    Symphony is the name we use internally for Playbooks. 


### Dashboards

Need to access dashboards? Search `dashboard` and you’ll get all the permissions linked to this page. 

| Name | Description |
| --- | --- |
| DASHBOARD_WRITE_DASHBOARDS | Write dashboards |
| DASHBOARD_READ_DASHBOARDS | Read dashboards |

### Manage communities

Need to manage your communities? Search `community` and you’ll get all the permissions linked to this section. 

| Name | Description |
| --- | --- |
| COMMUNITY_WRITE_APIKEY | Allow to generate and revoke community api keys |
| COMMUNITY_READ_APIKEY | Allow to read community api keys |
| COMMUNITY_READ_ROLE | Allow to read role. |
| COMMUNITY_WRITE_ROLE | Allow to write role. |
| COMMUNITY_ASSIGN_ROLE | Assign role to an avatar. |
| COMMUNITY_REMOVE_ROLE | Remove role of an avatar. |
| COMMUNITY_ADD_MEMBER | Add avatar to the community. |
| COMMUNITY_REMOVE_MEMBER | Remove avatar of the community. |
| COMMUNITY_LIST_MEMBER | List avatar of the community. |
| COMMUNITY_EDIT_COMMUNITY | Edit the community information. |
| COMMUNITY_WRITE_DELEGATION | Allow to create or revoke delegations |
| COMMUNITY_READ_DELEGATION | Allow to read delegations |




