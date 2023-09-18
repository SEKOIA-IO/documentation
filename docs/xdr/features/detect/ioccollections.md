{!_shared_content/ioccollections.md!}

## Telemetry Reports

Telemetry Reports can be used to quickly determine if any indicator inside the collection was seen within your events.

Telemetry Reports have the following properties:

- Telemetry is only available for some observable types: IP addresses, domain names and file hashes. File Hashes are only supported from January 31st, 2023
- Telemetry is checked for the past year, even if associated events are no longer available
- When looking at the telemetry for an indicator, the `valid from` and `valid until` dates are ignored

### Generate a telemetry report

Click on `Generate telemetry report` to automatically check all indicators against Sekoia.io’s telemetry. Depending on the numbers of indicators inside your collection, this can take a few minutes. When the report is available, the button will change to `See telemetry report`.

!!! Tip
    You don’t have to stay on this page waiting for your report to be available. When it eventually is, you will receive an in-app notification with a link.

!!! Note
    Inside an MSSP community, the report will be generated for the communities that are currently selected.

### Display a telemetry report

You can access a telemetry report by clicking on the `See telemetry report` button or on the in-app notification indicating that the report is available.

Telemetry reports list all indicators inside the collection that were seen in events, ordered by the number of sightings. At the end of each line, there is a `Sightings` column indicating the number of sightings for this indicator. Clicking on this number will show you the detailed telemetry heatmap.

## Detect threats using IOC Collections

Any IOC Collection can be used inside a detection rule in the Operations Center. Creating a rule for an IOC Collection has the following benefits:

- Any match of an indicator in future events will create an Alert
- Any match of an indicator in past events will create an Alert (retrohunt)

!!! Note 
    Detection rules using IOC Collections are taking the validity period of an indicator when creating alerts.

To create a detection rule based on an IOC Collection, you can:

- Select the option inside the IOC Collection creation modal
- Create a rule from the Rules Catalog. Choose `CTI` as rule type and `IOC Collections` as source
