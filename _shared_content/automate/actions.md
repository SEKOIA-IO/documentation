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
| [Get Event Field Common Values](/integration/action_library/generic/sekoia-io/#get-event-field-common-values) | Retrieve the most common values of an ECS field based on the time window |
| [List Assets](/integration/action_library/generic/sekoia-io/#list-assets) | Retrieve detailed information about assets based on a filter |
| [Search Alerts](/integration/action_library/generic/sekoia-io/#search-alerts) | Retrieve detailed information about alerts (such as the urgency, name of the rule, etc… except events) based on a filter. |
| [Get Alert](/integration/action_library/generic/sekoia-io/#get-alert) | Retrieve detailed alert information such as the urgency, name of the rule, pattern, etc… except events. |
| [Get Events](/integration/action_library/generic/sekoia-io/#get-events) | Retrieve events based on a search. This action is equivalent to a search on the event page and takes into consideration 3 parameters: a query with filters (`source.ip=xx.xxx.xx`), and earliest time/latest time: two dates to determine the date range of the search. |

!!!note
	`Get Events` can be used to retrieve events from an alert. Events associated to an alert contain the key `alert_short_ids` with the value of the ID of the alert.

### Setters

| Name | Description |
| --- | --- |
| [Create an asset](/integration/action_library/generic/sekoia-io/#create-asset) | Create an asset |
| [Delete an asset](/integration/action_library/generic/sekoia-io/#delete-an-asset) | Delete an asset |
| [Add attribute to asset](/integration/action_library/generic/sekoia-io/#add-attribute-to-asset) | Add attribute to asset |
| [Add key to asset](/integration/action_library/generic/sekoia-io/#add-key-to-asset) | Add key to asset |
| [Edit alert](/integration/action_library/generic/sekoia-io/#edit-alert) | Edit an alert details such as the urgency or the alert category |
| [Comment alert](/integration/action_library/generic/sekoia-io/#comment-alert) | Add a comment to the alert |
| [Update alert status](/integration/action_library/generic/sekoia-io/#update-alert-status) | Change the status of an alert |
| [Push Events to Intake](/integration/action_library/generic/sekoia-io/#push-events-to-intake) | Push one or more events to an Intake |
| [Attach Alerts to Case](/integration/action_library/generic/sekoia-io/#attach-alerts-to-case) | Attach one or more alerts to a case. |


#### How to update an alert status

To update an alert status, you need to copy the `status_uuid` corresponding to the needed action.

| Action | Description | status_uuid |
| --- | --- | --- |
| Pending | This alert needs to be addressed | `2efc4930-1442-4abb-acf2-58ba219a4fd0` |
| Acknowledge | Alert will be evaluated (true or false positive?) | `8f206505-af6d-433e-93f4-775d46dc7d0f` |
| Ongoing | Alert might be a true positive and action must be taken | `1f2f88d5-ff5b-48bf-bbbc-00c2fff82d9f` |
| Reject | It is a false positive or the alert will be not addressed | `4f68da89-38e0-4703-a6ab-652f02bdf24e` |
| Close | It was a true positive and the alert has been addressed | `1738b1c1-767d-489e-bada-19176621a007` |

## Notifications

To get notified, you can rely on these tools:

- [Mandrill](/integration/action_library/applicative/mandrill.md): Send Message
- [Mattermost](/integration/action_library/applicative/mattermost.md): Post message / Post Sekoia.io alert
- [Pagerduty](/integration/action_library/applicative/pagerduty.md): Trigger Alert
- [The Hive](/integration/action_library/collaboration_tools/the-hive.md): Create an alert in the Hive
- ...

## Data collection

If you have an account in one of the listed tools below, you can easily extract data from there and import it to Sekoia.io. This is made possible with an API key.

- [BinaryEdge](/integration/action_library/threat_intelligence/binaryedge-s-api.md)
- [Censys](/integration/action_library/threat_intelligence/censys.md)
- [GLIMPS](/integration/action_library/threat_intelligence/glimps.md)
- [IKnowWhatYouDownloaded](/integration/action_library/threat_intelligence/iknowwhatyoudownload.md)
- [Onyphe](/integration/action_library/threat_intelligence/onyphe.md)
- [Public Suffix](/integration/action_library/threat_intelligence/public-suffix.md)
- [RiskIQ](/integration/action_library/threat_intelligence/riskiq.md)
- [Shodan](/integration/action_library/threat_intelligence/shodan.md)
- [VirusTotal](/integration/action_library/threat_intelligence/virustotal.md)
- [Whois](/integration/action_library/threat_intelligence/whois.md)
- ...

## Helpers

| Name | Description |
| --- | --- |
| [fileutils](/integration/action_library/generic/fileutils.md) | Extract data from XML or JSON files |
| [http](/integration/action_library/generic/http.md) | Request HTTP resources (download file, request URL) |
| [STIX](/integration/action_library/threat_intelligence/stix.md) | Add source, add tags, create relationships, cryptolaemus to STIX, CVE to STIX, filter bundle, JSON objects to observables, VirusTotal LiveHunt to observables, MISP to STIX, observables to contextualized indicators, observables to indicators, remove orphan objects, STIX to MISP, string to observables |

These helpers need their associated trigger to function properly:

| Name | Description |
| --- | --- |
| [MISP](/integration/action_library/threat_intelligence/misp.md) | Gather, store, share and correlate threat intelligence. Convert from MISP to STIX, publish MISP event |
| [MWDB](/integration/action_library/threat_intelligence/mwdb.md) | Convert a MWDB config to a bundle of observables |
| [Triage](/integration/action_library/threat_intelligence/triage.md) | Triage raw results to observables |

## Third-party applications

- [Microsoft Entra ID (Azure AD) ](/integration/action_library/iam_sase/microsoft-entra-id.md)
- [Microsoft Remote Server](/integration/action_library/applicative/microsoft-remote-server.md)
- [Fortigate Firewalls](/integration/action_library/network/fortigate-firewalls.md)
- [HarfangLab](/integration/action_library/endpoint/harfanglab.md)
- [Panda Security](/integration/action_library/endpoint/panda-security.md)
- [Sentinel One](/integration/action_library/endpoint/sentinelone.md)
- [ServiceNow](/integration/action_library/collaboration_tools/servicenow.md)
- ...

More actions are available in the Actions Library. To learn how to set up an action, please refer to its documentation.

!!!note
	The dynamic content is written in JINJA. For more information on this language, please follow this [documentation](https://jinja.palletsprojects.com/en/2.10.x/templates/).
