# Create an Event Drop rule from an intake or asset

You can create an Event Drop detection rule directly from an intake or an asset, without starting from a blank rule in the catalog. The rule creation panel opens with the Event Drop pattern selected and the SOL pattern pre-filled with a condition on the source, so you only set the schedule and create the rule.

## Prerequisites

- You have permissions to create detection rules.
- You are on the details page of the intake or asset you want to monitor for missing data.

## Start from an intake

To create an Event Drop rule that monitors a specific intake:

1. Open the details page of the intake.
2. Open the more options menu (the `...` button) in the intake header.
3. Select **Create event drop alerting**.

The **Create new rule** panel opens with the **Event Drop** pattern selected. The rule name is set to `Event drop for intake "<intake name>"`, and the pattern targets the intake UUID:

```
event_telemetry
| where timestamp between (?time.start .. ?time.end)
| aggregate count() by bin(timestamp, 2h)
| where intake_uuid == "<intake uuid>"
| where count < 500
```

4. Adjust the time bin and the threshold if the defaults do not match the intake's expected volume.
5. Set the schedule and complete any remaining fields.
6. Click **Create**.

![Intake actions menu with Create event drop alerting](/assets/operation_center/rules_catalog/sol-intake-drop.png){: style="max-width:100%"}

![Pre-filled Event Drop rule panel for an intake](/assets/operation_center/rules_catalog/sol-intake-drop-panel.png){: style="max-width:100%"}

## Start from an asset

To create an Event Drop rule that monitors a specific asset:

1. Open the details page of the asset.
2. Click **Configure an event drop alert**.

The **Create new rule** panel opens with the **Event Drop** pattern selected. The rule name is set to `Event drop for asset "<asset name>"`, and the pattern targets the asset UUID:

```
asset_telemetry
| where timestamp between (?time.start .. ?time.end)
| aggregate count() by bin(timestamp, 1d)
| where asset_uuid == "<asset uuid>"
| where count < 1000000
```

3. Adjust the time bin and the threshold if the defaults do not match the asset's expected volume.
4. Set the schedule and complete any remaining fields.
5. Click **Create**.

![Asset details with the Configure an event drop alert button](/assets/operation_center/rules_catalog/sol-asset-drop.png){: style="max-width:100%"}

![Pre-filled Event Drop rule panel for an asset](/assets/operation_center/rules_catalog/sol-asset-drop-panel.png){: style="max-width:100%"}

## What gets pre-filled

The entry point determines the rule name, the datasource and the field used in the condition:

| Source | Entry point | Rule name | Datasource | Condition field | Default bin |
|---|---|---|---|---|---|
| Intake | **Create event drop alerting** in the intake more options menu | `Event drop for intake "<name>"` | `event_telemetry` | `intake_uuid` | 2 hours |
| Asset | **Configure an event drop alert** button on the asset page | `Event drop for asset "<name>"` | `asset_telemetry` | `asset_uuid` | 1 day |

Both pre-filled patterns also bound the query with `?time.start` and `?time.end`, the time conditions required by every SOL rule.

!!! note "Tune the defaults"
    The pre-filled threshold and time bin are starting points. Set them to values that reflect the normal telemetry volume of the intake or asset, so the rule alerts only when the data drop is meaningful.

## Complete and create the rule

Once the panel is open, scheduling and the remaining fields work exactly as in the standard creation flow. For the full description of each field and the run schedule, see [Create a SOL detection rule](/xdr/features/detect/create_sol_detection_rule.md).

## Related articles

* [Create a SOL detection rule](/xdr/features/detect/create_sol_detection_rule.md): Step-by-step instructions to configure and activate a SOL or Event Drop detection rule from the catalog.
* [SOL detection rules](/xdr/features/detect/sol_detection_rule.md): Conceptual overview of the SOL and Event Drop detection patterns, how they work, and when to use them.
* [Lag management for SOL detection rules](/xdr/features/detect/sol_detection_lag_management.md): How rules handle late-arriving events through a fixed run overlap and deduplication.
