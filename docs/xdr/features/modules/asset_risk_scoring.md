# Asset risk scoring

Asset risk scoring gives each host and account asset a current security priority based on persistent exposure, recent asset-linked security activity, and configured asset criticality. The score helps you understand which assets need attention now and why, but it does not represent breach probability, compromise likelihood, or organization-wide security posture.

!!! note "Reveal requirement"

    Asset risk scoring requires the Reveal add-on module. The score is calculated per asset and includes a last updated timestamp.

## What the score represents

The Asset Risk Score is a hybrid prioritization score for a single asset. It combines technical exposure that remains unresolved, recent operational evidence linked to the asset, and the asset's business importance.

The score is designed to answer three questions:

- How urgent is this asset right now?
- Which persistent or recent signals are driving the priority?
- What change would reduce the score?

The asset context panel describes the score as a combination of relevant signals such as known vulnerabilities, alert activity, asset criticality, suspicious behavior, and other available context. The current breakdown groups these signals into **Exposure**, **Recent activity**, and **Criticality**.

The score does not replace vulnerability severity, alert severity, case priority, or asset criticality. These values remain available as separate signals so you can understand the reason for the final priority.

## How the score is calculated

The calculation has four stages:

1. Calculate the **Exposure Score**.
2. Calculate the **Recent Activity Score**.
3. Add both values to obtain the **Base Score**.
4. Apply the **Criticality Factor** to obtain the final Asset Risk Score.

The formulas are:

- `Base Score = Exposure Score + Recent Activity Score`
- `Asset Risk Score = min(100, Base Score × Criticality Factor)`

The score is rounded to the nearest whole number for display.

| Component | Maximum | What it represents |
| --- | ---: | --- |
| Exposure Score | 40 | Persistent vulnerability and hygiene exposure |
| Recent Activity Score | 40 | Recent cases, alerts, and Points of Interest |
| Base Score | 80 | Technical and operational priority before criticality |
| Asset Risk Score | 100 | Final priority after the criticality adjustment |

### Example calculation

An asset has an Exposure Score of `32` and a Recent Activity Score of `18`.

- Base Score: `32 + 18 = 50`
- Criticality Factor: `1.26`
- Asset Risk Score: `50 × 1.26 = 63`

The displayed result is **63, High**. The criticality adjustment increases the score because the asset has a high configured criticality.

> 📸 [SCREENSHOT SUGGESTION: Asset risk breakdown showing Exposure 32/40, Recent activity 18/40, Base score 50, Criticality x1.26, and Final score 63. | ALT TEXT: Asset risk breakdown with exposure, recent activity, base score, criticality factor, and final score.]

## Understand the score bands

The final score maps to one of four severity bands.

| Asset Risk Score | Severity band |
| ---: | --- |
| 0–24 | Low |
| 25–49 | Moderate |
| 50–74 | High |
| 75–100 | Critical |

The severity band describes the asset's current prioritization. It does not describe the severity of an individual vulnerability, alert, case, or Point of Interest.

## Understand the Exposure Score

The Exposure Score contains persistent signals that remain relevant until their state changes or the platform stops receiving confirmation.

`Exposure Score = Vulnerability Contribution + Hygiene Contribution`

Exposure is capped at `40`.

> 📸 [SCREENSHOT SUGGESTION: Exposure tooltip showing that the score is calculated from Vulnerabilities and Hygiene, is capped at 40, and requires confirmation within the last 30 days. | ALT TEXT: Exposure score tooltip describing vulnerability, hygiene, cap, and confirmation rules.]

A persistent signal continues contributing while it has been confirmed within the previous 30 days. If the platform does not receive a confirmation for more than 30 days, the signal is treated as no longer confirmed and contributes `0` until it is confirmed again.

A signal becoming no longer confirmed does not prove that the issue was remediated or validated by an analyst. The change remains visible in the asset history so you can distinguish an expired confirmation from a remediation action.

### Vulnerability contribution

Only open, confirmed vulnerabilities contribute to the score. The contribution is based on the vulnerability's Common Vulnerability Scoring System (CVSS) score.

| CVSS score | Contribution per vulnerability |
| ---: | ---: |
| 9.0–10.0 | 10 |
| 7.0–8.9 | 6 |
| 4.0–6.9 | 3 |
| 0.1–3.9 | 1 |
| Missing or invalid | 0 |

The total vulnerability contribution is capped at `24`.

A vulnerability contributes `0` from the relevant decision or resolution timestamp forward when it is in one of the following states:

- Accepted Risk.
- False Positive.
- Resolved or another remediated state.

### Hygiene contribution

Hygiene applies only when the control is relevant to the asset type.

| Hygiene condition | Contribution |
| --- | ---: |
| Firewall disabled | 4 |
| Storage encryption disabled or absent | 4 |
| Enabled or safe state | 0 |
| Unsupported or non-applicable control | 0 |

The total hygiene contribution is capped at `8`. Hygiene findings follow the same 30-day confirmation rule as vulnerabilities.

## Understand the Recent Activity Score

The Recent Activity Score represents time-sensitive operational evidence linked to the asset. It includes:

- Cases.
- Alerts.
- Points of Interest.

Recent Activity is capped at `40`. Contributions decay according to the lifecycle and age of each signal.

> 📸 [SCREENSHOT SUGGESTION: Recent activity tooltip showing that the score is calculated from cases, alerts, and POIs, is capped at 40, and represents time-sensitive activity. | ALT TEXT: Recent activity tooltip describing cases, alerts, POIs, and the score cap.]

When a case is linked to an alert, the case takes precedence. The case contributes according to the case rules, and the linked alert contributes `0`. Reinforcement of an already correlated signal refreshes its timer but does not create another full-strength contribution.

### Case contribution

Case contributions depend on priority and lifecycle state.

| Case priority | Base contribution |
| --- | ---: |
| Low | 8 |
| Medium | 12 |
| High | 16 |
| Critical | 20 |

| Case state or condition | Contribution behavior |
| --- | --- |
| Open, up to 14 days from creation or latest update | 100% of base value |
| Open, more than 14 days without an update | 50% of base value |
| Open, more than 30 days without an update | 0 |
| Closed | 50% of base value for 7 days, then 0 |
| Closed and True positive | 50% of base value for 14 days, then 0 |
| False positive | 0 immediately |

The total case contribution is capped at `20`.

### Alert contribution

Alert contributions depend on severity and lifecycle state.

| Alert severity | Base contribution |
| --- | ---: |
| Informational | 1 |
| Low | 2 |
| Medium | 4 |
| High | 6 |
| Critical | 8 |

| Alert state or condition | Contribution behavior |
| --- | --- |
| Pending, up to 7 days from creation or latest meaningful update | 100% of base value |
| Pending, more than 7 days without a meaningful update | 50% of base value |
| Pending, more than 14 days without a meaningful update | 0 |
| Closed | 25% of base value for 3 days, then 0 |
| Closed and True positive | 25% of base value for 7 days, then 0 |
| False positive | 0 immediately |
| Superseded by a linked case | 0 |

The total alert contribution is capped at `14`.

### Point of Interest contribution

Points of Interest use the same severity labels as alerts for internal calibration. Their severity does not imply that a Point of Interest is equivalent to an alert or case of the same severity.

| Point of Interest severity | Base contribution |
| --- | ---: |
| Informational | 0.5 |
| Low | 1 |
| Medium | 2 |
| High | 3 |
| Critical | 4 |

A Point of Interest contributes its full base value for seven days from creation. It contributes 50% of its base value for the following seven days, then contributes `0`. Reinforcement refreshes the timer but does not stack a second full-strength contribution for the same correlated signal.

The total Point of Interest contribution is capped at `6`.

## Understand the Criticality Factor

Asset criticality is a business-context modifier applied after the Base Score is calculated. It can reduce, leave unchanged, or increase the final score.

A criticality value of `0` means **Default**. It applies a factor of `1.00`, so it does not change the Base Score.

| Criticality value | Label | Factor range |
| ---: | --- | ---: |
| 0 | Default | 1.00 |
| 1–24 | Low | 0.80–1.00 |
| 25–49 | High | 1.05–1.12 |
| 50–74 | Severe | 1.13–1.22 |
| 75–100 | Critical | 1.23–1.35 |

The platform uses linear interpolation within each range.

- `0` → `1.00`
- `1–24` → `0.80 + 0.20 × ((criticality - 1) / 23)`
- `25–49` → `1.05 + 0.07 × ((criticality - 25) / 24)`
- `50–74` → `1.13 + 0.09 × ((criticality - 50) / 24)`
- `75–100` → `1.23 + 0.12 × ((criticality - 75) / 25)`

The criticality adjustment is calculated as:

`Criticality Adjustment = Asset Risk Score - Base Score`

The overview can also identify the dominant component, for example, **Score mostly driven by: Exposure (51%)**. This highlights which part of the breakdown deserves attention first.

Criticality does not add technical evidence. A high criticality increases business priority, while a low criticality reduces prioritization. The underlying exposure and activity remain visible in the Base Score and its breakdown.

> 📸 [SCREENSHOT SUGGESTION: Criticality factor tooltip showing the 0–100 criticality range, the five criticality bands, and their linear factor ranges. | ALT TEXT: Criticality factor tooltip describing criticality bands and multiplier ranges.]

## Follow score changes over time

The asset context panel provides two complementary views:

- The **Timeline** tab lists meaningful score-driving signal changes.
- The **Risk score trajectory** graph shows the Asset Risk Score over time.

Timeline entries can include vulnerability state changes, hygiene changes, alert and case lifecycle changes, Point of Interest creation or expiration, and criticality changes. The **Related events** tab provides the associated event records separately from the score trajectory. An entry shows the timestamp, signal type, state change, and whether the change increased, reduced, or removed the signal's contribution.

The trajectory graph shows the Asset Risk Score on the Y-axis and time on the X-axis. It reflects exposure, recent activity, and criticality changes without adding a marker for every score recalculation.

> 📸 [SCREENSHOT SUGGESTION: Timeline tab showing the Risk score trajectory graph above timeline entries for vulnerabilities, alerts, cases, and Points of Interest. | ALT TEXT: Asset timeline with a risk score trajectory and contributing security events.]


## Related articles

- [Asset context panel](/xdr/features/investigate/asset_context_panel.md): Overview of the asset investigation surface and its core tabs.
- [Asset context panel, Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md): Overview of Reveal-specific asset context, including hygiene, vulnerabilities, Points of Interest, and security controls.
- [Assets](/xdr/features/collect/assets.md): Reference for asset categories, criticality, and asset management.
- [Interpret asset risk scores](/xdr/features/modules/interpret_asset_risk_scores.md): How to read and use the score during an investigation.
