uuid: c9aba2bc-245e-4c66-b3fd-9bf1546bb1e8
name: Bitwarden Event Logs
type: intake


## Overview

Bitwarden Event Logs provide an audit trail of authentication, vault usage, organization administration, policy changes, and secrets management activity.

- **Vendor**: Bitwarden
- **Supported environment**: SaaS and on-premises
- **Detection based on**: Telemetry
- **Supported application or feature**: Event Logs and Event Management (Generic HEC)

## Configure

### Generic HEC integration setup in Bitwarden

Follow the official Bitwarden guide to configure Event Management forwarding with Generic HEC.

[Bitwarden documentation - HTTP Event Collector](https://bitwarden.com/help/http-event-collector/)

### Create the intake in Sekoia.io

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Bitwarden Event Logs`.
2. Copy the generated Sekoia intake URL and intake key.
3. In Bitwarden Admin Console, open Integrations > Event Management, select Generic HEC, then paste:
   - Endpoint URL: the Sekoia intake URL
   - Token: the Sekoia intake key
4. Save the integration.

### Validate event ingestion

1. Trigger a test event from Bitwarden (for example, a successful login).
2. In Sekoia.io, open your intake and verify incoming events are received.
3. Confirm normalized fields are populated, including event.code, event.action, user.id, and source.ip.

{!_shared_content/operations_center/integrations/generated/c9aba2bc-245e-4c66-b3fd-9bf1546bb1e8.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_c9aba2bc-245e-4c66-b3fd-9bf1546bb1e8_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/c9aba2bc-245e-4c66-b3fd-9bf1546bb1e8.md!}

## Further readings

- [Bitwarden Help Center - Event Logs](https://bitwarden.com/help/event-logs/)
- [Bitwarden Help Center - HTTP Event Collector](https://bitwarden.com/help/http-event-collector/)
