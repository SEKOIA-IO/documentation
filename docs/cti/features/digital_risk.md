# Sekoia Digital Risk

Sekoia Digital Risk monitors your organization's external exposure across clear, deep, and dark web sources, such as leaked credentials, exposed data, and lookalike domains. It brings these exposures into Sekoia so that you can detect, investigate, and respond to them alongside your other security events.

## What the Flare integration does

Sekoia Digital Risk includes the Flare integration. It provides the Flare account settings and the **Fetch new events from Flare** connector, which retrieves events from your Flare tenant feed. The Flare Events intake then normalizes these events into the Elastic Common Schema (ECS) taxonomy that Sekoia uses for detection and investigation, and the detection rules that you activate generate Sekoia alerts from them.

Flare monitors the identifiers that you define, such as domains, names, keywords, and IP addresses. Depending on the configured identifiers and data sources, Flare can report exposures from:

- Chat channels and illicit networks.
- Forums and marketplaces.
- Paste sites and leak repositories.
- Stealer logs and leaked credentials.
- Source-code repositories.
- Lookalike and newly observed domains.
- Public buckets and exposed services.

## Event flow

The integration follows this flow:

1. You create identifiers and policies in Flare.
2. Flare creates events when collected data matches the configured monitoring scope.
3. The Sekoia connector retrieves events from the Flare tenant feed.
4. The Flare Events parser normalizes the events in Sekoia.
5. Sekoia displays the normalized data as events.
6. Activated detection rules evaluate the events and can create Sekoia alerts.
7. Analysts investigate the alert in Sekoia and pivot to the source event in Flare with `event.url`.

## Events and alerts

Flare events and Sekoia alerts are different objects in the workflow.

| Object | Created by | Purpose |
| --- | --- | --- |
| Flare event | Flare | Reports data that matches a monitored identifier and policy. |
| Sekoia event | The Flare Events connector and parser | Stores the normalized Flare event in Sekoia. |
| Sekoia alert | An activated Sekoia detection rule | Signals that a Sekoia event matches detection conditions and requires investigation. |

Collecting Flare events does not activate Sekoia detection rules automatically. You must activate the rules that match your monitoring and response requirements.

## Data available in Sekoia

The parser extracts common event information and Flare-specific context.

| Flare information | Sekoia field | Use |
| --- | --- | --- |
| Flare event identifier | `flare.events.uid` | Correlate the Sekoia event with the source event in Flare. |
| Flare event URL | `event.url` | Open or copy the link to pivot from Sekoia to Flare. |
| Event type | `event.type` and `flare.events.type` | Identify the Flare event subtype. |
| Event title | `event.reason` | Display a short description of the event. |
| Risk score | `event.risk_score` and `event.severity` | Prioritize events and apply detection conditions. |
| Source and source name | `event.provider` and Flare-specific fields | Identify where Flare observed the data. |
| Extracted domains, IP addresses, URLs, emails, and usernames | ECS threat fields and Flare-specific fields | Search, correlate, and create detection conditions. |

The exact fields available depend on the Flare event subtype and the data returned by Flare.

## Event coverage

The integration consumes Flare's unified tenant feed. Supported event subtypes include:

- `chat_message` and `attachment`.
- `forum_post` and `forum_topic`.
- `listing` and `seller`.
- `paste`.
- `leaked_credential` and `stealer_log`.
- `source_code` and `docker_image`.
- `driller_profile`.
- `domain`.
- `blog_post`.
- `bucket` and `bucket_object`.
- `document` from ransomware leak sources.
- `google` monitoring results.
- `service` and `social_media`.
- `experimental` events that Flare adds to the tenant feed.

The [Flare Events integration reference](/integration/categories/threat_intelligence/flare_events.md) contains the current event catalog and raw and normalized event samples.

## Collection model

The Sekoia connector uses a scheduled pull model.

- The connector retrieves pages of events from the Flare tenant feed.
- The initial lookback defines how far into the past the first collection starts.
- Later collections use the feed pagination and checkpoint information to retrieve new events.
- The frequency controls the time between searches for new events.
- The page size controls how many events the connector requests per page.
- The throttle controls the wait time between two event requests.

The recommended connector values are bounded to prevent invalid configurations. You can change them when needed, but larger intervals or smaller page sizes can increase collection time.

For the parameter limits and recommended defaults, see [Step 3: Monitor external exposure](/getting_started/intelligence_step3_monitor_external_exposure.md#review-the-connector-parameters).

## Investigation pivot

When Flare provides a source URL, the parser stores it in `event.url`. The event also contains the Flare event identifier for correlation.

To investigate the source event:

1. Open the Sekoia alert or event.
2. Open the event details.
3. Locate `event.url`.
4. Click the URL or copy it into a browser to open the event in Flare.

## What you configure in each product

| Configuration | Product |
| --- | --- |
| Users and tenant permissions | Flare |
| Identifiers and monitoring scope | Flare |
| Matching, ignored-term, discovery, and duplication policies | Flare |
| API key and optional tenant ID | Flare and Sekoia intake account |
| Event collection parameters | Sekoia intake trigger |
| Detection rules | Sekoia Rules catalog |
| Alert investigation and response | Sekoia and Flare |

## Prerequisites

You need:

- An active Flare tenant.
- A Flare API key that can read tenant events.
- Permission to create and manage an intake in Sekoia.
- Permission to activate detection rules in Sekoia.
- At least one identifier and an appropriate monitoring policy in Flare.

## Related articles

[Step 3: Monitor external exposure](/getting_started/intelligence_step3_monitor_external_exposure.md): How to configure Flare, collect events, activate detections, and investigate a Flare alert.

[Flare Events](/integration/categories/threat_intelligence/flare_events.md): Reference for prerequisites, supported event types, collection details, raw samples, normalized fields, and detection coverage.

[Rules catalog](/xdr/features/detect/rules_catalog.md): How to review and activate built-in detection rules.

[Events](/xdr/features/investigate/events.md): How to review and investigate events collected in Sekoia.
