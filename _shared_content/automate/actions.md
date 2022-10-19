# Actions

## Types of Actions

An `Action` helps you execute specific tasks depending on your needs. There are 5 main types of actions in the playbooks: 

- Interact with the platform: [getters](#getters) and [setters](#setters)
- Extract data: [data collection enrichers](#data-collection)
- Connect and use [third-party applications](#third-party-applications)
- Set up [notifications](#notifications)
- Use [helpers](#Helpers) to build your own actions

The Actions Library lists all available actions in playbooks with their detailed configuration.

## SEKOIA.IO Actions 

### Getters

**Get alerts**: To retrieve detailed alert information such as the urgency, name of the rule, pattern, etc… except events.

**Get events**: To retrieve events based on a search. This action is equivalent to a search on the event page and takes into consideration 3 parameters: a query with filters (`source.ip`=xx.xxx.xx), and earliest time/latest time: two dates to determine the date range of the search.

`get events` can be used to retrieve events from an alert. Events associated to an alert contain the key `alert_short_ids` with the value of the ID of the alert.

### Setters

- Edit alert
- Comment alert
- Update alert status

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
- [Mattermost](library/mattermost.md): Post message / Post SEKOIA.IO alert
- [Pagerduty](library/pagerduty.md): Trigger Alert
- [The Hive](library/the-hive.md): Create an alert in the Hive

## Data collection

If you have an account in one of the listed tools below, you can easily extract data from there and import it to SEKOIA.IO. This is made possible with an API key. 

- [BinaryEdge](_shared_content/automate/library/binaryedge-s-api.md)
- [Censys](_shared_content/automate/library/censys.md)
- [GLIMPS](_shared_content/automate/library/glimps.md)
- [IKnowWhatYouDownloaded](_shared_content/automate/library/iknowwhatyoudownload.md)
- [Onyphe](_shared_content/automate/library/onyphe.md)
- [Public Suffix](_shared_content/automate/library/public-suffix.md)
- [RiskIQ](_shared_content/automate/library/riskiq.md)
- [Shodan](_shared_content/automate/library/shodan.md)
- [VirusTotal](_shared_content/automate/library/virustotal.md)
- [Whois](_shared_content/automate/library/whois.md)

## Helpers

- [fileutils](_shared_content/automate/library/fileutils.md)
- [http](_shared_content/automate/library/http.md)
- [STIX](_shared_content/automate/library/stix.md)

These helpers need their associated trigger to function properly: 

- [MISP](_shared_content/automate/library/misp.md)
- [MWDB](_shared_content/automate/library/mwdb.md)
- [Triage](_shared_content/automate/library/triage.md)

## Third-party applications

- [Azure AD](_shared_content/automate/library/azure-active-directory.md) 
- [Fortigate Firewalls](_shared_content/automate/library/fortigate-firewalls.md)
- [HarfangLab](_shared_content/automate/library/harfanglab.md)
- [Panda Security](_shared_content/automate/library/panda-security.md)
- [Sentinel One](_shared_content/automate/library/sentinel-one.md)
- [ServiceNow](_shared_content/automate/library/servicenow.md)

More actions are available in the Actions Library. To learn how to set up an action, please refer to its documentation. 

!!!note 
	The dynamic content is written in JINJA. For more information on this language, please follow this [documentation](https://jinja.palletsprojects.com/en/2.10.x/templates/).
