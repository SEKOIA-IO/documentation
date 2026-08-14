---
uuid: 1540e5d1-e475-5b21-b774-689de0cb941e
name: BlackNoise AEV
type: intake
---

## Overview

BlackNoise is an agentless Adversarial Exposure Validation (AEV) platform. It safely executes real attack techniques across the information system and correlates each adversarial action with the detections it triggered, so security teams can measure and continuously improve their real MTTD and MTTR.

Once the connector is configured, BlackNoise forwards every adversarial action it executes to a Sekoia intake, as soon as the action finishes running. Your simulation activity then sits next to your real telemetry: you can search it, correlate it with your detections, and confirm that what BlackNoise executed was actually visible to your SOC. Each action displayed in BlackNoise also links to the matching event in Sekoia.

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

The configuration alternates between the two products: you set the Sekoia URL in BlackNoise, create the intake in Sekoia, then bring its intake key back to BlackNoise.

### Prerequisites

- A BlackNoise account belonging to a company allowed to use connectors. The connector is configured once per company and is then available to all its campaigns.
- A Sekoia account allowed to create intakes.

### Set the Sekoia API URL in BlackNoise

1. Log in to BlackNoise
2. In the `Resources` section of the navigation, open `Connectors`
3. On the `Sekoia` connector, click `Configure` — the `Edit connector` window opens
4. Fill the `API URL` field with the API base URL of your region: `https://api.sekoia.io` for FRA1, `https://app.<region>.sekoia.io/api` otherwise
5. Leave `Intake Key` empty for now, it is created in the next step
6. Click `Save and connect` and check that the result reported is a success, not an error

![connector_api_url.png](/assets/integration/application/blacknoise/connector_api_url.png)

!!! note
    This URL is the only Sekoia address BlackNoise asks you for: it derives the intake it pushes to (`https://intake.sekoia.io/batch` for FRA1, `https://intake.<region>.sekoia.io/api/v1/intake-http/batch` otherwise) and the links displayed on your adversarial actions from it. The result message lists both derived addresses, so check them to confirm that BlackNoise is aimed at your region. Regions and their codes are listed in [our dedicated article](/getting_started/regions.md).

!!! warning
    The expected value is the API base URL, not a page of the Sekoia web application: an address such as `https://app.sekoia.io/intakes/…` is rejected by the connection test.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

Search the intake catalog for `BlackNoise` and select the `BlackNoise AEV` format, then attach the intake to the entity your adversarial actions belong to.

Once the intake is created, copy the `Intake key` displayed in the intake details window before closing it: the next step needs it.

### Set the intake key in BlackNoise

1. Back in BlackNoise, open `Resources` > `Connectors` and click `Configure` on the `Sekoia` connector again
2. Paste the key copied above in the `Intake Key` field, leaving the `API URL` untouched
3. Click `Save and connect`

![connector_intake_key.png](/assets/integration/application/blacknoise/connector_intake_key.png)

BlackNoise now reports two results instead of one: the `API URL`, whose form is validated without sending any request, and the `Intake connection`, which is validated by ingesting one test event into your intake.

!!! note
    The intake exposes no dry-run endpoint, so that test event is a real event in your tenant. It carries no campaign, simulation or target, and is filtered out with `blacknoise.execution_id:"connector-healthcheck"` or found with `rule.name:"BlackNoise connector healthcheck"`.

### Run a campaign with the connector

1. Create a campaign as usual, with the Attack Vector that executes the techniques and the System Targets they run against
2. In the connectors step of the campaign, select `Sekoia`
3. Launch the simulation

![campaign_connectors.png](/assets/integration/application/blacknoise/campaign_connectors.png)

Only the campaigns the connector is selected on forward their events. Each event is sent as soon as its action finishes executing, so events arrive during the campaign run rather than at its end.

### Check that events are arriving

Open the intake you created, or the [Events page](https://app.sekoia.io/operations/events) filtered on `event.dataset:blacknoise.simulation`: you should see one event per executed adversarial action.

Useful filters:

| To see | Filter |
| --- | --- |
| Everything sent by BlackNoise | `event.dataset:blacknoise.simulation` |
| Adversarial actions only | `event.action:simulation_event` |
| One campaign | `blacknoise.campaign_id:"<campaign id>"` |
| One adversarial action | `trace.id:"<execution id>"` |
| One target | `host.ip:"<target ip>"` |
| One MITRE ATT&CK technique | `threat.technique.id:"<technique>"` |

To jump to the Sekoia event of a given action without typing its identifier, open the campaign in BlackNoise, go to its `Kill chain` tab, click the action, then scroll down to the `Connectors` section of the panel and click `View this event in Sekoia`. The link opens Sekoia filtered on that execution identifier and on the execution window.

![event_connectors_link.png](/assets/integration/application/blacknoise/event_connectors_link.png)

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/1540e5d1-e475-5b21-b774-689de0cb941e_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_1540e5d1-e475-5b21-b774-689de0cb941e_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/1540e5d1-e475-5b21-b774-689de0cb941e.md!}
