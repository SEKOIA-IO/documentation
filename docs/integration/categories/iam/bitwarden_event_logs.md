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

### Create the intake in Sekoia.io

1. Log in to the Sekoia.io workspace of your [region](/getting_started/regions.md), go to **Intakes** (for FRA1: [intake page](https://app.sekoia.io/operations/intakes)), and create a new intake from the format `Bitwarden Event Logs`.
2. Copy the **intake key** displayed in the intake details.

    ![Intake key in the intake details](/assets/integration/iam/bitwarden_event_logs/intake_key.png){: style="max-width:100%"}

    !!! warning
        The intake key is not the URL of the intake page (`https://app.sekoia.io/intakes/<uuid>`), nor the UUID in that URL.

        - Intake page URL (wrong): `https://app.sekoia.io/intakes/00000000-1111-2222-3333-444444444444`
        - Intake key (right): `ExAmPlEiNtAkEkEy0123456789abcdef`

### Connect Generic HEC in Bitwarden

1. In the Bitwarden **Admin Console**, go to **Integrations** > **Event management**.
2. On the **Generic HEC** card, select **Connect**.
3. Fill in the fields:

    | Bitwarden field | Value |
    |---|---|
    | **HTTP Event Collector URL** | `https://intake.sekoia.io/jsons?intake_key=<YOUR_INTAKE_KEY>` |
    | **HTTP Event Collector Token** | `<YOUR_INTAKE_KEY>` |

    Example with the intake key `ExAmPlEiNtAkEkEy0123456789abcdef`:

    | Bitwarden field | FRA1 | USA1 |
    |---|---|---|
    | **HTTP Event Collector URL** | `https://intake.sekoia.io/jsons?intake_key=ExAmPlEiNtAkEkEy0123456789abcdef` | `https://intake.usa1.sekoia.io/api/v1/intake-http/jsons?intake_key=ExAmPlEiNtAkEkEy0123456789abcdef` |
    | **HTTP Event Collector Token** | `ExAmPlEiNtAkEkEy0123456789abcdef` | `ExAmPlEiNtAkEkEy0123456789abcdef` |

    ![Generic HEC connection filled in for FRA1](/assets/integration/iam/bitwarden_event_logs/generic_hec_connect.png){: style="max-width:100%"}

    !!! warning
        - The intake key must be in the URL. Bitwarden sends the token in an `Authorization: Splunk <token>` header, which Sekoia.io does not read. The token field is mandatory in Bitwarden but not used by Sekoia.io.
        - The `/jsons` path is required. `https://intake.sekoia.io` alone does not work.
        - For regions other than FRA1, use `https://intake.<region>.sekoia.io/api/v1/intake-http/jsons?intake_key=<YOUR_INTAKE_KEY>` (for example, `intake.usa1.sekoia.io`). See [Regions](/getting_started/regions.md).

4. Select **Save**.

For details on the Bitwarden side, see [Bitwarden documentation - Generic HEC Integration](https://bitwarden.com/help/http-event-collector/).

### Validate event ingestion

1. Trigger a test event from Bitwarden (for example, a successful login).
2. In Sekoia.io, open your intake and verify incoming events are received.
3. Confirm normalized fields are populated, including event.code, event.action, user.id, and source.ip.

{!_shared_content/operations_center/integrations/generated/c9aba2bc-245e-4c66-b3fd-9bf1546bb1e8_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_c9aba2bc-245e-4c66-b3fd-9bf1546bb1e8_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/c9aba2bc-245e-4c66-b3fd-9bf1546bb1e8.md!}

## Further readings

- [Bitwarden Help Center - Event Logs](https://bitwarden.com/help/event-logs/)
- [Bitwarden Help Center - HTTP Event Collector](https://bitwarden.com/help/http-event-collector/)
