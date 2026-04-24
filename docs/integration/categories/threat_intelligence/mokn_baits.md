uuid: 1a1502f5-5a93-44b4-b0b5-359bbcb14902
name: MokN - Baits
type: intake

## Overview

- **Vendor**: MokN
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**:
    - Bait attempts
    - Credential exposure context
    - Attempt follow-up actions

MokN helps detect malicious authentication activity by exposing login attempts captured on bait services. This integration polls MokN bait attempts from the MokN API and forwards them to Sekoia.io as normalized events.

The integration also provides response actions so analysts can interact with an attempt directly from automation:

- Add or update the comment attached to an attempt
- Request a credential check for a specific attempt

## Configure

### Prerequisites

To use this integration, you need:

- A MokN tenant URL
- A MokN API token with access to bait attempts
- Access to create an intake and configure automation in Sekoia.io

### Create an API key in MokN

1. In MokN, go to `Settings`
2. Open `API`
3. Click `Create API KEY`
4. Enter a name for the API key
5. Assign a role
6. Copy the API key

### Create your intake

Go to your Sekoia.io [Intakes page](https://app.sekoia.io/operations/intakes), and follow these steps:

1. Click `+ Intake`
2. Choose `MokN - Baits`
3. Give the intake a name and select the relevant Entity
4. Enter the MokN tenant base URL in the `Base Url` field
5. Enter the MokN API token in the `Api Token` field
6. Keep `Verify Ssl` enabled unless your environment requires otherwise

### Configure the polling trigger

Once the module is configured, create and start the trigger `Fetch MokN Login Attempts`.

The trigger supports the following main options:

- `frequency`: Polling interval in seconds
- `page_size`: Number of attempts fetched per request
- `initial_lookback_minutes`: Initial lookback used when no checkpoint exists yet
- `threat_levels`: Threat levels to include in the query
- `pending`: Restrict collection to pending attempts only
- `statuses`: List of MokN status codes to include in the polling query

### Event content

Collected events include the main attempt metadata exposed by MokN, including:

- Attempt identifiers and timestamps
- Username and password submitted to the bait
- Source IP address and geographic context
- HTTP headers and user-agent
- JA4H fingerprint when available
- Attacker reputation and attempt counters
- Credential leak context
- Credential check history

The integration emits MokN bait attempts with the event action `mokn_bait_attempt` and the dataset `mokn.bait_attempt`.

## Response Actions

### Comment Attempt

Use the `Comment Attempt` action to add or update the comment of a specific MokN attempt.

Required parameters:

- `attempt_id`: Identifier of the MokN attempt
- `comment`: Comment to add to the attempt

### Request MokN Credential Check

Use the `Request MokN Credential Check` action to trigger a credential check for a specific MokN attempt.

Required parameters:

- `attempt_id`: Identifier of the MokN attempt

## Use Cases

This integration is useful to:

- Monitor targeted and opportunistic authentication activity observed by MokN
- Enrich investigations with leak context, attacker telemetry, and JA4H fingerprints
