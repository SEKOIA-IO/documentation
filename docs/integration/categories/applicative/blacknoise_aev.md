---
uuid: 1540e5d1-e475-5b21-b774-689de0cb941e
name: BlackNoise AEV
type: intake
---

## Overview

BlackNoise is an agentless Adversarial Exposure Validation (AEV) platform. It safely executes real attack techniques across the information system and correlates each adversarial action with the detections it triggered, so security teams can measure and continuously improve their real MTTD and MTTR.

This integration works in both directions: BlackNoise forwards the adversarial actions it executes to Sekoia, and reads back the alerts Sekoia raised, so that every action carries the evidence of whether the defensive stack caught it.

- **Vendor**: BlackNoise
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Application logs

The intake carries two kinds of record, published on the same intake and told apart by `event.action`:

| `event.action` | Record | Description |
| --- | --- | --- |
| `simulation_event` | Adversarial action | One attack technique executed against a target, with its outcome and the detections it triggered |
| `ioc` | Indicator of compromise | One indicator produced by an action, tied back to it through `trace.id` |

## Step-by-Step Configuration Procedure

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

Keep the intake key at hand: the next step needs it.

### BlackNoise forwarding configuration

<!-- TODO: replace the labels below with the real ones, and add the screenshots in
     docs/assets/integration/application/blacknoise/ -->

1. Log in to the BlackNoise console
2. Go to `Settings > Connectors`
3. Select `Sekoia`
4. Paste the intake key from the previous step in the `Intake key` field
5. Click `Save`

!!! warning
    BlackNoise sends events to `https://intake.sekoia.io/plain`, which is the FRA1 endpoint. If your community is hosted in another region, set the endpoint to `https://intake.<region>.sekoia.io/api/v1/intake-http/plain`. Regions and their codes are listed in [our dedicated article](/getting_started/regions.md).

### Read Sekoia alerts back in BlackNoise

This step is optional for ingestion, but it is what lets BlackNoise report whether an adversarial action was detected.

1. In Sekoia, create an API key from the [API keys page](/getting_started/manage_api_keys.md), with the permissions to read alerts and events
2. In the BlackNoise console, go to `Settings > Connectors` and select `Sekoia`
3. Fill the two fields:
    - **API URL**: `https://api.sekoia.io` for FRA1, or the API base URL of your region
    - **API Key**: the key created above
4. Click `Save`. The connector reports `Your connector is now connected!` once the credentials are validated

### Check that events are arriving

To validate the forwarding before running a real campaign, push one event by hand:

```bash
curl -X POST https://intake.sekoia.io/plain \
     -H "X-SEKOIAIO-INTAKE-KEY: REPLACE_BY_INTAKE_KEY" \
     -H "Content-Type: text/plain" \
     --data-binary '{"id": "c9f0f895-fb98-4b91-9f2b-3c4d5e6f7a11", "event_bn_id": "BLCKNS_DIS_N0002.001", "name": "Network Share Discovery", "execution_status": "executed", "start_time": "2026-01-20T21:10:00+00:00"}'
```

The endpoint answers `{"event_id": "…"}`. The event shows up on the Events page within a minute, with `event.action: simulation_event`.

For volume, BlackNoise uses the `/plain/batch` endpoint, one JSON record per line. See the [formatting options](/integration/ingestion_methods/https/format.md) for the details.

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/1540e5d1-e475-5b21-b774-689de0cb941e_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_1540e5d1-e475-5b21-b774-689de0cb941e_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/1540e5d1-e475-5b21-b774-689de0cb941e.md!}
