# Actions

## Types of Actions

An `Action` helps you execute specific tasks depending on your needs. There are 5 main types of actions in the playbooks:

- Interact with the platform: [getters](#getters) and [setters](#setters)
- Extract data: [data collection enrichers](#data-collection)
- Connect and use [third-party applications](#third-party-applications)
- Set up [notifications](#notifications)
- Use [helpers](#helpers) to build your own actions

The Actions Library lists all available actions in playbooks with their detailed configuration.

## Sekoia.io Actions

### Getters

| Name | Description |
| --- | --- |
| [Get Event Field Common Values](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#get-event-field-common-values) | Retrieve the most common values of an ECS field based on the time window |
| [List Assets](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#list-assets) | Retrieve detailed information about assets based on a filter |
| [Search Alerts](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#search-alerts) | Retrieve detailed information about alerts (such as the urgency, name of the rule, etc… except events) based on a filter. |
| [Get Alert](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#get-alert) | Retrieve detailed alert information such as the urgency, name of the rule, pattern, etc… except events. |
| [Get Events](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#get-events) | Retrieve events based on a search. This action is equivalent to a search on the event page and takes into consideration 3 parameters: a query with filters (`source.ip=xx.xxx.xx`), and earliest time/latest time: two dates to determine the date range of the search. |

{% hint style="info" %}
`Get Events` can be used to retrieve events from an alert. Events associated to an alert contain the key `alert_short_ids` with the value of the ID of the alert.
{% endhint %}

### Setters

| Name | Description |
| --- | --- |
| [Create an asset](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#create-asset) | Create an asset |
| [Delete an asset](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#delete-an-asset) | Delete an asset |
| [Add attribute to asset](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#add-attribute-to-asset) | Add attribute to asset |
| [Add key to asset](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#add-key-to-asset) | Add key to asset |
| [Edit alert](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#edit-alert) | Edit an alert details such as the urgency or the alert category |
| [Comment alert](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#comment-alert) | Add a comment to the alert |
| [Update alert status](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#update-alert-status) | Change the status of an alert |
| [Push Events to Intake](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#push-events-to-intake) | Push one or more events to an Intake |
| [Attach Alerts to Case](https://docs.sekoia.com/integrations/action_library/generic/sekoia-io#attach-alerts-to-case) | Attach one or more alerts to a case. |


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

- [Mandrill](https://docs.sekoia.com/integrations/action_library/applicative/mandrill): Send Message
- [Mattermost](https://docs.sekoia.com/integrations/action_library/applicative/mattermost): Post message / Post Sekoia.io alert
- [Pagerduty](https://docs.sekoia.com/integrations/action_library/applicative/pagerduty): Trigger Alert
- [The Hive](https://docs.sekoia.com/integrations/action_library/collaboration_tools/the-hive): Create an alert in the Hive
- ...

## Data collection

If you have an account in one of the listed tools below, you can easily extract data from there and import it to Sekoia.io. This is made possible with an API key.

- [Censys](https://docs.sekoia.com/integrations/action_library/threat_intelligence/censys)
- [GLIMPS](https://docs.sekoia.com/integrations/action_library/threat_intelligence/glimps)
- [IKnowWhatYouDownloaded](https://docs.sekoia.com/integrations/action_library/threat_intelligence/iknowwhatyoudownload)
- [Onyphe](https://docs.sekoia.com/integrations/action_library/threat_intelligence/onyphe)
- [Public Suffix](https://docs.sekoia.com/integrations/action_library/threat_intelligence/public-suffix)
- [Shodan](https://docs.sekoia.com/integrations/action_library/threat_intelligence/shodan)
- [VirusTotal](https://docs.sekoia.com/integrations/action_library/threat_intelligence/virustotal)
- [Whois](https://docs.sekoia.com/integrations/action_library/threat_intelligence/whois)
- ...

## Helpers

| Name | Description |
| --- | --- |
| [fileutils](https://docs.sekoia.com/integrations/action_library/generic/utils) | Extract data from XML or JSON files |
| [http](https://docs.sekoia.com/integrations/action_library/generic/http) | Request HTTP resources (download file, request URL) |
| [STIX](https://docs.sekoia.com/integrations/action_library/stix) | Add source, add tags, create relationships, cryptolaemus to STIX, CVE to STIX, filter bundle, JSON objects to observables, VirusTotal LiveHunt to observables, MISP to STIX, observables to contextualized indicators, observables to indicators, remove orphan objects, STIX to MISP, string to observables |

These helpers need their associated trigger to function properly:

| Name | Description |
| --- | --- |
| [MISP](https://docs.sekoia.com/integrations/action_library/threat_intelligence/misp) | Gather, store, share and correlate threat intelligence. Convert from MISP to STIX, publish MISP event |
| [MWDB](https://docs.sekoia.com/integrations/action_library/threat_intelligence/mwdb) | Convert a MWDB config to a bundle of observables |
| [Triage](https://docs.sekoia.com/integrations/action_library/threat_intelligence/triage) | Triage raw results to observables |

## Third-party applications

- [Microsoft Entra ID (Azure AD) ](https://docs.sekoia.com/integrations/action_library/iam/microsoft-entra-id)
- [Microsoft Remote Server](https://docs.sekoia.com/integrations/action_library/endpoint/microsoft-windows-server)
- [Fortigate Firewalls](https://docs.sekoia.com/integrations/action_library/network/fortigate-firewalls)
- [HarfangLab](https://docs.sekoia.com/integrations/action_library/endpoint/harfanglab)
- [Panda Security](https://docs.sekoia.com/integrations/action_library/endpoint/panda-security)
- [Sentinel One](https://docs.sekoia.com/integrations/action_library/endpoint/sentinelone)
- [ServiceNow](https://docs.sekoia.com/integrations/action_library/collaboration_tools/servicenow)
- ...

More actions are available in the Actions Library. To learn how to set up an action, please refer to its documentation.

{% hint style="info" %}
The dynamic content is written in JINJA. For more information on this language, please follow this [documentation](https://jinja.palletsprojects.com/en/2.10.x/templates/).
{% endhint %}
