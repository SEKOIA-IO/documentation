# Assets management

Assets in SEKOIA.IO can be of different types. The most commonly used are:

- Computers, identified by an ip address or a hostname
- Networks, identified by cidr
- Users, identified by an email address
- ...

The numbers of events and alerts associated with assets for the past 7 days, as well as the risk level, are displayed in the asset list.

Assets participate to the security workflow of the community, when an incoming event matches with a defined asset, the event is enriched with assets information. Their criticality will be taken into account when calculating the urgency of an alert, together with the severity of the rule that triggered the alert. When more than one asset match with an event, the highest criticality is used for urgency calculation. Criticality of assets ranges from 0 to 100, 100 being the most critical.

Assets also permit the selective application of detection rules: rules can be applied to one, several or all entities, and to one, several or all assets.

![Assets Management](/assets/operation_center/assets.gif)
