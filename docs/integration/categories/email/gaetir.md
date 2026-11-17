uuid: 0a7d3eed-4f64-4223-99e3-c5b1ce763189
name: GAETIR Email Security
type: intake

## Overview

GAETIR produces email security decisions and observations of mailbox feedback.
This integration normalizes `gaetir.decision.v2` and `gaetir.feedback.v1` events.

- **Vendor**: GAETIR
- **Detection based on**: Email security decisions and observed mailbox activity
- **Type of integration**: Outbound HTTPS PUSH from GAETIR to Sekoia.io
- **Data source**: Email gateway

## Architecture

GAETIR applies its disclosure settings before transmitting events over verified HTTPS.
The Sekoia intake authenticates each request, the parser normalizes the event, and
enabled detection rules can create alerts. Smart Descriptions summarize the evidence.
No Python polling connector or access to GAETIR application source is required.

## Prerequisites

- A GAETIR evaluation build with Sekoia HTTPS delivery (candidate v1.3.313). This candidate has passed isolated local checks; hosted availability remains pending the agreed evaluation.
- Permission to configure GAETIR's test event feed and the corresponding Sekoia intake.
- Network access to the FRA1 Sekoia HTTPS intake endpoint supported by this implementation.
- A Sekoia intake key stored privately by the sender.

## Sekoia configuration

For development review, create the GAETIR custom format with the supplied parser,
44 custom field definitions and Smart Descriptions. Save the main format after editing
fields. Create an intake associated with the designated test entity and copy its key
into private sender configuration. Leave the polling connector selection empty.
After catalog publication, select GAETIR Email Security from the intake catalog.

Use the provided six companion rules only in the intended entity scope. Group by
`gaetir.tenant_id` and `gaetir.event_id`; use the supplied rule settings and severities.
Creating a parser or setting `event.kind` does not itself enable a detection rule.

## GAETIR configuration

**Review status:** these instructions describe candidate v1.3.313. Local checks on
12 November 2026 covered application startup with a synthetic PostgreSQL database,
feed settings, a masked intake key, disclosure controls, desktop/mobile browser behavior
and HTTPS delivery to a controlled local receiver. Graph and CILL were disabled for
those checks. Hosted availability, Microsoft 365 evaluation and Sekoia homologation
remain pending; this candidate has not been published or deployed.
If the Sekoia mode is absent, obtain that build; changing the generic webhook URL/token
alone does not provide this protocol.

1. Sign in to the designated GAETIR evaluation installation with an authorized
   work/school account. Open its Live feed settings and keep the feed disabled during setup.
2. Select **Connect Sekoia**, or choose **Sekoia HTTPS (FRA1)** from the Mode list. The displayed endpoint is
   `https://intake.sekoia.io/jsons (FRA1)`. This implementation fixes that endpoint;
   it does not expose a regional endpoint selector. Agree a FRA1 intake for this evaluation.
3. Enter the key for that intake into **Sekoia intake key**. This is the intake key,
   not a Sekoia management API key. The password field does not display a saved key.
4. Select the intended event coverage and disclosure controls for addresses, subject,
   explanation, indicators and attachment metadata. Begin with synthetic test content.
   Save the settings. **Configured** confirms that the configuration was saved; it does not verify delivery. **Configured · feed paused** indicates that the feed remains disabled. Saving does not create an intake or send a test event. No mailbox selection or activation is performed by these settings.
5. Reopen the settings. A retained key is indicated by **Key saved; leave blank to keep it**.
   A blank key entry preserves the existing key; it does not delete it. To rotate the
   key, paste the replacement key and save. Keep keys out of screenshots and support exports.
6. When the separately agreed evaluation mailboxes and test activity are ready, enable
   the feed and save. Only permitted events produced by GAETIR under the chosen coverage
   and disclosure settings are transmitted. Enabling the feed is not historical replay.
7. Inspect GAETIR delivery diagnostics and the Sekoia intake's Valid, Warning and Invalid
   results. A `Live feed Sekoia HTTP accepted` entry records HTTP acceptance only.
   Check normalized fields, Smart Description and the expected alert/no-alert outcome
   using the source `gaetir.event_id`. Do not mistake Sekoia's own `event.id` for that ID.
8. To stop event transmission, disable the feed and save. Before revoking access or the
   intake key, agree how to conclude the evaluation and handle any in-flight delivery.

Delivery is asynchronous, bounded and best-effort; it is not a durable delivery queue.
The current queue limit is 256 events. There is no automatic HTTP retry or redirect
following, and TLS certificate verification stays enabled. Failed/uncertain sends require
inspection of diagnostics and receiver evidence before any deliberate resubmission.
Disabling the feed does not erase events already received by Sekoia.

The existing generic HTTP webhook and syslog modes retain their own behavior. Select the
Sekoia mode for this integration. No management API credential or polling adapter is needed.

## Tested HTTPS contract

For the FRA1 lab: POST `https://intake.sekoia.io/jsons`, `Content-Type: application/json`,
`X-SEKOIAIO-INTAKE-KEY: <private intake key>`. The request body is a JSON array whose
elements are serialized JSON event strings. The request must verify TLS and must not
forward the key to redirected destinations. An HTTP 202 acknowledges receipt, not
successful parsing or alert creation. The local Sekoia product mode makes no automatic retries and does not follow redirects.
Similarity grouping is not a transport deduplication guarantee.

## Disclosure

Addresses, subject, explanation, indicators and attachment metadata are controlled
by separate source disclosure flags. Explicit boolean true permits extraction of the
corresponding normalized optional fields. The sender must remove undisclosed values
before transmission: parser gating cannot remove content already in the raw event.
Message and tenant identifiers can remain identifying even with optional flags off.
No email body, MIME or attachment bytes are part of this event contract.

## Event and alert interpretation

Processing completion, a security verdict, an intended action and a recorded mailbox
action result are separate facts. A recorded successful primary quarantine does not
independently verify every mailbox operation. Inspection-incomplete decisions are not
treated as confirmed threats solely because their verdict is phishing.

Observed folder moves are feedback observations. They do not establish a verified
human actor, confirmed ground truth or a replacement verdict. Feedback produces no
alert under this policy. Source IDs remain in `gaetir.event_id`; Sekoia owns `event.id`.
Valid source time is preferred, valid emission time is the fallback, and otherwise
the receiver default applies. Invalid timestamp flags retain the distinction.

## Troubleshooting and validation

Inspect Valid, Warning and Invalid intake tabs after delivery. Undefined custom fields
require matching field definitions; Sekoia-owned event fields must not be overwritten.
Preserve evidence of uncertain submissions and reconcile receipt before retrying.
Do not replay accepted qualification batches merely to check configuration.

The synthetic lab accepted ten valid events and the six expected alerts, with four
negative cases producing no alerts in the observation window. Those results do not
establish product-side end-to-end delivery, load capacity or Sekoia homologation.

## References

- https://docs.sekoia.com/developer/api/
- https://github.com/SEKOIA-IO/intake-formats
