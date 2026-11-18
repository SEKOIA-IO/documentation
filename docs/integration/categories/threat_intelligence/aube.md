uuid: 491233f5-5491-4690-9344-fdfcf77a29f1
name: AUBE
type: intake

## Overview

AUBE detects the misuse of legitimate accounts on servers. Its analysis engine, AUBE Core, compares each period of a server's audit logs (Linux auditd `execve` records, Windows process events) with the server's own history, and flags the periods whose commands are statistically unusual. Analysts review the flagged periods in AUBE Portal. When an analyst confirms a period as an anomaly, AUBE Portal sends it to Sekoia.io.

- **Vendor**: AUBE Security
- **Supported environment**: On premises (AUBE Portal on Red Hat Enterprise Linux 9)
- **Version compatibility**: AUBE Portal 1.1.0 and later
- **Detection based on**: Alert (anomalies confirmed by an analyst)
- **Supported application or feature**: Linux auditd and Windows process events, analysed by AUBE Core

## Specification

### Prerequisites

- **Licence**:

    - The SIEM support option of the AUBE Portal licence.

- **Permissions**:

    - A superuser account in AUBE Portal
    - The right to create intakes in Sekoia.io

- **Network**:

    - Outbound HTTPS (TCP 443) from the AUBE Portal server to the intake address of your region: `intake.sekoia.io` for FRA1, `intake.<region>.sekoia.io` otherwise. An HTTPS proxy can be used.

### Transport Protocol/Method

- HTTPS push of JSON events, authenticated with the intake key

### Logs details

- **Supported functionalities**:

    - `confirmed_anomaly`: a period an analyst confirmed, with the server, the period, its severity and singularity score, the evaluation, and the most singular commands with the users who ran them
    - `confirmed_anomaly_withdrawn`: the analyst withdrew that confirmation
    - `test`: a test event sent from AUBE Portal

- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Alert

### When AUBE Portal sends an event

| In AUBE Portal, the analyst... | Sent to Sekoia.io |
|---|---|
| sets a period to Confirmed Anomaly | `confirmed_anomaly`, which raises an alert at the period's severity |
| later reopens it and sets it to Ignore, Accepted or Approved | `confirmed_anomaly_withdrawn`, which raises no alert |
| sets a confirmed period to Resolved, or reopens it | nothing: the anomaly was real |

Events wait in a queue in AUBE Portal and are retried while Sekoia.io cannot be reached. Each event links back to the period's evaluation page in AUBE Portal (`event.url`). Evaluation comments are never sent, and AUBE Portal can send each command's name without its arguments.

## Step-by-Step Configuration Procedure

### Create the intake in Sekoia.io

1. Go to the [Intakes page](https://app.sekoia.io/operations/intakes) and click `+ Intake`.
2. Choose `AUBE`.
3. Give the intake a name and select its entity.
4. Copy the intake key.

### Configure AUBE Portal

1. Sign in to AUBE Portal with a superuser account and go to `Settings` > `Integration`.
2. Click the `Sekoia.io` card.
3. Fill in the fields:
    - `Sekoia region`: the region of your tenant, as in its address (`app.sekoia.io` is FRA1)
    - `Intake key`: the key you copied
    - `Portal URL`: the address your analysts use to open AUBE Portal. Each event links back to it, and its identifier includes this host, so keep it stable.
    - `Command lines`: `Full command lines`, or `Executable only` to send each command's name without its arguments
    - `HTTPS proxy (optional)`: leave blank to connect directly
4. Tick `Enable Sekoia.io integration` and click `Save`.
5. Click `Send test event`.

!!! note
    The `Delivery` line of the card shows the events pending and failed, the last delivery and the last error. `Retry failed` sends the failed events again.

### Check the events

1. In Sekoia.io, open the [Events page](https://app.sekoia.io/operations/events) and search for the events of your AUBE intake.
2. The test event appears within a minute, with its smart description.

{!_shared_content/operations_center/integrations/generated/491233f5-5491-4690-9344-fdfcf77a29f1_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_491233f5-5491-4690-9344-fdfcf77a29f1_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/491233f5-5491-4690-9344-fdfcf77a29f1.md!}
