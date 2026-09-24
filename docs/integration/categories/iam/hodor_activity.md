uuid: 85a8611f-5389-402a-bfa0-932718101fc4
name: Hodor Activity
type: intake

## Overview

Hodor manages identities and access to tools for AI agents through a Model Context Protocol (MCP) gateway. This integration collects tool-call activity sent by Hodor, including the workspace, actor, agent, provider, access contract, duration, and outcome when available.

- **Vendor**: Hodor
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: MCP tool-call activity

The integration supports Hodor's version 1 activity envelope. It covers calls recorded by Hodor's activity logger; it does not collect Hodor's separate administrative audit stream or all authentication and policy-denial events.

## Prerequisites

- A Hodor workspace with an agent and a configured tool connection.
- Permission to create an intake in the target Sekoia community.
- Assistance from the Hodor team to enable external delivery for your workspace.

Hodor sends events directly to Sekoia over HTTPS. No collector or polling connector is required.

## Configure

### Create the intake in Sekoia

1. Open **Intakes** in the Operations Center and click **New intake**.
2. Search for and select **Hodor Activity**.
3. Enter a name, select the entity, and save the intake.
4. Copy the intake key from the intake details page.

Allow time for a newly created intake to become available to the HTTPS collector before enabling delivery. During activation, the collector can temporarily reject the new key. When testing a new custom format, its parser may also take time to become available to the ingestion workers.

See [Manage intakes](/xdr/features/collect/manage_intakes.md) for more information.

### Enable delivery from Hodor

External delivery is currently configured with assistance from the Hodor team. Contact your Hodor representative with:

- The Hodor workspace or workspaces whose activity you want to collect.
- The Sekoia intake key, shared through your agreed secure channel.
- The **HTTP Intake** URL for your [Sekoia region](/getting_started/regions.md), including its path when one is listed. For FRA1, the URL is `https://intake.sekoia.io`.
- The desired payload mode, described below.

The Hodor team configures and enables the Sekoia destination and links the selected workspaces. Once active, new recorded tool calls are forwarded automatically. Historical activity is not backfilled automatically when a destination is enabled.

### Choose the payload mode

| Mode | Request and response bodies |
| --- | --- |
| `metadata` (default) | Omitted. Actor, agent, workspace, contract, action, and result metadata remain available. |
| `truncated` | Forwarded when present. A body whose serialized JSON exceeds 2,048 bytes is replaced by an object containing `_truncated`, `_bytes`, and a `preview` of the first 2,048 bytes. |
| `full` | Forwarded in full when present. |

Payload mode is configured per destination. Hodor applies its internal visibility rules before forwarding: `do_not_store` removes the bodies and `workspace_redacted` applies redaction. Bodies marked `owner_only` can still be exported when the destination uses `truncated` or `full`. Choose the destination mode accordingly. Metadata mode still includes identity information such as names and email addresses when available.

## Verify collection

1. After the Hodor team confirms activation, perform a tool call through an agent in a linked workspace.
2. Open Sekoia's [events page](/xdr/features/investigate/events.md), search for `sekoiaio.intake.uuid:"<intake UUID>"` using the UUID of your Hodor intake, and use a time range covering the call.
3. Verify the event timestamp, `event.action`, `organization.id`, `hodor.agent.id`, and `event.outcome` against the call in Hodor. Optional identity and contract fields may be absent.
4. Confirm that parsing succeeded and that request and response fields match the configured payload mode.

A metadata-only event is sufficient to verify collection. Successful collection does not require request or response bodies.

## Interpret the events

| Hodor value | Sekoia field | Meaning |
| --- | --- | --- |
| `occurred_at` | `@timestamp` | Time the activity occurred in Hodor. |
| `id` | `hodor.event_id` | Hodor event identifier, retained across delivery retries and replays. Sekoia assigns its own `event.id`. |
| `workspace` | `organization.id`, `organization.name` | Workspace attribution. |
| `actor` | `user.id`, `user.email`, `user.full_name`, `user.name` | Human profile associated with the call. `user.name` uses the name, falling back to the email address. |
| `agent` | `hodor.agent.*` | AI agent identity in Hodor. |
| `provider` | `service.name` | Tool provider used for the call. |
| `contract` | `hodor.contract.*` | Access contract associated with the call. |
| `action` | `event.action` | Recorded action, for example `/mcp/tools/search`. The tool name can be prefixed with the name of the tool connection in Hodor, for example `/mcp/tools/Linear__get_issue`. |
| `result.is_error` | `event.outcome` | `true` becomes `failure`, `false` becomes `success`, and an absent value becomes `unknown`. |
| `result.duration_ms` | `event.duration` | Call duration converted from milliseconds to nanoseconds. |
| `result.status_code` | `hodor.status_code` | Hodor's status used to attribute the result or fault. This can differ from the provider's HTTP status. |
| `result.error_message` | `error.message` | Error details when supplied by Hodor. |
| `payload.request`, `payload.response` | `hodor.request`, `hodor.response` | Optional bodies, subject to the payload mode and internal visibility rules. |

Use `event.outcome` to identify failed calls. A tool error can have `hodor.status_code = 200`, so a status of 200 alone does not establish success. A failed call alone also does not establish that a Hodor policy blocked it.

Hodor's status convention attributes provider refusals to 4xx codes, provider availability failures to 502, 503, or 504, and internal gateway errors to 500. The parser preserves the recorded code without interpreting it as a raw upstream HTTP response.

Retries or replays can produce more than one Sekoia event for the same Hodor activity. Use `hodor.event_id` to correlate those copies.

## Troubleshooting

| Symptom | Checks |
| --- | --- |
| No events arrive | Confirm that the destination is enabled, the workspace is linked, the intake key and regional URL match, and a new tool call has been recorded since activation. Ask the Hodor team to inspect delivery errors. |
| A newly created intake returns `Invalid intake key` | Verify the key and regional URL. If the intake was just created, allow time for activation, then retry with a new test event. |
| A new custom format reports `Cannot find a parser for event` | Confirm that the format contains the saved parser, allow time for activation, then verify a new event. The error can also affect an isolated event shortly after other events parsed successfully. Events that failed are not parsed again, so send a new event to check. A successful test in the parser editor alone does not verify the ingestion workers. |
| Events arrive but parsing fails | Verify that the intake uses **Hodor Activity** and that the event is a version 1 Hodor activity envelope. Share an anonymized failing event with support. |
| Request or response fields are missing | Check the destination's payload mode and the event's `hodor.payload_visibility`. Metadata mode and `do_not_store` omit the bodies. |
| Actor or contract fields are missing | These attributes are optional. Missing values do not prevent parsing the rest of the event. |

## Event samples and extracted fields

The following samples use synthetic data. They show the Hodor envelope received by the parser after the HTTPS intake removes its transport wrapper.

{!_shared_content/operations_center/integrations/generated/85a8611f-5389-402a-bfa0-932718101fc4_sample.md!}

{!_shared_content/operations_center/integrations/generated/85a8611f-5389-402a-bfa0-932718101fc4.md!}

## Further reading

- [Send events using HTTPS](/integration/ingestion_methods/https/overview.md)
- [Sekoia regions](/getting_started/regions.md)
