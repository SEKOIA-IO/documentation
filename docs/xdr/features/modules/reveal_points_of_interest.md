# Points of Interest

Points of Interest (PoIs) are behavioral signals that Reveal surfaces on assets when it detects activity that deviates from an established baseline. They appear in the asset context panel timeline and help analysts identify unusual behavior that may not trigger a rule-based alert.

PoIs complement detection rules by capturing weak signals between alert events. They are not alerts. They do not create cases or require immediate action. They provide investigative context that helps analysts build a fuller picture of what happened around an asset.

## How Points of Interest work

Reveal evaluates asset activity against a behavioral baseline built from observed event data. When activity deviates from that baseline in a way that matches a PoI rule, Reveal creates a PoI entry on the asset timeline.

The baseline requires a minimum period of activity before PoIs can be generated. Assets with insufficient historical data or sparse telemetry may not produce PoIs.

!!! note "Data requirement"
    Points of Interest require behavioral event data. Authentication logs and identity provider logs are the primary sources. See [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md) for the full data source requirements.

## Types of Points of Interest

The following PoI types are currently available. Availability depends on the event data ingested for the asset.

| Point of Interest | Asset type | Description |
|---|---|---|
| Anomalous login time | User, host | Authentication occurred at an unusual time relative to the asset's baseline |
| Rare login location | User, host | Authentication originated from a location not previously observed for the asset |
| Anomalous login failure ratio | User, host | The ratio of failed to successful authentications deviates significantly from the baseline |

Additional PoI types are added as coverage expands.

## Where Points of Interest appear

PoIs are visible in two places:

- **Asset context panel, Timeline tab:** PoI entries appear inline with alerts and case associations, timestamped and labeled by type. Select a PoI entry to view its details.
- **Seen in (last 30 days) card:** The PoI counter shows the total number of PoIs observed for the asset over the last 30 days.

> 📸 [SCREENSHOT SUGGESTION: Asset timeline showing a PoI entry for anomalous login time between two alert entries, with a distinct PoI icon and timestamp. | ALT TEXT: Asset timeline with a Point of Interest entry visible between two alerts.]

## How to use Points of Interest during an investigation

PoIs are most useful when read in relation to surrounding alerts and events. A single PoI rarely requires action on its own. Its value increases when it connects to other signals.

Useful questions to ask when reviewing a PoI:

- Does this PoI precede or follow an alert on the same asset?
- Does this PoI appear on other assets involved in the same case?
- Does the deviation match a known attack technique such as off-hours access or credential stuffing?

??? example "Using PoIs to reconstruct an attack timeline"
    A user account triggers a *credential dumping* alert at 14:32. The asset timeline also shows a PoI for an anomalous login time at 12:15 and a rare login location PoI the previous evening. Together, these signals suggest the account was accessed by an unauthorized party several hours before the alert fired. This context changes the investigation scope and the recommended containment actions.

## Related links

- [Asset context panel](/xdr/features/investigate/asset_context_panel.md): How to access the timeline and interpret activity entries for an asset.
- [Asset context panel: Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md): Full reference for Reveal-specific sections of the asset context panel, including timeline enrichment.
- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md): How to configure the event data sources required for Points of Interest.
- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md): Data source requirements for each Reveal capability.
