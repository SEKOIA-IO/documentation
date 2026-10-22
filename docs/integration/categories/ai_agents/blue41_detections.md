uuid: 547aa49e-c29a-4dbf-992b-c5cc0db19f17
name: Blue41 Detections and Audit
type: intake

## Overview

Blue41 secures AI agents at runtime. This integration collects two Blue41 streams: detections, as firing, no-data and resolve transitions, and the audit trail of configuration, access-control and data-access actions on the Blue41 platform.

- **Vendor**: Blue41
- **Supported environment**: Blue41-hosted (a dedicated deployment per customer) or self-hosted
- **Detection based on**: Alert, Audit
- **Supported application or feature**: AI agent detections, platform audit trail

The full trace history stays in Blue41. Each event's `event.url` links back to it: the trace and span for a detection, the rule overview when no single span applies, or the audit log for an audit record.

## Prerequisites

- A Blue41 deployment.
- Permission to create an intake in the target Sekoia community.

Blue41 sends events directly to Sekoia over HTTPS. No collector or polling connector is required.

## Configure

### Create the intake in Sekoia

1. Open **Intakes** in the Operations Center and click **New intake**.
2. Search for and select **Blue41 Detections and Audit**.
3. Enter a name, select the entity, and save the intake.
4. Copy the intake key from the intake details page.

Allow time for a newly created intake to become available to the HTTPS collector before enabling delivery. During activation, the collector can temporarily reject the new key.

See [Manage intakes](/xdr/features/collect/manage_intakes.md) for more information.

### Enable delivery from Blue41

For a deployment hosted by Blue41, send the Blue41 team the intake key through your agreed secure channel, along with your [Sekoia region](/getting_started/regions.md) if it is not FRA1. The Blue41 team configures delivery.

For a self-hosted deployment, set these variables on the Blue41 platform:

| Variable | Value |
| --- | --- |
| `SEKOIA__INTAKE_KEY` | The intake key. |
| `SEKOIA__INTAKE_URL` | `https://intake.sekoia.io/batch` for FRA1. For other regions, `https://intake.<region>.sekoia.io/api/v1/intake-http/batch`. |
| `EXPORT__UI_BASE_URL` | The base URL of your Blue41 deployment. Without it, events carry no `event.url`. |

Once delivery is enabled, new detections and audit records are forwarded automatically. Earlier activity is not backfilled.

## Create the detection rules

Blue41 detections arrive as events. A Sekoia alert is raised only when an event matches a detection rule.

Severity is set on a Sekoia rule, not on the matched event, so create one rule per Blue41 severity band. Request the Sigma rule definitions from Blue41. Each one matches on `event.dataset` set to `blue41.detection`, `event.kind` set to `alert`, and the `event.severity` of its band:

| Blue41 severity | `event.severity` | Rule |
| --- | --- | --- |
| critical | `99` | critical rule |
| error | `75` | error rule |
| warning | `50` | warning rule |
| info | `25` | info rule |

Detections with no Blue41 severity, such as no-data detections, or with any other value score `25` and match the info rule.

Set the [similarity strategy](/xdr/features/detect/rules_catalog.md#custom-similarity-strategy) of each rule to `rule.id` and `blue41.alert.fingerprint`. Blue41 detections carry no `source.ip` or `destination.ip`, so default similarity groups all detections of a severity band into one Sekoia alert. With these two fields, each Blue41 rule and matched span gets its own alert, and re-fires are added to it as occurrences while it is open.

See [Create custom rules](/xdr/features/detect/rules_catalog.md#create-custom-rules) for more information.

## Verify collection

1. Trigger a detection in Blue41, or perform an audited action such as updating an alert rule.
2. Open Sekoia's [events page](/xdr/features/investigate/events.md), search for `sekoiaio.intake.uuid:"<intake UUID>"` using the UUID of your Blue41 intake, and use a time range covering the activity.
3. Verify the event timestamp, `event.action`, `rule.name` (detections) or `user.name` (audit records), and `event.url` against the activity in Blue41.
4. For a firing or no-data detection, check that the matching rule raised one Sekoia alert.

A resolve appears on the events page but never raises a second alert.

## Interpret the events

`event.dataset` separates the two streams: `blue41.detection` for detections and `blue41.audit` for audit records.

| Event | `event.kind` | `event.action` | `event.outcome` |
| --- | --- | --- | --- |
| Detection fires | `alert` | `alert-fired` | `unknown` |
| Detection fires because data stopped arriving | `alert` | `alert-no-data` | `unknown` |
| Detection resolves | `event` | `alert-resolved` | `unknown` |
| Audit record | `event` | The audited verb, for example `create`, `read`, `update` or `delete` | `success` or `failure` |

`log.level` carries the Blue41 severity, and `event.severity` its score. `rule.id` and `rule.name` identify the Blue41 rule. `trace.id` and `span.id` identify the matched trace and span.

Blue41 maps AI agent concepts onto these ECS fields so Sekoia can build assets and the investigation graph:

| Field | Meaning |
| --- | --- |
| `host.name` | The AI agent. |
| `process.name` | The tool the agent called. |
| `destination.domain` | The flagged domain, for example a link returned by a tool. |

Audit records carry the actor in `user.id`, `user.email` and `user.name`, and the client in `source.ip` and `user_agent.original`.

The format adds these custom fields:

| Field | Meaning |
| --- | --- |
| `blue41.event_id` | Blue41 event identifier, stable across redeliveries. Sekoia assigns its own `event.id`. |
| `blue41.alert.fingerprint` | Identifies what the detection matched, such as a span. Two rules matching the same span share a fingerprint, so pair it with `rule.id`. |
| `blue41.actor.type` | Principal that performed an audited action: `user`, `service_account`, `system` or `anonymous`. |
| `blue41.audit.resource_kind` | Kind of resource the audited action targeted, for example `rule`, `dashboard` or `session`. |
| `blue41.audit.resource_id` | Identifier of the resource the audited action targeted. |

A resolve carries the same `rule.id` and `blue41.alert.fingerprint` as the detection it closes. Correlate them on those two fields.

## Troubleshooting

| Symptom | Checks |
| --- | --- |
| No events arrive | Confirm that the intake key and regional URL match, and that a detection or audit record has occurred since delivery was enabled. On a Blue41-hosted deployment, ask the Blue41 team to check delivery errors. |
| Sekoia returns a `422` response with `INVALID_INTAKE_KEY` | Verify the key and regional URL. If the intake was just created, allow time for activation. Blue41 retries delivery. On a Blue41-hosted deployment, ask the Blue41 team to check delivery errors. |
| Events arrive but parsing fails | Check that the intake uses **Blue41 Detections and Audit**. Share an anonymized failing event with support. |
| Events arrive but no alert is raised | Check that a detection rule matches the event's `event.severity` and is enabled. Resolves never raise alerts. |
| Several Blue41 detections share one Sekoia alert | Set the rule's similarity strategy to `rule.id` and `blue41.alert.fingerprint`. |
| `event.url` is missing | On a self-hosted deployment, set `EXPORT__UI_BASE_URL`. |

## Event samples and extracted fields

The following samples use synthetic data.

{!_shared_content/operations_center/integrations/generated/547aa49e-c29a-4dbf-992b-c5cc0db19f17_sample.md!}

{!_shared_content/operations_center/integrations/generated/547aa49e-c29a-4dbf-992b-c5cc0db19f17.md!}

## Further reading

- [Send events using HTTPS](/integration/ingestion_methods/https/overview.md)
- [Sekoia regions](/getting_started/regions.md)
- [Alert similarity](/xdr/features/investigate/alerts.md#alert-similarity)
