uuid: b0325af0-b2db-40ca-a477-2b260435a565
name: SECUSERVE e-securemail
type: intake

## Overview

e-securemail is the email filtering service of SECUSERVE, a French managed service provider dedicated to email security. It filters the inbound and outbound messages of a protected domain against spam, phishing, malware and content policies, then delivers them. This integration collects the filtering events of a domain from the e-securemail SIEM API.

- **Vendor**: SECUSERVE
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Email gateway, Anti-virus

## How the collection works

The connector pulls the events of one protected domain from the e-securemail SIEM API.

- An event describes one message **for one recipient**: a message sent to three recipients produces three events, sharing the message fields and carrying their own verdict, score and delivery status.
- The API serves an event about two minutes after the message has been filtered, so events reach Sekoia with that delay.
- On its first start, the connector collects the last five minutes. After an interruption, it catches up on the missed period, up to seven days back.

## Configure

### Retrieve the SIEM API key of the domain

1. Log in to the [e-securemail administration console](https://www.security-mail.net).
2. Select the protected domain to collect.
3. In the **Tracking** menu, open **SIEM integration**.
4. In the **Endpoint & authentication** section, copy the **Domain API key**.

!!! note
    The API key is specific to a domain. To collect several domains, create one intake per domain, each with the API key of its domain.

### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `e-securemail` format.
2. Set the module configuration with the `api_host`: the URL of the e-securemail administration console, `https://www.security-mail.net` by default.
3. Set the connector configuration with the `api_key` retrieved in the previous step.

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

## Interpret the events

| e-securemail value | Sekoia field | Meaning |
| --- | --- | --- |
| `stamp_filter` | `@timestamp` | Time the message was filtered. |
| `action` | `event.action`, `event.type` | Action taken on the message: `pass`, `blocked`, `rejected` or `bounced`. `pass` becomes the `allowed` event type, the other actions `denied`. |
| `verdict` | `event.reason`, `secuserve.verdict` | Filtering verdict: `valid`, `spam`, `refused`, `rejected`, `virus`, `tagged`, `oversize`, `content` or `unchecked`. |
| `antispam_score` | `event.risk_score` | Antispam score of the message. |
| `filter_info` | `secuserve.filter.info`, `secuserve.filter.rules` | Antispam rules triggered by the message, with their score. |
| `delivery_status` | `secuserve.delivery.status`, `event.outcome` | Delivery towards the recipient server: `sent` becomes `success`; `bounced`, `rejected` and `disconnected` become `failure`; `deferred` and `quarantine` stay `unknown`. |
| `delivery_info` | `secuserve.delivery.info`, `error.message` | SMTP response of the recipient server, also copied to `error.message` when the delivery failed. |
| `message_id` | `email.local_id`, `email.message_id` | e-securemail identifier of the message. `email.message_id` is set only when it is the `Message-ID` header of the message. |
| `message_parts` | `email.attachments`, `secuserve.qrcode` | Parts of the message, with their name, MIME type, size and SHA-1. `secuserve.qrcode` flags a message holding at least one part that carries a QR code. |

## Event samples and extracted fields

{!_shared_content/operations_center/integrations/generated/b0325af0-b2db-40ca-a477-2b260435a565_sample.md!}

{!_shared_content/operations_center/integrations/generated/b0325af0-b2db-40ca-a477-2b260435a565.md!}
