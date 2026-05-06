# Cases

Cases let you group investigation findings across multiple perimeters, alerts, and analysts, and share results with your end-users in a structured and traceable way. You can create a case from an existing alert or add alerts to a case at any point during your investigation.

## What cases contain

A case consolidates the following elements into a single investigation workspace:

| Element | Description |
|---|---|
| Alerts | One or more alerts that triggered the investigation. |
| Tasks | Manual actions to track and assign across your team. |
| Events | Raw security events raised by the alerts or added directly. |
| Graph investigation | A visual map of observables, relationships, and threat intelligence objects. |
| Comments | A timestamped timeline of analyst notes. |

## Custom statuses and verdicts

Cases support the same custom status and verdict system as alerts, enabling consistent terminology and workflows across your SOC. You configure custom statuses and verdicts in **Settings > Statuses and verdicts**.

### Custom statuses

Custom statuses let you define case lifecycle stages that match your organization's investigation processes. Each status belongs to one of three stages:

* **Open**: cases that are active and require attention.
* **In progress**: cases under active investigation.
* **Closed**: cases that have been resolved or dismissed.

You can configure custom statuses to apply exclusively to cases, exclusively to alerts, or to both. Enabling a status for both contexts ensures consistent terminology across your investigation workflows.

!!! note "Status history"
    Case history preserves the original status name even if a custom status is modified later. Historical records always reflect the status names that were in use at the time of each change.

### Custom verdicts

Custom verdicts provide standardized classification of case outcomes. Each verdict belongs to either the **True positive** or **False positive** category, allowing your team to document investigation conclusions with organization-specific terminology.

Like custom statuses, you can enable verdicts for cases, alerts, or both.

## Related articles

* [Create a case](/xdr/features/investigate/create_a_case.md): Step-by-step instructions to open a new case and configure its initial properties.
* [Manage cases](/xdr/features/investigate/manage_cases.md): How to filter, sort, and perform bulk actions on cases from the listing page.
* [Case details](/xdr/features/investigate/case_details.md): Reference for every tab and field available on the case details page.
* [Graph investigation](/xdr/features/investigate/graph_investigation.md): How to use the interactive graph to correlate observables and threat intelligence.
* [Case custom fields](/xdr/features/investigate/case_custom_fields.md): How to extend cases with structured, typed metadata fields.
* [AI Cases](/xdr/features/investigate/ai_cases.md): How Sekoia.io automatically correlates alerts into cases using AI.
* [Alerts](/xdr/features/investigate/alerts.md): How alerts are created and how to manage them before grouping them into cases.
