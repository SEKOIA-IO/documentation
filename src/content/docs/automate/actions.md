---
title: "actions"
category: "automate"
---
# Actions

## Types of Actions

An `Action` helps you execute specific tasks depending on your needs. There are 5 main types of actions in the playbooks:

- Interact with the platform: [getters](#getters) and [setters](#setters)
- Extract data: [data collection enrichers](#data-collection)
- Connect and use [third-party applications](#third-party-applications)
- Set up [notifications](#notifications)
- Use [helpers](#Helpers) to build your own actions

The Actions Library lists all available actions in playbooks with their detailed configuration.

## Sekoia.io Actions

### Getters

| Name | Description |
| --- | --- |
| [Get Event Field Common Values](../library/sekoia-io/#get-event-field-common-values) | Retrieve the most common values of an ECS field based on the time window |
| [List Assets](../library/sekoia-io/#list-assets) | Retrieve detailed information about assets based on a filter |
| [Search Alerts](../library/sekoia-io/#search-alerts) | Retrieve detailed information about alerts (such as the urgency, name of the rule, etc… except events) based on a filter. |
| [Get Alert](../library/sekoia-io/#get-alert) | Retrieve detailed alert information such as the urgency, name of the rule, pattern, etc… except events. |
| [Get Events](../library/sekoia-io/#get-events) | Retrieve events based on a search. This action is equivalent to a search on the event page and takes into consideration 3 parameters: a query with filters (`source.ip=xx.xxx.xx`), and earliest time/latest time: two dates to determine the date range of the search. |

!!!note
	`Get Events` can be used to retrieve events from an alert. Events associated to an alert contain the key `alert_short_ids` with the value of the ID of the alert.

### Setters

| Name | Description |
| --- | --- |
| [Create an asset](../library/sekoia-io/#create-asset) | Create an asset |
| [Delete an asset](../library/sekoia-io/#delete-an-asset) | Delete an asset |
| [Add attribute to asset](../library/sekoia-io/#add-attribute-to-asset) | Add attribute to asset |
| [Add key to asset](../library/sekoia-io/#add-key-to-asset) | Add key to asset |
| [Edit alert](../library/sekoia-io/#edit-alert) | Edit an alert details such as the urgency or the alert category |
| [Comment alert](../library/sekoia-io/#comment-alert) | Add a comment to the alert |
| [Update alert status](../library/sekoia-io/#update-alert-status) | Change the status of an alert |
| [Push Events to Intake](../library/sekoia-io/#push-events-to-intake) | Push one or more events to an Intake |
| [Attach Alerts to Case](../library/sekoia-io/#attach-alerts-to-case) | Attach one or more alerts to a case. |


#### How to update an alert status

To update an alert status, you need to copy the `action_uuid` corresponding to the needed action.

| Action | Description | action_uuid |
| --- | --- | --- |
| Acknowledge | Acknowledge the alert | `937bdabf-6a08-434b-b6d3-d7447e4e452a` |
| Validate | Validate alert | `c39a0a95-aa2c-4d0d-8d2e-d3decf426eea` |
| Reject | Reject alert | `ade85d7b-7507-4026-bfc6-cc006d10ddac` |
| Close | Close alert | `1390be4e-ced8-4dd6-9bed-573471b235ab` |

## Notifications

To get notified, you can rely on these tools:

- [Mandrill](library/mandrill.md): Send Message
- [Mattermost](library/mattermost.md): Post message / Post Sekoia.io alert
- [Pagerduty](library/pagerduty.md): Trigger Alert
- [The Hive](library/the-hive.md): Create an alert in the Hive

## Data collection

If you have an account in one of the listed tools below, you can easily extract data from there and import it to Sekoia.io. This is made possible with an API key.

- [BinaryEdge](library/binaryedge-s-api.md)
- [Censys](library/censys.md)
- [GLIMPS](library/glimps.md)
- [IKnowWhatYouDownloaded](library/iknowwhatyoudownload.md)
- [Onyphe](library/onyphe.md)
- [Public Suffix](library/public-suffix.md)
- [RiskIQ](library/riskiq.md)
- [Shodan](library/shodan.md)
- [VirusTotal](library/virustotal.md)
- [Whois](library/whois.md)

## Helpers

| Name | Description |
| --- | --- |
| [fileutils](library/fileutils.md) | Extract data from XML or JSON files |
| [http](library/http.md) | Request HTTP resources (download file, request URL) |
| [STIX](library/stix.md) | Add source, ass tags, create relationships, cryptolaemus to STIX, CVE to STIX, filter bundle, JSON objects to observables, VirusTotal LiveHunt to observables, MISP to STIX, observables to contextualized indicators, observables to indicators, remove orphan objects, STIX to MISP, string to observables |

These helpers need their associated trigger to function properly:

| Name | Description |
| --- | --- |
| [MISP](library/misp.md) | Gather, store, share and correlate threat intelligence. Convert from MISP to STIX, publish MISP event |
| [MWDB](library/mwdb.md) | Convert a MWDB config to a bundle of observables |
| [Triage](library/triage.md) | Triage raw results to observables |

## Third-party applications

- [Azure AD](library/azure-active-directory.md)
- [Fortigate Firewalls](library/fortigate-firewalls.md)
- [HarfangLab](library/harfanglab.md)
- [Panda Security](library/panda-security.md)
- [Sentinel One](library/sentinel-one.md)
- [ServiceNow](library/servicenow.md)

More actions are available in the Actions Library. To learn how to set up an action, please refer to its documentation.

!!!note
	The dynamic content is written in JINJA. For more information on this language, please follow this [documentation](https://jinja.palletsprojects.com/en/2.10.x/templates/).
