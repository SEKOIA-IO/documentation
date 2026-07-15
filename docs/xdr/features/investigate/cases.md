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

## Custom statuses, verdicts and priorities

Cases support the same custom status and verdict system as alerts, enabling consistent terminology and workflows across your SOC. A status belongs to one of three stages, **Open**, **In progress** or **Closed**, and you can enable it for cases only, for alerts only, or for both. Case priorities are configured in the same place, and apply to cases only.

You configure all three in **Settings > Custom Statuses**.

!!! note "Status history"
    Case history preserves the original status name even if a custom status is modified later. Historical records always reflect the status names that were in use at the time of each change.

## Related articles

* [Custom statuses](/xdr/features/investigate/custom_statuses.md): What custom statuses are, the three stages, and how one status serves both alerts and cases.
* [Manage custom statuses](/xdr/features/investigate/manage_custom_statuses.md): How to create, edit, reorder and enable custom statuses.
* [Migrate custom statuses](/xdr/features/investigate/migrate_custom_statuses.md): How to disable or delete a status that alerts and cases already use.
* [Custom verdicts](/xdr/features/investigate/custom_verdicts.md): How to standardize the classification of case and alert outcomes.
* [Custom priorities](/xdr/features/investigate/custom_priorities.md): How case priority levels are configured and ordered.

* [Create a case](/xdr/features/investigate/create_a_case.md): Step-by-step instructions to open a new case and configure its initial properties.
* [Manage cases](/xdr/features/investigate/manage_cases.md): How to filter, sort, and perform bulk actions on cases from the listing page.
* [Case details](/xdr/features/investigate/case_details.md): Reference for every tab and field available on the case details page.
* [Graph investigation](/xdr/features/investigate/graph_investigation.md): How to use the interactive graph to correlate observables and threat intelligence.
* [Case custom fields](/xdr/features/investigate/case_custom_fields.md): How to extend cases with structured, typed metadata fields.
* [AI Cases](/xdr/features/investigate/ai_cases.md): How Sekoia.io automatically correlates alerts into cases using AI.
* [Alerts](/xdr/features/investigate/alerts.md): How alerts are created and how to manage them before grouping them into cases.
