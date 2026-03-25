# Points of interest

**[Reveal module](reveal_index.md)** — This feature requires the Reveal add-on module.

Points of interest (PoIs) are behavioral investigation signals surfaced in the asset context panel to help analysts assess whether an asset is associated with unusual or otherwise meaningful activity. A PoI provides context to support analyst judgment; it does not by itself confirm malicious activity.

> 📸 [SCREENSHOT SUGGESTION: Asset context panel timeline tab or overview showing a point of interest entry with its type label and timestamp. | ALT TEXT: Asset context panel showing a point of interest entry in the timeline.]

## Prerequisites

To benefit from points of interest:

- Reveal must be enabled on your community.
- Relevant authentication telemetry must be ingested.
- Enough historical data must exist for the underlying rules to operate meaningfully.

!!! note "Limited history or telemetry"
    If telemetry is incomplete or historical data is limited, PoIs may be absent or less useful. Newly onboarded environments and low-volume entities may not generate PoIs immediately.

## Where points of interest appear

Points of interest are displayed in the [asset context panel](asset_context_panel.md). This allows analysts to review them while triaging a case, reviewing an asset, investigating related alerts or events, or building context before deciding whether escalation is needed. Displaying PoIs in the asset context panel reduces context switching and keeps behavioral context close to the entity under review.

## Types of points of interest

Reveal currently supports two categories of PoI:

- **User and entity behavior analytics (UEBA)** — Available now. Surfaces unusual or rare login-related behavior on accounts and hosts.
- **Notable activities** — Coming soon. Will expand the PoI experience by surfacing meaningful activity patterns beyond anomaly-driven signals.

### UEBA points of interest

UEBA-based PoIs highlight behavior that stands out when compared with previously observed activity. They help analysts identify activity that may be difficult to spot from alerts or events alone.

**Current UEBA rules**

| Rule name | Type | Scope | Key parameters | What it helps detect |
|---|---|---|---|---|
| Anomalous login time by user | Anomaly (volume) | User | 35-day history, weekday/weekend merge, minimum 10 data points | A user authenticating outside their normal time pattern |
| Anomalous login time on host | Anomaly (volume) | Host | 35-day history, weekday/weekend merge, minimum 10 data points | A host associated with authentication activity at unusual times |
| Rare login location by user | Novelty | User | 35-day history, country field = `client_country_iso_code` | A user logging in from a country not previously observed in the historical window |
| Rare login location on host | Novelty | Host | 35-day history, country field = `client_country_iso_code` | A host associated with logins from a rare or previously unseen country |
| Anomalous login failure ratio by user | Anomaly (ratio) | User | Ratio target = failure, 35-day history, minimum 10 data points | A user showing an unusual increase in failed authentication attempts |
| Anomalous login failure ratio on host | Anomaly (ratio) | Host | Ratio target = failure, 35-day history, minimum 10 data points | A host showing an unusual increase in failed authentication attempts |

### Notable activities

**Coming soon.** Notable activities will surface meaningful activity patterns that are useful during triage and investigation, even when those patterns are not strictly anomaly-based. This capability will complement UEBA by broadening the types of behavior surfaced in the asset context panel.

## Interpret a point of interest

A PoI should be interpreted as context for investigation, not as a verdict.

Depending on its type, a PoI may indicate:

- a deviation from previously observed behavior
- a rare or previously unseen pattern
- a meaningful activity pattern that warrants review alongside stronger signals

**A PoI is not the same as:**

- a confirmed incident
- an alert verdict
- a detection that always requires escalation

PoIs are most useful when reviewed together with cases, alerts, related events, risk and exposure context, identity or host context, and known business or operational activity.

??? example "Contextual triage scenario"
    An alert fires on an asset. The same asset also shows a PoI for an unusual login time and another for a rare login location. These signals together may indicate compromised credentials with remote access from an unfamiliar country — a pattern that warrants escalation. Individually, each signal may have a benign explanation.

## What current UEBA PoIs can indicate

Current UEBA PoIs are login-focused and can help surface behaviors such as:

- a user authenticating at an unusual time
- a host associated with logins outside its typical activity pattern
- a user logging in from a country not previously observed
- a host suddenly showing logins from a rare location
- an unusual increase in failed login attempts for a user
- an unusual increase in failed login attempts associated with a host

These behaviors may indicate compromised credentials, suspicious remote access, password spray or brute-force attempts, broken service credentials or automation, infrastructure changes, or legitimate travel and changes in working patterns.

!!! warning "Always review PoIs in context"
    Because the same signal can have both benign and suspicious explanations, PoIs must always be reviewed alongside other investigation evidence. Treat PoIs as decision-support signals, not standalone evidence.

## Limitations

Keep the following in mind when using points of interest:

- PoIs depend on available telemetry and observed history.
- Newly onboarded environments may not generate PoIs immediately.
- Low-volume entities may not meet the minimum data threshold required by underlying rules.
- Novelty-based signals may reflect legitimate travel, VPN use, or infrastructure changes.
- Anomalous login failure ratios may be caused by expired passwords, broken scripts, or misconfigured services.

## Related links

- [Asset context panel](asset_context_panel.md) — Full reference for the asset context panel, where points of interest appear in the timeline and overview sections.
- [Attack path visualization](attack_path_visualization.md) — How to assess potential lateral movement paths from an asset, complementing the behavioral context provided by PoIs.
- [Detection — IOC detection](https://docs.sekoia.io/xdr/features/detect/iocdetection/) — Overview of detection capabilities in Sekoia, including rule-based and analytics-driven approaches that PoIs complement.
